"""
KFR-BLOCKOUT-v002 Stage 02B: Legs / Pants Only

Run this after Stage 02A passes and you save the file.

Creates:
    - left/right lower and upper leg blocks
    - thigh and knee reinforcement panels
    - cargo / utility pocket clearance masses

No scene reset. No cameras. No lights. Raw mesh cubes only.
"""

import bpy

ROOT_NAME = "kfr_blockout_v002_staged"
STAGE_NAME = "stage_02b_legs_only"


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
        (x - dx, y - dy, z - dz), (x + dx, y - dy, z - dz),
        (x + dx, y + dy, z - dz), (x - dx, y + dy, z - dz),
        (x - dx, y - dy, z + dz), (x + dx, y - dy, z + dz),
        (x + dx, y + dy, z + dz), (x - dx, y + dy, z + dz),
    ]
    faces = [(0,1,2,3), (4,7,6,5), (0,4,5,1), (1,5,6,2), (2,6,7,3), (3,7,4,0)]
    mesh = bpy.data.meshes.new(name + "_mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    obj.data.materials.append(mat)
    col.objects.link(obj)
    return obj


def build_stage_02b():
    print("KFR v002 Stage 02B legs-only starting")
    set_units()
    root = get_or_create_collection(ROOT_NAME)
    stage = get_or_create_collection(STAGE_NAME, root)

    mat_cloth = make_mat("kfr_stage_cloth_gray", (0.30, 0.31, 0.31, 1.0))
    mat_dark = make_mat("kfr_stage_dark_gray", (0.08, 0.08, 0.08, 1.0))

    raw_cube("kfr_part_009_leg_left_pants_blockout_lower_leg_stage02b", (8, 0, 20), (9, 10, 24), mat_cloth, stage)
    raw_cube("kfr_part_010_leg_right_pants_blockout_lower_leg_stage02b", (-8, 0, 20), (9, 10, 24), mat_cloth, stage)
    raw_cube("kfr_part_009_leg_left_pants_blockout_upper_leg_stage02b", (8, 0.5, 42), (10, 11, 24), mat_cloth, stage)
    raw_cube("kfr_part_010_leg_right_pants_blockout_upper_leg_stage02b", (-8, 0.5, 42), (10, 11, 24), mat_cloth, stage)

    raw_cube("kfr_left_thigh_reinforcement_panel_stage02b", (8, -5.6, 42), (9, 1.2, 12), mat_dark, stage)
    raw_cube("kfr_right_thigh_reinforcement_panel_stage02b", (-8, -5.6, 42), (9, 1.2, 12), mat_dark, stage)
    raw_cube("kfr_left_knee_reinforcement_panel_stage02b", (8, -5.6, 28), (9, 1.2, 8), mat_dark, stage)
    raw_cube("kfr_right_knee_reinforcement_panel_stage02b", (-8, -5.6, 28), (9, 1.2, 8), mat_dark, stage)
    raw_cube("kfr_left_cargo_pocket_hip_clearance_mass_stage02b", (14.3, -1.5, 40), (2.4, 7, 10), mat_dark, stage)
    raw_cube("kfr_right_utility_pocket_hip_clearance_mass_stage02b", (-14.3, -1.5, 38), (2.4, 5, 8), mat_dark, stage)

    print("KFR v002 Stage 02B complete. Save as kfr_blockout_v002_stage_02b_pass.blend")


if __name__ == "__main__":
    build_stage_02b()
