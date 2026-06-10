# Mixam 24-Page Template Spec

> Print-template specification for a Meridian Prime comic hype issue / framework PDF.

**Sandbox Status:** APPROVED PRODUCTION SPEC

**Canon Status:** SANDBOX PRODUCTION DOCUMENT. This file defines print layout behavior only. It does not establish main Meridian Prime story canon.

**Intended Output:** One print-ready PDF framework/template for US Standard comic printing.

---

## Repository Quarantine

Main canon repository:

`Discontent2/meridian-prime`

Comic sandbox repository:

`Discontent2/Discontent2-meridian-prime-comic-sandbox`

All print templates, layout guides, production notes, and PDF exports generated from this specification must remain in the comic sandbox unless explicitly approved elsewhere.

---

## Product Intent

Create a print-ready framework/template PDF for a short Meridian Prime hype comic.

The first PDF generated from this spec should be a **layout framework**, not final illustrated story art. It should use vector guides, page labels, placeholder art boxes, safe-area markings, and production notes.

The template should support future use for:

- comic issue planning
- page-by-page adaptation
- promo covers
- teaser pages
- pitch packet visuals
- sample sequential pages
- creator credits pages
- back-cover teaser images
- ad placeholder pages
- lettering-safe layouts
- panel templates
- print-ready PDFs

---

## Print Format

| Item | Requirement |
|---|---:|
| Product type | US Standard comic |
| Binding | Staple-bound / saddle-stitch |
| Printing | Double-sided |
| Cover pages | 4 |
| Interior pages | 20 |
| Total pages | 24 |
| Page count rule | Must remain a multiple of 4 |
| PDF layout | Single pages in reading order |
| Printer spreads | Do not use printer spreads |

---

## Page Size and Measurement Source of Truth

Physical inch measurements are the source of truth.

| Area | Width | Height |
|---|---:|---:|
| Trim size | 6.69 in | 10.24 in |
| Bleed | 0.125 in on all sides | 0.125 in on all sides |
| Final canvas including bleed | 6.94 in | 10.49 in |
| Safe / quiet area | 0.25 in inside trim | 0.25 in inside trim |

### Safe Area Position

Because bleed is 0.125 in and the safe area starts 0.25 in inside trim, important elements should sit at least:

**0.375 in from the final canvas edge**

on all four sides.

### 300 DPI Pixel Reference

Use these values as implementation references only. If pixel rounding conflicts with inches, trust the inch measurements.

| Area | Width | Height |
|---|---:|---:|
| Final canvas including bleed | 2082 px | 3147 px |
| Trim size | 2007 px | 3072 px |
| Bleed | 37.5 px | 37.5 px |
| Safe margin from final canvas edge | 112.5 px | 112.5 px |

Suggested rounded pixel guides:

- Canvas: 2082 px x 3147 px
- Trim box begins at approximately 38 px from each canvas edge
- Safe area begins at approximately 113 px from each canvas edge

---

## Guide System

Each template page should include visible production guides unless a future export asks for hidden guides.

### Required Guides

- Bleed edge / final canvas boundary
- Trim line
- Safe / quiet area
- Page role label
- Page number / reading-order label

### Suggested Guide Styling

Use vector lines and text labels whenever possible.

Suggested labels:

- `BLEED EDGE / FINAL CANVAS`
- `TRIM: 6.69 in x 10.24 in`
- `SAFE AREA: keep text/logos/captions inside`
- `0.125 in BLEED`
- `0.25 in SAFE INSIDE TRIM`

Do not place essential text, logos, issue numbers, captions, credits, or page numbers outside the safe area.

Background art placeholders may extend through bleed.

---

## Resolution and Image Rules

The framework/template should use vector shapes and text whenever possible.

If any raster images are later placed into the template:

- Build/export at 300 dpi at final page size.
- Do not use artwork that ends up under 100 dpi at final placed size.
- Do not fake quality by upsampling low-resolution art.
- Background images intended to bleed should fill the entire 6.94 in x 10.49 in canvas.
- Text/logos/captions must remain inside the safe area.

For the first framework PDF, use placeholder boxes rather than low-resolution filler art.

---

## Required PDF Page Order

Output one print-ready PDF containing **24 single pages in reading order**.

| PDF Page | Comic Role |
|---:|---|
| 1 | Front cover |
| 2 | Inside front cover / credits page |
| 3 | Interior page 1 |
| 4 | Interior page 2 |
| 5 | Interior page 3 |
| 6 | Interior page 4 |
| 7 | Interior page 5 |
| 8 | Interior page 6 |
| 9 | Interior page 7 |
| 10 | Interior page 8 |
| 11 | Interior page 9 |
| 12 | Interior page 10 |
| 13 | Interior page 11 |
| 14 | Interior page 12 |
| 15 | Interior page 13 |
| 16 | Interior page 14 |
| 17 | Interior page 15 |
| 18 | Interior page 16 |
| 19 | Interior page 17 |
| 20 | Interior page 18 |
| 21 | Interior page 19 |
| 22 | Interior page 20 |
| 23 | Inside back cover / ad page |
| 24 | Back cover / back-story image page |

Do not export as printer spreads.

---

## Page 1: Front Cover Framework

### Required Areas

- Full-bleed main cover art placeholder.
- Title / logo area at top, inside safe area.
- Issue info / creator names area, inside safe area.
- Optional barcode / price placeholder, inside safe area unless printer requirements later specify otherwise.
- Visible trim, bleed, and safe-area guides.

### Suggested Labels

- `PAGE 1 / FRONT COVER`
- `FULL-BLEED COVER ART AREA`
- `TITLE / LOGO SAFE AREA`
- `ISSUE INFO / CREATOR NAMES`
- `OPTIONAL BARCODE / PRICE AREA`

### Comic Route Note

For the approved hype route, final cover art may use **Non-Canon Promo / Adaptation Art** and can symbolically show Red Umbrielor, Tenet, the formation, Rob, Horus, or Aeonos / Àæonos teaser imagery.

The framework PDF should use placeholders only unless final art is separately requested.

---

## Page 2: Inside Front Cover / Credits Page

### Required Credit Placeholders

Keep all credit text inside the safe area.

- Series title
- Issue number / date
- Writer
- Artist
- Colorist
- Letterer
- Editor
- Cover artist
- Publisher / imprint, if any
- Website / socials, optional
- Optional small logo area at bottom

### Suggested Labels

- `PAGE 2 / INSIDE FRONT COVER / CREDITS`
- `SERIES TITLE`
- `ISSUE NUMBER / DATE`
- `CREATOR CREDITS`
- `PUBLISHER / IMPRINT`
- `WEBSITE / SOCIALS`
- `OPTIONAL LOGO AREA`

### Optional Styling

This page may later be styled as a corrupted NCI / World Works field packet, but the first framework should keep the credits clean and readable.

---

## Pages 3-22: Interior Comic Page Frameworks

These 20 pages should support final comic storytelling or page-by-page layout experiments.

### Required Areas

- Full-bleed art background placeholder.
- Safe-area guide for speech bubbles, captions, sound effects, and essential art details.
- Flexible panel / content area.
- Optional page-number placeholder inside safe area.
- Reading-order page label.

### Suggested Labels

Each page should include:

- `PAGE [PDF PAGE] / INTERIOR PAGE [1-20]`
- `FULL-BLEED ART MAY EXTEND TO BLEED`
- `KEEP LETTERING INSIDE SAFE AREA`
- `FLEXIBLE PANEL / CONTENT AREA`
- `PAGE NUMBER PLACEHOLDER`

### Panel Guidance

The first framework PDF may use simple page framework boxes rather than story-specific paneling.

Do not lock final panel layouts unless a later task specifically requests story panel templates.

---

## Page 23: Inside Back Cover / Ad Page

This page should function as an ad framework and production reference.

### Required Ad Options

Clearly mark both ad options with dimension labels:

1. **Full-page ad, trim area:** 6.69 in x 10.24 in
2. **Full-page ad, with bleed artwork:** 6.94 in x 10.49 in

### Required Note

Include this note inside the layout:

> Keep text/logos inside the safe area (0.25 in from trim). Backgrounds may extend to bleed.

### Suggested Labels

- `PAGE 23 / INSIDE BACK COVER / AD PAGE`
- `FULL-PAGE AD TRIM AREA: 6.69 in x 10.24 in`
- `FULL-PAGE AD WITH BLEED: 6.94 in x 10.49 in`
- `TEXT / LOGO SAFE AREA`

### Comic Route Note

For the approved hype route, this page may later become an in-world NCI recruitment / warning poster:

> Things are different On Traverse.

In the first framework PDF, keep it as an ad template unless requested otherwise.

---

## Page 24: Back Cover / Back-Story Image Page

### Required Areas

- Full-bleed single-image placeholder.
- Caption / teaser text placeholder inside safe area.
- Optional logo / website / socials placeholder inside safe area.
- Visible trim, bleed, and safe-area guides.

### Suggested Labels

- `PAGE 24 / BACK COVER / TEASER IMAGE`
- `FULL-BLEED BACK-STORY IMAGE AREA`
- `CAPTION / TEASER TEXT SAFE AREA`
- `OPTIONAL LOGO / WEBSITE AREA`

### Comic Route Note

For the approved hype route, this page may later show The House Ten Built with one light still burning.

Suggested teaser caption for later art pass:

> Rob did not die because he lost.  
> He died because he chose.

Label final art as **Non-Canon Promo / Adaptation Art** unless approved otherwise.

---

## File Output Target

When the framework PDF is generated, place it at:

`production/templates/mixam-us-standard-24-page-framework.pdf`

Recommended supporting build note:

`production/notes/template-build-log.md`

---

## Export Requirements

The final framework PDF should meet these requirements:

- 24 pages exactly.
- Single pages in reading order.
- Final page size including bleed: 6.94 in x 10.49 in.
- Trim: 6.69 in x 10.24 in.
- Bleed: 0.125 in on all sides.
- Safe area: 0.25 in inside trim.
- Important text/logos/captions inside safe area.
- 300 dpi target at final page size.
- No placed image below 100 dpi at final placed size.
- No low-resolution filler art.
- Visible framework guides unless hidden guides are requested.
- Cover, credits, interior, ad, and back-cover pages labeled correctly.
- No unauthorized main-canon changes.

---

## Related Sandbox Files

- `docs/comics/issue-01-hype-machine-route.md`
- `docs/comics/comic-only-continuity.md`
- `docs/comics/candidate-canon-log.md`
- `docs/comics/production-checklist.md`
