"""
KFR-BLOCKOUT-v002 Tail Fix 002 — Restore Stronger Tail Silhouette

Use this after:
    kfr_v002_lower_body_tail_balance_fix_001.py

Why this exists:
    Tail Balance Fix 001 improved leg balance, but the tail became underwhelming:
    too bead-like, too separated, and less useful as a character/balance silhouette.

Purpose:
    Keep the improved lower-body direction, but replace the underwhelming tail with a
    stronger version closer to the first tail concept: longer, more continuous, more
    substantial at the base, and clearly designed for future poseable segmentation.

Fixes:
    - Hides the Tail Balance Fix 001 tail pieces and dermal plates.
    - Builds a stronger overlapping segmented tail with a thicker base and smoother taper.
    - Uses oval/ellipsoid segments rather than small detached beads.
    - Adds larger dorsal dermal plates that echo the head quills.
    - Adds subtle collar/ring markers between segments to suggest future articulation.

Does not fix yet:
    - Pants details swallowed by lower-body rebuild.
    - Final boot proportions.
    - Production-ready mechanical tail joints.

Recommended file before running:
    kfr_blockout_v002_lower_body_tail_balance_fix_pass_001.blend

Recommended file after running:
    kfr_blockout_v002_tail_fix_pass_002.blend
"""

import math
import bpy
from mathutils import Vector

# -----------------------------------------------------------------------------
# TWEAKS
# -----------------------------------------------------------------------------

ROOT_COLLECTION_NAME = "kfr_blockout_v002_tail_fix_002_stronger_silhouette"

# Coordinate convention:
# X = character left/right. Positive X = character left.
# Y = front/back. Positive Y = tail/back direction.
# Z = up.

# Tail segments are intentionally overlapping/near-touching so the silhouette feels
# continuous, while ring markers still imply future articulation.
TAIL_SEGMENTS = [
    # suffix, y, z, length_y, width_x, height_z, pitch_degrees
    ("root_socket_mass", 13.8, 55.0, 7.0, 13.5, 9.0, -8),
    ("base_power",      19.5, 53.2, 10.5, 14.2, 8.2, -13),
    ("base_to_mid",     28.0, 49.2, 11.6, 12.3, 7.1, -18),
    ("mid_power",       37.0, 43.5, 11.0, 10.3, 6.0, -24),
    ("mid_to_tip",      45.2, 36.2, 9.4, 8.0, 4.9, -31),
    ("distal",          51.4, 28.3, 7.5, 5.9, 3.9, -36),
    ("tip",             55.5, 22.0, 5.0, 3.8, 2.8, -38),
]

DERMAL_PLATES = [
    # suffix, y, z, radius_base, height, lean_deg
    ("base_power", 19.2, 58.6, 2.2, 5.0, -18),
    ("base_power_b", 23.2, 56.6, 1.7, 4.1, -22),
    ("base_to_mid", 29.0, 53.1, 1.8, 4.2, -25),
    ("mid_power", 37.8, 47.2, 1.5, 3.6, -29),
    ("mid_to_tip", 45.5, 39.4, 1.2, 3.0, -34),
]

RING_MARKERS = [
    # y, z, width_x, length_y, height_z, pitch_deg
    (16.7, 54.4, 13.4, 1.0, 8.2, -10),
    (24.4, 51.1, 12.4, 1.0, 7.3, -16),
    (33.2, 46.4, 10.4, 0.9, 6.2, -21),
    (41.7, 39.6, 8.2, 0.8, 5.0, -28),
    (49.0, 31.4, 6.0, 0.7, 3.9, -34),
]

# Hide the underwhelming Tail Balance Fix 001 pieces and any older starter tail
# that survived previous passes.
HIDE_NAME_PARTS = [
    "kfr_tail_balance_fix_001_",
    "kfr_part_011_tail",
    "tail_keyed",
    "tail_socket",
]

# Keep anything this script creates if rerun is handled by clearing collection first.

# -----------------------------------------------------------------------------
# HELPERS
# -----------------------------------------------------------------------------


def log(msg):
    print(f"[KFR TAIL FIX 002] {msg}")


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


def name_has_any(obj, parts):
    low = obj.name.lower()
    return any(part.lower() in low for part in parts)


def hide_old_tail_parts():
    hidden = []
    for obj in bpy.data.objects:
        if obj.type != "MESH":
            continue
        if name_has_any(obj, HIDE_NAME_PARTS):
            obj.hide_viewport = True
            obj.hide_render = True
            hidden.append(obj.name)
    return hidden


def add_ellipsoid(name, loc, dims, mat, col, pitch_deg=0.0, segments=28, rings=14):
    bpy.ops.mesh.primitive_uv_sphere_add(
        segments=segments,
        ring_count=rings,
        radius=1.0,
        location=loc,
        rotation=(math.radians(pitch_deg), 0.0, 0.0),
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.scale = (dims[0] / 2.0, dims[1] / 2.0, dims[2] / 2.0)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    link_to_collection(obj, col)
    return obj


def add_cube(name, loc, dims, mat, col, pitch_deg=0.0):
    bpy.ops.mesh.primitive_cube_add(
        size=1.0,
        location=loc,
        rotation=(math.radians(pitch_deg), 0.0, 0.0),
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.dimensions = dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    link_to_collection(obj, col)
    return obj


def add_dermal_plate(name, loc, radius_base, height, mat, col, lean_deg):
    # vertices=4 gives a broad toy-safe triangular/quill-like plate, not a needle.
    bpy.ops.mesh.primitive_cone_add(
        vertices=4,
        radius1=radius_base,
        radius2=0.15,
        depth=height,
        location=loc,
        rotation=(math.radians(lean_deg), 0.0, math.radians(45.0)),
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.data.materials.append(mat)
    link_to_collection(obj, col)
    return obj


def build_tail(col, mat_tail, mat_plate, mat_ring, mat_socket):
    created = []

    # Pelvis socket bridge, still blue so it reads as engineering placeholder.
    created.append(add_cube(
        "kfr_tail_fix_002_clean_tail_socket_bridge_blue_placeholder",
        loc=(0.0, 11.8, 55.0),
        dims=(12.5, 3.6, 7.6),
        mat=mat_socket,
        col=col,
        pitch_deg=-7,
    ).name)

    for suffix, y, z, length_y, width_x, height_z, pitch in TAIL_SEGMENTS:
        created.append(add_ellipsoid(
            name=f"kfr_tail_fix_002_{suffix}_stronger_oval_poseable_segment",
            loc=(0.0, y, z),
            dims=(width_x, length_y, height_z),
            mat=mat_tail,
            col=col,
            pitch_deg=pitch,
        ).name)

    for idx, (y, z, width_x, length_y, height_z, pitch) in enumerate(RING_MARKERS, start=1):
        created.append(add_cube(
            name=f"kfr_tail_fix_002_articulation_ring_marker_{idx:02d}",
            loc=(0.0, y, z),
            dims=(width_x, length_y, height_z),
            mat=mat_ring,
            col=col,
            pitch_deg=pitch,
        ).name)

    for suffix, y, z, radius_base, height, lean in DERMAL_PLATES:
        created.append(add_dermal_plate(
            name=f"kfr_tail_fix_002_{suffix}_dorsal_dermal_plate",
            loc=(0.0, y, z),
            radius_base=radius_base,
            height=height,
            mat=mat_plate,
            col=col,
            lean_deg=lean,
        ).name)

    return created


# -----------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------


def main():
    log("Starting tail fix 002 stronger silhouette")

    col = make_collection(ROOT_COLLECTION_NAME)
    mat_tail = make_material("kfr_tail_fix_002_tail_body_gray", (0.48, 0.50, 0.50, 1.0))
    mat_plate = make_material("kfr_tail_fix_002_dermal_plate_red", (0.62, 0.18, 0.10, 1.0))
    mat_ring = make_material("kfr_tail_fix_002_articulation_ring_gray", (0.26, 0.27, 0.27, 1.0))
    mat_socket = make_material("kfr_tail_fix_002_socket_blue", (0.10, 0.45, 0.95, 0.75))

    hidden = hide_old_tail_parts()
    created = build_tail(col, mat_tail, mat_plate, mat_ring, mat_socket)

    log(f"Old tail objects hidden: {len(hidden)}")
    for name in hidden:
        log(f"  hidden: {name}")

    log(f"New stronger tail objects created: {len(created)}")
    for name in created:
        log(f"  created: {name}")

    log("TAIL FIX 002 COMPLETE")
    log("Save as: kfr_blockout_v002_tail_fix_pass_002.blend")
    log("Review: side tail silhouette, rear tail symmetry, and full-body shelf read.")


if __name__ == "__main__":
    main()
