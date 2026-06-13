# Kavo "Forest" Rill Joint Tolerance Test Plan

**Room:** Meridian Prime Toy Development Room / Action Figure Prototype Lab  
**Folder:** `production/toy-prototypes/kavo-forest-rill/print-notes/`  
**Status:** First-pass joint-fit and grip-fit test plan  
**Prototype Target:** 5-inch retro collector action figure  
**Canon Boundary:** Sandbox production file. Does not alter main canon.

---

## Purpose

This file defines the test coupons, clearance ladder, labeling system, resin notes, and pass / fail criteria needed before printing the full Kavo "Forest" Rill action figure prototype.

The goal is to test the boring little pegs before they become expensive little heartbreaks.

---

## Safety Positioning

This is an adult collectible prototype workflow.

3D printing safety requirements:

- use ventilation
- wear gloves when handling uncured resin
- avoid skin contact with uncured resin
- wear eye protection when clipping supports or sanding
- cure parts properly
- control sanding dust
- wet-sand where appropriate
- do not let children handle uncured resin, test coupons, or fragile printed parts

---

## Core Test Philosophy

Test joints and grips before the full figure.

Do not judge fit from digital dimensions alone. Resin type, printer calibration, exposure, wash time, cure time, and sanding all change the final feel.

Each test should answer:

- Does it assemble without cracking?
- Does it hold without drooping?
- Can it rotate or remove as intended?
- Does paint or sealant ruin the fit?
- Does the part survive repeated handling?

---

## Required Test Coupons

Create separate small test files for these features:

| Coupon ID | Test Area | Purpose |
|---|---|---|
| JT-01 | Neck peg / socket | Test head swivel or simple ball fit. |
| JT-02 | Shoulder peg / socket | Test arm rotation and socket wall strength. |
| JT-03 | Wrist peg / socket | Test swappable or swivel hand fit. |
| JT-04 | Hip peg / socket | Test leg fit and stance stability. |
| JT-05 | Tail peg / socket | Test keyed removable or swivel-ready tail fit. |
| JT-06 | Standard grip cylinder | Test gripping hand size. |
| JT-07 | Route-reader handle | Test device grip and hand clearance. |
| JT-08 | Black flag pole grip | Test flag marker handle durability. |
| JT-09 | Route probe grip | Test route probe handle and claw clearance. |
| JT-10 | Paint-rub sample joint | Test primer, paint, sealant, and movement tolerance. |

---

## Clearance Ladder

Print at least three clearance variants for each socketed joint:

| Clearance Code | Clearance | Use Case |
|---|---:|---|
| C10 | 0.10 mm | Tight fit test. May require sanding. |
| C15 | 0.15 mm | Medium fit test. Recommended starting point. |
| C20 | 0.20 mm | Loose fit test. Useful after paint / sealant. |

Optional additional variants:

| Clearance Code | Clearance | Use Case |
|---|---:|---|
| C25 | 0.25 mm | If resin swelling or paint buildup is high. |
| C30 | 0.30 mm | Emergency loose test for larger pegs only. |

Recommended first ladder:

- neck: C10, C15, C20
- shoulder: C10, C15, C20
- wrist: C10, C15, C20
- hip: C10, C15, C20
- tail: C10, C15, C20, optional C25

---

## Coupon Labeling System

Each coupon should include raised or engraved text if possible.

Format:

`KFR-[joint]-[clearance]-[resin/test batch]`

Examples:

- `KFR-NECK-C15-A`
- `KFR-SHLDR-C20-A`
- `KFR-WRIST-C10-A`
- `KFR-TAIL-C25-B`
- `KFR-GRIP-PROBE-A`

If printed text is too small, label parts immediately after curing using a paint marker or bag labels.

---

## Suggested Coupon Dimensions

Exact dimensions depend on sculpt scale, but test coupons should use production-like peg diameters and wall thickness.

Recommended minimum data per coupon:

- peg diameter
- peg length
- socket depth
- socket wall thickness
- clearance code
- resin type
- printer profile
- orientation
- cure time

Do not make abstract test pegs that are stronger than the real figure. Coupons should mimic the final part's wall thickness and support direction.

---

## Grip Test Standard

Define one shared accessory grip standard for first prototype tools.

Recommended grip tests:

- round grip cylinder
- slightly flattened grip cylinder
- route-reader side handle
- flag pole grip
- route probe grip

Grip test questions:

- Can the hand hold the accessory without stress whitening or cracking?
- Do claws collide with the grip?
- Can the accessory be inserted after paint?
- Does the hand look too oversized or too delicate?
- Does the handle read as field-tool scale, not toothpick scale?

---

## Resin Test Variables

Record these for every coupon batch:

| Field | Notes |
|---|---|
| Printer | Machine name / model. |
| Resin | Brand, type, color, mix ratio if blended. |
| Layer height | Example: 0.05 mm. |
| Exposure settings | Include normal and bottom exposure. |
| Orientation | Describe or screenshot orientation. |
| Support density | Light, medium, heavy, custom. |
| Wash time | Total wash duration and solvent type. |
| Cure time | Total UV cure duration and method. |
| Post-processing | Sanding, drilling, heat, lubricant, etc. |
| Result | Pass, conditional pass, fail. |

---

## Pass / Fail Criteria

### Neck Joint

Pass if:

- head attaches without cracking
- head can rotate enough for a sly side glance
- head does not wobble excessively
- joint does not scrape visible paint areas too severely

Fail if:

- neck peg snaps
- head cannot seat fully
- head falls off under light handling
- joint is so tight it risks breaking during assembly

---

### Shoulder Joint

Pass if:

- arm rotates forward and backward
- shoulder holds route-readiness pose
- socket wall does not crack
- harness does not block useful movement

Fail if:

- arm droops under its own weight
- shoulder peg fractures
- socket splits
- arm cannot clear harness or torso shape

---

### Wrist Joint

Pass if:

- hand can swivel or be swapped without cracking
- gripping hand holds route probe or route-reader
- wrist wrap hides seam reasonably well

Fail if:

- wrist peg is too small to survive handling
- hand falls out while holding accessory
- claws collide with accessory handle

---

### Hip Joint

Pass if:

- legs attach securely
- figure can stand in relaxed neutral stance
- hip rotation does not destabilize figure
- legs do not wobble under body weight

Fail if:

- figure cannot stand
- hip socket cracks
- legs splay unpredictably
- pelvis wall is too thin

---

### Tail Joint

Pass if:

- tail seats securely
- tail assists balance
- keyed shape prevents wrong orientation
- tail can be removed without tearing socket
- tail does not droop if swivel-ready

Fail if:

- tail falls out
- tail peg snaps
- socket cracks
- tail forces figure backward
- tail reads as plugged-on rather than anatomical

---

## Paint and Sealant Fit Test

At least one coupon per joint type should be primed, painted, sealed, and retested.

Paint test sequence:

1. Test raw fit.
2. Prime parts.
3. Test fit after primer.
4. Paint parts.
5. Test fit after paint.
6. Seal parts.
7. Test final fit.
8. Rotate or remove part 20 times.
9. Record paint rub and joint looseness.

This prevents the classic tragedy of a perfect raw fit becoming a crunchy painted fossil.

---

## Handling Cycle Test

For each passing coupon, perform 20 careful assembly / movement cycles.

Record:

- cracking
- stress whitening
- looseness
- paint rub
- squeaking / binding
- peg deformation
- socket widening

Pass standard:

- no cracks
- no severe stress marks
- joint still holds after 20 cycles

---

## Test Log Template

Use this format in future print logs:

```markdown
## Test Batch: KFR-JT-[date]-[batch letter]

**Printer:**  
**Resin:**  
**Layer Height:**  
**Exposure:**  
**Wash Time:**  
**Cure Time:**  
**Orientation:**  
**Support Notes:**  

| Coupon | Clearance | Raw Fit | Painted Fit | 20-Cycle Result | Verdict | Notes |
|---|---:|---|---|---|---|---|
| KFR-NECK-C10-A | 0.10 mm |  |  |  |  |  |
| KFR-NECK-C15-A | 0.15 mm |  |  |  |  |  |
| KFR-NECK-C20-A | 0.20 mm |  |  |  |  |  |
```

---

## Recommended First Batch

Print these first:

- neck C10 / C15 / C20
- shoulder C10 / C15 / C20
- wrist C10 / C15 / C20
- tail C10 / C15 / C20 / C25
- standard grip cylinder
- route probe grip
- flag pole grip

Delay hip testing until the pelvis block dimensions are drafted, unless the sculptor already has the hip system blocked.

---

## Production Decision Rules

Use results this way:

- If C10 cracks or requires force, reject for first prototype.
- If C15 holds and rotates without sanding, use as baseline.
- If C20 is loose raw but good after paint, mark for painted joints.
- If paint destroys fit, adjust socket clearance or mask joint surfaces during painting.
- If a joint only works with heavy sanding, revise the digital joint.
- If tail joint passes raw but fails balance, revise tail curve or foot stance.

---

## Output Files to Create Later

Recommended future files in `print-notes/`:

- `kavo-forest-rill-joint-test-log-batch-a.md`
- `kavo-forest-rill-resin-settings.md`
- `kavo-forest-rill-support-orientation-notes.md`
- `kavo-forest-rill-first-test-print-results.md`

---

## Next Production File

Recommended next file:

`production/toy-prototypes/kavo-forest-rill/sculpt-notes/kavo-forest-rill-stl-planning-notes.md`

Purpose:

Define the planned STL / 3MF asset list, naming convention, export scale, origin points, mirrored parts policy, and sculpt-to-print handoff requirements.
