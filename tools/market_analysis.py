"""Build Market CSVs and stats from raw scrapes.
usage: python3 tools/market_analysis.py   (run from repo root)
"""
import csv, statistics as S

USD_GEL = 2.5922  # NBG official rate, published for 2026-11-25
CUSTOMS_GEL = 480

def q(a, p):
    a = sorted(a)
    if not a:
        return None
    i = (len(a) - 1) * p
    lo, hi = int(i), min(int(i) + 1, len(a) - 1)
    return round(a[lo] + (a[hi] - a[lo]) * (i - lo))

def st(a):
    return {"n": len(a), "p25": q(a, .25), "med": q(a, .5), "p75": q(a, .75)}

def norm_d(d):
    d = d.lower()
    if "front" in d and "rear" in d: return "front+rear"
    if "front" in d: return "front"
    if "rear" in d: return "rear"
    if any(x in d for x in ("side", "left", "right")): return "side"
    if "under" in d: return "undercarriage"
    if any(x in d for x in ("minor", "dent", "scratch")): return "minor dent/scratch"
    if any(x in d for x in ("mechan", "electric")): return "mechanical/electrical"
    if any(x in d for x in ("water", "flood")): return "water/flood"
    if "hail" in d: return "hail"
    if "strip" in d: return "stripped"
    return d or "?"

def doc_g(d):
    u = d.upper()
    if u in ("CT", "CLEAR", "ORIGINAL", "BILL OF SALE"): return "clean / bill of sale"
    if "DESTRUCTION" in u or u in ("CD", "NON-REPAIRABLE"): return "non-repairable / CD"
    if u in ("RB", "REBUILDABLE"): return "rebuildable"
    return "salvage (SC/SV/ST/BS/Salvage/MV-907A…)"

rows = []
for part in ("Market/raw/bidcars_lr_part1.txt", "Market/raw/bidcars_lr_part2.txt"):
    for l in open(part):
        f = l.rstrip("\n").split("|")
        if len(f) < 17:
            continue
        date, year, vin, lot, auc, odo, seller, doc, state, loc, dmg, loss, start, price, bn, keys, sold_before = f[:17]
        odo_i = int(odo) if odo.isdigit() else None
        odo_ok = odo_i is not None and 500 < odo_i < 900000
        tag = f"{year}-Tesla-{'MODEL-3' if auc == 'Copart' else 'Model-3'}-{vin}"
        rows.append(dict(sale_date=date, year=year, vin=vin, auction=auc, lot=lot,
                         odometer_mi=odo_i if odo_ok else "", odometer_km=round(odo_i * 1.609344) if odo_ok else "",
                         odometer_note="" if odo_ok else ("not actual / exempt" if odo_i else "missing"),
                         seller=seller, sale_doc=doc, doc_state=state, doc_group=doc_g(doc), location=loc,
                         primary_damage=dmg, damage_group=norm_d(dmg), loss_type=loss, run_drive=start or "no info",
                         keys=keys, final_bid_usd=int(price), buy_now_usd=int(bn) if bn.isdigit() and bn != "0" else "",
                         airbags="n/a (not in source)", source="bid.cars archive",
                         url=f"https://bid.cars/en/lot/{lot}/{tag}?archived=true"))
rows.sort(key=lambda r: (r["sale_date"], r["final_bid_usd"]), reverse=True)
with open("Market/Copart_IAAI_LR_AWD_2021-2023_sales_2026-11.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)

P = [r["final_bid_usd"] for r in rows]
def grp(key, rs=rows):
    g = {}
    for r in rs:
        g.setdefault(key(r), []).append(r["final_bid_usd"])
    return sorted(((k, st(v)) for k, v in g.items()), key=lambda x: -x[1]["n"])

def band(r):
    m = r["odometer_mi"]
    if m == "": return "unknown"
    return "<25k mi" if m < 25000 else "25–50k" if m < 50000 else "50–75k" if m < 75000 else "75–100k" if m < 100000 else "100k+"

out = {"all": st(P), "year": grp(lambda r: r["year"]), "damage": grp(lambda r: r["damage_group"]),
       "run": grp(lambda r: r["run_drive"]), "doc": grp(lambda r: r["doc_group"]), "miles": grp(band),
       "auction": grp(lambda r: r["auction"]), "keys": grp(lambda r: r["keys"]),
       "rd_front_side_rear_2022": grp(lambda r: r["damage_group"], [r for r in rows if r["year"] == "2022" and r["run_drive"] == "Run / Drive"])}

# --- Georgia listings
ge = []
for l in open("Market/raw/myauto_2026-11-24.txt"):
    i, y, km, price, cur, drive, batt, loc, cust = l.rstrip("\n").split("|")
    in_ge = loc not in ("usa", "on-way-to-georgia", "")
    ge.append(dict(listing_id=i, year=y, mileage_km=km, price_gel=price, price_usd=round(int(price) / USD_GEL) if price else "",
                   drive=drive, location=loc or "?", in_georgia=in_ge, customs_flag=cust,
                   battery_or_range_field=batt, url=f"https://www.myauto.ge/en/pr/{i}/", scraped="2026-11-24"))
with open("Market/myauto_Model3_2021-2023_2026-11-24.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(ge[0].keys()))
    w.writeheader(); w.writerows(ge)
ge_awd = [g for g in ge if g["in_georgia"] and g["drive"] == "4x4" and g["price_usd"] != ""]
ge_way = [g for g in ge if g["location"] in ("on-way-to-georgia", "poti") and g["drive"] == "4x4" and g["price_usd"] != ""]
out["ge_awd_in_georgia_usd"] = st([g["price_usd"] for g in ge_awd])
out["ge_awd_in_georgia_by_year"] = [(y, st([g["price_usd"] for g in ge_awd if g["year"] == y])) for y in ("2021", "2022", "2023")]
out["ge_awd_on_way_usd"] = st([g["price_usd"] for g in ge_way])
out["ge_awd_in_georgia_list"] = [(g["year"], g["mileage_km"], g["price_gel"], g["price_usd"], g["location"], g["customs_flag"]) for g in ge_awd]
for k, v in out.items():
    print(k, v)
