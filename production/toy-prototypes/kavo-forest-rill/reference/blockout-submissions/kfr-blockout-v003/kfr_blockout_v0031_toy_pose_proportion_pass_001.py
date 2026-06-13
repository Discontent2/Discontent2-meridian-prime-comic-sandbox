"""
KFR-BLOCKOUT-v003.1 Toy Pose / Proportion Pass 001

Purpose
-------
Use the current v003 blockout as the foundation, then push the figure toward
an exaggerated hunched, chunky, creature-toy stance inspired by the user's
reference toy while preserving Kavo "Forest" Rill's own design language.

This pass is intentionally NON-DESTRUCTIVE.
It creates an overlay collection of guide / sculpt-target masses rather than
trying to permanently rewrite the existing base meshes.

Primary goals
-------------
- push the silhouette toward a toyetic creature stance
- add stronger forward head / muzzle projection
- round the torso so it reads less like a flat box and more like a toy body
- suggest a cropped jacket / shirt shell over a rounded torso
- push the lower body toward a crouched, chunkier leg rhythm
- reinforce oversized hands / feet / tail balance
- make the tail read as a lower counterbalance support

Suggested run order
-------------------
Run after the current v003 reboot / silhouette reboot scene is loaded.

Suggested save-as after running
-------------------------------
    kfr_blockout_v0031_toy_pose_proportion_pass_001.blend

Notes
-----
This pass does NOT require exact object names from the current scene.
It overlays proportional targets that can be used as visual sculpt guides.
"""

import math
import bpy
from mathutils import Vector

ROOT_COLLECTION_NAME = "kfr_blockout_v0031_toy_pose_proportion_pass_001"
TEXT_BLOCK_NAME = "KFR_V0031_TOY_POSE_PROPORTION_PASS_001_NOTES"

# -----------------------------------------------------------------------------
# Visibility controls
# -----------------------------------------------------------------------------

HIDE_PREVIOUS_V0031_PASSES = True
HIDE_OBJECT_FRAGMENTS = [
    "kfr_blockout_v0031_",
    "kfr_v0031_",
    "kfr_toy_pose_proportion_",
]

# -----------------------------------------------------------------------------
# Materials
# -----------------------------------------------------------------------------

MAT_GUIDE_SKIN = (0.84, 0.83, 0.68, 1.0)
MAT_GUIDE_BODY = (0.88, 0.88, 0.88, 1.0)
MAT_GUIDE_DARK = (0.12, 0.12, 0.12, 1.0)
MAT_GUIDE_ACCENT = (0.98, 0.61, 0.23, 1.0)
MAT_GUIDE_SOFT = (0.62, 0.73, 0.95, 0.55)
MAT_GUIDE_WARNING = (0.91, 0.78, 0.28, 0.7)

# Coordinate assumption for the user's working scene:
#   X = character left/right (positive X = character left)
#   Y = back/front-ish, with negative Y reading more toward character front
#   Z = up
# The placements below are tuned as a stylized overlay for the current v003 toy
# reboot screenshots rather than as exact hard-surface production geometry.

# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------


def log(msg):
    print(f"[KFR V003.1 TOY POSE] {msg}")



def has_fragment(name, fragments):
    low = name.lower()
    return any(fragment.lower() in low for fragment in fragments)



def hide_previous_objects():
    hidden = []
    if not HIDE_PREVIOUS_V0031_PASSES:
        return hidden
    for obj in bpy.data.objects:
        if obj.type == "MESH" and has_fragment(obj.name, HIDE_OBJECT_FRAGMENTS):
            obj.hide_viewport = True
            obj.hide_render = True
            hidden.append(obj.name)
    return hidden



def make_collection(name):
    existing = bpy.data.collections.get(name)
    if existing:
        for obj in list(existing.objects):
            bpy.data.objects.remove(obj, do_unlink=True)
        return existing
    col = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(col)
    return col



def unlink_except(obj, keep_col):
    for col in list(obj.users_collection):
        if col != keep_col:
            try:
                col.objects.unlink(obj)
            except RuntimeError:
                pass



def make_material(name, rgba, roughness=0.8, metallic=0.0):
    existing = bpy.data.materials.get(name)
    if existing:
        return existing
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = rgba
    try:
        mat.use_nodes = True
        bsdf = mat.node_tree.nodes.get("Principled BSDF")
        if bsdf:
            bsdf.inputs["Base Color"].default_value = rgba
            bsdf.inputs["Roughness"].default_value = roughness
            bsdf.inputs["Metallic"].default_value = metallic
            if "Alpha" in bsdf.inputs:
                bsdf.inputs["Alpha"].default_value = rgba[3]
        if rgba[3] < 1.0:
            mat.blend_method = "BLEND"
            mat.shadow_method = "HASHED"
    except Exception:
        pass
    return mat



def add_bevel(obj, amount=0.2, segments=3):
    if amount <= 0:
        return obj
    mod = obj.modifiers.new(name="bevel", type="BEVEL")
    mod.width = amount
    mod.segments = segments
    mod.affect = "EDGES"
    try:
        wn = obj.modifiers.new(name="weighted_normals", type="WEIGHTED_NORMAL")
        wn.keep_sharp = True
    except Exception:
        pass
    return obj



def shade_smooth(obj):
    try:
        for poly in obj.data.polygons:
            poly.use_smooth = True
    except Exception:
        pass
    return obj



def apply_material(obj, mat):
    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)
    return obj



def finalize_object(obj, col, mat=None, bevel=None, smooth=False):
    if mat is not None:
        apply_material(obj, mat)
    if bevel is not None:
        add_bevel(obj, bevel)
    if smooth:
        shade_smooth(obj)
    try:
        col.objects.link(obj)
    except RuntimeError:
        pass
    unlink_except(obj, col)
    return obj



def add_cube(name, loc, dims, mat, col, rotation=(0.0, 0.0, 0.0), bevel=0.22):
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=loc, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.dimensions = dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    return finalize_object(obj, col, mat=mat, bevel=bevel, smooth=False)



def add_uv_sphere(name, loc, dims, mat, col, rotation=(0.0, 0.0, 0.0), segments=32, rings=16):
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
    return finalize_object(obj, col, mat=mat, smooth=True)



def add_ico_sphere(name, loc, dims, mat, col, rotation=(0.0, 0.0, 0.0), subdivisions=2):
    bpy.ops.mesh.primitive_ico_sphere_add(
        subdivisions=subdivisions,
        radius=1.0,
        location=loc,
        rotation=rotation,
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.scale = (dims[0] / 2.0, dims[1] / 2.0, dims[2] / 2.0)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    return finalize_object(obj, col, mat=mat, smooth=True)



def add_cylinder(name, loc, dims, mat, col, rotation=(0.0, 0.0, 0.0), vertices=24, bevel=0.18):
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=vertices,
        radius=1.0,
        depth=2.0,
        location=loc,
        rotation=rotation,
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.dimensions = dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    return finalize_object(obj, col, mat=mat, bevel=bevel, smooth=True)



def add_cone(name, loc, dims, mat, col, rotation=(0.0, 0.0, 0.0), vertices=20, bevel=0.08):
    bpy.ops.mesh.primitive_cone_add(
        vertices=vertices,
        radius1=1.0,
        radius2=0.22,
        depth=2.0,
        location=loc,
        rotation=rotation,
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.dimensions = dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    return finalize_object(obj, col, mat=mat, bevel=bevel, smooth=True)



def add_empty(name, loc, col, empty_type='PLAIN_AXES', size=0.25):
    bpy.ops.object.empty_add(type=empty_type, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.empty_display_size = size
    try:
        col.objects.link(obj)
    except RuntimeError:
        pass
    unlink_except(obj, col)
    return obj



def parent_many(parent, children):
    for child in children:
        child.parent = parent



def add_measure_guide(col, mat):
    guide = add_cylinder(
        "kfr_v0031_scale_guide_127mm",
        loc=(8.5, 0.0, 63.5),
        dims=(1.4, 1.4, 127.0),
        mat=mat,
        col=col,
        rotation=(0.0, 0.0, 0.0),
        vertices=12,
        bevel=0.0,
    )
    guide.display_type = 'WIRE'
    return guide



def ensure_text_block():
    notes = bpy.data.texts.get(TEXT_BLOCK_NAME)
    if notes is None:
        notes = bpy.data.texts.new(TEXT_BLOCK_NAME)
    notes.clear()
    notes.write(
        "KFR-BLOCKOUT-v003.1 Toy Pose / Proportion Pass 001\n"
        "===================================================\n\n"
        "Intent:\n"
        "- use v003 as the base\n"
        "- push figure toward hunched creature-toy stance\n"
        "- round torso and belly\n"
        "- project head / muzzle forward\n"
        "- create stronger thigh / shin / boot rhythm\n"
        "- lower tail for counterbalance support\n\n"
        "Workflow suggestion:\n"
        "1. Toggle the new collection on/off to compare against the base.\n"
        "2. Use the new overlay masses as placement / sculpt guides.\n"
        "3. Match the foundation meshes to the guide shapes.\n"
        "4. Keep hands, boots, and head slightly oversized for toy read.\n"
        "5. Once major volumes are transferred, continue into face / jacket / skin detail.\n"
    )


# -----------------------------------------------------------------------------
# Construction
# -----------------------------------------------------------------------------


def build_center_guides(col, mats):
    skin, body, dark, accent, soft, warn = mats
    center = []

    neck = add_cylinder(
        "kfr_v0031_neck_thickener",
        loc=(0.0, -1.6, 105.0),
        dims=(8.8, 8.8, 8.5),
        mat=skin,
        col=col,
        rotation=(math.radians(83), 0.0, 0.0),
        vertices=20,
        bevel=0.10,
    )
    center.append(neck)

    head_mass = add_uv_sphere(
        "kfr_v0031_head_mass",
        loc=(0.0, -4.5, 117.5),
        dims=(28.0, 25.0, 24.0),
        mat=skin,
        col=col,
        segments=36,
        rings=18,
    )
    center.append(head_mass)

    muzzle = add_uv_sphere(
        "kfr_v0031_muzzle_mass",
        loc=(0.0, -13.0, 114.0),
        dims=(18.0, 14.0, 11.5),
        mat=skin,
        col=col,
        segments=32,
        rings=16,
    )
    center.append(muzzle)

    upper_jaw = add_cube(
        "kfr_v0031_upper_jaw_block",
        loc=(0.0, -13.4, 115.0),
        dims=(13.5, 11.5, 6.0),
        mat=body,
        col=col,
        rotation=(math.radians(3), 0.0, 0.0),
        bevel=0.30,
    )
    center.append(upper_jaw)

    lower_jaw = add_cube(
        "kfr_v0031_lower_jaw_block",
        loc=(0.0, -11.8, 110.0),
        dims=(12.8, 9.0, 3.2),
        mat=dark,
        col=col,
        rotation=(math.radians(-3), 0.0, 0.0),
        bevel=0.18,
    )
    center.append(lower_jaw)

    chest = add_uv_sphere(
        "kfr_v0031_chest_round_mass",
        loc=(0.0, -0.8, 86.0),
        dims=(34.0, 22.0, 31.0),
        mat=body,
        col=col,
    )
    center.append(chest)

    belly = add_uv_sphere(
        "kfr_v0031_belly_mass",
        loc=(0.0, -1.2, 74.0),
        dims=(31.0, 19.0, 22.0),
        mat=skin,
        col=col,
    )
    center.append(belly)

    jacket_shell = add_cube(
        "kfr_v0031_cropped_jacket_shell",
        loc=(0.0, -0.6, 82.0),
        dims=(34.0, 22.5, 33.0),
        mat=soft,
        col=col,
        bevel=0.40,
    )
    center.append(jacket_shell)

    torso_harness = add_cube(
        "kfr_v0031_harness_front_simplify",
        loc=(0.0, -10.5, 80.5),
        dims=(18.0, 1.6, 20.0),
        mat=dark,
        col=col,
        bevel=0.12,
    )
    center.append(torso_harness)

    belt = add_cube(
        "kfr_v0031_waist_belt_mass",
        loc=(0.0, -1.5, 66.8),
        dims=(33.0, 3.8, 3.5),
        mat=dark,
        col=col,
        bevel=0.16,
    )
    center.append(belt)

    pelvis = add_uv_sphere(
        "kfr_v0031_pelvis_chunk_mass",
        loc=(0.0, -0.5, 58.5),
        dims=(20.0, 16.0, 13.0),
        mat=skin,
        col=col,
        segments=28,
        rings=14,
    )
    center.append(pelvis)

    shorts_front = add_cube(
        "kfr_v0031_shorts_front_block",
        loc=(0.0, -6.4, 58.8),
        dims=(19.5, 7.4, 12.4),
        mat=warn,
        col=col,
        bevel=0.22,
    )
    center.append(shorts_front)

    tail_root = add_uv_sphere(
        "kfr_v0031_tail_root_support",
        loc=(0.0, 10.0, 57.0),
        dims=(14.0, 16.0, 12.0),
        mat=skin,
        col=col,
    )
    center.append(tail_root)

    return center



def build_side(col, mats, side_sign=1.0):
    skin, body, dark, accent, soft, warn = mats
    side_name = "L" if side_sign > 0 else "R"
    parts = []

    shoulder = add_uv_sphere(
        f"kfr_v0031_{side_name}_shoulder_ball",
        loc=(15.8 * side_sign, -1.5, 87.5),
        dims=(10.8, 10.8, 10.8),
        mat=body,
        col=col,
    )
    parts.append(shoulder)

    upper_arm = add_uv_sphere(
        f"kfr_v0031_{side_name}_upper_arm_sausage",
        loc=(20.5 * side_sign, -1.0, 76.2),
        dims=(8.8, 9.5, 18.5),
        mat=body,
        col=col,
        rotation=(math.radians(5 * -side_sign), 0.0, math.radians(6 * side_sign)),
    )
    parts.append(upper_arm)

    elbow = add_uv_sphere(
        f"kfr_v0031_{side_name}_elbow_ball",
        loc=(22.5 * side_sign, 0.0, 65.0),
        dims=(7.5, 7.5, 7.0),
        mat=body,
        col=col,
    )
    parts.append(elbow)

    forearm = add_uv_sphere(
        f"kfr_v0031_{side_name}_forearm_sausage",
        loc=(24.0 * side_sign, -0.3, 54.8),
        dims=(8.0, 8.8, 17.0),
        mat=body,
        col=col,
        rotation=(math.radians(6 * side_sign), 0.0, math.radians(8 * side_sign)),
    )
    parts.append(forearm)

    wrist = add_cube(
        f"kfr_v0031_{side_name}_wrist_cuff",
        loc=(25.3 * side_sign, -0.2, 45.3),
        dims=(7.4, 5.5, 4.0),
        mat=dark,
        col=col,
        bevel=0.14,
    )
    parts.append(wrist)

    hand = add_uv_sphere(
        f"kfr_v0031_{side_name}_hand_mass",
        loc=(27.5 * side_sign, -1.8, 40.0),
        dims=(12.8, 9.0, 6.3),
        mat=skin,
        col=col,
        rotation=(0.0, math.radians(18 * side_sign), math.radians(12 * side_sign)),
        segments=24,
        rings=14,
    )
    parts.append(hand)

    thumb = add_uv_sphere(
        f"kfr_v0031_{side_name}_thumb_mass",
        loc=(23.9 * side_sign, -3.9, 39.0),
        dims=(3.8, 3.5, 5.8),
        mat=skin,
        col=col,
        rotation=(math.radians(35), math.radians(20 * side_sign), math.radians(15 * side_sign)),
        segments=18,
        rings=10,
    )
    parts.append(thumb)

    finger_x_offsets = [2.8, 0.8, -1.2]
    finger_z = [37.4, 36.9, 36.0]
    finger_y = [-4.9, -5.3, -5.1]
    for idx, (fx, fy, fz) in enumerate(zip(finger_x_offsets, finger_y, finger_z), start=1):
        finger = add_uv_sphere(
            f"kfr_v0031_{side_name}_finger_{idx}",
            loc=((27.4 + fx) * side_sign, fy, fz),
            dims=(3.4, 3.0, 6.2),
            mat=skin,
            col=col,
            rotation=(math.radians(52), math.radians(8 * side_sign), math.radians(10 * side_sign)),
            segments=18,
            rings=10,
        )
        parts.append(finger)

        claw = add_cone(
            f"kfr_v0031_{side_name}_finger_{idx}_claw",
            loc=((27.8 + fx) * side_sign, fy - 1.4, fz - 2.4),
            dims=(1.1, 1.1, 2.6),
            mat=dark,
            col=col,
            rotation=(math.radians(90), 0.0, 0.0),
            vertices=10,
            bevel=0.0,
        )
        parts.append(claw)

    hip = add_uv_sphere(
        f"kfr_v0031_{side_name}_hip_ball",
        loc=(7.5 * side_sign, 0.0, 57.0),
        dims=(8.5, 8.5, 8.5),
        mat=skin,
        col=col,
    )
    parts.append(hip)

    thigh = add_uv_sphere(
        f"kfr_v0031_{side_name}_thigh_chunk",
        loc=(7.2 * side_sign, -0.4, 47.0),
        dims=(10.5, 11.0, 21.0),
        mat=skin,
        col=col,
        rotation=(math.radians(4), 0.0, math.radians(-5 * side_sign)),
    )
    parts.append(thigh)

    shorts_leg = add_cube(
        f"kfr_v0031_{side_name}_shorts_leg_panel",
        loc=(9.2 * side_sign, -1.8, 51.0),
        dims=(7.4, 4.6, 10.5),
        mat=warn,
        col=col,
        rotation=(0.0, 0.0, math.radians(3 * -side_sign)),
        bevel=0.18,
    )
    parts.append(shorts_leg)

    knee = add_uv_sphere(
        f"kfr_v0031_{side_name}_knee_ball",
        loc=(6.4 * side_sign, -0.8, 36.2),
        dims=(7.8, 7.3, 7.4),
        mat=body,
        col=col,
    )
    parts.append(knee)

    shin = add_cylinder(
        f"kfr_v0031_{side_name}_shin_column",
        loc=(5.9 * side_sign, -0.6, 24.5),
        dims=(7.6, 7.6, 19.5),
        mat=body,
        col=col,
        rotation=(math.radians(2), math.radians(4 * -side_sign), math.radians(0)),
        vertices=18,
        bevel=0.12,
    )
    parts.append(shin)

    calf = add_uv_sphere(
        f"kfr_v0031_{side_name}_calf_back_mass",
        loc=(7.8 * side_sign, 2.4, 24.0),
        dims=(5.2, 7.0, 12.5),
        mat=skin,
        col=col,
    )
    parts.append(calf)

    ankle = add_uv_sphere(
        f"kfr_v0031_{side_name}_ankle_ball",
        loc=(5.8 * side_sign, -0.8, 14.2),
        dims=(6.2, 6.0, 5.2),
        mat=body,
        col=col,
    )
    parts.append(ankle)

    boot = add_cube(
        f"kfr_v0031_{side_name}_boot_mass",
        loc=(5.9 * side_sign, -2.0, 8.0),
        dims=(12.5, 18.0, 10.0),
        mat=dark,
        col=col,
        bevel=0.44,
    )
    parts.append(boot)

    sole = add_cube(
        f"kfr_v0031_{side_name}_sole_mass",
        loc=(5.9 * side_sign, -1.0, 3.1),
        dims=(13.6, 19.5, 2.2),
        mat=body,
        col=col,
        bevel=0.28,
    )
    parts.append(sole)

    for i, toe_x in enumerate([-3.2, 0.0, 3.2], start=1):
        toe = add_uv_sphere(
            f"kfr_v0031_{side_name}_toe_{i}",
            loc=((5.9 + toe_x) * side_sign, -9.1, 6.2),
            dims=(2.5, 4.0, 3.2),
            mat=accent,
            col=col,
            rotation=(math.radians(85), 0.0, 0.0),
            segments=16,
            rings=8,
        )
        parts.append(toe)

    return parts



def build_tail(col, mats):
    skin, body, dark, accent, soft, warn = mats
    tail_parts = []

    centers = [
        (0.0, 13.0, 57.0),
        (0.0, 20.0, 52.0),
        (0.0, 27.2, 46.0),
        (0.0, 33.2, 39.0),
        (0.0, 37.8, 31.2),
        (0.0, 41.0, 23.5),
        (0.0, 43.0, 17.0),
    ]
    dims = [
        (13.0, 14.0, 11.0),
        (11.8, 12.6, 10.0),
        (10.6, 11.2, 9.2),
        (9.0, 10.0, 8.2),
        (7.8, 8.6, 7.2),
        (6.3, 7.0, 5.8),
        (4.8, 5.2, 4.6),
    ]
    rots = [
        math.radians(18),
        math.radians(24),
        math.radians(28),
        math.radians(34),
        math.radians(39),
        math.radians(42),
        math.radians(44),
    ]

    for idx, (c, d, r) in enumerate(zip(centers, dims, rots), start=1):
        seg = add_uv_sphere(
            f"kfr_v0031_tail_segment_{idx}",
            loc=c,
            dims=d,
            mat=skin,
            col=col,
            rotation=(math.radians(90), r, 0.0),
            segments=24,
            rings=12,
        )
        tail_parts.append(seg)

        if idx < len(centers):
            connector_loc = tuple((a + b) / 2.0 for a, b in zip(c, centers[idx]))
            connector = add_cylinder(
                f"kfr_v0031_tail_joint_{idx}",
                loc=connector_loc,
                dims=(4.8 - idx * 0.3, 4.8 - idx * 0.3, 3.0),
                mat=body,
                col=col,
                rotation=(math.radians(65), 0.0, 0.0),
                vertices=16,
                bevel=0.08,
            )
            tail_parts.append(connector)

    dorsal_positions = [
        (0.0, 22.5, 56.5),
        (0.0, 29.5, 50.0),
        (0.0, 35.2, 42.0),
    ]
    for idx, loc in enumerate(dorsal_positions, start=1):
        plate = add_cone(
            f"kfr_v0031_tail_dorsal_plate_{idx}",
            loc=loc,
            dims=(1.8, 1.8, 4.6),
            mat=accent,
            col=col,
            rotation=(0.0, 0.0, 0.0),
            vertices=10,
            bevel=0.0,
        )
        tail_parts.append(plate)

    return tail_parts



def add_pose_arrows(col, mat):
    arrows = []
    arrow_specs = [
        ("head_forward", (0.0, -9.0, 121.0), (0.0, -17.0, 121.0)),
        ("torso_round", (0.0, -2.5, 81.5), (0.0, -10.5, 81.5)),
        ("tail_lower", (0.0, 15.0, 58.0), (0.0, 23.0, 48.0)),
        ("knee_bend_L", (7.5, -0.5, 37.5), (10.5, -3.5, 33.0)),
        ("knee_bend_R", (-7.5, -0.5, 37.5), (-10.5, -3.5, 33.0)),
    ]
    for name, a, b in arrow_specs:
        vec = Vector(b) - Vector(a)
        length = vec.length
        mid = (Vector(a) + Vector(b)) / 2.0
        arrow = add_cylinder(
            f"kfr_v0031_arrow_{name}",
            loc=tuple(mid),
            dims=(0.8, 0.8, length),
            mat=mat,
            col=col,
            rotation=(0.0, 0.0, 0.0),
            vertices=10,
            bevel=0.0,
        )
        arrow.display_type = 'WIRE'
        arrows.append(arrow)
    return arrows


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------


def main():
    log("Starting v003.1 toy pose / proportion pass...")

    hidden = hide_previous_objects()
    if hidden:
        log(f"Hidden {len(hidden)} earlier v003.1 objects.")

    col = make_collection(ROOT_COLLECTION_NAME)
    ensure_text_block()

    mat_skin = make_material("KFR_V0031_Guide_Skin", MAT_GUIDE_SKIN, roughness=0.7)
    mat_body = make_material("KFR_V0031_Guide_Body", MAT_GUIDE_BODY, roughness=0.75)
    mat_dark = make_material("KFR_V0031_Guide_Dark", MAT_GUIDE_DARK, roughness=0.55)
    mat_accent = make_material("KFR_V0031_Guide_Accent", MAT_GUIDE_ACCENT, roughness=0.6)
    mat_soft = make_material("KFR_V0031_Guide_Soft", MAT_GUIDE_SOFT, roughness=0.7)
    mat_warn = make_material("KFR_V0031_Guide_Warn", MAT_GUIDE_WARNING, roughness=0.7)

    mats = (mat_skin, mat_body, mat_dark, mat_accent, mat_soft, mat_warn)

    root = add_empty("kfr_v0031_pose_root", (0.0, 0.0, 0.0), col, size=1.2)

    parts = []
    parts += build_center_guides(col, mats)
    parts += build_side(col, mats, side_sign=1.0)
    parts += build_side(col, mats, side_sign=-1.0)
    parts += build_tail(col, mats)
    parts += add_pose_arrows(col, mat_warn)
    parts.append(add_measure_guide(col, mat_soft))

    parent_many(root, parts)

    try:
        bpy.context.scene.display.shading.show_xray = True
    except Exception:
        pass

    log(f"Created {len(parts)} overlay guide objects in collection '{ROOT_COLLECTION_NAME}'.")
    log("Done. Use the overlay as a sculpt / proportion target for the v003 foundation.")


if __name__ == "__main__":
    main()
