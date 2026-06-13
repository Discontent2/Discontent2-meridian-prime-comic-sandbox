"""
KFR-BLOCKOUT-v002 Garment / Harness / Pants Restore 001

Run this after the accepted v002 stance/lower-body pass.

Purpose:
    Restore readable clothing layers that were swallowed by lower-body revisions.

Adds:
    - front harness straps
    - upper chest yoke
    - chest insert / inner shirt panel
    - waist strap / belt read
    - lower jacket hem bar
    - side torso reinforcement bars
    - thigh reinforcement panels
    - knee reinforcement panels
    - right cargo pocket with flap
    - slim side leg strip details

Important:
    This is non-destructive. It does not change the head, tail, boots, or stance.
    It creates a new collection so parts can be inspected or deleted easily.

Recommended file before running:
    kfr_blockout_v002_tail_original_reverted_or_current_working.blend

Recommended file after running:
    kfr_blockout_v002_garment_restore_pass_001.blend
"""

import bpy
from mathutils import Vector

ROOT_COLLECTION_NAME = "kfr_blockout_v002_garment_restore_001"

# Coordinate convention:
# X = character left/right. Positive X = character left.
# Y = front/back. Negative Y = figure front in most KFR blockout views.
# Z = up.

# These coordinates are tuned to the current KFR v002 127mm blockout scale.
# They are deliberately simple blockout forms, not final sculpt details.

# Materials
MAT_HARNESS = (0.08, 0.08, 0.08, 1.0)
MAT_JACKET = (0.32, 0.33, 0.33, 1.0)
MAT_PANTS_PANEL = (0.36, 0.36, 0.34, 1.0)
MAT_POCKET = (0.28, 0.24, 0.20, 1.0)
MAT_STITCH_GUIDE = (0.12, 0.12, 0.12, 1.0)
MAT_SHIRT = (0.52, 0.53, 0.50, 1.0)

# Torso / harness approximate placements.
TORSO_FRONT_Y = -7.8
TORSO_Z_CENTER = 70.0
TORSO_X_HALF = 16.0

# Leg approximate placements, matching the current accepted lower-body stance.
LEFT_LEG_X = 12.0
RIGHT_LEG_X = -12.0
THIGH_Z = 43.0
KNEE_Z = 32.8
SHIN_Z = 24.0
LEG_FRONT_Y = -6.2


def log(msg):
    print(f"[KFR GARMENT RESTORE 001] {msg}")


def make_collection(name):
    existing = bpy.data.collections.get(name)
    if existing:
        for obj in list(existing.objects):
            bpy.data.objects.remove(obj, do_unlink=True)
        return existing
    col = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(col)
    return col


def make_material(name, rgba):
    existing = bpy.data.materials.get(name)
    if existing:
        return existing
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = rgba
    return mat


def link_to_collection(obj, col):
    try:
        col.objects.link(obj)
    except RuntimeError:
        pass


def add_cube(name, loc, dims, mat, col, rotation=(0.0, 0.0, 0.0)):
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=loc, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.dimensions = dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    link_to_collection(obj, col)
    return obj


def add_torso_layers(col, mat_harness, mat_jacket, mat_shirt, mat_stitch):
    created = []

    # Inner shirt / chest insert, visible behind harness.
    created.append(add_cube(
        "kfr_garment_restore_001_chest_insert_inner_shirt_panel",
        loc=(0.0, TORSO_FRONT_Y - 0.18, 72.0),
        dims=(15.0, 0.9, 22.0),
        mat=mat_shirt,
        col=col,
    ))

    # Two vertical harness straps.
    for x, label in [(-8.5, "right_screen"), (8.5, "left_screen")]:
        created.append(add_cube(
            f"kfr_garment_restore_001_front_vertical_harness_strap_{label}",
            loc=(x, TORSO_FRONT_Y - 0.5, 71.0),
            dims=(2.4, 1.1, 28.0),
            mat=mat_harness,
            col=col,
        ))

    # Upper chest yoke / shoulder bridge.
    created.append(add_cube(
        "kfr_garment_restore_001_upper_harness_yoke_bar",
        loc=(0.0, TORSO_FRONT_Y - 0.6, 84.5),
        dims=(29.0, 1.2, 2.6),
        mat=mat_harness,
        col=col,
    ))

    # Waist belt/strap.
    created.append(add_cube(
        "kfr_garment_restore_001_waist_belt_bar",
        loc=(0.0, TORSO_FRONT_Y - 0.7, 57.8),
        dims=(32.0, 1.4, 2.8),
        mat=mat_harness,
        col=col,
    ))

    # Jacket lower hem, separated from belt.
    created.append(add_cube(
        "kfr_garment_restore_001_jacket_lower_hem_bar",
        loc=(0.0, TORSO_FRONT_Y - 0.35, 54.2),
        dims=(30.0, 1.1, 2.4),
        mat=mat_jacket,
        col=col,
    ))

    # Side torso reinforcement strips.
    for x, label in [(-15.0, "right_screen"), (15.0, "left_screen")]:
        created.append(add_cube(
            f"kfr_garment_restore_001_jacket_side_reinforcement_{label}",
            loc=(x, TORSO_FRONT_Y - 0.25, 70.0),
            dims=(2.2, 1.0, 29.0),
            mat=mat_jacket,
            col=col,
        ))

    # Stitch / seam guide line across lower torso.
    created.append(add_cube(
        "kfr_garment_restore_001_lower_torso_seam_guide",
        loc=(0.0, TORSO_FRONT_Y - 0.92, 61.0),
        dims=(24.0, 0.35, 0.7),
        mat=mat_stitch,
        col=col,
    ))

    return created


def add_leg_layers(col, mat_panel, mat_pocket, mat_stitch):
    created = []

    # Front thigh and knee reinforcement panels.
    for x, side in [(LEFT_LEG_X, "left"), (RIGHT_LEG_X, "right")]:
        created.append(add_cube(
            f"kfr_garment_restore_001_{side}_front_thigh_reinforcement_panel",
            loc=(x, LEG_FRONT_Y, THIGH_Z),
            dims=(8.2, 1.1, 10.0),
            mat=mat_panel,
            col=col,
        ))
        created.append(add_cube(
            f"kfr_garment_restore_001_{side}_front_knee_reinforcement_panel",
            loc=(x, LEG_FRONT_Y - 0.1, KNEE_Z),
            dims=(8.8, 1.1, 5.2),
            mat=mat_panel,
            col=col,
        ))
        created.append(add_cube(
            f"kfr_garment_restore_001_{side}_shin_vertical_seam_strip",
            loc=(x + (4.9 if side == "left" else -4.9), LEG_FRONT_Y + 0.1, SHIN_Z),
            dims=(1.1, 0.8, 13.0),
            mat=mat_stitch,
            col=col,
        ))

    # Right-side cargo pocket with flap. Character right is negative X.
    created.append(add_cube(
        "kfr_garment_restore_001_right_cargo_pocket_mass",
        loc=(RIGHT_LEG_X - 6.0, -1.4, 38.8),
        dims=(4.6, 4.0, 8.0),
        mat=mat_pocket,
        col=col,
    ))
    created.append(add_cube(
        "kfr_garment_restore_001_right_cargo_pocket_flap",
        loc=(RIGHT_LEG_X - 6.0, -3.7, 43.4),
        dims=(5.0, 1.0, 2.0),
        mat=mat_stitch,
        col=col,
    ))

    # Smaller left utility patch for asymmetry.
    created.append(add_cube(
        "kfr_garment_restore_001_left_utility_patch_mass",
        loc=(LEFT_LEG_X + 5.8, -1.2, 36.5),
        dims=(3.2, 3.2, 6.0),
        mat=mat_pocket,
        col=col,
    ))

    return created


def main():
    log("Starting garment / harness / pants restore 001")

    col = make_collection(ROOT_COLLECTION_NAME)
    mat_harness = make_material("kfr_garment_restore_001_harness_black", MAT_HARNESS)
    mat_jacket = make_material("kfr_garment_restore_001_jacket_gray", MAT_JACKET)
    mat_panel = make_material("kfr_garment_restore_001_pants_panel_gray", MAT_PANTS_PANEL)
    mat_pocket = make_material("kfr_garment_restore_001_pocket_brown_gray", MAT_POCKET)
    mat_stitch = make_material("kfr_garment_restore_001_stitch_dark", MAT_STITCH_GUIDE)
    mat_shirt = make_material("kfr_garment_restore_001_inner_shirt", MAT_SHIRT)

    created = []
    created.extend(add_torso_layers(col, mat_harness, mat_jacket, mat_shirt, mat_stitch))
    created.extend(add_leg_layers(col, mat_panel, mat_pocket, mat_stitch))

    log(f"Created garment objects: {len(created)}")
    for obj in created:
        log(f"  created: {obj.name}")

    log("GARMENT RESTORE 001 COMPLETE")
    log("Save as: kfr_blockout_v002_garment_restore_pass_001.blend")
    log("Review: front, side, back, torso close-up, thighs/knees/cargo close-up.")


if __name__ == "__main__":
    main()
