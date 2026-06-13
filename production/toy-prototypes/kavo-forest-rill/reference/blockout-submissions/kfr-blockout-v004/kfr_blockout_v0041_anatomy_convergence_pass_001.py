"""
KFR-BLOCKOUT-v004.1 Anatomy Convergence Pass 001

Purpose
-------
Create a clean, non-overlay v004.1 anatomy replacement that pushes v004 toward
Forest's reference sheet before clothing gets added.

This script intentionally does NOT add translucent guide masses on top of v004.
It hides earlier KFR blockout collections/objects and builds a single stronger
anatomy collection with a closer target silhouette:

- longer, flatter velociraptoroid head instead of round cartoon head
- stronger brow ridge above shades
- clearer snout bridge, nostrils, cheek pads, subtle mouth line
- thick sculpt-friendly neck with neck-joint clearance
- smaller / firmer torso, less balloon belly
- sturdier thighs and calves with relaxed route-ready stance
- wider four-toed raptor feet with dark claws
- longer smoother balancing tail with strong root
- short sparse red proto-quills swept backward, not birthday-hat cones
- scale-bump placeholders placed as sculpt targets

Run after opening the current v004 .blend. Save as:
    kfr_blockout_v0041_anatomy_convergence_pass_001.blend
"""

import math
import bpy
from mathutils import Vector

ROOT_COLLECTION_NAME = "KFR_BLOCKOUT_V0041_ANATOMY_CONVERGENCE_PASS_001"
TEXT_BLOCK_NAME = "KFR_V0041_ANATOMY_CONVERGENCE_NOTES"

HIDE_PRIOR_KFR = True
DELETE_EXISTING_V0041 = True
SET_UNITS_TO_MM = True

# Coordinates:
# X = left/right, positive X is character left.
# Y = front/back, negative Y is character front, positive Y is tail/back.
# Z = up. Figure target height is 127 mm / 5 in.

HIDE_FRAGMENTS = [
    "kfr_blockout_v001", "kfr_blockout_v002", "kfr_blockout_v003", "kfr_blockout_v004",
    "KFR_BLOCKOUT_V001", "KFR_BLOCKOUT_V002", "KFR_BLOCKOUT_V003", "KFR_BLOCKOUT_V004",
    "kfr_v001", "kfr_v002", "kfr_v003", "kfr_v004",
]

# Materials
MAT_SKIN = (0.47, 0.55, 0.34, 1.0)
MAT_BELLY = (0.63, 0.59, 0.41, 1.0)
MAT_DARK_SPOT = (0.16, 0.28, 0.27, 1.0)
MAT_QUILL = (0.68, 0.20, 0.10, 1.0)
MAT_CLAW = (0.055, 0.050, 0.040, 1.0)
MAT_SHADE = (0.01, 0.01, 0.01, 1.0)
MAT_LENS = (0.02, 0.025, 0.023, 0.78)
MAT_JOINT = (0.22, 0.23, 0.21, 1.0)
MAT_GUIDE = (0.10, 0.50, 0.90, 0.45)
MAT_FLOOR = (0.80, 0.80, 0.77, 0.18)

# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------


def log(msg):
    print(f"[KFR V004.1 CONVERGENCE] {msg}")


def rad(deg):
    return math.radians(deg)


def sx(value, side):
    return value * side


def side_name(side):
    return "left" if side > 0 else "right"


def contains_fragment(name, fragments):
    low = name.lower()
    return any(fragment.lower() in low for fragment in fragments)


def setup_scene():
    if SET_UNITS_TO_MM:
        bpy.context.scene.unit_settings.system = "METRIC"
        bpy.context.scene.unit_settings.scale_length = 0.001
        bpy.context.scene.unit_settings.length_unit = "MILLIMETERS"


def hide_prior_kfr():
    hidden_cols = []
    hidden_objs = []
    if not HIDE_PRIOR_KFR:
        return hidden_cols, hidden_objs

    for col in bpy.data.collections:
        if col.name == ROOT_COLLECTION_NAME:
            continue
        if contains_fragment(col.name, HIDE_FRAGMENTS):
            col.hide_viewport = True
            col.hide_render = True
            hidden_cols.append(col.name)

    for obj in bpy.data.objects:
        if obj.name.startswith("kfr_") or obj.name.startswith("KFR_"):
            if ROOT_COLLECTION_NAME.lower() not in obj.name.lower():
                obj.hide_viewport = True
                obj.hide_render = True
                hidden_objs.append(obj.name)

    return hidden_cols, hidden_objs


def make_collection(name):
    existing = bpy.data.collections.get(name)
    if existing and DELETE_EXISTING_V0041:
        for obj in list(existing.objects):
            bpy.data.objects.remove(obj, do_unlink=True)
        existing.hide_viewport = False
        existing.hide_render = False
        return existing
    if existing:
        existing.hide_viewport = False
        existing.hide_render = False
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


def link_to_collection(obj, col):
    try:
        col.objects.link(obj)
    except RuntimeError:
        pass
    unlink_except(obj, col)
    return obj


def make_mat(name, rgba, roughness=0.75, metallic=0.0):
    mat = bpy.data.materials.get(name)
    if mat:
        return mat
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


def set_mat(obj, mat):
    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)
    return obj


def shade_smooth(obj):
    try:
        for poly in obj.data.polygons:
            poly.use_smooth = True
    except Exception:
        pass
    return obj


def add_bevel(obj, width=0.2, segments=2):
    if width <= 0:
        return obj
    mod = obj.modifiers.new(name="v0041_soft_bevel", type="BEVEL")
    mod.width = width
    mod.segments = segments
    mod.affect = "EDGES"
    try:
        obj.modifiers.new(name="v0041_weighted_normals", type="WEIGHTED_NORMAL")
    except Exception:
        pass
    return obj


def finalize(obj, col, mat=None, smooth=False, bevel_width=0.0, bevel_segments=2):
    if mat:
        set_mat(obj, mat)
    if smooth:
        shade_smooth(obj)
    if bevel_width:
        add_bevel(obj, bevel_width, bevel_segments)
    link_to_collection(obj, col)
    return obj


def add_empty(name, loc, col, size=1.0):
    bpy.ops.object.empty_add(type="PLAIN_AXES", location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.empty_display_size = size
    return link_to_collection(obj, col)


def add_sphere(name, loc, dims, mat, col, rotation=(0, 0, 0), segments=32, rings=16):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segments, ring_count=rings, radius=1.0, location=loc, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.scale = (dims[0] / 2, dims[1] / 2, dims[2] / 2)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    return finalize(obj, col, mat=mat, smooth=True)


def add_cube(name, loc, dims, mat, col, rotation=(0, 0, 0), bevel_width=0.18):
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=loc, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.dimensions = dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    return finalize(obj, col, mat=mat, smooth=False, bevel_width=bevel_width, bevel_segments=3)


def add_cylinder(name, loc, dims, mat, col, rotation=(0, 0, 0), vertices=24, bevel_width=0.08):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=1.0, depth=2.0, location=loc, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.dimensions = dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    return finalize(obj, col, mat=mat, smooth=True, bevel_width=bevel_width, bevel_segments=2)


def cylinder_between(name, start, end, radius, mat, col, vertices=24, bevel_width=0.04):
    start_v = Vector(start)
    end_v = Vector(end)
    vec = end_v - start_v
    if vec.length <= 0.0001:
        return None
    mid = start_v + vec * 0.5
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=vec.length, location=mid)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.rotation_euler = vec.to_track_quat("Z", "Y").to_euler()
    return finalize(obj, col, mat=mat, smooth=True, bevel_width=bevel_width, bevel_segments=1)


def cone_between(name, start, end, radius, mat, col, vertices=16, radius2=0.0, bevel_width=0.02):
    start_v = Vector(start)
    end_v = Vector(end)
    vec = end_v - start_v
    if vec.length <= 0.0001:
        return None
    mid = start_v + vec * 0.5
    bpy.ops.mesh.primitive_cone_add(vertices=vertices, radius1=radius, radius2=radius2, depth=vec.length, location=mid)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.rotation_euler = vec.to_track_quat("Z", "Y").to_euler()
    return finalize(obj, col, mat=mat, smooth=True, bevel_width=bevel_width, bevel_segments=1)


def add_torus(name, loc, major_radius, minor_radius, mat, col, rotation=(0, 0, 0)):
    bpy.ops.mesh.primitive_torus_add(major_radius=major_radius, minor_radius=minor_radius, major_segments=32, minor_segments=8, location=loc, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    return finalize(obj, col, mat=mat, smooth=True)


def parent_all(root, objects):
    for obj in objects:
        if obj:
            obj.parent = root

# -----------------------------------------------------------------------------
# Notes
# -----------------------------------------------------------------------------


def write_notes():
    text = bpy.data.texts.get(TEXT_BLOCK_NAME)
    if text is None:
        text = bpy.data.texts.new(TEXT_BLOCK_NAME)
    text.clear()
    text.write(
        "KFR-BLOCKOUT-v004.1 Anatomy Convergence Pass 001\n"
        "=================================================\n\n"
        "This is a replacement anatomy pass, not an overlay guide.\n"
        "It hides earlier KFR blockout layers and builds a single cleaner figure.\n\n"
        "What changed from v004:\n"
        "- smaller/less round head with longer wedge snout\n"
        "- heavier brow ridge and better shades placement\n"
        "- thick vertical neck with forward rake\n"
        "- reduced balloon belly; firmer chest/waist/pelvis read\n"
        "- stronger relaxed route-ready stance\n"
        "- wider clawed feet and better tail counterbalance\n"
        "- shorter swept-back quills\n\n"
        "Next recommended pass: clothing / route harness / pouches.\n"
    )

# -----------------------------------------------------------------------------
# Build systems
# -----------------------------------------------------------------------------


def build_guides(col, mats):
    out = []
    out.append(add_cube("kfr_v0041_floor_reference_180mm", (0, 0, -1.0), (180, 180, 0.8), mats["floor"], col, bevel_width=0))
    out[-1].display_type = "WIRE"
    out.append(add_cylinder("kfr_v0041_height_guide_127mm", (-36, -34, 63.5), (1.3, 1.3, 127), mats["guide"], col, vertices=12, bevel_width=0))
    out[-1].display_type = "WIRE"
    out.append(add_cube("kfr_v0041_stance_width_guide_47mm", (0, -34, 0.6), (47, 1.6, 0.8), mats["guide"], col, bevel_width=0))
    out[-1].display_type = "WIRE"
    return out


def build_torso(col, mats):
    out = []
    # Smaller, firmer torso based on reference: compact, athletic, not spherical.
    out.append(add_sphere("kfr_v0041_pelvis_compact", (0, 0.8, 48.5), (21, 16, 15), mats["skin"], col, segments=32, rings=14))
    out.append(add_sphere("kfr_v0041_lower_abdomen_taper", (0, -1.7, 59.5), (22, 15, 20), mats["belly"], col, segments=32, rings=16))
    out.append(add_sphere("kfr_v0041_ribcage_compact", (0, -1.5, 75.0), (29, 18, 29), mats["skin"], col, segments=36, rings=18))
    out.append(add_sphere("kfr_v0041_upper_back_mass", (0, 4.4, 78.0), (28, 13, 25), mats["skin"], col, segments=32, rings=14))

    # Vertical belly plates embedded in the front, closer to sheet.
    plate_z = [50.5, 55.0, 59.6, 64.2, 69.0, 73.8, 78.0]
    plate_widths = [9.0, 12.0, 15.5, 17.5, 16.0, 13.5, 9.5]
    for i, (z, w) in enumerate(zip(plate_z, plate_widths), start=1):
        out.append(add_cube(
            f"kfr_v0041_abdominal_plate_{i:02d}",
            (0, -11.2, z),
            (w, 0.9, 2.1),
            mats["belly"],
            col,
            rotation=(rad(1), 0, 0),
            bevel_width=0.32,
        ))

    # Simple joint indicators, small and not overpowering.
    out.append(add_torus("kfr_v0041_waist_joint_clearance_ring", (0, 0.0, 53.0), 10.3, 0.35, mats["joint"], col, rotation=(rad(90), 0, 0)))
    out.append(add_torus("kfr_v0041_neck_joint_clearance_ring", (0, 0.0, 91.0), 8.1, 0.30, mats["joint"], col, rotation=(rad(90), 0, 0)))
    return out


def build_neck_head(col, mats):
    out = []
    # Thick neck stack, leaning slightly forward, with throat plates.
    neck_points = [
        (0, 1.4, 87.0),
        (0, 0.4, 93.0),
        (0, -1.3, 99.0),
        (0, -3.8, 104.0),
    ]
    neck_radii = [7.4, 7.2, 6.8, 6.2]
    for i, p in enumerate(neck_points, start=1):
        out.append(add_sphere(f"kfr_v0041_neck_volume_{i:02d}", p, (neck_radii[i-1]*2.2, neck_radii[i-1]*1.8, 7.2), mats["skin"], col, segments=30, rings=12))
    for i in range(len(neck_points) - 1):
        out.append(cylinder_between(f"kfr_v0041_neck_blend_{i+1:02d}", neck_points[i], neck_points[i+1], neck_radii[i], mats["skin"], col, vertices=24, bevel_width=0.04))

    for i, z in enumerate([88.5, 92.0, 95.5, 99.0], start=1):
        out.append(add_cube(f"kfr_v0041_front_neck_plate_{i:02d}", (0, -9.1, z), (9.0 - i*0.3, 0.7, 1.5), mats["belly"], col, bevel_width=0.18))

    # Head: replace ball read with stretched skull + wedge snout.
    out.append(add_sphere("kfr_v0041_skull_rear_oval", (0, -4.8, 111.5), (24.0, 18.5, 18.0), mats["skin"], col, segments=40, rings=18))
    out.append(add_sphere("kfr_v0041_skull_crown_flattened", (0, -10.2, 115.0), (25.5, 20.0, 9.8), mats["skin"], col, rotation=(rad(-4), 0, 0), segments=40, rings=14))
    out.append(add_sphere("kfr_v0041_snout_bridge_long", (0, -22.5, 111.0), (14.5, 29.0, 8.6), mats["skin"], col, rotation=(rad(-3), 0, 0), segments=36, rings=14))
    out.append(add_sphere("kfr_v0041_snout_tip_clear", (0, -37.3, 110.4), (12.2, 9.8, 7.2), mats["skin"], col, segments=28, rings=12))
    out.append(add_sphere("kfr_v0041_lower_jaw_long", (0, -24.6, 104.5), (15.0, 28.5, 5.2), mats["belly"], col, rotation=(rad(-2), 0, 0), segments=32, rings=10))
    out.append(add_sphere("kfr_v0041_chin_pad", (0, -35.0, 103.4), (9.6, 6.5, 3.8), mats["belly"], col, segments=20, rings=8))

    # Brow shelf and cheek pads. This is the key silhouette lock.
    out.append(add_cube("kfr_v0041_brow_shelf_left", (6.7, -27.6, 114.5), (12.2, 2.1, 3.0), mats["skin"], col, rotation=(rad(1), rad(0), rad(-4)), bevel_width=0.34))
    out.append(add_cube("kfr_v0041_brow_shelf_right", (-6.7, -27.6, 114.5), (12.2, 2.1, 3.0), mats["skin"], col, rotation=(rad(1), rad(0), rad(4)), bevel_width=0.34))
    out.append(add_sphere("kfr_v0041_left_cheek_sweep", (9.8, -20.2, 106.0), (5.0, 15.0, 4.6), mats["skin"], col, rotation=(0, 0, rad(-16)), segments=24, rings=10))
    out.append(add_sphere("kfr_v0041_right_cheek_sweep", (-9.8, -20.2, 106.0), (5.0, 15.0, 4.6), mats["skin"], col, rotation=(0, 0, rad(16)), segments=24, rings=10))

    # Nostrils and mouth line.
    out.append(add_cylinder("kfr_v0041_left_nostril_deep", (4.7, -41.0, 111.0), (2.5, 1.3, 1.3), mats["claw"], col, rotation=(rad(90), 0, 0), vertices=18, bevel_width=0.02))
    out.append(add_cylinder("kfr_v0041_right_nostril_deep", (-4.7, -41.0, 111.0), (2.5, 1.3, 1.3), mats["claw"], col, rotation=(rad(90), 0, 0), vertices=18, bevel_width=0.02))
    out.append(cylinder_between("kfr_v0041_left_subtle_smile", (2.6, -36.0, 105.8), (12.0, -18.0, 105.0), 0.35, mats["claw"], col, vertices=8, bevel_width=0.005))
    out.append(cylinder_between("kfr_v0041_right_subtle_smile", (-2.6, -36.0, 105.8), (-12.0, -18.0, 105.0), 0.35, mats["claw"], col, vertices=8, bevel_width=0.005))
    out.append(cylinder_between("kfr_v0041_front_mouth_curve", (-4.8, -36.5, 105.5), (4.8, -36.5, 105.5), 0.35, mats["claw"], col, vertices=8, bevel_width=0.005))

    # Shades: lower/smaller than v004, following brow line.
    out.append(add_cube("kfr_v0041_left_smoky_lens", (6.8, -29.3, 113.0), (10.2, 1.1, 5.5), mats["lens"], col, rotation=(rad(1), 0, rad(-2.5)), bevel_width=0.26))
    out.append(add_cube("kfr_v0041_right_smoky_lens", (-6.8, -29.3, 113.0), (10.2, 1.1, 5.5), mats["lens"], col, rotation=(rad(1), 0, rad(2.5)), bevel_width=0.26))
    out.append(add_cube("kfr_v0041_shades_bridge", (0, -29.5, 113.0), (3.3, 1.0, 1.9), mats["shade"], col, bevel_width=0.16))
    out.append(cylinder_between("kfr_v0041_left_shades_arm", (11.9, -29.0, 113.0), (14.4, -11.8, 111.2), 0.55, mats["shade"], col, vertices=8, bevel_width=0.005))
    out.append(cylinder_between("kfr_v0041_right_shades_arm", (-11.9, -29.0, 113.0), (-14.4, -11.8, 111.2), 0.55, mats["shade"], col, vertices=8, bevel_width=0.005))

    return out


def build_quills(col, mats):
    out = []
    # Short, sparse, backward-swept quills along head and neck.
    quills = [
        ((0, -15.5, 119.0), (0, -13.7, 124.0), 1.7),
        ((0, -10.8, 120.0), (0, -8.8, 126.1), 2.1),
        ((0, -5.2, 119.7), (0, -2.2, 126.2), 2.2),
        ((0, 0.0, 117.2), (0, 3.6, 123.0), 2.0),
        ((0, 4.2, 113.4), (0, 8.0, 118.0), 1.7),
        ((0, 7.4, 108.2), (0, 10.8, 112.0), 1.4),
        ((0, 8.6, 101.5), (0, 11.3, 104.6), 1.2),
    ]
    for i, (start, end, radius) in enumerate(quills, start=1):
        out.append(cone_between(f"kfr_v0041_swept_head_quill_{i:02d}", start, end, radius, mats["quill"], col, vertices=16, bevel_width=0.01))

    spine_quills = [
        ((0, 8.8, 91.5), (0, 11.2, 94.6), 1.0),
        ((0, 9.4, 82.5), (0, 12.0, 85.2), 0.95),
        ((0, 10.0, 72.5), (0, 12.7, 74.8), 0.90),
        ((0, 13.5, 57.0), (0, 16.5, 59.0), 0.85),
        ((0, 25.0, 49.0), (0, 28.0, 51.0), 0.75),
        ((0, 38.0, 38.0), (0, 40.8, 39.7), 0.65),
        ((0, 51.0, 25.0), (0, 53.4, 26.3), 0.50),
    ]
    for i, (start, end, radius) in enumerate(spine_quills, start=1):
        out.append(cone_between(f"kfr_v0041_swept_spine_tail_quill_{i:02d}", start, end, radius, mats["quill"], col, vertices=12, bevel_width=0.008))

    return out


def build_arm(col, mats, side):
    out = []
    label = side_name(side)
    shoulder = (sx(17.5, side), -0.8, 77.2)
    elbow = (sx(23.5, side), -2.0, 60.4)
    wrist = (sx(25.4, side), -4.2, 44.7)
    palm = (sx(25.8, side), -7.2, 40.2)

    out.append(add_sphere(f"kfr_v0041_{label}_shoulder_ball", shoulder, (11.0, 11.0, 11.0), mats["skin"], col, segments=28, rings=14))
    out.append(cylinder_between(f"kfr_v0041_{label}_upper_arm", shoulder, elbow, 4.35, mats["skin"], col, vertices=22, bevel_width=0.05))
    out.append(add_sphere(f"kfr_v0041_{label}_elbow_landmark", elbow, (7.0, 7.0, 7.0), mats["joint"], col, segments=20, rings=10))
    out.append(cylinder_between(f"kfr_v0041_{label}_forearm", elbow, wrist, 4.0, mats["skin"], col, vertices=22, bevel_width=0.05))
    out.append(add_sphere(f"kfr_v0041_{label}_wrist_landmark", wrist, (5.8, 5.8, 5.6), mats["joint"], col, segments=18, rings=9))
    out.append(add_sphere(f"kfr_v0041_{label}_palm", palm, (9.5, 7.0, 6.2), mats["skin"], col, rotation=(0, rad(10*side), rad(6*side)), segments=24, rings=12))

    # Three fingers and thumb, longer/slimmer than v004 cartoon mittens.
    finger_specs = [(-3.2, -0.1, 0.1), (0.0, -0.4, 0.4), (3.1, 0.0, 0.0)]
    for i, (ox, oy, oz) in enumerate(finger_specs, start=1):
        base = (sx(25.7 + ox, side), -10.0 + oy, 40.3 + oz)
        mid = (sx(25.7 + ox*1.03, side), -14.2 + oy, 37.7 + oz)
        tip = (sx(25.7 + ox*1.08, side), -17.5 + oy, 35.6 + oz)
        out.append(cylinder_between(f"kfr_v0041_{label}_finger_{i}_base", base, mid, 1.15, mats["skin"], col, vertices=14, bevel_width=0.02))
        out.append(cylinder_between(f"kfr_v0041_{label}_finger_{i}_tip", mid, tip, 0.95, mats["skin"], col, vertices=14, bevel_width=0.02))
        out.append(cone_between(f"kfr_v0041_{label}_finger_{i}_claw", tip, (tip[0], tip[1]-2.8, tip[2]-1.4), 0.78, mats["claw"], col, vertices=10, bevel_width=0.005))

    thumb_base = (sx(21.7, side), -8.5, 40.0)
    thumb_mid = (sx(19.4, side), -11.8, 37.7)
    thumb_tip = (sx(18.4, side), -14.2, 35.5)
    out.append(cylinder_between(f"kfr_v0041_{label}_thumb_base", thumb_base, thumb_mid, 1.25, mats["skin"], col, vertices=14, bevel_width=0.02))
    out.append(cylinder_between(f"kfr_v0041_{label}_thumb_tip", thumb_mid, thumb_tip, 1.0, mats["skin"], col, vertices=14, bevel_width=0.02))
    out.append(cone_between(f"kfr_v0041_{label}_thumb_claw", thumb_tip, (thumb_tip[0]-side*1.1, thumb_tip[1]-2.2, thumb_tip[2]-1.1), 0.75, mats["claw"], col, vertices=10, bevel_width=0.005))
    return out


def build_leg(col, mats, side):
    out = []
    label = side_name(side)
    hip = (sx(8.8, side), -0.3, 49.0)
    knee = (sx(11.6, side), -4.8, 31.5)
    ankle = (sx(10.5, side), -6.0, 14.2)
    foot = (sx(10.4, side), -11.7, 6.2)

    out.append(add_sphere(f"kfr_v0041_{label}_hip_landmark", hip, (8.8, 8.4, 8.4), mats["joint"], col, segments=22, rings=10))
    out.append(cylinder_between(f"kfr_v0041_{label}_thigh", hip, knee, 4.9, mats["skin"], col, vertices=24, bevel_width=0.05))
    out.append(add_sphere(f"kfr_v0041_{label}_knee_landmark", knee, (8.2, 7.8, 7.2), mats["joint"], col, segments=20, rings=10))
    out.append(cylinder_between(f"kfr_v0041_{label}_shin_calf", knee, ankle, 4.2, mats["skin"], col, vertices=24, bevel_width=0.05))
    out.append(add_sphere(f"kfr_v0041_{label}_ankle_landmark", ankle, (6.2, 6.0, 5.2), mats["joint"], col, segments=18, rings=8))
    out.append(add_sphere(f"kfr_v0041_{label}_wide_raptor_foot", foot, (12.0, 18.0, 5.8), mats["skin"], col, segments=28, rings=12))

    toe_specs = [
        ("inner", -4.4, -19.0, 6.4, 1.00),
        ("middle", 0.0, -21.2, 6.6, 1.15),
        ("outer", 4.4, -18.7, 6.4, 0.95),
        ("rear", -6.8, -8.5, 5.4, 0.75),
    ]
    for name, ox, end_y, z, scale in toe_specs:
        base = (sx(10.4 + ox, side), -11.0, z)
        mid = (sx(10.4 + ox*1.02, side), end_y, z - 0.25)
        tip = (sx(10.4 + ox*1.03, side), end_y - 4.0*scale, z - 0.55)
        out.append(cylinder_between(f"kfr_v0041_{label}_toe_{name}", base, mid, 1.25*scale, mats["skin"], col, vertices=14, bevel_width=0.018))
        out.append(cone_between(f"kfr_v0041_{label}_toe_{name}_claw", mid, tip, 0.98*scale, mats["claw"], col, vertices=12, bevel_width=0.004))
    return out


def build_tail(col, mats):
    out = []
    # Smoother, longer, natural counterbalance tail. Higher root, lower tip.
    pts = [
        (0.0, 8.2, 50.5),
        (0.0, 19.5, 48.0),
        (0.0, 31.5, 42.5),
        (0.0, 43.5, 34.0),
        (0.0, 55.0, 24.5),
        (0.0, 65.0, 15.0),
        (0.0, 73.0, 8.8),
    ]
    radii = [6.8, 6.0, 5.1, 4.2, 3.2, 2.2]
    out.append(add_sphere("kfr_v0041_tail_root_muscle", pts[0], (16, 13, 12), mats["skin"], col, segments=28, rings=12))
    for i in range(len(pts) - 1):
        out.append(cylinder_between(f"kfr_v0041_tail_taper_segment_{i+1:02d}", pts[i], pts[i+1], radii[i], mats["skin"], col, vertices=28, bevel_width=0.04))
        if i < len(pts) - 2:
            out.append(add_sphere(f"kfr_v0041_tail_joint_landmark_{i+1:02d}", pts[i+1], (radii[i]*1.55, radii[i]*1.55, radii[i]*1.40), mats["joint"], col, segments=18, rings=8))
    out.append(add_sphere("kfr_v0041_tail_tip", pts[-1], (4.0, 3.0, 2.6), mats["skin"], col, segments=16, rings=8))
    return out


def build_scale_bumps(col, mats):
    out = []
    bumps = [
        # crown and snout
        (-8.5, -21, 117), (-4.0, -23, 118), (4.0, -23, 118), (8.5, -21, 117),
        (-9.5, -11, 117), (-4.5, -8, 118), (4.5, -8, 118), (9.5, -11, 117),
        (-6.0, -34, 113), (6.0, -34, 113), (-2.5, -39, 113), (2.5, -39, 113),
        # neck, shoulders, torso
        (-12, 2, 102), (12, 2, 102), (-13, 2, 94), (13, 2, 94),
        (-13, -2, 79), (13, -2, 79), (-10, 6, 72), (10, 6, 72),
        # limbs
        (-22, -2, 67), (22, -2, 67), (-25, -4, 51), (25, -4, 51),
        (-10, -4, 37), (10, -4, 37), (-11, -3, 22), (11, -3, 22),
        # tail
        (0, 20, 51), (0, 32, 45), (0, 44, 37), (0, 56, 27), (0, 66, 17),
    ]
    for i, (x, y, z) in enumerate(bumps, start=1):
        d = 1.75 if z > 90 else 1.55
        out.append(add_sphere(f"kfr_v0041_dark_scale_bump_{i:02d}", (x, y, z), (d, d*0.75, d*0.45), mats["scale"], col, segments=10, rings=6))
    return out

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------


def main():
    log("Starting v004.1 anatomy convergence replacement pass.")
    setup_scene()
    hidden_cols, hidden_objs = hide_prior_kfr()
    col = make_collection(ROOT_COLLECTION_NAME)
    root = add_empty("kfr_v0041_anatomy_convergence_root", (0, 0, 0), col, size=1.2)

    mats = {
        "skin": make_mat("KFR_V0041_skin_route_dust_olive", MAT_SKIN, roughness=0.86),
        "belly": make_mat("KFR_V0041_light_belly_scutes", MAT_BELLY, roughness=0.84),
        "scale": make_mat("KFR_V0041_dark_teal_scale_spots", MAT_DARK_SPOT, roughness=0.82),
        "quill": make_mat("KFR_V0041_red_swept_proto_quills", MAT_QUILL, roughness=0.72),
        "claw": make_mat("KFR_V0041_dark_claws_and_mouth", MAT_CLAW, roughness=0.42),
        "shade": make_mat("KFR_V0041_shades_black_frame", MAT_SHADE, roughness=0.35),
        "lens": make_mat("KFR_V0041_smoky_lens", MAT_LENS, roughness=0.24),
        "joint": make_mat("KFR_V0041_neutral_joint_landmarks", MAT_JOINT, roughness=0.70),
        "guide": make_mat("KFR_V0041_blue_reference_guides", MAT_GUIDE, roughness=0.50),
        "floor": make_mat("KFR_V0041_translucent_floor_reference", MAT_FLOOR, roughness=0.50),
    }

    created = []
    created.extend(build_guides(col, mats))
    created.extend(build_torso(col, mats))
    created.extend(build_neck_head(col, mats))
    created.extend(build_quills(col, mats))
    created.extend(build_tail(col, mats))
    for side in (1, -1):
        created.extend(build_arm(col, mats, side))
        created.extend(build_leg(col, mats, side))
    created.extend(build_scale_bumps(col, mats))
    parent_all(root, created)
    write_notes()

    log(f"Hidden prior KFR collections: {len(hidden_cols)}")
    log(f"Hidden prior KFR objects: {len(hidden_objs)}")
    log(f"Created v004.1 anatomy objects: {len(created)}")
    log("Save as: kfr_blockout_v0041_anatomy_convergence_pass_001.blend")
    log("Review: front, left side, back, 3/4, head close-up, feet close-up, tail profile.")


if __name__ == "__main__":
    main()
