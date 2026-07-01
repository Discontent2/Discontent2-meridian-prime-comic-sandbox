# Red Warrant Damaged Cartridge BGM Findings

**Status:** Production Note / Suno Prompt Findings / Red Warrant BGM Doctrine  
**Project:** Red Warrant  
**Primary BGM Artist:** Pit ROM  
**Source Band Mythology:** Writ Hammer  
**Studio Context:** Devilment Studio  
**Related Track:** `docs/music/songs/pit-rom/condemned-block-intro.md`  
**Related Roadmap:** `docs/music/soundtracks/red-warrant-original-16-bit-soundtrack-roadmap.md`  
**Created:** 2026-06-30

---

## Core Finding

The goal is not polished 16-bit metal.

The goal is:

```text
damaged cartridge playback of a heavy track
```

Better project spell:

```text
MIDI thrash riffs forced through dirty tracker hardware.
```

Even better Red Warrant north star:

```text
Not retro metal.
Not chiptune thrash.
A dark, dusty, warped cartridge trying to remember a riot.
```

---

## What Went Wrong Earlier

Suno drifted toward:

```text
polished retro metal
cute chiptune
music box timbres
choir / vocal pad textures
wub-wub bass behavior
bright arcade melody
clean modern production
```

The issue was not lack of aggression. The issue was the wrong vocabulary.

Some words invited the wrong behavior:

```text
chip
light
shriek
scream
wobble
more
gets
feels
walks
chromatically
```

Observed problems:

```text
chip -> cute-retro behavior
light -> brighter mix behavior
shriek / scream -> novelty upper-register lead behavior
wobble -> wub-wub / techno bass behavior
no samples -> conflicts with SNES-style playback logic
negative-heavy style boxes -> waste limited style-box space
```

---

## Corrected Style Strategy

### Style Box Rule

The Suno Style / Prompt Box should be positive-only.

Do not spend limited style-box characters on the no-list. Use the style box to bait the target sound.

Use the Exclude Box for guardrails.

Preferred style-box approach:

```text
what the track is
what hardware frame it uses
what instruments/channels should dominate
what the mix should feel like
what the scene mood is
```

Avoid in the Style Box:

```text
long no-lists
cute-trigger words
conflicting instructions
broad genre labels without hardware constraints
```

---

## Correct Red Warrant / Pit ROM Doctrine

Use this as the default Red Warrant BGM language:

```text
dark 16-bit tracker-module combat BGM
warped dirty red-cartridge beat-'em-up metal
damaged computerized heavy-rock conversion
Genesis-style metallic FM synthesis
low-memory 16-bit console playback
short repeating thrash riff cell
square-wave bass descending in dark half steps
detuned square bass grind
stiff cartridge drum channel
boxy fake double-kick thud
flat digital snare crack
dry metallic hat noise
crushed low-bit guitar stabs
distorted upper-register FM saw-pulse lead
grimy fluorescent hum pad
ugly mono CRT speaker mix
muffled dark top end
dirty loop points
cramped memory
bad-speaker pressure
rotted cartridge grit
uneven playback drift
```

---

## Bass Language Corrections

Avoid:

```text
wobble
wub
filter sweep
filter wobble
modulated bass
dub bass
sub drop
bass drop
LFO bass
growl bass
neuro bass
```

Use instead:

```text
square-wave bass descending in dark half steps
detuned square bass grind
muffled low-end pressure
dirty midrange bass scrape
boxy cartridge bass
uneven playback drift
bass descent
low repeating figure
```

---

## Phrase Corrections

Avoid these words in arrangement boxes when possible:

```text
chromatically
feels
gets
more
walks
```

Preferred replacements:

```text
Down chromatically -> square bass descends in dark half steps
Riff feels heavier -> riff drops to a lower register
Kick pulse gets thicker -> kick pulse lands as a dense low thud
Bass becomes more repetitive -> bass locks into a tight repeating figure
Square bass walks down chromatically -> square bass descends in half steps
```

---

## Avoid Cute / Choir Drift

Strong Exclude Box items for this project:

```text
vocals, voice, singing, spoken words, narrator, lyrics, vocal chops, choir, chant, humming, vocal pad, angelic pad, children choir, opera, gospel, music box, toy piano, celesta, glockenspiel, bells, bell lead, chimes, wind chimes, fantasy sparkle, bright arcade melody, cute chiptune, cute retro game music, happy melody, cheerful lead, clean synth lead, clean arpeggio, heroic melody, uplifting melody, orchestral strings, cinematic choir
```

---

## Avoid Wub-Wub / Techno Bass Drift

Add these when the track starts producing wobble bass:

```text
wobble bass, wub bass, dubstep bass, LFO bass, filter wobble, filter sweep, bass drop, sub drop, growl bass, neuro bass, modulated bass
```

---

## Do Not Mention Samples Unless Needed

Earlier prompt attempts used both SNES-style sample playback and a blanket no-samples instruction. That may create confusion.

Current recommendation:

```text
Do not mention samples in the Style Box unless absolutely needed.
Use low-memory console playback, damaged computerized heavy-rock conversion, tracker-module combat BGM, or cartridge playback instead.
```

In Exclude Boxes, prefer specific sample restrictions only when needed:

```text
sampled dialogue
movie sample
field recording voice
```

Avoid broad:

```text
no samples
```

when SNES-style sample logic is part of the desired sound.

---

## Full Positive Style Box Pattern

Recommended formula:

```text
[Artist], [Game] Track [#], [Title]. Dark instrumental 16-bit tracker-module combat BGM for [Studio]. Warped dirty red-cartridge beat-'em-up metal, damaged computerized heavy-rock conversion, [BPM] fixed, one minor key center. Genesis-style metallic FM synthesis fused with low-memory 16-bit console playback. Short repeating thrash riff cell, square-wave bass descending in dark half steps, detuned square bass grind, stiff cartridge drum channel, boxy fake double-kick thud, flat digital snare crack, dry metallic hat noise, crushed low-bit guitar stabs, distorted upper-register FM saw-pulse lead, call-and-response between low chug rhythm and warped lead. [Scene hum/pad], [stage pulse], [mood]. Ugly mono CRT speaker mix, muffled dark top end, dirty loop points, cramped memory, bad-speaker pressure, rotted cartridge grit, uneven playback drift.
```

---

## Track 1 Keeper Vocabulary

For `Condemned Block Intro`, the keeper vocabulary is:

```text
condemned block
already convicted
red legal-stamp pulse
civic horror action stage
grimy fluorescent hum pad
condemned stairwell mood
paperwork rotting in the walls
the appeal was denied before it was filed
```

---

## Final Track 1 Direction

Approved direction for Track 1:

```text
Pit ROM, Red Warrant Track 1, Condemned Block Intro. Dark instrumental 16-bit tracker-module combat BGM for Devilment Studio. Warped dirty red-cartridge beat-'em-up metal, damaged computerized heavy-rock conversion, 94 BPM fixed, one minor key center. Genesis-style metallic FM synthesis fused with low-memory 16-bit console playback. Short repeating thrash riff cell, square-wave bass descending in dark half steps, detuned square bass grind, stiff cartridge drum channel, boxy fake double-kick thud, flat digital snare crack, dry metallic hat noise, crushed low-bit guitar stabs, distorted upper-register FM saw-pulse lead, call-and-response between low chug rhythm and warped lead. Grimy fluorescent hum pad, red legal-stamp pulse, condemned stairwell mood, civic horror action stage. Ugly mono CRT speaker mix, muffled dark top end, dirty loop points, cramped memory, bad-speaker pressure, rotted cartridge grit, uneven playback drift.
```

---

## Production Motto

```text
The Style Box is bait.
The Exclude Box is the bear trap.
The Lyrics Box is the hardware map.
```
