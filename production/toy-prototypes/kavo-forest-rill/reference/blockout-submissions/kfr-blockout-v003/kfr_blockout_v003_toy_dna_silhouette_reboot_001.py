"""
KFR-BLOCKOUT-v003 Toy-DNA Silhouette Reboot 001

Purpose
-------
Create a new non-destructive v003 blockout that uses the lessons from v002 but
pushes Kavo "Forest" Rill toward the childhood creature-toy DNA target:

- chunkier creature action-figure proportions
- larger head / stronger snout personality
- big expressive 3-finger + 1-thumb hands
- fingerless gloves with exposed reptilian fingers and claws
- simple bold cropped jacket / shirt / harness read
- squat stronger legs and oversized boots
- original-style long tail kept as the balance anchor
- watch retained on the left wrist
- toyetic bumpy skin placeholders and visible articulation landmarks

This is NOT a copy of the reference toy. It is an original Forest Rill reboot
that borrows the toy-language: chunky, readable, expressive, durable, and fun.

Run after / beside any v002 file. This creates a new collection and can hide the
older v002 pass collections if HIDE_OLD_V002_LAYERS is True.

Recommended save-as after running:
    kfr_blockout_v003_toy_dna_silhouette_reboot_001.blend
"""

import math
import bpy
from mathutils import Vector

ROOT_COLLECTION_NAME = "KFR_BLOCKOUT_V003_TOY_DNA_SILHOUETTE_REBOOT_001"
TEXT_BLOCK_NAME = "KFR_V003_TOY_DNA_REBOOT_001_NOTES"

# -----------------------------------------------------------------------------
# Scene options
# -----------------------------------------------------------------------------

HIDE_OLD_V002_LAYERS = True
OLD_LAYER_FRAGMENTS = [
    "kfr_blockout_v002",
    "kfr_v002",
    "kfr_v0025",
    "tail_balance_fix",
    "tail_fix_002",
    "garment_restore_001",
    "silhouette_boost_001",
    "jacket_sculpt_001",
    "jacket_sculpt_002",
    "arms_hands_gloves_001",
]

# Coordinate convention:
# X = character left/right. Positive X = character left.
# Y = front/back. Negative Y = character front.
# Z = up.
# Figure target height is roughly 127 mm / 5 in.

# -----------------------------------------------------------------------------
# Materials
# -----------------------------------------------------------------------------

MAT_SKIN = (0.55, 0.62, 0.38, 1.0)           # route-dust olive / reptile skin
MAT_SKIN_DARK = (0.24, 0.34, 0.28, 1.0)      # spots / scale bumps
MAT_BELLY = (0.66, 0.66, 0.48, 1.0)
MAT_QUILL = (0.78, 0.25, 0.10, 1.0)
MAT_JACKET = (0.34, 0.35, 0.32, 1.0)
MAT_SHIRT = (0.76, 0.70, 0.32, 1.0)
MAT_HARNESS = (0.055, 0.055, 0.055, 1.0)
MAT_GLOVE = (0.045, 0.045, 0.045, 1.0)
MAT_GLOVE_EDGE = (0.16, 0.16, 0.15, 1.0)
MAT_BOOT = (0.05, 0.05, 0.055, 1.0)
MAT_BOOT_SOLE = (0.16, 0.16, 0.16, 1.0)
MAT_CLAW = (0.11, 0.10, 0.09, 1.0)
MAT_WATCH = (0.05, 0.08, 0.09, 1.0)
MAT_WATCH_SCREEN = (0.10, 0.45, 0.95, 1.0)
MAT_EYEGLASS = (0.025, 0.025, 0.025, 1.0)
MAT_GUIDE = (0.10, 0.38, 0.95, 0.55)
MAT_SCALE_GUIDE = (0.20, 0.75, 0.45, 0.6)

# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------


def log(msg):
    print(f"[KFR V003 TOY DNA REBOOT] {msg}")


def has_fragment(name, fragments):
    low = name.lower()
    return any(fragment.lower() in low for fragment in fragments)


def hide_old_layers():
    hidden_objects = []
    hidden_collections = []
    if not HIDE_OLD_V002_LAYERS:
        return hidden_collections, hidden_objects

    for col in bpy.data.collections:
        if col.name == ROOT_COLLECTION_NAME:
            continue
        if has_fragment(col.name, OLD_LAYER_FRAGMENTS):
            col.hide_viewport = True
            col.hide_render = True
            hidden_collections.append(col.name)

    for obj in bpy.data.objects:
        if has_fragment(obj.name, OLD_LAYER_FRAGMENTS):
            obj.hide_viewport = True
            obj.hide_render = True
            hidden_objects.append(obj.name)

    return hidden_collections, hidden_objects


def make_collection(name):
    existing = bpy.data.collections.get(name)
    if existing:
        for obj in list(existing.objects):
            bpy.data.objects.remove(obj, do_unlink=True)
        return existing
    col = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(col)
    return col


def make_material(name, rgba, roughness=0.82, metallic=0.0):
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
    except Exception:
        pass
    return mat


def unlink_except(obj, keep_col):
    for col in list(obj.users_collection):
        if col != keep_col:
            try:
                col.objects.unlink(obj)
            except RuntimeError:
                pass


def link_obj(obj, col):
    try:
        col.objects.link(obj)
    except RuntimeError:
        pass
    unlink_except(obj, col)


def add_bevel(obj, amount=0.4, segments=3):
    if amount <= 0:
        return obj
    bevel = obj.modifiers.new(name="toy_soft_bevel", type="BEVEL")
    bevel.width = amount
    bevel.segments = segments
    bevel.affect = "EDGES"
    try:
        obj.modifiers.new(name="toy_weighted_normals", type="WEIGHTED_NORMAL")
    except Exception:
        pass
    return obj


def shade_smooth(obj):
    try:
        for poly in obj.data.polygons:
            poly.use_smooth = True
    except Exception:
        pass
    return obj


def add_cube(name, loc, dims, mat, col, rotation=(0.0, 0.0, 0.0), bevel=0.35):
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=loc, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.dimensions = dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    add_bevel(obj, bevel, 3)
    link_obj(obj, col)
    return obj


def add_ellipsoid(name, loc, dims, mat, col, rotation=(0.0, 0.0, 0.0), segments=32, rings=16):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segments, ring_count=rings, radius=1.0, location=loc, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.scale = (dims[0] / 2.0, dims[1] / 2.0, dims[2] / 2.0)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    shade_smooth(obj)
    link_obj(obj, col)
    return obj


def add_cylinder(name, loc, dims, mat, col, rotation=(0.0, 0.0, 0.0), vertices=32, bevel=0.25):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=1.0, depth=2.0, location=loc, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.dimensions = dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    shade_smooth(obj)
    add_bevel(obj, bevel, 3)
    link_obj(obj, col)
    return obj


def add_cone(name, loc, dims, mat, col, rotation=(0.0, 0.0, 0.0), vertices=24, bevel=0.0):
    bpy.ops.mesh.primitive_cone_add(vertices=vertices, radius1=1.0, radius2=0.0, depth=2.0, location=loc, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.dimensions = dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    shade_smooth(obj)
    if bevel:
        add_bevel(obj, bevel, 2)
    link_obj(obj, col)
    return obj


def add_scale_bump(name, loc, radius, mat, col, squash=0.38):
    return add_ellipsoid(name, loc, (radius, radius, radius * squash), mat, col, segments=16, rings=8)


def mloc(x, y, z, side=1):
    return (x * side, y, z)


def side_name(side):
    return "left" if side > 0 else "right"


def rad(deg):
    return math.radians(deg)

# -----------------------------------------------------------------------------
# Text notes
# -----------------------------------------------------------------------------


def create_notes():
    notes = """
KFR-BLOCKOUT-v003 TOY-DNA SILHOUETTE REBOOT 001

Intent:
    This is a v003 silhouette reboot, not a final sculpt. It keeps Forest's core
    identity but moves the figure toward a chunky creature-action-figure design.

Design language:
    - big expressive head and snout
    - toy shelf readability from across the room
    - chunky hands, feet, and boots
    - three fingers plus one thumb
    - fingerless gloves with exposed reptilian digits
    - simple bold jacket/shirt/harness shapes
    - long tail as a balance anchor
    - watch retained on the left wrist

What to review:
    1. Does the full-body silhouette feel more like a creature toy?
    2. Are the hands and boots bold enough?
    3. Is the jacket simple and readable?
    4. Does the head have enough character without final sculpt detail?
    5. Is the tail still useful as a balance/support element?

Do not judge yet:
    - exact face sculpt
    - final scale texture
    - final articulation engineering
    - final print splits
    - final paint colors

Suggested save-as:
    kfr_blockout_v003_toy_dna_silhouette_reboot_001.blend
""".strip()
    text = bpy.data.texts.get(TEXT_BLOCK_NAME)
    if text:
        text.clear()
    else:
        text = bpy.data.texts.new(TEXT_BLOCK_NAME)
    text.write(notes + "\n")
    return text.name

# -----------------------------------------------------------------------------
# Build systems
# -----------------------------------------------------------------------------


def build_scale_and_base(col, mats):
    created = []
    created.append(add_cube(
        "kfr_v003_scale_floor_180mm_square_reference",
        loc=(0, 0, -1.2),
        dims=(180, 180, 1.0),
        mat=mats["guide"],
        col=col,
        bevel=0.0,
    ))
    created[-1].display_type = "WIRE"
    created.append(add_cylinder(
        "kfr_v003_127mm_height_guide_5_inch",
        loc=(-50, 28, 63.5),
        dims=(1.8, 1.8, 127.0),
        mat=mats["scale"],
        col=col,
        vertices=16,
        bevel=0.0,
    ))
    return created


def build_body(col, mats):
    created = []

    # Squat creature core under clothing.
    created.append(add_ellipsoid(
        "kfr_v003_core_chunky_creature_torso_underbody",
        loc=(0, 0, 67.0),
        dims=(33.0, 22.0, 39.0),
        mat=mats["skin"],
        col=col,
    ))

    # Bold simple shirt/jacket language, toy-readable.
    created.append(add_ellipsoid(
        "kfr_v003_simple_bold_shirt_chest_plate",
        loc=(0, -9.3, 70.0),
        dims=(27.0, 5.0, 30.0),
        mat=mats["shirt"],
        col=col,
        rotation=(rad(2), 0, 0),
    ))
    created.append(add_cube(
        "kfr_v003_cropped_field_jacket_outer_shell",
        loc=(0, -0.5, 70.0),
        dims=(38.0, 17.0, 35.0),
        mat=mats["jacket"],
        col=col,
        bevel=2.2,
    ))
    created.append(add_cube(
        "kfr_v003_open_front_shirt_window",
        loc=(0, -10.6, 70.0),
        dims=(15.0, 1.2, 24.0),
        mat=mats["shirt"],
        col=col,
        bevel=0.9,
    ))
    created.append(add_cube(
        "kfr_v003_jacket_upper_collar_shelf",
        loc=(0, -0.5, 88.0),
        dims=(40.0, 18.0, 7.0),
        mat=mats["jacket"],
        col=col,
        bevel=1.5,
    ))
    created.append(add_cube(
        "kfr_v003_jacket_cropped_hem_bar",
        loc=(0, -8.9, 51.5),
        dims=(32.0, 2.0, 3.2),
        mat=mats["harness"],
        col=col,
        bevel=0.5,
    ))

    # Harness reduced to bold toy straps, not a cage.
    for x, label in [(-8.0, "right"), (8.0, "left")]:
        created.append(add_cube(
            f"kfr_v003_{label}_bold_vertical_harness_strap",
            loc=(x, -11.2, 69.0),
            dims=(2.5, 1.2, 29.0),
            mat=mats["harness"],
            col=col,
            bevel=0.35,
        ))
    created.append(add_cube(
        "kfr_v003_upper_chest_harness_bar_short",
        loc=(0, -11.4, 81.0),
        dims=(21.0, 1.2, 2.6),
        mat=mats["harness"],
        col=col,
        bevel=0.35,
    ))
    created.append(add_cube(
        "kfr_v003_waist_harness_belt",
        loc=(0, -11.1, 57.0),
        dims=(31.0, 1.2, 2.8),
        mat=mats["harness"],
        col=col,
        bevel=0.35,
    ))

    return created


def build_head(col, mats):
    created = []

    # Big toy creature head, slightly oversized.
    created.append(add_ellipsoid(
        "kfr_v003_big_toy_creature_head_cranium",
        loc=(0, -0.2, 103.0),
        dims=(35.0, 27.0, 29.0),
        mat=mats["skin"],
        col=col,
    ))

    # Strong snout, wider and friendlier than the v002 placeholder.
    created.append(add_ellipsoid(
        "kfr_v003_broad_forward_snout_mass",
        loc=(0, -19.2, 101.5),
        dims=(25.0, 25.0, 15.0),
        mat=mats["skin"],
        col=col,
        rotation=(rad(-4), 0, 0),
    ))
    created.append(add_ellipsoid(
        "kfr_v003_lower_jaw_grin_plate",
        loc=(0, -20.0, 94.4),
        dims=(23.0, 18.0, 6.0),
        mat=mats["belly"],
        col=col,
        rotation=(rad(-5), 0, 0),
    ))
    created.append(add_cube(
        "kfr_v003_simple_dark_smile_line",
        loc=(0, -31.0, 98.2),
        dims=(20.0, 0.7, 1.2),
        mat=mats["harness"],
        col=col,
        bevel=0.25,
    ))

    # Sunglasses retained, but bigger toy read.
    created.append(add_cube(
        "kfr_v003_left_shades_lens",
        loc=(7.3, -28.0, 106.2),
        dims=(10.5, 1.2, 5.8),
        mat=mats["eyeglass"],
        col=col,
        bevel=0.35,
    ))
    created.append(add_cube(
        "kfr_v003_right_shades_lens",
        loc=(-7.3, -28.0, 106.2),
        dims=(10.5, 1.2, 5.8),
        mat=mats["eyeglass"],
        col=col,
        bevel=0.35,
    ))
    created.append(add_cube(
        "kfr_v003_shades_bridge",
        loc=(0, -28.2, 106.1),
        dims=(3.5, 1.0, 2.0),
        mat=mats["eyeglass"],
        col=col,
        bevel=0.22,
    ))

    # Nostalgic creature-toy quills, bolder but still stout and print-minded.
    quill_specs = [
        (0, -3, 119.0, 3.2, 3.2, 10.0, 0),
        (4.0, -1.8, 117.3, 2.6, 2.6, 8.5, 7),
        (-4.0, -1.8, 117.3, 2.6, 2.6, 8.5, -7),
        (7.5, -0.4, 115.0, 2.2, 2.2, 7.2, 12),
        (-7.5, -0.4, 115.0, 2.2, 2.2, 7.2, -12),
    ]
    for idx, (x, y, z, dx, dy, dz, yaw) in enumerate(quill_specs, 1):
        created.append(add_cone(
            f"kfr_v003_stout_head_quill_{idx:02d}",
            loc=(x, y, z),
            dims=(dx, dy, dz),
            mat=mats["quill"],
            col=col,
            rotation=(rad(-8), rad(yaw), 0),
            vertices=20,
            bevel=0.08,
        ))

    # Neck thick enough for toy logic.
    created.append(add_ellipsoid(
        "kfr_v003_thick_creature_neck",
        loc=(0, 0.5, 88.4),
        dims=(18.0, 16.0, 17.0),
        mat=mats["skin"],
        col=col,
    ))

    return created


def build_arms_hands(col, mats, side):
    created = []
    name = side_name(side)

    # Shoulders and sleeve chain: chunky, not tube-man.
    created.append(add_ellipsoid(
        f"kfr_v003_{name}_round_shoulder_sleeve_cap",
        loc=mloc(23.0, -0.5, 82.0, side),
        dims=(14.0, 13.0, 15.0),
        mat=mats["sleeve"],
        col=col,
    ))
    created.append(add_ellipsoid(
        f"kfr_v003_{name}_chunky_upper_sleeve",
        loc=mloc(29.0, -1.5, 68.5, side),
        dims=(10.0, 10.0, 23.0),
        mat=mats["sleeve"],
        col=col,
        rotation=(rad(4), 0, rad(-12 * side)),
    ))
    created.append(add_cylinder(
        f"kfr_v003_{name}_visible_elbow_joint_band",
        loc=mloc(31.5, -1.9, 56.5, side),
        dims=(8.5, 8.5, 3.2),
        mat=mats["sleeve_shadow"],
        col=col,
        rotation=(rad(90), 0, rad(-12 * side)),
        bevel=0.18,
    ))
    created.append(add_ellipsoid(
        f"kfr_v003_{name}_forearm_sleeve_taper",
        loc=mloc(33.0, -3.8, 47.0, side),
        dims=(9.0, 9.0, 18.0),
        mat=mats["sleeve"],
        col=col,
        rotation=(rad(8), 0, rad(-10 * side)),
    ))
    created.append(add_cylinder(
        f"kfr_v003_{name}_black_glove_cuff_ring",
        loc=mloc(34.2, -5.2, 38.5, side),
        dims=(10.0, 9.0, 5.2),
        mat=mats["glove_edge"],
        col=col,
        rotation=(rad(90), 0, rad(-10 * side)),
        bevel=0.18,
    ))

    # Big palm / glove shell.
    created.append(add_ellipsoid(
        f"kfr_v003_{name}_oversized_fingerless_glove_palm",
        loc=mloc(34.0, -8.0, 32.8, side),
        dims=(12.0, 8.0, 9.0),
        mat=mats["glove"],
        col=col,
        rotation=(rad(12), 0, rad(-8 * side)),
    ))
    created.append(add_cube(
        f"kfr_v003_{name}_glove_knuckle_opening_band",
        loc=mloc(34.0, -8.9, 36.7, side),
        dims=(9.5, 3.0, 2.6),
        mat=mats["glove_edge"],
        col=col,
        rotation=(rad(8), 0, rad(-8 * side)),
        bevel=0.5,
    ))

    # 3 fingers, pushed big and readable.
    finger_xs = [30.7, 34.0, 37.3]
    finger_tags = ["inner", "middle", "outer"]
    for i, (fx, tag) in enumerate(zip(finger_xs, finger_tags)):
        length_bonus = 1.5 if tag == "middle" else 0.0
        created.append(add_ellipsoid(
            f"kfr_v003_{name}_{tag}_exposed_reptile_finger_base",
            loc=mloc(fx, -10.0, 36.0, side),
            dims=(3.2, 3.2, 6.2 + length_bonus),
            mat=mats["skin"],
            col=col,
            rotation=(rad(20), 0, rad((i - 1) * 4 * side)),
        ))
        created.append(add_ellipsoid(
            f"kfr_v003_{name}_{tag}_exposed_reptile_finger_tip",
            loc=mloc(fx, -11.2, 31.4 - length_bonus * 0.3, side),
            dims=(2.8, 2.8, 5.5 + length_bonus),
            mat=mats["skin"],
            col=col,
            rotation=(rad(28), 0, rad((i - 1) * 4 * side)),
        ))
        created.append(add_cone(
            f"kfr_v003_{name}_{tag}_toy_safe_claw",
            loc=mloc(fx, -12.4, 27.8 - length_bonus * 0.3, side),
            dims=(1.9, 1.9, 3.6),
            mat=mats["claw"],
            col=col,
            rotation=(rad(32), 0, rad((i - 1) * 4 * side)),
            bevel=0.05,
        ))

    # Thumb split: large, obvious, creature-toy readable.
    created.append(add_ellipsoid(
        f"kfr_v003_{name}_large_opposable_thumb_base",
        loc=mloc(40.0, -8.3, 32.5, side),
        dims=(4.5, 4.2, 7.0),
        mat=mats["skin"],
        col=col,
        rotation=(rad(38), rad(8 * side), rad(-38 * side)),
    ))
    created.append(add_ellipsoid(
        f"kfr_v003_{name}_large_opposable_thumb_tip",
        loc=mloc(42.3, -10.8, 28.7, side),
        dims=(3.6, 3.5, 5.6),
        mat=mats["skin"],
        col=col,
        rotation=(rad(45), rad(10 * side), rad(-44 * side)),
    ))
    created.append(add_cone(
        f"kfr_v003_{name}_thumb_claw",
        loc=mloc(44.2, -12.0, 25.3, side),
        dims=(2.0, 2.0, 3.4),
        mat=mats["claw"],
        col=col,
        rotation=(rad(48), rad(10 * side), rad(-44 * side)),
        bevel=0.05,
    ))

    # Left wrist watch on character left only.
    if side > 0:
        created.append(add_cube(
            "kfr_v003_left_wrist_route_reader_watch_body",
            loc=mloc(35.7, -9.4, 39.6, side),
            dims=(7.2, 2.2, 4.2),
            mat=mats["watch"],
            col=col,
            rotation=(rad(10), 0, rad(-10 * side)),
            bevel=0.35,
        ))
        created.append(add_cube(
            "kfr_v003_left_wrist_route_reader_watch_blue_screen",
            loc=mloc(35.7, -10.7, 39.6, side),
            dims=(4.8, 0.5, 2.4),
            mat=mats["watch_screen"],
            col=col,
            rotation=(rad(10), 0, rad(-10 * side)),
            bevel=0.12,
        ))

    return created


def build_legs_feet(col, mats, side):
    created = []
    name = side_name(side)

    # Squat sturdy toy legs.
    created.append(add_ellipsoid(
        f"kfr_v003_{name}_short_strong_thigh_pants",
        loc=mloc(10.5, -1.5, 38.5, side),
        dims=(13.0, 11.0, 22.0),
        mat=mats["jacket"],
        col=col,
        rotation=(rad(-3), 0, rad(5 * side)),
    ))
    created.append(add_cylinder(
        f"kfr_v003_{name}_round_knee_articulation_marker",
        loc=mloc(11.3, -6.0, 27.2, side),
        dims=(9.4, 4.0, 8.0),
        mat=mats["sleeve_shadow"],
        col=col,
        rotation=(rad(90), 0, 0),
        vertices=24,
        bevel=0.25,
    ))
    created.append(add_ellipsoid(
        f"kfr_v003_{name}_stocky_lower_leg_skin",
        loc=mloc(12.0, -1.2, 17.8, side),
        dims=(10.0, 9.0, 20.0),
        mat=mats["skin"],
        col=col,
        rotation=(rad(-3), 0, rad(3 * side)),
    ))

    # Big chunky boots, strong toy-foot read.
    created.append(add_cube(
        f"kfr_v003_{name}_oversized_boot_sole",
        loc=mloc(12.5, -4.0, 3.2, side),
        dims=(18.0, 27.0, 5.6),
        mat=mats["boot_sole"],
        col=col,
        bevel=1.0,
    ))
    created.append(add_cube(
        f"kfr_v003_{name}_oversized_boot_upper",
        loc=mloc(12.5, -3.5, 9.0, side),
        dims=(15.0, 21.0, 10.0),
        mat=mats["boot"],
        col=col,
        bevel=1.2,
    ))
    for toe_i, tx in enumerate([-4.2, 0.0, 4.2], 1):
        created.append(add_ellipsoid(
            f"kfr_v003_{name}_boot_toe_bump_{toe_i}",
            loc=mloc(12.5 + tx, -17.0, 9.2, side),
            dims=(4.0, 4.8, 3.2),
            mat=mats["quill"],
            col=col,
        ))

    return created


def build_tail(col, mats):
    created = []
    tail_specs = [
        (0, 14, 45, 20, 15, 13, -10),
        (0, 29, 39, 22, 13, 11, -18),
        (0, 45, 30, 21, 10, 8, -28),
        (0, 58, 19, 17, 7, 6, -35),
        (0, 67, 10, 10, 4, 4, -40),
    ]
    created.append(add_ellipsoid(
        "kfr_v003_tail_root_socket_muscle",
        loc=(0, 8, 47),
        dims=(18, 13, 12),
        mat=mats["skin"],
        col=col,
        rotation=(rad(-8), 0, 0),
    ))
    for i, (x, y, z, dy, dx, dz, pitch) in enumerate(tail_specs, 1):
        created.append(add_ellipsoid(
            f"kfr_v003_original_spirit_long_tail_segment_{i:02d}",
            loc=(x, y, z),
            dims=(dx, dy, dz),
            mat=mats["skin"],
            col=col,
            rotation=(rad(pitch), 0, 0),
        ))
        if i <= 4:
            created.append(add_cube(
                f"kfr_v003_tail_articulation_ring_hint_{i:02d}",
                loc=(x, y + dy * 0.42, z - 2.0),
                dims=(dx * 0.95, 1.3, dz * 0.85),
                mat=mats["skin_dark"],
                col=col,
                rotation=(rad(pitch), 0, 0),
                bevel=0.35,
            ))

    # A few dorsal plates echo head quills without turning the tail into a saw.
    plate_specs = [
        (0, 20, 54, 3.5, 2.5, 5.0),
        (0, 32, 47, 3.0, 2.2, 4.3),
        (0, 44, 38, 2.6, 2.0, 3.7),
    ]
    for i, (x, y, z, dx, dy, dz) in enumerate(plate_specs, 1):
        created.append(add_cone(
            f"kfr_v003_tail_dorsal_plate_{i:02d}",
            loc=(x, y, z),
            dims=(dx, dy, dz),
            mat=mats["quill"],
            col=col,
            rotation=(rad(-20), 0, rad(45)),
            vertices=4,
            bevel=0.05,
        ))

    return created


def build_skin_bumps(col, mats):
    created = []
    # Sparse, large readable scale-bump placeholders. Not final texture.
    bump_points = [
        (-10, -18, 108), (-4, -20, 111), (6, -19, 110), (12, -14, 105),
        (-13, -4, 100), (13, -2, 101), (-9, -11, 95), (9, -12, 95),
        (-29, -3, 69), (29, -3, 69), (-34, -7, 34), (34, -7, 34),
        (-13, -5, 23), (13, -5, 23), (0, 23, 43), (0, 37, 33),
    ]
    for i, (x, y, z) in enumerate(bump_points, 1):
        created.append(add_scale_bump(
            f"kfr_v003_large_toy_scale_bump_placeholder_{i:02d}",
            loc=(x, y, z),
            radius=3.0 if z > 90 else 2.4,
            mat=mats["skin_dark"],
            col=col,
            squash=0.32,
        ))
    return created


def build_all():
    hidden_cols, hidden_objs = hide_old_layers()
    col = make_collection(ROOT_COLLECTION_NAME)

    mats = {
        "skin": make_material("kfr_v003_skin_route_dust_olive", MAT_SKIN),
        "skin_dark": make_material("kfr_v003_skin_dark_scale_bumps", MAT_SKIN_DARK),
        "belly": make_material("kfr_v003_belly_jaw_light", MAT_BELLY),
        "quill": make_material("kfr_v003_quill_and_toe_accent", MAT_QUILL),
        "jacket": make_material("kfr_v003_cropped_jacket_gray", MAT_JACKET),
        "shirt": make_material("kfr_v003_bold_shirt_yellow", MAT_SHIRT),
        "harness": make_material("kfr_v003_harness_black", MAT_HARNESS),
        "sleeve": make_material("kfr_v003_jacket_sleeves", MAT_JACKET),
        "sleeve_shadow": make_material("kfr_v003_joint_band_gray", MAT_GLOVE_EDGE),
        "glove": make_material("kfr_v003_fingerless_glove_black", MAT_GLOVE),
        "glove_edge": make_material("kfr_v003_glove_edge", MAT_GLOVE_EDGE),
        "boot": make_material("kfr_v003_boot_black", MAT_BOOT),
        "boot_sole": make_material("kfr_v003_boot_sole", MAT_BOOT_SOLE),
        "claw": make_material("kfr_v003_dark_claws", MAT_CLAW),
        "watch": make_material("kfr_v003_route_reader_watch_body", MAT_WATCH),
        "watch_screen": make_material("kfr_v003_route_reader_blue_screen", MAT_WATCH_SCREEN),
        "eyeglass": make_material("kfr_v003_shades_black", MAT_EYEGLASS),
        "guide": make_material("kfr_v003_translucent_floor_guide", MAT_GUIDE),
        "scale": make_material("kfr_v003_green_height_guide", MAT_SCALE_GUIDE),
    }

    created = []
    created.extend(build_scale_and_base(col, mats))
    created.extend(build_body(col, mats))
    created.extend(build_head(col, mats))
    for side in [1, -1]:
        created.extend(build_arms_hands(col, mats, side))
        created.extend(build_legs_feet(col, mats, side))
    created.extend(build_tail(col, mats))
    created.extend(build_skin_bumps(col, mats))
    text_name = create_notes()

    log(f"Hidden old collections: {len(hidden_cols)}")
    for name in hidden_cols:
        log(f"  hidden collection: {name}")
    log(f"Hidden old objects: {len(hidden_objs)}")
    for name in hidden_objs[:80]:
        log(f"  hidden object: {name}")
    if len(hidden_objs) > 80:
        log(f"  ... plus {len(hidden_objs) - 80} more objects")

    log(f"Created v003 reboot objects: {len(created)}")
    for obj in created:
        log(f"  created: {obj.name}")
    log(f"Created/updated Text block: {text_name}")
    log("Suggested save-as: kfr_blockout_v003_toy_dna_silhouette_reboot_001.blend")
    log("Review package: front, side, back, three-quarter, hands close-up, head close-up, tail/stance close-up.")


if __name__ == "__main__":
    build_all()
