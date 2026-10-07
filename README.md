# Diverse Autoworks website

Bilingual (English / Spanish) static site for Diverse Autoworks, Inc., Phoenixville, PA.

- `docs/` is the built site. GitHub Pages: Settings > Pages > Deploy from branch > `main` / `/docs`.
- `tools/content.py` holds all copy (EN + ES). `tools/build.py` builds the site into `docs/`.
- Rebuild: `python3 tools/build.py`
- Optional env vars: `SITE_URL` (canonical, hreflang, sitemap) and `FORM_ENDPOINT` (form backend).
- Tests: `tests/axe_audit.py` (accessibility), `tests/visual.py` (screenshot compare).

Third-party names and logos (Google, Yelp, CARFAX) belong to their owners and appear only to attribute customer reviews.
