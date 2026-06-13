"""
KFR-BLOCKOUT-v002 Head Fix 001

Run this on top of a working KFR-BLOCKOUT-v002 starter scene.

Purpose:
    Apply the first head correction pass without rebuilding the whole figure.

Fixes:
    - Hides the original sideways quill row.
    - Adds a new front-to-back low proto-quill crest.
    - Hides the original rectangular snout block.
    - Adds a tapered saurian snout wedge.
    - Hides the original brow marker.
    - Adds a heavier forward brow mass.
    - Hides the original straight mouth line.
    - Adds a slightly angled sly mouth marker.

Notes:
    This is still blockout geometry, not final sculpt detail.
    Save a copy before running this script.

Recommended file before running:
    kfr_blockout_v002_working_pass_001.blend

Recommended file after running:
    kfr_blockout_v002_head_fix_pass_001.blend
"""

import math
import bpy
from mathutils import Vector

ROOT_COLLECTION_NAME = "kfr_blockout_v002_head_fix_001"

# Coordinate convention from the starter scene:
# X = left/right
# Y = front/back, negative Y is front, positive Y is back
# Z = up


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


def hide_matching_objects(patterns, suffix="_pre_headfix_hidden"):
    hidden = []
    for obj in list(bpy.data.objects):
        if any(pattern in obj.name for pattern in patterns):
            if not obj.name.endswith(suffix):
                obj.name = obj.name + suffix
            obj.hide_viewport = True
            obj.hide_render = True
            hidden.append(obj.name)
    return hidden


def link_to_collection(obj, col):
    # Keep existing collection links as backups, but also place object in fix collection.
    if obj.name not in col.objects:
        try:
            col.objects.link(obj)
        except RuntimeError:
            pass


def raw_wedge_mesh(name, front_y, back_y, center_z, front_width, back_width, front_height, back_height, mat, col):
    """Create a tapered cuboid snout wedge. Front is more negative Y."""
    # Front plane
    fw = front_width / 2.0
    fh = front_height / 2.0
    # Back plane
    bw = back_width / 2.0
    bh = back_height / 2.0

    verts = [
        (-fw, front_y, center_z - fh),
        ( fw, front_y, center_z - fh),
        ( fw, front_y, center_z + fh),
        (-fw, front_y, center_z + fh),
        (-bw, back_y, center_z - bh),
        ( bw, back_y, center_z - bh),
        ( bw, back_y, center_z + bh),
        (-bw, back_y, center_z + bh),
    ]
    faces = [
        (0, 1, 2, 3),  # front
        (4, 7, 6, 5),  # back
        (0, 4, 5, 1),  # bottom
        (3, 2, 6, 7),  # top
        (1, 5, 6, 2),  # right
        (0, 3, 7, 4),  # left
    ]
    mesh = bpy.data.meshes.new(name + "_mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.data.materials.append(mat)
    col.objects.link(obj)
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


def add_blunt_quill(name, loc, height, base_radius, tip_radius, lean_degrees, mat, col):
    """Create one short blunt cone leaned toward the back of the skull."""
    bpy.ops.mesh.primitive_cone_add(
        vertices=18,
        radius1=base_radius,
        radius2=tip_radius,
        depth=height,
        location=loc,
        rotation=(math.radians(-lean_degrees), 0.0, 0.0),
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.data.materials.append(mat)
    link_to_collection(obj, col)
    return obj


def apply_head_fix():
    print("KFR v002 head fix 001 starting")

    col = make_collection(ROOT_COLLECTION_NAME)

    mat_body = make_material("kfr_headfix_body_gray", (0.48, 0.50, 0.50, 1.0))
    mat_dark = make_material("kfr_headfix_dark_gray", (0.06, 0.06, 0.06, 1.0))
    mat_quill = make_material("kfr_headfix_short_red_proto_quills", (0.62, 0.18, 0.10, 1.0))

    hidden = hide_matching_objects([
        "kfr_short_sparse_proto_quill",
        "kfr_part_001_head_primary_shades_blockout_snout",
        "kfr_part_001_head_primary_shades_blockout_brow_mass",
        "kfr_part_001_head_primary_shades_blockout_mouth_line_plane",
    ])
    print("Hidden starter head objects:", hidden)

    # New tapered saurian snout wedge.
    # Back plane is wider near skull, front plane is narrower at muzzle tip.
    raw_wedge_mesh(
        name="kfr_part_001_head_primary_shades_blockout_snout_wedge_headfix001",
        front_y=-21.0,
        back_y=-7.5,
        center_z=110.4,
        front_width=10.5,
        back_width=17.5,
        front_height=6.8,
        back_height=9.5,
        mat=mat_body,
        col=col,
    )

    # Heavier brow mass, forward and slightly lower so the shades feel tucked under it.
    add_cube(
        name="kfr_part_001_head_primary_shades_blockout_forward_brow_headfix001",
        loc=(0.0, -11.8, 118.2),
        dims=(22.0, 4.2, 4.8),
        mat=mat_body,
        col=col,
    )

    # Slightly angled sly mouth marker on the snout face.
    add_cube(
        name="kfr_part_001_head_primary_shades_blockout_sly_mouth_line_headfix001",
        loc=(0.0, -21.35, 107.9),
        dims=(12.5, 0.7, 1.0),
        mat=mat_dark,
        col=col,
        rotation=(0.0, 0.0, math.radians(-3.0)),
    )

    # New front-to-back low crest, centered on skull line.
    # Negative Y is front. Positive Y is back.
    quills = [
        ("front",  -5.2, 123.0, 2.6, 1.10, 0.55, 20),
        ("front_mid", -2.1, 124.1, 3.2, 1.20, 0.60, 22),
        ("center", 1.0, 125.0, 3.8, 1.35, 0.70, 24),
        ("back_mid", 4.0, 124.8, 3.5, 1.30, 0.65, 26),
        ("back", 7.0, 123.8, 2.8, 1.10, 0.55, 28),
    ]

    for label, y, z, height, base_radius, tip_radius, lean in quills:
        add_blunt_quill(
            name=f"kfr_short_sparse_proto_quill_headfix001_{label}",
            loc=(0.0, y, z),
            height=height,
            base_radius=base_radius,
            tip_radius=tip_radius,
            lean_degrees=lean,
            mat=mat_quill,
            col=col,
        )

    print("KFR v002 head fix 001 complete.")
    print("Save as: kfr_blockout_v002_head_fix_pass_001.blend")
    print("Next review screenshots: head close-up, front view, side view.")


if __name__ == "__main__":
    apply_head_fix()
