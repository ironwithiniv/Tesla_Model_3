import json, os, sys, time, urllib.request, urllib.parse
from concurrent.futures import ThreadPoolExecutor

ROOT = sys.argv[1]  # .../NHTSA
RAW = os.path.join(ROOT, "raw")
YEARS = [2021, 2022, 2023, 2024]
UA = {"User-Agent": "Mozilla/5.0"}


def get(url, tries=6, binary=False):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=120) as r:
                b = r.read()
            if binary:
                return b
            d = json.loads(b)
            if "results" in d:
                return d
        except Exception as e:
            err = e
        time.sleep(3 + i * 3)
    print("FAIL", url, file=sys.stderr)
    return None


items = {"recalls": {}, "investigations": {}, "manufacturerCommunications": {}}
key = {"recalls": "nhtsaCampaignNumber", "investigations": "nhtsaActionNumber",
       "manufacturerCommunications": "nhtsaIdNumber"}
for y in YEARS:
    d = json.load(open(os.path.join(RAW, f"safety_{y}.json")))
    for r in d["results"]:
        if "AWD" not in r["series"]:
            continue
        for t in items:
            for it in r["safetyIssues"].get(t, []):
                k = str(it[key[t]])
                e = items[t].setdefault(k, {"item": it, "years": set()})
                e["years"].add(y)


def docs_for(t, k):
    nid = k
    u = ("https://api.nhtsa.gov/safetyIssues/byNhtsaId?nhtsaId=" + urllib.parse.quote(nid)
         + "&filter=issueType&filterValue=" + t + "&max=100")
    d = get(u)
    if not d or not d["results"]:
        return []
    lst = d["results"][0].get(t) or []
    out = []
    for it in lst:
        ad = it.get("associatedDocuments")
        if isinstance(ad, list):
            out += ad
    return out


folder = {"recalls": "Recalls", "investigations": "Investigations", "manufacturerCommunications": "TSB"}


def work(args):
    t, k = args
    docs = docs_for(t, k)
    items[t][k]["docs"] = docs
    d = os.path.join(ROOT, folder[t], k)
    os.makedirs(d, exist_ok=True)
    if t == "manufacturerCommunications" and (items[t][k]["item"].get("summary") or "").startswith("Tesla does not provide physical owner"):
        os.rmdir(d) if not os.listdir(d) else None
        return t, k, len(docs)
    for doc in docs:
        url = doc.get("url")
        if not url:
            continue
        base = os.path.basename(url)
        if t == "investigations" and not base.startswith(("INOA-", "INCLA-", "INRL-")):
            continue
        if (doc.get("fileSize") or 0) > 20000:  # KB; big files: keep URL in index only
            continue
        fn = os.path.join(d, os.path.basename(url))
        if os.path.exists(fn) and os.path.getsize(fn) > 0:
            continue
        b = get(url, binary=True)
        if b:
            open(fn, "wb").write(b)
    return t, k, len(docs)


jobs = [(t, k) for t in items for k in items[t]]
print("jobs", len(jobs), {t: len(v) for t, v in items.items()})
with ThreadPoolExecutor(6) as ex:
    for t, k, n in ex.map(work, jobs):
        print(t, k, n, flush=True)

for t in items:
    out = []
    for k, e in items[t].items():
        it = dict(e["item"])
        it["modelYears"] = sorted(e["years"])
        it["documents"] = e.get("docs", [])
        out.append(it)
    json.dump(out, open(os.path.join(ROOT, f"{folder[t]}_index.json"), "w"), ensure_ascii=False, indent=1)
print("done")
