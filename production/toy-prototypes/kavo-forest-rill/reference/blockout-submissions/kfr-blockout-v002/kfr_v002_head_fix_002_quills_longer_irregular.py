"""
KFR-BLOCKOUT-v002 Head Fix 002 — Longer Irregular Proto-Quills

Run this after Head Fix 001.

Purpose:
    Replace the Head Fix 001 quills with a longer, more irregular front-to-back crest.

Changes:
    - Hides Head Fix 001 quill objects.
    - Adds 7 front-to-back quills instead of 5.
    - Makes the quills longer and more varied.
    - Keeps them blunt and thick enough for toy / print safety.
    - Adds slight X offsets so they feel organic rather than ruler-straight.

This does not change:
    - snout wedge
    - brow mass
    - mouth marker
    - shades
    - body or garments

Recommended file before running:
    kfr_blockout_v002_head_fix_pass_001.blend

Recommended file after running:
    kfr_blockout_v002_head_fix_pass_002.blend
"""

import math
import bpy

ROOT_COLLECTION_NAME = "kfr_blockout_v002_head_fix_002_quills"

# Coordinate convention:
# X = left / right
# Y = front / back, negative Y is front, positive Y is back
# Z = up


def make_collection(name):
    existing = bpy.data.collections.get(name)
    if existing:
        return existing
    col = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(col)
    return col


def make_material(name, color):
    existing = bpy.data.materials.get(name)
    if existing:
        return existing
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = color
    return mat


def hide_matching_objects(patterns, suffix="_pre_headfix002_hidden"):
    hidden = []
    for obj in list(bpy.data.objects):
        if any(pattern in obj.name for pattern in patterns):
            if not obj.name.endswith(suffix):
                obj.name = obj.name + suffix
            obj.hide_viewport = True
            obj.hide_render = True
            hidden.append(obj.name)
    return hidden


def link_to_collection(obj, col):
    try:
        col.objects.link(obj)
    except RuntimeError:
        pass


def add_blunt_quill(name, loc, height, base_radius, tip_radius, lean_degrees, twist_degrees, mat, col):
    """Create one longer blunt cone leaned backward, with slight organic twist."""
    bpy.ops.mesh.primitive_cone_add(
        vertices=18,
        radius1=base_radius,
        radius2=tip_radius,
        depth=height,
        location=loc,
        rotation=(math.radians(-lean_degrees), 0.0, math.radians(twist_degrees)),
    )
    obj = bpy.context.object
    obj.name = name
    obj.data.name = name + "_mesh"
    obj.data.materials.append(mat)
    link_to_collection(obj, col)
    return obj


def apply_head_fix_002():
    print("KFR v002 Head Fix 002: longer irregular quills starting")

    col = make_collection(ROOT_COLLECTION_NAME)
    mat_quill = make_material("kfr_headfix002_longer_irregular_red_proto_quills", (0.62, 0.18, 0.10, 1.0))

    hidden = hide_matching_objects([
        "kfr_short_sparse_proto_quill_headfix001",
        "kfr_short_sparse_proto_quill_headfix002",
    ])
    print("Hidden previous head-fix quills:", hidden)

    # Longer, irregular, front-to-back crest.
    # loc = (x offset, y position front/back, z center)
    # height stays print-safe but has enough silhouette to read.
    quills = [
        # label        x      y      z      height  base  tip   lean  twist
        ("front_low", -0.35, -6.2, 123.0, 3.8,    1.05, 0.55, 17,   -8),
        ("front_mid",  0.25, -3.8, 124.0, 4.9,    1.22, 0.62, 21,    5),
        ("tall_01",   -0.20, -1.0, 125.2, 6.0,    1.38, 0.72, 24,   -4),
        ("tall_02",    0.30,  1.8, 125.8, 6.6,    1.48, 0.78, 27,    7),
        ("ragged_mid",-0.45,  4.4, 125.2, 5.5,    1.34, 0.68, 29,   -6),
        ("back_mid",   0.20,  6.8, 124.4, 4.7,    1.22, 0.62, 31,    4),
        ("back_low",  -0.15,  9.0, 123.4, 3.6,    1.05, 0.55, 33,   -3),
    ]

    for label, x, y, z, height, base_radius, tip_radius, lean, twist in quills:
        add_blunt_quill(
            name=f"kfr_short_sparse_proto_quill_headfix002_{label}",
            loc=(x, y, z),
            height=height,
            base_radius=base_radius,
            tip_radius=tip_radius,
            lean_degrees=lean,
            twist_degrees=twist,
            mat=mat_quill,
            col=col,
        )

    print("KFR v002 Head Fix 002 complete.")
    print("Save as: kfr_blockout_v002_head_fix_pass_002.blend")
    print("Next review screenshots: head close-up, front view, side view.")


if __name__ == "__main__":
    apply_head_fix_002()
