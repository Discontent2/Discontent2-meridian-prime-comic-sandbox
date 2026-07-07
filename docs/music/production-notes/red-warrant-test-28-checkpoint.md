# Red Warrant Test 28 Checkpoint

**Status:** Sandbox Production Notes / Non-Canon Until Promoted  
**Track:** Red Warrant  
**Artist:** Pit ROM  
**Checkpoint date:** 2026-07-07  

## Summary

Test 28 is the current saved working checkpoint before continuing non-Codex lead guitar improvements.

The stable foundation is based on the Test 24/25 line:

- FM1 bass problem addressed with the refined Sub Anchor approach.
- FM5 percussion/noise problem addressed with refined dry hat/open hat/crash handling.
- Rhythm wall is usable enough to preserve.
- FM4 lead is the current active development target.

## Test 28 Lead Lab Notes

Codex parsed the transferred Test 26 and Test 27 files directly and created Test 28 as an FM4 lead development lab.

Most important listening targets:

- Order 07: `RW FM4 Lead Mid Bite` cut-through test.
- Order 10: Mid Bite final context with narrow FM3 duck.
- Order 11: Mid Bite final context with wide FM3 duck.
- Order 12: Mid Bite final context with narrow FM3 duck.
- Order 13: Mid Bite final context with wide FM3 duck.
- Order 14: Mid Bite final context with wide FM3 duck.
- Order 03 vs 05: Dark family without vs with wide FM3 duck.

## Test 28 Identity

Canonical artifact in this checkpoint:

- `docs/music/dmf-checkpoints/red_warrant_test_28_download_fix.dmf.b64`

Restore command:

```sh
base64 -d docs/music/dmf-checkpoints/red_warrant_test_28_download_fix.dmf.b64 > red_warrant_test_28_download_fix.dmf
```

Expected SHA256 of restored DMF:

```text
6f35c7a0d6338cea7a027ef40f59a7932e5644562ad8a1ef4e6d3b84a7cd06a0
```

## Next Non-Codex Improvement Direction

Do not disturb FM1 or FM5 unless listening proves they regressed.

Next manual tests should focus on:

1. Whether Mid Bite is better than Dark Sustain.
2. Whether narrow or wide FM3 ducking preserves rhythm impact better.
3. Whether FM4 needs more mid bite, more sustain, or less phrase density.
4. Whether pinch harmonic and dive tail should remain accents only.

## Guardrails

- No live `11xx` feedback writes.
- No Algorithm 7 lead guitar.
- No broad `12xx-15xx` TL sweeps.
- No samples.
- No wavetables.
- FM4 is the lead lane.
- FM1 and FM5 are stable foundation lanes.
