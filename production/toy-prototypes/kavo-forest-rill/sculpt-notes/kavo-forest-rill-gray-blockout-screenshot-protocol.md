# Kavo "Forest" Rill Gray Blockout Screenshot Naming / Submission Protocol

**Room:** Meridian Prime Toy Development Room / Action Figure Prototype Lab  
**Prototype:** Kavo "Forest" Rill 5-inch adult collectible action figure  
**File Type:** Gray blockout screenshot naming and submission protocol  
**Status:** Ready for first gray blockout package  
**Canon Boundary:** Sandbox production protocol. Does not alter main canon.

---

## Purpose

Use this protocol when submitting the first gray / neutral-material Kavo blockout package for review.

The goal is to prevent mystery-angle goblins: unlabeled screenshots, random camera views, missing watch close-ups, missing tail balance checks, and files named things like `finalfinalmaybe3.png`.

---

## Required Companion Review File

Reviewers should use this protocol with:

- `production/toy-prototypes/kavo-forest-rill/sculpt-notes/kavo-forest-rill-gray-blockout-review-checklist.md`
- `production/toy-prototypes/kavo-forest-rill/sculpt-notes/kavo-forest-rill-sculpt-blockout-checklist.md`
- `production/toy-prototypes/kavo-forest-rill/sculpt-notes/kavo-forest-rill-modeler-kickoff-brief.md`
- `production/toy-prototypes/kavo-forest-rill/sculpt-notes/kavo-forest-rill-stl-part-manifest.md`

---

## Folder Location

Recommended submission folder:

`production/toy-prototypes/kavo-forest-rill/reference/blockout-submissions/kfr-blockout-v###/`

Example:

`production/toy-prototypes/kavo-forest-rill/reference/blockout-submissions/kfr-blockout-v001/`

If image files are submitted outside the repo, preserve this exact folder name in the transfer package.

---

## Version Naming

Use this version format:

`kfr-blockout-v###`

Examples:

- `kfr-blockout-v001`
- `kfr-blockout-v002`
- `kfr-blockout-v003`

Do not use:

- `final`
- `newfinal`
- `approvedmaybe`
- `latest`
- `real_latest`
- `use_this_one`

Those names summon fog.

---

## Screenshot File Naming Formula

Use lowercase snake-case.

Formula:

`kfr_blockout_v###_##_<view-name>.png`

Where:

- `kfr` = Kavo Forest Rill
- `blockout` = gray blockout stage
- `v###` = version number
- `##` = ordered view number
- `<view-name>` = required view label

Example:

`kfr_blockout_v001_01_front_ortho.png`

Preferred format: `.png`  
Acceptable backup format: `.jpg`  
Do not submit screenshots as `.webp` unless specifically requested.

---

## Required Screenshot Set

Submit all required views for first review.

| Order | Required Filename | View | Camera / Notes | Required? |
|---:|---|---|---|---:|
| 01 | `kfr_blockout_v###_01_front_ortho.png` | Front orthographic | Full figure, ground plane visible, neutral pose. | Yes |
| 02 | `kfr_blockout_v###_02_side_ortho.png` | Side orthographic | Full figure, snout / tail / stance readable. | Yes |
| 03 | `kfr_blockout_v###_03_back_ortho.png` | Back orthographic | Full figure, tail base, jacket back, harness back visible. | Yes |
| 04 | `kfr_blockout_v###_04_three_quarter_shelf.png` | Three-quarter shelf read | Slightly above shelf angle, full figure. | Yes |
| 05 | `kfr_blockout_v###_05_head_closeup.png` | Head close-up | Snout, brow, shades mass, proto-quill mass visible. | Yes |
| 06 | `kfr_blockout_v###_06_left_wrist_watch_closeup.png` | Left wrist watch close-up | Watch, black fingerless glove, wrist scale area visible. | Yes |
| 07 | `kfr_blockout_v###_07_hands_grip_closeup.png` | Hands / grip close-up | Four fingers, glove cuffs, grip placeholder visible. | Yes |
| 08 | `kfr_blockout_v###_08_boots_stance_closeup.png` | Boots / stance close-up | Four-toe clearance, boot footprint, ground contact. | Yes |
| 09 | `kfr_blockout_v###_09_tail_socket_balance_closeup.png` | Tail socket / balance close-up | Tail base, keyed socket area, stance relation. | Yes |
| 10 | `kfr_blockout_v###_10_jacket_harness_pants_closeup.png` | Garment / harness close-up | Cropped jacket, under-layer, harness, pants pocket masses. | Yes |
| 11 | `kfr_blockout_v###_11_top_down_mass_check.png` | Top-down mass check | Shoulders, hips, tail, stance footprint. | Recommended |
| 12 | `kfr_blockout_v###_12_scale_ruler_scene.png` | Scale / ruler scene | 127 mm height marker or ruler visible. | Recommended |
| 13 | `kfr_blockout_v###_13_accessory_grip_placeholders.png` | Accessory grip placeholders | Route probe / flag marker handle cylinders. | Recommended |
| 14 | `kfr_blockout_v###_14_joint_placeholders.png` | Joint placeholders | Neck, shoulder, wrist, hip, tail socket markers. | Recommended |

A submission missing views 01 through 10 should not be approved for detail sculpt.

---

## Optional Turntable / Video

Optional video filename:

`kfr_blockout_v###_turntable_360.mp4`

Turntable requirements:

- neutral gray material
- ground plane visible
- slow full rotation
- no dramatic lens distortion
- no animation pose changes
- no music / effects needed

Video is useful, but screenshots still remain required.

---

## Required Submission Notes File

Include a short notes file named:

`kfr_blockout_v###_submission_notes.md`

Template:

```md
# Kavo Forest Rill Blockout Submission Notes

**Version:** kfr-blockout-v###  
**Date:** YYYY-MM-DD  
**Modeler:** TBD  
**Software:** Blender / ZBrush / Nomad / Other  
**Scene units:** millimeters  
**Target height:** 127 mm / 5 inches  
**Blockout file:** TBD  

## Submitted Views

- [ ] 01 front ortho
- [ ] 02 side ortho
- [ ] 03 back ortho
- [ ] 04 three-quarter shelf
- [ ] 05 head close-up
- [ ] 06 left wrist watch close-up
- [ ] 07 hands / grip close-up
- [ ] 08 boots / stance close-up
- [ ] 09 tail socket / balance close-up
- [ ] 10 jacket / harness / pants close-up
- [ ] 11 top-down mass check
- [ ] 12 scale / ruler scene
- [ ] 13 accessory grip placeholders
- [ ] 14 joint placeholders

## Known Issues

- TBD

## Questions For Review

- TBD

## Changes Since Previous Version

- First submission / TBD
```

---

## Camera / Display Rules

Use these rules for all screenshots:

- neutral gray material only unless a quick color overlay is specifically requested
- flat or simple studio lighting
- no dramatic shadows hiding silhouette
- no perspective distortion on orthographic views
- full body should fit within frame with a small margin
- ground plane visible in full-body views
- camera height consistent across front / side / back if possible
- close-ups should crop tightly but not hide context
- left wrist watch view must show the glove and wrist area together
- tail view must show relationship to pelvis, jacket hem, and ground plane
- boot view must show both boot footprint and four-toe clearance

---

## Review Overlay Suggestions

If possible, include simple annotations on duplicate copies only, not the clean screenshots.

Optional annotated filenames:

- `kfr_blockout_v###_a01_front_ortho_annotated.png`
- `kfr_blockout_v###_a06_left_wrist_watch_annotated.png`
- `kfr_blockout_v###_a09_tail_balance_annotated.png`

Annotation labels may include:

- 127 mm height marker
- tail contact / near-contact point
- keyed tail socket area
- left wrist watch scale
- wrist swivel placeholder
- shoulder clearance area
- hip / pocket clearance area
- four-finger hand count
- four-toe boot clearance

Do not submit annotated images without clean versions.

---

## Quick Pre-Submission Self-Check

Before sending the package, confirm:

- [ ] filenames match the protocol
- [ ] version number is consistent across all files
- [ ] views 01 through 10 are included
- [ ] scene units are millimeters
- [ ] target height is 127 mm / 5 inches
- [ ] watch is visible on left wrist
- [ ] watch is compact, not wrist-warmer-like
- [ ] black fingerless glove read is visible
- [ ] exposed skin does not look human
- [ ] tail balance view is included
- [ ] boots / stance view is included
- [ ] jacket / harness / pants view is included
- [ ] no real-world branding appears
- [ ] no final-detail sculpting is hiding unresolved blockout issues
- [ ] submission notes file is included

---

## Reviewer Intake Checklist

When receiving a submission, reviewer should check:

- [ ] folder uses `kfr-blockout-v###`
- [ ] all required screenshots are present
- [ ] submission notes file is present
- [ ] version number is consistent
- [ ] images are readable resolution
- [ ] no required angle is replaced by a mystery glamour shot
- [ ] gray blockout review checklist can be completed from submitted views

If not, request a corrected package before judging design quality.

---

## Example Complete Package

```text
kfr-blockout-v001/
  kfr_blockout_v001_submission_notes.md
  kfr_blockout_v001_01_front_ortho.png
  kfr_blockout_v001_02_side_ortho.png
  kfr_blockout_v001_03_back_ortho.png
  kfr_blockout_v001_04_three_quarter_shelf.png
  kfr_blockout_v001_05_head_closeup.png
  kfr_blockout_v001_06_left_wrist_watch_closeup.png
  kfr_blockout_v001_07_hands_grip_closeup.png
  kfr_blockout_v001_08_boots_stance_closeup.png
  kfr_blockout_v001_09_tail_socket_balance_closeup.png
  kfr_blockout_v001_10_jacket_harness_pants_closeup.png
  kfr_blockout_v001_11_top_down_mass_check.png
  kfr_blockout_v001_12_scale_ruler_scene.png
  kfr_blockout_v001_13_accessory_grip_placeholders.png
  kfr_blockout_v001_14_joint_placeholders.png
  kfr_blockout_v001_turntable_360.mp4
```

---

## Rejection For Submission Hygiene

Reject or return the package for cleanup if:

- required views are missing
- filenames are inconsistent
- version numbers conflict
- watch close-up is missing
- tail balance view is missing
- front / side / back are perspective glamour shots instead of orthographic
- screenshots are too dark or cropped
- file names do not identify the view
- the notes file does not list units and target height

This is not a design rejection. It is a package-quality correction so the design can be reviewed cleanly.
