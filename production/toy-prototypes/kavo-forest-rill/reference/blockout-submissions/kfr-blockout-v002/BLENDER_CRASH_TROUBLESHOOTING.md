# Blender Crash Troubleshooting — KFR-BLOCKOUT-v002

**Status:** Blender closed unexpectedly when running the starter scripts.  
**Immediate response:** Stop running the full / lite scripts until the smoke test passes.

---

## Diagnostic Order

Run scripts in this order:

1. `kfr_blender_crash_diagnostic_smoke_test.py`
2. `create_kfr_blockout_v002_lite_safe_scene.py`
3. `create_kfr_blockout_v002_starter_scene.py`

Do not run step 2 until step 1 succeeds.
Do not run step 3 until step 2 succeeds.

---

## Smoke Test Meaning

The smoke test creates only one cube using raw mesh data.

If the smoke test succeeds, Blender can run basic Python scene creation.

If the smoke test crashes Blender, the issue is probably not the Kavo script. Check:

- Blender install
- graphics driver
- Wayland / X11 session issues on Linux
- add-on conflict
- corrupted startup file
- Python console errors
- system memory / GPU instability

---

## Recommended Local Test Launch

On Linux, try starting Blender from a terminal so the crash leaves a message behind:

```bash
blender --factory-startup
```

Then run the smoke test from the Scripting workspace.

If it crashes, try:

```bash
blender --factory-startup --debug-all
```

Copy the last 30 to 60 terminal lines into the project chat for diagnosis.

---

## If Smoke Test Passes

Run:

`create_kfr_blockout_v002_lite_safe_scene.py`

Then immediately save as:

`kfr_blockout_v002_lite_safe_starter_scene.blend`

Do not run the full starter script until the Lite script has saved successfully.

---

## If Lite Script Crashes But Smoke Test Passes

Likely cause is one of:

- too many created objects for the current setup
- a primitive creation call causing instability
- a collection or viewport update problem
- camera setup instability

Next fix should be a staged builder split into separate scripts:

1. scale / ground only
2. boots / legs only
3. pelvis / tail only
4. torso / garments only
5. head only
6. arms / watch only
7. joints / cameras only

---

## Do Not Keep Re-running a Crashing Script

Repeated crash loops risk corrupting unsaved files or hiding the actual error.

Run the smoke test first, then continue one stage at a time.
