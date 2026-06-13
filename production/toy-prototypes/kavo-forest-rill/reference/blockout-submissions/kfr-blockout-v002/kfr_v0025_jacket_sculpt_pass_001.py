"""
KFR-BLOCKOUT-v002.5 Jacket Sculpt Pass 001

Run this after:
    kfr_v0025_sculpt_cleanup_setup_001.py

Purpose:
    Scripted sculpt-like jacket pass. This does not use hand brushes, but it creates
    a cleaner cohesive jacket proxy that demonstrates the next manual sculpt target.

What it does:
    - Hides the earlier v002.5 torso cleanup guide pieces so the scene is easier to read.
    - Builds a single tapered jacket shell mesh instead of another plain cube.
    - Adds softened shoulder blends, raised collar, open front lapels, cropped hem,
      waist taper shadows, and cleaner harness straps.
    - Adds a Blender Text block explaining what to look at.

Important:
    Non-destructive. It creates a new collection. If this overdoes the look, hide
    the collection and restore the previous cleanup guide visibility.

Recommended file before running:
    kfr_blockout_v0025_sculpt_cleanup_setup_001.blend

Recommended save-as after running:
    kfr_blockout_v0025_jacket_sculpt_pass_001.blend
"""

import math
import bpy
from mathutils import Vector

ROOT_COLLECTION_NAME = "kfr_blockout_v0025_jacket_sculpt_pass_001"
TEXT_BLOCK_NAME = "KFR_V0025_JACKET_SCULPT_PASS_001_NOTES"

# Coordinate convention:
# X = character left/right. Positive X = character left.
# Y = front/back. Negative Y = figure front.
# Z = up.

HIDE_PREVIOUS_TORSO_GUIDES = True
PREVIOUS_GUIDE_FRAGMENTS = [
    "kfr_v0025_cleanup_unified_cropped_jacket_shell",
    "kfr_v0025_cleanup_recessed_front_shirt_opening",
    "kfr_v0025_cleanup_soft_jacket_shoulder_blend",
    "kfr_v0025_cleanup_raised_back_collar_bridge",
    "kfr_v0025_cleanup_left_front_collar_lapel",
    "kfr_v0025_cleanup_right_front_collar_lapel",
    "kfr_v0025_cleanup_left_waist_taper_shadow_guide",
    "kfr_v0025_cleanup_right_waist_taper_shadow_guide",
    "kfr_v0025_cleanup_cropped_jacket_hem_curve_bar",
    "kfr_v0025_cleanup_jacket_side_depth_plane",
    "kfr_v0025_cleanup_clean_front_harness_strap",
    "kfr_v0025_cleanup_clean_upper_harness_yoke",
    "kfr_v0025_cleanup_clean_waist_belt",
    "kfr_v0025_cleanup_BLUE_GUIDE_blend_harness_into_jacket_not_pasted",
]

# Materials
MAT_JACKET = (0.34, 0.35, 0.34, 1.0)
MAT_JACKET_DARK = (0.19, 0.20, 0.20, 1.0)
MAT_SHIRT = (0.55, 0.56, 0.53, 1.0)
MAT_HARNESS = (0.05, 0.05, 0.05, 1.0)
MAT_SHADOW = (0.025, 0.025, 0.025, 1.0)
MAT_GUIDE_BLUE = (0.10, 0.38, 0.95, 0.55)

# Main sculpted jacket shell outline on the X/Z plane.
# This creates a tapered vest/jacket mass with softened bevels.
JACKET_FRONT_Y = -9.2
JACKET_BACK_Y = 4.8
JACKET_OUTLINE_XZ = [
    (-17.5, 88.5),
    (-16.4, 80.0),
    (-15.2, 64.0),
    (-12.5, 54.2),
    (-6.0, 52.8),
    (6.0, 52.8),
    (12.5, 54.2),
    (15.2, 64.0),
    (16.4, 80.0),
    (17.5, 88.5),
    (12.5, 93.2),
    (-12.5, 93.2),
]

# Chest opening shape is separate and lighter, set slightly in front.
CHEST_OPENING_OUTLINE_XZ = [
    (-8.0, 83.5),
    (-9.2, 75.0),
    (-7.4, 62.0),
    (-4.0, 57.0),
    (4.0, 57.0),
    (7.4, 62.0),
    (9.2, 75.0),
    (8.0, 83.5),
]

# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------

def log(msg):
    print(f"[KFR JACKET SCULPT 001] {msg}")


def name_has_fragment(name, fragments):
    low = name.lower()
    return any(fragment.lower() in low for fragment in fragments)


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
            bsdf.inputs["Roughness"].default_value = 0.78
    except Exception:
        pass
    return mat


def link_to_collection(obj, col):
    try:
        col.objects.link(obj)
    except RuntimeError:
        pass


def unlink_from_other_collections(obj, keep_col):
    for c in list(obj.users_collection):
        if c != keep_col:
            try:
                c.objects.unlink(obj)
            except RuntimeError:
                pass


def add_bevel(obj, amount=0.5, segments=3):
    if amount <= 0:
        return obj
    bevel = obj.modifiers.new(name="scripted_sculpt_soft_bevel", type="BEVEL")
    bevel.width = amount
    bevel.segments = segments
    bevel.affect = "EDGES"
    obj.modifiers.new(name="scripted_sculpt_weighted_normals", type="WEIGHTED_NORMAL")
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
    link_to_collection(obj, col)
    unlink_from_other_collections(obj, col)
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
    link_to_collection(obj, col)
    unlink_from_other_collections(obj, col)
    return obj


def create_prism_from_xz_outline(name, outline_xz, front_y, back_y, mat, col, bevel=0.75):
    """Create an extruded jacket shell from an X/Z outline and Y depth."""
    verts = []
    # front loop
    for x, z in outline_xz:
        verts.append((x, front_y, z))
    # back loop
    for x, z in outline_xz:
        verts.append((x, back_y, z))

    n = len(outline_xz)
    faces = []
    # front face, reverse order for outward normal toward negative Y
    faces.append(tuple(range(n - 1, -1, -1)))
    # back face
    faces.append(tuple(range(n, 2 * n)))
    # side faces
    for i in range(n):
        j = (i + 1) % n
        faces.append((i, j, j + n, i + n))

    mesh = bpy.data.meshes.new(name + "_mesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()

    obj = bpy.data.objects.new(name, mesh)
    obj.data.materials.append(mat)
    col.objects.link(obj)
    add_bevel(obj, bevel, 5)
    return obj


def hide_previous_guides():
    hidden = []
    if not HIDE_PREVIOUS_TORSO_GUIDES:
        return hidden
    for obj in bpy.data.objects:
        if name_has_fragment(obj.name, PREVIOUS_GUIDE_FRAGMENTS):
            obj.hide_viewport = True
            obj.hide_render = True
            hidden.append(obj.name)
    return hidden


def create_notes_text_block():
    notes = """
KFR V002.5 JACKET SCULPT PASS 001

What changed:
    This scripted pass creates a cleaner sculpt target for the torso jacket.
    It replaces the visual read of stacked blockout plates with a tapered jacket
    shell, softened shoulders, raised collar, lapels, belt/hem, and cleaner harness.

How to review:
    - Front: jacket should read as one garment, not a box with parts stuck on.
    - Side: collar and back depth should make the torso feel less flat.
    - Three-quarter: shoulders should start to connect head/arms/torso.
    - Close-up: harness should be readable but still simple enough for later sculpt.

What not to worry about yet:
    - tiny wrinkles
    - exact seam lines
    - final surface texture
    - final boot detail
    - final tail articulation

Recommended save-as:
    kfr_blockout_v0025_jacket_sculpt_pass_001.blend
""".strip()

    text = bpy.data.texts.get(TEXT_BLOCK_NAME)
    if text:
        text.clear()
    else:
        text = bpy.data.texts.new(TEXT_BLOCK_NAME)
    text.write(notes + "\n")
    return text.name

# -----------------------------------------------------------------------------
# Sculpt-like jacket build
# -----------------------------------------------------------------------------

def build_jacket_sculpt(col, mats):
    created = []

    # Unified shell: main jacket body as tapered extruded mesh.
    shell = create_prism_from_xz_outline(
        "kfr_v0025_jacket_sculpt_001_unified_tapered_jacket_shell",
        JACKET_OUTLINE_XZ,
        JACKET_FRONT_Y,
        JACKET_BACK_Y,
        mats["jacket"],
        col,
        bevel=1.15,
    )
    created.append(shell)

    # Recessed shirt/chest opening. Slightly in front so it is easy to judge.
    shirt = create_prism_from_xz_outline(
        "kfr_v0025_jacket_sculpt_001_recessed_chest_shirt_panel",
        CHEST_OPENING_OUTLINE_XZ,
        front_y=-10.15,
        back_y=-9.45,
        mat=mats["shirt"],
        col=col,
        bevel=0.45,
    )
    created.append(shirt)

    # Shoulder blends: rounded masses linking arms to jacket shelf.
    for x, side in [(19.8, "left"), (-19.8, "right")]:
        created.append(add_ellipsoid(
            f"kfr_v0025_jacket_sculpt_001_{side}_soft_shoulder_jacket_blend",
            loc=(x, -1.8, 86.2),
            dims=(12.2, 13.0, 13.0),
            mat=mats["jacket"],
            col=col,
            rotation=(0.0, 0.0, 0.0),
        ))

    # Raised back collar, slightly protective and scout-like.
    created.append(add_cube(
        "kfr_v0025_jacket_sculpt_001_raised_back_collar_sculpt_mass",
        loc=(0.0, 4.9, 94.0),
        dims=(24.5, 7.6, 8.4),
        mat=mats["jacket_dark"],
        col=col,
        bevel=1.1,
    ))

    # Front lapels/open collar, angled inward.
    created.append(add_cube(
        "kfr_v0025_jacket_sculpt_001_left_front_lapel_sculpt_mass",
        loc=(7.1, -10.25, 88.3),
        dims=(8.2, 1.4, 11.8),
        mat=mats["jacket_dark"],
        col=col,
        rotation=(0.0, 0.0, math.radians(-14.0)),
        bevel=0.75,
    ))
    created.append(add_cube(
        "kfr_v0025_jacket_sculpt_001_right_front_lapel_sculpt_mass",
        loc=(-7.1, -10.25, 88.3),
        dims=(8.2, 1.4, 11.8),
        mat=mats["jacket_dark"],
        col=col,
        rotation=(0.0, 0.0, math.radians(14.0)),
        bevel=0.75,
    ))

    # Dark taper shadows at the waist. These guide sculpting; they are not holes.
    for x, side in [(13.9, "left"), (-13.9, "right")]:
        created.append(add_cube(
            f"kfr_v0025_jacket_sculpt_001_{side}_waist_taper_shadow_sculpt_guide",
            loc=(x, -10.65, 62.6),
            dims=(2.8, 0.55, 15.5),
            mat=mats["shadow"],
            col=col,
            bevel=0.25,
        ))

    # Cropped hem and belt. This gives the jacket a toy-like readable stop line.
    created.append(add_cube(
        "kfr_v0025_jacket_sculpt_001_cropped_jacket_hem_soft_bar",
        loc=(0.0, -10.55, 55.3),
        dims=(28.8, 0.85, 2.6),
        mat=mats["jacket_dark"],
        col=col,
        bevel=0.45,
    ))
    created.append(add_cube(
        "kfr_v0025_jacket_sculpt_001_clean_waist_belt_over_jacket",
        loc=(0.0, -10.85, 59.4),
        dims=(30.0, 1.0, 2.5),
        mat=mats["harness"],
        col=col,
        bevel=0.38,
    ))

    # Harness, now cleaner and placed over the shell.
    for x, side in [(7.8, "left"), (-7.8, "right")]:
        created.append(add_cube(
            f"kfr_v0025_jacket_sculpt_001_{side}_vertical_harness_strap_over_jacket",
            loc=(x, -11.05, 73.5),
            dims=(2.15, 0.95, 28.2),
            mat=mats["harness"],
            col=col,
            bevel=0.35,
        ))

    created.append(add_cube(
        "kfr_v0025_jacket_sculpt_001_upper_harness_yoke_over_chest",
        loc=(0.0, -11.08, 84.2),
        dims=(25.5, 0.95, 2.3),
        mat=mats["harness"],
        col=col,
        bevel=0.35,
    ))

    # Small tabs under belt keep earlier gear logic without cluttering the read.
    for x, side in [(5.8, "left"), (-5.8, "right")]:
        created.append(add_cube(
            f"kfr_v0025_jacket_sculpt_001_{side}_short_harness_drop_tab",
            loc=(x, -11.0, 54.5),
            dims=(2.0, 0.85, 6.0),
            mat=mats["harness"],
            col=col,
            bevel=0.25,
        ))

    # Side depth planes help the side view read as jacket thickness instead of slab torso.
    for x, side in [(16.8, "left"), (-16.8, "right")]:
        created.append(add_cube(
            f"kfr_v0025_jacket_sculpt_001_{side}_side_depth_seam_mass",
            loc=(x, 1.9, 72.0),
            dims=(3.2, 7.6, 30.0),
            mat=mats["jacket_dark"],
            col=col,
            bevel=0.75,
        ))

    # Blue low-profile guide line: shows intended blend zone without dominating the sculpt.
    created.append(add_cube(
        "kfr_v0025_jacket_sculpt_001_BLUE_GUIDE_blend_zone_keep_soft",
        loc=(0.0, -11.6, 68.0),
        dims=(17.0, 0.35, 0.75),
        mat=mats["guide"],
        col=col,
        bevel=0.15,
    ))

    return created

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

def main():
    log("Starting scripted jacket sculpt pass 001")

    hidden = hide_previous_guides()
    col = make_collection(ROOT_COLLECTION_NAME)

    mats = {
        "jacket": make_material("kfr_v0025_jacket_sculpt_001_jacket_gray", MAT_JACKET),
        "jacket_dark": make_material("kfr_v0025_jacket_sculpt_001_jacket_dark", MAT_JACKET_DARK),
        "shirt": make_material("kfr_v0025_jacket_sculpt_001_inner_shirt", MAT_SHIRT),
        "harness": make_material("kfr_v0025_jacket_sculpt_001_harness_black", MAT_HARNESS),
        "shadow": make_material("kfr_v0025_jacket_sculpt_001_shadow_dark", MAT_SHADOW),
        "guide": make_material("kfr_v0025_jacket_sculpt_001_blue_guide", MAT_GUIDE_BLUE),
    }

    created = build_jacket_sculpt(col, mats)
    text_name = create_notes_text_block()

    log(f"Previous torso guide objects hidden: {len(hidden)}")
    for name in hidden:
        log(f"  hidden: {name}")

    log(f"Created jacket sculpt objects: {len(created)}")
    for obj in created:
        log(f"  created: {obj.name}")

    log(f"Created/updated Text block: {text_name}")
    log("Save as: kfr_blockout_v0025_jacket_sculpt_pass_001.blend")
    log("Review: front torso close-up, front full-body, side full-body, three-quarter view.")
    log("This is a sculpt target/proxy, not final detailing. Keep the clay broad and readable.")


if __name__ == "__main__":
    main()
