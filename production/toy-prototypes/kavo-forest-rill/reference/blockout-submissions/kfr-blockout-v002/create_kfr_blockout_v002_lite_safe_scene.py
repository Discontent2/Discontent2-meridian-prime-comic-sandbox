"""
Kavo "Forest" Rill KFR-BLOCKOUT-v002 Lite Safe Blender Starter Scene

Use this if the full starter script crashes Blender.

Run in Blender:
    1. Open Blender.
    2. File > New > General.
    3. Go to Scripting.
    4. Open this file.
    5. Press Run Script.

Safety choices in this version:
    - No bevel modifiers.
    - No weighted normals.
    - No text objects.
    - No smooth shading.
    - No node materials.
    - No automatic rendering.
    - No automatic exporting.
    - Fewer objects.

Goal:
    Create a stable, correctly named, millimeter-scale v002 layout skeleton.
"""

import math
import bpy
from mathutils import Vector

FIGURE_HEIGHT_MM = 127.0

# Coordinate convention:
# X = character left / right. Character left wrist is positive X.
# Y = front / back. Negative Y is figure front.
# Z = up.


def reset_scene():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()


def set_units():
    scene = bpy.context.scene
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.scale_length = 0.001
    scene.unit_settings.length_unit = "MILLIMETERS"
    scene.render.resolution_x = 1200
    scene.render.resolution_y = 1200


def make_mat(name, rgba):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = rgba
    return mat


def make_collection(name):
    col = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(col)
    return col


def move_to_collection(obj, col):
    for c in list(obj.users_collection):
        c.objects.unlink(obj)
    col.objects.link(obj)


def cube(name, loc, scale, mat, col):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.dimensions = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    move_to_collection(obj, col)
    return obj


def sphere(name, loc, scale, mat, col, segments=16, rings=8):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segments, ring_count=rings, radius=1, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.scale = (scale[0] / 2, scale[1] / 2, scale[2] / 2)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    move_to_collection(obj, col)
    return obj


def cyl_between(name, start, end, radius, mat, col, vertices=16):
    start = Vector(start)
    end = Vector(end)
    mid = (start + end) / 2
    direction = end - start
    length = direction.length
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=length, location=mid)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.rotation_euler = direction.to_track_quat("Z", "Y").to_euler()
    obj.data.materials.append(mat)
    move_to_collection(obj, col)
    return obj


def camera(name, loc, target, ortho_scale, col):
    bpy.ops.object.camera_add(location=loc)
    cam = bpy.context.object
    cam.name = name
    cam.data.type = "ORTHO"
    cam.data.ortho_scale = ortho_scale
    direction = Vector(target) - cam.location
    cam.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    move_to_collection(cam, col)
    return cam


def build_scene():
    reset_scene()
    set_units()

    # Collections
    root = make_collection("kfr_blockout_v002_lite_safe")
    guides = bpy.data.collections.new("00_guides")
    body = bpy.data.collections.new("01_body_parts")
    garments = bpy.data.collections.new("02_garments_harness")
    joints = bpy.data.collections.new("03_joint_placeholders")
    accessories = bpy.data.collections.new("04_accessory_placeholders")
    cameras = bpy.data.collections.new("05_review_cameras")
    for col in [guides, body, garments, joints, accessories, cameras]:
        root.children.link(col)

    # Materials, viewport-only simple diffuse.
    gray = make_mat("kfr_lite_body_gray", (0.48, 0.50, 0.50, 1))
    dark = make_mat("kfr_lite_dark_gray", (0.08, 0.08, 0.08, 1))
    cloth = make_mat("kfr_lite_cloth_gray", (0.30, 0.31, 0.31, 1))
    joint = make_mat("kfr_lite_joint_blue", (0.1, 0.3, 0.9, 0.75))
    guide = make_mat("kfr_lite_guide_green", (0.1, 0.7, 0.35, 1))
    quill = make_mat("kfr_lite_quill_marker", (0.45, 0.12, 0.08, 1))
    ground = make_mat("kfr_lite_ground_gray", (0.70, 0.70, 0.70, 1))

    # Ground and scale guide.
    cube("kfr_ground_plane", (0, 0, -0.5), (180, 180, 1), ground, guides)
    cube("kfr_scale_127mm_height_guide", (-55, -45, 63.5), (2, 2, 127), guide, guides)

    # Boots and legs.
    cube("kfr_part_009_leg_left_pants_boot_blockout_boot", (8, -2, 4), (15, 25, 8), dark, body)
    cube("kfr_part_010_leg_right_pants_boot_blockout_boot", (-8, -2, 4), (15, 25, 8), dark, body)
    cyl_between("kfr_part_009_leg_left_pants_boot_blockout_leg", (8, 0, 10), (8, 0, 50), 5, cloth, body)
    cyl_between("kfr_part_010_leg_right_pants_boot_blockout_leg", (-8, 0, 10), (-8, 0, 50), 5, cloth, body)

    # Four toe placeholders per boot.
    for x_base, side in [(8, "left"), (-8, "right")]:
        for i, dx in enumerate([-4.5, -1.5, 1.5, 4.5], start=1):
            sphere(f"kfr_{side}_boot_toe_placeholder_{i}", (x_base + dx, -15, 5), (2.5, 4, 2), gray, body)

    # Pelvis, torso, jacket, underlayer, harness.
    cube("kfr_part_004_pelvis_hip_tail_socket_blockout", (0, 2, 55), (30, 18, 15), gray, body)
    sphere("kfr_torso_core_mass", (0, 0, 82), (32, 20, 40), gray, body)
    cube("kfr_cropped_route_jacket_front_mass", (0, -6, 82), (36, 5, 38), cloth, garments)
    cube("kfr_cropped_route_jacket_back_mass", (0, 6, 82), (36, 5, 38), cloth, garments)
    cube("kfr_black_field_knit_underlayer_visible_mass", (0, -9, 82), (18, 2, 30), dark, garments)
    cube("kfr_jacket_collar_mass", (0, -2, 103), (34, 10, 6), cloth, garments)
    cube("kfr_route_harness_left_strap", (9, -10, 84), (3, 2, 32), dark, garments)
    cube("kfr_route_harness_right_strap", (-9, -10, 84), (3, 2, 32), dark, garments)
    cube("kfr_route_harness_waist_belt", (0, -9, 70), (34, 2, 4), dark, garments)

    # Head, snout, brow, shades, proto-quills.
    sphere("kfr_part_001_head_primary_shades_blockout_skull", (0, -1, 113), (24, 18, 22), gray, body)
    cube("kfr_part_001_head_primary_shades_blockout_snout", (0, -13, 110), (16, 14, 9), gray, body)
    cube("kfr_part_001_head_primary_shades_blockout_brow", (0, -10, 118), (20, 5, 4), gray, body)
    cube("kfr_primary_shades_mass", (0, -13.5, 116.5), (18, 2, 4), dark, body)
    cyl_between("kfr_neck_swivel_ready_mass", (0, 0, 95), (0, 0, 105), 6, gray, body)
    for i, x in enumerate([-5, -2.5, 0, 2.5, 5], start=1):
        cyl_between(f"kfr_short_sparse_proto_quill_{i}", (x, 2, 123), (x, 2.5, 128), 0.8, quill, body)

    # Arms and hands. Character left is positive X.
    cyl_between("kfr_part_005_arm_left_watch_wrist_blockout_upper", (21, 0, 91), (32, 0, 73), 4, gray, body)
    cyl_between("kfr_part_006_arm_right_blockout_upper", (-21, 0, 91), (-32, 0, 73), 4, gray, body)
    cyl_between("kfr_part_005_arm_left_watch_wrist_blockout_forearm", (32, 0, 73), (35, -1, 58), 3.5, gray, body)
    cyl_between("kfr_part_006_arm_right_blockout_forearm", (-32, 0, 73), (-35, -1, 58), 3.5, gray, body)
    cube("kfr_left_black_fingerless_glove_cuff", (35.5, -1.5, 55), (8, 7, 4), dark, body)
    cube("kfr_right_black_fingerless_glove_cuff", (-35.5, -1.5, 55), (8, 7, 4), dark, body)
    cube("kfr_part_007_hand_left_gloved_blockout_palm", (36, -4, 50), (8, 6, 7), gray, body)
    cube("kfr_part_008_hand_right_grip_blockout_palm", (-36, -4, 50), (8, 6, 7), gray, body)

    # Four fingers per hand.
    for side, x_base, sign in [("left", 36, 1), ("right", -36, -1)]:
        for i, dx in enumerate([-3, -1, 1], start=1):
            cyl_between(f"kfr_{side}_hand_finger_{i}", (x_base + dx * sign, -7, 50), (x_base + dx * sign, -11, 50), 0.8, gray, body)
        cyl_between(f"kfr_{side}_hand_thumb_equivalent_4", (x_base + 4 * sign, -5, 50), (x_base + 7 * sign, -8, 50), 0.8, gray, body)

    # Compact left wrist watch, not wrist warmer.
    cube("kfr_left_wrist_compact_gpr_watch_case", (36, -5.2, 57.5), (6, 2.5, 4), dark, body)
    cube("kfr_left_wrist_compact_gpr_watch_screen", (36, -6.6, 57.5), (4, 0.3, 2), joint, body)

    # Tail and keyed socket.
    cube("kfr_tail_keyed_socket_placeholder", (0, 12, 56), (13, 5, 9), joint, joints)
    tail_pts = [(0, 13, 55), (0, 27, 48), (0, 42, 34), (0, 57, 18), (0, 68, 8)]
    radii = [5.8, 5.0, 4.0, 3.0]
    for i in range(len(tail_pts) - 1):
        cyl_between(f"kfr_part_011_tail_segment_{i+1}", tail_pts[i], tail_pts[i+1], radii[i], gray, body)
    sphere("kfr_part_011_tail_blunt_tip", tail_pts[-1], (5, 5, 5), gray, body)

    # Joint placeholders.
    joint_specs = [
        ("kfr_joint_neck_placeholder", (0, 0, 102), (9, 9, 9)),
        ("kfr_joint_left_shoulder_placeholder", (21, 0, 91), (8, 8, 8)),
        ("kfr_joint_right_shoulder_placeholder", (-21, 0, 91), (8, 8, 8)),
        ("kfr_joint_left_wrist_placeholder_watch_clearance", (35, -1, 57), (5, 5, 5)),
        ("kfr_joint_right_wrist_placeholder", (-35, -1, 57), (5, 5, 5)),
        ("kfr_joint_left_hip_placeholder", (8, 1, 56), (7, 7, 7)),
        ("kfr_joint_right_hip_placeholder", (-8, 1, 56), (7, 7, 7)),
        ("kfr_joint_tail_socket_placeholder", (0, 11, 56), (10, 5, 8)),
    ]
    for name, loc, scale in joint_specs:
        sphere(name, loc, scale, joint, joints)

    # Accessory placeholders.
    cyl_between("kfr_acc_route_probe_staff_handle_placeholder", (54, -20, 8), (54, -20, 68), 1.3, dark, accessories)
    cyl_between("kfr_acc_black_path_flag_marker_handle_placeholder", (61, -20, 8), (61, -20, 48), 1.3, dark, accessories)
    cube("kfr_acc_black_path_flag_panel_placeholder", (61, -21.5, 47), (14, 1, 9), dark, accessories)
    cube("kfr_acc_optional_handheld_route_reader_backup_placeholder", (51, -20, 82), (9, 3, 7), dark, accessories)

    # Lights.
    bpy.ops.object.light_add(type="AREA", location=(0, -80, 160))
    light = bpy.context.object
    light.name = "kfr_lite_key_area_light"
    light.data.energy = 350
    light.data.size = 120

    # Review cameras.
    cam_specs = [
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
    made_cameras = []
    for name, loc, target, ortho in cam_specs:
        made_cameras.append(camera(name, loc, target, ortho, cameras))
    bpy.context.scene.camera = made_cameras[0]

    print("KFR-BLOCKOUT-v002 Lite Safe starter scene created.")
    print("Save the file now as: kfr_blockout_v002_lite_safe_starter_scene.blend")


if __name__ == "__main__":
    build_scene()
