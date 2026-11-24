import json, os, sys, re, csv, collections, html

ROOT = sys.argv[1]
RAW = os.path.join(ROOT, "raw")
YEARS = [2021, 2022, 2023, 2024]

rec, inv, mc = {}, {}, {}
for y in YEARS:
    d = json.load(open(os.path.join(RAW, f"safety_{y}.json")))
    for r in d["results"]:
        if "AWD" not in r["series"]:
            continue
        s = r["safetyIssues"]
        for it in s.get("recalls", []):
            rec.setdefault(it["nhtsaCampaignNumber"], [it, set()])[1].add(y)
        for it in s.get("investigations", []):
            inv.setdefault(it["nhtsaActionNumber"], [it, set()])[1].add(y)
        for it in s.get("manufacturerCommunications", []):
            mc.setdefault(str(it["nhtsaIdNumber"]), [it, set()])[1].add(y)


def yrs(s):
    return ", ".join(str(x) for x in sorted(s))


def clean(t, n=None):
    t = re.sub(r"<[^>]+>", " ", t or "")
    t = html.unescape(re.sub(r"\s+", " ", t)).strip()
    return t if n is None or len(t) <= n else t[: n - 1] + "…"


def md(t):
    return t.replace("|", "/")


# ---- CSVs
with open(os.path.join(ROOT, "recalls.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["nhtsa_campaign", "tesla_number", "date", "model_years", "ota", "units", "subject", "summary", "remedy"])
    for k, (it, ys) in sorted(rec.items(), key=lambda x: x[1][0]["reportReceivedDate"], reverse=True):
        w.writerow([k, it.get("mfrCampaignNumber"), it["reportReceivedDate"][:10], yrs(ys), it.get("overTheAirUpdate"),
                    it.get("potentialNumberOfUnitsAffected"), it.get("subject"), clean(it.get("summary")), clean(it.get("correctiveAction"))])
with open(os.path.join(ROOT, "tsb_manufacturer_communications.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["nhtsa_id", "tesla_number", "date", "model_years", "components", "summary", "pdf"])
    for k, (it, ys) in sorted(mc.items(), key=lambda x: x[1][0]["communicationDate"], reverse=True):
        w.writerow([k, it.get("manufacturerCommunicationNumber"), it["communicationDate"][:10], yrs(ys),
                    "; ".join(c["name"] for c in it.get("components", [])), clean(it.get("summary")),
                    f"TSB/{k}/"])
with open(os.path.join(ROOT, "investigations.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["action_number", "opened", "closed", "status", "model_years", "subject", "summary"])
    for k, (it, ys) in sorted(inv.items(), key=lambda x: x[1][0].get("openDate") or "", reverse=True):
        w.writerow([k, (it.get("openDate") or "")[:10], (it.get("closeDate") or "")[:10], it.get("status"), yrs(ys),
                    it.get("subject"), clean(it.get("summary"))])

# ---- complaints by component
comp = collections.Counter(); comp_y = collections.defaultdict(collections.Counter)
crash = fire = inj = 0
for y in YEARS:
    d = json.load(open(os.path.join(RAW, f"complaints_{y}.json")))
    for c in d["results"]:
        for part in (c.get("components") or "").split(","):
            p = part.strip()
            if p:
                comp[p] += 1; comp_y[p][y] += 1
        crash += bool(c.get("crash")); fire += bool(c.get("fire")); inj += c.get("numberOfInjuries") or 0
ncomp = {y: len(json.load(open(os.path.join(RAW, f"complaints_{y}.json")))["results"]) for y in YEARS}

# ---- README
o = []
o.append("# NHTSA: Tesla Model 3, 2021–2024 (AWD)\n")
o.append("Источник: api.nhtsa.gov, выгрузка **2026-11-24**. Данные NHTSA одинаковы для RWD и AWD одного года (общий список по модели).\n")
o.append("| Файл / папка | Что внутри |\n|---|---|")
o.append("| `raw/recalls_YYYY.json` | `recalls/recallsByVehicle` (публичный API) |")
o.append("| `raw/complaints_YYYY.json` | `complaints/complaintsByVehicle`, все жалобы владельцев |")
o.append("| `raw/safety_YYYY.json` | `vehicles/byYmmt` (API сайта nhtsa.gov): отзывы + расследования + manufacturer communications (TSB) |")
o.append("| [recalls.csv](recalls.csv) | Сводка отзывов |")
o.append("| [tsb_manufacturer_communications.csv](tsb_manufacturer_communications.csv) | Сводка TSB / Manufacturer Communications |")
o.append("| [investigations.csv](investigations.csv) | Расследования ODI (PE/EA/RQ/DP) |")
o.append("| `Recalls/<кампания>/`, `TSB/<nhtsaId>/`, `Investigations/<номер>/` | PDF-документы с static.nhtsa.gov |")
o.append("| `*_index.json` | Индекс документов по каждой записи (со ссылками и на нескачанные файлы) |\n")
o.append("По расследованиям скачаны только ключевые документы: `INOA` (резюме открытия), `INCLA` (резюме закрытия), `INRL` (связанный отзыв). Переписка ODI с Tesla не скачана, ссылки в `Investigations_index.json`. Файлы больше 20 МБ тоже не скачаны.\n")
o.append("## Количество записей\n")
o.append("| Модельный год | Жалобы | Отзывы | Расследования | TSB (MC) |\n|---|---|---|---|---|")
for y in YEARS:
    d = json.load(open(os.path.join(RAW, f"safety_{y}.json")))["results"][0]["safetyIssues"]
    o.append(f"| {y} | {ncomp[y]} | {len(d['recalls'])} | {len(d['investigations'])} | {len(d['manufacturerCommunications'])} |")
o.append(f"\nУникальных записей за 2021–2024: отзывов **{len(rec)}**, расследований **{len(inv)}**, TSB **{len(mc)}**. "
         f"В жалобах: с ДТП {crash}, с пожаром {fire}, пострадавших {inj}.\n")

o.append("## Отзывы (recalls)\n")
o.append("| Кампания NHTSA | № Tesla | Дата | Годы | OTA | Суть |\n|---|---|---|---|---|---|")
for k, (it, ys) in sorted(rec.items(), key=lambda x: x[1][0]["reportReceivedDate"], reverse=True):
    o.append(f"| [{k}](https://www.nhtsa.gov/recalls?nhtsaId={k}) | {it.get('mfrCampaignNumber') or ''} | {it['reportReceivedDate'][:10]} | {yrs(ys)} | "
             f"{'да' if it.get('overTheAirUpdate') else 'нет'} | {md(clean(it.get('subject')))} |")

o.append("\n## Расследования ODI\n")
o.append("| Номер | Открыто | Закрыто | Годы | Тема |\n|---|---|---|---|---|")
for k, (it, ys) in sorted(inv.items(), key=lambda x: x[1][0].get("openDate") or "", reverse=True):
    o.append(f"| {k} | {(it.get('openDate') or '')[:10]} | {(it.get('closeDate') or '')[:10] or 'открыто'} | {yrs(ys)} | {md(clean(it.get('subject')))} |")

OM = lambda it: (it.get("summary") or "").startswith("Tesla does not provide physical owner")
om = [k for k, (it, ys) in mc.items() if OM(it)]
o.append("\n## TSB / Manufacturer Communications\n")
o.append(f"Полный текст аннотаций в CSV, PDF в `TSB/<nhtsaId>/`. **{len(om)} из {len(mc)}** записей — это не бюллетени, а выгрузки Owner's Manual под каждую версию ПО "
         "(PDF по ~46 МБ на 1500+ страниц, все модели сразу). Их PDF не скачаны, ссылки есть в `TSB_index.json`. В таблице ниже только технические бюллетени.\n")
o.append("| nhtsaId | № Tesla | Дата | Годы | Узел | Кратко |\n|---|---|---|---|---|---|")
for k, (it, ys) in sorted(mc.items(), key=lambda x: x[1][0]["communicationDate"], reverse=True):
    if OM(it):
        continue
    o.append(f"| [{k}](TSB/{k}/) | {it.get('manufacturerCommunicationNumber') or ''} | {it['communicationDate'][:10]} | {yrs(ys)} | "
             f"{md('; '.join(c['name'] for c in it.get('components', [])))} | {md(clean(it.get('summary'), 160))} |")

o.append("\n## Жалобы по узлам (топ-30)\n")
o.append("| Узел (NHTSA) | Всего | " + " | ".join(str(y) for y in YEARS) + " |\n|---|---|" + "---|" * len(YEARS))
for p, n in comp.most_common(30):
    o.append(f"| {md(p)} | {n} | " + " | ".join(str(comp_y[p][y]) for y in YEARS) + " |")
open(os.path.join(ROOT, "README.md"), "w").write("\n".join(o) + "\n")
print(len(rec), len(inv), len(mc))
