# Enum Rage Engine Style Card

**Status:** Sandbox Music Style Card / Non-Canon Until Promoted  
**Artist Identity:** Enum Rage Engine  
**Primary Style:** lo-fi 16-bit industrial EBM / corrupted cartridge music  
**Related Profile:** `docs/music/collectives/enum-rage-engine.md`  
**Production Findings:** `docs/music/production-notes/enum-rage-engine-suno-generation-findings.md`  
**Created:** 2026-06-29

---

## Core Style

Enum Rage Engine creates primitive, ugly, fixed-pulse Antisapian console music from degraded 16-bit hardware textures, industrial EBM pulse, and broken arcade-board aggression.

This is not bright retro nostalgia. It is a damaged fight cartridge coughing through a tiny speaker.

---

## Reusable Style Box

```text
Enum Rage Engine, Antisapian console-music producer, extremely lo-fi 16-bit industrial EBM, corrupted cartridge music, fixed-tempo machine pulse, fixed minor key, full-length instrumental cue, raw FM synths, dirty square-wave bass, fake chip kick, digital snare tick, metallic chip hi-hat tick, simple FM arp, hostile FM lead phrase, mono feel, bitcrushed, tiny speaker, crushed dynamics, low sample rate, basement cartridge grime, damaged game-board mood, no voices, no vocals, no speech, no realistic drums, no hi-fi mix, no modern polish, no fills, no breakdowns, no drops, no pitch bends, no real artist names
```

---

## Under 1000 Characters Prompt Template

```text
Enum Rage Engine, [Track Title]. Full-length instrumental cue, instrumental only, no voices, no vocals, no speech. Minimum 1:30, target 1:45. Slow 16-bit [mood] EBM, [BPM] fixed, one minor key, no tempo changes, no key changes. Primitive FM console audio, raw square/FM bass pulse, fake chip kick blip, digital noise snare tick, thin metallic FM hat tick, no realistic drums. Extremely lo-fi, dull mono arcade-cabinet mix, bitcrushed, low sample rate, tiny speaker, no shiny highs, no modern polish. Structure: 0:00 intro pulse, 0:20 main bass/drums, 0:50 eerie FM lead, 1:15 cold pad layer, 1:35 clear ending. Avoid short-loop behavior, power-up sounds, coin sounds, laser zaps, risers, drops, fills, breakdowns, pitch bends, modulation, samples, choir, cute bleeps, real names, direct imitation.
```

---

## Sound Rules

Use:

```text
full-length instrumental cue
minimum 1:30
target 1:45
fixed BPM
fixed key center
square-wave bass
raw FM synths
cheap 16-bit cartridge sound
primitive FM console audio
fake chip kick
digital snare tick
metallic hi-hat tick
simple FM arp
hostile FM lead phrase
low sample rate
mono / near-mono feel
bitcrushed dynamics
extreme lo-fi mix
small texture additions across timed passes
clear ending after final pass
```

Avoid:

```text
voices
vocals
speech
choir
vocal chops
hi-fi drums
realistic drums
acoustic drums
live drummer feel
breakbeats
fills
breakdowns
risers
drops
pitch bends
modulation sweeps
key changes
tempo changes
cute chiptune
cheerful retro game music
modern EDM polish
loop language when a full-length cue is wanted
short cue language
power-up sounds
coin sounds
laser zaps
```

---

## Suno Duration Patch

Enum prompts should avoid short-loop wording when the goal is a full song-length cue. Testing suggests that words like `loop`, `loopable`, `same groove full track`, and `short cue` can encourage short outputs.

Preferred duration language:

```text
full-length instrumental cue
minimum 1:30
target 1:45
three minimal passes
clear ending after final pass
```

Preferred structure language:

```text
0:00 intro pulse
0:20 main bass and chip drums
0:50 eerie FM lead enters
1:15 cold pad layer
1:35 clear ending after final pass
```

This keeps Enum primitive and fixed while telling Suno to continue past short-loop length.

---

## Voice Control

Place voice prevention in both the main prompt and the exclude field.

Main prompt:

```text
instrumental only
no voices
no vocals
no speech
```

Exclude field:

```text
voices, vocals, speech, vocal chops, choir, chants, sampled dialogue, announcement samples
```

---

## Recommended Exclude Field

```text
voices, vocals, speech, vocal chops, choir, chants, sampled dialogue, announcement samples, realistic drums, acoustic drums, live drummer, hi-fi mix, modern polish, short loop, game loop, sound-effect cue, power-up sounds, coin sounds, laser zaps, risers, drops, fills, breakdowns, pitch bends, modulation, key changes, tempo changes, cute 8-bit bleeps, real game names, real artist names, direct imitation
```

---

## Visual / Cover Art Language

```text
blue-skinned Antisapian console producer
black irises
magenta pupils
teal tapetum glow
cracked arcade board
wet alley CRT glow
cartridge shell
pixel warning screen
blacklight console grime
exposed wires like nerves
cheap plastic buttons
basement machine altar
```

---

## First Saved Track

```text
Buried Pulse / Dumb Terminal Crawl
```

Song file:

```text
docs/music/songs/enum-rage-engine/buried-pulse-dumb-terminal-crawl.md
```

---

## Current Test Prompt

```text
Enum Rage Engine, Biosphere Error v3. Full-length instrumental cue, instrumental only, no voices, no vocals, no speech. Minimum 1:30, target 1:45. Slow 16-bit alien exploration EBM, 92 BPM fixed, one minor key, no tempo changes, no key changes. Primitive FM console audio, raw square/FM bass pulse, fake chip kick blip, digital noise snare tick, thin metallic FM hat tick, no realistic drums. Extremely lo-fi, dull mono arcade-cabinet mix, bitcrushed, low sample rate, tiny speaker, no shiny highs, no modern polish. Structure: 0:00 intro pulse, 0:20 main bass and chip drums, 0:50 eerie FM lead, 1:15 cold alien pad layer, 1:35 clear ending. Abandoned biome, wet metal corridor, subterranean ruins, black-screen console dread. Avoid short-loop behavior, no power-up sounds, no coin sounds, no laser zaps, no risers, no drops, no fills, no breakdowns, no pitch bends, no modulation, no samples, no choir, no cute bleeps, no real game names, no real artist names, no direct imitation.
```

---

## Search Tags

```text
Enum Rage Engine
Antisapian console music
16-bit industrial EBM
industrial chiptune
lo-fi chiptune
corrupted cartridge music
beat-em-up cartridge music
full-length instrumental cue
minimum 1:30
target 1:45
raw FM synth
square-wave bass
chip drums
fixed BPM
fixed key
no voices
no vocals
Suno generation findings
Biosphere Error
Buried Pulse
Dumb Terminal Crawl
Meridian Prime music
Suno
```
