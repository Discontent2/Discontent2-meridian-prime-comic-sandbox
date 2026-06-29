# Enum Rage Engine / Suno Generation Findings

**Status:** Sandbox Production Note / Non-Canon Until Promoted  
**Artist:** Enum Rage Engine  
**Related Style Card:** `docs/music/bad-influence/style-cards/enum-rage-engine-style.md`  
**Related Profile:** `docs/music/collectives/enum-rage-engine.md`  
**Created:** 2026-06-29

---

## Purpose

This note patches lessons from Enum Rage Engine prompt testing into the music workspace so future Suno prompts stay aligned with the repo identity while avoiding unwanted short-loop behavior.

Enum Rage Engine should remain:

```text
Antisapian console music
lo-fi 16-bit industrial EBM
cheap cartridge sound
raw FM synths
fake chip drums
fixed BPM
fixed key center
no voices
no realistic drums
no hi-fi polish
```

---

## Main Finding

Short 30-second outputs are likely caused by prompt language that reads like a game-loop asset instead of a full cue.

Avoid overusing:

```text
loop
loopable
game loop
same groove full track
short cue
one-shot
background loop
sound effect
```

These words may encourage Suno to produce a short repeatable asset rather than a complete 1:30+ instrumental.

---

## Full-Length Cue Strategy

Use duration and cue-structure language instead of loop language.

Preferred language:

```text
full-length instrumental cue
minimum 1:30
target 1:45
2:00 to 2:30 duration
three minimal passes
hard ending after final pass
continues through timed sections
```

For Enum, timed structure should be minimal and should not create a polished modern arrangement.

Good structure language:

```text
0:00 intro pulse
0:20 main bass and chip drums
0:50 eerie FM lead enters
1:15 cold alien pad layer
1:35 hard ending after final pass
```

Use small texture additions rather than big changes.

Allowed small additions:

```text
pad layer
lead phrase enters
second pass
final pass
slightly thicker bass pulse
```

Avoid dramatic additions:

```text
breakdown
build-up
riser
drop
solo
bridge
key change
modulation sweep
```

---

## 16-Bit Sound Guidance

`Chiptune` alone can skew too cute, too 8-bit, or too bleepy.

For Enum, prefer:

```text
16-bit FM console audio
raw FM synths
Sega-style FM synths
square/FM bass pulse
fake chip kick blip
digital noise snare tick
thin metallic FM hat tick
low sample rate
bitcrushed
mono / near-mono arcade-cabinet mix
tiny speaker
no shiny highs
no modern polish
```

Avoid:

```text
cute 8-bit bleeps
bright platformer music
power-up sounds
coin sounds
laser zaps
hi-fi mix
modern polish
realistic drums
acoustic drums
live drummer feel
```

---

## Voice Control

Voice prevention should appear in both the main prompt and the exclude field.

Main prompt language:

```text
instrumental only
no voices
no vocals
no speech
```

Exclude language:

```text
voices
vocals
speech
vocal chops
choir
chants
sampled dialogue
announcement samples
field-tape voices
```

---

## Recommended Enum Prompt Pattern

```text
Enum Rage Engine, [Track Title]. Full-length instrumental cue, instrumental only, no voices, no vocals, no speech. Minimum 1:30, target 1:45. Slow 16-bit [mood] EBM, [BPM] fixed, one minor key, no tempo changes, no key changes. Primitive FM console audio, raw square/FM bass pulse, fake chip kick blip, digital noise snare tick, thin metallic FM hat tick, no realistic drums. Extremely lo-fi, dull mono arcade-cabinet mix, bitcrushed, low sample rate, tiny speaker, no shiny highs, no modern polish. Structure: 0:00 intro pulse, 0:20 main bass and chip drums, 0:50 eerie FM lead, 1:15 cold pad layer, 1:35 hard ending. [Scene imagery]. No loopable cue, no power-up sounds, no coin sounds, no laser zaps, no risers, no drops, no fills, no breakdowns, no pitch bends, no modulation, no samples, no choir, no cute bleeps, no real game names, no real artist names, no direct imitation.
```

---

## Recommended Exclude Field

```text
voices, vocals, speech, vocal chops, choir, chants, sampled dialogue, announcement samples, field-tape voices, realistic drums, acoustic drums, live drummer, hi-fi mix, modern polish, loopable cue, short loop, game loop, sound effect, one-shot, sample pack, power-up sounds, coin sounds, laser zaps, risers, drops, fills, breakdowns, pitch bends, modulation, key changes, tempo changes, cute 8-bit bleeps, real game names, real artist names, direct imitation
```

---

## Current Best Test Prompt

```text
Enum Rage Engine, Biosphere Error v3. Full-length instrumental cue, instrumental only, no voices, no vocals, no speech. Minimum 1:30, target 1:45. Slow 16-bit alien exploration EBM, 92 BPM fixed, one minor key, no tempo changes, no key changes. Primitive FM console audio, raw square/FM bass pulse, fake chip kick blip, digital noise snare tick, thin metallic FM hat tick, no realistic drums. Extremely lo-fi, dull mono arcade-cabinet mix, bitcrushed, low sample rate, tiny speaker, no shiny highs, no modern polish. Structure: 0:00 intro pulse, 0:20 main bass and chip drums, 0:50 eerie FM lead, 1:15 cold alien pad layer, 1:35 hard ending. Abandoned biome, wet metal corridor, subterranean ruins, black-screen console dread. No loopable cue, no power-up sounds, no coin sounds, no laser zaps, no risers, no drops, no fills, no breakdowns, no pitch bends, no modulation, no samples, no choir, no cute bleeps, no real game names, no real artist names, no direct imitation.
```

---

## Extension Workflow

If a generated seed is musically correct but too short, use Suno Extend rather than abandoning it.

Extension prompt pattern:

```text
Continue this same full-length Enum Rage Engine cue to at least 1:45. Keep 92 BPM fixed, same minor key, same raw FM bass, same fake chip drums, no voices, no vocals, no speech, no new instruments beyond a small cold pad layer, no fills, no drops, no risers, no hi-fi polish, no realistic drums. End hard after the final pass.
```

---

## Search Tags

```text
Enum Rage Engine
Suno generation findings
Suno prompt strategy
full-length instrumental cue
minimum 1:30
target 1:45
16-bit FM console audio
lo-fi chiptune
industrial EBM
no loopable cue
no voices
no realistic drums
fake chip drums
raw FM synths
Biosphere Error
Meridian Prime music
```
