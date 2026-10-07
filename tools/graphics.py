# -*- coding: utf-8 -*-
"""SVG graphics: line icons, hero gauge, motorcycle inspection diagram. All original artwork."""
import math


def _polar(cx, cy, r, deg):
    """deg measured clockwise from 12 o'clock."""
    a = math.radians(deg)
    return cx + r * math.sin(a), cy - r * math.cos(a)


def _f(x):
    return f"{x:.2f}".rstrip("0").rstrip(".")


# ------------------------------------------------------------------ icons
def _snow():
    parts = []
    for ang in (0, 60, 120):
        x1, y1 = _polar(24, 24, 17, ang)
        x2, y2 = _polar(24, 24, 17, ang + 180)
        parts.append(f'<path d="M{_f(x1)} {_f(y1)}L{_f(x2)} {_f(y2)}"/>')
    for ang in range(0, 360, 60):
        bx, by = _polar(24, 24, 11, ang)
        l1 = _polar(bx, by, 5, ang - 50)
        l2 = _polar(bx, by, 5, ang + 50)
        parts.append(f'<path d="M{_f(l1[0])} {_f(l1[1])}L{_f(bx)} {_f(by)}L{_f(l2[0])} {_f(l2[1])}"/>')
    return "".join(parts)


def _tire():
    ticks = []
    for i in range(16):
        a = i * 22.5
        x1, y1 = _polar(24, 24, 14, a)
        x2, y2 = _polar(24, 24, 18, a)
        ticks.append(f'<path d="M{_f(x1)} {_f(y1)}L{_f(x2)} {_f(y2)}"/>')
    return '<circle cx="24" cy="24" r="19"/><circle cx="24" cy="24" r="6"/><circle cx="24" cy="24" r="12" stroke-dasharray="2 3"/>' + "".join(ticks)


def _brakes():
    dots = []
    for i in range(6):
        x, y = _polar(24, 24, 11.5, i * 60)
        dots.append(f'<circle cx="{_f(x)}" cy="{_f(y)}" r="1.7"/>')
    return '<circle cx="24" cy="24" r="18"/><circle cx="24" cy="24" r="5"/>' + "".join(dots) + '<path d="M36 7c4 3 6 7 6.5 11M41 14l1.5 4"/>'


def _gear():
    return ('<circle cx="24" cy="24" r="15" stroke-width="6" stroke-dasharray="4.7 3.15" />'
            '<circle cx="24" cy="24" r="10"/><circle cx="24" cy="24" r="4"/>')


ICONS = {
    "inspection": '<rect x="7" y="7" width="34" height="34" rx="6"/><path d="M15 25l6 6 12-14"/>',
    "oil": '<path d="M24 6c7 9.5 12 14.5 12 21a12 12 0 0 1-24 0c0-6.500 5-11.500 12-21z"/><path d="M18 29a6 6 0 0 0 6 6"/>',
    "brakes": _brakes(),
    "tire": _tire(),
    "engine": '<path d="M9 19h6l3-5h12l3 5h6v15H9z"/><path d="M5 23v7M43 23v7M20 14v-4h8v4M16 34v4M32 34v4"/>',
    "spring": '<path d="M16 7h16M24 7v6l-8 3.500 16 4.500-16 4.500 16 4.500-8 3.500v5M16 41h16"/>',
    "snow": _snow(),
    "battery": '<rect x="5" y="15" width="38" height="24" rx="3"/><path d="M13 15v-5h7v5M28 15v-5h7v5M25 21l-4 7h7l-4 7"/>',
    "gear": _gear(),
    "van": '<path d="M4 13h25v20H4zM29 19h9l6 7v7H29z"/><circle cx="14" cy="35" r="4.500"/><circle cx="36" cy="35" r="4.500"/>',
    "seal": '<circle cx="24" cy="20" r="13"/><path d="M18 20l4.500 4.500L31 15M17 31l-3 12 10-4.500L34 43l-3-12"/>',
    "moto": '<circle cx="11" cy="33" r="7"/><circle cx="37" cy="33" r="7"/><path d="M11 33l8-13h9l9 13M19 20l-3-5h-5M28 20l-2-6h7M16 29h14"/>',
    "phone": '<path d="M12 6h7l3 9-4 3a22 22 0 0 0 11 11l3-4 9 3v7a4 4 0 0 1-4 4C22 39 9 26 8 10a4 4 0 0 1 4-4z"/>',
    "pin": '<path d="M24 43s13-12 13-22a13 13 0 0 0-26 0c0 10 13 22 13 22z"/><circle cx="24" cy="21" r="5"/>',
    "mail": '<rect x="5" y="10" width="38" height="28" rx="4"/><path d="M6 14l18 14 18-14"/>',
}


def icon(name, size=48, cls="ic"):
    return (f'<svg class="{cls}" width="{size}" height="{size}" viewBox="0 0 48 48" fill="none" stroke="currentColor" '
            f'stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{ICONS[name]}</svg>')


# ------------------------------------------------------------------ hero gauge
def gauge(label_top, label_bottom, aria):
    cx = cy = 260
    out = []
    out.append(f'<svg class="gauge-svg" viewBox="0 0 520 520" role="img" aria-label="{aria}">')
    out.append('''<defs>
<radialGradient id="gFace" cx="50%" cy="42%" r="62%"><stop offset="0" stop-color="#2A2C30"/><stop offset="1" stop-color="#08090A"/></radialGradient>
<linearGradient id="gBezel" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8A8D92"/><stop offset=".5" stop-color="#3A3C40"/><stop offset="1" stop-color="#A0A3A8"/></linearGradient>
<radialGradient id="gGlow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#E4372F" stop-opacity=".22"/><stop offset="1" stop-color="#E4372F" stop-opacity="0"/></radialGradient>
</defs>''')
    out.append('<circle cx="260" cy="260" r="258" fill="url(#gBezel)"/>')
    out.append('<circle cx="260" cy="260" r="246" fill="#0A0A0B"/>')
    out.append('<circle cx="260" cy="260" r="240" fill="url(#gFace)"/>')
    out.append('<circle cx="260" cy="260" r="240" fill="url(#gGlow)"/>')
    # redline arc (last 3 majors: 6..9 => 60..135 deg)
    a0, a1 = 75, 135
    x0, y0 = _polar(cx, cy, 214, a0)
    x1, y1 = _polar(cx, cy, 214, a1)
    out.append(f'<path d="M{_f(x0)} {_f(y0)}A214 214 0 0 1 {_f(x1)} {_f(y1)}" fill="none" stroke="#E4372F" stroke-width="6" stroke-linecap="butt" opacity=".95"/>')
    # ticks: -135..135, major every 30, minor every 6
    for i in range(0, 46):
        ang = -135 + i * 6
        major = (i % 5 == 0)
        r1, r2 = (196, 224) if major else (210, 224)
        xa, ya = _polar(cx, cy, r1, ang)
        xb, yb = _polar(cx, cy, r2, ang)
        hot = ang >= 75
        col = "#E4372F" if hot else "#D5D7DA"
        w = 4 if major else 1.8
        out.append(f'<path d="M{_f(xa)} {_f(ya)}L{_f(xb)} {_f(yb)}" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>')
        if major:
            n = i // 5
            tx, ty = _polar(cx, cy, 168, ang)
            out.append(f'<text x="{_f(tx)}" y="{_f(ty + 11)}" text-anchor="middle" class="g-num{" hot" if hot else ""}">{n}</text>')
    # face text in the lower gap
    out.append(f'<text x="260" y="326" text-anchor="middle" class="g-name">{label_top}</text>')
    out.append(f'<text x="260" y="356" text-anchor="middle" class="g-sub">{label_bottom}</text>')
    # needle
    out.append('<g class="needle" id="needle"><path d="M255.500 300L260 52L264.500 300Z" fill="#E4372F"/>'
               '<path d="M258 300L260 52L262 300Z" fill="#fff" opacity=".35"/></g>')
    out.append('<circle cx="260" cy="260" r="26" fill="#0A0A0B" stroke="#E4372F" stroke-width="4"/>'
               '<circle cx="260" cy="260" r="9" fill="#E4372F"/>')
    out.append('</svg>')
    return "".join(out)


# ------------------------------------------------------------------ motorcycle diagram
# (id, marker x, y)
MOTO_MARKERS = {
    "brakes": (532, 214),
    "steering": (418, 112),
    "suspension": (474, 190),
    "tires": (96, 206),
    "lights": (486, 142),
    "mirrors": (374, 40),
    "fuel": (322, 118),
    "horn": (398, 196),
    "body": (214, 196),
}


def moto(parts, aria):
    """parts: list of (id, label). Returns inline SVG. Marker numbers match list order."""
    order = [p[0] for p in parts]
    labels = {p[0]: p[1] for p in parts}
    s = []
    s.append(f'<svg class="moto-svg" viewBox="0 0 620 360" role="group" aria-label="{aria}">')
    # base neutral drawing (engine, wheels' hubs, ground)
    s.append('<path class="ground" d="M20 328H600"/>')
    s.append('<g class="neutral"><rect x="250" y="202" width="128" height="74" rx="14"/>'
             '<rect x="288" y="168" width="58" height="36" rx="4"/>'
             '<path d="M298 168v36M310 168v36M322 168v36M334 168v36"/>'
             '<circle cx="150" cy="250" r="10"/><circle cx="500" cy="250" r="10"/>'
             '<circle cx="150" cy="250" r="3"/><circle cx="500" cy="250" r="3"/>'
             '<path d="M230 255L150 250"/></g>')
    # parts
    P = {}
    P["tires"] = ('<circle cx="150" cy="250" r="78"/><circle cx="150" cy="250" r="58"/>'
                  '<circle cx="500" cy="250" r="78"/><circle cx="500" cy="250" r="58"/>')
    P["brakes"] = ('<circle cx="500" cy="250" r="38"/><circle cx="500" cy="250" r="26"/>'
                   '<rect x="518" y="198" width="22" height="30" rx="6"/>')
    P["suspension"] = '<path d="M440 112L500 250M452 106L512 244"/><path d="M468 172l-10 5M484 208l-10 5"/>'
    P["steering"] = ('<circle cx="426" cy="124" r="9"/><path d="M440 108L410 92L384 98"/>'
                     '<path d="M384 98l-6-6"/>')
    P["lights"] = ('<ellipse cx="480" cy="140" rx="17" ry="21"/><path d="M468 140h24"/>'
                   '<rect x="46" y="176" width="16" height="22" rx="5"/>')
    P["mirrors"] = '<path d="M386 96L376 62"/><ellipse cx="374" cy="50" rx="15" ry="9"/>'
    P["fuel"] = ('<path d="M246 142C250 106 300 96 340 100C376 104 396 116 402 132L396 152L250 162Z"/>'
                 '<path d="M296 266C276 304 196 308 118 288L72 276"/><path d="M118 290L72 278L70 266L118 276"/>')
    P["horn"] = '<rect x="384" y="188" width="28" height="16" rx="6"/><path d="M392 192v8M400 192v8"/>'
    P["body"] = ('<path d="M430 140L230 255M230 255L206 168M150 250L230 255"/>'
                 '<path d="M150 142C170 126 216 126 246 142L250 162L160 166Z"/>'
                 '<path d="M62 218A92 92 0 0 1 238 218"/>')
    for pid in order:
        s.append(f'<g class="part" data-part="{pid}">{P[pid]}</g>')
    # markers
    for i, pid in enumerate(order, start=1):
        x, y = MOTO_MARKERS[pid]
        s.append(f'<g class="hot" data-part="{pid}" role="button" tabindex="0" aria-label="{i}. {labels[pid]}" transform="translate({x} {y})">'
                 f'<circle r="17" class="hot-bg"/><text y="6" text-anchor="middle">{i}</text></g>')
    s.append('</svg>')
    return "".join(s)
