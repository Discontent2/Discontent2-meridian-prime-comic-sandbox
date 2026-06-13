"""
Kavo "Forest" Rill
Mondo Scan Reference Import 001

Purpose:
    Import Mondo.zip as a textured reference shell inside Blender so we can use
    the real toy proportions as a sculptural guide for Forest.

What this does:
    - Finds Mondo.zip in common local places or beside the current .blend.
    - Extracts model.glb plus texture maps to a local _kfr_mondo_scan_extract folder.
    - Imports the GLB.
    - Moves it into a safe reference collection.
    - Recenters it near the origin.
    - Scales it to 127 mm tall using the imported mesh Z height.
    - Adds a 127 mm height guide and footprint guide.
    - Does NOT hide, delete, or modify existing Forest versions.

Before running:
    Put Mondo.zip in one of these places:
        1. The same folder as your open .blend
        2. Your Downloads folder
        3. Your Documents folder
    Or edit MONDO_ZIP_PATH below to the exact file path.

Save as:
    kfr_mondo_scan_reference_import_001.blend
"""

import os
import zipfile
from pathlib import Path

import bpy
from mathutils import Vector

COLLECTION_NAME = "KFR_MONDO_SCAN_REFERENCE_001"
ROOT_NAME = "kfr_mondo_scan_reference_root"
NOTES_NAME = "KFR_MONDO_SCAN_REFERENCE_NOTES"

TARGET_HEIGHT_M = 0.127
MONDO_ZIP_PATH = ""  # Optional: paste exact path here, for example r"C:\\Users\\You\\Downloads\\Mondo.zip"

MAT_GUIDE = (0.12, 0.12, 0.12, 1.0)
MAT_FLOOR = (0.50, 0.50, 0.50, 0.20)


def ensure_object_mode():
    if bpy.context.object and bpy.context.object.mode != "OBJECT":
        bpy.ops.object.mode_set(mode="OBJECT")


def make_mat(name, color, roughness=0.7, alpha=False):
    mat = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    mat.use_nodes = True
    mat.diffuse_color = color
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        if "Base Color" in bsdf.inputs:
            bsdf.inputs["Base Color"].default_value = color
        if "Roughness" in bsdf.inputs:
            bsdf.inputs["Roughness"].default_value = roughness
        if "Alpha" in bsdf.inputs:
            bsdf.inputs["Alpha"].default_value = color[3]
    if alpha or color[3] < 1.0:
        mat.blend_method = "BLEND"
        if hasattr(mat, "show_transparent_back"):
            mat.show_transparent_back = True
    return mat


def link_to_col(obj, col):
    for user_col in list(obj.users_collection):
        user_col.objects.unlink(obj)
    col.objects.link(obj)
    return obj


def clean_or_create_collection(name):
    col = bpy.data.collections.get(name)
    if col is None:
        col = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(col)
    else:
        # Clean only our previous import objects, not Forest.
        for obj in list(col.objects):
            bpy.data.objects.remove(obj, do_unlink=True)
    col.hide_viewport = False
    col.hide_render = False
    return col


def find_mondo_zip():
    candidates = []

    if MONDO_ZIP_PATH.strip():
        candidates.append(Path(MONDO_ZIP_PATH.strip()).expanduser())

    blend_path = bpy.data.filepath
    if blend_path:
        blend_dir = Path(blend_path).parent
        candidates.extend([
            blend_dir / "Mondo.zip",
            blend_dir / "mondo.zip",
        ])

    home = Path.home()
    candidates.extend([
        home / "Downloads" / "Mondo.zip",
        home / "Downloads" / "mondo.zip",
        home / "Documents" / "Mondo.zip",
        home / "Documents" / "mondo.zip",
        Path.cwd() / "Mondo.zip",
        Path.cwd() / "mondo.zip",
    ])

    seen = set()
    for p in candidates:
        if str(p) in seen:
            continue
        seen.add(str(p))
        if p.exists() and p.is_file():
            return p

    raise FileNotFoundError(
        "Could not find Mondo.zip. Put it beside the .blend, in Downloads, "
        "or edit MONDO_ZIP_PATH at the top of this script."
    )


def extract_zip(zip_path):
    base_dir = Path(bpy.data.filepath).parent if bpy.data.filepath else zip_path.parent
    extract_dir = base_dir / "_kfr_mondo_scan_extract"
    extract_dir.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(zip_path, "r") as zf:
        names = zf.namelist()
        zf.extractall(extract_dir)

    model_path = extract_dir / "model.glb"
    if not model_path.exists():
        glbs = list(extract_dir.glob("*.glb"))
        if not glbs:
            raise FileNotFoundError("Mondo.zip did not contain model.glb or another .glb file.")
        model_path = glbs[0]

    return extract_dir, model_path, names


def bounds_for_objects(objects):
    pts = []
    for obj in objects:
        if obj.type != "MESH":
            continue
        for corner in obj.bound_box:
            pts.append(obj.matrix_world @ Vector(corner))
    if not pts:
        raise RuntimeError("No mesh bounds found after import.")
    mn = Vector((min(p.x for p in pts), min(p.y for p in pts), min(p.z for p in pts)))
    mx = Vector((max(p.x for p in pts), max(p.y for p in pts), max(p.z for p in pts)))
    return mn, mx


def add_empty(name, loc, col):
    bpy.ops.object.empty_add(type="PLAIN_AXES", location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.empty_display_size = 0.006
    return link_to_col(obj, col)


def add_cylinder_between(name, a, b, radius, mat, col, parent=None, vertices=12):
    a = Vector(a)
    b = Vector(b)
    vec = b - a
    mid = a + vec * 0.5
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=vec.length, location=mid)
    obj = bpy.context.object
    obj.name = name
    obj.rotation_euler = vec.to_track_quat("Z", "Y").to_euler()
    obj.data.materials.append(mat)
    if parent:
        obj.parent = parent
    return link_to_col(obj, col)


def add_cube(name, loc, scale, mat, col, parent=None):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    obj.data.materials.append(mat)
    if parent:
        obj.parent = parent
    return link_to_col(obj, col)


def import_mondo_reference(model_path, col, root):
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=str(model_path))
    after = set(bpy.data.objects)
    imported = list(after - before)

    if not imported:
        raise RuntimeError("GLB import produced no objects.")

    for obj in imported:
        link_to_col(obj, col)
        obj.parent = root
        obj.name = "kfr_mondo_scan_ref_" + obj.name
        obj.hide_viewport = False
        obj.hide_render = False
        if obj.type == "MESH":
            obj.show_in_front = True
            try:
                for poly in obj.data.polygons:
                    poly.use_smooth = True
            except Exception:
                pass

    bpy.context.view_layer.update()
    mn, mx = bounds_for_objects(imported)
    center = (mn + mx) * 0.5
    z_height = max(mx.z - mn.z, 0.000001)
    scale_factor = TARGET_HEIGHT_M / z_height

    # Parent-based normalization. Keep internal scan transforms intact.
    root.location = -center
    root.scale = (scale_factor, scale_factor, scale_factor)

    bpy.context.view_layer.update()
    mn2, mx2 = bounds_for_objects(imported)
    # Move ground to z=0 after scaling.
    root.location.z -= mn2.z

    bpy.context.view_layer.update()
    return imported, scale_factor


def add_guides(col, root):
    guide_mat = make_mat("KFR_MONDO_scan_guide_dark_gray", MAT_GUIDE, 0.7)
    floor_mat = make_mat("KFR_MONDO_translucent_floor_footprint", MAT_FLOOR, 0.8, True)

    add_cylinder_between(
        "kfr_mondo_127mm_height_guide",
        (-0.060, -0.040, 0.0),
        (-0.060, -0.040, TARGET_HEIGHT_M),
        0.00065,
        guide_mat,
        col,
        root,
        vertices=8,
    )
    add_cube(
        "kfr_mondo_47mm_stance_width_guide",
        (-0.020, 0.000, 0.0004),
        (0.001, 0.047 / 2, 0.00035),
        guide_mat,
        col,
        root,
    )
    floor = add_cube(
        "kfr_mondo_reference_floor_plate",
        (0.010, 0.000, -0.00035),
        (0.090, 0.055, 0.00025),
        floor_mat,
        col,
        root,
    )
    floor.display_type = "TEXTURED"


def write_notes(zip_path, extract_dir, model_path, names, scale_factor):
    text = bpy.data.texts.get(NOTES_NAME) or bpy.data.texts.new(NOTES_NAME)
    text.clear()
    text.write(
        "KFR Mondo Scan Reference Import 001\n\n"
        f"Source zip: {zip_path}\n"
        f"Extracted to: {extract_dir}\n"
        f"Model imported: {model_path}\n"
        f"Scale factor applied to root: {scale_factor:.8f}\n\n"
        "Zip contents:\n"
    )
    for name in names:
        text.write(f"- {name}\n")
    text.write(
        "\nUse this as a proportion/reference shell only. Do not treat raw scan geometry "
        "as final toy parts. Build clean Forest anatomy and clothing over/around it.\n"
    )


def frame_imported(imported):
    bpy.ops.object.select_all(action="DESELECT")
    active = None
    for obj in imported:
        if obj.type == "MESH":
            obj.select_set(True)
            active = obj
    if active:
        bpy.context.view_layer.objects.active = active


def main():
    ensure_object_mode()
    bpy.context.scene.unit_settings.system = "METRIC"
    bpy.context.scene.unit_settings.scale_length = 1.0
    bpy.context.scene.unit_settings.length_unit = "METERS"

    zip_path = find_mondo_zip()
    extract_dir, model_path, names = extract_zip(zip_path)

    col = clean_or_create_collection(COLLECTION_NAME)
    root = add_empty(ROOT_NAME, (0, 0, 0), col)

    imported, scale_factor = import_mondo_reference(model_path, col, root)
    add_guides(col, root)
    write_notes(zip_path, extract_dir, model_path, names, scale_factor)
    frame_imported(imported)

    print("KFR Mondo scan reference import complete.")
    print(f"Zip: {zip_path}")
    print(f"Collection: {COLLECTION_NAME}")
    print(f"Imported objects: {len(imported)}")
    print(f"Scale factor: {scale_factor:.8f}")
    print("No existing Forest collection was hidden or deleted.")
    print("Press Home / Frame Selected if the scan is off-screen.")


if __name__ == "__main__":
    main()
