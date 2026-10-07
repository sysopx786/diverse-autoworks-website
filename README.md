# Diverse Autoworks website

Bilingual (English / Spanish) static site for Diverse Autoworks, Inc., Phoenixville, PA.

## Links
- Public (GitHub Pages): https://sysopx786.github.io/diverse-autoworks-website/
- Private preview (Claude artifact, owner access only): https://claude.ai/artifact/9Zd66Fr1JT8dMqqUMcFHsL

- `docs/` is the built site. GitHub Pages: Settings > Pages > Deploy from branch > `main` / `/docs`.
- `tools/content.py` holds all copy (EN + ES). `tools/build.py` builds the site into `docs/`.
- Rebuild: `python3 tools/build.py`
- Optional env vars: `SITE_URL` (canonical, hreflang, sitemap) and `FORM_ENDPOINT` (form backend).
- Tests: `tests/axe_audit.py` (accessibility), `tests/visual.py` (screenshot compare).

Third-party names and logos (Google, Yelp, CARFAX) belong to their owners and appear only to attribute customer reviews.

## Header, call bar, rating icons (Oct 7, 2026)
- Language switch is a single button (no dropdown): it shows the OTHER language ("Español" on the English site, "English" on the Spanish site) and one click goes to the same page in that language.
- Mobile sticky bottom bar removed (Oct 7, 2026). Phone stays in the header and every page's text.
- Mobile menu adds a Notary Services link (mobile only).
- CARFAX badge and Yelp mark added to the rating cards on /reviews/.

## Notary section redesign (Oct 7, 2026)
- The Contact page notary block (`/contact/#notary`, `/es/contact/#notary`) is now a full section: what we notarize, how it works in Pennsylvania, PA rules, what to bring or avoid, 15 FAQs, and a link band to Inspections and Services.
- Copy (EN + ES) lives in `tools/notary.py`; markup is `notary_sections()` in `tools/build.py`; styles are the `.nt-*` block at the end of `docs/assets/css/main.css`. The block also writes FAQPage JSON-LD for the contact page.
- The Spanish is a draft. Have a native speaker review it before treating it as final.
- The older three-question notary FAQ in `FAQ_CATS` still feeds `/faq/`; it was left as is.
