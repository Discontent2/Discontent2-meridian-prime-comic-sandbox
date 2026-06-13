# Kavo "Forest" Rill Blockout v002

**Submission:** `kfr-blockout-v002`  
**Status:** Commissioned / awaiting refined modeler blockout  
**Target:** Real sculpt-aware gray blockout in Blender, ZBrush, Nomad Sculpt, or equivalent  
**Recommended Starter Script:** `create_kfr_blockout_v002_lite_safe_scene.py`  
**Full Starter Script:** `create_kfr_blockout_v002_starter_scene.py`  
**Canon Boundary:** Sandbox production submission folder. Does not alter main canon.

---

## Purpose

This folder is the submission location for KFR-BLOCKOUT-v002.

v002 is the first real modeler refinement pass after the procedural KFR-BLOCKOUT-v001 workflow proof.

v002 should still be a gray / neutral-material blockout. It should not be final detail sculpt.

---

## Start Here

Modeler should open these files first:

1. `create_kfr_blockout_v002_lite_safe_scene.py`  
   Run this first in Blender. It is the crash-safe starter scene.

2. `kfr_blockout_v002_refinement_brief.md`  
   Read before editing the generated forms.

3. `kfr_blockout_v002_commission_packet.md`  
   Use as the production task packet.

4. `kfr_blockout_v002_submission_notes_template.md`  
   Copy into `kfr_blockout_v002_submission_notes.md` when submitting.

Use KFR-BLOCKOUT-v001 as layout reference only.

---

## Running the Lite Safe Blender Starter Script

Use this version if the full starter script crashes or closes Blender.

In Blender:

1. Open **File > New > General**.
2. Open the **Scripting** workspace.
3. Open `create_kfr_blockout_v002_lite_safe_scene.py`.
4. Press **Run Script**.
5. The script creates the v002 starter scene with named parts, millimeter units, a 127 mm guide, joint placeholders, a compact left-wrist watch, accessory placeholders, and 14 review cameras.
6. Save the `.blend` file as `kfr_blockout_v002_lite_safe_starter_scene.blend` before manual refinement.

This Lite version avoids bevel modifiers, weighted normals, text objects, smooth shading, node materials, automatic rendering, and automatic exporting.

---

## Full Starter Script

The full script remains available as:

`create_kfr_blockout_v002_starter_scene.py`

Only use it after the Lite script works, or if your Blender setup handles the heavier script safely.

Optional full-script toggles near the top of that file:

- `RENDER_ALL_VIEWS = False`
- `EXPORT_SCENE_ASSETS = False`
- `SAVE_BLEND_FILE = False`

Set any of those to `True` only after the scene is stable.

---

## Expected v002 Deliverables

Required model / scene:

- 127 mm / 5-inch target height
- millimeter units
- ground plane
- neutral relaxed stance
- refined sculpt-aware big forms
- visible joint placeholders
- visible compact left-wrist watch
- visible garment layers
- visible tail socket plan

Required screenshot package:

- `kfr_blockout_v002_01_front_ortho.png`
- `kfr_blockout_v002_02_side_ortho.png`
- `kfr_blockout_v002_03_back_ortho.png`
- `kfr_blockout_v002_04_three_quarter_shelf.png`
- `kfr_blockout_v002_05_head_closeup.png`
- `kfr_blockout_v002_06_left_wrist_watch_closeup.png`
- `kfr_blockout_v002_07_hands_grip_closeup.png`
- `kfr_blockout_v002_08_boots_stance_closeup.png`
- `kfr_blockout_v002_09_tail_socket_balance_closeup.png`
- `kfr_blockout_v002_10_jacket_harness_pants_closeup.png`
- `kfr_blockout_v002_11_top_down_mass_check.png`
- `kfr_blockout_v002_12_scale_ruler_scene.png`
- `kfr_blockout_v002_13_accessory_grip_placeholders.png`
- `kfr_blockout_v002_14_joint_placeholders.png`

Required notes:

- `kfr_blockout_v002_submission_notes.md`

Optional but useful:

- source scene file, such as `.blend`, `.ztl`, `.obj`, `.glb`, or equivalent
- turntable video
- exported model preview

---

## v002 Review Outcome Options

When submitted, v002 will be reviewed as one of:

- Approved for Detail Sculpt
- Approved with Required Fixes
- Rejected / Rework Blockout

No detail sculpting should begin until v002 is approved or conditionally approved.
