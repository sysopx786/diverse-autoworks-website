"""Build docs/assets/img/og-default.jpg (1200x630 social-share card) from the logo and site fonts.

Run from the repo root:  python tools/make_og_image.py
Swap the photo/logo or text here when the owner supplies a real shop photo, then rebuild.
"""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.join(os.path.dirname(__file__), "..", "docs", "assets")
W, H = 1200, 630
BG, RED, WHITE, MIST = (15, 16, 18), (228, 55, 47), (255, 255, 255), (166, 169, 174)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
# soft lighter band on the right so the card is not flat
for x in range(W // 2, W):
    t = (x - W // 2) / (W // 2)
    shade = int(10 * t)
    d.line([(x, 0), (x, H)], fill=(BG[0] + shade, BG[1] + shade, BG[2] + shade + 2))

logo = Image.open(os.path.join(ROOT, "img", "diverse-autoworks-logo.png")).convert("RGBA")
lw = 400
logo = logo.resize((lw, round(logo.height * lw / logo.width)), Image.LANCZOS)
img.paste(logo, (W - lw - 70, (H - logo.height) // 2), logo)

head = ImageFont.truetype(os.path.join(ROOT, "fonts", "barlow-condensed-latin-800-normal.woff2"), 92)
sub = ImageFont.truetype(os.path.join(ROOT, "fonts", "barlow-latin-600-normal.woff2"), 40)

x = 70
d.rectangle([x, 150, x + 120, 158], fill=RED)
d.text((x, 176), "Auto Repair &", font=head, fill=WHITE)
d.text((x, 272), "State Inspections", font=head, fill=WHITE)
d.text((x, 430), "Phoenixville, PA", font=sub, fill=WHITE)
d.text((x, 484), "610-650-0316", font=sub, fill=MIST)

out = os.path.join(ROOT, "img", "og-default.jpg")
img.save(out, "JPEG", quality=88, optimize=True)
print(out, os.path.getsize(out), "bytes")
