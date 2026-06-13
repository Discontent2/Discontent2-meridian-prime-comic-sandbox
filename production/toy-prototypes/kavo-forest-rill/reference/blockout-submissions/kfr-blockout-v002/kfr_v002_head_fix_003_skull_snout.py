"""
KFR-BLOCKOUT-v002 Head Fix 003 — Skull / Snout Shape Refinement

Run this after:
    1. create_kfr_blockout_v002_starter_scene.py
    2. kfr_v002_head_fix_001.py
    3. kfr_v002_head_fix_002_quills_longer_irregular.py

Purpose:
    Improve the head blockout before moving on to the watch.

Changes:
    - Hides the original round skull sphere.
    - Hides previous snout / brow / mouth head-fix objects.
    - Adds a more saurian skull mass with a longer rear cranium and lower forehead.
    - Adds a tapered muzzle assembly instead of a rectangular box snout.
    - Adds cheek / jaw planes to reduce the snowman-round head read.
    - Adds a heavier brow shelf that makes the shades feel seated under the brow.
    - Adds a slightly angled sly mouth line.
    - Adds a stronger neck transition block.

Preserves:
    - Head Fix 002 longer irregular proto-quills.
    - Existing shades unless you manually change them later.
    - Body, garments, tail, hands, and watch.

Recommended file before running:
    kfr_blockout_v002_head_fix_pass_002.blend

Recommended file after running:
    kfr_blockout_v002_head_fix_pass_003.blend
"""

import math
import bpy

ROOT_COLLECTION_NAME = "kfr_blockout_v002_head_fix_003_skull_snout"

# Coordinate convention:
# X = left / right
# Y = front / back, negative Y is front, positive Y is back
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


def hide_matching_objects(patterns, suffix="_pre_headfix003_hidden"):
    hidden = []
    for obj in list(bpy.data.objects):
        if any(pattern in obj.name for pattern in patterns):
            # Do not hide the corrected Head Fix 002 quills.
            if "headfix002" in obj.name:
                continue
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


def add_ellipsoid(name, loc, scale, mat, col, segments=32, rings=16, rotation=(0.0, 0.0, 0.0)):
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
    obj.scale = (scale[0] / 2.0, scale[1] / 2.0, scale[2] / 2.0)
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


def raw_wedge_mesh(name, front_y, back_y, center_z, front_width, back_width, front_height, back_height, mat, col, x_offset=0.0):
    """Create a tapered cuboid wedge. Front is more negative Y."""
    fw = front_width / 2.0
    fh = front_height / 2.0
    bw = back_width / 2.0
    bh = back_height / 2.0
    verts = [
        (x_offset - fw, front_y, center_z - fh),
        (x_offset + fw, front_y, center_z - fh),
        (x_offset + fw, front_y, center_z + fh),
        (x_offset - fw, front_y, center_z + fh),
        (x_offset - bw, back_y, center_z - bh),
        (x_offset + bw, back_y, center_z - bh),
        (x_offset + bw, back_y, center_z + bh),
        (x_offset - bw, back_y, center_z + bh),
    ]
    faces = [
        (0, 1, 2, 3),
        (4, 7, 6, 5),
        (0, 4, 5, 1),
        (3, 2, 6, 7),
        (1, 5, 6, 2),
        (0, 3, 7, 4),
    ]
    mesh = bpy.data.meshes.new(name + "_mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.data.materials.append(mat)
    col.objects.link(obj)
    return obj


def apply_head_fix_003():
    print("KFR v002 Head Fix 003: skull / snout refinement starting")

    col = make_collection(ROOT_COLLECTION_NAME)

    mat_body = make_material("kfr_headfix003_body_gray", (0.48, 0.50, 0.50, 1.0))
    mat_shadow = make_material("kfr_headfix003_shadow_gray", (0.32, 0.34, 0.34, 1.0))
    mat_dark = make_material("kfr_headfix003_mouth_dark", (0.05, 0.05, 0.05, 1.0))

    hidden = hide_matching_objects([
        "kfr_part_001_head_primary_shades_blockout_skull",
        "kfr_part_001_head_primary_shades_blockout_snout",
        "kfr_part_001_head_primary_shades_blockout_brow",
        "kfr_part_001_head_primary_shades_blockout_forward_brow_headfix001",
        "kfr_part_001_head_primary_shades_blockout_snout_wedge_headfix001",
        "kfr_part_001_head_primary_shades_blockout_sly_mouth_line_headfix001",
        "kfr_part_001_head_primary_shades_blockout_mouth_line_plane",
        "kfr_neck_thick_swivel_ready_mass",
    ])
    print("Hidden previous skull/snout/brow/mouth objects:", hidden)

    # Saurian skull: less ball, more elongated rear cranium and lower brow slope.
    add_ellipsoid(
        name="kfr_part_001_head_skull_long_rear_cranium_headfix003",
        loc=(0.0, 1.2, 114.0),
        scale=(23.0, 23.5, 19.0),
        mat=mat_body,
        col=col,
    )

    add_ellipsoid(
        name="kfr_part_001_head_forehead_slope_mass_headfix003",
        loc=(0.0, -6.7, 115.2),
        scale=(21.0, 10.0, 12.0),
        mat=mat_body,
        col=col,
    )

    # Tapered upper muzzle and lower jaw. The upper muzzle is longer and narrower at the front.
    raw_wedge_mesh(
        name="kfr_part_001_head_upper_muzzle_taper_headfix003",
        front_y=-24.0,
        back_y=-7.5,
        center_z=111.3,
        front_width=9.5,
        back_width=17.5,
        front_height=6.2,
        back_height=9.2,
        mat=mat_body,
        col=col,
    )

    raw_wedge_mesh(
        name="kfr_part_001_head_lower_jaw_taper_headfix003",
        front_y=-23.2,
        back_y=-7.0,
        center_z=106.7,
        front_width=8.8,
        back_width=15.0,
        front_height=4.2,
        back_height=5.8,
        mat=mat_body,
        col=col,
    )

    # Cheek / jaw side planes help kill the round snowball head read.
    add_cube(
        name="kfr_part_001_head_left_cheek_plane_headfix003",
        loc=(8.8, -9.8, 109.0),
        dims=(2.4, 8.0, 9.0),
        mat=mat_shadow,
        col=col,
        rotation=(0.0, 0.0, math.radians(-5.0)),
    )
    add_cube(
        name="kfr_part_001_head_right_cheek_plane_headfix003",
        loc=(-8.8, -9.8, 109.0),
        dims=(2.4, 8.0, 9.0),
        mat=mat_shadow,
        col=col,
        rotation=(0.0, 0.0, math.radians(5.0)),
    )

    # Stronger brow shelf, placed so existing shades sit underneath it.
    add_cube(
        name="kfr_part_001_head_heavy_brow_shelf_headfix003",
        loc=(0.0, -12.4, 118.3),
        dims=(22.0, 4.8, 4.4),
        mat=mat_body,
        col=col,
    )
    add_cube(
        name="kfr_part_001_head_brow_center_notch_shadow_headfix003",
        loc=(0.0, -14.7, 116.9),
        dims=(3.0, 1.0, 2.2),
        mat=mat_shadow,
        col=col,
    )

    # Sly mouth line, slight asymmetry without becoming expression detail yet.
    add_cube(
        name="kfr_part_001_head_sly_mouth_line_headfix003",
        loc=(0.0, -24.25, 107.6),
        dims=(12.5, 0.65, 1.0),
        mat=mat_dark,
        col=col,
        rotation=(0.0, 0.0, math.radians(-4.0)),
    )

    # Neck transition, slightly thicker at back so the head no longer floats on a tube.
    add_ellipsoid(
        name="kfr_part_001_head_neck_transition_mass_headfix003",
        loc=(0.0, 2.0, 101.0),
        scale=(12.5, 10.0, 13.0),
        mat=mat_body,
        col=col,
        segments=24,
        rings=12,
    )

    print("KFR v002 Head Fix 003 complete.")
    print("Save as: kfr_blockout_v002_head_fix_pass_003.blend")
    print("Next review screenshots: head close-up, front view, side view.")


if __name__ == "__main__":
    apply_head_fix_003()
