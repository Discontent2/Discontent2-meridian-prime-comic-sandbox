"""
Kavo "Forest" Rill
KFR-BLOCKOUT-v004.3 Goal Sprint Rebuild Pass 001

Purpose:
    Fast, clean rebuild toward the reference sheet.
    This is not a timid patch. It hides old v004 collections only after the new
    figure has been successfully created.

Blender 5.x safe:
    No Material.shadow_method calls.
    No destructive edits to existing meshes.
    No external files.

Run:
    Open the working .blend, paste/run this script in Blender's Python editor.

Save as:
    kfr_blockout_v0043_goal_sprint_rebuild_pass_001.blend
"""

import math
import bpy
from mathutils import Vector

COLLECTION_NAME = "KFR_BLOCKOUT_V0043_GOAL_SPRINT_REBUILD_PASS_001"
ROOT_NAME = "kfr_v0043_goal_sprint_rebuild_root"
NOTES_NAME = "KFR_V0043_GOAL_SPRINT_REBUILD_NOTES"

HEIGHT_M = 0.127

# Axis convention:
# X negative = front / snout direction
# X positive = back / tail direction
# Y = left/right
# Z = up

MAT_SKIN = (0.69, 0.77, 0.48, 1.0)
MAT_BELLY = (0.84, 0.80, 0.61, 1.0)
MAT_DARK = (0.025, 0.023, 0.022, 1.0)
MAT_LENS = (0.04, 0.055, 0.052, 0.55)
MAT_QUILL = (0.92, 0.42, 0.22, 1.0)
MAT_SCALE = (0.25, 0.43, 0.39, 1.0)
MAT_JOINT = (0.66, 0.70, 0.65, 1.0)
MAT_GUIDE = (0.13, 0.13, 0.13, 1.0)
MAT_CLAW = (0.055, 0.052, 0.047, 1.0)


def rad(deg):
    return math.radians(deg)


def ensure_object_mode():
    if bpy.context.object and bpy.context.object.mode != "OBJECT":
        bpy.ops.object.mode_set(mode="OBJECT")


def make_mat(name, color, roughness=0.7, alpha=False):
    mat = bpy.data.materials.get(name)
    if mat is None:
        mat = bpy.data.materials.new(name)

    mat.use_nodes = True
    mat.diffuse_color = color

    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        if "Base Color" in bsdf.inputs:
            bsdf.inputs["Base Color"].default_value = color
        if "Roughness" in bsdf.inputs:
            bsdf.inputs["Roughness"].default_value = roughness
        if "Alpha" in bsdf.inputs:
            bsdf.inputs["Alpha"].default_value = color[3]

    if alpha or color[3] < 1.0:
        mat.blend_method = "BLEND"
        if hasattr(mat, "use_screen_refraction"):
            mat.use_screen_refraction = True
        if hasattr(mat, "show_transparent_back"):
            mat.show_transparent_back = True

    return mat


def mats():
    return {
        "skin": make_mat("KFR_V0043_route_dust_olive_skin", MAT_SKIN, 0.82),
        "belly": make_mat("KFR_V0043_light_belly_scutes", MAT_BELLY, 0.78),
        "dark": make_mat("KFR_V0043_black_shades_mouth_straps", MAT_DARK, 0.45),
        "lens": make_mat("KFR_V0043_smoky_shade_lenses", MAT_LENS, 0.22, True),
        "quill": make_mat("KFR_V0043_red_proto_quills", MAT_QUILL, 0.62),
        "scale": make_mat("KFR_V0043_blue_teal_scale_spots", MAT_SCALE, 0.84),
        "joint": make_mat("KFR_V0043_soft_joint_gray", MAT_JOINT, 0.72),
        "guide": make_mat("KFR_V0043_scale_guides_dark_gray", MAT_GUIDE, 0.7),
        "claw": make_mat("KFR_V0043_dark_claws", MAT_CLAW, 0.5),
    }


def rescue_visibility():
    # If a prior script crashed after hiding Forest, bring the old forest ghosts back first.
    for col in bpy.data.collections:
        n = col.name.lower()
        if "kfr" in n or "forest" in n or "blockout" in n:
            col.hide_viewport = False
            col.hide_render = False


def clean_or_create_collection(name):
    old = bpy.data.collections.get(name)
    if old:
        for obj in list(old.objects):
            bpy.data.objects.remove(obj, do_unlink=True)
        old.hide_viewport = False
        old.hide_render = False
        return old

    col = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(col)
    return col


def hide_prior_versions_after_success():
    for col in bpy.data.collections:
        if col.name == COLLECTION_NAME:
            continue
        n = col.name.lower()
        if (
            "kfr_blockout_v004" in n
            or "kfr_v004" in n
            or "kfr-blockout-v004" in n
            or "kfr_blockout_v003" in n
            or "kfr_v003" in n
        ):
            col.hide_viewport = True
            col.hide_render = True


def link_to_col(obj, col):
    for user_col in list(obj.users_collection):
        user_col.objects.unlink(obj)
    col.objects.link(obj)
    return obj


def apply_mat(obj, mat):
    if hasattr(obj.data, "materials"):
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


def bevel(obj, width=0.00035, segments=2):
    if width <= 0:
        return obj
    try:
        mod = obj.modifiers.new("soft_toy_bevel", "BEVEL")
        mod.width = width
        mod.segments = segments
        try:
            mod.affect = "EDGES"
        except Exception:
            pass
    except Exception:
        pass
    try:
        obj.modifiers.new("soft_weighted_normals", "WEIGHTED_NORMAL")
    except Exception:
        pass
    return obj


def finalize(obj, col, mat, parent=None, smooth=True, bevel_width=0.0):
    apply_mat(obj, mat)
    if smooth:
        shade_smooth(obj)
    bevel(obj, bevel_width, 2)
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
    bpy.ops.mesh.primitive_uv_sphere_add(
        segments=segments,
        ring_count=rings,
        radius=1,
        location=loc,
        rotation=rotation,
    )
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    return finalize(obj, col, mat, parent, True)


def cube(name, loc, scale, col, mat, parent, rotation=(0, 0, 0), bevel_width=0.00035):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    return finalize(obj, col, mat, parent, False, bevel_width)


def cyl(name, loc, radius, depth, col, mat, parent, rotation=(0, 0, 0), vertices=24, bevel_width=0.0):
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=vertices,
        radius=radius,
        depth=depth,
        location=loc,
        rotation=rotation,
    )
    obj = bpy.context.object
    obj.name = name
    return finalize(obj, col, mat, parent, True, bevel_width)


def cylinder_between(name, a, b, radius, col, mat, parent, vertices=24):
    a = Vector(a)
    b = Vector(b)
    vec = b - a
    if vec.length < 0.0001:
        return sphere(name + "_tiny", a, (radius, radius, radius), col, mat, parent)
    mid = a + vec * 0.5
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=vec.length, location=mid)
    obj = bpy.context.object
    obj.name = name
    obj.rotation_euler = vec.to_track_quat("Z", "Y").to_euler()
    return finalize(obj, col, mat, parent, True)


def cone_between(name, a, b, radius1, radius2, col, mat, parent, vertices=16):
    a = Vector(a)
    b = Vector(b)
    vec = b - a
    if vec.length < 0.0001:
        return sphere(name + "_tiny", a, (radius1, radius1, radius1), col, mat, parent)
    mid = a + vec * 0.5
    bpy.ops.mesh.primitive_cone_add(
        vertices=vertices,
        radius1=radius1,
        radius2=radius2,
        depth=vec.length,
        location=mid,
    )
    obj = bpy.context.object
    obj.name = name
    obj.rotation_euler = vec.to_track_quat("Z", "Y").to_euler()
    return finalize(obj, col, mat, parent, True)


def add_scale_dot(name, loc, radius, col, mat, parent, flat_axis="x"):
    scale = (radius, radius, radius)
    if flat_axis == "x":
        scale = (radius * 0.35, radius, radius * 0.55)
    elif flat_axis == "z":
        scale = (radius, radius, radius * 0.35)
    return sphere(name, loc, scale, col, mat, parent, segments=12, rings=6)


def build_guides(col, m, root):
    cyl("kfr_v0043_127mm_scale_guide", (-0.055, -0.034, HEIGHT_M / 2), 0.00055, HEIGHT_M, col, m["guide"], root, vertices=8)
    cube("kfr_v0043_47mm_footprint_guide", (-0.010, 0.0, 0.0004), (0.001, 0.047 / 2, 0.00035), col, m["guide"], root, bevel_width=0.0)


def build_core_anatomy(col, m, root):
    # Aggressive side-view correction: pelvis and tail sit behind, chest and head lean forward.
    sphere("kfr_v0043_pelvis_forward_tucked", (0.010, 0.000, 0.048), (0.013, 0.016, 0.012), col, m["skin"], root, rotation=(rad(-10), 0, 0), segments=32, rings=14)
    sphere("kfr_v0043_lower_belly_keel", (0.000, 0.000, 0.060), (0.013, 0.014, 0.012), col, m["belly"], root, rotation=(rad(-8), 0, 0), segments=32, rings=14)
    sphere("kfr_v0043_ribcage_leaning_forward", (-0.008, 0.000, 0.077), (0.016, 0.019, 0.020), col, m["skin"], root, rotation=(rad(-12), 0, 0), segments=36, rings=16)
    sphere("kfr_v0043_upper_back_hump", (0.001, 0.000, 0.082), (0.014, 0.017, 0.016), col, m["skin"], root, rotation=(rad(-8), 0, 0), segments=32, rings=14)
    sphere("kfr_v0043_chest_front_plane_mass", (-0.015, 0.000, 0.079), (0.006, 0.014, 0.014), col, m["belly"], root, rotation=(rad(-12), 0, 0), segments=28, rings=12)

    # Belly and throat scutes follow the creature surface, not an overlay ladder.
    scute_specs = [
        (-0.0180, 0.000, 0.087, 0.0125),
        (-0.0170, 0.000, 0.081, 0.0145),
        (-0.0155, 0.000, 0.075, 0.0152),
        (-0.0130, 0.000, 0.068, 0.0140),
        (-0.0105, 0.000, 0.061, 0.0122),
        (-0.0065, 0.000, 0.054, 0.0105),
        (-0.0020, 0.000, 0.047, 0.0085),
    ]
    for i, (x, y, z, width) in enumerate(scute_specs, 1):
        cube(
            f"kfr_v0043_embedded_ventral_scute_{i:02d}",
            (x, y, z),
            (0.00085, width / 2, 0.00105),
            col,
            m["belly"],
            root,
            rotation=(rad(-12), 0, 0),
            bevel_width=0.00018,
        )


def build_neck_head(col, m, root):
    # Neck is a thick forward ramp, not a straight giraffe tube.
    neck_chain = [
        ((-0.004, 0, 0.091), (0.0105, 0.0135, 0.0085)),
        ((-0.010, 0, 0.099), (0.0100, 0.0122, 0.0080)),
        ((-0.018, 0, 0.105), (0.0094, 0.0110, 0.0074)),
        ((-0.026, 0, 0.109), (0.0085, 0.0102, 0.0068)),
    ]
    for i, (loc, sc) in enumerate(neck_chain, 1):
        sphere(f"kfr_v0043_sloped_power_neck_{i:02d}", loc, sc, col, m["skin"], root, rotation=(rad(-10), 0, 0), segments=30, rings=12)

    # Long low raptor head: wedge skull, snout bridge, tapered snout, lips, jaw, cheeks.
    sphere("kfr_v0043_long_low_skull_back", (-0.033, 0, 0.114), (0.014, 0.018, 0.011), col, m["skin"], root, rotation=(rad(-2), 0, 0), segments=36, rings=16)
    sphere("kfr_v0043_flat_brow_cranium", (-0.045, 0, 0.115), (0.015, 0.0165, 0.0075), col, m["skin"], root, rotation=(rad(-3), 0, 0), segments=32, rings=14)
    sphere("kfr_v0043_snout_bridge_long", (-0.060, 0, 0.112), (0.021, 0.0078, 0.0050), col, m["skin"], root, rotation=(rad(-3), 0, 0), segments=32, rings=12)
    sphere("kfr_v0043_snout_tip_tapered", (-0.076, 0, 0.111), (0.0085, 0.0062, 0.0045), col, m["skin"], root, rotation=(rad(-3), 0, 0), segments=24, rings=10)
    sphere("kfr_v0043_upper_muzzle_lip", (-0.062, 0, 0.105), (0.020, 0.0084, 0.0032), col, m["belly"], root, rotation=(rad(2), 0, 0), segments=28, rings=10)
    sphere("kfr_v0043_lower_jaw_slim", (-0.059, 0, 0.101), (0.020, 0.0089, 0.0032), col, m["belly"], root, rotation=(rad(2), 0, 0), segments=28, rings=10)

    sphere("kfr_v0043_left_cheek_jowl", (-0.044, 0.0102, 0.105), (0.006, 0.0042, 0.0042), col, m["skin"], root, segments=22, rings=10)
    sphere("kfr_v0043_right_cheek_jowl", (-0.044, -0.0102, 0.105), (0.006, 0.0042, 0.0042), col, m["skin"], root, segments=22, rings=10)
    sphere("kfr_v0043_left_nostril", (-0.080, 0.0033, 0.112), (0.0012, 0.0015, 0.00075), col, m["dark"], root, segments=12, rings=6)
    sphere("kfr_v0043_right_nostril", (-0.080, -0.0033, 0.112), (0.0012, 0.0015, 0.00075), col, m["dark"], root, segments=12, rings=6)

    cylinder_between("kfr_v0043_left_mouth_cut", (-0.077, 0.0050, 0.1032), (-0.039, 0.0100, 0.1046), 0.00030, col, m["dark"], root, vertices=8)
    cylinder_between("kfr_v0043_right_mouth_cut", (-0.077, -0.0050, 0.1032), (-0.039, -0.0100, 0.1046), 0.00030, col, m["dark"], root, vertices=8)

    # Shades are tucked under brow like the reference, not floating billboard goggles.
    cube("kfr_v0043_left_shades_lens", (-0.052, 0.0070, 0.1133), (0.0095, 0.0007, 0.0034), col, m["lens"], root, rotation=(rad(-4), 0, 0), bevel_width=0.00022)
    cube("kfr_v0043_right_shades_lens", (-0.052, -0.0070, 0.1133), (0.0095, 0.0007, 0.0034), col, m["lens"], root, rotation=(rad(-4), 0, 0), bevel_width=0.00022)
    cube("kfr_v0043_left_shades_top_frame", (-0.052, 0.0070, 0.1162), (0.0103, 0.0010, 0.0008), col, m["dark"], root, rotation=(rad(-4), 0, 0), bevel_width=0.00012)
    cube("kfr_v0043_right_shades_top_frame", (-0.052, -0.0070, 0.1162), (0.0103, 0.0010, 0.0008), col, m["dark"], root, rotation=(rad(-4), 0, 0), bevel_width=0.00012)
    cube("kfr_v0043_shades_bridge", (-0.049, 0, 0.1135), (0.002, 0.0010, 0.0015), col, m["dark"], root, rotation=(rad(-4), 0, 0), bevel_width=0.00012)
    cylinder_between("kfr_v0043_left_shades_arm", (-0.041, 0.0115, 0.1140), (-0.024, 0.0130, 0.1120), 0.00045, col, m["dark"], root, vertices=8)
    cylinder_between("kfr_v0043_right_shades_arm", (-0.041, -0.0115, 0.1140), (-0.024, -0.0130, 0.1120), 0.00045, col, m["dark"], root, vertices=8)

    # Head and neck scale bumps.
    scale_locations = [
        (-0.075, 0.0048, 0.116), (-0.075, -0.0048, 0.116),
        (-0.063, 0.0090, 0.117), (-0.063, -0.0090, 0.117),
        (-0.048, 0.0120, 0.119), (-0.048, -0.0120, 0.119),
        (-0.034, 0.0135, 0.116), (-0.034, -0.0135, 0.116),
        (-0.024, 0.0115, 0.105), (-0.024, -0.0115, 0.105),
    ]
    for i, loc in enumerate(scale_locations, 1):
        add_scale_dot(f"kfr_v0043_head_scale_dot_{i:02d}", loc, 0.00115, col, m["scale"], root, "z")


def build_dorsal_quills(col, m, root):
    # Smaller, more numerous swept red proto-quills. The line follows skull, neck, back, and tail root.
    quill_specs = [
        ((-0.050, 0, 0.121), (-0.054, 0, 0.127), 0.0017),
        ((-0.042, 0, 0.122), (-0.043, 0, 0.130), 0.0019),
        ((-0.034, 0, 0.121), (-0.031, 0, 0.129), 0.0018),
        ((-0.026, 0, 0.117), (-0.021, 0, 0.124), 0.0016),
        ((-0.017, 0, 0.110), (-0.011, 0, 0.117), 0.0014),
        ((-0.008, 0, 0.101), (-0.001, 0, 0.107), 0.00125),
        ((-0.001, 0, 0.090), (0.006, 0, 0.095), 0.00115),
        ((0.005, 0, 0.077), (0.012, 0, 0.081), 0.00105),
        ((0.011, 0, 0.061), (0.018, 0, 0.064), 0.00095),
        ((0.022, 0, 0.047), (0.029, 0, 0.049), 0.00085),
    ]
    for i, (a, b, r) in enumerate(quill_specs, 1):
        cone_between(f"kfr_v0043_swept_red_proto_quill_{i:02d}", a, b, r, 0.0, col, m["quill"], root, vertices=14)


def build_legs_and_feet(col, m, root):
    for side, sign in [("left", 1), ("right", -1)]:
        hip = (0.008, 0.0145 * sign, 0.051)
        knee = (-0.006, 0.0185 * sign, 0.030)
        ankle = (-0.015, 0.0175 * sign, 0.011)

        sphere(f"kfr_v0043_{side}_hip_socket", hip, (0.0058, 0.0065, 0.0055), col, m["joint"], root, segments=20, rings=10)
        cone_between(f"kfr_v0043_{side}_heavy_thigh_taper", hip, knee, 0.0060, 0.0048, col, m["skin"], root, vertices=24)
        sphere(f"kfr_v0043_{side}_rounded_knee", knee, (0.0048, 0.0052, 0.0046), col, m["joint"], root, segments=20, rings=10)
        cone_between(f"kfr_v0043_{side}_forward_bent_shin", knee, ankle, 0.0048, 0.0042, col, m["skin"], root, vertices=24)
        sphere(f"kfr_v0043_{side}_ankle_ball", ankle, (0.0038, 0.0040, 0.0034), col, m["joint"], root, segments=18, rings=8)

        # Feet are planted and connected: no floating pancakes.
        foot_center = (-0.025, 0.0185 * sign, 0.0048)
        sphere(f"kfr_v0043_{side}_plantigrade_foot_pad", foot_center, (0.0145, 0.0088, 0.0048), col, m["skin"], root, rotation=(rad(-2), 0, rad(4 * -sign)), segments=28, rings=12)
        sphere(f"kfr_v0043_{side}_heel_mass", (-0.013, 0.0170 * sign, 0.0053), (0.0052, 0.0060, 0.0043), col, m["skin"], root, segments=20, rings=10)
        cylinder_between(f"kfr_v0043_{side}_ankle_to_foot_bridge", ankle, (-0.014, 0.0175 * sign, 0.0065), 0.0032, col, m["skin"], root, vertices=18)

        toe_offsets = [-0.0062, -0.0021, 0.0021, 0.0062]
        for i, off in enumerate(toe_offsets, 1):
            toe_y = (0.0185 + off) * sign
            toe_base = (-0.035, toe_y, 0.0045)
            toe_tip = (-0.044, toe_y + (0.0005 * sign), 0.0038)
            cylinder_between(f"kfr_v0043_{side}_toe_{i}_meaty_base", (-0.027, toe_y, 0.0050), toe_base, 0.0017, col, m["skin"], root, vertices=12)
            cone_between(f"kfr_v0043_{side}_toe_{i}_dark_claw", toe_base, toe_tip, 0.0016, 0.0, col, m["claw"], root, vertices=10)

        # Subtle knee and shin landmark plates for action-figure readability.
        cube(f"kfr_v0043_{side}_knee_front_plate", (-0.010, 0.0185 * sign, 0.0305), (0.0010, 0.0045, 0.0022), col, m["joint"], root, rotation=(rad(10), 0, 0), bevel_width=0.00018)


def build_arms_and_hands(col, m, root):
    for side, sign in [("left", 1), ("right", -1)]:
        shoulder = (-0.005, 0.0220 * sign, 0.082)
        elbow = (-0.010, 0.0280 * sign, 0.057)
        wrist = (-0.014, 0.0255 * sign, 0.035)

        sphere(f"kfr_v0043_{side}_rounded_shoulder", shoulder, (0.0075, 0.0080, 0.0075), col, m["skin"], root, segments=24, rings=12)
        cone_between(f"kfr_v0043_{side}_upper_arm_dropped", shoulder, elbow, 0.0052, 0.0044, col, m["skin"], root, vertices=22)
        sphere(f"kfr_v0043_{side}_elbow_joint", elbow, (0.0041, 0.0042, 0.0040), col, m["joint"], root, segments=18, rings=8)
        cone_between(f"kfr_v0043_{side}_forearm_thick", elbow, wrist, 0.0044, 0.0038, col, m["skin"], root, vertices=22)
        sphere(f"kfr_v0043_{side}_wrist_joint", wrist, (0.0035, 0.0037, 0.0033), col, m["joint"], root, segments=18, rings=8)
        sphere(f"kfr_v0043_{side}_wide_palm", (-0.018, 0.0250 * sign, 0.030), (0.0048, 0.0066, 0.0032), col, m["skin"], root, segments=20, rings=10)

        finger_y_offsets = [-0.0042, 0.0, 0.0042]
        for i, off in enumerate(finger_y_offsets, 1):
            y = (0.0250 + off) * sign
            base = (-0.0215, y, 0.0295)
            mid = (-0.0265, y + 0.0004 * sign, 0.0275)
            tip = (-0.0305, y + 0.0008 * sign, 0.0258)
            cylinder_between(f"kfr_v0043_{side}_hand_finger_{i}_base", base, mid, 0.00125, col, m["skin"], root, vertices=12)
            cone_between(f"kfr_v0043_{side}_hand_finger_{i}_claw", mid, tip, 0.0011, 0.0, col, m["claw"], root, vertices=10)

        thumb_base = (-0.019, (0.0200) * sign, 0.030)
        thumb_tip = (-0.025, (0.0162) * sign, 0.027)
        cylinder_between(f"kfr_v0043_{side}_opposable_thumb", thumb_base, thumb_tip, 0.0013, col, m["skin"], root, vertices=12)
        cone_between(f"kfr_v0043_{side}_thumb_claw", thumb_tip, (-0.028, (0.0140) * sign, 0.0256), 0.0010, 0.0, col, m["claw"], root, vertices=10)


def build_tail(col, m, root):
    # Long counterbalancing tail, tapered and slightly descending. Root is thicker and blended into pelvis.
    pts = [
        (0.020, 0, 0.048),
        (0.033, 0, 0.045),
        (0.049, 0, 0.039),
        (0.066, 0, 0.032),
        (0.083, 0, 0.025),
        (0.100, 0, 0.019),
        (0.116, 0, 0.014),
    ]
    radii = [0.0075, 0.0068, 0.0058, 0.0047, 0.0037, 0.0028]
    sphere("kfr_v0043_tail_root_muscle_left", (0.018, 0.006, 0.049), (0.007, 0.005, 0.006), col, m["skin"], root, segments=20, rings=10)
    sphere("kfr_v0043_tail_root_muscle_right", (0.018, -0.006, 0.049), (0.007, 0.005, 0.006), col, m["skin"], root, segments=20, rings=10)
    for i in range(len(pts) - 1):
        cone_between(f"kfr_v0043_tail_taper_segment_{i + 1:02d}", pts[i], pts[i + 1], radii[i], max(radii[i] * 0.82, 0.0018), col, m["skin"], root, vertices=24)
        if i in [0, 1, 2, 3]:
            ring_loc = pts[i + 1]
            cyl(f"kfr_v0043_tail_joint_ring_{i + 1:02d}", ring_loc, radii[i] * 1.03, 0.0010, col, m["joint"], root, rotation=(0, rad(90), 0), vertices=24)
    sphere("kfr_v0043_tail_tip_point_mass", pts[-1], (0.0030, 0.0026, 0.0020), col, m["skin"], root, segments=16, rings=8)

    # Back/tail teal spots and a few small tail quills for directionality.
    spot_locs = [
        (0.036, 0.0050, 0.048),
        (0.036, -0.0050, 0.048),
        (0.052, 0.0045, 0.041),
        (0.052, -0.0045, 0.041),
        (0.070, 0.0040, 0.034),
        (0.070, -0.0040, 0.034),
        (0.088, 0.0033, 0.027),
        (0.088, -0.0033, 0.027),
    ]
    for i, loc in enumerate(spot_locs, 1):
        add_scale_dot(f"kfr_v0043_tail_teal_spot_{i:02d}", loc, 0.0011, col, m["scale"], root, "z")

    quills = [
        ((0.032, 0, 0.051), (0.037, 0, 0.056), 0.0010),
        ((0.050, 0, 0.043), (0.056, 0, 0.047), 0.0009),
        ((0.069, 0, 0.035), (0.075, 0, 0.038), 0.00075),
    ]
    for i, (a, b, r) in enumerate(quills, 1):
        cone_between(f"kfr_v0043_tail_small_dorsal_quill_{i:02d}", a, b, r, 0.0, col, m["quill"], root, vertices=12)


def build_surface_detail(col, m, root):
    # A useful density bump pass without getting into true sculpting yet.
    dot_specs = [
        (-0.016, 0.014, 0.086), (-0.016, -0.014, 0.086),
        (-0.006, 0.016, 0.080), (-0.006, -0.016, 0.080),
        (0.004, 0.014, 0.071), (0.004, -0.014, 0.071),
        (0.008, 0.012, 0.060), (0.008, -0.012, 0.060),
        (-0.004, 0.019, 0.092), (-0.004, -0.019, 0.092),
        (0.007, 0.020, 0.086), (0.007, -0.020, 0.086),
    ]
    for i, loc in enumerate(dot_specs, 1):
        add_scale_dot(f"kfr_v0043_body_teal_scale_dot_{i:02d}", loc, 0.00115, col, m["scale"], root, "z")


def write_notes():
    text = bpy.data.texts.get(NOTES_NAME) or bpy.data.texts.new(NOTES_NAME)
    text.clear()
    text.write(
        "KFR-BLOCKOUT-v004.3 Goal Sprint Rebuild Pass 001\n"
        "Fast convergence pass toward reference sheet.\n\n"
        "Key changes:\n"
        "- Rebuilt from scratch in its own collection.\n"
        "- Much longer low raptor snout and lower sunglasses.\n"
        "- Forward sloping thick neck instead of vertical tube.\n"
        "- Compact chest, tucked pelvis, forward lean.\n"
        "- Connected bent legs and planted four-toed feet.\n"
        "- Long tapered counterbalance tail with root blend.\n"
        "- More numerous swept proto-quills and teal scale dots.\n\n"
        "Next likely pass: head/neck refinement or leg/foot pose lock before clothing.\n"
    )


def set_view_quality():
    try:
        bpy.context.scene.render.engine = "BLENDER_EEVEE_NEXT"
    except Exception:
        try:
            bpy.context.scene.render.engine = "BLENDER_EEVEE"
        except Exception:
            pass
    try:
        bpy.context.scene.unit_settings.system = "METRIC"
        bpy.context.scene.unit_settings.scale_length = 1.0
        bpy.context.scene.unit_settings.length_unit = "METERS"
    except Exception:
        pass


def main():
    ensure_object_mode()
    set_view_quality()
    rescue_visibility()

    m = mats()
    col = clean_or_create_collection(COLLECTION_NAME)
    root = empty(ROOT_NAME, (0, 0, 0.060), col)

    build_guides(col, m, root)
    build_core_anatomy(col, m, root)
    build_neck_head(col, m, root)
    build_dorsal_quills(col, m, root)
    build_legs_and_feet(col, m, root)
    build_arms_and_hands(col, m, root)
    build_tail(col, m, root)
    build_surface_detail(col, m, root)
    write_notes()

    # Only hide old work once the new build is actually completed.
    hide_prior_versions_after_success()
    col.hide_viewport = False
    col.hide_render = False

    bpy.ops.object.select_all(action="DESELECT")
    root.select_set(True)
    bpy.context.view_layer.objects.active = root

    print("KFR v004.3 goal sprint rebuild complete.")
    print(f"Collection: {COLLECTION_NAME}")
    print("Save as: kfr_blockout_v0043_goal_sprint_rebuild_pass_001.blend")


if __name__ == "__main__":
    main()
