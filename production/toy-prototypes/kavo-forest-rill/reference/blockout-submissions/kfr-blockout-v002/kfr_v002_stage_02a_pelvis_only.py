"""
KFR-BLOCKOUT-v002 Stage 02A: Pelvis Only

Run this on top of Stage 01 pass.
This is the smallest pelvis test after Stage 01.

Creates:
    - pelvis / hip / tail socket block
    - waistband seam block
    - left/right hip placeholders
    - tail socket placeholder

No scene reset. No cameras. No lights. Raw mesh cubes only.
"""

import bpy

ROOT_NAME = "kfr_blockout_v002_staged"
STAGE_NAME = "stage_02a_pelvis_only"


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


def build_stage_02a():
    print("KFR v002 Stage 02A pelvis-only starting")
    set_units()
    root = get_or_create_collection(ROOT_NAME)
    stage = get_or_create_collection(STAGE_NAME, root)

    mat_body = make_mat("kfr_stage_body_gray", (0.48, 0.50, 0.50, 1.0))
    mat_cloth = make_mat("kfr_stage_cloth_gray", (0.30, 0.31, 0.31, 1.0))
    mat_joint = make_mat("kfr_stage_joint_blue", (0.10, 0.30, 0.90, 0.75))

    raw_cube("kfr_part_004_pelvis_hip_tail_socket_blockout_stage02a", (0, 2, 55), (30, 18, 15), mat_body, stage)
    raw_cube("kfr_pants_waistband_seam_blockout_stage02a", (0, -1, 62), (32, 16, 4), mat_cloth, stage)
    raw_cube("kfr_joint_left_hip_placeholder_stage02a", (8, 1, 56), (7, 7, 7), mat_joint, stage)
    raw_cube("kfr_joint_right_hip_placeholder_stage02a", (-8, 1, 56), (7, 7, 7), mat_joint, stage)
    raw_cube("kfr_tail_keyed_socket_blockout_in_pelvis_stage02a", (0, 12, 56), (13, 5, 9), mat_joint, stage)

    print("KFR v002 Stage 02A complete. Save as kfr_blockout_v002_stage_02a_pass.blend")


if __name__ == "__main__":
    build_stage_02a()
