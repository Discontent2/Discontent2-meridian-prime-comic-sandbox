# Kavo "Forest" Rill First Test Print Checklist

**Room:** Meridian Prime Toy Development Room / Action Figure Prototype Lab  
**Folder:** `production/toy-prototypes/kavo-forest-rill/print-notes/`  
**Status:** First physical test-print checklist  
**Prototype Target:** 5-inch retro collector action figure  
**Canon Boundary:** Sandbox production file. Does not alter main canon.

---

## Purpose

This checklist defines the first physical test-print workflow for the Kavo "Forest" Rill action figure prototype.

Use it before printing the full figure. The first print should prove joint tolerances, hand grips, tail fit, head readability, and support strategy before committing to a full body batch.

---

## Prototype Safety Positioning

This is an adult collectible prototype workflow.

This prototype is not:

- intended for children
- safety-certified
- ready for sale
- approved for rough handling
- approved for mass production

3D printing safety requirements:

- [ ] Work in a ventilated area.
- [ ] Wear gloves when handling uncured resin.
- [ ] Avoid skin contact with uncured resin.
- [ ] Wear eye protection when clipping supports.
- [ ] Cure parts fully before sanding or extended handling.
- [ ] Control sanding dust.
- [ ] Wet-sand resin where appropriate.
- [ ] Dispose of resin waste safely according to local requirements.
- [ ] Keep uncured resin and fragile test parts away from children and pets.

---

## Do Not Print Full Prototype Until

- [ ] Model-sheet / sculpt brief is reviewed.
- [ ] Parts breakdown is reviewed.
- [ ] STL naming plan is followed.
- [ ] Joint tolerance coupons are exported.
- [ ] Support orientation notes are reviewed.
- [ ] Resin and printer settings are recorded.
- [ ] Test batch contents are chosen.
- [ ] Safety setup is ready.

---

## Recommended First Test Batch

Print the smallest useful batch first.

### Required First Batch

- [ ] Neck joint coupon: C10 / C15 / C20
- [ ] Shoulder joint coupon: C10 / C15 / C20
- [ ] Wrist joint coupon: C10 / C15 / C20
- [ ] Tail joint coupon: C10 / C15 / C20 / optional C25
- [ ] Standard grip cylinder
- [ ] Route probe grip test
- [ ] Black flag pole grip test
- [ ] Route-reader handle grip test
- [ ] One head test, shades version
- [ ] One gripping hand test
- [ ] One route probe
- [ ] One black Path flag marker
- [ ] One route-reader device

### Optional First Batch

- [ ] One route-goggles head test
- [ ] One tail test section
- [ ] One paint-rub sample joint

### Delay Until Later

- full torso
- full pelvis
- full legs
- full arms
- full assembled figure
- alternate hand set
- display base

---

## Pre-Print File Checklist

Before slicing:

- [ ] File names follow `kfr_[part-id]_[part-name]_[side-or-type]_[version]_[status].stl`.
- [ ] Units are millimeters.
- [ ] Parts are at intended print scale.
- [ ] Meshes are watertight.
- [ ] Normals face outward.
- [ ] No hidden debris geometry exists.
- [ ] Peg / socket clearances match file labels.
- [ ] Left / right identity is clear where relevant.
- [ ] Test coupons match production-like wall thickness.
- [ ] Support orientation follows support notes.
- [ ] Protected surfaces are support-free where possible.

---

## Print Setup Log

Record before printing:

```markdown
## Test Batch: KFR-FTP-[date]-[batch letter]

**Printer:**  
**Resin:**  
**Resin Mix Ratio:**  
**Layer Height:**  
**Normal Exposure:**  
**Bottom Exposure:**  
**Lift Speed / Settings:**  
**Slicer:**  
**Supports:**  
**Orientation Notes:**  
**Wash Method and Time:**  
**Cure Method and Time:**  
**Room Temperature:**  
**Notes:**  
```

Do not rely on memory. Resin goblins thrive in undocumented settings.

---

## Support Review Before Print

Check each item:

- [ ] Face is protected from support marks.
- [ ] Shades / goggles lenses are protected.
- [ ] Head socket is supported.
- [ ] Shoulder pegs are supported.
- [ ] Wrist pegs and sockets are supported.
- [ ] Tail peg and socket coupon are supported.
- [ ] Hand grip interior is protected.
- [ ] Route-reader screen face is protected.
- [ ] Flag face is protected.
- [ ] Flag pole has enough supports.
- [ ] Route probe has enough supports to prevent warping.
- [ ] Labels on coupons are readable or separately bag-labeled.

---

## Post-Print Handling Checklist

After printing:

- [ ] Wear gloves before touching uncured parts.
- [ ] Remove build plate carefully.
- [ ] Photograph parts on plate before removal.
- [ ] Wash according to resin workflow.
- [ ] Let parts dry before clipping supports if appropriate.
- [ ] Clip supports, do not twist fragile parts.
- [ ] Cure fully.
- [ ] Photograph cured parts before sanding.
- [ ] Bag and label all coupons immediately.
- [ ] Record any obvious warp, failure, or breakage.

---

## Raw Part Inspection

Inspect before assembly tests:

- [ ] No uncured resin remains trapped.
- [ ] Parts are fully cured.
- [ ] Labels are readable or manually logged.
- [ ] Pegs are not cracked.
- [ ] Sockets are not ovalized.
- [ ] Hand grip cavity is clear.
- [ ] Route probe is straight enough to test.
- [ ] Flag pole survived support removal.
- [ ] Route-reader handle survived support removal.
- [ ] Head expression is readable at shelf distance.
- [ ] Shades are intact.
- [ ] Quills are intact.
- [ ] No part has sharp dangerous points that cannot be sanded.

---

## Joint Fit Test Order

Test in this order:

1. Neck C20, then C15, then C10.
2. Shoulder C20, then C15, then C10.
3. Wrist C20, then C15, then C10.
4. Tail C25 if printed, then C20, then C15, then C10.
5. Grip cylinder in hand.
6. Route probe in hand.
7. Black flag pole in hand.
8. Route-reader handle in hand.

Reason:

Start loose and move tighter to avoid cracking parts before learning the fit range.

---

## Raw Fit Pass / Fail Criteria

### Pass

- [ ] Part assembles without force.
- [ ] Part holds without falling out.
- [ ] Joint moves or removes as intended.
- [ ] No cracking or stress whitening appears.
- [ ] Fit feels repeatable.

### Conditional Pass

- [ ] Part needs light sanding only.
- [ ] Part is slightly tight but safe.
- [ ] Part is slightly loose but paint may improve fit.
- [ ] Fit works but needs geometry adjustment before full body print.

### Fail

- [ ] Peg cracks.
- [ ] Socket splits.
- [ ] Part cannot seat.
- [ ] Part falls out immediately.
- [ ] Fit requires unsafe force.
- [ ] Accessory breaks during grip test.
- [ ] Hand cannot hold any core accessory.

---

## 20-Cycle Handling Test

For each passing or conditional passing joint:

- [ ] Assemble and remove or rotate 20 times.
- [ ] Check for cracks.
- [ ] Check for stress whitening.
- [ ] Check for peg deformation.
- [ ] Check for socket widening.
- [ ] Record looseness after cycle 20.

Pass standard:

- no cracking
- no severe stress marks
- joint still holds after cycle 20

---

## Head Readability Test

Evaluate the head print at three distances:

- [ ] 3 feet: silhouette reads as Kavo / Velocisapien.
- [ ] 1 foot: brow, snout, shades, and quill crest read clearly.
- [ ] close inspection: support scars are manageable.

Head fail conditions:

- face support scars dominate expression
- shades are too fragile
- quills snap easily
- head looks animalistic or monster-only
- expression loses relaxed menace

---

## Accessory Handling Test

### Route Probe

- [ ] Probe prints straight enough.
- [ ] Probe tip is blunt.
- [ ] Grip fits hand.
- [ ] Probe does not read as spear first.

### Black Path Flag Marker

- [ ] Pole survives support removal.
- [ ] Pole fits hand.
- [ ] Flag face remains clean enough to paint matte black.
- [ ] Stake tip is not sharp.

### Route-Reader Device

- [ ] Handle fits hand.
- [ ] Screen face is clean enough to paint.
- [ ] Device reads as field tool, not weapon.
- [ ] Buttons / gauge details did not become brittle crumbs.

---

## Balance Preview Test

If tail or lower-body test parts are available:

- [ ] Check tail weight against planned pelvis socket.
- [ ] Check whether tail curve supports a tripod stance.
- [ ] Check foot footprint against figure scale.
- [ ] Flag any backward tipping risk.

If no lower body has printed yet, note balance risks for the next batch.

---

## Failure Photography Checklist

Photograph failures immediately.

Required views:

- [ ] whole failed part
- [ ] close-up of failure point
- [ ] support side
- [ ] protected surface side
- [ ] peg or socket close-up
- [ ] accessory grip close-up if relevant
- [ ] comparison with successful clearance variant if available

Name photos consistently:

`kfr_ftp_[date]_[part]_[failure-type]_[view].jpg`

---

## Test Result Table

Use this table in a future batch log:

```markdown
| Part / Coupon | Variant | Raw Fit | 20-Cycle Result | Surface Quality | Verdict | Notes |
|---|---|---|---|---|---|---|
| Neck | C10 |  |  |  |  |  |
| Neck | C15 |  |  |  |  |  |
| Neck | C20 |  |  |  |  |  |
| Shoulder | C10 |  |  |  |  |  |
| Shoulder | C15 |  |  |  |  |  |
| Shoulder | C20 |  |  |  |  |  |
| Wrist | C10 |  |  |  |  |  |
| Wrist | C15 |  |  |  |  |  |
| Wrist | C20 |  |  |  |  |  |
| Tail | C15 |  |  |  |  |  |
| Tail | C20 |  |  |  |  |  |
| Grip Cylinder | Standard |  |  |  |  |  |
| Route Probe | Standard |  |  |  |  |  |
```

---

## Go / No-Go Criteria for Full Prototype Print

### Go

Proceed to full prototype print only if:

- [ ] Neck tolerance is selected.
- [ ] Shoulder tolerance is selected.
- [ ] Wrist or fixed-hand plan is selected.
- [ ] Tail socket tolerance is selected.
- [ ] Standard grip size is selected.
- [ ] Head support strategy works.
- [ ] Hand grip strategy works.
- [ ] Route probe, flag marker, and route-reader are printable.
- [ ] No required detail is too fragile.
- [ ] Failure risks are logged.

### No-Go

Do not print full prototype if:

- [ ] Tail peg fails.
- [ ] Head expression is damaged by supports.
- [ ] Hand cannot hold core accessories.
- [ ] Wrist pegs crack repeatedly.
- [ ] Flag pole or route probe cannot survive handling.
- [ ] Resin settings are inconsistent or undocumented.
- [ ] Sockets split during raw fit.
- [ ] Figure balance risk is unresolved.

---

## Immediate Revision Actions

If tests fail:

- Tail peg fails: thicken peg, widen socket wall, try tough resin, reprint tail coupon.
- Head support scars fail: reorient head and move supports to rear / underside.
- Hand grip fails: adjust grip diameter or hand pose, reprint grip coupon.
- Wrist fails: switch to fixed hands for prototype one or thicken wrist peg.
- Flag pole fails: thicken pole, ovalize profile, print multiples.
- Route probe warps: thicken shaft or adjust orientation and supports.
- Paint rub is predicted: increase clearance or mask joint surfaces during paint.

---

## Next Production File

Recommended next file:

`production/toy-prototypes/kavo-forest-rill/print-notes/kavo-forest-rill-test-log-batch-a.md`

Purpose:

Create the reusable log template for the first actual print batch, including printer settings, resin settings, coupon outcomes, photo references, fit verdicts, and revision decisions.
