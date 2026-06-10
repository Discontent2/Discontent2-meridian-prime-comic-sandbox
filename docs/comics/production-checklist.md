# Production Checklist

> Preflight checklist for Meridian Prime comic template PDFs and future print-ready comic files.

**Sandbox Status:** ACTIVE PRODUCTION CHECKLIST

**Canon Status:** SANDBOX PRODUCTION DOCUMENT. This checklist validates print readiness only. It does not establish story canon.

---

## Repository Quarantine Check

- [ ] Main canon repo was not modified: `Discontent2/meridian-prime`
- [ ] All generated comic production files live in the sandbox repo: `Discontent2/Discontent2-meridian-prime-comic-sandbox`
- [ ] Any adaptation, promo, or comic-only invention is labeled clearly.
- [ ] Any possible main-canon improvement is logged in `docs/comics/candidate-canon-log.md`.

---

## Required Output File

Expected PDF path:

`production/templates/mixam-us-standard-24-page-framework.pdf`

Optional supporting build log:

`production/notes/template-build-log.md`

---

## Core Print Checklist

- [ ] PDF contains exactly **24 pages**.
- [ ] Page count is a multiple of 4.
- [ ] Pages are exported as **single pages in reading order**.
- [ ] PDF is not exported as printer spreads.
- [ ] Binding assumption is staple-bound / saddle-stitch.
- [ ] Printing assumption is double-sided.
- [ ] Cover count is 4 pages.
- [ ] Interior count is 20 pages.

---

## Page Size Checklist

Physical inch measurements are the source of truth.

- [ ] Final page canvas including bleed is **6.94 in x 10.49 in**.
- [ ] Trim size is **6.69 in x 10.24 in**.
- [ ] Bleed is **0.125 in** on all sides.
- [ ] Safe / quiet area is **0.25 in inside trim** on all sides.
- [ ] Important elements are at least **0.375 in from the final canvas edge**.
- [ ] 300 dpi reference canvas is approximately **2082 px x 3147 px**.
- [ ] Trim reference is approximately **2007 px x 3072 px**.
- [ ] Bleed reference is approximately **37.5 px** on each side.
- [ ] Safe area begins approximately **112.5 px** from the final canvas edge.

---

## Guide / Template Layer Checklist

- [ ] Bleed edge / final canvas boundary is visible or documented.
- [ ] Trim line is visible or documented.
- [ ] Safe area is visible or documented.
- [ ] Each page has a clear page-role label.
- [ ] Each page has a reading-order page number or role label.
- [ ] Guide labels do not obscure template purpose.
- [ ] All guide text stays inside the page canvas.
- [ ] No critical template instruction is outside the safe area unless it is purely a production guide.

---

## Page Order Checklist

- [ ] Page 1 = Front cover.
- [ ] Page 2 = Inside front cover / credits page.
- [ ] Page 3 = Interior page 1.
- [ ] Page 4 = Interior page 2.
- [ ] Page 5 = Interior page 3.
- [ ] Page 6 = Interior page 4.
- [ ] Page 7 = Interior page 5.
- [ ] Page 8 = Interior page 6.
- [ ] Page 9 = Interior page 7.
- [ ] Page 10 = Interior page 8.
- [ ] Page 11 = Interior page 9.
- [ ] Page 12 = Interior page 10.
- [ ] Page 13 = Interior page 11.
- [ ] Page 14 = Interior page 12.
- [ ] Page 15 = Interior page 13.
- [ ] Page 16 = Interior page 14.
- [ ] Page 17 = Interior page 15.
- [ ] Page 18 = Interior page 16.
- [ ] Page 19 = Interior page 17.
- [ ] Page 20 = Interior page 18.
- [ ] Page 21 = Interior page 19.
- [ ] Page 22 = Interior page 20.
- [ ] Page 23 = Inside back cover / ad page.
- [ ] Page 24 = Back cover / back-story image page.

---

## Page 1: Front Cover Checklist

- [ ] Page is labeled `PAGE 1 / FRONT COVER`.
- [ ] Full-bleed cover art placeholder extends to bleed.
- [ ] Title / logo placeholder is inside safe area.
- [ ] Issue info / creator names placeholder is inside safe area.
- [ ] Optional barcode / price area is inside safe area unless printer rules later require otherwise.
- [ ] Trim, bleed, and safe-area guides are visible.
- [ ] No final low-resolution art is used.

---

## Page 2: Inside Front Cover / Credits Checklist

- [ ] Page is labeled `PAGE 2 / INSIDE FRONT COVER / CREDITS`.
- [ ] Series title placeholder is inside safe area.
- [ ] Issue number / date placeholder is inside safe area.
- [ ] Writer placeholder is inside safe area.
- [ ] Artist placeholder is inside safe area.
- [ ] Colorist placeholder is inside safe area.
- [ ] Letterer placeholder is inside safe area.
- [ ] Editor placeholder is inside safe area.
- [ ] Cover artist placeholder is inside safe area.
- [ ] Publisher / imprint placeholder is inside safe area.
- [ ] Website / socials placeholder is inside safe area, if included.
- [ ] Optional logo area is inside safe area.

---

## Pages 3-22: Interior Page Checklist

For each interior page:

- [ ] Page is labeled with PDF page number and interior page number.
- [ ] Full-bleed art background placeholder reaches bleed.
- [ ] Safe-area guide is visible.
- [ ] Flexible panel / content area is visible.
- [ ] Lettering reminder is included or otherwise documented.
- [ ] Optional page number placeholder is inside safe area.
- [ ] No critical text, captions, or speech bubbles fall outside safe area.
- [ ] No final low-resolution art is used.

Interior page mapping:

| PDF Page | Interior Page | Checked |
|---:|---:|---|
| 3 | 1 | [ ] |
| 4 | 2 | [ ] |
| 5 | 3 | [ ] |
| 6 | 4 | [ ] |
| 7 | 5 | [ ] |
| 8 | 6 | [ ] |
| 9 | 7 | [ ] |
| 10 | 8 | [ ] |
| 11 | 9 | [ ] |
| 12 | 10 | [ ] |
| 13 | 11 | [ ] |
| 14 | 12 | [ ] |
| 15 | 13 | [ ] |
| 16 | 14 | [ ] |
| 17 | 15 | [ ] |
| 18 | 16 | [ ] |
| 19 | 17 | [ ] |
| 20 | 18 | [ ] |
| 21 | 19 | [ ] |
| 22 | 20 | [ ] |

---

## Page 23: Inside Back Cover / Ad Page Checklist

- [ ] Page is labeled `PAGE 23 / INSIDE BACK COVER / AD PAGE`.
- [ ] Full-page ad trim area is labeled **6.69 in x 10.24 in**.
- [ ] Full-page ad with bleed area is labeled **6.94 in x 10.49 in**.
- [ ] Required note appears inside layout:

> Keep text/logos inside the safe area (0.25 in from trim). Backgrounds may extend to bleed.

- [ ] Text / logo safe area is clear.
- [ ] Any future in-world ad usage is labeled correctly as Adaptation Choice, Promo Exaggeration, or Comic-Only Continuity.

---

## Page 24: Back Cover / Back-Story Image Checklist

- [ ] Page is labeled `PAGE 24 / BACK COVER / TEASER IMAGE`.
- [ ] Full-bleed single-image placeholder extends to bleed.
- [ ] Caption / teaser text placeholder is inside safe area.
- [ ] Optional logo / website area is inside safe area.
- [ ] Trim, bleed, and safe-area guides are visible.
- [ ] Any future teaser art is labeled **Non-Canon Promo / Adaptation Art** unless approved otherwise.

---

## Raster Image / Resolution Checklist

For the framework PDF:

- [ ] Vector boxes and text are used wherever possible.
- [ ] Placeholder boxes are used instead of low-resolution filler images.
- [ ] No placed raster image is under 100 dpi at final placed size.
- [ ] No low-resolution art has been upsampled to fake print quality.
- [ ] Any full-bleed raster image fills the entire **6.94 in x 10.49 in** canvas.
- [ ] Any final placed art is suitable for 300 dpi output at final size.

---

## Story / Spoiler Checklist

For framework/template PDFs:

- [ ] No unauthorized main-canon spoilers are included.
- [ ] Hype-route material is clearly labeled if referenced.
- [ ] Non-canon promo imagery is labeled as non-canon.
- [ ] Candidate-canon inventions are logged before reuse as if official.
- [ ] The template does not redefine Tenet, Rob, Horus, Red Umbrielor, NCI, the pistol, Aeonos / Àæonos, species body plans, or the Core.

---

## Approved Hype Route Compatibility Checklist

If the framework is later adapted into the approved hype comic route:

- [ ] Rob's death-chain material is labeled as Adaptation Choice or Comic-Only Continuity if placed earlier than the novella reveal order.
- [ ] Door / hidden formation imagery is labeled Promo Exaggeration if shown early.
- [ ] Aeonos / Àæonos symbolic imagery does not collapse the distinction between worlds.
- [ ] The pistol is treated as inheritance / key / test / trust marker, not merely a weapon.
- [ ] Horus remains personal and tragic, not a generic villain.
- [ ] Tenet remains practical and field-grounded.
- [ ] Red Umbrielor remains MMS Quadtrack 289.

---

## Final Preflight Sign-Off

Before delivering any PDF as print-ready:

- [ ] Page count confirmed: 24.
- [ ] Page order confirmed.
- [ ] Page size confirmed: 6.94 in x 10.49 in including bleed.
- [ ] Trim confirmed: 6.69 in x 10.24 in.
- [ ] Bleed confirmed: 0.125 in on all sides.
- [ ] Safe area confirmed: 0.25 in inside trim.
- [ ] Important text/logos/captions confirmed inside safe area.
- [ ] Single-page export confirmed.
- [ ] 300 dpi target confirmed.
- [ ] Image resolution check completed.
- [ ] No low-resolution filler art.
- [ ] Cover and interior labels confirmed.
- [ ] Ad page dimensions confirmed.
- [ ] Back cover teaser placeholder confirmed.
- [ ] Quarantine labels confirmed.
- [ ] Main repo untouched.

---

## Related Sandbox Files

- `docs/comics/mixam-24-page-template-spec.md`
- `docs/comics/issue-01-hype-machine-route.md`
- `docs/comics/comic-only-continuity.md`
- `docs/comics/candidate-canon-log.md`
