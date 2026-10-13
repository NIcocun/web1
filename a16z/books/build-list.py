#!/usr/bin/env python3
"""Regenerate books/list/index.html — the plain-HTML, crawlable version of the
3D library — from books/lib.json (the single source of truth).

    python3 books/build-list.py

Run this after any edit to lib.json so the text list stays in sync.
"""
import json, os, html, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
LIB  = os.path.join(HERE, 'lib.json')
OUT  = os.path.join(HERE, 'list', 'index.html')

THEMES = ["Spirit", "Mind", "Stories", "Lives", "Builders", "Everything else"]
BLURB = {
    "Spirit":          "Yoga, meditation, and the books that came out of Rishikesh and Bali.",
    "Mind":            "Psychology, philosophy, and how thinking works.",
    "Stories":         "Fiction, which took over in 2025.",
    "Lives":           "Biographies and memoirs.",
    "Builders":        "Founders, companies, and how things get made.",
    "Everything else": "History, geopolitics, physics, and whatever else I picked up.",
}

def stars(v):
    """Mirror the 3D page: full stars, then a half, then empties."""
    if not v:
        return ""
    full = int(v)
    half = (v - full) >= .45
    return "★" * full + ("½" if half else "") + "☆" * (5 - full - (1 if half else 0))

def esc(s):
    return html.escape(s or "", quote=True)

def book_html(b):
    gr    = "https://www.goodreads.com/book/show/%s" % esc(b["id"])
    when  = b.get("fd") or b.get("w") or ""
    st    = stars(b.get("rr"))
    meta  = []
    if st:
        meta.append('<span class="st" aria-label="%s out of 5">%s</span>' % (b.get("rr"), st))
    if b.get("cur"):
        meta.append('<span class="now">Reading now</span>')
    elif when:
        meta.append('<span class="when">Read %s</span>' % esc(when))
    if b.get("lc"):
        meta.append('<span class="bg">life changer</span>')
    if b.get("fav"):
        meta.append('<span class="bg">favorite</span>')

    rev = ""
    if b.get("rev"):
        paras = "".join("<p>%s</p>" % esc(p) for p in b["rev"].split("\n\n") if p.strip())
        if b.get("sp"):
            rev = "<details><summary>My review (has spoilers)</summary>%s</details>" % paras
        else:
            rev = '<div class="rev">%s</div>' % paras
    elif b.get("cur"):
        rev = '<p class="none">Still reading this one.</p>'

    return (
        '<article class="bk">\n'
        '  <h3>%s</h3>\n'
        '  <p class="by">%s</p>\n'
        '  <p class="meta">%s</p>\n'
        '  %s\n'
        '  <p class="gr"><a href="%s" rel="noopener" target="_blank">On Goodreads ↗</a></p>\n'
        '</article>'
    ) % (esc(b.get("t")), esc(b.get("a")), " · ".join(meta), rev, gr)

def main():
    d     = json.load(open(LIB, encoding="utf-8"))
    books = d["books"]
    stats = d["stats"]

    # Same mutually-exclusive grouping the 3D page uses.
    lc  = [b for b in books if b.get("lc") and not b.get("cur")]
    fav = [b for b in books if b.get("fav") and not b.get("lc") and not b.get("cur")]
    cur = [b for b in books if b.get("cur")]
    special = {id(b) for b in lc + fav}
    by_theme = {t: [] for t in THEMES}
    for b in books:
        if not b.get("cur") and id(b) not in special:
            by_theme[b["th"]].append(b)
    for t in THEMES:
        by_theme[t].sort(key=lambda b: b.get("k") or "")

    groups = [
        ("life-changers", "Life changers", "The ones that actually rearranged something.", lc),
        ("favorites",     "Favorites",     "Not life changers, but I think about them a lot.", fav),
        ("reading-now",   "Reading now",   "In progress as of this page being built.", cur),
    ] + [(t.lower().replace(" ", "-"), t, BLURB[t], by_theme[t]) for t in THEMES]
    groups = [g for g in groups if g[3]]

    total = sum(len(g[3]) for g in groups)
    assert total == len(books), (total, len(books))

    nav = " ".join('<a href="#%s">%s <b>%d</b></a>' % (gid, esc(name), len(bs))
                   for gid, name, _, bs in groups)

    sections = []
    for gid, name, blurb, bs in groups:
        sections.append(
            '<section id="%s">\n<h2>%s <span class="n">%d</span></h2>\n<p class="gb">%s</p>\n%s\n</section>'
            % (gid, esc(name), len(bs), esc(blurb), "\n".join(book_html(b) for b in bs))
        )

    doc = TEMPLATE % {
        "read":  stats["read"],
        "pages": "{:,}".format(stats["pages"]),
        "five":  stats["five"],
        "cur":   len(cur),
        "nav":   nav,
        "body":  "\n\n".join(sections),
        "built": datetime.date.today().strftime("%B %Y"),
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(doc)
    print("wrote %s  (%d books, %.0f KB)" % (OUT, len(books), os.path.getsize(OUT) / 1024))

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Every book I've read &middot; %(read)s books, with reviews</title>
<meta name="description" content="A plain-text list of all %(read)s books Nico Perez Diaz has read since 2023 — %(pages)s pages — with his rating and review for each one.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,400..800&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,600;1,7..72,400&display=swap" rel="stylesheet">
<style>
:root{--paper:#F3EEE4; --ink:#1D2B24; --muted:#5A685F; --saffron:#D9901A; --line:#D8D0C0; --card:#FBF8F1; box-sizing:border-box}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--paper:#171E1A; --ink:#E9ECE3; --muted:#A3AFA6; --saffron:#EBA83A; --line:#2D3A33; --card:#1D2622}}
:root[data-theme="dark"]{--paper:#171E1A; --ink:#E9ECE3; --muted:#A3AFA6; --saffron:#EBA83A; --line:#2D3A33; --card:#1D2622}
*,*::before,*::after{box-sizing:inherit}
body{margin:0; background:var(--paper); color:var(--ink); font-family:"Literata",Georgia,"Times New Roman",serif; font-size:1.02rem; line-height:1.6; -webkit-font-smoothing:antialiased}
.f,h1,h2,h3,nav,.meta,.n,.gb,.gr{font-family:"Bricolage Grotesque",system-ui,sans-serif}
a{color:inherit; text-decoration-color:var(--saffron); text-decoration-thickness:2px; text-underline-offset:.2em}
a:hover{color:var(--saffron)}
:focus-visible{outline:3px solid var(--saffron); outline-offset:3px}
main{max-width:44rem; margin:0 auto; padding:clamp(1.75rem,5vw,3.5rem) 1.25rem 5rem}
.top a{font-weight:600; font-size:.9rem; text-decoration:none; border:1px solid var(--line); border-radius:999px; padding:.4rem .9rem; display:inline-block; margin:0 .4rem .5rem 0; font-family:"Bricolage Grotesque",system-ui,sans-serif}
h1{font-size:clamp(1.9rem,6vw,2.6rem); line-height:1.1; margin:1.5rem 0 .5rem; font-weight:800}
.lede{color:var(--muted); margin:0 0 1.5rem}
.sts{display:flex; flex-wrap:wrap; gap:1.5rem; padding:1rem 0 1.25rem; border-top:1px solid var(--line); border-bottom:1px solid var(--line); margin-bottom:1.5rem}
.sts div{min-width:5rem}
.sts b{display:block; font-family:"Bricolage Grotesque",system-ui,sans-serif; font-size:1.5rem; font-weight:800; line-height:1}
.sts span{font-size:.82rem; color:var(--muted)}
nav{margin:0 0 2.5rem; font-size:.88rem; line-height:2.1}
nav a{text-decoration:none; border:1px solid var(--line); border-radius:999px; padding:.3rem .75rem; margin:0 .3rem .3rem 0; display:inline-block}
nav a b{color:var(--saffron)}
section{margin:0 0 3.5rem}
h2{font-size:1.45rem; font-weight:800; margin:0 0 .2rem; padding-top:.5rem; border-top:3px solid var(--ink)}
h2 .n{color:var(--muted); font-weight:600; font-size:1rem}
.gb{color:var(--muted); font-size:.9rem; margin:0 0 1.5rem}
.bk{border-top:1px solid var(--line); padding:1.15rem 0 .25rem}
.bk h3{font-size:1.06rem; font-weight:700; margin:0 0 .15rem; line-height:1.3}
.by{margin:0 0 .4rem; color:var(--muted); font-size:.94rem; font-style:italic}
.meta{margin:0 0 .6rem; font-size:.82rem; color:var(--muted); display:flex; flex-wrap:wrap; gap:.6rem; align-items:baseline}
.st{color:var(--saffron); letter-spacing:.04em; font-size:.95rem}
.now{background:var(--saffron); color:#1D2B24; border-radius:999px; padding:.1rem .55rem; font-weight:700; font-size:.76rem}
.bg{border:1px solid var(--saffron); color:var(--saffron); border-radius:999px; padding:.1rem .55rem; font-weight:600; font-size:.76rem}
.rev p,details p{margin:0 0 .7rem}
.rev,details{background:var(--card); border-left:3px solid var(--saffron); border-radius:0 6px 6px 0; padding:.8rem 1rem .2rem; margin:0 0 .6rem}
details{padding:.8rem 1rem}
details summary{cursor:pointer; font-family:"Bricolage Grotesque",system-ui,sans-serif; font-weight:600; font-size:.88rem; color:var(--saffron)}
details[open] summary{margin-bottom:.7rem}
.none{color:var(--muted); font-style:italic; margin:0 0 .6rem}
.gr{margin:0 0 .3rem; font-size:.8rem}
.gr a{color:var(--muted); text-decoration:none}
.gr a:hover{color:var(--saffron)}
footer{border-top:1px solid var(--line); padding-top:1.25rem; color:var(--muted); font-size:.88rem}
.up{position:fixed; right:1rem; bottom:1rem; background:var(--ink); color:var(--paper); border-radius:999px; padding:.55rem 1rem; font-family:"Bricolage Grotesque",system-ui,sans-serif; font-size:.82rem; font-weight:600; text-decoration:none}
@media print{.up,nav,.top{display:none}body{font-size:10pt}}
</style>
</head>
<body>
<main>
  <p class="top"><a href="/a16z/">&larr; Nico</a> <a href="/a16z/books/">The Train (3D)</a> <a href="/a16z/books/shala/">The Shala (3D)</a></p>

  <h1>Every book I've read</h1>
  <p class="lede">All %(read)s of them, with my rating and what I thought. This is the plain version of
  my <a href="/a16z/books/">3D library</a> &mdash; same books, no WebGL required.</p>

  <div class="sts">
    <div><b>%(read)s</b><span>books read</span></div>
    <div><b>%(pages)s</b><span>pages</span></div>
    <div><b>%(five)s</b><span>five stars</span></div>
    <div><b>%(cur)s</b><span>reading now</span></div>
  </div>

  <nav aria-label="Jump to a section">%(nav)s</nav>

%(body)s

  <footer>
    <p>Ratings are mine, at half-star precision. Reviews are copied straight from my Goodreads,
    typos and all. Last built %(built)s.</p>
    <p><a href="/a16z/books/">Walk through the 3D library &rarr;</a></p>
  </footer>
</main>
<a class="up" href="#">&uarr; Top</a>
</body>
</html>
"""

if __name__ == "__main__":
    main()
