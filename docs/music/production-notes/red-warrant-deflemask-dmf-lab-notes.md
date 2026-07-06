# Red Warrant DefleMask DMF Lab Notes

**Status:** Sandbox Production Notes / Non-Canon Until Promoted  
**Project:** Red Warrant  
**Primary Soundtrack Artist:** Pit ROM  
**Label Context:** Pulse Width Music / PWM  
**Related Track:** `docs/music/songs/pit-rom/condemned-block-intro.md`  
**Created:** 2026-07-06  

---

## Core Purpose

```text
The Suno track is the crime scene.
The stems are evidence.
DefleMask is the cartridge brain.
Reaper is the surgery table.
The SP-404mkII is the dirt printer.
```

This note preserves what was learned while shifting the Red Warrant / Pit ROM tracker workflow from Furnace Tracker into DefleMask `.dmf` production.

The practical goal is to build native Genesis / Mega Drive style tracker modules for Red Warrant without depending on imported samples unless a later production pass specifically calls for them.

---

## Working File Specimen

Reference file studied:

```text
mad_man_ness.dmf
```

Key findings from the practice file:

| Item | Finding |
|---|---|
| Format | DefleMask `.dmf` |
| Compression | zlib-compressed binary payload |
| Header after decompression | `.DelekDefleMask.` |
| DMF version | v24 / `0x18` |
| System | Genesis / Mega Drive |
| Channels | 10 |
| Rows per pattern | 64 |
| Order / matrix length | 54 |
| Wavetables | 0 |
| Samples | 0 |
| Instruments | 26 |
| Pattern effect columns | 1 effect column per channel |
| Metadata | Song name and author blank |

The file proved that a Genesis `.dmf` can be opened, decompressed, parsed, cloned, and rebuilt without damaging the DefleMask structure.

---

## DefleMask File Structure Lessons

A `.dmf` should be treated as a compressed binary cartridge, not a plain text tracker project.

Basic creation chain:

```text
build uncompressed DMF binary payload
write DefleMask header / version / system metadata
write song info and timing data
write pattern matrix
write instruments
write wavetables
write pattern data
write sample data if used
zlib compress
save as .dmf
```

Important validated practice steps:

1. A byte-identical copy of `mad_man_ness.dmf` was created as `practice_run.dmf`.
2. A native-drum Red Warrant skeleton was created using the `mad_man_ness.dmf` file as a structural and instrument donor.
3. A structural thrash-study file was created using `mad_man_ness.dmf` instruments.
4. A later native Genesis thrash-study file was created with new FM / PSG instruments instead of donor instruments.

---

## Genesis / Mega Drive Channel Map

DefleMask Genesis / Mega Drive mode gives 10 channels.

Practical Red Warrant channel map:

| DMF Channel | Working Role |
|---:|---|
| 0 | FM1 / bass grind |
| 1 | FM2 / low guitar stab |
| 2 | FM3 / high metallic accent or EXT.CH3 tricks |
| 3 | FM4 / rotted lead |
| 4 | FM5 / hum, pad, warning tone |
| 5 | FM6 / FM drums or extra FM voice |
| 6 | PSG1 / square pulse |
| 7 | PSG2 / counter pulse |
| 8 | PSG3 / alarm tone or pulse support |
| 9 | PSG Noise / hats, grit, static pressure |

Earlier Furnace thinking treated FM6 as a sample / PCM lane. In DefleMask Genesis work, FM6 can be used musically or for native FM drum synthesis. For the current Red Warrant direction, native FM drums are preferred.

---

## Most Important Conceptual Correction

DefleMask does not mainly provide a fixed soundbank of native instruments.

It provides native chip engines and instrument editor types.

Relevant instrument-editor model:

| Editor Type | Red Warrant Use |
|---|---|
| STD | Macro instruments, especially PSG square / noise behavior |
| FM | YM2612 operator instruments for basses, guitars, drums, leads, pads |
| Wavetable | Useful on systems with drawable wave channels, less central for Genesis |
| Samples | Optional WAV / PCM support when wanted, not the first foundation |

Therefore, future Red Warrant `.dmf` files should not depend on the `mad_man_ness.dmf` instrument set. That file is now best used as a structural specimen, not a permanent sound donor.

---

## Native Red Warrant DefleMask Palette

Preferred native Genesis palette for Pit ROM:

| Slot | Instrument | Type | Purpose |
|---:|---|---|---|
| 00 | Legal Stamp Kick | FM | short boxy kick / hard legal-stamp thud |
| 01 | Concrete Snare | FM | flat hard snare crack |
| 02 | Chain Hat | PSG Noise or FM | dry metallic tick |
| 03 | Boot Tom | FM | low impact fill / stomp accent |
| 04 | Dirt Crash | FM feedback / noise | ugly transition hit |
| 05 | Razor Bass | FM | main F#1 to F-1 grind bass |
| 06 | Docket Bass | FM | tighter alternate bass |
| 07 | Low Warrant Stab | FM | fake guitar chunk |
| 08 | High Warrant Stab | FM | metallic upper stab |
| 09 | Rotted Lead | FM | combat melody / saw-pulse lead |
| 0A | Fluorescent Hum | FM | pad / drone / CRT pressure |
| 0B | Red Stamp Pulse | STD PSG Square | warning pulse |
| 0C | Counter Pulse | STD PSG Square | octave shadow |
| 0D | Static Gate | STD PSG Noise | texture, hats, riser grit |
| 0E | Siren Operator | FM / EXT.CH3-ready | panic accent / operator squeal |

Practical lesson: when the goal is Red Warrant, the sound should feel like hardware being forced to impersonate heavy music, not like a realistic band arranged in tracker software.

---

## FM Design Vocabulary

For YM2612 / Genesis FM instruments, the main useful control ideas are:

| Parameter | Practical Meaning |
|---|---|
| ALG | operator routing / basic voice architecture |
| FB | feedback bite, grit, fake distortion |
| MULT | harmonic multiplier, useful for metallic edges and guitar-like upper bite |
| TL | operator total level; lower TL usually means louder operator contribution |
| AR | attack speed |
| DR / D2R | decay behavior |
| SL | sustain level |
| RR | release speed |
| DT | detune / sourness / cartridge wobble |
| SSG-EG | alternate envelope shapes, useful for buzz and odd decay |

Useful Red Warrant FM categories:

```text
kick: fast attack, quick pitch/body decay, short release
snare: noisy feedback, sharp attack, short-to-medium decay
bass: low carrier body, mild feedback, short attack, controlled sustain
guitar stab: aggressive attack, short gate, metallic harmonic multiplier, feedback bite
lead: nasal upper harmonic focus, moderate sustain, dirty release
hum pad: slower attack, low volume, dark midrange pressure
```

---

## PSG / STD Design Vocabulary

PSG channels are valuable for thinness, alarm logic, and grit.

Useful Red Warrant PSG categories:

```text
PSG square pulse: legal stamp beep, warning light blink, octave shadow
PSG counter pulse: call-and-response with bass or lead
PSG noise hat: dry tick, cartridge grit, cheap metallic hat
PSG noise snare layer: static slap under FM snare
PSG noise gate: texture that opens and closes around impact rows
```

Do not underestimate PSG noise. It is the dirt-pressure lane.

---

## Pattern Grid Standard

For Red Warrant DefleMask work:

```text
Tempo target: depends on DefleMask timing, but preserve the intended feel first
Rows per pattern: 64
1 row: practical sixteenth-note grid
16 rows: 1 bar
64 rows: 4 bars
```

Bar map:

| Bar | Rows |
|---|---|
| Bar 1 | 00-0F |
| Bar 2 | 10-1F |
| Bar 3 | 20-2F |
| Bar 4 | 30-3F |

Beat-start rows:

```text
00, 04, 08, 0C
10, 14, 18, 1C
20, 24, 28, 2C
30, 34, 38, 3C
```

This grid remains the safest foundation for both slow 94 BPM stage music and faster thrash-study material.

---

## Arrangement / Matrix Lessons

A DefleMask order matrix is per-channel, not just one global pattern number.

This means each order row can route different pattern numbers to different channels.

Example:

```text
Order 04 can use:
FM1 pattern 04
FM2 pattern 07
FM3 pattern 02
FM6 pattern 05
PSG Noise pattern 03
```

For beginner-safe builds, use the same pattern number across all channels at first:

```text
Order 00 = Pattern 00 on all channels
Order 01 = Pattern 01 on all channels
Order 02 = Pattern 02 on all channels
Order 03 = Pattern 03 on all channels
```

For more advanced builds, reuse drum and bass patterns while changing only stabs, leads, or PSG pulses.

---

## Red Warrant Track 1 DefleMask Skeleton

Current core track:

```text
Condemned Block Intro
Internal Subtitle: Already Convicted
Artist: Pit ROM
Game: Red Warrant
Track Number: 1
Function: Opening stage / first combat zone
```

Core bass motion:

```text
F#1 -> F-1
```

Important tracker spelling:

```text
F#1 = F sharp octave 1
F-1 = F natural octave 1
```

The dash in `F-1` is normal tracker notation.

Minimum DefleMask build target:

```text
Order 00: Boot pressure / condemned block wakes up
Order 01: Native FM drums + F#1 to F-1 bass engine
Order 02: Engine + low warrant stabs
Order 03: Engine + stab variation + high metallic accents
```

---

## Thrash-Study / Copyright-Safe Practice Lessons

A practice run was made around the broad feel of fast crossover-thrash metal: fast engine, half-time stomp, hard stops, chant-like hook pressure, and final sprint energy.

Important legal / creative boundary:

```text
Do not copy real riffs.
Do not copy vocal melodies.
Do not copy lyrics.
Do not copy exact arrangement.
Study energy, section logic, density, and gesture shapes only.
```

Copyright-safe translation targets:

| Reference Trait | DefleMask-Safe Translation |
|---|---|
| Fast thrash engine | original low FM chug pattern on sixteenth grid |
| Half-time stomp | wider kick / snare spacing and chant-shadow PSG pulses |
| Axe-like stops | gated block hits followed by short silences |
| Hook-forward energy | original PSG call shapes, not copied melody |
| Final sprint | denser hats, bass locks, short lead accents |

Useful in-world naming direction:

```text
Tax Warrant Study
Pit ROM
Red Warrant
```

Avoid putting real band names or real song titles into in-world `.dmf` metadata.

---

## Generated Practice Files So Far

Local practice artifacts generated during the DefleMask lab:

| File | Purpose |
|---|---|
| `practice_run.dmf` | byte-identical clone of `mad_man_ness.dmf` to prove safe reproduction |
| `red_warrant_condemned_block_intro_native_drums.dmf` | first native-drums Red Warrant skeleton using donor structure/instruments |
| `executioners_tax_structural_study.dmf` | structural thrash-study using donor instruments |
| `tax_warrant_native_thrash_study.dmf` | native Genesis thrash-study using new FM / PSG instruments |

These files are practice artifacts, not canon releases.

---

## Preferred Next Build Direction

Next useful DefleMask build should be:

```text
Fresh Genesis v24 .dmf
No samples
Original native FM / PSG instruments
Pit ROM / Red Warrant metadata
64-row patterns
Simple order matrix at first
Native FM drums
PSG noise grit
F#1 to F-1 bass pressure
Low fake-guitar stabs
Rotted lead fragments
Fluorescent hum pad
```

Recommended immediate milestone:

```text
Condemned Block Intro / Already Convicted
DefleMask Native Build 01
Orders 00-03 only
```

This keeps the project playable while avoiding the trap of trying to arrange the whole stage before the cartridge engine sounds right.

---

## Production Rule Going Forward

```text
mad_man_ness.dmf is the format specimen.
It is not the permanent instrument bank.
```

Future Red Warrant `.dmf` files should use native instrument recipes authored for Pit ROM unless the user specifically requests donor instruments or an intentional study file.
