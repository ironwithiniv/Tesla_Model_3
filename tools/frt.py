"""Extract Tesla Flat Rate Times (correction code + hours) from Search-Text manual dumps.
usage: python3 tools/frt.py Search-Text/ServiceManual_2017-2023.txt OUT.csv
"""
import csv, re, sys

src, out = sys.argv[1], sys.argv[2]
text = open(src, encoding="utf-8").read()
pages = re.split(r"\n\n===== ", text)
rows = []
for p in pages:
    m = re.match(r"(?:===== )?(.*?) \| (https://\S+) =====\n", p)
    if not m:
        continue
    title, url = m.group(1).strip(), m.group(2)
    head = p[:1500]
    c = re.search(r"Correction [Cc]ode\s*\n\s*(\d{8})\s*\n\s*(\d+\.\d+)", head)
    if not c:
        continue
    rows.append([title, c.group(1), float(c.group(2)), url])
rows.sort(key=lambda r: r[0].lower())
with open(out, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["procedure", "correction_code", "frt_hours", "source_url"])
    w.writerows(rows)
print(out, len(rows))
