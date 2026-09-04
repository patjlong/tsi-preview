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

intro-storm.mp4, loop-drydock.mp4, loop-crane.mp4, loop-branch.mp4,
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
