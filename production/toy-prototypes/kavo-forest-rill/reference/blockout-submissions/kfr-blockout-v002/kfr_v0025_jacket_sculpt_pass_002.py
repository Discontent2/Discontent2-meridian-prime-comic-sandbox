"""
KFR-BLOCKOUT-v002.5 Jacket Sculpt Pass 002

Run this after:
    kfr_v0025_jacket_sculpt_pass_001.py

Purpose:
    Improve the scripted jacket sculpt target after review. Pass 001 successfully
    made the torso read more like clothing, but it is still too rectangular and
    the front harness is still a bit cage-like.

This pass:
    - Hides Jacket Sculpt Pass 001 objects so the new pass reads cleanly.
    - Builds a slimmer, more shaped cropped jacket shell.
    - Adds rounder shoulder-to-jacket transitions.
    - Improves the open collar and lapel shape.
    - Reduces the big rectangular harness frame feeling.
    - Adds diagonal strap hints and shorter lower tabs.
    - Adds side/back jacket depth without creating a giant backpack slab.
    - Adds small sculpt guide beads/creases for jacket seams and belt breaks.

Important:
    This is still a sculpt proxy / visual target, not final hand sculpt detail.
    It is non-destructive. Toggle or delete this collection if needed.

Recommended file before running:
    kfr_blockout_v0025_jacket_sculpt_pass_001.blend

Recommended save-as after running:
    kfr_blockout_v0025_jacket_sculpt_pass_002.blend
"""

import math
import bpy

ROOT_COLLECTION_NAME = "kfr_blockout_v0025_jacket_sculpt_pass_002"
TEXT_BLOCK_NAME = "KFR_V0025_JACKET_SCULPT_PASS_002_NOTES"

# -----------------------------------------------------------------------------
# Visibility control
# -----------------------------------------------------------------------------

HIDE_PREVIOUS_JACKET_PASS = True
HIDE_OBJECT_FRAGMENTS = [
    "kfr_v0025_jacket_sculpt_001_",
    "kfr_v0025_cleanup_unified_cropped_jacket_shell",
    "kfr_v0025_cleanup_recessed_front_shirt_opening",
    "kfr_v0025_cleanup_clean_front_harness_strap",
    "kfr_v0025_cleanup_clean_upper_harness_yoke",
    "kfr_v0025_cleanup_clean_waist_belt",
    "kfr_v0025_cleanup_left_front_collar_lapel",
    "kfr_v0025_cleanup_right_front_collar_lapel",
    "kfr_v0025_cleanup_raised_back_collar_bridge",
]

# -----------------------------------------------------------------------------
# Materials
# -----------------------------------------------------------------------------

MAT_JACKET_MAIN = (0.35, 0.36, 0.35, 1.0)
MAT_JACKET_DARK = (0.18, 0.19, 0.19, 1.0)
MAT_JACKET_EDGE = (0.25, 0.26, 0.25, 1.0)
MAT_SHIRT = (0.56, 0.57, 0.54, 1.0)
MAT_HARNESS = (0.045, 0.045, 0.045, 1.0)
MAT_SHADOW = (0.025, 0.025, 0.025, 1.0)
MAT_GUIDE_BLUE = (0.10, 0.38, 0.95, 0.55)

# Coordinate convention:
# X = character left/right. Positive X = character left.
# Y = front/back. Negative Y = figure front.
# Z = up.

# A shaped X/Z outline for the jacket. It is intentionally less boxy than pass 001.
# The lower hem pulls inward, shoulders stay broad, and the chest has a gentle taper.
JACKET_FRONT_Y = -9.55
JACKET_BACK_Y = 4.20
JACKET_OUTLINE_XZ = [
    (-15.2, 91.2),
    (-18.0, 87.0),
    (-17.2, 79.0),
    (-15.4, 67.0),
    (-12.6, 57.2),
    (-7.2, 53.0),
    (-2.5, 52.0),
    (2.5, 52.0),
    (7.2, 53.0),
    (12.6, 57.2),
    (15.4, 67.0),
    (17.2, 79.0),
    (18.0, 87.0),
    (15.2, 91.2),
    (9.0, 94.3),
    (-9.0, 94.3),
]

# Shirt opening is taller and cleaner, with an angled lower point so it looks like
# an opening in a jacket rather than a plain rectangle.
SHIRT_OPENING_XZ = [
    (-7.7, 84.0),
    (-9.2, 76.5),
    (-8.4, 66.0),
    (-5.2, 59.0),
    (-1.4, 55.8),
    (0.0, 55.0),
    (1.4, 55.8),
    (5.2, 59.0),
    (8.4, 66.0),
    (9.2, 76.5),
    (7.7, 84.0),
]

# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------

def log(msg):
    print(f"[KFR JACKET SCULPT 002] {msg}")


def has_fragment(name, fragments):
    low = name.lower()
    return any(fragment.lower() in low for fragment in fragments)


def hide_previous_objects():
    hidden = []
    if not HIDE_PREVIOUS_JACKET_PASS:
        return hidden
    for obj in bpy.data.objects:
        if obj.type == "MESH" and has_fragment(obj.name, HIDE_OBJECT_FRAGMENTS):
            obj.hide_viewport = True
            obj.hide_render = True
            hidden.append(obj.name)
    return hidden


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
    try:
        mat.use_nodes = True
        bsdf = mat.node_tree.nodes.get("Principled BSDF")
        if bsdf:
            bsdf.inputs["Base Color"].default_value = rgba
            bsdf.inputs["Roughness"].default_value = 0.8
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


def add_bevel(obj, amount=0.5, segments=3):
    if amount <= 0:
        return obj
    bevel = obj.modifiers.new(name="jacket002_soft_bevel", type="BEVEL")
    bevel.width = amount
    bevel.segments = segments
    bevel.affect = "EDGES"
    obj.modifiers.new(name="jacket002_weighted_normals", type="WEIGHTED_NORMAL")
    return obj


def shade_smooth(obj):
    try:
        for poly in obj.data.polygons:
            poly.use_smooth = True
    except Exception:
        pass
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
    try:
        col.objects.link(obj)
    except RuntimeError:
        pass
    unlink_except(obj, col)
    return obj


def add_ellipsoid(name, loc, dims, mat, col, rotation=(0.0, 0.0, 0.0), segments=32, rings=16):
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
    shade_smooth(obj)
    try:
        col.objects.link(obj)
    except RuntimeError:
        pass
    unlink_except(obj, col)
    return obj


def create_prism_from_xz_outline(name, outline_xz, front_y, back_y, mat, col, bevel=0.8):
    verts = []
    for x, z in outline_xz:
        verts.append((x, front_y, z))
    for x, z in outline_xz:
        verts.append((x, back_y, z))

    n = len(outline_xz)
    faces = []
    faces.append(tuple(range(n - 1, -1, -1)))
    faces.append(tuple(range(n, 2 * n)))
    for i in range(n):
        j = (i + 1) % n
        faces.append((i, j, j + n, i + n))

    mesh = bpy.data.meshes.new(name + "_mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()

    obj = bpy.data.objects.new(name, mesh)
    obj.data.materials.append(mat)
    col.objects.link(obj)
    add_bevel(obj, bevel, 6)
    return obj


def create_notes_text_block():
    notes = """
KFR V002.5 JACKET SCULPT PASS 002

Review intent:
    Pass 002 should feel less like a rectangular chest cage and more like a cropped
    field jacket with harness gear over it.

Look for:
    - cleaner jacket taper at waist
    - softer shoulder transition into arms
    - more intentional raised collar
    - front shirt/opening still visible
    - harness reduced from a big rectangle into straps and useful gear blocks
    - side and three-quarter views reading less flat

Not final yet:
    - seam stitching
    - wrinkles
    - fabric texture
    - final harness buckles
    - final hard-surface cleanup

Recommended save-as:
    kfr_blockout_v0025_jacket_sculpt_pass_002.blend
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

def build_jacket_body(col, mats):
    created = []

    shell = create_prism_from_xz_outline(
        "kfr_v0025_jacket_sculpt_002_shaped_cropped_jacket_shell",
        JACKET_OUTLINE_XZ,
        JACKET_FRONT_Y,
        JACKET_BACK_Y,
        mats["jacket"],
        col,
        bevel=1.25,
    )
    created.append(shell)

    shirt = create_prism_from_xz_outline(
        "kfr_v0025_jacket_sculpt_002_recessed_open_shirt_panel",
        SHIRT_OPENING_XZ,
        front_y=-10.40,
        back_y=-9.72,
        mat=mats["shirt"],
        col=col,
        bevel=0.45,
    )
    created.append(shirt)

    # Rounded shoulder blobs that help the jacket attach to the arms.
    for x, side in [(18.8, "left"), (-18.8, "right")]:
        created.append(add_ellipsoid(
            f"kfr_v0025_jacket_sculpt_002_{side}_rounded_shoulder_blend",
            loc=(x, -1.9, 86.0),
            dims=(12.0, 13.0, 13.5),
            mat=mats["jacket"],
            col=col,
        ))
        created.append(add_cube(
            f"kfr_v0025_jacket_sculpt_002_{side}_side_panel_tapered_depth_mass",
            loc=(x * 0.86, 1.8, 72.0),
            dims=(3.8, 7.0, 29.0),
            mat=mats["edge"],
            col=col,
            bevel=0.75,
        ))

    # Better collar: back guard plus front lapels that point toward the shirt opening.
    created.append(add_cube(
        "kfr_v0025_jacket_sculpt_002_raised_back_collar_guard",
        loc=(0.0, 4.3, 94.2),
        dims=(24.0, 7.2, 7.6),
        mat=mats["dark"],
        col=col,
        bevel=1.0,
    ))
    created.append(add_cube(
        "kfr_v0025_jacket_sculpt_002_left_lapel_sloped_into_opening",
        loc=(6.4, -10.6, 88.0),
        dims=(7.5, 1.25, 12.0),
        mat=mats["dark"],
        col=col,
        rotation=(0.0, 0.0, math.radians(-18.0)),
        bevel=0.65,
    ))
    created.append(add_cube(
        "kfr_v0025_jacket_sculpt_002_right_lapel_sloped_into_opening",
        loc=(-6.4, -10.6, 88.0),
        dims=(7.5, 1.25, 12.0),
        mat=mats["dark"],
        col=col,
        rotation=(0.0, 0.0, math.radians(18.0)),
        bevel=0.65,
    ))

    # Waist shape and cropped hem. Dark pieces help us see where sculpt should pinch.
    for x, side in [(13.2, "left"), (-13.2, "right")]:
        created.append(add_cube(
            f"kfr_v0025_jacket_sculpt_002_{side}_waist_pinched_shadow",
            loc=(x, -10.75, 62.4),
            dims=(2.5, 0.52, 14.8),
            mat=mats["shadow"],
            col=col,
            bevel=0.22,
        ))
    created.append(add_cube(
        "kfr_v0025_jacket_sculpt_002_cropped_hem_slight_curve_proxy",
        loc=(0.0, -10.65, 55.0),
        dims=(27.5, 0.85, 2.4),
        mat=mats["dark"],
        col=col,
        bevel=0.45,
    ))

    # Tiny hem side blocks give the cropped jacket a manufactured toy seam read.
    for x, side in [(11.8, "left"), (-11.8, "right")]:
        created.append(add_cube(
            f"kfr_v0025_jacket_sculpt_002_{side}_hem_corner_turn_under",
            loc=(x, -10.5, 54.0),
            dims=(4.2, 0.8, 3.2),
            mat=mats["edge"],
            col=col,
            rotation=(0.0, 0.0, math.radians(-8.0 if x > 0 else 8.0)),
            bevel=0.35,
        ))

    return created


def build_refined_harness(col, mats):
    created = []

    # Vertical straps are narrower and sit on the chest instead of forming a giant box.
    for x, side in [(7.2, "left"), (-7.2, "right")]:
        created.append(add_cube(
            f"kfr_v0025_jacket_sculpt_002_{side}_narrow_front_harness_strap",
            loc=(x, -11.15, 72.8),
            dims=(1.75, 0.88, 26.0),
            mat=mats["harness"],
            col=col,
            bevel=0.28,
        ))

    created.append(add_cube(
        "kfr_v0025_jacket_sculpt_002_upper_chest_harness_bar_shorter",
        loc=(0.0, -11.18, 83.4),
        dims=(20.8, 0.82, 2.1),
        mat=mats["harness"],
        col=col,
        bevel=0.28,
    ))

    created.append(add_cube(
        "kfr_v0025_jacket_sculpt_002_waist_belt_slimmed",
        loc=(0.0, -11.08, 59.0),
        dims=(28.0, 0.95, 2.25),
        mat=mats["harness"],
        col=col,
        bevel=0.32,
    ))

    # Diagonal straps break the square-cage effect and give route-worker gear flavor.
    created.append(add_cube(
        "kfr_v0025_jacket_sculpt_002_left_diagonal_harness_hint",
        loc=(3.8, -11.28, 73.0),
        dims=(1.25, 0.65, 18.0),
        mat=mats["harness"],
        col=col,
        rotation=(0.0, 0.0, math.radians(-18.0)),
        bevel=0.22,
    ))
    created.append(add_cube(
        "kfr_v0025_jacket_sculpt_002_right_diagonal_harness_hint",
        loc=(-3.8, -11.28, 73.0),
        dims=(1.25, 0.65, 18.0),
        mat=mats["harness"],
        col=col,
        rotation=(0.0, 0.0, math.radians(18.0)),
        bevel=0.22,
    ))

    # Smaller drop tabs under the belt.
    for x, side in [(5.5, "left"), (-5.5, "right")]:
        created.append(add_cube(
            f"kfr_v0025_jacket_sculpt_002_{side}_short_lower_harness_drop_tab",
            loc=(x, -11.05, 54.2),
            dims=(1.7, 0.75, 5.4),
            mat=mats["harness"],
            col=col,
            bevel=0.22,
        ))

    # A tiny center buckle/read point, because the old blue line was too much like a UI marker.
    created.append(add_cube(
        "kfr_v0025_jacket_sculpt_002_center_buckle_placeholder",
        loc=(0.0, -11.6, 59.1),
        dims=(2.8, 0.45, 2.0),
        mat=mats["edge"],
        col=col,
        bevel=0.2,
    ))

    return created


def build_sculpt_guides(col, mats):
    created = []
    # Low-profile guide lines showing where to blend, not final details.
    created.append(add_cube(
        "kfr_v0025_jacket_sculpt_002_BLUE_GUIDE_soften_shoulder_to_chest_transition",
        loc=(0.0, -11.75, 86.7),
        dims=(18.0, 0.28, 0.55),
        mat=mats["guide"],
        col=col,
        bevel=0.12,
    ))
    created.append(add_cube(
        "kfr_v0025_jacket_sculpt_002_BLUE_GUIDE_keep_chest_opening_readable",
        loc=(0.0, -11.75, 66.0),
        dims=(12.0, 0.28, 0.55),
        mat=mats["guide"],
        col=col,
        bevel=0.12,
    ))
    return created

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

def main():
    log("Starting jacket sculpt improvement pass 002")

    hidden = hide_previous_objects()
    col = make_collection(ROOT_COLLECTION_NAME)

    mats = {
        "jacket": make_material("kfr_v0025_jacket_sculpt_002_jacket_main", MAT_JACKET_MAIN),
        "dark": make_material("kfr_v0025_jacket_sculpt_002_jacket_dark", MAT_JACKET_DARK),
        "edge": make_material("kfr_v0025_jacket_sculpt_002_jacket_edge", MAT_JACKET_EDGE),
        "shirt": make_material("kfr_v0025_jacket_sculpt_002_recessed_shirt", MAT_SHIRT),
        "harness": make_material("kfr_v0025_jacket_sculpt_002_harness_black", MAT_HARNESS),
        "shadow": make_material("kfr_v0025_jacket_sculpt_002_shadow", MAT_SHADOW),
        "guide": make_material("kfr_v0025_jacket_sculpt_002_blue_guide", MAT_GUIDE_BLUE),
    }

    created = []
    created.extend(build_jacket_body(col, mats))
    created.extend(build_refined_harness(col, mats))
    created.extend(build_sculpt_guides(col, mats))

    text_name = create_notes_text_block()

    log(f"Previous jacket/cleanup objects hidden: {len(hidden)}")
    for name in hidden:
        log(f"  hidden: {name}")

    log(f"Created jacket improvement objects: {len(created)}")
    for obj in created:
        log(f"  created: {obj.name}")

    log(f"Created/updated Text block: {text_name}")
    log("Save as: kfr_blockout_v0025_jacket_sculpt_pass_002.blend")
    log("Review: front torso close-up, front full-body, side full-body, three-quarter view.")


if __name__ == "__main__":
    main()
