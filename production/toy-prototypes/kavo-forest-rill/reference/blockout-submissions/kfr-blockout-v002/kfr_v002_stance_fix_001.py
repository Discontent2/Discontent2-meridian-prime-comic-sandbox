"""
KFR-BLOCKOUT-v002
STANCE FIX 001
Leg + feet correction pass

Purpose:
- Feet slightly farther apart
- Feet slightly splayed outward
- Knees slightly bent
- More relaxed / ready stance
- Preserve blockout simplicity

Recommended before running:
- Save current file first

Recommended after running:
- Save as: kfr_blockout_v002_stance_fix_pass_001.blend

If auto-detection fails:
- Fill in EXPLICIT_NAMES with exact object names from the Outliner
"""

import bpy
import math
from mathutils import Vector, Matrix

# =========================================================
# USER SETTINGS
# =========================================================

EXPLICIT_NAMES = {
    # Fill these only if auto-detection fails
    "left_foot": "",
    "right_foot": "",
    "left_shin": "",
    "right_shin": "",
    "left_thigh": "",
    "right_thigh": "",
}

# Core stance changes
FOOT_SPREAD_MM = 2.5       # move each foot outward
FOOT_SPLAY_DEG = 6.0       # rotate toes outward
KNEE_BEND_DEG = 5.0        # bend knees slightly
THIGH_COMPENSATE_DEG = 2.0 # slight thigh settle so legs read naturally

# If something bends the wrong way, flip these
SPLAY_DIRECTION_MULT = 1.0
KNEE_DIRECTION_MULT = 1.0
THIGH_DIRECTION_MULT = 1.0

GROUND_Z = 0.0

FOOT_HINTS = ["boot", "foot", "shoe"]
SHIN_HINTS = ["shin", "lower_leg", "calf"]
THIGH_HINTS = ["thigh", "upper_leg", "leg_upper"]

EXCLUDE_HINTS = [
    "camera", "cam_", "light", "ground", "plane", "guide", "marker",
    "text", "label", "tail", "watch", "harness", "goggle", "shade"
]

# =========================================================
# HELPERS
# =========================================================

def log(msg):
    print(f"[KFR STANCE FIX] {msg}")

def valid_mesh(obj):
    if obj.type != "MESH":
        return False
    low = obj.name.lower()
    if any(tok in low for tok in EXCLUDE_HINTS):
        return False
    return True

def obj_origin_world(obj):
    return obj.matrix_world.translation.copy()

def world_bbox_points(obj):
    return [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]

def bbox_min_z(obj):
    pts = world_bbox_points(obj)
    return min(p.z for p in pts)

def bbox_top_center(obj):
    pts = world_bbox_points(obj)
    min_x = min(p.x for p in pts)
    max_x = max(p.x for p in pts)
    min_y = min(p.y for p in pts)
    max_y = max(p.y for p in pts)
    max_z = max(p.z for p in pts)
    return Vector(((min_x + max_x) / 2.0, (min_y + max_y) / 2.0, max_z))

def bbox_bottom_center(obj):
    pts = world_bbox_points(obj)
    min_x = min(p.x for p in pts)
    max_x = max(p.x for p in pts)
    min_y = min(p.y for p in pts)
    max_y = max(p.y for p in pts)
    min_z = min(p.z for p in pts)
    return Vector(((min_x + max_x) / 2.0, (min_y + max_y) / 2.0, min_z))

def move_world(obj, delta):
    obj.location += delta

def rotate_about_world_pivot(obj, angle_radians, axis, pivot_world):
    rot = Matrix.Rotation(angle_radians, 4, axis)
    t1 = Matrix.Translation(pivot_world)
    t2 = Matrix.Translation(-pivot_world)
    obj.matrix_world = t1 @ rot @ t2 @ obj.matrix_world

def plant_to_ground(obj, ground_z=0.0):
    min_z = bbox_min_z(obj)
    delta_z = ground_z - min_z
    move_world(obj, Vector((0.0, 0.0, delta_z)))

def find_by_exact(name):
    if not name:
        return None
    return bpy.data.objects.get(name)

def find_candidates(tokens):
    found = []
    for obj in bpy.data.objects:
        if not valid_mesh(obj):
            continue
        low = obj.name.lower()
        if any(tok in low for tok in tokens):
            found.append(obj)
    return found

def choose_left_right(candidates):
    if len(candidates) < 2:
        return None, None
    ordered = sorted(candidates, key=lambda o: obj_origin_world(o).x)
    return ordered[0], ordered[-1]

def get_pair(left_key, right_key, hints):
    left_obj = find_by_exact(EXPLICIT_NAMES[left_key])
    right_obj = find_by_exact(EXPLICIT_NAMES[right_key])

    if left_obj and right_obj:
        return left_obj, right_obj

    candidates = find_candidates(hints)
    if len(candidates) < 2:
        return None, None

    auto_left, auto_right = choose_left_right(candidates)

    if left_obj is None:
        left_obj = auto_left
    if right_obj is None:
        right_obj = auto_right

    return left_obj, right_obj

# =========================================================
# MAIN
# =========================================================

def main():
    log("Starting KFR v002 stance fix...")

    left_foot, right_foot = get_pair("left_foot", "right_foot", FOOT_HINTS)
    left_shin, right_shin = get_pair("left_shin", "right_shin", SHIN_HINTS)
    left_thigh, right_thigh = get_pair("left_thigh", "right_thigh", THIGH_HINTS)

    if not left_foot or not right_foot:
        log("Could not find left/right foot.")
        log("Fill EXPLICIT_NAMES['left_foot'] and EXPLICIT_NAMES['right_foot'].")
        return

    if not left_shin or not right_shin:
        log("Could not find left/right shin.")
        log("Fill EXPLICIT_NAMES['left_shin'] and EXPLICIT_NAMES['right_shin'].")
        return

    log(f"Left foot:  {left_foot.name}")
    log(f"Right foot: {right_foot.name}")
    log(f"Left shin:  {left_shin.name}")
    log(f"Right shin: {right_shin.name}")

    if left_thigh and right_thigh:
        log(f"Left thigh:  {left_thigh.name}")
        log(f"Right thigh: {right_thigh.name}")
    else:
        log("Thigh objects not found. Script will continue without thigh compensation.")

    # -----------------------------------------------------
    # 1) Spread feet outward
    # -----------------------------------------------------
    move_world(left_foot, Vector((-FOOT_SPREAD_MM, 0.0, 0.0)))
    move_world(right_foot, Vector((FOOT_SPREAD_MM, 0.0, 0.0)))
    log(f"Moved feet outward by {FOOT_SPREAD_MM} mm per side.")

    # -----------------------------------------------------
    # 2) Splay feet outward
    # -----------------------------------------------------
    left_ankle = bbox_top_center(left_foot)
    right_ankle = bbox_top_center(right_foot)

    left_splay = math.radians(FOOT_SPLAY_DEG * SPLAY_DIRECTION_MULT)
    right_splay = math.radians(-FOOT_SPLAY_DEG * SPLAY_DIRECTION_MULT)

    rotate_about_world_pivot(left_foot, left_splay, 'Z', left_ankle)
    rotate_about_world_pivot(right_foot, right_splay, 'Z', right_ankle)

    log(f"Splayed feet outward by {FOOT_SPLAY_DEG} degrees.")

    # -----------------------------------------------------
    # 3) Bend shins slightly for knee bend
    # -----------------------------------------------------
    # Positive/negative may depend on model orientation.
    bend_angle = math.radians(KNEE_BEND_DEG * KNEE_DIRECTION_MULT)

    left_knee_pivot = bbox_top_center(left_shin)
    right_knee_pivot = bbox_top_center(right_shin)

    rotate_about_world_pivot(left_shin, bend_angle, 'X', left_knee_pivot)
    rotate_about_world_pivot(right_shin, bend_angle, 'X', right_knee_pivot)

    log(f"Applied shin knee bend: {KNEE_BEND_DEG} degrees.")

    # -----------------------------------------------------
    # 4) Optional slight thigh compensation
    # -----------------------------------------------------
    if left_thigh and right_thigh:
        thigh_angle = math.radians(THIGH_COMPENSATE_DEG * THIGH_DIRECTION_MULT)
        left_hip_pivot = bbox_top_center(left_thigh)
        right_hip_pivot = bbox_top_center(right_thigh)

        rotate_about_world_pivot(left_thigh, -thigh_angle, 'X', left_hip_pivot)
        rotate_about_world_pivot(right_thigh, -thigh_angle, 'X', right_hip_pivot)

        log(f"Applied thigh compensation: {THIGH_COMPENSATE_DEG} degrees.")

    # -----------------------------------------------------
    # 5) Re-plant boots to ground
    # -----------------------------------------------------
    plant_to_ground(left_foot, GROUND_Z)
    plant_to_ground(right_foot, GROUND_Z)

    log("Re-planted both feet to ground.")

    # -----------------------------------------------------
    # 6) Final notes
    # -----------------------------------------------------
    log("STANCE FIX COMPLETE")
    log("Recommended save-as:")
    log("kfr_blockout_v002_stance_fix_pass_001.blend")
    log("If the feet splay inward, flip SPLAY_DIRECTION_MULT = -1.0")
    log("If the knees bend backward/wrong way, flip KNEE_DIRECTION_MULT = -1.0")
    log("If the thighs overcompensate, reduce THIGH_COMPENSATE_DEG or set to 0.0")

if __name__ == "__main__":
    main()
