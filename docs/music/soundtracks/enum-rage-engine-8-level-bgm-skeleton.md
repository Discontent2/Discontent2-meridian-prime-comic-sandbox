# Enum Rage Engine / 8-Level 16-Bit Game BGM Skeleton

**Status:** Sandbox Soundtrack Skeleton / Non-Canon Until Promoted  
**Artist:** Enum Rage Engine  
**Project:** TBD Enum Rage Engine Cartridge Material  
**Primary Use:** 16-bit game background music map  
**Created:** 2026-06-29

---

## Canon / Sandbox Note

This file is a working soundtrack and biome-planning skeleton. It does not canonize the game, biomes, level order, bosses, or soundtrack titles until explicitly promoted.

---

## Core Premise

This is an 8-level 16-bit game soundtrack framework for Enum Rage Engine.

The first established world is:

```text
Level 1: Null Cavern
First single: Null Cavern BGM
```

`Null Cavern BGM` defines the BGM-safe direction: music-only background cue, no gameplay cues, no event sounds, no voices, no realistic drums, and no extra sounds that could confuse players.

---

## BGM Safety Lock

All tracks in this game soundtrack should follow this rule:

```text
If it sounds like information, keep it out of the BGM.
If it sounds like atmosphere, it can stay.
```

Avoid in all BGM prompts:

```text
power-up sounds
item sounds
coin sounds
menu beeps
UI chirps
alarms
sirens
doors
weapons
impacts
creatures
footsteps
scanning sounds
laser zaps
voices
vocals
speech
choir
realistic drums
hi-fi polish
```

---

## 8-Level Biome Map

| Level | Biome | Core Feel | Gameplay Identity | Enum BGM Direction |
|---|---|---|---|---|
| 1 | Null Cavern | Alien cave, wet stone, dead console glow | Basic traversal, first enemies, hidden passages | Slow 16-bit alien cavern EBM. First single: `Null Cavern BGM`. |
| 2 | Rust Marsh | Toxic swamp, metal reeds, sinking machinery | Slow platforms, poison pools, lurking enemies | Murky pulse, wet FM bass, muffled chip drums, no alarm-like sounds. |
| 3 | Relay Spires | Vertical antenna forest, storm towers, signal ruins | Climbing, elevators, wind/current hazards | Thin high FM arps, static tension, non-event background pressure. |
| 4 | Furnace District | Industrial foundry, lava vents, conveyor ruins | Moving belts, heat gates, crushing machinery | Heavy EBM pulse, dull metal rhythm, hot low-end, no impact-like hits. |
| 5 | Blueglass Reef | Submerged crystal biome, alien aquatic ruins | Swimming / low gravity, drifting enemies | Slow liquid FM pads, glassy but lo-fi bass pulse, no bubble/item cues. |
| 6 | Graveyard Arcade | Abandoned game city, dead cabinets, neon bones | Maze-like city stage, fake exits, corrupted signage | Broken console funk, BGM-safe, no coin sounds, no menu beeps, no power-up blips. |
| 7 | Orbital Rootworks | Organic space station, vines through machinery | Gravity shifts, biotech enemies, branching routes | Cold alien EBM, pulsing bass, sterile pad pressure, no scan/event sounds. |
| 8 | The Enum Core | Final machine-organism, code cathedral, boss biome | Gauntlet, final locks, last boss, escape | Minimal industrial trance, fixed pulse, darker reprise of `Null Cavern BGM`. |

---

## Level Notes

### 1. Null Cavern

The first breath underground. Wet stone, alien fungal glow, dead console green, black mineral walls. The player learns movement, combat spacing, doors, and hidden cracks.

BGM identity:

```text
slow
subterranean
non-interactive
low-distraction
primitive 16-bit FM console audio
alien cavern pressure
```

Saved track:

```text
docs/music/songs/enum-rage-engine/null-cavern-bgm.md
```

Boss candidate:

```text
The Blind Gate Larva
```

---

### 2. Rust Marsh

A toxic swamp full of half-submerged industrial junk. Trees grow through old pipes. Water reflects magenta hazard lights, but the BGM must avoid actual alarm sounds.

BGM identity:

```text
slow murky EBM
wet low FM bass
muffled chip percussion
sinking mechanical pulse
no sirens
no warning beeps
```

Boss candidate:

```text
Siltjaw Clampbeast
```

---

### 3. Relay Spires

A vertical signal-tower biome. Broken antennas, lightning rods, service platforms, magnetic lifts, wind pressure, and distant storms.

BGM identity:

```text
thin high FM arps
static-like synth texture without actual alerts
vertical tension
cold exposed height
no UI chirps
no scan sounds
```

Boss candidate:

```text
The Weather Antenna
```

---

### 4. Furnace District

A factory / foundry level with molten channels, conveyors, crushing pistons, smoke stacks, and old worker tunnels.

BGM identity:

```text
heavy slow EBM pulse
dull metal rhythm
hot low-end pressure
compressed cartridge grime
no impact sounds
no weapon-like hits
```

Boss candidate:

```text
Kilnback Executor
```

---

### 5. Blueglass Reef

The beauty level. Alien underwater ruins, crystal coral, pressure doors, floating debris, and soft bioluminescence.

BGM identity:

```text
slow liquid FM pads
glassy but lo-fi bass pulse
soft underwater pressure
no bubble-pop item cues
no sparkling pickup sounds
```

Boss candidate:

```text
Pearl Circuit Leviathan
```

---

### 6. Graveyard Arcade

A dead neon entertainment district. Broken cabinets, signboards, prize machines, shuttered malls, dead escalators, rain on blacktop.

BGM identity:

```text
broken console funk
primitive FM bass
low-distraction background groove
no coin sounds
no menu beeps
no power-up blips
```

Boss candidate:

```text
Attract Mode Wraith
```

---

### 7. Orbital Rootworks

A late-game biome where the player reaches an overgrown orbital structure or sky-machine. Roots through metal. Organic cables. Gravity tricks. Half garden, half server rack.

BGM identity:

```text
cold alien EBM
sterile pad pressure
fixed pulse
organic-machine unease
no scan tones
no alert tones
```

Boss candidate:

```text
The Photosynthetic Lock
```

---

### 8. The Enum Core

Final area. A code-cathedral machine buried inside the world's logic. Black glass, blue light, red status glyphs, pulsing organic circuits.

The BGM should echo `Null Cavern BGM`, making the player realize the cave was the mouth of the whole system.

BGM identity:

```text
minimal industrial trance
fixed pulse
slow 16-bit final-core EBM
darker reprise of Null Cavern BGM
no final-boss stingers unless used in a separate boss track
```

Boss candidate:

```text
The Root Error
```

---

## Clean Level Title Set

```text
1. Null Cavern
2. Rust Marsh
3. Relay Spires
4. Furnace District
5. Blueglass Reef
6. Graveyard Arcade
7. Orbital Rootworks
8. The Enum Core
```

---

## Soundtrack Development Order

Recommended next track order:

```text
1. Null Cavern BGM - saved first single
2. Rust Marsh BGM
3. Relay Spires BGM
4. Furnace District BGM
5. Blueglass Reef BGM
6. Graveyard Arcade BGM
7. Orbital Rootworks BGM
8. Enum Core BGM
```

---

## Search Tags

```text
Enum Rage Engine
8-level game
16-bit game soundtrack
BGM skeleton
background music
music-only background cue
Null Cavern BGM
Rust Marsh
Relay Spires
Furnace District
Blueglass Reef
Graveyard Arcade
Orbital Rootworks
The Enum Core
Antisapian console music
16-bit industrial EBM
industrial chiptune
lo-fi chiptune
raw FM synth
square-wave bass
chip drums
Meridian Prime music
Suno
```
