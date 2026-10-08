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
- Language switch is one round flag button (no dropdown) that shows the OTHER language: Spain flag + ES on the English site, US flag + EN on the Spanish site. One click opens the same page in that language. Art is `flag_svg()` in `tools/build.py`; styles are the `.lang` block in `main.css`.
- Reviews page in Spanish (Oct 7, 2026): all Google, CARFAX and Yelp reviews plus the featured quotes are translated. Translations live in `tools/reviews_es.py`, matched by position to the source lists; `build.py` asserts the counts, so adding a review to a JSON file fails the build until its Spanish line is added. The Spanish is a draft: have a native speaker review it.
- Mobile sticky bottom bar removed (Oct 7, 2026). Phone stays in the header and every page's text.
- Mobile menu adds a Notary Services link (mobile only).
- CARFAX badge and Yelp mark added to the rating cards on /reviews/.

## Notary section redesign (Oct 7, 2026)
- The Contact page notary block (`/contact/#notary`, `/es/contact/#notary`) is now a full section: what we notarize, how it works in Pennsylvania, PA rules, what to bring or avoid, 15 FAQs, and a link band to Inspections and Services.
- Copy (EN + ES) lives in `tools/notary.py`; markup is `notary_sections()` in `tools/build.py`; styles are the `.nt-*` block at the end of `docs/assets/css/main.css`. The block also writes FAQPage JSON-LD for the contact page.
- The Spanish is a draft. Have a native speaker review it before treating it as final.
- The older three-question notary FAQ in `FAQ_CATS` still feeds `/faq/`; it was left as is.

## More "ask us about" services (Oct 8, 2026)
- 14 services from the owner checklist (Part B) are on `/services/` under "Also ask us about (call to confirm)": towing, pre-purchase inspections, cylinder head & block, fuel system & gas tank, spark plugs, onboard computer, differential, emission control repair, heater, corrosion, wheels, tire retreads, ball joints, body work. Copy and FAQs (5 questions each, EN + ES) live in `tools/more_services.py`.
- They are NOT confirmed offerings. Wording is "call to confirm," same as tags/title, EV/hybrid, tire rotation, and alternators. When the owner marks one Yes, move it from `more_services.py` into `SERVICES` in `tools/content.py` with confirmed wording.
- Deduplicated: tire rotation and alternators/starters already existed; gas tank + fuel system and differential + axles are one card each; the old general "bodywork" FAQ became the Body work card; a repeated alternator question under Batteries was replaced.
- Part A: Engine, Oil/maintenance (fuel), Tires, Steering & suspension, A/C and Drivetrain descriptions now say what is listed and point to the call-to-confirm cards for the rest.
- The Spanish is a draft. Have a native speaker review it.
