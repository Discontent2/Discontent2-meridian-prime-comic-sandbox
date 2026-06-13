"""
KFR-BLOCKOUT-v002 Head Fix 004 — Head Rebalance Cleanup

Run this after:
    1. create_kfr_blockout_v002_starter_scene.py
    2. kfr_v002_head_fix_001.py
    3. kfr_v002_head_fix_002_quills_longer_irregular.py
    4. kfr_v002_head_fix_003_skull_snout.py

Purpose:
    Clean up Head Fix 003, which overcorrected the skull and muzzle.

Changes:
    - Preserves Head Fix 002 longer irregular proto-quills.
    - Hides bulky Head Fix 003 skull / snout / brow / cheek / neck pieces.
    - Adds a smaller, lower, less egg-shaped skull mass.
    - Adds a shorter tapered muzzle and lower jaw.
    - Adds slimmer cheek planes.
    - Adds a brow shelf that seats the shades without creating a forehead plank.
    - Adds a cleaner neck transition that does not crowd the head.

Recommended file before running:
    kfr_blockout_v002_head_fix_pass_003.blend

Recommended file after running:
    kfr_blockout_v002_head_fix_pass_004.blend
"""

import math
import bpy

ROOT_COLLECTION_NAME = "kfr_blockout_v002_head_fix_004_rebalance"

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


def hide_matching_objects(patterns, suffix="_pre_headfix004_hidden"):
    hidden = []
    for obj in list(bpy.data.objects):
        if any(pattern in obj.name for pattern in patterns):
            # Keep the approved longer irregular quills from Head Fix 002.
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


def apply_head_fix_004():
    print("KFR v002 Head Fix 004: rebalance cleanup starting")

    col = make_collection(ROOT_COLLECTION_NAME)

    mat_body = make_material("kfr_headfix004_body_gray", (0.48, 0.50, 0.50, 1.0))
    mat_shadow = make_material("kfr_headfix004_shadow_gray", (0.31, 0.33, 0.33, 1.0))
    mat_dark = make_material("kfr_headfix004_mouth_dark", (0.05, 0.05, 0.05, 1.0))

    hidden = hide_matching_objects([
        "kfr_part_001_head_skull_long_rear_cranium_headfix003",
        "kfr_part_001_head_forehead_slope_mass_headfix003",
        "kfr_part_001_head_upper_muzzle_taper_headfix003",
        "kfr_part_001_head_lower_jaw_taper_headfix003",
        "kfr_part_001_head_left_cheek_plane_headfix003",
        "kfr_part_001_head_right_cheek_plane_headfix003",
        "kfr_part_001_head_heavy_brow_shelf_headfix003",
        "kfr_part_001_head_brow_center_notch_shadow_headfix003",
        "kfr_part_001_head_sly_mouth_line_headfix003",
        "kfr_part_001_head_neck_transition_mass_headfix003",
        # Also hide any remaining older head-fix 001 geometry if it was still visible.
        "kfr_part_001_head_primary_shades_blockout_snout_wedge_headfix001",
        "kfr_part_001_head_primary_shades_blockout_forward_brow_headfix001",
        "kfr_part_001_head_primary_shades_blockout_sly_mouth_line_headfix001",
    ])
    print("Hidden bulky previous head objects:", hidden)

    # Smaller, lower, less egg-shaped skull. Still elongated front/back, but no melon dome.
    add_ellipsoid(
        name="kfr_part_001_head_skull_rebalanced_headfix004",
        loc=(0.0, 0.6, 113.6),
        scale=(21.0, 20.0, 17.0),
        mat=mat_body,
        col=col,
        segments=32,
        rings=16,
    )

    # Rear cranium pad gives the back-of-skull read without becoming huge.
    add_ellipsoid(
        name="kfr_part_001_head_rear_cranium_pad_headfix004",
        loc=(0.0, 6.0, 113.0),
        scale=(18.0, 10.0, 15.0),
        mat=mat_body,
        col=col,
        segments=24,
        rings=12,
    )

    # Subtler forehead / brow transition, less plank-like.
    add_ellipsoid(
        name="kfr_part_001_head_forehead_slope_rebalanced_headfix004",
        loc=(0.0, -6.2, 114.8),
        scale=(19.0, 8.0, 9.0),
        mat=mat_body,
        col=col,
        segments=24,
        rings=12,
    )

    # Shorter upper muzzle. Still tapered, no long shoebox.
    raw_wedge_mesh(
        name="kfr_part_001_head_upper_muzzle_rebalanced_headfix004",
        front_y=-21.6,
        back_y=-7.4,
        center_z=111.0,
        front_width=8.6,
        back_width=16.2,
        front_height=5.8,
        back_height=8.2,
        mat=mat_body,
        col=col,
    )

    # Shorter lower jaw, tucked under the upper muzzle.
    raw_wedge_mesh(
        name="kfr_part_001_head_lower_jaw_rebalanced_headfix004",
        front_y=-20.8,
        back_y=-7.0,
        center_z=106.6,
        front_width=8.0,
        back_width=13.8,
        front_height=3.8,
        back_height=5.2,
        mat=mat_body,
        col=col,
    )

    # Slimmer cheek planes. These are hint planes, not big side blocks.
    add_cube(
        name="kfr_part_001_head_left_cheek_plane_slim_headfix004",
        loc=(8.1, -9.3, 109.0),
        dims=(1.4, 6.2, 7.2),
        mat=mat_shadow,
        col=col,
        rotation=(0.0, 0.0, math.radians(-4.0)),
    )
    add_cube(
        name="kfr_part_001_head_right_cheek_plane_slim_headfix004",
        loc=(-8.1, -9.3, 109.0),
        dims=(1.4, 6.2, 7.2),
        mat=mat_shadow,
        col=col,
        rotation=(0.0, 0.0, math.radians(4.0)),
    )

    # Brow shelf: narrower front-to-back, seated above existing shades.
    add_cube(
        name="kfr_part_001_head_brow_shelf_rebalanced_headfix004",
        loc=(0.0, -12.0, 117.9),
        dims=(21.0, 3.4, 3.6),
        mat=mat_body,
        col=col,
    )
    add_cube(
        name="kfr_part_001_head_brow_center_notch_subtle_headfix004",
        loc=(0.0, -13.9, 116.6),
        dims=(2.5, 0.8, 1.8),
        mat=mat_shadow,
        col=col,
    )

    # Sly mouth line, shortened to fit the shorter muzzle.
    add_cube(
        name="kfr_part_001_head_sly_mouth_line_rebalanced_headfix004",
        loc=(0.0, -21.95, 107.4),
        dims=(11.0, 0.55, 0.9),
        mat=mat_dark,
        col=col,
        rotation=(0.0, 0.0, math.radians(-3.5)),
    )

    # Cleaner neck transition: lower and smaller, so the head sits naturally.
    add_ellipsoid(
        name="kfr_part_001_head_neck_transition_rebalanced_headfix004",
        loc=(0.0, 1.6, 100.6),
        scale=(10.5, 8.5, 11.0),
        mat=mat_body,
        col=col,
        segments=20,
        rings=10,
    )

    print("KFR v002 Head Fix 004 complete.")
    print("Save as: kfr_blockout_v002_head_fix_pass_004.blend")
    print("Next review screenshots: head close-up, front view, side view.")


if __name__ == "__main__":
    apply_head_fix_004()
