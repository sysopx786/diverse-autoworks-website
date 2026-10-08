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

## Services and FAQ expansion (Oct 8, 2026)
- Services page grew from 16 to 25 cards; FAQ page from 36 to 84 questions (27 categories), English and Spanish.
- Items from the owner's extracted services list that matched an existing card were merged into it, not added again: safety inspection and emissions testing (Inspections), tires and tire repair (Tires), tire rotation (Tires; the old "Ask us" rotation card was removed), cooling systems (A/C & cooling), spark plugs and on-board computer (Engine analysis), ball joints (Steering & suspension), axles and differentials (Drivetrain).
- New cards: Emissions control, Pre-purchase inspections, Engine repair & cylinder head, Fuel system & gas tanks, Imports, Wheels & wheel repair, Retreads & tire recycling, Heating, A/C refrigerant & coolant recycling, Corrosion control. They are listed in `NEW_SERVICES` in `tools/content.py`.
- New cards reuse the closest existing illustration (`SVC_IMG`). Imports and Corrosion control have no image yet.
- `build.py` no longer checks for exactly 36 FAQs. It now fails on duplicate service ids, titles, cards, FAQ category ids, or FAQ questions, and on services that point to a missing FAQ category.
- Removed a duplicate FAQ ("Do you repair alternators and starters?") that appeared under both Batteries and Alternators & Starters.
- Not published: the extracted list's general FAQs (appointments, written estimates, warranty, payment methods, approval before work) and any certification claim for refrigerant handling. Add them once the shop confirms the exact terms.
- The Spanish for all new copy is a draft. Have a native speaker review it.
