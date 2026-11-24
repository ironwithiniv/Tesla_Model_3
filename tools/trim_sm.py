"""Trim crawled Tesla manual pages to main content, build TOC + search text.
usage: trim_sm.py MANUAL_DIR BASE_URL SEARCH_TXT_OUT
"""
import os, re, sys, html as H
from html.parser import HTMLParser

D, BASE, OUT = sys.argv[1], sys.argv[2].rstrip("/") + "/", sys.argv[3]
HD = os.path.join(D, "html")


class Text(HTMLParser):
    SKIP = {"script", "style", "svg", "button"}
    BLOCK = {"p", "div", "li", "tr", "h1", "h2", "h3", "h4", "h5", "br", "table", "section", "dt", "dd", "article"}

    def __init__(self):
        super().__init__(); self.out = []; self.skip = 0

    def handle_starttag(self, t, a):
        if t in self.SKIP: self.skip += 1
        if t in self.BLOCK: self.out.append("\n")
        if t in ("td", "th"): self.out.append(" | ")
        if t == "li": self.out.append("- ")

    def handle_endtag(self, t):
        if t in self.SKIP and self.skip: self.skip -= 1

    def handle_data(self, d):
        if not self.skip: self.out.append(d)


def to_text(h):
    p = Text(); p.feed(h)
    t = re.sub(r"[ \t\xa0]+", " ", "".join(p.out))
    return re.sub(r"\n\s*\n+", "\n", t).strip()


def main_part(h):
    s = h.find('<main')
    e = h.find('<div class="side-nav', s)
    if s < 0:
        return None
    return h[s:e if e > 0 else len(h)]


# TOC from index side-nav
idx = open(os.path.join(HD, "index.html"), encoding="utf-8", errors="replace").read()
toc_lines = []
nav_s = idx.find('<div class="side-nav')
nav = idx[nav_s: idx.find('<nav class="tds-footer-nav', nav_s)] if nav_s >= 0 else ""
depth = 0
for m in re.finditer(r'<(/?)(ul|ol)\b[^>]*>|<a\b[^>]*href="([^"]+)"[^>]*>(.*?)</a>', nav, re.S):
    if m.group(2):
        depth += -1 if m.group(1) else 1
    elif m.group(3):
        title = H.unescape(re.sub(r"<[^>]+>", "", m.group(4))).strip()
        if title:
            href = m.group(3).lstrip("./")
            toc_lines.append(f"{'  ' * max(depth - 1, 0)}- [{title}](html/{href})")
open(os.path.join(D, "TOC.md"), "w").write(f"# Оглавление\n\nИсточник: {BASE}index.html\n\n" + "\n".join(toc_lines) + "\n")

title_re = re.compile(r"<title>(.*?)</title>", re.S)
rows = []
with open(OUT, "w") as out:
    for fn in sorted(os.listdir(HD)):
        if not fn.endswith(".html"):
            continue
        p = os.path.join(HD, fn)
        h = open(p, encoding="utf-8", errors="replace").read()
        m = title_re.search(h)
        title = H.unescape(m.group(1)).strip() if m else fn
        body = main_part(h)
        if body is None:  # already trimmed
            body = h
        else:
            body = re.sub(r'(src|href)="(?!https?:|#|mailto:)(\./)?([^"]+)"',
                          lambda mm: f'{mm.group(1)}="{BASE}{mm.group(3)}"' if not mm.group(3).startswith("GUID-") else mm.group(0), body)
            page = (f'<!doctype html><meta charset="utf-8"><title>{H.escape(title)}</title>'
                    f'<p><small>Source: <a href="{BASE}{fn}">{BASE}{fn}</a> (downloaded 2026-11-24)</small></p>\n{body}\n')
            open(p, "w").write(page)
        txt = to_text(body)
        rows.append((fn, title))
        out.write(f"\n\n===== {title} | {BASE}{fn} =====\n{txt}\n")
with open(os.path.join(D, "_page_index.tsv"), "w") as f:
    f.write("file\ttitle\turl\n")
    for fn, t in sorted(rows, key=lambda r: r[1].lower()):
        f.write(f"html/{fn}\t{t}\t{BASE}{fn}\n")
for junk in ("_all_text.txt",):
    if os.path.exists(os.path.join(D, junk)):
        os.remove(os.path.join(D, junk))
print(D, len(rows), "toc", len(toc_lines))
