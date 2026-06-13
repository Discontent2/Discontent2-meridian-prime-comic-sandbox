"""
KFR-BLOCKOUT-v002 Stance Fix 003 — Corrected Splay + Bent Tube Legs

Use this after Stance Fix 002 if the feet became pigeon-toed and the knees still read straight.

Purpose:
    Correct the stance at blockout level without adding functional knee articulation.

Fixes:
    - Reverses the incorrect pigeon-toe rotation from Stance Fix 002.
    - Keeps the wider foot spacing.
    - Hides the old straight tube-leg capsule parts.
    - Hides Stance Fix 002 knee marker blocks.
    - Adds new bent upper-leg and lower-leg tube segments.
    - Adds simple knee masses / seam placeholders.
    - Keeps knees as a visual sculpt guide, not a functional joint.

Recommended file before running:
    kfr_blockout_v002_stance_fix_pass_002.blend

Recommended file after running:
    kfr_blockout_v002_stance_fix_pass_003.blend

If you skipped Stance Fix 002:
    Set ASSUME_STANCE_FIX_002_ALREADY_RAN = False below before running.
"""

import math
import bpy
from mathutils import Matrix, Vector

# =========================================================
# TWEAKS
# =========================================================

ASSUME_STANCE_FIX_002_ALREADY_RAN = True

# Fix 002 used 7 degrees in the wrong direction. If it already ran, we rotate back through neutral
# and onward to the desired outward splay. If it did not run, we only apply TARGET_OUTWARD_SPLAY_DEG.
PREVIOUS_BAD_SPLAY_DEG = 7.0
TARGET_OUTWARD_SPLAY_DEG = 8.0

# New bent-leg placement. Positive X = character left, negative X = character right.
LEFT_X = 11.0
RIGHT_X = -11.0
HIP_Z = 56.0
KNEE_Z = 33.0
ANKLE_Z = 11.5

# Negative Y is figure front. Knees come slightly forward, ankles remain near boot centers.
HIP_Y = 0.8
KNEE_Y = -4.0
ANKLE_Y = -1.2

UPPER_LEG_RADIUS = 4.6
LOWER_LEG_RADIUS = 4.2
KNEE_MASS_DIMS = (10.0, 7.5, 6.5)
KNEE_SEAM_DIMS = (9.5, 1.2, 5.0)
GROUND_Z = 0.0

ROOT_COLLECTION_NAME = "kfr_blockout_v002_stance_fix_003_bent_legs"

# Starter scene object name fragments.
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

# Hide original straight capsule leg pieces and older stance-fix markers.
HIDE_NAME_PARTS = [
    "kfr_part_009_leg_left_pants_boot_blockout_upper_leg",
    "kfr_part_010_leg_right_pants_boot_blockout_upper_leg",
    "kfr_stancefix002_left_forward_knee_bend_marker",
    "kfr_stancefix002_right_forward_knee_bend_marker",
    "kfr_stancefix003_",
]

# Optional hide for old pants panels that may no longer align cleanly with bent legs.
# Set False if you prefer to keep all old pants panels visible.
HIDE_MISALIGNED_PANTS_PANELS = False
OLD_PANTS_PANEL_PARTS = [
    "kfr_left_pants_thigh_reinforcement_panel",
    "kfr_right_pants_thigh_reinforcement_panel",
    "kfr_left_pants_knee_reinforcement_panel",
    "kfr_right_pants_knee_reinforcement_panel",
]

# =========================================================
# HELPERS
# =========================================================


def log(msg):
    print(f"[KFR STANCE FIX 003] {msg}")


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


def hide_matching(name_parts, suffix="_pre_stancefix003_hidden"):
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


def world_bbox_points(obj):
    return [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]


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
    if not objects:
        return
    min_z = group_min_z(objects)
    dz = ground_z - min_z
    move_objects(objects, Vector((0.0, 0.0, dz)))


def link_to_collection(obj, col):
    try:
        col.objects.link(obj)
    except RuntimeError:
        pass


def add_cylinder_between(name, start, end, radius, mat, col, vertices=20):
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


def build_bent_leg(side_label, x, mat_cloth, mat_shadow, col):
    hip = (x, HIP_Y, HIP_Z)
    knee = (x, KNEE_Y, KNEE_Z)
    ankle = (x, ANKLE_Y, ANKLE_Z)

    add_cylinder_between(
        f"kfr_stancefix003_{side_label}_upper_leg_bent_tube",
        hip,
        knee,
        UPPER_LEG_RADIUS,
        mat_cloth,
        col,
    )
    add_cylinder_between(
        f"kfr_stancefix003_{side_label}_lower_leg_bent_tube",
        knee,
        ankle,
        LOWER_LEG_RADIUS,
        mat_cloth,
        col,
    )
    add_uv_sphere(
        f"kfr_stancefix003_{side_label}_knee_mass_visual_not_joint",
        knee,
        KNEE_MASS_DIMS,
        mat_cloth,
        col,
    )
    add_cube(
        f"kfr_stancefix003_{side_label}_forward_knee_seam_placeholder",
        (x, KNEE_Y - 3.6, KNEE_Z + 0.2),
        KNEE_SEAM_DIMS,
        mat_shadow,
        col,
    )


# =========================================================
# MAIN
# =========================================================


def main():
    log("Starting corrected splay + bent legs pass")

    col = make_collection(ROOT_COLLECTION_NAME)
    mat_cloth = make_material("kfr_stancefix003_cloth_gray", (0.30, 0.31, 0.31, 1.0))
    mat_shadow = make_material("kfr_stancefix003_shadow_gray", (0.14, 0.14, 0.14, 1.0))

    left_foot = collect_objects(LEFT_FOOT_NAME_PARTS)
    right_foot = collect_objects(RIGHT_FOOT_NAME_PARTS)

    log(f"Left foot group objects found: {len(left_foot)}")
    log(f"Right foot group objects found: {len(right_foot)}")

    if left_foot:
        for obj in left_foot:
            log(f"  LF: {obj.name}")
    if right_foot:
        for obj in right_foot:
            log(f"  RF: {obj.name}")

    if not left_foot or not right_foot:
        log("Could not find boot groups. No foot splay correction applied.")
        log("Still adding bent leg geometry so the knee correction can be reviewed.")
    else:
        # Correct pigeon-toe.
        # Fix 002 rotated left by -7 and right by +7. To correct and arrive at outward splay,
        # left rotates positive, right rotates negative.
        correction = TARGET_OUTWARD_SPLAY_DEG
        if ASSUME_STANCE_FIX_002_ALREADY_RAN:
            correction += PREVIOUS_BAD_SPLAY_DEG

        left_pivot = group_top_center(left_foot)
        right_pivot = group_top_center(right_foot)
        rotate_objects_about_pivot(left_foot, math.radians(correction), "Z", left_pivot)
        rotate_objects_about_pivot(right_foot, math.radians(-correction), "Z", right_pivot)
        plant_group_to_ground(left_foot, GROUND_Z)
        plant_group_to_ground(right_foot, GROUND_Z)
        log(f"Corrected foot splay by {correction} degrees each side.")

    # Hide old straight tube legs and older marker geometry.
    hide_parts = list(HIDE_NAME_PARTS)
    if HIDE_MISALIGNED_PANTS_PANELS:
        hide_parts.extend(OLD_PANTS_PANEL_PARTS)
    hidden = hide_matching(hide_parts)
    log(f"Hidden old straight-leg / marker objects: {len(hidden)}")
    for name in hidden:
        log(f"  hidden: {name}")

    # Add new bent tube legs. These are visual pose geometry, not functional knee joints.
    build_bent_leg("left", LEFT_X, mat_cloth, mat_shadow, col)
    build_bent_leg("right", RIGHT_X, mat_cloth, mat_shadow, col)
    log("Added bent upper/lower tube legs and visual knee masses.")

    log("STANCE FIX 003 COMPLETE")
    log("Save as: kfr_blockout_v002_stance_fix_pass_003.blend")
    log("Review: front full-body, side full-body, boots/stance close-up.")


if __name__ == "__main__":
    main()
