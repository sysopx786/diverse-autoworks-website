"""Visual regression. `python3 tests/visual.py update` writes baselines; `python3 tests/visual.py` compares.
Serves docs/ on :8124. Needs playwright + Pillow."""
import asyncio, subprocess, sys, os, time
from datetime import datetime
from zoneinfo import ZoneInfo
from playwright.async_api import async_playwright
from PIL import Image, ImageChops
HERE = os.path.dirname(__file__); BASE = os.path.join(HERE, "baseline")
# Monday 19 Oct 2026, 10:00 a.m. New York: inside shop hours, so the status strip is always "Open now" or "Closing soon" on this clock.
FIXED_TIME = datetime(2026, 10, 19, 10, 0, tzinfo=ZoneInfo("America/New_York"))
PAGES = {"home": "/", "services": "/services/", "inspections": "/inspections/", "fleet": "/fleet-repairs/", "about": "/about/",
         "reviews": "/reviews/", "faq": "/faq/", "contact": "/contact/", "es-home": "/es/",
         "moto": "/motorcycle-inspection/", "es-moto": "/es/motorcycle-inspection/"}
VPS = {"d": {"width": 1440, "height": 900}, "m": {"width": 390, "height": 844}}
async def main(update):
    srv = subprocess.Popen([sys.executable, "-m", "http.server", "8124"], cwd=os.path.join(HERE, "..", "docs"), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(1); bad = 0
    try:
        async with async_playwright() as p:
            b = await p.chromium.launch()
            for vn, vp in VPS.items():
                pg = await b.new_page(viewport=vp, reduced_motion="reduce")
                # Freeze the clock so the open/closed strip (computed from the current New York time) is stable.
                await pg.clock.set_fixed_time(FIXED_TIME)
                for name, path in PAGES.items():
                    await pg.goto("http://localhost:8124" + path); await pg.wait_for_timeout(1200)
                    f = os.path.join(BASE, f"{name}-{vn}.png"); tmp = f + ".new.png"
                    await pg.screenshot(path=tmp)
                    if update or not os.path.exists(f): os.replace(tmp, f); continue
                    diff = ImageChops.difference(Image.open(f).convert("RGB"), Image.open(tmp).convert("RGB")).getbbox()
                    os.remove(tmp)
                    if diff: bad += 1; print("CHANGED", name, vn, diff)
            await b.close()
    finally:
        srv.terminate()
    print("baseline updated" if update else ("no visual changes" if not bad else f"{bad} changed"))
asyncio.run(main("update" in sys.argv))
