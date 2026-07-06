# Red Warrant Reference PDF Study Index

**Status:** Sandbox Production Notes / Non-Canon Until Promoted  
**Project:** Red Warrant  
**Primary Soundtrack Artist:** Pit ROM  
**Label Context:** Pulse Width Music / PWM  
**Related Track:** `docs/music/songs/pit-rom/condemned-block-intro.md`  
**Related Lab Notes:**

- `docs/music/production-notes/red-warrant-deflemask-dmf-lab-notes.md`
- `docs/music/production-notes/red-warrant-deflemask-shmup-calibration-addendum-2026-07-06.md`

**Created:** 2026-07-06  

---

## Rights / Use Boundary

The source PDFs are third-party reference material. Do **not** commit the actual PDF files or reproduce the tabs, notation, or lyrics in this repository unless rights are explicitly cleared.

This note preserves only repo-safe study metadata and high-level structural lessons for transforming the reference material into original Red Warrant / Pit ROM tracker work.

Working rule:

```text
Study gesture, density, role, register, and arrangement logic.
Do not copy riffs, melodies, lyrics, notation, or exact arrangement.
```

---

## Reference PDFs Studied

| Local Filename | Working Role in Study | Repo-Safe Takeaway |
|---|---|---|
| `Power Trip - Executioners Tax - Chords.pdf` | Chord/tab language reference | Dense palm-muted low-string pressure, chromatic power movement, slide gestures, and short upper stabs |
| `Power Trip - Executioners Tax - Pro.pdf` | Drum-score reference | 167 BPM thrash/crossover drum drive, dense cymbal grid, kick/snare motion, fills, chorus stomp shapes, outro energy |
| `Power Trip - Executioners Tax - Pro (1).pdf` | Drive guitar reference | Held / repeated power-slab architecture, sparse intro and chorus repeat structure, simple heavy chord anchors |
| `Power Trip - Executioners Tax - Pro (2).pdf` | Rhythm guitar 2 / effects reference | Palm-muted low-pedal movement, whammy bar / artificial harmonic gestures, doubled rhythm-guitar pressure |
| `Power Trip - Executioners Tax - Pro (3).pdf` | Bass reference | EADG bass role, open low-root intro behavior, repeated low-pedal support, chromatic pickup motion, chorus root support, held outro roots |
| `Power Trip - Executioners Tax - Pro (4).pdf` | Vocal rhythm reference | Treat vocal rhythm as another muted/stab guitar layer; x-note syllable energy becomes short percussive guitar chops, chant markers become chorus stab accents |

---

## DefleMask Translation Model

The reference material should be translated into original Red Warrant Genesis / Mega Drive tracker language.

Core channel model:

| Channel | Red Warrant Role |
|---|---|
| FM1 | Bass foundation / low-root pedal support |
| FM2 | Main rhythm-guitar attack weapon |
| FM3 | Fifth slabs / doubled rhythm guitar / power support |
| FM4 | Whammy / AH / vocal-guitar chop layer when needed |
| FM5 | Donor crash / auxiliary impact only if it belongs to the band palette |
| FM6 | Donor drum body: kick, snare, hats, crashes as supported by `mad_man_ness.dmf` instruments |
| PSG channels | Avoid unless specifically needed; earlier tests showed chirpy PSG percussion does not fit this direction |

Current stripped-palette rule:

```text
Drums + bass + rhythm guitars only.
No PSG chirps.
No bullet arps.
No red-stamp pulses.
No synth pads.
No unrelated melodic hooks.
```

---

## Lessons Added From the PDF Set

### 1. Drums

The donor drums from `mad_man_ness.dmf` are currently preferred over hand-authored PSG drums.

Reason:

```text
The hand-authored Sega drum pass sounded like chirps.
The donor kit reads more like usable tracker drums.
```

Confirmed working direction:

```text
Keep donor drum volume strong.
Lower hats first only if they mask guitar.
Do not reduce kick/snare before checking guitar and bass balance.
```

### 2. Rhythm Guitar

The useful guitar behavior is not realistic guitar synthesis. It is midrange attack.

Current direction:

```text
FM2 = main palm-muted / power-rhythm attack lane
FM3 = fifth slab / doubled rhythm support
FM4 = whammy / AH / vocal-chop layer, not a melodic lead hook
```

Avoid returning to the earlier problem:

```text
No sitar-like melodic lead identity.
No unrelated upper sparkle.
No long ornamental FM4 hook unless requested.
```

### 3. Bass

The bass PDF clarified that bass should not just copy the guitar at the same register. It should glue drums and guitars with low-root pressure.

Working bass role:

```text
low-root pedal
open-root intro support
chromatic pickup motion
chorus root reinforcement
held outro roots
```

Mix rule:

```text
If the mix muddies, lower bass first, not the now-confirmed donor drum volume.
```

### 4. Vocal-as-Guitar Layer

The vocal PDF should be treated as rhythm-guitar energy, not as a synth vocal or lead melody.

Translation:

```text
x-note syllable hits -> short muted guitar chops
chorus chant markers -> short stab accents
held vocal space -> leave room or use restrained slabs
```

This adds chant/stomp shape while preserving the stripped band-palette direction.

---

## Practice Builds Informed by This PDF Set

| Build | Purpose |
|---|---|
| `red_warrant_drive_guitar_donor_drums_test_02.dmf` | Combined drive guitar reference with louder donor drums |
| `red_warrant_four_pdf_stripped_test_03.dmf` | Removed unrelated sounds and used only the four-PDF guitar/drum palette |
| `red_warrant_bass_integrated_test_04.dmf` | Added bass PDF behavior as low foundation |
| `red_warrant_vocal_guitar_integrated_test_05.dmf` | Added vocal rhythm PDF as muted/stab guitar layer |

These files are practice artifacts, not canon releases.

---

## Current Best Working Recipe

```text
Use donor drums from mad_man_ness.dmf.
Keep drum volume strong.
Build around FM2 rhythm attack.
Use FM3 for slabs and doubled power support.
Use FM1 for bass root pressure.
Use FM4 only for effects, whammy/AH, and vocal-chop translation.
Avoid PSG/chiptune ornament unless requested.
Keep the palette band-like and stripped.
```

---

## Next Recommended Build Direction

The next `.dmf` should continue from:

```text
red_warrant_vocal_guitar_integrated_test_05.dmf
```

Recommended next experiment:

```text
Test 06: tighten arrangement and balance
- preserve donor drum volume
- keep bass integrated
- keep vocal-as-guitar layer
- compare +5 body versus +7 bite
- reduce any layer that sounds unrelated to the five instrumental roles
```

Primary listening goal:

```text
Does it feel like drums, bass, and multiple rhythm guitars performing one original Sega-thrash stage cue?
```
