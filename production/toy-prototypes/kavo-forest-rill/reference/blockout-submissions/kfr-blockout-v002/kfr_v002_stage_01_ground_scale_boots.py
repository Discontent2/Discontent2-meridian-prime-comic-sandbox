"""
KFR-BLOCKOUT-v002 Stage 01: Ground / Scale / Boots

Run this after the smoke test passes.

This stage creates only:
    - millimeter unit setup
    - one root collection
    - ground plane
    - 127 mm height guide
    - left/right boot blocks
    - four toe placeholders per boot

Safety choices:
    - raw mesh cubes only
    - no bpy.ops primitive mesh creation
    - no cameras
    - no lights
    - no modifiers
    - no scene reset

If this crashes Blender, stop and report that Stage 01 crashed.
If this succeeds, save the file before running Stage 02.
"""

import bpy

ROOT_NAME = "kfr_blockout_v002_staged"
STAGE_NAME = "stage_01_ground_scale_boots"


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


def build_stage_01():
    print("KFR v002 Stage 01 starting")
    set_units()

    root = get_or_create_collection(ROOT_NAME)
    stage = get_or_create_collection(STAGE_NAME, root)

    mat_ground = make_mat("kfr_stage_ground_light_gray", (0.70, 0.70, 0.70, 1.0))
    mat_guide = make_mat("kfr_stage_scale_guide_green", (0.10, 0.70, 0.35, 1.0))
    mat_dark = make_mat("kfr_stage_boot_dark_gray", (0.08, 0.08, 0.08, 1.0))
    mat_body = make_mat("kfr_stage_body_gray", (0.48, 0.50, 0.50, 1.0))

    raw_cube("kfr_stage_01_ground_plane_180mm", (0, 0, -0.5), (180, 180, 1), mat_ground, stage)
    raw_cube("kfr_stage_01_scale_127mm_height_guide", (-55, -45, 63.5), (2, 2, 127), mat_guide, stage)

    # Boots. Negative Y is front.
    raw_cube("kfr_part_009_leg_left_pants_boot_blockout_boot_base_stage01", (8, -2, 4), (15, 25, 8), mat_dark, stage)
    raw_cube("kfr_part_010_leg_right_pants_boot_blockout_boot_base_stage01", (-8, -2, 4), (15, 25, 8), mat_dark, stage)

    # Four toe placeholders per boot.
    for side, x_base in [("left", 8), ("right", -8)]:
        for i, dx in enumerate([-4.5, -1.5, 1.5, 4.5], start=1):
            raw_cube(
                f"kfr_stage_01_{side}_boot_toe_placeholder_{i}",
                (x_base + dx, -15, 5),
                (2.4, 4.0, 2.0),
                mat_body,
                stage,
            )

    print("KFR v002 Stage 01 complete: ground, scale guide, boots, and toe placeholders created.")
    print("Save now as kfr_blockout_v002_stage_01_pass.blend before continuing.")


if __name__ == "__main__":
    build_stage_01()
