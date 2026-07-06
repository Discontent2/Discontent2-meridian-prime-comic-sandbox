# Red Warrant DefleMask Shmup Calibration Addendum

**Status:** Sandbox Production Notes / Non-Canon Until Promoted  
**Project:** Red Warrant  
**Primary Soundtrack Artist:** Pit ROM  
**Label Context:** Pulse Width Music / PWM  
**Related Track:** `docs/music/songs/pit-rom/condemned-block-intro.md`  
**Related Lab Note:** `docs/music/production-notes/red-warrant-deflemask-dmf-lab-notes.md`  
**Created:** 2026-07-06  

---

## Core Purpose

This addendum preserves the lessons learned after the first DefleMask DMF lab note.

The focus shifted from simply proving `.dmf` construction to learning how to make **badass indie shoot-'em-up chiptune stage music** in Genesis / Mega Drive DefleMask mode.

The main breakthrough:

```text
The track does not need a realistic guitar.
It needs an audible midrange attack weapon that survives the full chip mix.
```

---

## Key Diagnostic Lesson

Several practice `.dmf` files showed that pattern data can be correct while the intended musical layer is still inaudible.

Important rule:

```text
Pattern data is not music.
Audible identity is music.
```

A channel can contain hundreds of events and still fail if the instrument patch, register, volume, or mix balance is wrong.

---

## Practice Files Since Last Entry

| File | Purpose | Result |
|---|---|---|
| `red_warrant_lead_guitar_practice_01.dmf` | Sega thrash lead-guitar practice | Cool but drifted into desert / sitar character |
| `red_warrant_rhythm_guitar_practice_02.dmf` | Anti-sitar rhythm-guitar correction | Guitar data existed but was not audible |
| `red_warrant_shmup_engine_calibration_01.dmf` | Diagnostic shmup engine calibration | FM2 was good throughout |
| `red_warrant_shmup_stage_practice_01.dmf` | First stage-loop practice using calibrated FM2 | Established a working stage loop direction |
| `red_warrant_upper_range_calibration_01.dmf` | Upper-range dynamics test | FM4 was not audible |
| `red_warrant_fm4_boost_calibration_01.dmf` | FM4 volume / boost test | `5C` too low, `7F` too loud |

These are practice artifacts, not canon releases.

---

## Sitar / Desert Drift Diagnosis

The first lead-guitar practice sounded cool but too much like a desert level or sitar-like lead.

Likely causes:

| Symptom | Likely Cause |
|---|---|
| Sitar-like tone | too nasal, too resonant, too much upper harmonic focus |
| Desert-coded mood | overuse of Phrygian / flat-second movement |
| Too much lead identity | FM4 lead was too central too early |
| Not enough thrash body | rhythm-guitar / midrange attack layer was not dominant enough |
| Too ornate | melodic decoration instead of right-hand pressure |

Correction rule:

```text
Less singing wire snake.
More rusted downstroke engine.
```

---

## Thrash Guitar Lesson: Right Hand First

The deep dive on thrash guitar clarified that the rhythm feel matters more than lead realism.

Thrash guitar is built from:

```text
downstroke pressure
palm muting
tight stops
low-register riff cells
power-chord hits
chromatic tension
minor-third / tritone menace
short bursts of speed
rhythmic authority
```

For Sega chiptune, the translation is not:

```text
FM2 = realistic guitar
```

The better translation is:

```text
FM2 = midrange attack weapon
```

The player does not need to identify a real guitar. The player needs to feel pressure, motion, danger, and impact.

---

## Shmup Chiptune Design Lesson

A shoot-'em-up track should be arranged like enemy waves, not like a rock band performance.

Core rule:

```text
Motion first.
Hook second.
Texture third.
Realism never.
```

Indie shmup chiptune should feel like:

```text
engine + warning lights + bullets + panic math + heroic grime
```

Bad direction:

```text
band intro + verse + chorus + solo
```

---

## Working Shmup Layer Stack

| Layer | Purpose | Genesis Channel Idea |
|---|---|---|
| Clock | makes the screen move | FM6 drums + PSG noise hats |
| Engine | bass propulsion | FM1 |
| Midrange Attack | aggression / fake-guitar role | FM2 |
| Slab / Squeal / Harmony | power accents | FM3 |
| Hook | stage identity | FM4 |
| Bullet Lattice | arps, alarms, sparks | PSG1 / PSG2 / PSG3 |
| Atmosphere | place and pressure | FM5 sparingly |

Important correction:

```text
FM5 hum must not enter early calibration.
Pads and hums can murder midrange.
```

---

## New Channel Priority

| Channel | Priority | Role |
|---|---:|---|
| FM1 | 1 | bass engine |
| FM2 | 1 | midrange attack weapon, confirmed audible |
| FM3 | 3 | root/fifth slabs, squeals, metallic accents |
| FM4 | 4 | hook / upper dynamic layer, volume still being calibrated |
| FM5 | 6 | sparse hum, not early calibration |
| FM6 | 1 | native drums |
| PSG1 | 5 | red stamp pulse / bullet arp |
| PSG2 | 5 | counter pulse / bullet lattice |
| PSG3 | 7 | optional alarm |
| PSG Noise | 1 | hats, grit, impact dust |

---

## FM2 Breakthrough

The diagnostic file `red_warrant_shmup_engine_calibration_01.dmf` proved that FM2 can work as the main midrange attack layer.

User finding:

```text
FM2 was good throughout.
```

Meaning:

| Test Result | Meaning |
|---|---|
| FM2 audible alone | patch has enough carrier body |
| FM2 audible with bass | FM1 is not swallowing the low-mid range |
| FM2 audible with drums | FM6 / PSG noise are not masking the attack |
| FM2 audible in full mini-loop | Red Warrant stage music can be built around this layer |

New rule:

```text
Every new Red Warrant track starts with a calibration order.
No full arrangement until the attack layer survives bass and drums.
```

---

## FM2 Design Rules Going Forward

FM2 should be treated as the proven attack lane.

Working principles:

```text
Carrier body first.
Feedback bite second.
Fancy harmonics last.
```

Practical FM2 rules:

| Rule | Reason |
|---|---|
| Use a carrier-heavy FM patch | prevents the layer from vanishing in the mix |
| Test at high volume first | prove audibility before mixing |
| Avoid too many OFF rows early | let the instrument envelope do the muting |
| Keep most material around F#2-C#4 | gives attack without becoming bass mud or toy treble |
| Use FM3 fifths only on accents | creates power-slab illusion without crowding |
| Keep FM5 hum out during calibration | avoids midrange masking |

---

## FM4 Upper-Range Discovery

The upper-range calibration showed:

```text
FM4 was not audible.
```

The follow-up boost calibration showed:

```text
Volume 5C was too low.
Volume 7F was too loud.
```

Conclusion:

```text
FM4 is not dead.
FM4 needs volume choreography.
```

Likely useful FM4 window:

```text
68 to 74
```

Best first candidates:

```text
6C, 70, 74
```

---

## FM4 Dynamic Volume Rule

Do not use one fixed lead volume for FM4.

Recommended behavior:

| FM4 Volume | Use |
|---:|---|
| `5C` | too low / avoid for primary hook |
| `64` | very light shadow only |
| `68` | quiet hook note / sparse mix |
| `6C` | normal hook note candidate |
| `70` | main hook target |
| `74` | phrase ending / accent / danger call |
| `78` | rare emergency accent |
| `7F` | too loud / avoid as default |

Pattern-volume shaping example:

```text
C#4 09 6C
E-4 09 68
F#4 09 70
A-4 09 74
```

New FM4 rule:

```text
Normal hook notes: 6C
Important hook notes: 70
Phrase-ending accents: 74
Emergency calls: 78 max, rarely
Never default to 7F
```

---

## FM4 Register Rule

FM4 should not begin as a very high lead.

Better first range:

```text
C#4
E-4
F#4
A-4
C#5
```

Only after that is audible should it reach:

```text
E-5
F#5
C#6
```

Working interpretation:

```text
FM4 is the upper-mid hook weapon first.
It is the high squeal lane second.
```

---

## Better Practice Build Sequence

The successful methodology is now:

```text
1. Isolate the instrument.
2. Prove it loud.
3. Add bass.
4. Add drums.
5. Add PSG motion.
6. Add hook.
7. Only then build a stage loop.
```

Avoid:

```text
writing full arrangements before the channel mix works
```

---

## Stage Loop Direction

The stage-loop practice should follow this shape:

| Order | Function |
|---:|---|
| 00 | boot pressure / FM2 teaser |
| 01 | bass + drums + FM2 engine |
| 02 | FM3 root/fifth slabs |
| 03 | PSG bullet lattice |
| 04 | FM4 short hook |
| 05 | enemy-wave variation |
| 06 | layer-removal break, motion stays |
| 07 | full loop return |
| 08 | final tag / loop seam |
| 09 | stop marker |

Key rule:

```text
Breaks in shmup music remove layers.
They do not remove motion.
```

---

## Current Working Formula

For Red Warrant / Pit ROM Genesis `.dmf` practice:

```text
FM1 = bass conveyor
FM2 = midrange attack weapon
FM3 = root/fifth slab or metallic accent
FM4 = dynamic-volume hook layer
FM5 = sparse fluorescent hum only after mix works
FM6 = native FM drums
PSG1 = red stamp pulse
PSG2 = bullet lattice counterline
PSG3 = optional alarm
PSG Noise = hats, grit, impact dust
```

Core motto for this phase:

```text
Do not chase realistic guitar.
Build an engine that makes the screen move.
```

---

## Recommended Next Test

The next useful `.dmf` should be:

```text
FM4 Dynamic Volume Calibration 01
```

Suggested order plan:

| Order | Test |
|---:|---|
| 00 | FM2 known-good reference |
| 01 | FM4 volume ladder: `60, 64, 68, 6C, 70, 74, 78` |
| 02 | FM4 shaped hook using `68-74` |
| 03 | FM4 shaped hook with FM2 |
| 04 | FM4 shaped hook with bass/drums |
| 05 | FM4 phrase accents: mostly `6C`, ending `74` |
| 06 | full mix with dynamic FM4 |
| 07 | full mix with FM4 removed for comparison |
| 08 | final corrected stage loop |
| 09 | stop |

Purpose:

```text
Find the musical FM4 hook window without repeating the 5C-too-low / 7F-too-loud problem.
```

---

## Production Rule Update

```text
mad_man_ness.dmf remains the format specimen.
FM2 calibration is now the sonic foundation.
FM4 requires dynamic volume choreography before it becomes a reliable hook lane.
```

This addendum should guide the next Red Warrant DefleMask build before any attempt at a longer stage track.
