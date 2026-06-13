"""
KFR-BLOCKOUT-v002 Lower Body / Tail Balance Fix 001

Run this after the current accepted lower-body stance pass.

Purpose:
    Balance Forest's lower-body and tail proportions without starting final sculpt.

Fixes:
    - Slightly strengthens visible leg blockout geometry where matching objects are found.
    - Hides prior tail blockout / stance-fix tail objects.
    - Rebuilds the tail as slimmer oval segmented pieces, less rotund than the current version.
    - Keeps a strong but not balloon-like tail base.
    - Adds pointed dorsal dermal plate placeholders to echo the head quills.
    - Preserves the final intent that the tail should become poseable / jointed later.

Important:
    This is still v002 blockout geometry. It does not create production-ready tail joints.

Recommended file before running:
    kfr_blockout_v002_stance_fix_pass_004.blend

Recommended file after running:
    kfr_blockout_v002_lower_body_tail_balance_fix_pass_001.blend
"""

import math
import bpy
from mathutils import Vector

# -----------------------------------------------------------------------------
# TWEAKS
# -----------------------------------------------------------------------------

ROOT_COLLECTION_NAME = "kfr_blockout_v002_lower_body_tail_balance_fix_001"

# Coordinate convention from the KFR starter scene:
# X = character left/right. Positive X = character left.
# Y = front/back. Negative Y = figure front. Positive Y = tail/back direction.
# Z = up.

# Light lower-body strengthening. This only affects found leg objects.
UPPER_LEG_SCALE_XY = 1.10
LOWER_LEG_SCALE_XY = 1.08
KNEE_MASS_SCALE_XY = 1.08

# New tail path and proportions.
TAIL_ROOT = Vector((0.0, 13.4, 55.5))
TAIL_SEGMENTS = [
    # name_suffix, center_y, center_z, length_y, width_x, height_z
    ("base_socket", 15.2, 54.8, 8.5, 13.0, 8.2),
    ("base_muscle", 22.4, 51.8, 10.8, 12.0, 7.3),
    ("mid_01",      31.2, 47.1, 11.0, 10.2, 6.2),
    ("mid_02",      40.2, 40.7, 10.8, 8.6, 5.4),
    ("distal",      48.5, 32.5, 9.2, 6.8, 4.5),
    ("tip",         55.0, 24.2, 6.8, 4.8, 3.4),
]

# Dermal plates: one or two per main segment can be sculpted later. Here we place one per segment.
DERMAL_PLATES = [
    # segment_name_suffix, y, z, width_x, depth_y, height_z
    ("base_muscle", 21.8, 56.2, 3.8, 2.4, 4.2),
    ("mid_01",      31.0, 51.3, 3.4, 2.2, 3.8),
    ("mid_02",      40.0, 44.7, 3.0, 2.0, 3.4),
    ("distal",      48.2, 35.9, 2.4, 1.7, 2.8),
]

# Existing objects to hide.
HIDE_TAIL_NAME_PARTS = [
    "tail",
    "kfr_part_011_tail",
    "tail_keyed",
]

# Do not hide this new script's collection if the script is rerun; it is deleted first.
KEEP_IF_NAME_PARTS = [
    "lower_body_tail_balance_fix_001",
]

LEG_STRENGTHEN_NAME_PARTS = [
    "upper_leg_longer_bent_tube_connected",
    "lower_leg_longer_bent_tube_connected",
    "upper_leg_bent_tube",
    "lower_leg_bent_tube",
    "knee_mass_visual",
]

# -----------------------------------------------------------------------------
# HELPERS
# -----------------------------------------------------------------------------


def log(message):
    print(f"[KFR TAIL BALANCE FIX 001] {message}")


def make_collection(name):
    existing = bpy.data.collections.get(name)
    if existing:
        # Clear previous run output.
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


def name_has_any(obj, parts):
    low = obj.name.lower()
    return any(part.lower() in low for part in parts)


def scale_matching_legs():
    changed = []
    for obj in bpy.data.objects:
        if obj.type != "MESH":
            continue
        if not name_has_any(obj, LEG_STRENGTHEN_NAME_PARTS):
            continue
        low = obj.name.lower()
        if "upper" in low:
            obj.scale.x *= UPPER_LEG_SCALE_XY
            obj.scale.y *= UPPER_LEG_SCALE_XY
        elif "lower" in low:
            obj.scale.x *= LOWER_LEG_SCALE_XY
            obj.scale.y *= LOWER_LEG_SCALE_XY
        elif "knee" in low:
            obj.scale.x *= KNEE_MASS_SCALE_XY
            obj.scale.y *= KNEE_MASS_SCALE_XY
        changed.append(obj.name)
    return changed


def hide_old_tail():
    hidden = []
    for obj in bpy.data.objects:
        if obj.type != "MESH":
            continue
        if name_has_any(obj, KEEP_IF_NAME_PARTS):
            continue
        if name_has_any(obj, HIDE_TAIL_NAME_PARTS):
            obj.hide_viewport = True
            obj.hide_render = True
            hidden.append(obj.name)
    return hidden


def add_ellipsoid(name, loc, dims, mat, col, rotation=(0.0, 0.0, 0.0), segments=24, rings=12):
    bpy.ops.mesh.primitive_uv_sphere_add(
        segments=segments,
        ring_count=rings,
        radius=1.0,
        location=loc,
        rotation=rotation,
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.scale = (dims[0] / 2.0, dims[1] / 2.0, dims[2] / 2.0)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    link_to_collection(obj, col)
    return obj


def add_dermal_plate(name, loc, dims, mat, col, lean_deg=-18.0):
    # Four-sided cone gives a chunky triangular toy-safe plate.
    bpy.ops.mesh.primitive_cone_add(
        vertices=4,
        radius1=max(dims[0], dims[1]) / 2.0,
        radius2=0.0,
        depth=dims[2],
        location=loc,
        rotation=(math.radians(lean_deg), 0.0, math.radians(45.0)),
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.scale.x *= max(0.55, dims[0] / max(dims[1], 0.01))
    obj.scale.y *= max(0.55, dims[1] / max(dims[0], 0.01))
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    link_to_collection(obj, col)
    return obj


def add_socket_marker(col, mat_socket):
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0.0, 12.2, 55.0))
    obj = bpy.context.object
    obj.name = "kfr_tail_balance_fix_001_clean_blue_socket_marker"
    obj.data.name = obj.name + "_mesh"
    obj.dimensions = (12.5, 4.0, 8.0)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat_socket)
    link_to_collection(obj, col)
    return obj


def rebuild_tail(col, mat_tail, mat_plate, mat_socket):
    created = []
    add_socket_marker(col, mat_socket)
    for suffix, y, z, length_y, width_x, height_z in TAIL_SEGMENTS:
        obj = add_ellipsoid(
            name=f"kfr_tail_balance_fix_001_{suffix}_oval_segment_poseable_placeholder",
            loc=(0.0, y, z),
            dims=(width_x, length_y, height_z),
            mat=mat_tail,
            col=col,
            rotation=(math.radians(-13.0), 0.0, 0.0),
        )
        created.append(obj.name)

    for suffix, y, z, width_x, depth_y, height_z in DERMAL_PLATES:
        plate = add_dermal_plate(
            name=f"kfr_tail_balance_fix_001_{suffix}_dorsal_dermal_plate",
            loc=(0.0, y, z),
            dims=(width_x, depth_y, height_z),
            mat=mat_plate,
            col=col,
        )
        created.append(plate.name)
    return created


# -----------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------


def main():
    log("Starting lower body / tail balance fix 001")

    col = make_collection(ROOT_COLLECTION_NAME)
    mat_tail = make_material("kfr_tail_balance_fix_001_tail_gray", (0.48, 0.50, 0.50, 1.0))
    mat_plate = make_material("kfr_tail_balance_fix_001_dermal_plate_red", (0.62, 0.18, 0.10, 1.0))
    mat_socket = make_material("kfr_tail_balance_fix_001_socket_blue", (0.10, 0.45, 0.95, 0.75))

    strengthened = scale_matching_legs()
    hidden = hide_old_tail()
    created = rebuild_tail(col, mat_tail, mat_plate, mat_socket)

    log(f"Leg objects strengthened: {len(strengthened)}")
    for name in strengthened:
        log(f"  strengthened: {name}")

    log(f"Old tail objects hidden: {len(hidden)}")
    for name in hidden:
        log(f"  hidden: {name}")

    log(f"New tail/socket/plate objects created: {len(created)}")
    for name in created:
        log(f"  created: {name}")

    log("LOWER BODY / TAIL BALANCE FIX 001 COMPLETE")
    log("Save as: kfr_blockout_v002_lower_body_tail_balance_fix_pass_001.blend")
    log("Review: side tail silhouette, rear tail symmetry, full-body front, and tail socket close-up.")


if __name__ == "__main__":
    main()
