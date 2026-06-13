# Kavo Forest Rill Gray Blockout Review — v001

**Submission:** `kfr-blockout-v001`  
**Review date:** 2026-06-13  
**Reviewer:** ChatGPT Toy Development Room  
**Decision:** Approved with Required Fixes / Not Approved for Detail Sculpt Yet

## One-Sentence Verdict

KFR blockout v001 successfully proves the overall route-worker silhouette, broad stance, functional tail, left-wrist watch placement, and core part layout, but it is too procedural and schematic to enter detail sculpt without a human modeler refinement pass.

---

## What Works

- The figure is built at the 5-inch / 127 mm target in millimeters.
- The full-body silhouette includes saurian head, snout, brow, shades, short proto-quills, broad boots, tail, cropped jacket, cargo pants, harness, and compact left-wrist watch.
- The left-wrist watch is compact and does not read as a wrist warmer in the blockout.
- The tail has a thick base, visible keyed socket area, and a balance-support trajectory.
- Boots are broad enough in blockout to suggest freestanding support.
- Four-finger hands and four-toe boot/claw reads are represented.
- The blockout package includes required views 01 through 10 plus recommended views 11 through 14.

---

## Required Fixes Before Detail Sculpt

| Priority | Fix Label | Issue | Required Change | Reference |
|---|---|---|---|---|
| P0 | `modeler-refinement-required` | Procedural primitive mesh is not a production sculpt base. | Rebuild / refine in Blender, ZBrush, Nomad, or equivalent using this as layout reference. | modeler kickoff brief |
| P0 | `joint-placeholder-fix` | Joint positions are marked but not toleranced. | Replace placeholder spheres with actual socket / peg planning after coupons. | STL manifest / 3D print plan |
| P1 | `head-identity-fix` | Head reads as a correct saurian mass but lacks refined Forest expression. | Refine brow, snout, mouth line, shades, and calm-dangerous expression before detail sculpt approval. | KFR-REF-005 |
| P1 | `garment-layer-fix` | Jacket, under-layer, and pants are broad masses only. | Refine garment silhouette, collar, cuffs, cargo pocket placement, and hip/shoulder clearance. | KFR-REF-014A |
| P1 | `tail-balance-fix` | Tail reads functional, but balance needs real 3D modeler check with center of mass. | Validate side/back tail line and keyed socket in sculpt software. | KFR-REF-009 / KFR-REF-012 |
| P1 | `watch-scale-fix` | Watch scale is acceptable as a blockout, but the watch coupon still needs real geometry. | Build KFR-COUPON-004 before final left arm export. | KFR-REF-014B |
| P2 | `accessory-grip-fix` | Accessory placeholders are simple cylinders. | Match handle diameters to KFR-COUPON-008 before accessory sculpt. | accessory sheet / STL manifest |

---

## Review Decision

**Status:** KFR-BLOCKOUT-v001 is accepted as a schematic layout submission and workflow proof.

**Not approved for detail sculpt yet.** Proceed to a modeler refinement pass, then submit `kfr-blockout-v002` using the same screenshot protocol.

---

## Do Not Change

- Left-wrist watch placement.
- Compact watch intention.
- Black fingerless glove read.
- Broad field boot stance.
- Cropped jacket / cargo pants / harness layering.
- Tail as functional balance and attitude feature.
- Wrist GPR as primary route-reader, with handheld route-reader deferred / optional backup.

---

## Next Action

Create `kfr-blockout-v002` as a real sculpt blockout in modeling software using v001 as a proportion and workflow guide. Do not detail scales, badges, checker trim, zippers, UI, or tiny hardware until v002 blockout passes.
