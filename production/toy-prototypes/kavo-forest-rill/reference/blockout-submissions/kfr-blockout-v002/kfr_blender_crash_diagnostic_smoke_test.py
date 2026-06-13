"""
Kavo Blender Crash Diagnostic Smoke Test

Run this before any KFR-BLOCKOUT-v002 starter scene if Blender keeps closing.

This script creates only:
    - one collection
    - one cube
    - one plain material

If this crashes Blender, the issue is not the Kavo blockout scene.
It is likely Blender install, graphics driver, add-on conflict, Python environment, or session/display issue.
"""

import bpy

print("KFR smoke test starting")

# No scene reset. Keep default cube if present.
mat = bpy.data.materials.new("kfr_smoke_test_plain_gray")
mat.diffuse_color = (0.5, 0.5, 0.5, 1.0)

col = bpy.data.collections.new("kfr_smoke_test_collection")
bpy.context.scene.collection.children.link(col)

mesh = bpy.data.meshes.new("kfr_smoke_test_cube_mesh")
verts = [
    (-1, -1, -1),
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, 1, 1),
]
faces = [
    (0, 1, 2, 3),
    (4, 7, 6, 5),
    (0, 4, 5, 1),
    (1, 5, 6, 2),
    (2, 6, 7, 3),
    (3, 7, 4, 0),
]
mesh.from_pydata(verts, [], faces)
mesh.update()
obj = bpy.data.objects.new("kfr_smoke_test_cube", mesh)
obj.data.materials.append(mat)
col.objects.link(obj)

print("KFR smoke test complete. If you can see kfr_smoke_test_cube, Blender can run a minimal script.")
