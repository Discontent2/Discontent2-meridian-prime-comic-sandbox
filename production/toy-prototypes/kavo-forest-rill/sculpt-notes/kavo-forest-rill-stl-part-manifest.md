# Kavo "Forest" Rill STL Part Manifest / Sculpt Export Checklist

**Room:** Meridian Prime Toy Development Room / Action Figure Prototype Lab  
**Prototype:** Kavo "Forest" Rill 5-inch adult collectible action figure  
**File Type:** STL / 3MF sculpt export manifest and checklist  
**Status:** First export manifest template  
**Canon Boundary:** Sandbox production record. Does not alter main canon.

---

## Purpose

Use this manifest to track every sculpted part from blockout through STL / 3MF export, joint coupon testing, first full print, paint testing, and revision.

This file is the bridge between sculpt notes and print logs. If a part does not appear here, it should not wander into the slicer like an unsupervised resin cryptid.

---

## Required Companion Files

Use this manifest with:

- `production/toy-prototypes/kavo-forest-rill/sculpt-notes/kavo-forest-rill-sculptor-parts-articulation-packet.md`
- `docs/toy-development/kavo-forest-rill-3d-print-plan.md`
- `production/toy-prototypes/kavo-forest-rill/print-notes/kavo-forest-rill-joint-test-coupon-log.md`
- `production/toy-prototypes/kavo-forest-rill/print-notes/kavo-forest-rill-support-orientation-notes.md`
- `production/toy-prototypes/kavo-forest-rill/print-notes/kavo-forest-rill-first-test-print-log.md`
- `production/toy-prototypes/kavo-forest-rill/print-notes/kavo-forest-rill-failure-and-revision-log.md`
- `docs/toy-development/kavo-forest-rill-paint-guide.md`

---

## Export Standards

| Field | Standard |
|---|---|
| Figure scale | 5-inch / 127 mm adult collectible prototype target |
| Units | Millimeters |
| Preferred export | STL for print test, 3MF if color / orientation metadata is needed |
| Coordinate note | Keep consistent origin and orientation across all parts where possible |
| File naming | Lowercase snake-case with version suffix |
| Version format | `v001`, `v002`, etc. |
| Prototype label | Adult collectible prototype only, not child-safe or toy-certified |
| Brand guardrail | No real-world boot, watch, garment, or device branding in sculpted geometry |
| Text guardrail | No generated placeholder text in sculpted geometry unless deliberately approved as non-canon toy detail |
| Skin guardrail | Forest exposed skin must be Velocisapien scaled skin, never human skin |

---

## Export Status Labels

Use these consistently:

- `Not Started`
- `Blockout In Progress`
- `Sculpt In Progress`
- `Ready for Review`
- `Needs Revision`
- `Ready for Coupon Export`
- `Coupon Exported`
- `Coupon Passed`
- `Ready for STL Export`
- `STL Exported`
- `Print Tested`
- `Paint Tested`
- `Approved for Prototype A`
- `Deferred`
- `Rejected / Do Not Use`

---

## Joint Dependency Labels

Use one or more:

- `neck-socket`
- `shoulder-left`
- `shoulder-right`
- `wrist-left`
- `wrist-right`
- `watch-left-wrist`
- `hip-left`
- `hip-right`
- `waist-optional`
- `knee-left-optional`
- `knee-right-optional`
- `tail-keyed-socket`
- `accessory-grip`
- `harness-clearance`
- `jacket-clearance`
- `pants-pocket-clearance`
- `paint-rub-risk`
- `none`

---

## Primary Figure Part Manifest

| Part ID | Sculpt Part | Planned Export Filename | Units | Scale / Size Target | Joint Dependency | Coupon Dependency | Print-Test Status | Notes |
|---|---|---|---|---|---|---|---|---|
| KFR-PART-001 | Head with primary shades | `kfr_part_001_head_primary_shades_v001.stl` | mm | Fits 5-inch figure; head scale supports expression, shades, snout, brow, proto-quills | neck-socket, paint-rub-risk | KFR-COUPON-001 | Not Started | Protect face, shades, snout, mouth line, and short sparse red proto-quills. |
| KFR-PART-002 | Torso front / solid torso front | `kfr_part_002_torso_front_jacket_harness_v001.stl` | mm | 5-inch torso, jacket / harness visible at shelf distance | shoulder-left, shoulder-right, waist-optional, harness-clearance, jacket-clearance, paint-rub-risk | KFR-COUPON-002 | Not Started | Includes cropped jacket front, under-layer, harness front, badges, checker trim zones. |
| KFR-PART-003 | Torso back / solid torso back | `kfr_part_003_torso_back_jacket_harness_v001.stl` | mm | Aligns with torso front and tail socket clearance | shoulder-left, shoulder-right, tail-keyed-socket, waist-optional, harness-clearance, jacket-clearance | KFR-COUPON-002, KFR-COUPON-006 | Not Started | Includes jacket back yoke, harness back, upper back panel, tail socket clearance. |
| KFR-PART-004 | Pelvis / hip block | `kfr_part_004_pelvis_hip_tail_socket_v001.stl` | mm | Stable hip block; supports tail socket and stance | hip-left, hip-right, tail-keyed-socket, waist-optional, pants-pocket-clearance | KFR-COUPON-005, KFR-COUPON-006 | Not Started | Belt / pants waistband may hide seam. Must support tail base. |
| KFR-PART-005 | Left arm with watch-bearing wrist | `kfr_part_005_arm_left_watch_wrist_v001.stl` | mm | Arm fits shoulder range; compact watch at left wrist | shoulder-left, wrist-left, watch-left-wrist, jacket-clearance, paint-rub-risk | KFR-COUPON-002, KFR-COUPON-003, KFR-COUPON-004 | Not Started | Watch sculpted on. No wrist warmers. No human skin. Black fingerless glove preserved. |
| KFR-PART-006 | Right arm | `kfr_part_006_arm_right_v001.stl` | mm | Matches left arm minus watch | shoulder-right, wrist-right, jacket-clearance, paint-rub-risk | KFR-COUPON-002, KFR-COUPON-003 | Not Started | Sleeve / cuff and glove cuff must clear wrist swivel. |
| KFR-PART-007 | Left gloved hand | `kfr_part_007_hand_left_gloved_v001.stl` | mm | Four-finger hand at 5-inch scale | wrist-left, accessory-grip, watch-left-wrist, paint-rub-risk | KFR-COUPON-003, KFR-COUPON-004, KFR-COUPON-008 | Not Started | Black fingerless glove, visible Velocisapien fingers, dark horn claws. Must not be swallowed by watch. |
| KFR-PART-008 | Right gloved hand / tool grip | `kfr_part_008_hand_right_grip_v001.stl` | mm | Four-finger tool grip at 5-inch scale | wrist-right, accessory-grip, paint-rub-risk | KFR-COUPON-003, KFR-COUPON-008 | Not Started | Primary grip hand for route probe / black flag marker. |
| KFR-PART-009 | Left leg / cargo pants / boot | `kfr_part_009_leg_left_pants_boot_v001.stl` | mm | Stable stance; cargo pants taper to boot | hip-left, knee-left-optional, pants-pocket-clearance, paint-rub-risk | KFR-COUPON-005, KFR-COUPON-007 | Not Started | Reinforced knee / thigh panels, boot collar seam only, four-toe claw read. |
| KFR-PART-010 | Right leg / cargo pants / boot | `kfr_part_010_leg_right_pants_boot_v001.stl` | mm | Stable stance; matches left leg | hip-right, knee-right-optional, pants-pocket-clearance, paint-rub-risk | KFR-COUPON-005, KFR-COUPON-007 | Not Started | Keep pockets from blocking hip movement. No functional ankle. |
| KFR-PART-011 | Keyed removable tail | `kfr_part_011_tail_keyed_v001.stl` | mm | Thick base, taper, blunt tip; supports balance | tail-keyed-socket, paint-rub-risk | KFR-COUPON-006 | Not Started | Tail must install securely and help standing balance. |
| KFR-PART-012 | Harness / gear overlays, if separate | `kfr_part_012_harness_overlay_optional_v001.stl` | mm | Optional separate overlay only if needed for paint / cleanup | harness-clearance, shoulder-left, shoulder-right, paint-rub-risk | KFR-COUPON-002 | Deferred | Default is sculpted-on harness. Use separate only if benefit outweighs fragility. |
| KFR-PART-013 | Route goggles accessory | `kfr_part_013_route_goggles_v001.stl` | mm | 5-inch hand / head compatible accessory | accessory-grip | KFR-COUPON-008 | Not Started | Separate accessory first. Protect lens fronts. |
| KFR-PART-014 | Accessory set master plate | `kfr_part_014_accessory_set_master_v001.stl` | mm | Includes route tools sized for 5-inch figure | accessory-grip | KFR-COUPON-008 | Not Started | Use only if printing accessories as combined master plate. Individual exports preferred for tests. |
| KFR-PART-015 | Optional handheld route-reader backup | `kfr_part_015_handheld_route_reader_backup_v001.stl` | mm | Secondary compact accessory; smaller than wrist GPR emphasis | accessory-grip | KFR-COUPON-008 | Deferred | Wrist watch is primary. Do not make this a giant duplicate device. |

---

## Individual Accessory Export Manifest

Use individual accessory exports for first tests unless the slicer benefits from a master plate.

| Accessory ID | Accessory | Planned Export Filename | Units | Scale / Size Target | Joint / Grip Dependency | Coupon Dependency | Print-Test Status | Notes |
|---|---|---|---|---|---|---|---|---|
| KFR-ACC-001 | Black Path flag marker | `kfr_acc_001_black_path_flag_marker_v001.stl` | mm | Thick enough for adult prototype handling | accessory-grip | KFR-COUPON-008 | Not Started | Blunt tip. Matte black. No weapon-forward read. |
| KFR-ACC-002 | Route probe / collapsible staff | `kfr_acc_002_route_probe_staff_v001.stl` | mm | Fits tool-grip hand; shaft not too thin | accessory-grip | KFR-COUPON-008 | Not Started | Print multiple copies; avoid warping. |
| KFR-ACC-003 | Compact Mountaineer field pack | `kfr_acc_003_field_pack_v001.stl` | mm | Fits back / harness silhouette if separate | harness-clearance, paint-rub-risk | TBD | Not Started | Consider sculpted-on or lightweight if back-heavy. |
| KFR-ACC-004 | EMT pouch, no symbol | `kfr_acc_004_emt_pouch_no_symbol_v001.stl` | mm | Small pouch, no medical symbol | harness-clearance, paint-rub-risk | TBD | Not Started | Sculpted-on preferred unless separation helps paint. |
| KFR-ACC-005 | Brass route token / whistle | `kfr_acc_005_route_token_whistle_v001.stl` | mm | Chunky enough to print | accessory-grip | TBD | Not Started | Markings are toy-only placeholders unless separately approved. |
| KFR-ACC-006 | Carabiner / route clip | `kfr_acc_006_route_clip_v001.stl` | mm | Thick nonfunctional clip | accessory-grip | TBD | Not Started | Do not make tiny functional spring clip. |
| KFR-ACC-007 | Folded terrain map / route card | `kfr_acc_007_route_card_v001.stl` | mm | Thick enough not to warp | accessory-grip | TBD | Not Started | Graphics are placeholder only. |
| KFR-ACC-008 | Alternate gripping hand pair | `kfr_acc_008_alt_grip_hands_pair_v001.stl` | mm | Matches four-finger black glove direction | wrist-left, wrist-right, accessory-grip | KFR-COUPON-003, KFR-COUPON-008 | Deferred | Only needed if primary hands cannot hold tools. |
| KFR-ACC-009 | Optional handheld route-reader backup | `kfr_acc_009_handheld_route_reader_backup_v001.stl` | mm | Compact backup, not primary | accessory-grip | KFR-COUPON-008 | Deferred | Wrist GPR watch is primary route-reader interface. |

---

## Coupon Export Manifest

| Coupon ID | Coupon | Planned Export Filename | Units | Tests | Print-Test Status | Notes |
|---|---|---|---|---|---|---|
| KFR-COUPON-001 | Neck peg / socket | `kfr_coupon_001_neck_peg_socket_clearance_ladder_v001.stl` | mm | Neck fit, rotation, paint clearance | Not Started | Include 0.10, 0.15, 0.20 mm variants. |
| KFR-COUPON-002 | Shoulder with jacket / harness clearance | `kfr_coupon_002_shoulder_jacket_harness_clearance_v001.stl` | mm | Shoulder movement, jacket / harness collision | Not Started | Include left and right shoulder geometry if asymmetrical. |
| KFR-COUPON-003 | Wrist peg / socket | `kfr_coupon_003_wrist_peg_socket_clearance_ladder_v001.stl` | mm | Wrist swivel, glove cuff seam | Not Started | Include left and right if watch changes left clearance. |
| KFR-COUPON-004 | Left wrist watch / glove / cuff sample | `kfr_coupon_004_left_watch_glove_cuff_scale_v001.stl` | mm | Compact watch scale, no wrist-warmer read, no human skin reference | Not Started | Required before full left arm export. |
| KFR-COUPON-005 | Hip / pants pocket clearance | `kfr_coupon_005_hip_pants_pocket_clearance_v001.stl` | mm | Hip movement, cargo pocket collision | Not Started | Include representative pelvis / thigh / pocket geometry. |
| KFR-COUPON-006 | Tail keyed peg / socket | `kfr_coupon_006_tail_keyed_socket_clearance_ladder_v001.stl` | mm | Tail installation, balance support, socket cracking | Not Started | Include tight / medium / loose variants. |
| KFR-COUPON-007 | Optional knee hinge / panel seam | `kfr_coupon_007_knee_panel_hinge_optional_v001.stl` | mm | Optional knee hinge, reinforced panel seam | Deferred | Only export if knees remain in Prototype A. |
| KFR-COUPON-008 | Accessory handle / gripping hand | `kfr_coupon_008_accessory_handle_grip_ladder_v001.stl` | mm | Route probe, flag marker, optional handheld reader grip | Not Started | Include multiple handle diameters. |

---

## Sculpt Export Checklist

Complete before exporting any STL / 3MF.

### Global Scale / Units

- [ ] Scene units set to millimeters.
- [ ] Figure target height checked against 5-inch / 127 mm target.
- [ ] Part scale applied / frozen before export.
- [ ] Origin / pivot convention documented.
- [ ] Left and right parts named correctly.
- [ ] Version suffix included in filename.

### Geometry Health

- [ ] Mesh is manifold or repairable in slicer.
- [ ] Normals checked.
- [ ] No non-printable floating slivers.
- [ ] No accidental internal loose geometry.
- [ ] Thin walls checked.
- [ ] Drainage planned for any hollowed large torso part.
- [ ] No trapped resin risk in sealed hollow parts.

### Canon / Toy Guardrails

- [ ] Kavo reads as Velocisapien / Velociraptoroid.
- [ ] No human skin detail or human anatomy drift in sculpt.
- [ ] Four-finger hands preserved.
- [ ] Four-toed boot / claw read preserved.
- [ ] Tail remains functional and expressive.
- [ ] Black fingerless gloves preserved.
- [ ] Left-wrist watch is compact and not a wrist warmer.
- [ ] Cropped route jacket and cargo pants read as route-worker gear.
- [ ] No ninja / assassin / generic raptor scout / dinosaur monster drift.
- [ ] No real-world boot, watch, garment, or device branding.
- [ ] No generated placeholder text embedded as final sculpt detail.

### Joint / Fit Guardrails

- [ ] Neck socket matches KFR-COUPON-001 plan.
- [ ] Shoulders match KFR-COUPON-002 clearance plan.
- [ ] Wrists match KFR-COUPON-003 plan.
- [ ] Left wrist watch sample passes KFR-COUPON-004 before final left arm export.
- [ ] Hips / pants pockets match KFR-COUPON-005 plan.
- [ ] Tail key matches KFR-COUPON-006 plan.
- [ ] Accessory handles match KFR-COUPON-008 plan.
- [ ] Paint rub zones identified.

### Support / Orientation Guardrails

- [ ] Export reviewed against support orientation notes.
- [ ] Face protected from support scars.
- [ ] Watch screen protected from support scars.
- [ ] Badge faces and checker trim protected.
- [ ] Cargo pocket faces protected.
- [ ] Tail key surfaces protected.
- [ ] Hand grip interiors protected.
- [ ] Accessories thickened where needed for printing.

---

## Export Batch Record Template

Duplicate for every export batch.

### Export Batch: `YYYY-MM-DD — Batch Name`

**Sculpt file version:** TBD  
**Exported by:** TBD  
**Software:** Blender / ZBrush / Nomad Sculpt / Other  
**Units:** mm  
**Scale check:** TBD  
**Parts exported:** TBD  
**Destination folder:** TBD  
**Linked coupon batch:** TBD  
**Linked print batch:** TBD

| Part / Coupon ID | Export Filename | Export Format | Export Status | Slicer Imported? | Notes |
|---|---|---|---|---|---|
| TBD | TBD | STL / 3MF | TBD | TBD | TBD |

---

## Print-Test Status Tracker

| Date | Part / Coupon ID | File Version | Test Type | Result | Linked Log | Next Action |
|---|---|---|---|---|---|---|
| TBD | TBD | TBD | Coupon / First Print / Reprint / Paint Test | TBD | TBD | TBD |

---

## Approval Gate for Full Prototype Export

Do not export the final full Prototype A set until:

- [ ] KFR-COUPON-001 neck test passes.
- [ ] KFR-COUPON-002 shoulder / jacket / harness clearance test passes.
- [ ] KFR-COUPON-003 wrist test passes.
- [ ] KFR-COUPON-004 left wrist watch / glove / cuff scale test passes.
- [ ] KFR-COUPON-005 hip / pants pocket clearance test passes.
- [ ] KFR-COUPON-006 tail keyed socket test passes.
- [ ] KFR-COUPON-008 accessory grip test passes.
- [ ] Optional KFR-COUPON-007 knee test is either passed or formally deferred.
- [ ] Watch is confirmed compact and not wrist-warmer-like.
- [ ] No human-skin reference remains in any figure part.
- [ ] Tail balance strategy is confirmed.
- [ ] Accessory hierarchy is confirmed: wrist GPR watch primary, handheld route-reader optional backup.

---

## Deferred / Do Not Export Yet

| Item | Reason | Revisit When |
|---|---|---|
| Segmented tail | Too risky for Prototype A until keyed tail succeeds. | Prototype B engineering pass. |
| Removable wrist watch | Too small / fragile for first figure. | After sculpted-on watch proves scale. |
| Functional ankle rocker | Not part of Prototype A. | After basic stance succeeds. |
| Double elbows / double knees | Too complex for durable first prototype. | Deluxe articulation pass. |
| Large handheld route-reader as primary device | Superseded by compact wrist GPR watch. | Only if watch is removed or reworked. |
