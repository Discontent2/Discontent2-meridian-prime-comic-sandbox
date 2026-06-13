"""
Kavo "Forest" Rill
KFR-BLOCKOUT-v004 Visibility Rescue / Unhide Everything 001

Purpose:
    If a rebuild script hides Forest or crashes after hiding old work, run this.
    It does not delete or reshape anything. It only restores visibility.

Run:
    Open the working .blend, paste/run this script in Blender's Python editor.

What it does:
    - Unhides every collection containing KFR, Forest, Blockout, or Kavo.
    - Unhides all objects inside those collections.
    - Also unhides every object in the scene as a safety net.
    - Selects likely Forest root objects so you can press Home / Frame Selected.
"""

import bpy

KEYWORDS = ["kfr", "forest", "blockout", "kavo", "rill"]


def ensure_object_mode():
    if bpy.context.object and bpy.context.object.mode != "OBJECT":
        bpy.ops.object.mode_set(mode="OBJECT")


def matches(name):
    low = name.lower()
    return any(k in low for k in KEYWORDS)


def unhide_collection_tree(col):
    col.hide_viewport = False
    col.hide_render = False
    for obj in col.objects:
        obj.hide_set(False)
        obj.hide_viewport = False
        obj.hide_render = False
    for child in col.children:
        unhide_collection_tree(child)


def main():
    ensure_object_mode()

    touched_cols = []
    touched_objs = []

    # First restore targeted KFR / Forest / Kavo collections.
    for col in bpy.data.collections:
        if matches(col.name):
            unhide_collection_tree(col)
            touched_cols.append(col.name)

    # Then restore all objects as a safety net. This is rescue mode, not polish mode.
    for obj in bpy.data.objects:
        try:
            obj.hide_set(False)
        except Exception:
            pass
        obj.hide_viewport = False
        obj.hide_render = False
        touched_objs.append(obj.name)

    bpy.ops.object.select_all(action="DESELECT")

    selected = []
    priority_words = ["root", "v0043", "v0042", "v0041", "v004", "forest", "kfr"]
    for obj in bpy.data.objects:
        if matches(obj.name) and any(word in obj.name.lower() for word in priority_words):
            obj.select_set(True)
            selected.append(obj.name)
            if bpy.context.view_layer.objects.active is None:
                bpy.context.view_layer.objects.active = obj

    if selected:
        bpy.context.view_layer.objects.active = bpy.data.objects[selected[0]]

    print("KFR visibility rescue complete.")
    print(f"Collections restored: {len(touched_cols)}")
    print(f"Objects unhidden: {len(touched_objs)}")
    print("Press Home or View > Frame Selected if Forest is off-screen.")
    print("No objects were deleted or modified beyond visibility flags.")


if __name__ == "__main__":
    main()
