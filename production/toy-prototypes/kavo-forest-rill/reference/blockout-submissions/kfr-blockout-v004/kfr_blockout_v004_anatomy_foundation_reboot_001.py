"""
KFR-BLOCKOUT-v004 Anatomy Foundation Reboot 001

Purpose
-------
Start from a clean anatomy foundation using everything learned from v001-v003.
This script aims for the Kavo "Forest" Rill turnaround/head-sheet target:

- original Velocisapien / velociraptoroid action figure anatomy
- 5-inch / 127 mm figure scale
- natural forward-lean creature stance
- long balancing tail
- strong raptor-like snout and brow ridge
- thick sculpt-friendly neck with articulation clearance
- four-fingered hands: three fingers + one thumb
- four-toed feet with large claws
- red proto-quill mohawk from head down spine/tail
- sunglasses/shades retained as a canon marker
- no final clothing yet, only anatomy and articulation landmarks

This is a fresh foundation, not an overlay guide. It hides earlier KFR blockout
collections/objects by default, then creates a single clean v004 collection.

Run in Blender, then save as:
    kfr_blockout_v004_anatomy_foundation_reboot_001.blend
"""

import math
import bpy
from mathutils import Vector

ROOT_COLLECTION_NAME = "KFR_BLOCKOUT_V004_ANATOMY_FOUNDATION_REBOOT_001"
TEXT_BLOCK_NAME = "KFR_V004_ANATOMY_FOUNDATION_REBOOT_001_NOTES"

# -----------------------------------------------------------------------------
# Scene control
# -----------------------------------------------------------------------------

HIDE_EXISTING_KFR = True
DELETE_EXISTING_V004 = True
SET_UNITS_TO_MM = True
ADD_HEIGHT_AND_STANCE_GUIDES = True

KFR_NAME_FRAGMENTS_TO_HIDE = [
    "kfr_",
    "KFR_",
    "KFR-BLOCKOUT",
    "kfr-blockout",
]

# Coordinate convention:
# X = character left/right. Positive X = character left.
# Y = front/back. Negative Y = character front. Positive Y = tail/back.
# Z = up.
# Target figure height: ~127 mm / 5 in.

# -----------------------------------------------------------------------------
# Materials
# -----------------------------------------------------------------------------

MAT_SKIN = (0.48, 0.55, 0.34, 1.0)          # route-dust olive reptile skin
MAT_BELLY = (0.62, 0.58, 0.39, 1.0)         # lighter throat / belly plates
MAT_DARK_SCALE = (0.18, 0.30, 0.28, 1.0)    # teal-dark scale spots
MAT_QUILL = (0.70, 0.22, 0.10, 1.0)         # red proto-quill material
MAT_CLAW = (0.06, 0.055, 0.045, 1.0)        # dark claws
MAT_SHADE = (0.015, 0.015, 0.012, 1.0)      # black shades
MAT_SHADE_LENS = (0.01, 0.012, 0.012, 0.82)
MAT_JOINT = (0.20, 0.22, 0.21, 1.0)         # neutral articulation markers
MAT_GUIDE = (0.10, 0.45, 0.95, 0.45)        # transparent blue guides
MAT_FLOOR = (0.75, 0.75, 0.72, 0.18)

# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------


def log(msg):
    print(f"[KFR V004 FOUNDATION] {msg}")


def rad(degrees):
    return math.radians(degrees)


def side_name(side):
    return "left" if side > 0 else "right"


def sx(x, side):
    return x * side


def has_fragment(name, fragments):
    low = name.lower()
    return any(f.lower() in low for f in fragments)


def hide_existing_kfr():
    hidden_collections = []
    hidden_objects = []
    if not HIDE_EXISTING_KFR:
        return hidden_collections, hidden_objects

    for col in bpy.data.collections:
        if col.name == ROOT_COLLECTION_NAME:
            continue
        if has_fragment(col.name, KFR_NAME_FRAGMENTS_TO_HIDE):
            col.hide_viewport = True
            col.hide_render = True
            hidden_collections.append(col.name)

    for obj in bpy.data.objects:
        if has_fragment(obj.name, KFR_NAME_FRAGMENTS_TO_HIDE):
            obj.hide_viewport = True
            obj.hide_render = True
            hidden_objects.append(obj.name)

    return hidden_collections, hidden_objects


def make_collection(name):
    existing = bpy.data.collections.get(name)
    if existing and DELETE_EXISTING_V004:
        for obj in list(existing.objects):
            bpy.data.objects.remove(obj, do_unlink=True)
        return existing
    if existing:
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


def link_to_col(obj, col):
    try:
        col.objects.link(obj)
    except RuntimeError:
        pass
    unlink_except(obj, col)
    return obj


def make_material(name, rgba, roughness=0.78, metallic=0.0):
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
            mat.use_screen_refraction = True
    except Exception:
        pass
    return mat


def apply_mat(obj, mat):
    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)
    return obj


def smooth(obj):
    try:
        for poly in obj.data.polygons:
            poly.use_smooth = True
    except Exception:
        pass
    return obj


def bevel(obj, width=0.2, segments=2):
    if width <= 0:
        return obj
    mod = obj.modifiers.new(name="v004_soft_bevel", type="BEVEL")
    mod.width = width
    mod.segments = segments
    mod.affect = "EDGES"
    try:
        obj.modifiers.new(name="v004_weighted_normals", type="WEIGHTED_NORMAL")
    except Exception:
        pass
    return obj


def finalize(obj, col, mat=None, do_smooth=False, bevel_width=None, bevel_segments=2):
    if mat:
        apply_mat(obj, mat)
    if do_smooth:
        smooth(obj)
    if bevel_width is not None and bevel_width > 0:
        bevel(obj, bevel_width, bevel_segments)
    link_to_col(obj, col)
    return obj


def add_empty(name, loc, col, size=0.8):
    bpy.ops.object.empty_add(type="PLAIN_AXES", location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.empty_display_size = size
    link_to_col(obj, col)
    return obj


def add_sphere(name, loc, dims, mat, col, rotation=(0, 0, 0), segments=32, rings=16):
    bpy.ops.mesh.primitive_uv_sphere_add(
        segments=segments,
        ring_count=rings,
        radius=1.0,
        location=loc,
        rotation=rotation,
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.scale = (dims[0] / 2.0, dims[1] / 2.0, dims[2] / 2.0)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    return finalize(obj, col, mat=mat, do_smooth=True)


def add_cube(name, loc, dims, mat, col, rotation=(0, 0, 0), bevel_width=0.2):
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=loc, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.dimensions = dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    return finalize(obj, col, mat=mat, bevel_width=bevel_width, bevel_segments=3)


def add_cylinder(name, loc, dims, mat, col, rotation=(0, 0, 0), vertices=24, bevel_width=0.1):
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=vertices,
        radius=1.0,
        depth=2.0,
        location=loc,
        rotation=rotation,
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.dimensions = dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    return finalize(obj, col, mat=mat, do_smooth=True, bevel_width=bevel_width, bevel_segments=2)


def add_cone(name, loc, dims, mat, col, rotation=(0, 0, 0), vertices=20, radius2=0.0, bevel_width=0.03):
    bpy.ops.mesh.primitive_cone_add(
        vertices=vertices,
        radius1=1.0,
        radius2=radius2,
        depth=2.0,
        location=loc,
        rotation=rotation,
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.dimensions = dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    return finalize(obj, col, mat=mat, do_smooth=True, bevel_width=bevel_width, bevel_segments=1)


def cylinder_between(name, start, end, radius, mat, col, vertices=18, bevel_width=0.04):
    start_v = Vector(start)
    end_v = Vector(end)
    vec = end_v - start_v
    length = vec.length
    if length == 0:
        return None
    mid = start_v + vec * 0.5
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=length, location=mid)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    # Cylinder local Z axis points up by default; align it to vector.
    quat = vec.to_track_quat("Z", "Y")
    obj.rotation_euler = quat.to_euler()
    return finalize(obj, col, mat=mat, do_smooth=True, bevel_width=bevel_width, bevel_segments=1)


def cone_between(name, start, end, radius, mat, col, vertices=18):
    start_v = Vector(start)
    end_v = Vector(end)
    vec = end_v - start_v
    length = vec.length
    if length == 0:
        return None
    mid = start_v + vec * 0.5
    bpy.ops.mesh.primitive_cone_add(vertices=vertices, radius1=radius, radius2=0.0, depth=length, location=mid)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    quat = vec.to_track_quat("Z", "Y")
    obj.rotation_euler = quat.to_euler()
    return finalize(obj, col, mat=mat, do_smooth=True, bevel_width=0.02, bevel_segments=1)


def parent_all(parent, children):
    for obj in children:
        if obj:
            obj.parent = parent

# -----------------------------------------------------------------------------
# Notes / setup
# -----------------------------------------------------------------------------


def setup_scene():
    if SET_UNITS_TO_MM:
        bpy.context.scene.unit_settings.system = "METRIC"
        bpy.context.scene.unit_settings.scale_length = 0.001
        bpy.context.scene.unit_settings.length_unit = "MILLIMETERS"


def create_notes():
    text = bpy.data.texts.get(TEXT_BLOCK_NAME)
    if text is None:
        text = bpy.data.texts.new(TEXT_BLOCK_NAME)
    text.clear()
    text.write(
        "KFR-BLOCKOUT-v004 Anatomy Foundation Reboot 001\n"
        "==============================================\n\n"
        "This is the clean start-from-scratch anatomy foundation.\n"
        "Earlier v001-v003 layers are hidden by default.\n\n"
        "Focus of this pass:\n"
        "- Velocisapien / velociraptoroid anatomy\n"
        "- snout, brow, shades, thick neck, red proto-quills\n"
        "- natural forward lean, long counterbalance tail\n"
        "- four-fingered hands and four-toed feet\n"
        "- scale-bump placeholders for sculpt language\n"
        "- articulation landmark rings / balls\n\n"
        "Not included yet:\n"
        "- route harness final design\n"
        "- pouches / badges\n"
        "- checker trim\n"
        "- claw wraps / clothing wraps\n"
        "- final sculpted scale texture\n\n"
        "Suggested save-as:\n"
        "kfr_blockout_v004_anatomy_foundation_reboot_001.blend\n"
    )

# -----------------------------------------------------------------------------
# Build: guides
# -----------------------------------------------------------------------------


def build_guides(col, mats):
    created = []
    if not ADD_HEIGHT_AND_STANCE_GUIDES:
        return created
    created.append(add_cube(
        "kfr_v004_floor_180mm_square_reference",
        loc=(0, 0, -1.0),
        dims=(180, 180, 0.8),
        mat=mats["floor"],
        col=col,
        bevel_width=0.0,
    ))
    created[-1].display_type = "WIRE"
    created.append(add_cylinder(
        "kfr_v004_127mm_height_guide_5inch",
        loc=(-38, -33, 63.5),
        dims=(1.5, 1.5, 127),
        mat=mats["guide"],
        col=col,
        vertices=12,
        bevel_width=0.0,
    ))
    created[-1].display_type = "WIRE"
    created.append(add_cube(
        "kfr_v004_stance_width_47mm_guide",
        loc=(0, -35, 0.6),
        dims=(47, 2, 1.0),
        mat=mats["guide"],
        col=col,
        bevel_width=0.0,
    ))
    created[-1].display_type = "WIRE"
    return created

# -----------------------------------------------------------------------------
# Build: torso, neck, head
# -----------------------------------------------------------------------------


def build_torso(col, mats):
    c = []
    # Creature body underneath clothing. Rounded, not cube-stack.
    c.append(add_sphere("kfr_v004_pelvis_ball", (0, 0.6, 49.0), (22, 17, 17), mats["skin"], col, segments=32, rings=16))
    c.append(add_sphere("kfr_v004_belly_core", (0, -1.8, 63.0), (27, 20, 29), mats["belly"], col, segments=36, rings=18))
    c.append(add_sphere("kfr_v004_chest_ribcage", (0, -1.2, 78.0), (31, 21, 30), mats["skin"], col, segments=36, rings=18))
    c.append(add_sphere("kfr_v004_upper_back_hump", (0, 4.8, 82.0), (29, 16, 24), mats["skin"], col, segments=32, rings=16))

    # Front belly/throat plates, important for the reference read.
    for i, z in enumerate([54, 59, 64, 69, 74, 79], 1):
        width = 14 + i * 1.2 if i < 4 else 20 - (i - 4) * 2
        c.append(add_cube(
            f"kfr_v004_front_belly_plate_{i:02d}",
            loc=(0, -12.3, z),
            dims=(width, 1.0, 3.0),
            mat=mats["belly"],
            col=col,
            rotation=(rad(0), 0, 0),
            bevel_width=0.5,
        ))

    # Joint landmarks for toy engineering.
    c.append(add_cylinder("kfr_v004_waist_articulation_landmark", (0, 0, 55.5), (25, 25, 1.2), mats["joint"], col, rotation=(rad(90), 0, 0), vertices=32, bevel_width=0.04))
    c.append(add_cylinder("kfr_v004_neck_base_clearance_landmark", (0, 0.5, 91.0), (18, 18, 1.2), mats["joint"], col, rotation=(rad(90), 0, 0), vertices=32, bevel_width=0.04))

    return c


def build_neck_head(col, mats):
    c = []
    # Thick forward-sloping neck.
    neck_points = [
        (0, 1.0, 88.0),
        (0, -0.2, 94.0),
        (0, -2.0, 100.0),
        (0, -4.0, 105.0),
    ]
    neck_dims = [(18, 14, 10), (18, 14, 10), (17, 13, 9), (16, 12, 8)]
    for i, (p, d) in enumerate(zip(neck_points, neck_dims), 1):
        c.append(add_sphere(f"kfr_v004_sturdy_neck_segment_{i:02d}", p, d, mats["skin"], col, segments=32, rings=14))
    for i in range(len(neck_points) - 1):
        c.append(cylinder_between(f"kfr_v004_neck_blend_{i+1:02d}", neck_points[i], neck_points[i+1], 7.0 - i * 0.35, mats["skin"], col, vertices=24, bevel_width=0.06))

    # Head mass: raptor-like cranium plus long snout.
    c.append(add_sphere("kfr_v004_head_cranium", (0, -5.5, 109.0), (27, 22, 22), mats["skin"], col, segments=42, rings=20))
    c.append(add_sphere("kfr_v004_head_rear_cheek_mass", (0, -1.2, 106.5), (25, 18, 18), mats["skin"], col, segments=36, rings=16))
    c.append(add_sphere("kfr_v004_long_snout_upper_mass", (0, -21.5, 106.2), (18, 29, 10), mats["skin"], col, rotation=(rad(-2), 0, 0), segments=36, rings=16))
    c.append(add_sphere("kfr_v004_snout_tip_bulge", (0, -36.0, 106.0), (14, 10, 8), mats["skin"], col, segments=32, rings=14))
    c.append(add_sphere("kfr_v004_lower_jaw_mass", (0, -23.0, 101.2), (17, 27, 6.2), mats["belly"], col, segments=32, rings=12))

    # Brow ridge and cheek lines under shades.
    c.append(add_cube("kfr_v004_brow_ridge_left", (6.3, -25.8, 111.4), (10.5, 2.0, 3.0), mats["skin"], col, rotation=(0, 0, rad(-4)), bevel_width=0.35))
    c.append(add_cube("kfr_v004_brow_ridge_right", (-6.3, -25.8, 111.4), (10.5, 2.0, 3.0), mats["skin"], col, rotation=(0, 0, rad(4)), bevel_width=0.35))
    c.append(add_sphere("kfr_v004_left_cheek_pad", (8.8, -19.5, 102.5), (5.0, 13.0, 5.0), mats["skin"], col, rotation=(0, 0, rad(-10)), segments=24, rings=12))
    c.append(add_sphere("kfr_v004_right_cheek_pad", (-8.8, -19.5, 102.5), (5.0, 13.0, 5.0), mats["skin"], col, rotation=(0, 0, rad(10)), segments=24, rings=12))

    # Nostrils.
    c.append(add_cylinder("kfr_v004_left_nostril", (4.6, -39.4, 106.7), (2.7, 1.4, 1.4), mats["claw"], col, rotation=(rad(90), 0, 0), vertices=18, bevel_width=0.02))
    c.append(add_cylinder("kfr_v004_right_nostril", (-4.6, -39.4, 106.7), (2.7, 1.4, 1.4), mats["claw"], col, rotation=(rad(90), 0, 0), vertices=18, bevel_width=0.02))

    # Smile/mouth line as short cylinders following the snout.
    c.append(cylinder_between("kfr_v004_left_smile_line", (2.8, -34.0, 102.4), (12.2, -18.0, 102.0), 0.45, mats["claw"], col, vertices=10, bevel_width=0.01))
    c.append(cylinder_between("kfr_v004_right_smile_line", (-2.8, -34.0, 102.4), (-12.2, -18.0, 102.0), 0.45, mats["claw"], col, vertices=10, bevel_width=0.01))
    c.append(cylinder_between("kfr_v004_front_mouth_line", (-4.8, -34.5, 102.35), (4.8, -34.5, 102.35), 0.45, mats["claw"], col, vertices=10, bevel_width=0.01))

    # Shades/goggles: canon marker, sculpt-friendly thick frame.
    c.append(add_cube("kfr_v004_shades_left_lens", (7.3, -27.3, 110.5), (11.4, 1.2, 6.2), mats["lens"], col, rotation=(rad(1), 0, rad(-3)), bevel_width=0.35))
    c.append(add_cube("kfr_v004_shades_right_lens", (-7.3, -27.3, 110.5), (11.4, 1.2, 6.2), mats["lens"], col, rotation=(rad(1), 0, rad(3)), bevel_width=0.35))
    c.append(add_cube("kfr_v004_shades_bridge", (0, -27.4, 110.4), (3.8, 1.2, 2.4), mats["shade"], col, bevel_width=0.22))
    c.append(cylinder_between("kfr_v004_left_shades_arm", (12.6, -27.1, 110.7), (15.2, -11.5, 109.6), 0.75, mats["shade"], col, vertices=10, bevel_width=0.01))
    c.append(cylinder_between("kfr_v004_right_shades_arm", (-12.6, -27.1, 110.7), (-15.2, -11.5, 109.6), 0.75, mats["shade"], col, vertices=10, bevel_width=0.01))

    return c

# -----------------------------------------------------------------------------
# Build: quills and scales
# -----------------------------------------------------------------------------


def build_quills(col, mats):
    c = []
    # Red proto-quill mohawk: short, sturdy, sculpt/print friendly.
    quill_path = [
        (0, -20.0, 119.0, 2.4, 5.2),
        (0, -15.0, 120.4, 2.7, 6.0),
        (0, -9.5, 121.0, 3.0, 7.0),
        (0, -4.0, 120.0, 3.0, 7.6),
        (0, 1.0, 117.6, 2.8, 7.2),
        (0, 5.2, 113.8, 2.4, 6.2),
        (0, 8.2, 109.0, 2.1, 5.4),
        (0, 9.8, 103.5, 1.9, 4.8),
    ]
    for i, (x, y, z, radius, height) in enumerate(quill_path, 1):
        start = (x, y, z - height * 0.35)
        end = (x, y + 0.4, z + height * 0.65)
        c.append(cone_between(f"kfr_v004_head_proto_quill_{i:02d}", start, end, radius, mats["quill"], col, vertices=18))

    # Spine/tail red dorsal quills.
    spine_path = [
        (0, 8.5, 97.0, 1.8, 4.5),
        (0, 8.8, 89.5, 1.8, 4.3),
        (0, 8.5, 81.8, 1.7, 4.0),
        (0, 9.0, 73.5, 1.6, 3.8),
        (0, 10.5, 62.0, 1.5, 3.6),
        (0, 18.0, 52.0, 1.4, 3.4),
        (0, 29.5, 43.0, 1.2, 3.0),
        (0, 41.0, 32.0, 1.0, 2.7),
        (0, 52.0, 21.0, 0.8, 2.3),
    ]
    for i, (x, y, z, radius, height) in enumerate(spine_path, 1):
        c.append(cone_between(f"kfr_v004_spine_tail_proto_quill_{i:02d}", (x, y, z), (x, y + 0.2, z + height), radius, mats["quill"], col, vertices=14))

    return c


def build_scale_bumps(col, mats):
    c = []
    # Hand-placed major bumps so the toy reads reptilian before full sculpt.
    major_bumps = [
        # head crown / snout
        (-9, -22, 115), (-4, -23, 116), (4, -23, 116), (9, -22, 115),
        (-10, -12, 116), (-5, -8, 118), (5, -8, 118), (10, -12, 116),
        (-7, -34, 110), (7, -34, 110), (-4, -29, 113), (4, -29, 113),
        # neck / shoulders
        (-11, 3, 98), (11, 3, 98), (-13, 2, 91), (13, 2, 91),
        (-16, -2, 82), (16, -2, 82), (-12, 5, 76), (12, 5, 76),
        # arms / legs
        (-29, -2, 74), (29, -2, 74), (-30, -2, 58), (30, -2, 58),
        (-12, -3, 42), (12, -3, 42), (-11, -1, 24), (11, -1, 24),
        # tail
        (0, 18, 49), (0, 28, 43), (0, 37, 36), (0, 47, 27), (0, 56, 18),
    ]
    for i, (x, y, z) in enumerate(major_bumps, 1):
        size = 2.2 if z > 90 else 2.0
        c.append(add_sphere(f"kfr_v004_large_scale_bump_{i:02d}", (x, y, z), (size, size * 0.75, size * 0.45), mats["scale"], col, segments=12, rings=8))

    # Rows of smaller throat plates.
    for i, z in enumerate([88, 84, 80, 76, 72, 68, 64, 60], 1):
        width = max(7.0, 14.0 - abs(z - 74) * 0.25)
        c.append(add_cube(f"kfr_v004_throat_plate_{i:02d}", (0, -10.7, z), (width, 0.8, 1.4), mats["belly"], col, bevel_width=0.25))

    return c

# -----------------------------------------------------------------------------
# Build: limbs
# -----------------------------------------------------------------------------


def build_arm(col, mats, side):
    c = []
    label = side_name(side)

    shoulder = (sx(18.5, side), -1.0, 80.5)
    elbow = (sx(25.5, side), -2.5, 63.0)
    wrist = (sx(28.2, side), -5.2, 47.5)
    palm = (sx(29.2, side), -8.0, 42.0)

    c.append(add_sphere(f"kfr_v004_{label}_shoulder_ball", shoulder, (12, 12, 12), mats["skin"], col, segments=32, rings=16))
    c.append(cylinder_between(f"kfr_v004_{label}_upper_arm_mass", shoulder, elbow, 4.7, mats["skin"], col, vertices=24, bevel_width=0.08))
    c.append(add_sphere(f"kfr_v004_{label}_elbow_joint_landmark", elbow, (8.4, 8.4, 8.4), mats["joint"], col, segments=24, rings=12))
    c.append(cylinder_between(f"kfr_v004_{label}_forearm_mass", elbow, wrist, 4.2, mats["skin"], col, vertices=24, bevel_width=0.08))
    c.append(add_sphere(f"kfr_v004_{label}_wrist_joint_landmark", wrist, (6.4, 6.4, 6.4), mats["joint"], col, segments=20, rings=10))

    # Hand palm with long raptor fingers, but toy-thick enough.
    c.append(add_sphere(f"kfr_v004_{label}_palm_mass", palm, (11, 8, 7), mats["skin"], col, rotation=(0, rad(12 * side), rad(8 * side)), segments=28, rings=14))

    # Three fingers plus thumb.
    finger_offsets = [(-3.5, 0.0, 0.0), (0.0, -0.2, 0.4), (3.4, 0.0, -0.1)]
    for i, (ox, oy, oz) in enumerate(finger_offsets, 1):
        base = (sx(29.0 + ox, side), -11.0 + oy, 42.4 + oz)
        mid = (sx(29.0 + ox * 1.05, side), -14.8 + oy, 39.4 + oz)
        tip = (sx(29.0 + ox * 1.12, side), -17.2 + oy, 36.8 + oz)
        c.append(cylinder_between(f"kfr_v004_{label}_finger_{i}_base", base, mid, 1.45, mats["skin"], col, vertices=16, bevel_width=0.03))
        c.append(cylinder_between(f"kfr_v004_{label}_finger_{i}_tip", mid, tip, 1.25, mats["skin"], col, vertices=16, bevel_width=0.03))
        c.append(cone_between(f"kfr_v004_{label}_finger_{i}_claw", tip, (tip[0], tip[1] - 3.0, tip[2] - 1.5), 1.0, mats["claw"], col, vertices=12))

    thumb_base = (sx(24.5, side), -9.5, 42.0)
    thumb_mid = (sx(22.0, side), -12.8, 39.0)
    thumb_tip = (sx(20.6, side), -15.5, 36.4)
    c.append(cylinder_between(f"kfr_v004_{label}_thumb_base", thumb_base, thumb_mid, 1.55, mats["skin"], col, vertices=16, bevel_width=0.03))
    c.append(cylinder_between(f"kfr_v004_{label}_thumb_tip", thumb_mid, thumb_tip, 1.32, mats["skin"], col, vertices=16, bevel_width=0.03))
    c.append(cone_between(f"kfr_v004_{label}_thumb_claw", thumb_tip, (thumb_tip[0] - 1.1 * side, thumb_tip[1] - 2.2, thumb_tip[2] - 1.1), 0.95, mats["claw"], col, vertices=12))

    return c


def build_leg_and_foot(col, mats, side):
    c = []
    label = side_name(side)

    hip = (sx(9.5, side), -0.2, 51.0)
    knee = (sx(11.8, side), -4.8, 33.5)
    ankle = (sx(11.0, side), -5.8, 16.5)
    foot_root = (sx(10.8, side), -10.0, 7.8)

    c.append(add_sphere(f"kfr_v004_{label}_hip_joint_landmark", hip, (9.5, 9.5, 9.5), mats["joint"], col, segments=24, rings=12))
    c.append(cylinder_between(f"kfr_v004_{label}_thigh_mass", hip, knee, 5.3, mats["skin"], col, vertices=24, bevel_width=0.08))
    c.append(add_sphere(f"kfr_v004_{label}_knee_joint_landmark", knee, (9.2, 8.8, 8.5), mats["joint"], col, segments=24, rings=12))
    c.append(cylinder_between(f"kfr_v004_{label}_lower_leg_mass", knee, ankle, 4.5, mats["skin"], col, vertices=24, bevel_width=0.08))
    c.append(add_sphere(f"kfr_v004_{label}_ankle_joint_landmark", ankle, (7.2, 7.2, 6.4), mats["joint"], col, segments=20, rings=10))

    c.append(add_sphere(f"kfr_v004_{label}_wide_raptor_foot_mass", foot_root, (13.5, 18.0, 6.8), mats["skin"], col, rotation=(rad(0), 0, rad(0)), segments=32, rings=14))

    # Four toes: three front + one inner rear/side toe.
    toe_specs = [
        ("inner", -4.8, -18.0, 7.2, 1.35),
        ("middle", 0.0, -20.5, 7.5, 1.50),
        ("outer", 4.8, -17.7, 7.2, 1.25),
        ("rear_inner", -7.0, -7.8, 6.2, 1.05),
    ]
    for name, ox, y, z, scale in toe_specs:
        base = (sx(10.8 + ox, side), -10.5, z)
        mid = (sx(10.8 + ox * 1.04, side), y, z - 0.4)
        tip = (sx(10.8 + ox * 1.06, side), y - 4.0 * scale, z - 0.8)
        c.append(cylinder_between(f"kfr_v004_{label}_toe_{name}_mass", base, mid, 1.55 * scale, mats["skin"], col, vertices=16, bevel_width=0.03))
        c.append(cone_between(f"kfr_v004_{label}_toe_{name}_claw", mid, tip, 1.15 * scale, mats["claw"], col, vertices=14))

    return c

# -----------------------------------------------------------------------------
# Build: tail
# -----------------------------------------------------------------------------


def build_tail(col, mats):
    c = []
    # Tail curves back and down for dynamic balance, with segment taper.
    points = [
        (0.0, 9.5, 51.0),
        (0.0, 20.0, 47.5),
        (0.0, 31.0, 41.0),
        (0.0, 42.0, 32.5),
        (0.0, 52.0, 23.5),
        (0.0, 60.0, 15.5),
        (0.0, 67.0, 9.5),
    ]
    radii = [7.5, 6.8, 6.0, 5.0, 4.0, 3.0]
    for i in range(len(points) - 1):
        c.append(cylinder_between(f"kfr_v004_tail_segment_{i+1:02d}", points[i], points[i+1], radii[i], mats["skin"], col, vertices=28, bevel_width=0.08))
        c.append(add_sphere(f"kfr_v004_tail_joint_landmark_{i+1:02d}", points[i+1], (radii[i] * 1.75, radii[i] * 1.75, radii[i] * 1.75), mats["joint"], col, segments=20, rings=10))
    c.append(add_sphere("kfr_v004_tail_root_socket_landmark", points[0], (17, 14, 13), mats["joint"], col, segments=24, rings=12))
    c.append(add_sphere("kfr_v004_tail_tip_taper", points[-1], (5.5, 4.0, 3.0), mats["skin"], col, segments=16, rings=8))
    return c

# -----------------------------------------------------------------------------
# Build: future clothing markers only
# -----------------------------------------------------------------------------


def build_future_clothing_markers(col, mats):
    c = []
    # Tiny hidden-by-default landmarks so future clothing pass has anchors.
    c.append(add_cube("kfr_v004_FUTURE_harness_anchor_crossbody_A", (0, -13.8, 79.0), (28, 0.8, 1.4), mats["guide"], col, rotation=(0, 0, rad(-18)), bevel_width=0.05))
    c.append(add_cube("kfr_v004_FUTURE_harness_anchor_crossbody_B", (0, -13.9, 75.0), (28, 0.8, 1.4), mats["guide"], col, rotation=(0, 0, rad(18)), bevel_width=0.05))
    c.append(add_cube("kfr_v004_FUTURE_belt_anchor", (0, -12.0, 57.0), (26, 0.8, 1.2), mats["guide"], col, bevel_width=0.05))
    for obj in c:
        obj.hide_viewport = True
        obj.hide_render = True
    return c

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------


def main():
    log("Starting clean anatomy foundation reboot.")
    setup_scene()
    hidden_cols, hidden_objs = hide_existing_kfr()
    col = make_collection(ROOT_COLLECTION_NAME)

    mats = {
        "skin": make_material("KFR_V004_route_dust_olive_skin", MAT_SKIN, roughness=0.86),
        "belly": make_material("KFR_V004_light_belly_throat_plates", MAT_BELLY, roughness=0.84),
        "scale": make_material("KFR_V004_dark_teal_scale_spots", MAT_DARK_SCALE, roughness=0.82),
        "quill": make_material("KFR_V004_red_proto_quills", MAT_QUILL, roughness=0.72),
        "claw": make_material("KFR_V004_dark_claws", MAT_CLAW, roughness=0.42),
        "shade": make_material("KFR_V004_shades_frame_black", MAT_SHADE, roughness=0.40),
        "lens": make_material("KFR_V004_smoky_shades_lens", MAT_SHADE_LENS, roughness=0.25),
        "joint": make_material("KFR_V004_neutral_joint_landmarks", MAT_JOINT, roughness=0.70),
        "guide": make_material("KFR_V004_future_clothing_blue_guides", MAT_GUIDE, roughness=0.5),
        "floor": make_material("KFR_V004_floor_reference_translucent", MAT_FLOOR, roughness=0.5),
    }

    root = add_empty("kfr_v004_anatomy_foundation_root", (0, 0, 0), col, size=1.2)
    created = []
    created.extend(build_guides(col, mats))
    created.extend(build_torso(col, mats))
    created.extend(build_neck_head(col, mats))
    created.extend(build_quills(col, mats))
    created.extend(build_scale_bumps(col, mats))
    for side in (1, -1):
        created.extend(build_arm(col, mats, side))
        created.extend(build_leg_and_foot(col, mats, side))
    created.extend(build_tail(col, mats))
    created.extend(build_future_clothing_markers(col, mats))

    parent_all(root, created)
    create_notes()

    log(f"Hidden old KFR collections: {len(hidden_cols)}")
    log(f"Hidden old KFR objects: {len(hidden_objs)}")
    log(f"Created v004 foundation objects: {len(created)}")
    log("Save as: kfr_blockout_v004_anatomy_foundation_reboot_001.blend")
    log("Review angles: front, left side, rear, three-quarter, head close-up, hand/foot close-up, tail side view.")


if __name__ == "__main__":
    main()
