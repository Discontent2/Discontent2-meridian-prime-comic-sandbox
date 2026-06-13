"""
Kavo "Forest" Rill KFR-BLOCKOUT-v002 Blender Starter Scene

Purpose:
    Create a correctly scaled, named, gray blockout starter scene for the
    KFR-BLOCKOUT-v002 refinement pass.

Run in Blender:
    1. Open Blender.
    2. Go to the Scripting workspace.
    3. Open this file.
    4. Press Run Script.

What this script does:
    - Sets metric units with millimeter workflow.
    - Creates a 127 mm / 5 inch scale guide.
    - Creates named blockout objects for Kavo / Forest.
    - Blocks broad boots, pelvis, torso, jacket, harness, head, arms, hands,
      compact left-wrist watch, tail, joint placeholders, and accessory handles.
    - Creates 14 named cameras matching the v002 screenshot protocol.
    - Optionally renders all 14 review views and exports OBJ / STL / GLB.

Important:
    This is an automated starter scene, not the final sculpt.
    A modeler should refine this into sculpt-aware forms before detail sculpt.
"""

import math
import os
from mathutils import Vector

import bpy

# -----------------------------------------------------------------------------
# User toggles
# -----------------------------------------------------------------------------

RENDER_ALL_VIEWS = False
EXPORT_SCENE_ASSETS = False
SAVE_BLEND_FILE = False

# Optional: set this to a local v001 OBJ path if you want to import it as a wire guide.
# Example: V001_REFERENCE_PATH = r"C:\\path\\to\\kfr_blockout_v001_full_model.obj"
IMPORT_V001_REFERENCE = False
V001_REFERENCE_PATH = ""

OUTPUT_FOLDER_NAME = "kfr-blockout-v002-output"

# -----------------------------------------------------------------------------
# Scene constants
# -----------------------------------------------------------------------------

FIGURE_HEIGHT_MM = 127.0
GROUND_Z = 0.0

COLLECTION_ROOT = "kfr_blockout_v002"
COLLECTION_GUIDES = "00_guides"
COLLECTION_BODY = "01_body_parts"
COLLECTION_GARMENTS = "02_garments_harness"
COLLECTION_JOINTS = "03_joint_placeholders"
COLLECTION_ACCESSORIES = "04_accessory_placeholders"
COLLECTION_CAMERAS = "05_review_cameras"
COLLECTION_V001 = "99_v001_reference_optional"

# Coordinate convention:
#   X = left / right
#   Y = front / back, negative Y is figure front
#   Z = up
#   Character left wrist is placed at positive X.

# -----------------------------------------------------------------------------
# Utility functions
# -----------------------------------------------------------------------------


def clean_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()


def set_units():
    scene = bpy.context.scene
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.scale_length = 0.001
    scene.unit_settings.length_unit = "MILLIMETERS"
    scene.render.resolution_x = 1400
    scene.render.resolution_y = 1400
    scene.render.film_transparent = False


def get_output_dir():
    root = bpy.path.abspath("//")
    if not root or root == "//":
        root = os.path.expanduser("~")
    out_dir = os.path.join(root, OUTPUT_FOLDER_NAME)
    os.makedirs(out_dir, exist_ok=True)
    return out_dir


def make_collection(name, parent=None):
    collection = bpy.data.collections.new(name)
    if parent is None:
        bpy.context.scene.collection.children.link(collection)
    else:
        parent.children.link(collection)
    return collection


def link_to_collection(obj, collection):
    for existing in list(obj.users_collection):
        existing.objects.unlink(obj)
    collection.objects.link(obj)


def create_material(name, color, roughness=0.55, alpha=1.0):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = (color[0], color[1], color[2], alpha)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        try:
            bsdf.inputs["Base Color"].default_value = (color[0], color[1], color[2], alpha)
            bsdf.inputs["Roughness"].default_value = roughness
            bsdf.inputs["Alpha"].default_value = alpha
        except Exception:
            pass
    if alpha < 1.0:
        mat.blend_method = "BLEND"
        mat.use_screen_refraction = True
    return mat


def apply_material(obj, mat):
    obj.data.materials.clear()
    obj.data.materials.append(mat)


def add_bevel(obj, amount=1.0, segments=3):
    bevel = obj.modifiers.new(name="soft_blockout_bevel", type="BEVEL")
    bevel.width = amount
    bevel.segments = segments
    bevel.affect = "EDGES"
    smooth = obj.modifiers.new(name="weighted_normals", type="WEIGHTED_NORMAL")
    return bevel, smooth


def add_cube(name, loc, dims, mat, collection, bevel=0.0):
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = f"{name}_mesh"
    obj.dimensions = dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    apply_material(obj, mat)
    if bevel > 0:
        add_bevel(obj, bevel, segments=3)
    link_to_collection(obj, collection)
    return obj


def add_uv_sphere(name, loc, dims, mat, collection, segments=32, rings=16):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segments, ring_count=rings, radius=1.0, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = f"{name}_mesh"
    obj.scale = (dims[0] / 2.0, dims[1] / 2.0, dims[2] / 2.0)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    apply_material(obj, mat)
    try:
        bpy.ops.object.shade_smooth()
    except Exception:
        pass
    link_to_collection(obj, collection)
    return obj


def add_cylinder_between(name, start, end, radius, mat, collection, vertices=24):
    start_v = Vector(start)
    end_v = Vector(end)
    mid = (start_v + end_v) / 2.0
    direction = end_v - start_v
    length = direction.length
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=length, location=mid)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = f"{name}_mesh"
    obj.rotation_euler = direction.to_track_quat("Z", "Y").to_euler()
    apply_material(obj, mat)
    try:
        bpy.ops.object.shade_smooth()
    except Exception:
        pass
    link_to_collection(obj, collection)
    return obj


def add_capsule(name, start, end, radius, mat, collection):
    parts = []
    parts.append(add_cylinder_between(f"{name}_shaft", start, end, radius, mat, collection))
    parts.append(add_uv_sphere(f"{name}_cap_a", start, (radius * 2, radius * 2, radius * 2), mat, collection))
    parts.append(add_uv_sphere(f"{name}_cap_b", end, (radius * 2, radius * 2, radius * 2), mat, collection))
    return parts


def add_cone(name, loc, radius1, radius2, depth, mat, collection, rotation=(0, 0, 0), vertices=16):
    bpy.ops.mesh.primitive_cone_add(vertices=vertices, radius1=radius1, radius2=radius2, depth=depth, location=loc, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = f"{name}_mesh"
    apply_material(obj, mat)
    try:
        bpy.ops.object.shade_smooth()
    except Exception:
        pass
    link_to_collection(obj, collection)
    return obj


def add_text(name, text, loc, size, mat, collection, rotation=(math.radians(90), 0, 0)):
    bpy.ops.object.text_add(location=loc, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = f"{name}_curve"
    obj.data.body = text
    obj.data.align_x = "CENTER"
    obj.data.align_y = "CENTER"
    obj.data.size = size
    apply_material(obj, mat)
    link_to_collection(obj, collection)
    return obj


def look_at(obj, target):
    target_v = Vector(target)
    direction = target_v - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def add_camera(name, loc, target, ortho_scale, collection):
    bpy.ops.object.camera_add(location=loc)
    cam = bpy.context.object
    cam.name = name
    cam.data.name = f"{name}_data"
    cam.data.type = "ORTHO"
    cam.data.ortho_scale = ortho_scale
    look_at(cam, target)
    link_to_collection(cam, collection)
    return cam


def add_sun_and_area_lights():
    bpy.ops.object.light_add(type="AREA", location=(0, -80, 170))
    area = bpy.context.object
    area.name = "kfr_scene_key_area_light"
    area.data.energy = 450
    area.data.size = 120

    bpy.ops.object.light_add(type="SUN", location=(0, 0, 120))
    sun = bpy.context.object
    sun.name = "kfr_scene_soft_sun_light"
    sun.data.energy = 1.2
    sun.rotation_euler = (math.radians(40), 0, math.radians(35))


def create_materials():
    return {
        "body": create_material("kfr_blockout_body_gray", (0.48, 0.50, 0.50), 0.65),
        "dark": create_material("kfr_blockout_dark_gray_gloves_watch_shades", (0.08, 0.08, 0.08), 0.72),
        "garment": create_material("kfr_blockout_garment_gray", (0.32, 0.33, 0.33), 0.68),
        "harness": create_material("kfr_blockout_harness_midgray", (0.20, 0.20, 0.20), 0.7),
        "joint": create_material("kfr_blockout_joint_placeholder_blue", (0.15, 0.38, 0.78), 0.45, 0.72),
        "guide": create_material("kfr_blockout_scale_guide_green", (0.2, 0.7, 0.45), 0.4, 0.9),
        "quill": create_material("kfr_blockout_proto_quill_marker", (0.45, 0.13, 0.10), 0.6),
        "ground": create_material("kfr_blockout_ground_light_gray", (0.70, 0.70, 0.70), 0.8),
    }

# -----------------------------------------------------------------------------
# Blockout builders
# -----------------------------------------------------------------------------


def build_guides(collections, mats):
    guides = collections[COLLECTION_GUIDES]
    add_cube("kfr_ground_plane_180mm_x_180mm", (0, 0, -0.5), (180, 180, 1), mats["ground"], guides)
    add_cube("kfr_scale_127mm_height_guide", (-58, -46, FIGURE_HEIGHT_MM / 2), (2, 2, FIGURE_HEIGHT_MM), mats["guide"], guides)
    add_text("kfr_scale_127mm_height_label", "127 mm / 5 in", (-58, -51, 130), 4.0, mats["guide"], guides)


def build_boots_legs_pants(collections, mats):
    body = collections[COLLECTION_BODY]
    garments = collections[COLLECTION_GARMENTS]

    # Boots and soles
    add_cube("kfr_part_009_leg_left_pants_boot_blockout_boot_base", (8, -2, 4), (14, 25, 8), mats["dark"], body, bevel=1.5)
    add_cube("kfr_part_010_leg_right_pants_boot_blockout_boot_base", (-8, -2, 4), (14, 25, 8), mats["dark"], body, bevel=1.5)
    add_cube("kfr_part_009_leg_left_pants_boot_blockout_sole", (8, -2, 1.2), (16, 27, 2.5), mats["harness"], body, bevel=0.8)
    add_cube("kfr_part_010_leg_right_pants_boot_blockout_sole", (-8, -2, 1.2), (16, 27, 2.5), mats["harness"], body, bevel=0.8)

    # Four-toe placeholders on each boot front, negative Y side
    for side_name, x_center in [("left", 8), ("right", -8)]:
        for idx, offset in enumerate([-4.5, -1.5, 1.5, 4.5], start=1):
            add_uv_sphere(
                f"kfr_{side_name}_boot_four_toe_clearance_{idx}",
                (x_center + offset, -15.5, 5.0),
                (2.5, 4.0, 2.2),
                mats["body"],
                body,
                segments=16,
                rings=8,
            )

    # Pants / legs
    add_capsule("kfr_part_009_leg_left_pants_boot_blockout_upper_leg", (8, 0, 14), (8, 1, 50), 5.2, mats["garment"], body)
    add_capsule("kfr_part_010_leg_right_pants_boot_blockout_upper_leg", (-8, 0, 14), (-8, 1, 50), 5.2, mats["garment"], body)

    # Reinforcement panels and cargo pockets
    add_cube("kfr_left_pants_thigh_reinforcement_panel", (8, -5.6, 36), (9, 1.3, 13), mats["harness"], garments, bevel=0.4)
    add_cube("kfr_right_pants_thigh_reinforcement_panel", (-8, -5.6, 36), (9, 1.3, 13), mats["harness"], garments, bevel=0.4)
    add_cube("kfr_left_pants_knee_reinforcement_panel", (8, -5.7, 22), (9, 1.3, 8), mats["harness"], garments, bevel=0.4)
    add_cube("kfr_right_pants_knee_reinforcement_panel", (-8, -5.7, 22), (9, 1.3, 8), mats["harness"], garments, bevel=0.4)
    add_cube("kfr_left_cargo_pocket_clearance_mass", (14.2, -1.5, 34), (2.2, 7, 10), mats["harness"], garments, bevel=0.4)
    add_cube("kfr_right_utility_pocket_clearance_mass", (-14.2, -1.5, 32), (2.2, 5, 8), mats["harness"], garments, bevel=0.4)


def build_pelvis_torso_garments(collections, mats):
    body = collections[COLLECTION_BODY]
    garments = collections[COLLECTION_GARMENTS]

    add_cube("kfr_part_004_pelvis_hip_tail_socket_blockout", (0, 2, 55), (29, 18, 15), mats["body"], body, bevel=2.0)
    add_cube("kfr_pants_waistband_seam_blockout", (0, -1, 62), (31, 16, 4), mats["garment"], garments, bevel=0.6)

    # Torso core and garment stack
    add_uv_sphere("kfr_torso_core_mass_under_garments", (0, 0, 82), (31, 19, 40), mats["body"], body)
    add_cube("kfr_part_002_torso_front_jacket_harness_blockout_jacket_front", (0, -5.5, 82), (35, 4.5, 39), mats["garment"], garments, bevel=1.2)
    add_cube("kfr_part_003_torso_back_jacket_harness_blockout_jacket_back", (0, 5.7, 82), (35, 4.2, 39), mats["garment"], garments, bevel=1.2)
    add_cube("kfr_black_field_knit_underlayer_visible_panel", (0, -8.1, 82), (18, 2, 31), mats["dark"], garments, bevel=0.5)
    add_cube("kfr_cropped_jacket_hem_clearance_marker", (0, -4.9, 64), (35, 5, 3), mats["harness"], garments, bevel=0.5)

    # Collar and jacket cuffs are handled with arms too, but collar belongs here.
    add_cube("kfr_jacket_sturdy_collar_mass", (0, -2.5, 102), (34, 10, 6), mats["garment"], garments, bevel=1.0)

    # Harness path, simplified straps and panels
    add_cube("kfr_route_harness_chest_vertical_strap_left", (9.5, -9.0, 84), (3, 2, 32), mats["harness"], garments, bevel=0.3)
    add_cube("kfr_route_harness_chest_vertical_strap_right", (-9.5, -9.0, 84), (3, 2, 32), mats["harness"], garments, bevel=0.3)
    add_cube("kfr_route_harness_waist_belt", (0, -8.8, 70), (33, 2.5, 4), mats["harness"], garments, bevel=0.4)
    add_cube("kfr_route_harness_back_panel", (0, 8.4, 84), (20, 2.5, 16), mats["harness"], garments, bevel=0.5)
    add_cube("kfr_chest_badge_zone_placeholder_left", (6.2, -10.5, 91), (5, 1.2, 5), mats["joint"], garments, bevel=0.25)
    add_cube("kfr_chest_badge_zone_placeholder_right", (-6.2, -10.5, 91), (5, 1.2, 5), mats["joint"], garments, bevel=0.25)


def build_head(collections, mats):
    body = collections[COLLECTION_BODY]
    head_z = 113.5
    add_uv_sphere("kfr_part_001_head_primary_shades_blockout_skull", (0, -1, head_z), (23, 18, 22), mats["body"], body)
    add_cube("kfr_part_001_head_primary_shades_blockout_snout", (0, -13, 110.5), (16, 14, 9), mats["body"], body, bevel=1.1)
    add_cube("kfr_part_001_head_primary_shades_blockout_brow_mass", (0, -10.2, 118.2), (20, 5, 4), mats["body"], body, bevel=0.8)
    add_cube("kfr_part_001_head_primary_shades_blockout_mouth_line_plane", (0, -20.2, 108), (14, 0.8, 1.2), mats["dark"], body, bevel=0.2)

    # Thick shades, not wire-thin eyewear.
    add_cube("kfr_primary_shades_left_lens_mass", (5.4, -13.3, 116.6), (7, 1.6, 4.2), mats["dark"], body, bevel=0.5)
    add_cube("kfr_primary_shades_right_lens_mass", (-5.4, -13.3, 116.6), (7, 1.6, 4.2), mats["dark"], body, bevel=0.5)
    add_cube("kfr_primary_shades_bridge_mass", (0, -13.4, 116.6), (3, 1.5, 2.2), mats["dark"], body, bevel=0.3)

    # Neck mass
    add_capsule("kfr_neck_thick_swivel_ready_mass", (0, 0, 95), (0, 0, 105), 6.0, mats["body"], body)

    # Short sparse proto-quills, intentionally chunky.
    quill_positions = [(-5.5, 2.0, 124.5), (-2.5, 2.2, 126.0), (0, 2.4, 126.8), (2.5, 2.2, 126.0), (5.5, 2.0, 124.5)]
    for i, loc in enumerate(quill_positions, start=1):
        add_cone(f"kfr_short_sparse_proto_quill_{i}", loc, 1.4, 0.35, 5.0, mats["quill"], body, rotation=(0, 0, 0), vertices=14)


def build_arms_hands_watch(collections, mats):
    body = collections[COLLECTION_BODY]
    garments = collections[COLLECTION_GARMENTS]

    # Shoulders and arms. Character left is positive X and carries the watch.
    add_capsule("kfr_part_005_arm_left_watch_wrist_blockout_upper_arm", (21, 0, 91), (32, 0, 73), 4.2, mats["body"], body)
    add_capsule("kfr_part_006_arm_right_blockout_upper_arm", (-21, 0, 91), (-32, 0, 73), 4.2, mats["body"], body)
    add_capsule("kfr_part_005_arm_left_watch_wrist_blockout_forearm", (32, 0, 73), (35, -1, 58), 3.8, mats["body"], body)
    add_capsule("kfr_part_006_arm_right_blockout_forearm", (-32, 0, 73), (-35, -1, 58), 3.8, mats["body"], body)

    # Jacket cuffs and glove cuffs
    add_cube("kfr_left_jacket_cuff_clearance_mass", (34.8, -1, 62), (8, 8, 5), mats["garment"], garments, bevel=0.7)
    add_cube("kfr_right_jacket_cuff_clearance_mass", (-34.8, -1, 62), (8, 8, 5), mats["garment"], garments, bevel=0.7)
    add_cube("kfr_left_black_fingerless_glove_cuff", (35.5, -1.5, 55.2), (8, 7, 4), mats["dark"], body, bevel=0.6)
    add_cube("kfr_right_black_fingerless_glove_cuff", (-35.5, -1.5, 55.2), (8, 7, 4), mats["dark"], body, bevel=0.6)

    # Palms
    add_cube("kfr_part_007_hand_left_gloved_blockout_palm", (36.0, -3.8, 50.5), (8, 6, 7), mats["body"], body, bevel=0.7)
    add_cube("kfr_part_008_hand_right_grip_blockout_palm", (-36.0, -3.8, 50.5), (8, 6, 7), mats["body"], body, bevel=0.7)

    # Fingers, exactly four per hand including thumb equivalent.
    for side_name, x_base, sign in [("left", 36.0, 1), ("right", -36.0, -1)]:
        for idx, offset in enumerate([-3.0, -1.0, 1.0], start=1):
            add_capsule(
                f"kfr_{side_name}_hand_visible_saurian_finger_{idx}",
                (x_base + offset * sign, -7.0, 50.5),
                (x_base + offset * sign, -11.0, 50.0),
                0.9,
                mats["body"],
                body,
            )
        # Thumb equivalent angles outward.
        add_capsule(
            f"kfr_{side_name}_hand_visible_saurian_thumb_equivalent_4",
            (x_base + 4.2 * sign, -4.5, 50.3),
            (x_base + 7.0 * sign, -8.0, 50.0),
            0.9,
            mats["body"],
            body,
        )

    # Compact left-wrist GPR watch, hard device not wrist warmer.
    add_cube("kfr_part_005_left_wrist_compact_gpr_watch_case", (36.1, -5.0, 57.5), (6.2, 2.6, 4.2), mats["dark"], body, bevel=0.35)
    add_cube("kfr_left_wrist_compact_gpr_watch_screen_plane", (36.1, -6.45, 57.5), (4.3, 0.35, 2.3), mats["joint"], body, bevel=0.15)
    add_cube("kfr_left_wrist_watch_strap_upper", (36.1, -2.6, 57.5), (7.5, 2.0, 4.8), mats["dark"], body, bevel=0.4)


def build_tail(collections, mats):
    body = collections[COLLECTION_BODY]
    joints = collections[COLLECTION_JOINTS]

    # Keyed socket placeholder and tail mass chain.
    add_cube("kfr_tail_keyed_socket_blockout_in_pelvis", (0, 11.7, 56), (13, 5, 9), mats["joint"], joints, bevel=0.5)

    tail_points = [
        (0, 13, 55),
        (0, 25, 49),
        (0, 38, 39),
        (0, 50, 27),
        (0, 61, 16),
        (0, 68, 8),
    ]
    radii = [6.0, 5.4, 4.7, 3.8, 2.8]
    for i in range(len(tail_points) - 1):
        add_capsule(f"kfr_part_011_tail_keyed_blockout_segment_{i + 1}", tail_points[i], tail_points[i + 1], radii[i], mats["body"], body)
    add_uv_sphere("kfr_part_011_tail_keyed_blockout_blunt_tip", tail_points[-1], (5, 5, 5), mats["body"], body, segments=16, rings=8)


def build_joint_placeholders(collections, mats):
    joints = collections[COLLECTION_JOINTS]
    joint_specs = [
        ("kfr_joint_neck_placeholder", (0, 0, 102), (9, 9, 9)),
        ("kfr_joint_left_shoulder_placeholder", (21, 0, 91), (8, 8, 8)),
        ("kfr_joint_right_shoulder_placeholder", (-21, 0, 91), (8, 8, 8)),
        ("kfr_joint_left_wrist_placeholder_watch_clearance", (35.4, -1, 57), (5, 5, 5)),
        ("kfr_joint_right_wrist_placeholder", (-35.4, -1, 57), (5, 5, 5)),
        ("kfr_joint_left_hip_placeholder_pocket_clearance", (8, 1, 56), (7, 7, 7)),
        ("kfr_joint_right_hip_placeholder_pocket_clearance", (-8, 1, 56), (7, 7, 7)),
        ("kfr_joint_optional_waist_placeholder", (0, 0, 64), (12, 12, 5)),
        ("kfr_joint_left_knee_optional_placeholder", (8, 0, 26), (6, 6, 5)),
        ("kfr_joint_right_knee_optional_placeholder", (-8, 0, 26), (6, 6, 5)),
        ("kfr_joint_tail_keyed_socket_placeholder", (0, 11.5, 56), (10, 5, 8)),
    ]
    for name, loc, dims in joint_specs:
        add_uv_sphere(name, loc, dims, mats["joint"], joints, segments=16, rings=8)


def build_accessory_placeholders(collections, mats):
    accessories = collections[COLLECTION_ACCESSORIES]
    # Side layout, not in hand yet, for scale and grip checks.
    add_cylinder_between("kfr_acc_placeholder_route_probe_staff_handle", (54, -20, 8), (54, -20, 70), 1.4, mats["dark"], accessories, vertices=20)
    add_cylinder_between("kfr_acc_placeholder_black_path_flag_marker_handle", (61, -20, 8), (61, -20, 50), 1.3, mats["dark"], accessories, vertices=20)
    add_cube("kfr_acc_placeholder_black_path_flag_panel", (61, -21.5, 48), (14, 1.2, 9), mats["dark"], accessories, bevel=0.2)
    add_cube("kfr_acc_placeholder_optional_handheld_route_reader_backup", (51, -20, 82), (9, 3, 7), mats["harness"], accessories, bevel=0.5)
    add_text("kfr_accessory_placeholders_label", "Accessory grip placeholders", (58, -30, 5), 3.2, mats["guide"], accessories)


def import_v001_reference(collections, mats):
    if not IMPORT_V001_REFERENCE or not V001_REFERENCE_PATH or not os.path.exists(V001_REFERENCE_PATH):
        return
    ext = os.path.splitext(V001_REFERENCE_PATH)[1].lower()
    before = set(bpy.data.objects)
    try:
        if ext == ".obj":
            bpy.ops.import_scene.obj(filepath=V001_REFERENCE_PATH)
        elif ext in [".glb", ".gltf"]:
            bpy.ops.import_scene.gltf(filepath=V001_REFERENCE_PATH)
        else:
            print(f"Unsupported v001 reference format: {ext}")
            return
    except Exception as exc:
        print(f"Could not import v001 reference: {exc}")
        return
    after = set(bpy.data.objects)
    imported = list(after - before)
    for obj in imported:
        obj.name = f"v001_reference_{obj.name}"
        if hasattr(obj, "display_type"):
            obj.display_type = "WIRE"
        link_to_collection(obj, collections[COLLECTION_V001])


def build_cameras(collections):
    cams = collections[COLLECTION_CAMERAS]
    camera_specs = [
        ("kfr_blockout_v002_cam_01_front_ortho", (0, -220, 70), (0, 0, 65), 145),
        ("kfr_blockout_v002_cam_02_side_ortho", (220, 0, 70), (0, 0, 65), 145),
        ("kfr_blockout_v002_cam_03_back_ortho", (0, 220, 70), (0, 0, 65), 145),
        ("kfr_blockout_v002_cam_04_three_quarter_shelf", (150, -190, 95), (0, 0, 66), 145),
        ("kfr_blockout_v002_cam_05_head_closeup", (0, -95, 115), (0, -5, 114), 45),
        ("kfr_blockout_v002_cam_06_left_wrist_watch_closeup", (90, -70, 60), (35, -3, 56), 34),
        ("kfr_blockout_v002_cam_07_hands_grip_closeup", (0, -90, 52), (0, -5, 52), 80),
        ("kfr_blockout_v002_cam_08_boots_stance_closeup", (0, -80, 15), (0, -3, 7), 60),
        ("kfr_blockout_v002_cam_09_tail_socket_balance_closeup", (80, 115, 45), (0, 28, 39), 85),
        ("kfr_blockout_v002_cam_10_jacket_harness_pants_closeup", (0, -110, 75), (0, -3, 76), 75),
        ("kfr_blockout_v002_cam_11_top_down_mass_check", (0, 0, 220), (0, 0, 55), 155),
        ("kfr_blockout_v002_cam_12_scale_ruler_scene", (-100, -180, 85), (-20, -20, 65), 165),
        ("kfr_blockout_v002_cam_13_accessory_grip_placeholders", (105, -100, 55), (56, -20, 42), 85),
        ("kfr_blockout_v002_cam_14_joint_placeholders", (110, -140, 85), (0, 0, 65), 150),
    ]
    created = {}
    for name, loc, target, ortho in camera_specs:
        created[name] = add_camera(name, loc, target, ortho, cams)
    bpy.context.scene.camera = created["kfr_blockout_v002_cam_01_front_ortho"]
    return created


def render_all_views(cameras):
    out_dir = os.path.join(get_output_dir(), "renders")
    os.makedirs(out_dir, exist_ok=True)
    name_map = [
        ("kfr_blockout_v002_cam_01_front_ortho", "kfr_blockout_v002_01_front_ortho.png"),
        ("kfr_blockout_v002_cam_02_side_ortho", "kfr_blockout_v002_02_side_ortho.png"),
        ("kfr_blockout_v002_cam_03_back_ortho", "kfr_blockout_v002_03_back_ortho.png"),
        ("kfr_blockout_v002_cam_04_three_quarter_shelf", "kfr_blockout_v002_04_three_quarter_shelf.png"),
        ("kfr_blockout_v002_cam_05_head_closeup", "kfr_blockout_v002_05_head_closeup.png"),
        ("kfr_blockout_v002_cam_06_left_wrist_watch_closeup", "kfr_blockout_v002_06_left_wrist_watch_closeup.png"),
        ("kfr_blockout_v002_cam_07_hands_grip_closeup", "kfr_blockout_v002_07_hands_grip_closeup.png"),
        ("kfr_blockout_v002_cam_08_boots_stance_closeup", "kfr_blockout_v002_08_boots_stance_closeup.png"),
        ("kfr_blockout_v002_cam_09_tail_socket_balance_closeup", "kfr_blockout_v002_09_tail_socket_balance_closeup.png"),
        ("kfr_blockout_v002_cam_10_jacket_harness_pants_closeup", "kfr_blockout_v002_10_jacket_harness_pants_closeup.png"),
        ("kfr_blockout_v002_cam_11_top_down_mass_check", "kfr_blockout_v002_11_top_down_mass_check.png"),
        ("kfr_blockout_v002_cam_12_scale_ruler_scene", "kfr_blockout_v002_12_scale_ruler_scene.png"),
        ("kfr_blockout_v002_cam_13_accessory_grip_placeholders", "kfr_blockout_v002_13_accessory_grip_placeholders.png"),
        ("kfr_blockout_v002_cam_14_joint_placeholders", "kfr_blockout_v002_14_joint_placeholders.png"),
    ]
    for cam_name, filename in name_map:
        bpy.context.scene.camera = cameras[cam_name]
        bpy.context.scene.render.filepath = os.path.join(out_dir, filename)
        bpy.ops.render.render(write_still=True)


def export_scene_assets():
    out_dir = os.path.join(get_output_dir(), "exports")
    os.makedirs(out_dir, exist_ok=True)
    obj_path = os.path.join(out_dir, "kfr_blockout_v002_starter_scene.obj")
    stl_path = os.path.join(out_dir, "kfr_blockout_v002_starter_scene.stl")
    glb_path = os.path.join(out_dir, "kfr_blockout_v002_starter_scene.glb")

    try:
        bpy.ops.wm.obj_export(filepath=obj_path, export_selected_objects=False)
    except Exception:
        try:
            bpy.ops.export_scene.obj(filepath=obj_path)
        except Exception as exc:
            print(f"OBJ export skipped: {exc}")

    try:
        bpy.ops.wm.stl_export(filepath=stl_path)
    except Exception:
        try:
            bpy.ops.export_mesh.stl(filepath=stl_path)
        except Exception as exc:
            print(f"STL export skipped: {exc}")

    try:
        bpy.ops.export_scene.gltf(filepath=glb_path, export_format="GLB")
    except Exception as exc:
        print(f"GLB export skipped: {exc}")


def save_blend_file():
    out_dir = get_output_dir()
    blend_path = os.path.join(out_dir, "kfr_blockout_v002_starter_scene.blend")
    bpy.ops.wm.save_as_mainfile(filepath=blend_path)

# -----------------------------------------------------------------------------
# Main build
# -----------------------------------------------------------------------------


def build_scene():
    clean_scene()
    set_units()

    root = make_collection(COLLECTION_ROOT)
    collections = {
        COLLECTION_GUIDES: make_collection(COLLECTION_GUIDES, root),
        COLLECTION_BODY: make_collection(COLLECTION_BODY, root),
        COLLECTION_GARMENTS: make_collection(COLLECTION_GARMENTS, root),
        COLLECTION_JOINTS: make_collection(COLLECTION_JOINTS, root),
        COLLECTION_ACCESSORIES: make_collection(COLLECTION_ACCESSORIES, root),
        COLLECTION_CAMERAS: make_collection(COLLECTION_CAMERAS, root),
        COLLECTION_V001: make_collection(COLLECTION_V001, root),
    }

    mats = create_materials()

    build_guides(collections, mats)
    build_boots_legs_pants(collections, mats)
    build_pelvis_torso_garments(collections, mats)
    build_tail(collections, mats)
    build_head(collections, mats)
    build_arms_hands_watch(collections, mats)
    build_joint_placeholders(collections, mats)
    build_accessory_placeholders(collections, mats)
    import_v001_reference(collections, mats)
    add_sun_and_area_lights()
    cameras = build_cameras(collections)

    # Add a scene-level note as a text object near the ground.
    add_text(
        "kfr_v002_scene_note",
        "KFR-BLOCKOUT-v002 starter scene: refine before detail sculpt",
        (0, -70, 4),
        3.2,
        mats["guide"],
        collections[COLLECTION_GUIDES],
    )

    return cameras


if __name__ == "__main__":
    cameras = build_scene()
    if RENDER_ALL_VIEWS:
        render_all_views(cameras)
    if EXPORT_SCENE_ASSETS:
        export_scene_assets()
    if SAVE_BLEND_FILE:
        save_blend_file()

    print("KFR-BLOCKOUT-v002 starter scene created.")
    print("Next: refine the forms by hand, then render / submit views 01 through 14.")
