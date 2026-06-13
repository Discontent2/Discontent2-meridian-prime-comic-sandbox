# Kavo "Forest" Rill STL Planning Notes

**Room:** Meridian Prime Toy Development Room / Action Figure Prototype Lab  
**Folder:** `production/toy-prototypes/kavo-forest-rill/sculpt-notes/`  
**Status:** First-pass STL / 3MF asset planning and handoff notes  
**Prototype Target:** 5-inch retro collector action figure  
**Canon Boundary:** Sandbox production file. Does not alter main canon.

---

## Purpose

This file defines the planned STL / 3MF asset list, naming convention, export scale, origin-point logic, mirrored-parts policy, and sculpt-to-print handoff requirements for the Kavo "Forest" Rill prototype.

The goal is to keep every digital part findable, printable, testable, and revision-friendly.

---

## Export Philosophy

Every exported part should answer four questions:

1. What is this part?
2. What version is this part?
3. Is it left, right, centered, alternate, or accessory?
4. Is it sculpt-review, test-print, or production-test ready?

No mystery chunks. No `final_final_REAL_tail_2.stl` goblin behavior.

---

## Scale Standard

**Figure scale:** 5 inches tall, measured from bottom of feet to top of head / quill silhouette in neutral standing pose.

**Units:** millimeters.

**Export rule:** all sculpt and print files should export at real intended print scale.

Recommended scale checks:

- overall figure height: approx. 127 mm
- head size: verify against full-body sheet before export
- hand grip diameter: consistent with grip test coupon
- tail length: balanced for shelf stance, not arbitrary
- feet footprint: wide enough for neutral standing pose

---

## Coordinate and Origin Rules

Use consistent origin points so parts do not become digital confetti.

Recommended origin logic:

| Asset Type | Origin Recommendation |
|---|---|
| Full figure reference mesh | Centered between feet at ground plane. |
| Head | Center at neck joint axis. |
| Torso | Center at neck / torso vertical axis, ground-independent. |
| Pelvis | Center at hip axis. |
| Arms | Center at shoulder peg axis. |
| Hands | Center at wrist peg axis. |
| Legs | Center at hip peg axis or foot-ground alignment marker. |
| Tail | Center at tail peg axis. |
| Accessories | Center at grip axis or functional center. |
| Test coupons | Centered on part geometry, label facing up. |

For assembly reference, also export one non-printing aligned assembly scene in the sculpt source file.

---

## File Naming Convention

Recommended format:

`kfr_[part-id]_[part-name]_[side-or-type]_[version]_[status].stl`

Examples:

- `kfr_p01_head_shades_v001_sculptreview.stl`
- `kfr_p02_torso_center_v001_testprint.stl`
- `kfr_p03_pelvis_center_v001_testprint.stl`
- `kfr_p04_arm_left_v001_testprint.stl`
- `kfr_p05_arm_right_v001_testprint.stl`
- `kfr_p06_hand_left_grip_v001_testprint.stl`
- `kfr_p07_hand_right_grip_v001_testprint.stl`
- `kfr_p10_tail_keyed_v001_testprint.stl`
- `kfr_p11_route-reader_accessory_v001_testprint.stl`

Use lowercase file names with hyphens only inside descriptive part names when needed.

---

## Status Tags

Use one of these status tags:

| Status Tag | Meaning |
|---|---|
| `blockout` | Rough shape only. Not for print. |
| `sculptreview` | Visual review mesh. May not be print-ready. |
| `jointtest` | Test coupon or joint-fit asset. |
| `testprint` | Printable prototype test file. |
| `painttest` | Intended for paint / finish testing. |
| `productiontest` | Final-ish prototype print test. |
| `archive` | Retired but preserved for reference. |

Do not label anything `final` until a physical printed and painted prototype has passed review.

---

## Planned STL Asset List

### Core Body Parts

| Part ID | Export Name Seed | Required | Notes |
|---|---|---:|---|
| P-01 | `kfr_p01_head_shades` | Yes | Primary head with sculpted black-frame shades. |
| P-02 | `kfr_p02_torso_center` | Yes | Torso with route harness and badge cluster. |
| P-03 | `kfr_p03_pelvis_center` | Yes | Hip support and tail socket. |
| P-04 | `kfr_p04_arm_left` | Yes | Left full arm if no elbow joint. |
| P-05 | `kfr_p05_arm_right` | Yes | Right full arm if no elbow joint. |
| P-06 | `kfr_p06_hand_left_grip` | Yes | Four-fingered clawed hand. |
| P-07 | `kfr_p07_hand_right_grip` | Yes | Four-fingered clawed hand. |
| P-08 | `kfr_p08_leg_left` | Yes | Integrated broad four-toed foot. |
| P-09 | `kfr_p09_leg_right` | Yes | Integrated broad four-toed foot. |
| P-10 | `kfr_p10_tail_keyed` | Yes | Keyed removable or swivel-ready tail. |

### Optional / Alternate Parts

| Part ID | Export Name Seed | Required | Notes |
|---|---|---:|---|
| P-14 | `kfr_p14_head_goggles` | Optional | Alternate route goggles head. |
| P-15 | `kfr_p15_field-pack` | Optional | Separate only if not sculpted onto torso. |
| P-16 | `kfr_p16_emt-pouch` | Optional | Separate only if paint or fit requires it. |
| P-17 | `kfr_p17_hand-alt` | Optional | Alternate hand set after grip tests. |
| P-18 | `kfr_p18_display-base` | Optional | Use only if balance requires support. |

### Accessories

| Part ID | Export Name Seed | Required | Notes |
|---|---|---:|---|
| P-11 | `kfr_p11_route-reader` | Yes | Handheld route-reader / GPR device. |
| P-12 | `kfr_p12_black-path-flag` | Yes | Thickened pole and flag. |
| P-13 | `kfr_p13_route-probe` | Yes | Blunt field-tool probe. |

### Test Coupons

| Coupon ID | Export Name Seed | Required | Notes |
|---|---|---:|---|
| JT-01 | `kfr_jt01_neck` | Yes | C10 / C15 / C20 variants. |
| JT-02 | `kfr_jt02_shoulder` | Yes | C10 / C15 / C20 variants. |
| JT-03 | `kfr_jt03_wrist` | Yes | C10 / C15 / C20 variants. |
| JT-04 | `kfr_jt04_hip` | Yes | C10 / C15 / C20 variants. |
| JT-05 | `kfr_jt05_tail` | Yes | C10 / C15 / C20 / optional C25. |
| JT-06 | `kfr_jt06_grip-cylinder` | Yes | Shared grip standard. |
| JT-07 | `kfr_jt07_route-reader-handle` | Yes | Grip and claw clearance. |
| JT-08 | `kfr_jt08_flag-pole-grip` | Yes | Flag marker handle durability. |
| JT-09 | `kfr_jt09_route-probe-grip` | Yes | Probe handle and claw clearance. |
| JT-10 | `kfr_jt10_paint-rub` | Yes | Paint and sealant fit test. |

---

## Clearance Variant Naming

For test coupons, add clearance code before status tag.

Examples:

- `kfr_jt01_neck_c10_v001_jointtest.stl`
- `kfr_jt01_neck_c15_v001_jointtest.stl`
- `kfr_jt01_neck_c20_v001_jointtest.stl`
- `kfr_jt05_tail_c25_v001_jointtest.stl`

Clearance codes:

- `c10` = 0.10 mm
- `c15` = 0.15 mm
- `c20` = 0.20 mm
- `c25` = 0.25 mm
- `c30` = 0.30 mm, emergency loose test only

---

## Mirrored Parts Policy

Do not rely on slicer mirroring for the final handoff unless explicitly noted.

Export left and right parts separately when:

- sculpt details are asymmetrical
- wraps differ
- accessory grip differs
- hand posing differs
- badge or harness details cross the shoulder or wrist area

Mirroring allowed only for early blockout:

- arms during rough proportion tests
- legs during rough stance tests
- blank hands before grip detail

Final export should include actual left and right files.

---

## Watertight Mesh Requirements

Before exporting printable files:

- mesh must be watertight
- normals should face outward
- no non-manifold edges
- no floating hidden geometry
- no paper-thin surfaces
- sockets should have real wall thickness
- pegs should be physically printable
- accessories should be one-piece unless intentionally split
- scale texture should not create accidental fragile flakes

Run mesh repair or validation before sending to slicer.

---

## Detail Separation Rules

Sculpted detail should be divided into three tiers:

### Tier 1: Must Print Clearly

- head / snout / brow expression
- red proto-quill mohawk shape
- four-finger hand structure
- four-toed feet
- tail curve
- route harness
- shades or goggles silhouette

### Tier 2: Should Print Clearly

- claw-wraps
- badge cluster
- checker trim zone
- EMT pouch
- route-reader screen shape
- black Path flag
- route probe grip

### Tier 3: Paint or Texture Optional

- tiny scratches
- micro scale variation
- small badge symbols
- route-reader screen graphics
- cloth weave
- minute buckle scratches

If a Tier 3 detail threatens printability, remove it or convert it into paint guidance.

---

## 3MF Bundle Recommendation

In addition to separate STL files, create a 3MF bundle for each test batch when possible.

Suggested bundles:

- `kfr_joint-test-batch-a_v001.3mf`
- `kfr_core-body-test_v001.3mf`
- `kfr_accessory-test_v001.3mf`
- `kfr_full-prototype-test_v001.3mf`

Bundle notes should include:

- intended printer profile
- resin type
- support strategy
- orientation screenshots if possible
- parts included
- date exported

---

## Sculpt Source File Handoff

The sculptor should provide source files in addition to STL / 3MF exports.

Recommended source handoff:

- Blender `.blend`, ZBrush `.ztl`, Nomad source, or equivalent
- separated named objects matching STL names
- visible scale reference ruler
- neutral assembled model
- exploded parts layout
- hidden backup mesh layers clearly labeled
- articulation axes or helper objects retained
- notes on any non-print-ready decorative layers

---

## Folder Placement Recommendation

Until actual STL files exist, keep this file in:

`production/toy-prototypes/kavo-forest-rill/sculpt-notes/`

When actual mesh exports are added later, recommended folders:

```text
production/toy-prototypes/kavo-forest-rill/stl/
production/toy-prototypes/kavo-forest-rill/3mf/
production/toy-prototypes/kavo-forest-rill/source-files/
production/toy-prototypes/kavo-forest-rill/test-coupons/
```

Do not add binary model files unless the repo storage plan is approved.

---

## Export Checklist

Before a file is handed to print testing:

- [ ] file name follows convention
- [ ] scale is millimeters
- [ ] part is at intended print scale
- [ ] mesh is watertight
- [ ] normals are correct
- [ ] no hidden debris geometry
- [ ] peg / socket clearance matches label
- [ ] left / right part identity is clear
- [ ] part has status tag
- [ ] source file contains matching named object
- [ ] slicer screenshot or orientation note exists
- [ ] export version is recorded

---

## Review Gates

### Gate 1: Digital Blockout Review

Approve:

- silhouette
- canon markers
- scale
- tail balance concept
- part separation proposal

### Gate 2: Joint Coupon Export

Approve:

- coupon naming
- clearance ladder
- peg and socket geometry
- resin test plan

### Gate 3: First Printable Parts

Approve:

- head
- torso
- pelvis
- tail
- hands
- route probe
- route-reader
- black Path flag marker

### Gate 4: Full Prototype Test Export

Approve:

- all parts align
- figure stands in digital assembly
- accessory grips match
- mesh validation passes
- file names and versions are clean

---

## Next Production File

Recommended next file:

`production/toy-prototypes/kavo-forest-rill/print-notes/kavo-forest-rill-support-orientation-notes.md`

Purpose:

Define print orientation, support placement rules, surface-protection zones, and risk areas for each body part and accessory before slicing.
