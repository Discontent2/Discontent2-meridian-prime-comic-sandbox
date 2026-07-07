# Red Warrant VGM to DMF Toolchain

This folder records the Red Warrant VGM-to-DMF toolchain checkpoint created during Test 28A / Test 29 preparation.

Current local source scripts created in the working artifact bundle:

1. `red_warrant_vgm_register_lens.py`
2. `red_warrant_channel_role_report.py`
3. `red_warrant_grid_quantizer.py`
4. `red_warrant_collision_resolver.py`
5. `red_warrant_pattern_finder.py`
6. `red_warrant_dmf_model.py`
7. `red_warrant_dmf_packer.py`
8. `red_warrant_dmf_audit.py`

Pipeline order:

```sh
python red_warrant_vgm_register_lens.py input.vgm --out-dir lens --prefix test2 --dump-tfi --keep-writes
python red_warrant_channel_role_report.py lens --prefix test2
python red_warrant_grid_quantizer.py lens --prefix test2 --out-dir work --bpm 167 --rows-per-beat 4 --max-orders 16
python red_warrant_collision_resolver.py work/test2_quantized_grid.json --role-report test2_channel_role_report.json --out-dir work --prefix test2
python red_warrant_pattern_finder.py work/test2_resolved_grid.json --out-dir work --prefix test2_resolved
python red_warrant_dmf_model.py work/test2_resolved_pattern_plan.json --out work/test2_resolved_dmf_model.json --song-name "Red Warrant Import"
python red_warrant_dmf_packer.py --model-json work/test2_resolved_dmf_model.json --out work/test2_resolved_import.dmf
python red_warrant_dmf_audit.py work/test2_resolved_import.dmf
```

Resolved demo smoke-test result:

```text
Input quantized events: 6,747
Resolved events: 1,208
Dropped events: 5,539
Packed DMF audit: OK
Resolved demo DMF SHA256: 888af768e6b5bf42db5339af0e21fc57bd72251075d1b052533e56ffa9540b95
```

Restore/source note:

The generated source bundle was also provided in the working artifact as `red_warrant_vgm_to_dmf_toolchain_with_resolver.zip`. The earlier register lens source was separately checkpointed as `docs/music/tools/red_warrant_vgm_register_lens.py.gz.b64` on this branch.

Important limitation of this repo checkpoint:

The individual `.py` files exist as downloadable working artifacts in the active session. This README records the repo-side checkpoint. The next repo pass should commit the individual plain `.py` files under this folder when a direct file-content commit path is available.
