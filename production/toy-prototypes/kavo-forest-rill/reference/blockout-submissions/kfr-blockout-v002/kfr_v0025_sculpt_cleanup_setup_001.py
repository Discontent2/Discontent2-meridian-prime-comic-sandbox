"""
KFR-BLOCKOUT-v002.5 Sculpt Cleanup Setup 001

Run this after the current v002 silhouette / garment restore work.

Purpose:
    Teach-by-seeing setup pass for the next stage. This script does two things:

    1. Scene hygiene:
       - hides known failed/experimental tail, stance, and old marker objects/collections
       - leaves the current accepted working figure visible
       - adds a Blender Text block with a short cleanup plan

    2. Visual cleanup guide geometry:
       - adds a new cohesive torso/jacket/harness cleanup layer
       - shows how to unify the boxy jacket/torso/harness stack into one readable toy form
       - adds guide forms for shoulder blending, collar integration, waist taper, and harness placement

Important:
    This is non-destructive. It creates a new collection and hides known experiments by name.
    If anything looks wrong, toggle the collection visibility or undo.

Recommended file before running:
    kfr_blockout_v002_silhouette_boost_pass_001.blend

Recommended save-as after running:
    kfr_blockout_v0025_sculpt_cleanup_setup_001.blend
"""

import math
import bpy

ROOT_COLLECTION_NAME = "kfr_blockout_v0025_sculpt_cleanup_setup_001"
TEXT_BLOCK_NAME = "KFR_V0025_SCULPT_CLEANUP_SETUP_001_NOTES"

# Coordinate convention:
# X = character left/right. Positive X = character left.
# Y = front/back. Negative Y = figure front.
# Z = up.

# -----------------------------------------------------------------------------
# Visibility hygiene lists
# -----------------------------------------------------------------------------

# These are the experimental pieces we know are not the current target direction.
# The script hides objects/collections containing these fragments.
HIDE_NAME_FRAGMENTS = [
    "tail_balance_fix_001",
    "tail_fix_002",
    "stancefix002",
    "stancefix003",
    "forward_knee_bend_marker",
    "kfr_v002_stage_02",
    "stage_02_legs_pelvis_tail",
    "old_disconnected",
    "misaligned",
]

# These are current/valuable directions and should not be hidden by this script.
KEEP_NAME_FRAGMENTS = [
    ROOT_COLLECTION_NAME,
    "garment_restore_001",
    "silhouette_boost_001",
    "headfix002",
    "headfix004",
    "watch",
    "route_reader",
    "original_tail",
    "tail_keyed_blockout",
    "part_011_tail",
]

# -----------------------------------------------------------------------------
# Materials
# -----------------------------------------------------------------------------
MAT_CLEANUP_JACKET = (0.30, 0.31, 0.31, 1.0)
MAT_CLEANUP_SHADOW = (0.04, 0.04, 0.04, 1.0)
MAT_CLEANUP_HARNESS = (0.08, 0.08, 0.08, 1.0)
MAT_CLEANUP_SHIRT = (0.54, 0.55, 0.52, 1.0)
MAT_CLEANUP_GUIDE_BLUE = (0.10, 0.36, 0.95, 0.75)
MAT_CLEANUP_PANTS = (0.34, 0.32, 0.28, 1.0)

# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------

def log(msg):
    print(f"[KFR V002.5 CLEANUP SETUP] {msg}")


def name_has_fragment(name, fragments):
    low = name.lower()
    return any(fragment.lower() in low for fragment in fragments)


def should_keep_name(name):
    return name_has_fragment(name, KEEP_NAME_FRAGMENTS)


def make_collection(name):
    existing = bpy.data.collections.get(name)
    if existing:
        for obj in list(existing.objects):
            bpy.data.objects.remove(obj, do_unlink=True)
        return existing
    col = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(col)
    return col


def make_material(name, rgba):
    existing = bpy.data.materials.get(name)
    if existing:
        return existing
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = rgba
    return mat


def link_to_collection(obj, col):
    try:
        col.objects.link(obj)
    except RuntimeError:
        pass


def add_bevel(obj, amount=0.5, segments=3):
    if amount <= 0:
        return obj
    bevel = obj.modifiers.new(name="cleanup_soft_bevel", type="BEVEL")
    bevel.width = amount
    bevel.segments = segments
    bevel.affect = "EDGES"
    obj.modifiers.new(name="cleanup_weighted_normals", type="WEIGHTED_NORMAL")
    return obj


def add_cube(name, loc, dims, mat, col, rotation=(0.0, 0.0, 0.0), bevel=0.45):
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=loc, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.dimensions = dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    add_bevel(obj, bevel, 3)
    link_to_collection(obj, col)
    return obj


def add_ellipsoid(name, loc, dims, mat, col, rotation=(0.0, 0.0, 0.0), segments=24, rings=12):
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
    obj.data.materials.append(mat)
    link_to_collection(obj, col)
    return obj

# -----------------------------------------------------------------------------
# Scene hygiene
# -----------------------------------------------------------------------------

def hide_known_experiments():
    hidden_objects = []
    hidden_collections = []

    for col in bpy.data.collections:
        if should_keep_name(col.name):
            continue
        if name_has_fragment(col.name, HIDE_NAME_FRAGMENTS):
            col.hide_viewport = True
            col.hide_render = True
            hidden_collections.append(col.name)

    for obj in bpy.data.objects:
        if should_keep_name(obj.name):
            continue
        if name_has_fragment(obj.name, HIDE_NAME_FRAGMENTS):
            obj.hide_viewport = True
            obj.hide_render = True
            hidden_objects.append(obj.name)

    return hidden_collections, hidden_objects


def create_cleanup_text_block():
    notes = """
KFR V002.5 SCULPT CLEANUP SETUP 001

Scene goal:
    Use the current v002 as a visual foundation, then start making the figure feel
    like one cohesive toy prototype instead of stacked blockout parts.

What this script did:
    - Hid known failed/experimental tail and stance pieces by name fragment.
    - Added a new cleanup guide collection for torso/jacket/harness cohesion.
    - Added visual forms showing shoulder blending, collar integration, waist taper,
      cleaner harness placement, and garment layering.

How to read the new guide shapes:
    - Jacket shell: the large softened torso layer. Sculpt toward this as one clothing mass.
    - Shoulder blends: rounded caps that show where jacket shoulders should merge into arms.
    - Collar pieces: guide the raised collar/neck transition.
    - Dark side cuts: visual taper marks, not literal holes.
    - Harness straps: placement guide for final straps over the jacket, not pasted cubes.

Do next:
    1. Save as kfr_blockout_v0025_sculpt_cleanup_setup_001.blend.
    2. Review front, side, three-quarter, and torso close-up.
    3. If the cleanup guide works, use it as the sculpt target for manual cleanup.
    4. Do not start final small details yet.
""".strip()

    existing = bpy.data.texts.get(TEXT_BLOCK_NAME)
    if existing:
        existing.clear()
        text = existing
    else:
        text = bpy.data.texts.new(TEXT_BLOCK_NAME)
    text.write(notes + "\n")
    return text.name

# -----------------------------------------------------------------------------
# Visual cleanup guide geometry
# -----------------------------------------------------------------------------

def build_torso_jacket_cleanup(col, mats):
    created = []
    mat_jacket = mats["jacket"]
    mat_shadow = mats["shadow"]
    mat_harness = mats["harness"]
    mat_shirt = mats["shirt"]
    mat_guide = mats["guide"]

    # Main softened jacket shell. It intentionally covers some earlier box clutter.
    created.append(add_cube(
        "kfr_v0025_cleanup_unified_cropped_jacket_shell",
        loc=(0.0, -1.8, 73.0),
        dims=(33.0, 15.0, 37.0),
        mat=mat_jacket,
        col=col,
        bevel=1.8,
    ))

    # Front shirt opening recessed inside jacket.
    created.append(add_cube(
        "kfr_v0025_cleanup_recessed_front_shirt_opening",
        loc=(0.0, -9.7, 73.0),
        dims=(14.0, 1.0, 25.0),
        mat=mat_shirt,
        col=col,
        bevel=0.65,
    ))

    # Shoulder-to-torso blends. These show where to sculpt shoulder shelf into torso.
    for x, side in [(19.5, "left"), (-19.5, "right")]:
        created.append(add_ellipsoid(
            f"kfr_v0025_cleanup_{side}_soft_jacket_shoulder_blend",
            loc=(x, -1.8, 86.0),
            dims=(13.5, 14.0, 14.0),
            mat=mat_jacket,
            col=col,
            rotation=(0.0, 0.0, 0.0),
        ))

    # Raised collar/neck transition. This makes the head-neck-jacket read more unified.
    created.append(add_cube(
        "kfr_v0025_cleanup_raised_back_collar_bridge",
        loc=(0.0, 4.8, 93.5),
        dims=(25.0, 8.0, 8.5),
        mat=mat_jacket,
        col=col,
        bevel=1.0,
    ))
    created.append(add_cube(
        "kfr_v0025_cleanup_left_front_collar_lapel",
        loc=(7.0, -9.0, 89.0),
        dims=(8.5, 2.6, 12.0),
        mat=mat_jacket,
        col=col,
        rotation=(0.0, 0.0, math.radians(-13.0)),
        bevel=0.8,
    ))
    created.append(add_cube(
        "kfr_v0025_cleanup_right_front_collar_lapel",
        loc=(-7.0, -9.0, 89.0),
        dims=(8.5, 2.6, 12.0),
        mat=mat_jacket,
        col=col,
        rotation=(0.0, 0.0, math.radians(13.0)),
        bevel=0.8,
    ))

    # Waist taper read. These are visible dark guide shapes to sculpt around.
    for x, side in [(13.8, "left"), (-13.8, "right")]:
        created.append(add_cube(
            f"kfr_v0025_cleanup_{side}_waist_taper_shadow_guide",
            loc=(x, -10.2, 62.5),
            dims=(3.4, 0.9, 16.0),
            mat=mat_shadow,
            col=col,
            bevel=0.3,
        ))

    # Jacket hem line and side depth. Helps the jacket read cropped, not a torso brick.
    created.append(add_cube(
        "kfr_v0025_cleanup_cropped_jacket_hem_curve_bar",
        loc=(0.0, -9.6, 55.5),
        dims=(29.0, 1.1, 2.8),
        mat=mat_shadow,
        col=col,
        bevel=0.45,
    ))
    for x, side in [(16.5, "left"), (-16.5, "right")]:
        created.append(add_cube(
            f"kfr_v0025_cleanup_{side}_jacket_side_depth_plane",
            loc=(x, 2.0, 72.0),
            dims=(4.0, 8.0, 31.0),
            mat=mat_jacket,
            col=col,
            bevel=0.8,
        ))

    # Cleaner harness as a guide over the unified jacket shell.
    for x, side in [(7.8, "left"), (-7.8, "right")]:
        created.append(add_cube(
            f"kfr_v0025_cleanup_{side}_clean_front_harness_strap",
            loc=(x, -10.8, 73.5),
            dims=(2.2, 1.0, 29.0),
            mat=mat_harness,
            col=col,
            bevel=0.35,
        ))
    created.append(add_cube(
        "kfr_v0025_cleanup_clean_upper_harness_yoke",
        loc=(0.0, -11.0, 85.0),
        dims=(26.0, 1.0, 2.4),
        mat=mat_harness,
        col=col,
        bevel=0.35,
    ))
    created.append(add_cube(
        "kfr_v0025_cleanup_clean_waist_belt",
        loc=(0.0, -10.8, 59.0),
        dims=(30.0, 1.1, 2.6),
        mat=mat_harness,
        col=col,
        bevel=0.35,
    ))

    # Blue guide pads tell the learner where to blend, not final art.
    created.append(add_cube(
        "kfr_v0025_cleanup_BLUE_GUIDE_blend_harness_into_jacket_not_pasted",
        loc=(0.0, -12.0, 68.0),
        dims=(19.0, 0.45, 1.0),
        mat=mat_guide,
        col=col,
        bevel=0.2,
    ))

    return created


def build_pants_cleanup_guides(col, mats):
    created = []
    mat_pants = mats["pants"]
    mat_shadow = mats["shadow"]
    mat_guide = mats["guide"]

    # These are small guide overlays, not a full lower-body rebuild.
    for x, side, outer in [(12.0, "left", 1), (-12.0, "right", -1)]:
        created.append(add_ellipsoid(
            f"kfr_v0025_cleanup_{side}_pants_panel_blend_volume_thigh",
            loc=(x + outer * 1.5, -5.8, 42.0),
            dims=(10.0, 4.8, 13.0),
            mat=mat_pants,
            col=col,
            rotation=(math.radians(-4.0), 0.0, 0.0),
        ))
        created.append(add_cube(
            f"kfr_v0025_cleanup_{side}_knee_panel_blend_guide",
            loc=(x, -8.0, 33.2),
            dims=(9.5, 1.0, 5.8),
            mat=mat_shadow,
            col=col,
            bevel=0.45,
        ))
        created.append(add_cube(
            f"kfr_v0025_cleanup_BLUE_GUIDE_{side}_pants_panels_should_sculpt_into_leg",
            loc=(x, -9.1, 38.0),
            dims=(8.5, 0.45, 0.9),
            mat=mat_guide,
            col=col,
            bevel=0.15,
        ))

    return created

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

def main():
    log("Starting v002.5 sculpt cleanup setup 001")

    hidden_collections, hidden_objects = hide_known_experiments()
    text_name = create_cleanup_text_block()

    col = make_collection(ROOT_COLLECTION_NAME)
    mats = {
        "jacket": make_material("kfr_v0025_cleanup_jacket_gray", MAT_CLEANUP_JACKET),
        "shadow": make_material("kfr_v0025_cleanup_shadow_dark", MAT_CLEANUP_SHADOW),
        "harness": make_material("kfr_v0025_cleanup_harness_black", MAT_CLEANUP_HARNESS),
        "shirt": make_material("kfr_v0025_cleanup_inner_shirt_gray", MAT_CLEANUP_SHIRT),
        "guide": make_material("kfr_v0025_cleanup_blue_learning_guides", MAT_CLEANUP_GUIDE_BLUE),
        "pants": make_material("kfr_v0025_cleanup_pants_gray_brown", MAT_CLEANUP_PANTS),
    }

    created = []
    created.extend(build_torso_jacket_cleanup(col, mats))
    created.extend(build_pants_cleanup_guides(col, mats))

    log(f"Hidden collections: {len(hidden_collections)}")
    for name in hidden_collections:
        log(f"  hidden collection: {name}")

    log(f"Hidden objects: {len(hidden_objects)}")
    for name in hidden_objects:
        log(f"  hidden object: {name}")

    log(f"Created cleanup guide objects: {len(created)}")
    for obj in created:
        log(f"  created: {obj.name}")

    log(f"Created/updated Text block: {text_name}")
    log("Save as: kfr_blockout_v0025_sculpt_cleanup_setup_001.blend")
    log("Review: front full-body, front torso close-up, side full-body, and three-quarter view.")
    log("If it feels too bulky, hide the collection and we will make cleanup setup 002 lighter.")


if __name__ == "__main__":
    main()
