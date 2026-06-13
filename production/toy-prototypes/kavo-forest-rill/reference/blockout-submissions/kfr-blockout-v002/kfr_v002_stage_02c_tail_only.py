"""
KFR-BLOCKOUT-v002 Stage 02C: Tail Only

Run this after Stage 02A and 02B pass and you save the file.

Creates:
    - blocky balance-tail path
    - blunt tail tip

No scene reset. No cameras. No lights. Raw mesh cubes only.
"""

import bpy

ROOT_NAME = "kfr_blockout_v002_staged"
STAGE_NAME = "stage_02c_tail_only"


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


def build_stage_02c():
    print("KFR v002 Stage 02C tail-only starting")
    set_units()
    root = get_or_create_collection(ROOT_NAME)
    stage = get_or_create_collection(STAGE_NAME, root)

    mat_body = make_mat("kfr_stage_body_gray", (0.48, 0.50, 0.50, 1.0))

    raw_cube("kfr_part_011_tail_keyed_blockout_base_stage02c", (0, 18, 53), (12, 13, 8), mat_body, stage)
    raw_cube("kfr_part_011_tail_keyed_blockout_mid_01_stage02c", (0, 31, 46), (10, 15, 7), mat_body, stage)
    raw_cube("kfr_part_011_tail_keyed_blockout_mid_02_stage02c", (0, 45, 34), (8, 15, 6), mat_body, stage)
    raw_cube("kfr_part_011_tail_keyed_blockout_mid_03_stage02c", (0, 58, 20), (6, 13, 5), mat_body, stage)
    raw_cube("kfr_part_011_tail_keyed_blockout_blunt_tip_stage02c", (0, 68, 9), (5, 8, 4), mat_body, stage)

    print("KFR v002 Stage 02C complete. Save as kfr_blockout_v002_stage_02c_pass.blend")


if __name__ == "__main__":
    build_stage_02c()
