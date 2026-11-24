"""Parse 'Torque Specifications - *' pages from Tesla SM html into CSV.
usage: torque.py MANUAL_DIR OUT_CSV
"""
import csv, os, re, sys, html as H
from html.parser import HTMLParser

D, OUT = sys.argv[1], sys.argv[2]


class T(HTMLParser):
    def __init__(self):
        super().__init__(); self.tables = []; self.cur = None; self.row = None; self.cell = None; self.cap = None

    def handle_starttag(self, t, a):
        if t == "table": self.cur = {"caption": "", "rows": []}
        elif t == "caption" and self.cur is not None: self.cap = []
        elif t == "tr" and self.cur is not None: self.row = []
        elif t in ("td", "th") and self.row is not None: self.cell = []
        elif t == "br" and self.cell is not None: self.cell.append(" ")

    def handle_endtag(self, t):
        if t == "caption" and self.cap is not None:
            self.cur["caption"] = norm("".join(self.cap)); self.cap = None
        elif t in ("td", "th") and self.cell is not None:
            self.row.append(norm("".join(self.cell))); self.cell = None
        elif t == "tr" and self.row is not None:
            self.cur["rows"].append(self.row); self.row = None
        elif t == "table" and self.cur is not None:
            self.tables.append(self.cur); self.cur = None

    def handle_data(self, d):
        if self.cap is not None: self.cap.append(d)
        if self.cell is not None: self.cell.append(d)


def norm(s):
    return re.sub(r"\s+", " ", H.unescape(s)).strip()


rows = []
idx = [l.rstrip("\n").split("\t") for l in open(os.path.join(D, "_page_index.tsv"))][1:]
for fn, title, url in idx:
    if not title.startswith("Torque Specifications"):
        continue
    system = title.replace("Torque Specifications - ", "").strip()
    p = T(); p.feed(open(os.path.join(D, fn), encoding="utf-8", errors="replace").read())
    seen = set()
    for tb in p.tables:
        proc = re.sub(r"^Table \d+\.\s*Torque Specifications:\s*", "", tb["caption"]).strip()
        for r in tb["rows"]:
            if len(r) < 2 or r[0].lower() == "description":
                continue
            desc, torque = r[0], r[1]
            if not re.search(r"\d\s*Nm", torque):
                continue
            key = (desc.lower(), torque)
            if key in seen:
                continue
            seen.add(key)
            rows.append([system, proc, desc, torque, r[2] if len(r) > 2 else "", r[3] if len(r) > 3 else "",
                         r[4] if len(r) > 4 else "", url])
with open(OUT, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["system", "procedure", "description", "torque", "tools", "reuse_replace", "notes", "source_url"])
    w.writerows(rows)
print(OUT, len(rows))
