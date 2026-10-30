# Diverse Autoworks website

Bilingual (English / Spanish) static site for Diverse Autoworks, Inc., Phoenixville, PA.

## Links
- Live site (canonical host): https://mydiverseauto.com/ (Cloudflare Pages). Use the apex host, not www.
- GitHub Pages mirror (may lag the live site): https://sysopx786.github.io/diverse-autoworks-website/
- Private preview (Claude artifact, owner access only): https://claude.ai/artifact/9Zd66Fr1JT8dMqqUMcFHsL

- `docs/` is the built site. Deploy target: see the hosting note above. The GitHub Pages setting is Settings > Pages > Deploy from branch > `main` / `/docs`.
- Known drift (Oct 18, 2026): the live site's header shows "Shop open Monday–Friday. Call for current hours." with no open/closed strip, but this repo's build includes the strip. Check which build is deployed before treating either as current.
- `tools/content.py` holds all copy (EN + ES). `tools/build.py` builds the site into `docs/`.
- Rebuild: `SITE_URL=https://mydiverseauto.com python3 tools/build.py` (on Windows: `python`, and set the variable first, e.g. `$env:SITE_URL="https://mydiverseauto.com"` in PowerShell).
- **Always build with `SITE_URL` set to the live host.** Without it the build leaves out the canonical and hreflang tags, the sitemap and robots.txt sitemap line, and all structured data (JSON-LD) except a bare business block on the home page. Check `docs/index.html` for `rel="canonical"` and `application/ld+json` after building.
- Env vars: `SITE_URL` (required for production builds: canonical, hreflang, sitemap, structured data) and the optional `FORM_ENDPOINT` (form backend).
- Tests: `tests/axe_audit.py` (accessibility), `tests/visual.py` (screenshot compare).

Third-party names and logos (Google, Yelp, CARFAX) belong to their owners and appear only to attribute customer reviews.

## SEO build notes (Oct 20, 2026)
- **Always build with `SITE_URL`** (see Rebuild). Production builds also write `docs/sitemap.xml`, `docs/_headers` and update `tools/lastmod.json`.
- **Titles, descriptions, H1s** live in `PAGES` in `tools/content.py`. Keep titles at 60 characters or fewer and descriptions at 160 or fewer. After building, every page should still have exactly one `rel="canonical"`.
- **Structured data** is built in `structured_data()` in `tools/build.py`: one `AutoRepair` entity (`/#business`, hours read from `SHOP`, `sameAs` from `YELP_URL`/`CARFAX_URL`, offer catalog from the owner-confirmed services only), plus WebSite/WebPage on the home page and Service + BreadcrumbList on inner pages. Deliberately NOT included until real values exist: `geo` (needs real coordinates), `image` (needs a real shop photo), `priceRange`. Do not add `aggregateRating`: the reviews are third-party.
- **Motorcycle page** `/motorcycle-inspection/` (`PAGES["moto"]`, `page_moto()`): year-round motorcycle inspections under PA Act 149 of 2024, as stated in the PennDOT announcement linked on the page. No price, walk-in policy or timing is published because the owner has not confirmed them. Spanish verified by a native speaker (Oct 2026).
- **Sitemap `lastmod`**: `tools/lastmod.json` holds a hash and a date per page; a date only moves when that page's HTML changes. Commit the file with the build.
- **Share image**: `python tools/make_og_image.py` rebuilds `docs/assets/img/og-default.jpg` (1200x630). Re-run it, or replace the file, when the owner supplies a real shop photo.
- **Images**: the logo and hero photos are served as WebP (`diverse-autoworks-logo.webp`, `-560.webp`, `shop-hero-800.webp`, `shop-hero-1600.webp`). The PNG logo stays for the schema `logo` URL. The home hero is preloaded in `head_tags()`.
- **Cache-busting**: the CSS and JS links carry `?v=<hash of the file>` (`asset()` in `tools/build.py`), so a changed stylesheet or script is fetched straight away; they are cached for a year (`immutable`). Edit `docs/assets/css/main.css` or `docs/assets/js/main.js` directly, then rebuild; the version in every page updates by itself. Without this the 1-day cache could serve new HTML with an old stylesheet.
- **Home trust strip** (rating + address above the headline): built from `RATINGS` / `RATINGS_ASOF` in `tools/content.py`, the same figures as the Reviews page, so update them in one place when the ratings change. On phones only the Google rating and the address show; the CARFAX rating and the "as of" date show on wider screens. The home hero photo is 2:1 on phones to keep the strip and the Call button near the first screen.
- **Inner-page schema**: every page repeats a short business and website node (same `@id` as the full node on the home page), so a Service's provider resolves on the page itself. The privacy pages carry a WebPage + breadcrumb too.
- **/inspections/ facts** (what the safety inspection checks, sticker validity, the Philadelphia-area emissions region that includes Chester County, and that fees are posted at stations) come from PennDOT's consumer FAQ and Drive Clean PA, each linked on the page. Re-check them if PennDOT's pages change. The Spanish for this block was added Oct 21, 2026 and still needs a native-speaker review.
- **Old Wix paths**: `docs/_redirects` (built from `REDIRECTS_FILE` in `tools/build.py`) sends the old Wix paths (`/about-us`, `/contact-us`, `/book-online`, `/services-1`, `/blank`) to the new pages. The old domain redirects here and keeps the path. Add a line when Cloudflare shows another old path being requested.
- **Hosting headers**: `docs/_headers` (from `HEADERS_FILE` in `tools/build.py`) is read by Cloudflare Pages: security headers and cache lifetimes. No CSP yet. The email obfuscation ("[email protected]") is a Cloudflare dashboard setting (Scrape Shield), not something the repo controls.

## Header, call bar, rating icons (Oct 7, 2026)
- Language switch is one round flag button (no dropdown) that shows the OTHER language: Spain flag + ES on the English site, US flag + EN on the Spanish site. One click opens the same page in that language. Art is `flag_svg()` in `tools/build.py`; styles are the `.lang` block in `main.css`.
- Reviews page in Spanish (Oct 7, 2026): all Google, CARFAX and Yelp reviews plus the featured quotes are translated. Translations live in `tools/reviews_es.py`, matched by position to the source lists; `build.py` asserts the counts, so adding a review to a JSON file fails the build until its Spanish line is added. The Spanish was verified by a native speaker (Oct 2026).
- Mobile sticky bottom bar removed (Oct 7, 2026). Phone stays in the header and every page's text.
- Mobile menu adds a Notary Services link (mobile only).
- CARFAX badge and Yelp mark added to the rating cards on /reviews/.

## Confirmed services (Oct 18, 2026)
- 13 services the owner confirmed are in `tools/confirmed_services.py` and appear in the main services list (`/services/`), each with its own FAQ category (5 questions, EN + ES). Groups: Maintenance & engine, Brakes/tires/ride, Climate & cooling, and a new "Exhaust & emissions" group.
- Emission control repair moved from "Also ask us about" to the main list.
- Batteries and belts/coolant wording was updated to the owner's confirmed scope (testing, replacement, starting and charging diagnosis; fan and accessory belts; coolant systems).
- `tools/build.py` checks the FAQ count: 36 original + 65 new = 101. Update that number when adding or removing FAQs.
- The Spanish for these services was verified by a native speaker (Oct 2026).
- Engine card (Oct 18, 2026) now covers the owner's full engine list: ignition, fuel system, sensors, cooling, oil and seals, timing and valves, belts, internal repair, rebuild or replacement. Cylinder head & block repair, spark plugs, and onboard computer diagnostics moved from "Also ask us about" into the engine card. "Also ask us about" → Fuel system is now Gas tank service only.
- `build.py` FAQ count is now 36 + 65 + 2 = 103.

## Spanish coverage (Oct 8, 2026)
- Process rule: any English copy change in `tools/content.py`, `tools/more_services.py`, `tools/notary.py` or `tools/reviews_es.py` ships with its Spanish text in the same commit. Run `python3 tests/es_audit.py` before committing.
- Every page under `/es/` is built from the `es` side of each `t(en, es)` pair. `python3 tests/es_audit.py` scans all built Spanish pages (visible text, alt text, aria-labels, titles, meta, JSON-LD) for English and exits 1 if it finds any. Run it after adding a page, service or review.
- Fixed Oct 8: the three Pennsylvania source links on the notary section, the Google 4.9-star label on /es/reviews/, and the "(struts)" and "(retread)" asides. The search box now finds the 14 call-to-confirm services in both languages. The 404 page shows Spanish only on `/es/` paths and both languages elsewhere.
- Left in English on purpose: the shop name, addresses, e-mail, customer names, car trim names in CARFAX owner lines, the "check engine" dashboard label, and the titles of the three English-language PA government pages (marked "en inglés").

## Notary section redesign (Oct 7, 2026)
- The Contact page notary block (`/contact/#notary`, `/es/contact/#notary`) is now a full section: what we notarize, how it works in Pennsylvania, PA rules, what to bring or avoid, 15 FAQs, and a link band to Inspections and Services.
- Copy (EN + ES) lives in `tools/notary.py`; markup is `notary_sections()` in `tools/build.py`; styles are the `.nt-*` block at the end of `docs/assets/css/main.css`. The block also writes FAQPage JSON-LD for the contact page.
- The Spanish was verified by a native speaker (Oct 2026).
- The older three-question notary FAQ in `FAQ_CATS` still feeds `/faq/`; it was left as is.

## More "ask us about" services (Oct 8, 2026)
- 14 services from the owner checklist (Part B) are on `/services/` under "Also ask us about (call to confirm)" (renamed "More services" on Oct 30, 2026): towing, pre-purchase inspections, cylinder head & block, fuel system & gas tank, spark plugs, onboard computer, differential, emission control repair, heater, corrosion, wheels, tire retreads, ball joints, body work. Copy and FAQs (5 questions each, EN + ES) live in `tools/more_services.py`.
- Superseded Oct 30, 2026: the owner confirmed every service in this group. See "All services confirmed" below.
- Deduplicated: tire rotation and alternators/starters already existed; gas tank + fuel system and differential + axles are one card each; the old general "bodywork" FAQ became the Body work card; a repeated alternator question under Batteries was replaced.
- Part A: Engine, Oil/maintenance (fuel), Tires, Steering & suspension, A/C and Drivetrain descriptions now say what is listed and point to the call-to-confirm cards for the rest.
- The Spanish was verified by a native speaker (Oct 2026).

## Header: shrink on scroll, open/closed strip, search (Oct 8, 2026)

- Two rows: main row (logo, ES flag, call, search, menu) and a status strip. Logo and main row are larger at the top of the page and shrink smoothly on scroll; buttons and the strip never change size. The header is `position:fixed` with a `.hdr-spacer` of its full height, so shrinking never moves the page.
- **Shop hours live in one place: `SHOP` near the top of `tools/build.py`.** Hours are read in the shop's time zone (`America/New_York`), not the visitor's clock. Open = green, within `closingSoonMinutes` of closing = amber, closed = gray with the next opening.
- **Shop hours are confirmed by the owner (Oct 18, 2026): Mon-Fri 7:30 a.m.-4:30 p.m., Sat and Sun closed.** `sample` is `False`. Change them only in `SHOP`, then run `python3 tools/build.py`.
- Search button opens a local-index search (EN/ES, accent-insensitive). Index is `SEARCH_ROWS` in `tools/build.py`.
- Status wording (EN/ES) lives in `UI[...]["status"]`.

## All services confirmed; Google tag moved into the build (Oct 30, 2026)
- The owner confirmed every service that was worded "call to confirm" (tags & title, EV/hybrid, tire rotation & balancing, alternators & starters, pickup/drop-off/after-hours, towing, pre-purchase inspections, gas tanks, differential, heater, corrosion, wheels, retreads, ball joints, body work, transmission rebuild/replacement, no-start diagnosis).
- All "call to confirm" / "llame para confirmar" / "not listed" / "not a confirmed service" wording is gone from the site (EN + ES). The group heading "Also ask us about (call to confirm)" is now "More services" / "Más servicios". Cards stay in that group; copy and FAQs are in `tools/content.py` (`ASK_SERVICES`, `ASK_FAQ_CATS`) and `tools/more_services.py`.
- Structured data: the offer catalog in `business_node()` now lists every service except pickup/drop-off (a visit arrangement, not a service).
- Google tag (GA4 `G-R4MYP7LT9Z`, Google Ads `AW-18451378396`) and the click-to-call conversion (`gtag_report_conversion`) were added to `docs/` by hand in PRs #17-#19, so any rebuild would have deleted them. They now live in `GTAG_HEAD` / `add_tracking()` in `tools/build.py`, which runs on every page in `write()`. Never add tracking by editing `docs/` directly.

## Body work removed; PennDOT authorized agent (Oct 30, 2026)
- Owner: the shop does not do body work. The Body work card and its FAQ category are gone from `tools/more_services.py`, and the home "See all services" subtext no longer mentions it. `docs/assets/img/svc-bodywork.webp` is unused. Do not add body work, dent, paint or collision services back without the owner's OK.
- Owner confirmed the shop is a PennDOT authorized agent. The notary FAQ "Do you complete the title application and issue plates?" now says so (EN + ES). Owner also confirmed the shop issues plates (Oct 30, 2026); the answer says so.

## Brands not serviced (Oct 30, 2026)
- Joe confirmed: no repairs on Tesla, Rivian, Lucid, Karma, Polestar (factory software and high-voltage training), and no service on Rolls-Royce, McLaren, Bentley, Aston Martin, Lotus (specialized tools). They are removed from `BRAND_GROUPS` in `tools/content.py`, and the Brands note, the Electric & hybrid card and its first FAQ say so (EN + ES).
- Joe also confirmed no state inspections on those five luxury brands. The Inspections page lead, the inspections service card and the "which vehicles" inspection FAQ say so (EN + ES).
- The Google review about a Tesla state inspection and tire rotation stays: it is a real review, and those are not repairs.
