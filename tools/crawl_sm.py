"""Crawl a service.tesla.com manual (flat GUID-*.html pages) into a folder.
usage: crawl_sm.py BASE_URL OUT_DIR
"""
import os, re, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser

BASE, OUT = sys.argv[1].rstrip("/") + "/", sys.argv[2]
os.makedirs(os.path.join(OUT, "html"), exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0"}
LINK = re.compile(r'href="((?:\./)?(GUID-[0-9A-F-]+|[A-Za-z0-9_-]+)\.html)')


def get(url):
    for i in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
        except Exception:
            pass
        time.sleep(2 + 2 * i)
    return None


class Text(HTMLParser):
    SKIP = {"script", "style", "nav", "header", "footer", "svg"}
    BLOCK = {"p", "div", "li", "tr", "h1", "h2", "h3", "h4", "h5", "br", "table", "section", "dt", "dd"}

    def __init__(self):
        super().__init__(); self.out = []; self.skip = 0

    def handle_starttag(self, t, a):
        if t in self.SKIP: self.skip += 1
        if t in self.BLOCK: self.out.append("\n")
        if t in ("td", "th"): self.out.append(" | ")

    def handle_endtag(self, t):
        if t in self.SKIP and self.skip: self.skip -= 1

    def handle_data(self, d):
        if not self.skip: self.out.append(d)


def to_text(html):
    p = Text(); p.feed(html.decode("utf-8", "replace"))
    t = "".join(p.out)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    return re.sub(r"\n\s*\n+", "\n", t).strip()


seen, queue = set(), ["index"]
title_re = re.compile(rb"<title>(.*?)</title>", re.S)
titles = {}


def fetch(name):
    fn = os.path.join(OUT, "html", name + ".html")
    if os.path.exists(fn):
        b = open(fn, "rb").read()
    else:
        b = get(BASE + name + ".html")
        if b is None:
            return name, None
        open(fn, "wb").write(b)
    return name, b


with ThreadPoolExecutor(8) as ex:
    while queue:
        batch = [q for q in queue if q not in seen]
        seen.update(batch); queue = []
        for name, b in ex.map(fetch, batch):
            if b is None:
                continue
            m = title_re.search(b)
            titles[name] = m.group(1).decode("utf-8", "replace").strip() if m else name
            for _, n in LINK.findall(b.decode("utf-8", "replace")):
                if n not in seen:
                    queue.append(n)
        print("fetched", len(seen), flush=True)

# text dump: one combined file + index
with open(os.path.join(OUT, "_all_text.txt"), "w") as all_f, open(os.path.join(OUT, "_page_index.tsv"), "w") as idx:
    idx.write("file\ttitle\turl\n")
    for name in sorted(titles, key=lambda n: titles[n].lower()):
        b = open(os.path.join(OUT, "html", name + ".html"), "rb").read()
        idx.write(f"{name}.html\t{titles[name]}\t{BASE}{name}.html\n")
        all_f.write(f"\n\n===== {titles[name]} | {BASE}{name}.html =====\n")
        all_f.write(to_text(b))
print("pages", len(titles))
