"""
KFR-BLOCKOUT-v002 Stance Fix 002 — Targeted Boots / Legs

Use this if kfr_v002_stance_fix_001.py runs but nothing visibly changes.

Purpose:
    Apply the stance corrections directly to the known starter-scene object names.

Fixes:
    - Moves left/right boots farther apart.
    - Splays left/right boots outward.
    - Carries toe placeholders, soles, and boot bases together.
    - Nudges lower leg / pants masses outward to follow the new foot stance.
    - Adds a small forward knee-bend suggestion using safe guide geometry instead of risky object rotations.

Important:
    This does not try to perfectly rig the leg. It creates a visible blockout correction
    that a modeler can later sculpt into true bent knees.

Recommended file before running:
    kfr_blockout_v002_head_fix_pass_004.blend

Recommended file after running:
    kfr_blockout_v002_stance_fix_pass_002.blend
"""

import math
import bpy
from mathutils import Matrix, Vector

# =========================================================
# TWEAKS
# =========================================================

FOOT_SPREAD_MM = 3.0
FOOT_SPLAY_DEG = 7.0
LEG_OUTWARD_NUDGE_MM = 1.5
KNEE_FORWARD_NUDGE_MM = 1.4
GROUND_Z = 0.0

ROOT_COLLECTION_NAME = "kfr_blockout_v002_stance_fix_002"

# In the starter script, character left is positive X.
# Many Blender screen views may feel mirrored. This script follows object names, not screen side.

LEFT_FOOT_NAME_PARTS = [
    "kfr_part_009_leg_left_pants_boot_blockout_boot_base",
    "kfr_part_009_leg_left_pants_boot_blockout_sole",
    "kfr_left_boot_four_toe_clearance_",
]

RIGHT_FOOT_NAME_PARTS = [
    "kfr_part_010_leg_right_pants_boot_blockout_boot_base",
    "kfr_part_010_leg_right_pants_boot_blockout_sole",
    "kfr_right_boot_four_toe_clearance_",
]

LEFT_LEG_NAME_PARTS = [
    "kfr_part_009_leg_left_pants_boot_blockout_upper_leg",
    "kfr_left_pants_thigh_reinforcement_panel",
    "kfr_left_pants_knee_reinforcement_panel",
    "kfr_left_cargo_pocket_clearance_mass",
]

RIGHT_LEG_NAME_PARTS = [
    "kfr_part_010_leg_right_pants_boot_blockout_upper_leg",
    "kfr_right_pants_thigh_reinforcement_panel",
    "kfr_right_pants_knee_reinforcement_panel",
    "kfr_right_utility_pocket_clearance_mass",
]

# Lower-leg visual correction pieces added by this script.
# They are deliberately neutral gray blockout markers, not final anatomy.

# =========================================================
# HELPERS
# =========================================================


def log(msg):
    print(f"[KFR STANCE FIX 002] {msg}")


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


def collect_objects(name_parts):
    found = []
    for obj in bpy.data.objects:
        if obj.type != "MESH":
            continue
        if any(part in obj.name for part in name_parts):
            found.append(obj)
    return found


def world_bbox_points(obj):
    return [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]


def group_bbox_center(objects):
    pts = []
    for obj in objects:
        pts.extend(world_bbox_points(obj))
    if not pts:
        return Vector((0, 0, 0))
    min_x = min(p.x for p in pts)
    max_x = max(p.x for p in pts)
    min_y = min(p.y for p in pts)
    max_y = max(p.y for p in pts)
    min_z = min(p.z for p in pts)
    max_z = max(p.z for p in pts)
    return Vector(((min_x + max_x) / 2, (min_y + max_y) / 2, (min_z + max_z) / 2))


def group_top_center(objects):
    pts = []
    for obj in objects:
        pts.extend(world_bbox_points(obj))
    if not pts:
        return Vector((0, 0, 0))
    min_x = min(p.x for p in pts)
    max_x = max(p.x for p in pts)
    min_y = min(p.y for p in pts)
    max_y = max(p.y for p in pts)
    max_z = max(p.z for p in pts)
    return Vector(((min_x + max_x) / 2, (min_y + max_y) / 2, max_z))


def group_min_z(objects):
    pts = []
    for obj in objects:
        pts.extend(world_bbox_points(obj))
    if not pts:
        return 0.0
    return min(p.z for p in pts)


def move_objects(objects, delta):
    for obj in objects:
        obj.location += delta


def rotate_objects_about_pivot(objects, angle_radians, axis, pivot_world):
    rot = Matrix.Rotation(angle_radians, 4, axis)
    t1 = Matrix.Translation(pivot_world)
    t2 = Matrix.Translation(-pivot_world)
    transform = t1 @ rot @ t2
    for obj in objects:
        obj.matrix_world = transform @ obj.matrix_world


def plant_group_to_ground(objects, ground_z=0.0):
    min_z = group_min_z(objects)
    dz = ground_z - min_z
    move_objects(objects, Vector((0.0, 0.0, dz)))


def add_cube(name, loc, dims, mat, col, rotation=(0.0, 0.0, 0.0)):
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=loc, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.dimensions = dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    try:
        col.objects.link(obj)
    except RuntimeError:
        pass
    return obj


def add_knee_bend_markers(col, mat):
    """
    Adds subtle front knee wedge markers to show intended bent-knee direction.
    These are blockout correction guides, not final knee sculpt.
    Negative Y is figure front.
    """
    add_cube(
        "kfr_stancefix002_left_forward_knee_bend_marker",
        loc=(8.0 + LEG_OUTWARD_NUDGE_MM, -6.6 - KNEE_FORWARD_NUDGE_MM, 29.0),
        dims=(9.0, 1.4, 5.8),
        mat=mat,
        col=col,
        rotation=(math.radians(0), math.radians(0), math.radians(0)),
    )
    add_cube(
        "kfr_stancefix002_right_forward_knee_bend_marker",
        loc=(-8.0 - LEG_OUTWARD_NUDGE_MM, -6.6 - KNEE_FORWARD_NUDGE_MM, 29.0),
        dims=(9.0, 1.4, 5.8),
        mat=mat,
        col=col,
        rotation=(math.radians(0), math.radians(0), math.radians(0)),
    )


# =========================================================
# MAIN
# =========================================================


def main():
    log("Starting targeted stance fix 002")

    fix_col = make_collection(ROOT_COLLECTION_NAME)
    mat_marker = make_material("kfr_stancefix002_knee_bend_marker_gray", (0.40, 0.42, 0.42, 1.0))

    left_foot = collect_objects(LEFT_FOOT_NAME_PARTS)
    right_foot = collect_objects(RIGHT_FOOT_NAME_PARTS)
    left_leg = collect_objects(LEFT_LEG_NAME_PARTS)
    right_leg = collect_objects(RIGHT_LEG_NAME_PARTS)

    log(f"Left foot objects found: {len(left_foot)}")
    for obj in left_foot:
        log(f"  LF: {obj.name}")

    log(f"Right foot objects found: {len(right_foot)}")
    for obj in right_foot:
        log(f"  RF: {obj.name}")

    log(f"Left leg objects found: {len(left_leg)}")
    for obj in left_leg:
        log(f"  LL: {obj.name}")

    log(f"Right leg objects found: {len(right_leg)}")
    for obj in right_leg:
        log(f"  RL: {obj.name}")

    if not left_foot or not right_foot:
        log("Could not find starter boot/foot objects. No changes made.")
        log("Use the Outliner search for 'boot_blockout_boot_base' and confirm object names.")
        return

    # 1. Spread feet farther apart. Character left = positive X, character right = negative X.
    move_objects(left_foot, Vector((FOOT_SPREAD_MM, 0.0, 0.0)))
    move_objects(right_foot, Vector((-FOOT_SPREAD_MM, 0.0, 0.0)))
    log(f"Moved named boot groups outward by {FOOT_SPREAD_MM} mm.")

    # 2. Splay feet outward around top-center ankle area.
    left_pivot = group_top_center(left_foot)
    right_pivot = group_top_center(right_foot)
    rotate_objects_about_pivot(left_foot, math.radians(-FOOT_SPLAY_DEG), "Z", left_pivot)
    rotate_objects_about_pivot(right_foot, math.radians(FOOT_SPLAY_DEG), "Z", right_pivot)
    log(f"Splayed named boot groups by {FOOT_SPLAY_DEG} degrees outward.")

    # 3. Nudge leg masses outward a little so ankles/knees do not look pasted onto old foot positions.
    if left_leg:
        move_objects(left_leg, Vector((LEG_OUTWARD_NUDGE_MM, 0.0, 0.0)))
    if right_leg:
        move_objects(right_leg, Vector((-LEG_OUTWARD_NUDGE_MM, 0.0, 0.0)))
    log(f"Nudged leg groups outward by {LEG_OUTWARD_NUDGE_MM} mm where found.")

    # 4. Add visible knee-bend markers instead of risky rotating capsule parts.
    add_knee_bend_markers(fix_col, mat_marker)
    log("Added forward knee-bend markers to indicate intended bent-knee stance.")

    # 5. Replant feet to ground.
    plant_group_to_ground(left_foot, GROUND_Z)
    plant_group_to_ground(right_foot, GROUND_Z)
    log("Replanted boot groups to ground.")

    log("STANCE FIX 002 COMPLETE")
    log("Save as: kfr_blockout_v002_stance_fix_pass_002.blend")
    log("Review: front full-body, side full-body, boots close-up.")


if __name__ == "__main__":
    main()
