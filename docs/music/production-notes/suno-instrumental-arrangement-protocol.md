# Suno Instrumental Arrangement Protocol

**Status:** Sandbox Production Note / Non-Canon Until Promoted  
**Scope:** Suno instrumental prompting / lyrics-box arrangement control  
**Applies To:** Enum Rage Engine, Wet Signal District, Pulse Width Music, Worldskin BGM, instrumental soundtrack cues  
**Created:** 2026-06-30

---

## Purpose

This note preserves a working Suno discovery:

```text
The lyrics box can be used for instrumental arrangement control only if every line is bracketed.
```

The lyrics field may support far more text than the style / prompt box, but unbracketed text is likely to be interpreted as words to sing or speak.

This protocol turns the lyrics box into an instrumental cue sheet instead of a lyric sheet.

---

## Core Finding

A previous instrumental test failed when the lyrics box included unbracketed prose such as:

```text
Primitive FM console ambience.
```

Suno interpreted that prose as singable / speakable lyric content and began vocalizing it.

Working correction:

```text
Every line in the lyrics box must be bracketed.
No free-floating words.
No prose outside brackets.
```

---

## Core Rule

Use this exact rule for instrumental lyrics-box arrangements:

```text
Suno Instrumental Lyrics Box Protocol:
Every line must be bracketed.
No prose outside brackets.
No complete lyric-like sentences.
Use short arrangement commands only.
Repeat [INSTRUMENTAL ONLY] and [NO VOCALS] at the top.
```

---

## Why This Works

Bracketed lines are more likely to be treated as section markers, arrangement instructions, or metadata.

Unbracketed lines are more likely to be treated as lyrics.

For instrumental cues, the lyrics box should look like a technical score map:

```text
[0:00 INTRO]
[DEEP REEF PULSE]
[SOFT FM PAD]
[NO VOCALS]
```

It should not look like prose or poetry:

```text
The reef remembers the city.
Primitive FM console ambience.
The current opens like a door.
```

---

## Required Header

Begin instrumental lyrics-box arrangements with a hard anti-vocal header:

```text
[INSTRUMENTAL ONLY]
[NO VOCALS]
[NO SINGING]
[NO SPOKEN WORDS]
[NO LYRICS]
[NO CHOIR]
[NO VOCAL CHOPS]
```

Optional extra reinforcement:

```text
[MUSIC ONLY]
[ARRANGEMENT MAP ONLY]
[SECTION MARKERS ONLY]
[DO NOT SING TEXT]
```

---

## Recommended Syntax

Use compact bracket commands:

```text
[0:00 INTRO]
[DEEP REEF PULSE]
[WARM LIQUID SQUARE BASS]
[SOFT UNDERWATER PAD]
[NO MELODY YET]
[MOOD: ALIEN REEF AT NIGHT]
```

Use short mood labels instead of sentences:

```text
[MOOD: WISTFUL AQUATIC ADVENTURE]
[MOOD: BEAUTIFUL BUT UNSAFE]
[MOOD: RAINLIT TRANSIT MELANCHOLY]
```

Use instrument/action labels:

```text
[SOFT CHIP KICK]
[TINY DIGITAL SNARE TICK]
[GENTLE METALLIC FM HAT]
[GLASSY FM MARIMBA LEAD]
[REPEAT MOTIF EVERY 8 BARS]
```

---

## Avoid Inside Lyrics Box

Avoid all of the following in instrumental lyrics-box arrangements:

```text
unbracketed prose
poetic lines
complete lyric-like sentences
quoted dialogue
character phrases
field-tape transcript text
paragraphs
punctuation-heavy emotional prose
anything that could be sung
anything that could be spoken
```

Even inside brackets, avoid overly lyric-like lines:

```text
[THE REEF REMEMBERS THE LOST CITY]
[I DREAM IN STATIC]
[WE SINK INTO BLUE LIGHT]
```

Safer replacements:

```text
[MOOD: LOST CITY MEMORY]
[TEXTURE: SOFT STATIC DREAM]
[MOOD: BLUE LIGHT DESCENT]
```

---

## Style Box Role

The Suno style / prompt box should still carry the track identity:

```text
artist name
track title
instrumental only
style lane
BPM
key behavior
instrument palette
core mood
hard exclusions
```

The lyrics box should carry the extended arrangement:

```text
timed sections
instrument entrances
motif instructions
texture changes
ending behavior
anti-vocal reinforcement
```

Core workflow:

```text
Style box = constitution
Lyrics box = level map
Exclude box = guardrail
```

---

## Exclude Field Reinforcement

Use the Exclude field to reinforce anti-vocal and anti-genre controls:

```text
vocals, voice, singing, spoken words, narrator, lyrics, vocal chops, choir, chant, humming, sampled dialogue, field-tape voices, bluegrass, banjo, fiddle, country, realistic drums, EDM drop, riser, alarm, siren, UI sound, coin sound, power-up sound, laser, sample-based nostalgia, real artist names, direct imitation
```

Adjust exclusions for each track as needed.

---

## Working Example: Blue Hole Reef BGM

### Style / Prompt Box

```text
Enum Rage Engine x Wet Signal District, Blue Hole Reef BGM. Instrumental only, no vocals, no speech. Slow 16-bit tropical alien reef EBM with rainfield ambient depth, 84 BPM fixed, one minor key. Primitive FM console audio, warm liquid square/FM bass, soft chip kick, tiny digital snare tick, gentle metallic FM hat. Dreamy aquatic adventure mood, eerie lagoon depth, deep underwater ambience, playful but lonely. Memorable glassy FM marimba lead, 5-note rising/falling hook. Low-distraction BGM, no gameplay cues, no bluegrass, no banjo, no fiddle, no country, no samples, no real names.
```

### Lyrics Box

```text
[INSTRUMENTAL ONLY]
[NO VOCALS]
[NO SINGING]
[NO SPOKEN WORDS]
[NO LYRICS]
[NO CHOIR]
[NO VOCAL CHOPS]

[0:00 INTRO]
[DEEP REEF PULSE]
[WARM LIQUID SQUARE BASS ONLY]
[SOFT UNDERWATER PAD]
[NO MELODY YET]
[MOOD: ALIEN REEF AT NIGHT]
[MOOD: BEAUTIFUL BUT UNSAFE]

[0:20 MAIN GROOVE]
[SOFT CHIP KICK]
[TINY DIGITAL SNARE TICK]
[GENTLE METALLIC FM HAT]
[WARM SLOW BASS]
[SMALL STEADY BACKGROUND DRUMS]
[NO FILLS]
[NO DROPS]
[NO RISERS]

[0:40 MAIN THEME]
[GLASSY FM MARIMBA LEAD]
[SIMPLE 5 NOTE RISING FALLING MOTIF]
[MEMORABLE WISTFUL PLAYFUL LONELY]
[REPEAT MOTIF EVERY 8 BARS]
[DO NOT OVERDEVELOP]

[1:05 DEEP WATER LAYER]
[WIDE LIQUID PAD]
[SOFT FM BELLS]
[SLOW UNDERWATER SHIMMER]
[MOOD SHIFT: SUNLIT REEF TO BLUE HOLE]
[NO ALARM TONE]
[NO DANGER CUE]

[1:25 FINAL THEME PASS]
[MAIN 5 NOTE MOTIF RETURNS CLEARLY]
[BASS AND PAD STEADY]
[TINY DRUMS CONTINUE]
[NO FILLS]

[1:40 CLEAR ENDING]
[FADE REEF PULSE]
[CLEAN ENDING]
[NO UI SOUND]
[NO COIN SOUND]
[NO POWER UP SOUND]
```

---

## Working Example: Rainfield Ambient / Wet Signal District

### Lyrics Box Arrangement Template

```text
[INSTRUMENTAL ONLY]
[NO VOCALS]
[NO SINGING]
[NO SPOKEN WORDS]
[NO LYRICS]
[NO CHOIR]
[NO VOCAL CHOPS]

[0:00 RAIN INTRO]
[SOFT PAD FADE IN]
[DISTANT STATION CHORD]
[LOW SUB BASS WARMTH]
[NO DRUMS]
[MOOD: EMPTY TRANSIT PLATFORM]

[0:30 FIRST GLOW]
[SOFT FM BELLS]
[TEAL TAPETUM SHIMMER]
[MAGENTA REFLECTIONS]
[WET PAVEMENT REVERB]
[NO VOCAL TEXTURE]

[1:00 MAIN DRIFT]
[LONG CINEMATIC PAD]
[GENTLE SQUARE WAVE UNDERCURRENT]
[DISTANT CRT HUM]
[MOOD: RAINLIT CIVIC LONELINESS]
[NO BEAT DROP]

[1:40 SECOND DRIFT]
[STATION CHORDS WIDEN]
[SOFT FM BELL ANSWERS]
[SUB BASS STAYS LOW]
[NO CHOIR]
[NO VOCAL PAD]

[2:20 CLOSING PLATFORM]
[PAD THINS]
[BELLS FADE]
[RAINFIELD ATMOSPHERE REMAINS]
[CLEAN SLOW ENDING]
```

---

## Test Protocol

When testing a new instrumental:

```text
1. Generate with style box only.
2. Generate with style box plus bracket-only lyrics box.
3. Generate with style box plus shorter bracket-only lyrics box.
4. Generate with style box plus bracket-only lyrics box plus Exclude field.
```

Listen for:

```text
vocal leakage
spoken-word leakage
whether structure improves
whether motif control improves
whether the ending behaves correctly
whether the style box identity survives the longer arrangement
```

---

## Search Tags

```text
Suno
Suno instrumental arrangement protocol
instrumental lyrics box
bracket-only lyrics box
bracketed arrangement
instrumental arrangement map
no vocals
no lyrics
no spoken words
Enum Rage Engine
Wet Signal District
Pulse Width Music
PWM
Worldskin BGM
Blue Hole Reef
Into the Blue
music-only BGM
Suno production note
```
