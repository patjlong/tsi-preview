# site/assets provenance (phase two build, started 2026-09-04)

Every file under site/assets/ is a copy of an already-published asset from the
tsi-preview repo-root assets/ tree (tag tsi-client-release-2026-08-28). Nothing
here was generated, retouched or upscaled for phase two. Neutral names replace
the r4 names per DESIGN-RULES R60; credits stay in this file, never on a page.

## img/ (hero-r4 copies, neutral names)

| site/assets/img | original (repo-root assets/hero-r4/) | provenance line |
|---|---|---|
| tsi-drydock-{480,960,1920}.jpg | r4-drydock-norfolk-*.jpg | hero-r4/SOURCES.md, US Navy public domain, sourced 2026-08-25 under R31 |
| tsi-welder-{480,960,1920}.jpg | r4-welder-hull-*.jpg | hero-r4/SOURCES.md, US Navy public domain, sourced 2026-08-25 under R31 |
| tsi-crane-{480,960,1920}.jpg | r4-crane-mast-nn-*.jpg | hero-r4/SOURCES.md, US Navy public domain, sourced 2026-08-25 under R31 |
| tsi-sparks-{480,960,1920}.jpg | r4-sparks-shower-*.jpg | hero-r4/SOURCES.md |
| tsi-firewatch-{480,960,1920}.jpg | r4-firewatch-nn-*.jpg | hero-r4/SOURCES.md |
| tsi-welder-review-{480,960,1920}.jpg | r4-welder-review-*.jpg | hero-r4/SOURCES.md |

r4-keel-welder-nn is NOT copied (R48: out of every page of the new build).

## video/ (the six R59 files, byte-identical copies)

intro-storm-b.mp4 (2026-10-05 recut of intro-storm.mp4: 3.85 s to 4.40 s removed, 0.25 s dissolve; original in assets-archive/intro-original-2026-09-04/), loop-drydock.mp4, loop-crane.mp4, loop-branch.mp4,
loop-warehouse.mp4, loop-training.mp4. Provenance unchanged: repo-root
assets/video/SOURCES.md (Seedance-generated, flagged against R32 on 2026-08-25
and 2026-08-26; exempt for this draft on Pat's authority, R59). loop-keel.mp4 and
loop-welder.mp4 are not copied.

## photos/ (Jay's eight, derivatives as published)

Copied one to one from repo-root assets/photos/ (tsi-arrival, tsi-branch,
tsi-crew, tsi-marine, tsi-orientation, tsi-training, tsi-warehouse sets).
Client-owned photography supplied by Jay Prock 2026-08-14; usage per the
2026-08-15 photo library audit.

## logo/, fonts/, vendor/

Untouched copies of the published assets (R1 for the logo). Fonts: Encode Sans,
Space Grotesk, IBM Plex Mono 400/500 (R12). Vendor: GSAP, ScrollTrigger, Lenis.

## Migrated client media (blog and page images)

One provenance line, per the kickoff prompt: origin https://www.tidewaterstaffing.com/wp-content/uploads/,
client-owned, fetched 2026-09-04 through the public WordPress REST API with a
browser User-Agent, one request per second, cached under ~/tsi-site/import/.
Re-encoded to the Technical foundation v1 widths at build time.

## TSI photo drop, 2026-09-10 (R78)

Two photographs received as email attachments from TSI's office via Marion (Jay copied), 2026-09-10 13:28 ET.
Client-owned, chosen by TSI for having no client name or logo visible. Filed at natural aspect, never upscaled:
photos/tsi-cookout-1920.jpg and -960.jpg (from 3547x2672 PNG), photos/tsi-ppe-crew-1491.jpg and -960.jpg (from 1491x1988 PNG).
Originals under ~/tsi-site/import/photos-2026-09-10/. Nine further Drive links in the same email are not yet accessible to KODA.

## Warehouse still, 2026-09-10 (R74)

img/tsi-warehouse-1280.jpg and -960.jpg are a single frame (t=2 s) from assets/video/loop-warehouse.mp4, the loop already
used behind the warehouse hero. Same provenance as that loop. 1280 is the loop's native width; not upscaled.

## photos/ TESC set (added 2026-10-03)

tsi-tesc-front, tsi-tesc-side, tsi-tesc-floor, each as 1200 and 1920 wide JPEGs (16:9).
Photographs of TESC, the Tidewater Employment Simulation Center in Portsmouth, taken and
emailed by Clarissa Shaddock (TSI) on 2026-10-01 after Jay asked for a picture of TESC on
the TESC page. Cropped to 16:9 and downscaled from 3072x4080 originals, never upscaled or
retouched. Originals and the crop record: assets-archive/tesc-originals-2026-10-01/.
Client-owned photography; checked for customer and shipyard identifiers (R60): none.

## 2026-10-05 hero additions (Pat, in session)

Real photographs, TSI's own, from their existing website's media library (import/media):
- photos/tsi-merch-{1200,1920}.jpg from 2019/10/IMG_4308.jpeg (hoodie and beanie). Opens Merchandise.
- photos/tsi-riverstar-{1200,1920}.jpg from 2021/02/IMG_2850-scaled.jpg (Elizabeth River Project River Star Business banner, 2021; faces masked). Opens Environmental Stewardship.
- photos/tsi-tesc-front-* (Clarissa, 2026-10-01) now opens the Portsmouth branch page, focal point on the 742 Florida Ave. sign.

Real photograph, widened by AI on one side only:
- photos/tsi-tesc-wide-{1200,1920}.jpg. Centre is Clarissa's PXL_20261001_150921652 untouched (the whole building face, door, logo and brick sign are real pixels). The left third (the end of the building with the roll door, trees, lawn) was generated with Codex image generation to give the hero band room. Canvas and result in assets-archive/generated-2026-10-05/. Opens TESC.

AI GENERATED, not photographs of Tidewater Staffing (Codex image generation, no people, no logos, no text):
- photos/tsi-gen-jobs-* (boots, gloves and tool bag on a pier). Opens Open Jobs.
- photos/tsi-gen-resume-* (application on a clipboard). Opens Submit Resume.
- photos/tsi-gen-contact-* (a brick office entrance; NOT a real Tidewater Staffing office). Opens Contact.
- photos/tsi-gen-contracting-* (paperwork on a desk, dry dock beyond). Opens Contracting Details.
- photos/tsi-gen-manufacturing-* (a plant floor: press brake, CNC machining centers, welding tables, bridge crane; no hard hats). Opens Manufacturing and Industrial Staffing (Gabe, 2026-10-06; added 2026-10-08).
- photos/tsi-gen-blog-* (a steel workbench with gloves, tape measure, clipboard and tools in a fabrication shop at sunrise; no people, no hard hats). Opens the Blog index (Pat, design decision 08, 2026-10-08; replaces the Chesapeake office photo there, R82).
These six are placeholders for real photographs from TSI. Originals in assets-archive/generated-2026-10-05/ and assets-archive/generated-2026-10-08/.

## 2026-10-05 later: branch office photographs (Pat, in session)

Real photographs, uploaded by Tidewater Staffing to its own Google Business listings ("By owner" tab, read 2026-10-05). Originals in assets-archive/google-listing-owner-photos-2026-10-05/. No Street View or Google-owned imagery is used.
- photos/tsi-vb-office-{1200,1920}.jpg: the Virginia Beach office, 5184x3456 original. Opens Virginia Beach.
- photos/tsi-vb-sign-{1200,1920}.jpg: the roadside sign at 5425 Virginia Beach Blvd., 1600x1067 original. Opens Branches.
- photos/tsi-branch-* is the Chesapeake office (the same photograph is on the Chesapeake listing). Opens Chesapeake; still opens the blog index too.
TSI should confirm it holds the rights to these three (it posted them as owner).
