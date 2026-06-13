"""
Kavo "Forest" Rill
KFR-BLOCKOUT-v004.2 Reference Silhouette Lock Pass 001

Run in Blender after opening the current working scene.

Goal:
    Replace v004.1 with a clean rebuild that pushes the anatomy closer to the
    reference sheet before clothing work begins.

Focus:
    - longer, flatter velociraptoroid head
    - stronger brow shelf with shades tucked beneath it
    - forward-sloping thick neck, less vertical tube
    - compact torso, tighter waist, less beach-ball belly
    - stronger thighs, calves, planted four-toed feet
    - smoother balancing tail with better root
    - smaller, more numerous swept proto-quills

Save as:
    kfr_blockout_v0042_reference_silhouette_lock_pass_001.blend
"""

import math
import bpy
from mathutils import Vector

COLLECTION_NAME = "KFR_BLOCKOUT_V0042_REFERENCE_SILHOUETTE_LOCK_PASS_001"
ROOT_NAME = "kfr_v0042_reference_silhouette_lock_root"
NOTES_NAME = "KFR_V0042_REFERENCE_SILHOUETTE_LOCK_NOTES"

# Blender units: meters. 127 mm target height = 0.127 m.
HEIGHT_M = 0.127

# Character axis convention used here:
# X = front/back. Negative X is snout/front. Positive X is tail/back.
# Y = left/right.
# Z = up.

# Materials.
MAT_BODY = (0.74, 0.80, 0.56, 1.0)
MAT_BELLY = (0.86, 0.83, 0.65, 1.0)
MAT_SCALE = (0.27, 0.42, 0.39, 1.0)
MAT_QUILL = (0.92, 0.45, 0.24, 1.0)
MAT_DARK = (0.035, 0.033, 0.032, 1.0)
MAT_LENS = (0.06, 0.08, 0.08, 0.58)
MAT_JOINT = (0.74, 0.78, 0.72, 1.0)
MAT_GUIDE = (0.15, 0.15, 0.15, 1.0)

# -----------------------------------------------------------------------------
# Utility helpers
# -----------------------------------------------------------------------------


def rad(deg):
    return math.radians(deg)


def ensure_object_mode():
    if bpy.context.object and bpy.context.object.mode != "OBJECT":
        bpy.ops.object.mode_set(mode="OBJECT")


def make_mat(name, color, roughness=0.65, alpha=False):
    mat = bpy.data.materials.get(name)
    if mat is None:
        mat = bpy.data.materials.new(name)
        mat.use_nodes = True
    mat.diffuse_color = color
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = color
        bsdf.inputs["Roughness"].default_value = roughness
        if "Alpha" in bsdf.inputs:
            bsdf.inputs["Alpha"].default_value = color[3]
    if alpha or color[3] < 1.0:
        mat.blend_method = "BLEND"
        mat.shadow_method = "HASHED"
    return mat


def get_materials():
    return {
        "body": make_mat("KFR_V0042_route_dust_olive_skin", MAT_BODY, 0.82),
        "belly": make_mat("KFR_V0042_light_belly_scutes", MAT_BELLY, 0.78),
        "scale": make_mat("KFR_V0042_blue_teal_scale_spots", MAT_SCALE, 0.82),
        "quill": make_mat("KFR_V0042_red_proto_quills", MAT_QUILL, 0.66),
        "dark": make_mat("KFR_V0042_dark_claws_mouth_frames", MAT_DARK, 0.44),
        "lens": make_mat("KFR_V0042_smoky_shade_lenses", MAT_LENS, 0.22, True),
        "joint": make_mat("KFR_V0042_joint_landmark_soft_gray", MAT_JOINT, 0.74),
        "guide": make_mat("KFR_V0042_scale_guide_dark_gray", MAT_GUIDE, 0.7),
    }


def clean_or_create_collection(name):
    ensure_object_mode()
    old = bpy.data.collections.get(name)
    if old:
        for obj in list(old.objects):
            bpy.data.objects.remove(obj, do_unlink=True)
        return old
    col = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(col)
    return col


def hide_prior_kfr_collections():
    for col in bpy.data.collections:
        n = col.name.lower()
        if col.name == COLLECTION_NAME:
            continue
        if "kfr_blockout_v004" in n or "kfr_v004" in n or "kfr-blockout-v004" in n:
            col.hide_viewport = True
            col.hide_render = True


def link_to_col(obj, col):
    for user_col in list(obj.users_collection):
        user_col.objects.unlink(obj)
    col.objects.link(obj)
    return obj


def apply_mat(obj, mat):
    obj.data.materials.clear()
    obj.data.materials.append(mat)
    return obj


def shade_smooth(obj):
    try:
        for poly in obj.data.polygons:
            poly.use_smooth = True
    except Exception:
        pass
    return obj


def add_bevel(obj, width=0.001, segments=2):
    mod = obj.modifiers.new("soft_bevel", "BEVEL")
    mod.width = width
    mod.segments = segments
    mod.affect = "EDGES"
    try:
        obj.modifiers.new("weighted_normals", "WEIGHTED_NORMAL")
    except Exception:
        pass
    return obj


def finalize(obj, col, mat, parent=None, smooth=True, bevel=0.0):
    apply_mat(obj, mat)
    if smooth:
        shade_smooth(obj)
    if bevel:
        add_bevel(obj, bevel, 2)
    if parent:
        obj.parent = parent
    return link_to_col(obj, col)


def empty(name, loc, col):
    bpy.ops.object.empty_add(type="PLAIN_AXES", location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.empty_display_size = 0.006
    return link_to_col(obj, col)


def sphere(name, loc, scale, col, mat, parent, rotation=(0, 0, 0), segments=32, rings=16):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segments, ring_count=rings, radius=1, location=loc, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    return finalize(obj, col, mat, parent, True)


def cube(name, loc, scale, col, mat, parent, rotation=(0, 0, 0), bevel=0.00045):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    return finalize(obj, col, mat, parent, False, bevel)


def cyl(name, loc, radius, depth, col, mat, parent, rotation=(0, 0, 0), vertices=24, bevel=0.0):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=depth, location=loc, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    return finalize(obj, col, mat, parent, True, bevel)


def cone(name, loc, radius, depth, col, mat, parent, rotation=(0, 0, 0), vertices=16):
    bpy.ops.mesh.primitive_cone_add(vertices=vertices, radius1=radius, radius2=0, depth=depth, location=loc, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    return finalize(obj, col, mat, parent, True)


def cylinder_between(name, a, b, radius, col, mat, parent, vertices=24):
    a = Vector(a)
    b = Vector(b)
    vec = b - a
    mid = a + vec * 0.5
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=vec.length, location=mid)
    obj = bpy.context.object
    obj.name = name
    obj.rotation_euler = vec.to_track_quat("Z", "Y").to_euler()
    return finalize(obj, col, mat, parent, True)


def cone_between(name, a, b, radius, col, mat, parent, vertices=16):
    a = Vector(a)
    b = Vector(b)
    vec = b - a
    mid = a + vec * 0.5
    bpy.ops.mesh.primitive_cone_add(vertices=vertices, radius1=radius, radius2=0, depth=vec.length, location=mid)
    obj = bpy.context.object
    obj.name = name
    obj.rotation_euler = vec.to_track_quat("Z", "Y").to_euler()
    return finalize(obj, col, mat, parent, True)

# -----------------------------------------------------------------------------
# Anatomy build
# -----------------------------------------------------------------------------


def build_guides(col, mats, root):
    cyl(
        "kfr_v0042_127mm_height_guide",
        (-0.045, -0.035, HEIGHT_M / 2),
        0.0007,
        HEIGHT_M,
        col,
        mats["guide"],
        root,
        vertices=10,
    )
    cube(
        "kfr_v0042_47mm_stance_width_guide",
        (-0.010, 0.0, -0.001),
        (0.001, 0.047 / 2, 0.0005),
        col,
        mats["guide"],
        root,
        bevel=0.0,
    )


def build_torso(col, mats, root):
    # Compact reptile torso with stronger taper and less mascot-ball volume.
    sphere("kfr_v0042_chest_compact_oval", (0.006, 0, 0.061), (0.018, 0.020, 0.022), col, mats["body"], root, rotation=(rad(-4), 0, 0))
    sphere("kfr_v0042_upper_back_muscle", (0.015, 0, 0.061), (0.010, 0.017, 0.017), col, mats["body"], root)
    sphere("kfr_v0042_abdomen_tighter", (0.003, 0, 0.043), (0.014, 0.0155, 0.016), col, mats["belly"], root)
    sphere("kfr_v0042_pelvis_compact", (0.005, 0, 0.027), (0.0135, 0.015, 0.011), col, mats["body"], root, rotation=(rad(-4), 0, 0))

    # Embedded ventral scutes, flatter and more anatomy-like than ladder strips.
    plate_specs = [
        (0.057, 0.0105), (0.052, 0.0120), (0.047, 0.0132), (0.042, 0.0138),
        (0.037, 0.0130), (0.032, 0.0116), (0.027, 0.0100),
    ]
    for i, (z, width) in enumerate(plate_specs, 1):
        cube(
            f"kfr_v0042_ventral_scute_{i:02d}",
            (-0.0075, 0, z),
            (0.0008, width / 2, 0.00105),
            col,
            mats["belly"],
            root,
            rotation=(rad(-4), 0, 0),
            bevel=0.00025,
        )


def build_neck_and_head(col, mats, root):
    # Forward-sloping neck column that flows into skull.
    neck_points = [
        (0.0085, 0, 0.073),
        (0.0055, 0, 0.082),
        (0.0015, 0, 0.091),
        (-0.0030, 0, 0.099),
    ]
    neck_scales = [
        (0.0115, 0.0135, 0.0090),
        (0.0105, 0.0128, 0.0085),
        (0.0095, 0.0115, 0.0078),
        (0.0085, 0.0105, 0.0070),
    ]
    for i, (pt, sc) in enumerate(zip(neck_points, neck_scales), 1):
        sphere(f"kfr_v0042_forward_neck_mass_{i:02d}", pt, sc, col, mats["body"], root, rotation=(rad(10), 0, 0), segments=28, rings=12)

    # Neck throat plates.
    for i, z in enumerate([0.094, 0.089, 0.084, 0.079], 1):
        cube(
            f"kfr_v0042_neck_throat_scute_{i:02d}",
            (-0.0077 + i * 0.0015, 0, z),
            (0.00075, (0.008 + i * 0.0013) / 2, 0.001),
            col,
            mats["belly"],
            root,
            rotation=(rad(8), 0, 0),
            bevel=0.00025,
        )

    # Raptor head: flatter skull, long wedge snout, smaller roundness.
    sphere("kfr_v0042_skull_low_wedge", (-0.004, 0, 0.110), (0.0185, 0.0205, 0.0162), col, mats["body"], root, rotation=(rad(3), 0, 0), segments=36, rings=16)
    sphere("kfr_v0042_rear_cranium_taper", (0.010, 0, 0.109), (0.012, 0.016, 0.014), col, mats["body"], root, segments=32, rings=14)
    sphere("kfr_v0042_brow_shelf_heavy", (-0.012, 0, 0.1125), (0.012, 0.0195, 0.006), col, mats["body"], root, rotation=(rad(-3), 0, 0), segments=32, rings=12)
    sphere("kfr_v0042_snout_bridge_long_flat", (-0.026, 0, 0.1085), (0.020, 0.0105, 0.0065), col, mats["body"], root, rotation=(rad(-3), 0, 0), segments=32, rings=12)
    sphere("kfr_v0042_snout_tip_narrow", (-0.039, 0, 0.108), (0.0075, 0.0065, 0.0048), col, mats["body"], root, segments=24, rings=10)
    sphere("kfr_v0042_upper_lip_subtle", (-0.026, 0, 0.1025), (0.019, 0.010, 0.0035), col, mats["belly"], root, rotation=(rad(3), 0, 0), segments=28, rings=10)
    sphere("kfr_v0042_lower_jaw_slim", (-0.024, 0, 0.0982), (0.018, 0.0105, 0.0038), col, mats["belly"], root, rotation=(rad(3), 0, 0), segments=28, rings=10)
    sphere("kfr_v0042_cheek_left", (-0.014, 0.0112, 0.1017), (0.0052, 0.0042, 0.0043), col, mats["body"], root, segments=22, rings=10)
    sphere("kfr_v0042_cheek_right", (-0.014, -0.0112, 0.1017), (0.0052, 0.0042, 0.0043), col, mats["body"], root, segments=22, rings=10)

    # Nostrils and subtle mouth lines.
    sphere("kfr_v0042_nostril_left", (-0.0405, 0.0031, 0.1087), (0.0012, 0.00155, 0.0008), col, mats["dark"], root, segments=12, rings=6)
    sphere("kfr_v0042_nostril_right", (-0.0405, -0.0031, 0.1087), (0.0012, 0.00155, 0.0008), col, mats["dark"], root, segments=12, rings=6)
    cylinder_between("kfr_v0042_left_mouth_line", (-0.036, 0.006, 0.101), (-0.010, 0.0105, 0.1015), 0.00028, col, mats["dark"], root, vertices=8)
    cylinder_between("kfr_v0042_right_mouth_line", (-0.036, -0.006, 0.101), (-0.010, -0.0105, 0.1015), 0.00028, col, mats["dark"], root, vertices=8)

    # Shades tucked under brow, with heavy readable frames.
    cube("kfr_v0042_shades_lens_left", (-0.0165, 0.0076, 0.1110), (0.0065, 0.00075, 0.0037), col, mats["lens"], root, rotation=(rad(-5), 0, 0), bevel=0.00028)
    cube("kfr_v0042_shades_lens_right", (-0.0165, -0.0076, 0.1110), (0.0065, 0.00075, 0.0037), col, mats["lens"], root, rotation=(rad(-5), 0, 0), bevel=0.00028)
    cube("kfr_v0042_shades_frame_left", (-0.0165, 0.0076, 0.1110), (0.0073, 0.00115, 0.0044), col, mats["dark"], root, rotation=(rad(-5), 0, 0), bevel=0.00025)
    cube("kfr_v0042_shades_frame_right", (-0.0165, -0.0076, 0.1110), (0.0073, 0.00115, 0.0044), col, mats["dark"], root, rotation=(rad(-5), 0, 0), bevel=0.00025)
    cube("kfr_v0042_shades_bridge", (-0.014, 0, 0.1110), (0.0015, 0.0010, 0.0014), col, mats["dark"], root, rotation=(rad(-5), 0, 0), bevel=0.0002)
    cylinder_between("kfr_v0042_shades_left_arm", (-0.010, 0.012, 0.1115), (0.006, 0.014, 0.110), 0.00045, col, mats["dark"], root, vertices=8)
    cylinder_between("kfr_v0042_shades_right_arm", (-0.010, -0.012, 0.1115), (0.006, -0.014, 0.110), 0.00045, col, mats["dark"], root, vertices=8)


def build_quills_and_scales(col, mats, root):
    # Smaller swept-back quills from skull to tail root.
    quills = [
        ((-0.010, 0, 0.122), (-0.006, 0, 0.129), 0.0018),
        ((-0.004, 0, 0.122), (0.001, 0, 0.130), 0.0020),
        ((0.003, 0, 0.120), (0.010, 0, 0.127), 0.0019),
        ((0.010, 0, 0.116), (0.018, 0, 0.122), 0.0016),
        ((0.015, 0, 0.110), (0.023, 0, 0.115), 0.0014),
        ((0.016, 0, 0.098), (0.023, 0, 0.102), 0.0012),
        ((0.017, 0, 0.083), (0.024, 0, 0.086), 0.0010),
        ((0.018, 0, 0.063), (0.024, 0, 0.065), 0.0009),
        ((0.029, 0, 0.028), (0.035, 0, 0.030), 0.0008),
    ]
    for i, (a, b, r) in enumerate(quills, 1):
        cone_between(f"kfr_v0042_swept_proto_quill_{i:02d}", a, b, r, col, mats["quill"], root, vertices=14)

    # Major scale bump targets. Clothing will cover some later, but these steer the sculpt read now.
    scale_points = [
        (-0.032, 0.0045, 0.113), (-0.032, -0.0045, 0.113),
        (-0.022, 0.009, 0.116), (-0.022, -0.009, 0.116),
        (-0.010, 0.012, 0.118), (-0.010, -0.012, 0.118),
        (0.005, 0.012, 0.104), (0.005, -0.012, 0.104),
        (0.008, 0.015, 0.067), (0.008, -0.015, 0.067),
        (0.014, 0.014, 0.050), (0.014, -0.014, 0.050),
        (0.035, 0.008, 0.023), (0.035, -0.008, 0.023),
        (0.052, 0.006, 0.011), (0.052, -0.006, 0.011),
    ]
    for i, p in enumerate(scale_points, 1):
        sphere(f"kfr_v0042_large_scale_target_{i:02d}", p, (0.0015, 0.0011, 0.00075), col, mats["scale"], root, segments=10, rings=6)


def build_limbs(col, mats, root):
    for side, sign in [("left", 1), ("right", -1)]:
        # Arms hang lower and feel creature-toy sturdy.
        sphere(f"kfr_v0042_{side}_shoulder_ball", (0.005, 0.019 * sign, 0.059), (0.0072, 0.0078, 0.0078), col, mats["body"], root, segments=24, rings=12)
        cylinder_between(f"kfr_v0042_{side}_upper_arm", (0.005, 0.022 * sign, 0.054), (0.004, 0.025 * sign, 0.037), 0.0042, col, mats["body"], root, vertices=20)
        sphere(f"kfr_v0042_{side}_elbow_knuckle", (0.004, 0.025 * sign, 0.037), (0.0038, 0.0038, 0.0038), col, mats["joint"], root, segments=18, rings=8)
        cylinder_between(f"kfr_v0042_{side}_forearm", (0.004, 0.025 * sign, 0.034), (0.001, 0.023 * sign, 0.018), 0.0038, col, mats["body"], root, vertices=20)
        sphere(f"kfr_v0042_{side}_wrist", (0.001, 0.023 * sign, 0.016), (0.0034, 0.0038, 0.0032), col, mats["joint"], root, segments=16, rings=8)
        sphere(f"kfr_v0042_{side}_palm", (-0.001, 0.023 * sign, 0.011), (0.0048, 0.0065, 0.0031), col, mats["body"], root, segments=20, rings=10)

        finger_offsets = [0.0188, 0.0225, 0.0260]
        for i, yabs in enumerate(finger_offsets, 1):
            y = yabs * sign
            cylinder_between(f"kfr_v0042_{side}_finger_{i}_base", (-0.003, y, 0.010), (-0.008, y, 0.008), 0.00105, col, mats["body"], root, vertices=12)
            cylinder_between(f"kfr_v0042_{side}_finger_{i}_tip", (-0.008, y, 0.008), (-0.011, y, 0.006), 0.0009, col, mats["body"], root, vertices=12)
            cone_between(f"kfr_v0042_{side}_finger_{i}_claw", (-0.011, y, 0.006), (-0.014, y, 0.0045), 0.0009, col, mats["dark"], root, vertices=10)
        cylinder_between(f"kfr_v0042_{side}_thumb", (-0.002, 0.018 * sign, 0.010), (-0.005, 0.014 * sign, 0.007), 0.0011, col, mats["body"], root, vertices=12)
        cone_between(f"kfr_v0042_{side}_thumb_claw", (-0.005, 0.014 * sign, 0.007), (-0.007, 0.011 * sign, 0.0055), 0.0008, col, mats["dark"], root, vertices=10)

        # Legs: thicker, subtly bent, planted. Foot is bigger and claw-bearing.
        sphere(f"kfr_v0042_{side}_hip", (0.004, 0.011 * sign, 0.027), (0.0055, 0.0062, 0.0054), col, mats["joint"], root, segments=20, rings=10)
        cylinder_between(f"kfr_v0042_{side}_thigh_heavy", (0.003, 0.011 * sign, 0.025), (0.001, 0.0135 * sign, 0.004), 0.0053, col, mats["body"], root, vertices=22)
        sphere(f"kfr_v0042_{side}_knee", (0.0005, 0.0135 * sign, 0.003), (0.0044, 0.0048, 0.0042), col, mats["joint"], root, segments=18, rings=8)
        cylinder_between(f"kfr_v0042_{side}_shin_calf", (0.0005, 0.0135 * sign, 0.001), (-0.0015, 0.012 * sign, -0.020), 0.0046, col, mats["body"], root, vertices=22)
        sphere(f"kfr_v0042_{side}_ankle", (-0.0015, 0.012 * sign, -0.021), (0.0036, 0.004, 0.0033), col, mats["joint"], root, segments=16, rings=8)
        sphere(f"kfr_v0042_{side}_wide_foot", (-0.0115, 0.012 * sign, -0.027), (0.0105, 0.0095, 0.0042), col, mats["body"], root, rotation=(rad(-3), 0, 0), segments=24, rings=10)
        sphere(f"kfr_v0042_{side}_heel_pad", (-0.002, 0.012 * sign, -0.028), (0.0042, 0.0045, 0.003), col, mats["body"], root, segments=16, rings=8)

        toe_y_offsets = [-0.0055, -0.0018, 0.0018, 0.0055]
        for i, off in enumerate(toe_y_offsets, 1):
            toe_y = (0.012 + off) * sign
            sphere(f"kfr_v0042_{side}_toe_{i}", (-0.018, toe_y, -0.028), (0.0043, 0.0019, 0.00145), col, mats["body"], root, segments=16, rings=8)
            cone_between(f"kfr_v0042_{side}_toe_{i}_claw", (-0.021, toe_y, -0.0283), (-0.025, toe_y, -0.0285), 0.0011, col, mats["dark"], root, vertices=10)


def build_tail(col, mats, root):
    # Clean, long counterbalance tail with stronger root and taper.
    tail_centers = [
        (0.018, 0, 0.026),
        (0.031, 0, 0.020),
        (0.044, 0, 0.013),
        (0.058, 0, 0.006),
        (0.071, 0, 0.000),
        (0.083, 0, -0.004),
        (0.094, 0, -0.0065),
    ]
    radii = [0.0070, 0.0062, 0.0054, 0.0046, 0.0038, 0.0030]
    for i in range(len(tail_centers) - 1):
        cylinder_between(
            f"kfr_v0042_tail_segment_{i+1:02d}",
            tail_centers[i],
            tail_centers[i + 1],
            radii[i],
            col,
            mats["body"],
            root,
            vertices=24,
        )
    sphere("kfr_v0042_tail_root_muscle", tail_centers[0], (0.009, 0.010, 0.008), col, mats["body"], root, segments=24, rings=10)
    sphere("kfr_v0042_tail_tip", tail_centers[-1], (0.0030, 0.0026, 0.0022), col, mats["body"], root, segments=16, rings=8)

# -----------------------------------------------------------------------------
# Notes and main
# -----------------------------------------------------------------------------


def write_notes():
    text = bpy.data.texts.get(NOTES_NAME)
    if text is None:
        text = bpy.data.texts.new(NOTES_NAME)
    text.clear()
    text.write(
        "KFR-BLOCKOUT-v004.2 Reference Silhouette Lock Pass 001\n"
        "========================================================\n\n"
        "Clean rebuild from v004.1 direction. Not an overlay.\n\n"
        "Primary changes:\n"
        "- Longer flatter velociraptoroid head and snout\n"
        "- Brow shelf strengthened; shades tucked beneath it\n"
        "- Neck slopes forward and blends into shoulders\n"
        "- Torso compacted with tighter abdomen and pelvis\n"
        "- Limbs thickened; feet widened and planted\n"
        "- Tail root strengthened and taper smoothed\n"
        "- Quills made smaller, more numerous, and swept back\n\n"
        "Next suggested pass before clothes: v004.3 lower-body and head refinement.\n"
    )


def main():
    ensure_object_mode()
    bpy.context.scene.unit_settings.system = "METRIC"
    bpy.context.scene.unit_settings.scale_length = 1.0
    bpy.context.scene.unit_settings.length_unit = "METERS"

    hide_prior_kfr_collections()
    col = clean_or_create_collection(COLLECTION_NAME)
    mats = get_materials()
    root = empty(ROOT_NAME, (0, 0, 0.049), col)

    build_guides(col, mats, root)
    build_torso(col, mats, root)
    build_neck_and_head(col, mats, root)
    build_quills_and_scales(col, mats, root)
    build_limbs(col, mats, root)
    build_tail(col, mats, root)
    write_notes()

    bpy.ops.object.select_all(action="DESELECT")
    root.select_set(True)
    bpy.context.view_layer.objects.active = root
    print("KFR v004.2 reference silhouette lock pass complete.")
    print(f"Collection: {COLLECTION_NAME}")
    print("Save as: kfr_blockout_v0042_reference_silhouette_lock_pass_001.blend")


if __name__ == "__main__":
    main()
