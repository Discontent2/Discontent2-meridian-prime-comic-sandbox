"""
KFR-BLOCKOUT-v002 Stance Fix 004 — Lower Body Rebuild

Use this after Stance Fix 003 if the feet / legs became disconnected or misaligned.

Purpose:
    Stop nudging broken inherited lower-body parts and rebuild the lower-body blockout cleanly.

Fixes:
    - Hides old/misaligned boot, toe, leg, pants-panel, and stance-fix lower-body parts.
    - Builds new aligned boots with soles, toe boxes, heel blocks, ankle cuffs, and four toe placeholders.
    - Builds longer bent tube legs that actually connect from hips to knees to ankle cuffs.
    - Adds knee masses and forward knee seam placeholders as visual bend guides only.
    - Keeps feet wider apart and slightly outward-splayed.

Important:
    This is still a v002 blockout correction, not final boot sculpting and not functional knee articulation.

Recommended file before running:
    kfr_blockout_v002_stance_fix_pass_003.blend

Recommended file after running:
    kfr_blockout_v002_stance_fix_pass_004.blend
"""

import math
import bpy
from mathutils import Vector

# =========================================================
# TWEAKS
# =========================================================

ROOT_COLLECTION_NAME = "kfr_blockout_v002_stance_fix_004_lower_body_rebuild"

# Coordinate convention from starter scene:
# X = character left/right. Character left is positive X.
# Y = front/back. Negative Y is figure front.
# Z = up.

LEFT_X = 12.0
RIGHT_X = -12.0
FOOT_SPLAY_DEG = 7.0

BOOT_CENTER_Y = -3.0
BOOT_CENTER_Z = 4.2
BOOT_DIMS = (16.0, 27.0, 8.4)
SOLE_DIMS = (17.2, 29.0, 2.0)
TOE_BOX_DIMS = (15.4, 9.5, 6.2)
HEEL_BLOCK_DIMS = (14.4, 7.5, 7.0)
ANKLE_CUFF_DIMS = (12.0, 10.0, 5.0)

HIP_Z = 57.0
KNEE_Z = 34.0
ANKLE_Z = 11.0
HIP_Y = 0.8
KNEE_Y = -4.4
ANKLE_Y = -1.6

UPPER_LEG_RADIUS = 4.7
LOWER_LEG_RADIUS = 4.2
KNEE_MASS_DIMS = (10.0, 7.6, 6.8)
KNEE_SEAM_DIMS = (9.0, 1.2, 5.2)

# Hide old lower-body objects that are now visually superseded.
HIDE_NAME_PARTS = [
    "kfr_part_009_leg_left_pants_boot_blockout",
    "kfr_part_010_leg_right_pants_boot_blockout",
    "kfr_left_boot_four_toe_clearance_",
    "kfr_right_boot_four_toe_clearance_",
    "kfr_left_pants_thigh_reinforcement_panel",
    "kfr_right_pants_thigh_reinforcement_panel",
    "kfr_left_pants_knee_reinforcement_panel",
    "kfr_right_pants_knee_reinforcement_panel",
    "kfr_left_cargo_pocket_clearance_mass",
    "kfr_right_utility_pocket_clearance_mass",
    "kfr_stancefix002_",
    "kfr_stancefix003_",
]

# =========================================================
# HELPERS
# =========================================================


def log(msg):
    print(f"[KFR STANCE FIX 004] {msg}")


def make_collection(name):
    existing = bpy.data.collections.get(name)
    if existing:
        return existing
    col = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(col)
    return col


def make_material(name, color):
    existing = bpy.data.materials.get(name)
    if existing:
        return existing
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = color
    return mat


def hide_matching(name_parts, suffix="_pre_stancefix004_hidden"):
    hidden = []
    for obj in list(bpy.data.objects):
        if obj.type != "MESH":
            continue
        if any(part in obj.name for part in name_parts):
            if not obj.name.endswith(suffix):
                obj.name = obj.name + suffix
            obj.hide_viewport = True
            obj.hide_render = True
            hidden.append(obj.name)
    return hidden


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


def add_cylinder_between(name, start, end, radius, mat, col, vertices=22):
    start_v = Vector(start)
    end_v = Vector(end)
    mid = (start_v + end_v) / 2.0
    direction = end_v - start_v
    length = direction.length
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=length, location=mid)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.rotation_euler = direction.to_track_quat("Z", "Y").to_euler()
    obj.data.materials.append(mat)
    link_to_collection(obj, col)
    return obj


def add_uv_sphere(name, loc, dims, mat, col, segments=20, rings=10):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segments, ring_count=rings, radius=1.0, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.scale = (dims[0] / 2.0, dims[1] / 2.0, dims[2] / 2.0)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    link_to_collection(obj, col)
    return obj


def build_boot(side_label, x, splay_deg, mat_boot, mat_sole, mat_toe, mat_cuff, col):
    """Build a clean blockout boot system. Positive splay rotates toe outward for left side."""
    rot_z = math.radians(splay_deg)
    center = (x, BOOT_CENTER_Y, BOOT_CENTER_Z)

    add_cube(
        f"kfr_stancefix004_{side_label}_boot_base_clean_aligned",
        center,
        BOOT_DIMS,
        mat_boot,
        col,
        rotation=(0.0, 0.0, rot_z),
    )
    add_cube(
        f"kfr_stancefix004_{side_label}_boot_sole_clean_aligned",
        (x, BOOT_CENTER_Y, 1.0),
        SOLE_DIMS,
        mat_sole,
        col,
        rotation=(0.0, 0.0, rot_z),
    )
    add_cube(
        f"kfr_stancefix004_{side_label}_boot_front_toe_box_clean",
        (x, -13.0, 5.1),
        TOE_BOX_DIMS,
        mat_boot,
        col,
        rotation=(0.0, 0.0, rot_z),
    )
    add_cube(
        f"kfr_stancefix004_{side_label}_boot_heel_block_clean",
        (x, 8.2, 5.0),
        HEEL_BLOCK_DIMS,
        mat_boot,
        col,
        rotation=(0.0, 0.0, rot_z),
    )
    add_cube(
        f"kfr_stancefix004_{side_label}_ankle_cuff_connected_to_leg",
        (x, -0.8, 10.0),
        ANKLE_CUFF_DIMS,
        mat_cuff,
        col,
        rotation=(0.0, 0.0, rot_z),
    )

    # Four toe placeholders. Slight arc in X and Y so they read as toes, not buttons.
    # Offsets are local-ish but kept simple for blockout.
    toe_x_offsets = [-5.2, -1.8, 1.8, 5.2]
    toe_y_offsets = [-17.1, -17.8, -17.8, -17.1]
    for i, (dx, y) in enumerate(zip(toe_x_offsets, toe_y_offsets), start=1):
        add_uv_sphere(
            f"kfr_stancefix004_{side_label}_boot_four_toe_placeholder_{i}",
            (x + dx, y, 5.7),
            (2.7, 3.2, 2.5),
            mat_toe,
            col,
            segments=16,
            rings=8,
        )


def build_bent_leg(side_label, x, mat_pants, mat_shadow, col):
    hip = (x, HIP_Y, HIP_Z)
    knee = (x, KNEE_Y, KNEE_Z)
    ankle = (x, ANKLE_Y, ANKLE_Z)

    add_cylinder_between(
        f"kfr_stancefix004_{side_label}_upper_leg_longer_bent_tube_connected",
        hip,
        knee,
        UPPER_LEG_RADIUS,
        mat_pants,
        col,
    )
    add_cylinder_between(
        f"kfr_stancefix004_{side_label}_lower_leg_longer_bent_tube_connected",
        knee,
        ankle,
        LOWER_LEG_RADIUS,
        mat_pants,
        col,
    )
    add_uv_sphere(
        f"kfr_stancefix004_{side_label}_knee_mass_visual_bend_not_joint",
        knee,
        KNEE_MASS_DIMS,
        mat_pants,
        col,
    )
    add_cube(
        f"kfr_stancefix004_{side_label}_forward_knee_seam_placeholder",
        (x, KNEE_Y - 3.7, KNEE_Z + 0.2),
        KNEE_SEAM_DIMS,
        mat_shadow,
        col,
    )

    # Simple pants panel blocks placed onto the new bent-leg read.
    add_cube(
        f"kfr_stancefix004_{side_label}_thigh_reinforcement_panel_replaced",
        (x, -4.8, 43.5),
        (8.2, 1.2, 10.5),
        mat_shadow,
        col,
    )
    add_cube(
        f"kfr_stancefix004_{side_label}_shin_reinforcement_panel_replaced",
        (x, -5.2, 23.5),
        (7.6, 1.2, 9.0),
        mat_shadow,
        col,
    )


# =========================================================
# MAIN
# =========================================================


def main():
    log("Starting clean lower-body rebuild")

    col = make_collection(ROOT_COLLECTION_NAME)

    mat_pants = make_material("kfr_stancefix004_pants_gray", (0.30, 0.31, 0.31, 1.0))
    mat_boot = make_material("kfr_stancefix004_boot_dark_gray", (0.07, 0.07, 0.07, 1.0))
    mat_sole = make_material("kfr_stancefix004_sole_mid_gray", (0.20, 0.20, 0.20, 1.0))
    mat_toe = make_material("kfr_stancefix004_toe_placeholder_gray", (0.55, 0.56, 0.56, 1.0))
    mat_cuff = make_material("kfr_stancefix004_ankle_cuff_gray", (0.26, 0.27, 0.27, 1.0))
    mat_shadow = make_material("kfr_stancefix004_panel_shadow_gray", (0.16, 0.16, 0.16, 1.0))

    hidden = hide_matching(HIDE_NAME_PARTS)
    log(f"Hidden old lower-body objects: {len(hidden)}")
    for name in hidden:
        log(f"  hidden: {name}")

    # Left boot: positive splay. Right boot: negative splay.
    build_boot("left", LEFT_X, FOOT_SPLAY_DEG, mat_boot, mat_sole, mat_toe, mat_cuff, col)
    build_boot("right", RIGHT_X, -FOOT_SPLAY_DEG, mat_boot, mat_sole, mat_toe, mat_cuff, col)

    build_bent_leg("left", LEFT_X, mat_pants, mat_shadow, col)
    build_bent_leg("right", RIGHT_X, mat_pants, mat_shadow, col)

    log("LOWER BODY REBUILD COMPLETE")
    log("Save as: kfr_blockout_v002_stance_fix_pass_004.blend")
    log("Review: front full-body, side full-body, boots/stance close-up.")
    log("If boot splay is still wrong, edit FOOT_SPLAY_DEG sign logic inside build_boot calls.")


if __name__ == "__main__":
    main()
