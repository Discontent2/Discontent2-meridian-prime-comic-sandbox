"""
KFR-BLOCKOUT-v002 Stage 02: Legs / Pelvis / Tail

Run this only after Stage 01 passes and you have saved:
    kfr_blockout_v002_stage_01_pass.blend

This stage adds:
    - left/right leg blocks over the boots
    - pants reinforcement panels
    - cargo pocket clearance masses
    - pelvis / hip / tail socket block
    - keyed tail socket placeholder
    - blocky balance-tail path

Safety choices:
    - raw mesh cubes only
    - no bpy.ops primitive mesh creation
    - no cameras
    - no lights
    - no modifiers
    - no scene reset

If this crashes Blender, reopen your Stage 01 saved file and report Stage 02 crashed.
If this succeeds, save as kfr_blockout_v002_stage_02_pass.blend.
"""

import bpy

ROOT_NAME = "kfr_blockout_v002_staged"
STAGE_NAME = "stage_02_legs_pelvis_tail"


def set_units():
    scene = bpy.context.scene
    scene.unit_settings.system = "METRIC"
    scene.unit_settings.scale_length = 0.001
    scene.unit_settings.length_unit = "MILLIMETERS"


def get_or_create_collection(name, parent=None):
    existing = bpy.data.collections.get(name)
    if existing:
        return existing
    col = bpy.data.collections.new(name)
    if parent:
        parent.children.link(col)
    else:
        bpy.context.scene.collection.children.link(col)
    return col


def make_mat(name, rgba):
    existing = bpy.data.materials.get(name)
    if existing:
        return existing
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = rgba
    return mat


def raw_cube(name, loc, dims, mat, col):
    x, y, z = loc
    dx, dy, dz = dims[0] / 2, dims[1] / 2, dims[2] / 2
    verts = [
        (x - dx, y - dy, z - dz),
        (x + dx, y - dy, z - dz),
        (x + dx, y + dy, z - dz),
        (x - dx, y + dy, z - dz),
        (x - dx, y - dy, z + dz),
        (x + dx, y - dy, z + dz),
        (x + dx, y + dy, z + dz),
        (x - dx, y + dy, z + dz),
    ]
    faces = [
        (0, 1, 2, 3),
        (4, 7, 6, 5),
        (0, 4, 5, 1),
        (1, 5, 6, 2),
        (2, 6, 7, 3),
        (3, 7, 4, 0),
    ]
    mesh = bpy.data.meshes.new(name + "_mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.data.materials.append(mat)
    col.objects.link(obj)
    return obj


def build_stage_02():
    print("KFR v002 Stage 02 starting")
    set_units()

    root = get_or_create_collection(ROOT_NAME)
    stage = get_or_create_collection(STAGE_NAME, root)

    mat_body = make_mat("kfr_stage_body_gray", (0.48, 0.50, 0.50, 1.0))
    mat_cloth = make_mat("kfr_stage_cloth_gray", (0.30, 0.31, 0.31, 1.0))
    mat_dark = make_mat("kfr_stage_dark_gray", (0.08, 0.08, 0.08, 1.0))
    mat_joint = make_mat("kfr_stage_joint_blue", (0.10, 0.30, 0.90, 0.75))

    # Legs / pants, blocky but positioned to connect with Stage 01 boots.
    raw_cube("kfr_part_009_leg_left_pants_blockout_lower_leg_stage02", (8, 0, 20), (9, 10, 24), mat_cloth, stage)
    raw_cube("kfr_part_010_leg_right_pants_blockout_lower_leg_stage02", (-8, 0, 20), (9, 10, 24), mat_cloth, stage)
    raw_cube("kfr_part_009_leg_left_pants_blockout_upper_leg_stage02", (8, 0.5, 42), (10, 11, 24), mat_cloth, stage)
    raw_cube("kfr_part_010_leg_right_pants_blockout_upper_leg_stage02", (-8, 0.5, 42), (10, 11, 24), mat_cloth, stage)

    # Reinforcement panels and pocket clearance masses.
    raw_cube("kfr_left_thigh_reinforcement_panel_stage02", (8, -5.6, 42), (9, 1.2, 12), mat_dark, stage)
    raw_cube("kfr_right_thigh_reinforcement_panel_stage02", (-8, -5.6, 42), (9, 1.2, 12), mat_dark, stage)
    raw_cube("kfr_left_knee_reinforcement_panel_stage02", (8, -5.6, 28), (9, 1.2, 8), mat_dark, stage)
    raw_cube("kfr_right_knee_reinforcement_panel_stage02", (-8, -5.6, 28), (9, 1.2, 8), mat_dark, stage)
    raw_cube("kfr_left_cargo_pocket_hip_clearance_mass_stage02", (14.3, -1.5, 40), (2.4, 7, 10), mat_dark, stage)
    raw_cube("kfr_right_utility_pocket_hip_clearance_mass_stage02", (-14.3, -1.5, 38), (2.4, 5, 8), mat_dark, stage)

    # Pelvis, waistband, and hip placeholders.
    raw_cube("kfr_part_004_pelvis_hip_tail_socket_blockout_stage02", (0, 2, 55), (30, 18, 15), mat_body, stage)
    raw_cube("kfr_pants_waistband_seam_blockout_stage02", (0, -1, 62), (32, 16, 4), mat_cloth, stage)
    raw_cube("kfr_joint_left_hip_placeholder_stage02", (8, 1, 56), (7, 7, 7), mat_joint, stage)
    raw_cube("kfr_joint_right_hip_placeholder_stage02", (-8, 1, 56), (7, 7, 7), mat_joint, stage)

    # Keyed tail socket and stepped tail path.
    raw_cube("kfr_tail_keyed_socket_blockout_in_pelvis_stage02", (0, 12, 56), (13, 5, 9), mat_joint, stage)
    raw_cube("kfr_part_011_tail_keyed_blockout_base_stage02", (0, 18, 53), (12, 13, 8), mat_body, stage)
    raw_cube("kfr_part_011_tail_keyed_blockout_mid_01_stage02", (0, 31, 46), (10, 15, 7), mat_body, stage)
    raw_cube("kfr_part_011_tail_keyed_blockout_mid_02_stage02", (0, 45, 34), (8, 15, 6), mat_body, stage)
    raw_cube("kfr_part_011_tail_keyed_blockout_mid_03_stage02", (0, 58, 20), (6, 13, 5), mat_body, stage)
    raw_cube("kfr_part_011_tail_keyed_blockout_blunt_tip_stage02", (0, 68, 9), (5, 8, 4), mat_body, stage)

    print("KFR v002 Stage 02 complete: legs, pelvis, hip placeholders, tail socket, and blocky tail path created.")
    print("Save now as kfr_blockout_v002_stage_02_pass.blend before continuing.")


if __name__ == "__main__":
    build_stage_02()
