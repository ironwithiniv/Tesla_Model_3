import csv, re, sys, collections

OUT = sys.argv[1]
SRC = [("2017–2023", "Guides/data/torque_2017-2023.csv"), ("2024+ (Highland)", "Guides/data/torque_2024+.csv")]
KEY = [
    ("Колёса", r"lug nut|wheel"),
    ("Передние верхние рычаги (FUCA)", r"upper control arm|fuca"),
    ("Передняя подвеска: нижние рычаги, стабилизатор, амортизатор", r"(front|lh front|rh front).*(lateral link|compliance link|stabar|stabilizer|damper|shock|strut)|lateral link|compliance link"),
    ("Задняя подвеска", r"aft link|fore link|toe link|rear .*damper|rear .*knuckle|upper link|lower link"),
    ("Тормоза", r"caliper|rotor|brake"),
    ("Подрамники", r"subframe.*body|body.*subframe|shear plate"),
    ("Приводные блоки", r"drive unit"),
    ("12V АКБ", r"12v|low voltage battery|lv battery"),
    ("Рулевое", r"steering gear|tie rod"),
]


def tq(s):
    return s.replace("lbs-ft", "lb·ft")


o = ["# Моменты затяжки Tesla Model 3", "",
     "Источник: страницы «Torque Specifications – <узел>» официального Service Manual (service.tesla.com), скачано 2026-11-24. "
     "Таблицы собраны скриптом из HTML без ручного ввода цифр. Ссылка у каждой строки ведёт на страницу-источник.", "",
     "- **2017–2023** = [Service Manual Model 3](../Service-Manual/2017-2023_en-us/) (ваш кузов LR AWD 2021–2023).",
     "- **2024+** = [Service Manual Model 3 2024+](../Service-Manual/2024+_Highland_en-us/) (Highland).",
     "- Полные данные: [data/torque_2017-2023.csv](data/torque_2017-2023.csv) и [data/torque_2024+.csv](data/torque_2024+.csv). "
     "Колонки: узел, процедура, описание, момент, инструмент, повторное использование крепежа, примечания, URL.", "",
     "> ⚠️ Для одного и того же болта Tesla иногда даёт разные моменты в разных процедурах или для разных ревизий деталей "
     "(пример: болт shear plate заднего подрамника 125 и 130 Nm; болт нижнего поперечного рычага 135 Nm для NA, PN 1109912-00-B, и 190 Nm для EMEA/APAC, PN 2123635-00-A). "
     "Перед затяжкой открывайте страницу процедуры и сверяйте номер детали. «Replace» означает, что крепёж одноразовый: болт или гайку менять.", ""]

for label, path in SRC:
    rows = list(csv.DictReader(open(path)))
    o.append(f"## Ключевые узлы: {label}\n")
    for title, rx in KEY:
        sel, seen = [], set()
        for r in rows:
            d = r["description"]
            if re.search(rx, d, re.I) and (d.lower(), r["torque"]) not in seen:
                seen.add((d.lower(), r["torque"])); sel.append(r)
        if not sel:
            continue
        o.append(f"### {title}\n")
        o.append("| Крепёж | Момент | Крепёж: reuse/replace | Источник |\n|---|---|---|---|")
        for r in sel[:40]:
            o.append(f"| {r['description'].replace('|','/')} | {tq(r['torque']).replace('|','/')} | {r['reuse_replace']} | [{r['system']}]({r['source_url']}) |")
        o.append("")

for label, path in SRC:
    rows = list(csv.DictReader(open(path)))
    by = collections.defaultdict(list)
    for r in rows:
        by[r["system"]].append(r)
    o.append(f"## Полная таблица: {label}\n")
    for sysname in sorted(by):
        o.append(f"<details><summary><b>{sysname}</b> ({len(by[sysname])})</summary>\n")
        o.append("| Процедура | Крепёж | Момент | Reuse/Replace |\n|---|---|---|---|")
        for r in by[sysname]:
            o.append(f"| {r['procedure'][:70].replace('|','/')} | {r['description'].replace('|','/')} | {tq(r['torque']).replace('|','/')} | {r['reuse_replace']} |")
        o.append(f"\nИсточник: {by[sysname][0]['source_url']}\n\n</details>\n")
open(OUT, "w").write("\n".join(o) + "\n")
print("ok")
