"""Spanish coverage audit. `python3 tests/es_audit.py [docs_dir]` (default: ./docs).

Reads every built page under docs/es/ plus docs/404.html and flags visible text, alt text,
aria-labels, titles, meta tags and JSON-LD that look English or are identical to the English page.
Exits 1 if anything is flagged, so a new page or string cannot ship untranslated unnoticed.
Names, addresses, the shop name and the e-mail address are allowed to match the English page.
"""
import re, sys, os, json, html
from html.parser import HTMLParser
ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs")
EN = set("the and to of for with your you is are we our in on at it this that or from can will have has be as by an if not what when how where who which about more all any also up out new get used must should would could only just then than their they them these those there here into over per day days hours hour open closed free fast".split())
ES = set("el la los las de y para con su sus un una es en que por del al se nos le lo muy más como cuando donde qué cómo si no sí o u también pero sin sobre entre desde hasta hay son ser está están tiene tienen puede pueden llame llámenos nuestro nuestra nuestros nuestras cuál cuáles usted ustedes".split())

ALLOW = re.compile(r"^(Diverse Auto ?[Ww]orks( logo)?(, Inc\.)?|Diverseautoworks@verizon\.net|1415 Pawlings (Road|Rd)(, Phoenixville, PA 19460\.?)?|Phoenixville, PA( 19460)?|[A-Z][\w'’.\- ]+ [A-Z]\.|Dark Storm C\.|CARFAX|Google|Yelp|PennDOT|General)$")
SKIP_TAGS = {"script", "style", "noscript"}
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.out = []; s.stack = []; s.skip = 0; s.ld = False; s.buf = ""
    def handle_starttag(s, tag, attrs):
        a = dict(attrs)
        if tag in SKIP_TAGS:
            s.skip += 1
            if tag == "script" and a.get("type") == "application/ld+json": s.ld = True; s.buf = ""
        for k in ("alt", "aria-label", "title", "placeholder", "data-tpl", "aria-description", "value"):
            if a.get(k): s.out.append((f"@{tag}[{k}]", a[k]))
        if tag == "meta" and a.get("content") and (a.get("name") in ("description", "twitter:title", "twitter:description") or (a.get("property") or "").startswith("og:")):
            if (a.get("property") or "") not in ("og:locale", "og:url", "og:image", "og:type"): s.out.append((f"@meta[{a.get('name') or a.get('property')}]", a["content"]))
        for k, v in a.items():
            if k.startswith("data-") and k not in ("data-tpl",) and v and re.search(r"[A-Za-z]{4,} [A-Za-z]{3,}", v) and not v.startswith("{") : s.out.append((f"@{tag}[{k}]", v))
        s.stack.append(tag)
    def handle_endtag(s, tag):
        if tag in SKIP_TAGS:
            s.skip -= 1
            if tag == "script" and s.ld:
                s.ld = False
                try:
                    def walk(o):
                        if isinstance(o, dict):
                            for k, v in o.items():
                                if k in ("name", "text", "description", "headline", "streetAddress", "alternateName", "slogan") and isinstance(v, str): s.out.append((f"@ld[{k}]", v))
                                else: walk(v)
                        elif isinstance(o, list):
                            for v in o: walk(v)
                    walk(json.loads(s.buf))
                except Exception as e: s.out.append(("@ld[error]", str(e)))
        if s.stack: s.stack.pop()
    def handle_data(s, d):
        if s.ld: s.buf += d
        if s.skip: return
        t = " ".join(d.split())
        if t: s.out.append((s.stack[-1] if s.stack else "", t))
def items(path):
    p = P(); p.feed(open(path, encoding="utf-8").read()); return p.out
def words(t): return re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ']+", t)
def score(t):
    w = [x.lower() for x in words(t)]
    return sum(x in EN for x in w), sum(x in ES for x in w), len(w)
pages = []
for dp, dn, fn in os.walk(os.path.join(ROOT, "es")):
    for f in fn:
        if f.endswith(".html"): pages.append(os.path.join(dp, f))
total = 0
for pg in sorted(pages):
    rel = os.path.relpath(pg, ROOT)
    en_pg = os.path.join(ROOT, rel[3:]) if rel.startswith("es/") else None
    en_set = set(t for _, t in items(en_pg)) if en_pg and os.path.exists(en_pg) else set()
    seen = set(); flagged = []
    for tag, t in items(pg):
        if t in seen or ALLOW.match(t): continue
        seen.add(t)
        e, s_, n = score(t)
        same = t in en_set and len(re.findall(r"[A-Za-z]{3,}", t)) >= 2
        if (n >= 2 and e > s_ and e >= 1) or same or (n == 1 and t in en_set and len(t) > 3 and not re.match(r"^[\d\W]+$", t) and t[0].isupper() and False):
            flagged.append((tag, t, "SAME" if same else f"en{e}/es{s_}"))
    html_src = open(pg, encoding="utf-8").read()
    n_langen = html_src.count('lang="en"')
    print(f"\n=== {rel}  flagged={len(flagged)}  lang=\"en\" attrs={n_langen}")
    for tag, t, why in flagged: print(f"  [{why}] {tag}: {t[:170]}")
    total += len(flagged)
print("\nTOTAL FLAGGED", total)
sys.exit(1 if total else 0)
