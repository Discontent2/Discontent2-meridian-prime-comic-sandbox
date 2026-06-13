"""
KFR-BLOCKOUT-v002 Silhouette Boost 001

Run this after:
    kfr_v002_garment_restore_001.py

Purpose:
    Get the v002 figure closer to a strong readable Forest Rill silhouette without
    starting final sculpt detail.

Current problem this fixes:
    The model reads, but the silhouette is too mannequin-straight and too flat:
    - torso is still boxy without enough jacket shape
    - shoulders / collar are not strong enough
    - legs need stronger pants bulk against the accepted tail
    - boots need a little more grounded toy weight
    - gear profile needs a few larger read-from-distance landmarks

Adds:
    - broader jacket shoulder/collar masses
    - cropped jacket side flares and rear/side depth hints
    - waist taper shadow blocks so torso is less rectangular
    - stronger thigh/calf outer silhouettes
    - knee pad / pants panel landmarks
    - boot toe/sole silhouette boosters
    - forearm glove cuff boosters
    - compact pack/route-worker side profile blocks

Important:
    Non-destructive. It creates a new collection and does not modify the original
    tail, head, watch, or stance. Toggle/delete the collection if it overdoes the look.

Recommended file before running:
    kfr_blockout_v002_garment_restore_pass_001.blend

Recommended file after running:
    kfr_blockout_v002_silhouette_boost_pass_001.blend
"""

import math
import bpy

ROOT_COLLECTION_NAME = "kfr_blockout_v002_silhouette_boost_001"

# Coordinate convention:
# X = character left/right. Positive X = character left.
# Y = front/back. Negative Y = figure front.
# Z = up.

# -----------------------------------------------------------------------------
# Materials
# -----------------------------------------------------------------------------
MAT_JACKET_DARK = (0.18, 0.19, 0.19, 1.0)
MAT_JACKET_MID = (0.34, 0.35, 0.34, 1.0)
MAT_PANTS = (0.38, 0.34, 0.28, 1.0)
MAT_BOOT = (0.06, 0.06, 0.06, 1.0)
MAT_SOLE = (0.16, 0.16, 0.16, 1.0)
MAT_GLOVE = (0.08, 0.08, 0.08, 1.0)
MAT_GEAR = (0.20, 0.22, 0.22, 1.0)
MAT_SHADOW = (0.03, 0.03, 0.03, 1.0)

# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------

def log(msg):
    print(f"[KFR SILHOUETTE BOOST 001] {msg}")


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


def add_bevel(obj, amount=0.6, segments=3):
    mod = obj.modifiers.new(name="blockout_soft_bevel", type="BEVEL")
    mod.width = amount
    mod.segments = segments
    mod.affect = "EDGES"
    obj.modifiers.new(name="blockout_weighted_normals", type="WEIGHTED_NORMAL")
    return obj


def add_cube(name, loc, dims, mat, col, rotation=(0.0, 0.0, 0.0), bevel=0.45):
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=loc, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.dimensions = dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    if bevel:
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
    add_bevel(obj, 0.0, 1)
    link_to_collection(obj, col)
    return obj


def add_cylinder(name, loc, radius, depth, mat, col, rotation=(0.0, 0.0, 0.0), vertices=24):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=depth, location=loc, rotation=rotation)
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.data.materials.append(mat)
    add_bevel(obj, 0.15, 2)
    link_to_collection(obj, col)
    return obj

# -----------------------------------------------------------------------------
# Silhouette systems
# -----------------------------------------------------------------------------

def build_jacket_and_torso(col, mat_dark, mat_mid, mat_shadow, mat_gear):
    created = []

    # Broader cropped jacket shoulder shelf. This gives Forest a stronger toyetic upper silhouette.
    created.append(add_cube(
        "kfr_silhouette_boost_001_broad_cropped_jacket_shoulder_shelf",
        loc=(0.0, -0.8, 91.0),
        dims=(39.0, 13.0, 7.0),
        mat=mat_mid,
        col=col,
        bevel=1.2,
    ))

    # Shoulder cap blocks that break the straight cylinder-arm mannequin read.
    for x, label in [(23.0, "left"), (-23.0, "right")]:
        created.append(add_ellipsoid(
            f"kfr_silhouette_boost_001_{label}_jacket_shoulder_cap",
            loc=(x, -1.5, 86.0),
            dims=(9.5, 12.0, 12.0),
            mat=mat_mid,
            col=col,
            rotation=(0.0, math.radians(0.0), 0.0),
        ))

    # Chunky raised collar / neck shelter. Helps the head stop floating on a tube.
    created.append(add_cube(
        "kfr_silhouette_boost_001_raised_back_collar_mass",
        loc=(0.0, 5.0, 95.5),
        dims=(25.0, 8.0, 9.0),
        mat=mat_dark,
        col=col,
        bevel=1.0,
    ))
    created.append(add_cube(
        "kfr_silhouette_boost_001_front_open_collar_left",
        loc=(8.0, -7.2, 91.5),
        dims=(8.0, 3.0, 8.5),
        mat=mat_dark,
        col=col,
        rotation=(0.0, 0.0, math.radians(-10.0)),
        bevel=0.8,
    ))
    created.append(add_cube(
        "kfr_silhouette_boost_001_front_open_collar_right",
        loc=(-8.0, -7.2, 91.5),
        dims=(8.0, 3.0, 8.5),
        mat=mat_dark,
        col=col,
        rotation=(0.0, 0.0, math.radians(10.0)),
        bevel=0.8,
    ))

    # Side jacket depth panels, visible in side view.
    for x, label in [(17.5, "left"), (-17.5, "right")]:
        created.append(add_cube(
            f"kfr_silhouette_boost_001_{label}_jacket_side_depth_panel",
            loc=(x, 1.8, 73.0),
            dims=(5.0, 10.0, 31.0),
            mat=mat_mid,
            col=col,
            bevel=0.9,
        ))

    # Cropped jacket hem flares, wider than waist, to avoid the plain rectangle torso.
    for x, label, rot in [(15.5, "left", -7.0), (-15.5, "right", 7.0)]:
        created.append(add_cube(
            f"kfr_silhouette_boost_001_{label}_cropped_jacket_hem_flare",
            loc=(x, -3.8, 56.0),
            dims=(9.0, 5.0, 8.0),
            mat=mat_mid,
            col=col,
            rotation=(0.0, 0.0, math.radians(rot)),
            bevel=0.8,
        ))

    # Waist shadow cut-ins imply taper without boolean cutting the torso.
    for x, label in [(14.6, "left"), (-14.6, "right")]:
        created.append(add_cube(
            f"kfr_silhouette_boost_001_{label}_waist_taper_shadow_cut_in",
            loc=(x, -8.7, 63.5),
            dims=(3.0, 1.2, 14.0),
            mat=mat_shadow,
            col=col,
            bevel=0.25,
        ))

    # Front diagonal harness suggestions for a stronger torso read.
    created.append(add_cube(
        "kfr_silhouette_boost_001_front_diagonal_harness_left_to_center",
        loc=(5.6, -9.2, 75.0),
        dims=(2.5, 1.0, 24.0),
        mat=mat_dark,
        col=col,
        rotation=(0.0, 0.0, math.radians(-18.0)),
        bevel=0.35,
    ))
    created.append(add_cube(
        "kfr_silhouette_boost_001_front_diagonal_harness_right_to_center",
        loc=(-5.6, -9.2, 75.0),
        dims=(2.5, 1.0, 24.0),
        mat=mat_dark,
        col=col,
        rotation=(0.0, 0.0, math.radians(18.0)),
        bevel=0.35,
    ))

    # Compact back/side gear pack block visible in profile, but not a giant backpack.
    created.append(add_cube(
        "kfr_silhouette_boost_001_compact_back_route_worker_pack_mass",
        loc=(0.0, 10.4, 73.0),
        dims=(21.0, 5.2, 24.0),
        mat=mat_gear,
        col=col,
        bevel=0.8,
    ))

    return created


def build_arms_gloves(col, mat_glove, mat_mid):
    created = []

    # Forearm cuff boosters make gloves read better from a distance.
    for x, label in [(24.8, "left"), (-24.8, "right")]:
        created.append(add_cube(
            f"kfr_silhouette_boost_001_{label}_fingerless_glove_cuff_mass",
            loc=(x, -5.5, 43.5),
            dims=(9.0, 6.0, 5.8),
            mat=mat_glove,
            col=col,
            bevel=0.75,
        ))
        created.append(add_cube(
            f"kfr_silhouette_boost_001_{label}_forearm_wrap_band",
            loc=(x, -4.8, 50.0),
            dims=(8.5, 5.5, 3.0),
            mat=mat_mid,
            col=col,
            bevel=0.55,
        ))

    return created


def build_legs_and_boots(col, mat_pants, mat_shadow, mat_boot, mat_sole):
    created = []

    for x, side, outer_sign in [(12.0, "left", 1), (-12.0, "right", -1)]:
        # Outer thigh silhouette pad. This makes legs match the tail better without becoming tree trunks.
        created.append(add_ellipsoid(
            f"kfr_silhouette_boost_001_{side}_outer_thigh_pants_mass",
            loc=(x + outer_sign * 3.4, -1.7, 43.0),
            dims=(7.5, 8.0, 18.0),
            mat=mat_pants,
            col=col,
            rotation=(math.radians(-5.0), 0.0, 0.0),
        ))

        # Forward thigh patch, larger than garment restore detail.
        created.append(add_cube(
            f"kfr_silhouette_boost_001_{side}_large_thigh_patch_landmark",
            loc=(x, -7.0, 43.0),
            dims=(9.5, 1.4, 11.0),
            mat=mat_shadow,
            col=col,
            bevel=0.45,
        ))

        # Knee cap and lower-leg calf volume.
        created.append(add_ellipsoid(
            f"kfr_silhouette_boost_001_{side}_knee_cap_mass",
            loc=(x, -6.8, 33.5),
            dims=(10.2, 4.0, 6.8),
            mat=mat_pants,
            col=col,
        ))
        created.append(add_ellipsoid(
            f"kfr_silhouette_boost_001_{side}_outer_calf_pants_mass",
            loc=(x + outer_sign * 2.7, -1.3, 23.0),
            dims=(6.4, 7.0, 15.5),
            mat=mat_pants,
            col=col,
            rotation=(math.radians(-5.0), 0.0, 0.0),
        ))

        # Boot grounding boosters. Adds toy weight and makes stance less spindly.
        created.append(add_cube(
            f"kfr_silhouette_boost_001_{side}_boot_outer_wall_booster",
            loc=(x + outer_sign * 4.8, -2.5, 6.5),
            dims=(3.8, 22.0, 8.5),
            mat=mat_boot,
            col=col,
            bevel=0.75,
        ))
        created.append(add_cube(
            f"kfr_silhouette_boost_001_{side}_boot_front_toe_slab_booster",
            loc=(x, -16.0, 5.8),
            dims=(15.0, 6.0, 6.0),
            mat=mat_boot,
            col=col,
            bevel=0.8,
        ))
        created.append(add_cube(
            f"kfr_silhouette_boost_001_{side}_boot_wide_sole_booster",
            loc=(x, -3.0, 1.0),
            dims=(18.5, 28.0, 2.0),
            mat=mat_sole,
            col=col,
            bevel=0.6,
        ))

    # Center crotch/shorts shadow to stop the legs reading as separate posts attached to a box.
    created.append(add_cube(
        "kfr_silhouette_boost_001_center_pelvis_shadow_gap",
        loc=(0.0, -7.2, 49.5),
        dims=(7.5, 1.2, 9.0),
        mat=mat_shadow,
        col=col,
        bevel=0.35,
    ))

    return created


def build_tail_root_integration(col, mat_mid, mat_shadow):
    created = []

    # Does not replace the original tail. This just integrates the socket/root better.
    created.append(add_cube(
        "kfr_silhouette_boost_001_tail_root_pelvis_saddle",
        loc=(0.0, 10.6, 53.5),
        dims=(15.5, 5.0, 8.5),
        mat=mat_mid,
        col=col,
        rotation=(math.radians(-8.0), 0.0, 0.0),
        bevel=0.9,
    ))
    created.append(add_cube(
        "kfr_silhouette_boost_001_tail_socket_shadow_break",
        loc=(0.0, 8.2, 54.0),
        dims=(13.0, 1.0, 6.5),
        mat=mat_shadow,
        col=col,
        rotation=(math.radians(-8.0), 0.0, 0.0),
        bevel=0.3,
    ))

    return created

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

def main():
    log("Starting silhouette boost 001")

    col = make_collection(ROOT_COLLECTION_NAME)
    mat_jacket_dark = make_material("kfr_silhouette_boost_001_jacket_dark", MAT_JACKET_DARK)
    mat_jacket_mid = make_material("kfr_silhouette_boost_001_jacket_mid", MAT_JACKET_MID)
    mat_pants = make_material("kfr_silhouette_boost_001_pants_mass", MAT_PANTS)
    mat_boot = make_material("kfr_silhouette_boost_001_boot_black", MAT_BOOT)
    mat_sole = make_material("kfr_silhouette_boost_001_sole_gray", MAT_SOLE)
    mat_glove = make_material("kfr_silhouette_boost_001_glove_black", MAT_GLOVE)
    mat_gear = make_material("kfr_silhouette_boost_001_gear_gray", MAT_GEAR)
    mat_shadow = make_material("kfr_silhouette_boost_001_shadow_dark", MAT_SHADOW)

    created = []
    created.extend(build_jacket_and_torso(col, mat_jacket_dark, mat_jacket_mid, mat_shadow, mat_gear))
    created.extend(build_arms_gloves(col, mat_glove, mat_jacket_mid))
    created.extend(build_legs_and_boots(col, mat_pants, mat_shadow, mat_boot, mat_sole))
    created.extend(build_tail_root_integration(col, mat_jacket_mid, mat_shadow))

    log(f"Created silhouette boost objects: {len(created)}")
    for obj in created:
        log(f"  created: {obj.name}")

    log("SILHOUETTE BOOST 001 COMPLETE")
    log("Save as: kfr_blockout_v002_silhouette_boost_pass_001.blend")
    log("Review: front full-body, side full-body, three-quarter shelf view, boots/legs close-up, torso close-up.")


if __name__ == "__main__":
    main()
