# Cedar Bend demo — the Quorum small-town website template (HEAD)

Built 2026-09-21. A fictional Texas town, so no real town is misrepresented; the black ribbon says so on every page.
Purpose: the thing we show a town clerk when they say "show me". Sells the packages in
`Circle-Vault/Quorum/Gov-Bids/small-town-website-offer.md`.

- `build.py` writes the 7 pages from one layout. Edit build.py, not the HTML. `python build.py`.
- `assets/site.css` holds the tokens. Newsreader (display) + Source Sans 3 (body), civic green, brick accent rationed.
- Verified 2026-09-21: 0 accessibility violations on all 7 pages (accesslint, WCAG 2.1 A/AA), impeccable detect down to one padding nit, no em-dashes, no emoji icons, phone layout checked at 375px.
- All PDF links are `#` placeholders and the pay button is disabled: it is a demo.
- NOT a CMS. A town's clerk cannot edit this. The paid build is this design on WordPress (see the offer doc, "What we still need to build"). This repo is the design spec for that theme.
- Live (noindex): see README / git remote.
