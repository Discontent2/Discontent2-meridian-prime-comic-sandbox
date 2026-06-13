"""
KFR-BLOCKOUT-v002 Phase 3 Sculpt Cleanup Brief

This script records the current production decision:
KFR-BLOCKOUT-v002 is approved to advance out of rough automated blockout and into
sculpt-aware cleanup, but not into final detail sculpt yet.

Run in Blender if desired. It creates a Text data block containing the brief so
it travels with the .blend file. It also prints the brief to the console.
"""

BRIEF_TEXT = """
KFR-BLOCKOUT-v002 PHASE 3 SCULPT CLEANUP BRIEF

Verdict
-------
It is not too early to move into the next phase.

The next phase should not be final detail sculpting yet. The correct next phase is:

PHASE 3: SCULPT-AWARE CLEANUP / COHESIVE BLOCKOUT REFINEMENT

Current Approval State
----------------------
Ready to leave rough automated blockout: YES
Ready for final sculpt / detail sculpt: NO
Ready for sculpt-aware cleanup: YES

Why We Are Moving Forward
-------------------------
The model now contains enough information to sculpt from. More automated booster
scripts are likely to create clutter, stacked forms, and competing silhouette
pieces. The v002 figure has crossed the threshold where manual cleanup will help
more than additional blockout patching.

What Is Working
---------------
- Forest reads as a Kavo-style figure rather than a human figure.
- The watch is present and correctly placed on the left wrist.
- The jacket / harness / pants language is visible enough to refine.
- The tail is back to the stronger original silhouette.
- The lower body is more grounded than the earlier straight-post version.
- The front view has enough character landmarks to continue.

What Still Needs Cleanup Before Final Detail
--------------------------------------------
- The silhouette is better, but still too box-stacked.
- Jacket, harness, and torso need to become one believable garment system.
- Shoulders are improved but still blocky.
- Pants panels need to be sculpted into the legs instead of reading as pasted-on plates.
- Boots are acceptable for now, but proportions remain clunky.
- Tail needs a later redesign with dermal plates and articulation logic.
- Head, snout, and quills are acceptable only as placeholder direction.
- Hands remain symbolic placeholders and need their own pass later.

Phase 3 Action Plan
-------------------
1. Duplicate the current Blender file.
2. Save the duplicate as:
   kfr_blockout_v002_sculpt_cleanup_pass_001.blend
3. Keep the accepted silhouette boost collection visible as reference.
4. Hide or delete failed tail-fix experiments.
5. Begin manual sculpt-aware cleanup by unifying these systems visually:
   - jacket into torso
   - harness into jacket
   - pants panels into legs
   - cuffs into arms
   - boots into lower stance
   - tail socket into pelvis

Phase Goal
----------
The next goal is cohesion, not detail.

Make the figure read as one designed toy prototype instead of a stack of separate
blockout parts. The model should feel like Forest Rill before surface detail,
texture, wrinkles, seams, and final accessory polish are added.

Locked Status Note
------------------
KFR-BLOCKOUT-v002: approved to advance into sculpt-aware cleanup.
Do not proceed to final detail sculpt yet.
Next target: cohesive v002.5 cleanup sculpt with unified garment, improved
silhouette, and preserved toy articulation logic.

Recommended Review Package After Cleanup Pass 001
-------------------------------------------------
Send screenshots for:
- front full-body
- side full-body
- back full-body
- three-quarter shelf view
- torso / harness close-up
- legs / boots close-up
- tail socket close-up
- watch / left wrist close-up
"""

TEXT_BLOCK_NAME = "KFR_PHASE_3_SCULPT_CLEANUP_BRIEF"
OUTPUT_BLEND_NAME = "kfr_blockout_v002_sculpt_cleanup_pass_001.blend"


def print_brief():
    print("=" * 72)
    print(BRIEF_TEXT.strip())
    print("=" * 72)


def create_blender_text_block():
    try:
        import bpy
    except Exception:
        print("Blender bpy module not available. Printing brief only.")
        return None

    existing = bpy.data.texts.get(TEXT_BLOCK_NAME)
    if existing:
        existing.clear()
        text_block = existing
    else:
        text_block = bpy.data.texts.new(TEXT_BLOCK_NAME)

    text_block.write(BRIEF_TEXT.strip() + "\n")
    print(f"Created or updated Blender Text data block: {TEXT_BLOCK_NAME}")
    print(f"Recommended save-as: {OUTPUT_BLEND_NAME}")
    return text_block


def main():
    print_brief()
    create_blender_text_block()


if __name__ == "__main__":
    main()
