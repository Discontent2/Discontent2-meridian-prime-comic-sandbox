# test2 Channel Role Report

Generated from `red_warrant_vgm_register_lens.py` output.

## Executive Summary

- **FM1**: **rhythm / rapid pulse** (high confidence).
- **FM2**: **bass / low pedal** (medium confidence).
- **FM3**: **rhythm / rapid pulse** (low confidence).
- **FM4**: **expressive lead / melody** (high confidence).
- **FM5**: **bass / low pedal** (medium confidence).
- **FM6**: **expressive lead / melody** (high confidence).

## Channel Feature Table

| Channel | Inferred Role | Conf. | Notes | Pitch Events | Notes/Sec | MIDI Median | MIDI p10-p90 | Median Dur | Inst Groups |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|
| FM1 | rhythm / rapid pulse | high | 7938 | 0 | 46.911 | 77.5 | 32.0 to 115.0 | 0.001247 | 1 |
| FM2 | bass / low pedal | medium | 3788 | 0 | 22.386 | 44.0 | 32.0 to 82.0 | 0.002494 | 2 |
| FM3 | rhythm / rapid pulse | low | 409 | 0 | 2.417 | 60.0 | 32.0 to 82.0 | 0.001247 | 5 |
| FM4 | expressive lead / melody | high | 2516 | 1773 | 14.869 | 56.0 | 38.5 to 106.0 | 0.003741 | 14 |
| FM5 | bass / low pedal | medium | 653 | 0 | 3.859 | 46.0 | 44.0 to 48.0 | 0.099773 | 9 |
| FM6 | expressive lead / melody | high | 594 | 716 | 3.51 | 67.0 | 38.0 to 79.0 | 0.049887 | 10 |

## Per-Channel Notes

### FM1 — rhythm / rapid pulse

**Confidence:** high  
**Score:** 5.0  
**Runner-up:** rapid arpeggio / register animation (3.8)

Evidence:
- Median pitch is MIDI 77.5 with p10-p90 32.0 to 115.0.
- 7938 notes at 46.91 notes/sec.
- Median duration 0.001247 sec; short-note ratio 0.944.
- 1 instrument groups; top note B8 appears in 0.056 of notes.
- Runner-up role score: rapid arpeggio / register animation (3.8)

All role scores:
- rhythm / rapid pulse: 5.0
- rapid arpeggio / register animation: 3.8
- percussion / hat-noise / auxiliary: 1.0
- expressive lead / melody: 0.8
- bass / low pedal: 0.7

### FM2 — bass / low pedal

**Confidence:** medium  
**Score:** 3.8  
**Runner-up:** rhythm / rapid pulse (3.3)

Evidence:
- Median pitch is MIDI 44.0 with p10-p90 32.0 to 82.0.
- 3788 notes at 22.39 notes/sec.
- Median duration 0.002494 sec; short-note ratio 0.639.
- 2 instrument groups; top note C2 appears in 0.303 of notes.
- Runner-up role score: rhythm / rapid pulse (3.3)

All role scores:
- bass / low pedal: 3.8
- rhythm / rapid pulse: 3.3
- rapid arpeggio / register animation: 1.1
- percussion / hat-noise / auxiliary: 1.0

### FM3 — rhythm / rapid pulse

**Confidence:** low  
**Score:** 2.4  
**Runner-up:** expressive lead / melody (1.3)

Evidence:
- Median pitch is MIDI 60.0 with p10-p90 32.0 to 82.0.
- 409 notes at 2.42 notes/sec.
- Median duration 0.001247 sec; short-note ratio 0.807.
- 5 instrument groups; top note D#5 appears in 0.083 of notes.
- Runner-up role score: expressive lead / melody (1.3)

All role scores:
- rhythm / rapid pulse: 2.4
- expressive lead / melody: 1.3
- sustain / harmony bed: 1.3
- rapid arpeggio / register animation: 1.1

### FM4 — expressive lead / melody

**Confidence:** high  
**Score:** 6.0  
**Runner-up:** lead FX / bend lane (3.8)

Evidence:
- 1773 pitch events, 0.705 per note.
- Median pitch is MIDI 56.0 with p10-p90 38.5 to 106.0.
- 2516 notes at 14.87 notes/sec.
- Median duration 0.003741 sec; short-note ratio 0.601.
- 14 instrument groups; top note G3 appears in 0.099 of notes.
- Runner-up role score: lead FX / bend lane (3.8)

All role scores:
- expressive lead / melody: 6.0
- lead FX / bend lane: 3.8
- rhythm / rapid pulse: 2.0
- rapid arpeggio / register animation: 1.1

### FM5 — bass / low pedal

**Confidence:** medium  
**Score:** 3.1  
**Runner-up:** percussion / hat-noise / auxiliary (2.9)

Evidence:
- Median pitch is MIDI 46.0 with p10-p90 44.0 to 48.0.
- 653 notes at 3.86 notes/sec.
- Median duration 0.099773 sec; short-note ratio 0.0.
- 9 instrument groups; top note C3 appears in 0.456 of notes.
- Runner-up role score: percussion / hat-noise / auxiliary (2.9)

All role scores:
- bass / low pedal: 3.1
- percussion / hat-noise / auxiliary: 2.9
- sustain / harmony bed: 1.3
- expressive lead / melody: 1.2
- lead FX / bend lane: 0.8
- rhythm / rapid pulse: 0.7

### FM6 — expressive lead / melody

**Confidence:** high  
**Score:** 6.0  
**Runner-up:** lead FX / bend lane (3.8)

Evidence:
- 716 pitch events, 1.205 per note.
- Median pitch is MIDI 67.0 with p10-p90 38.0 to 79.0.
- 594 notes at 3.51 notes/sec.
- Median duration 0.049887 sec; short-note ratio 0.241.
- 10 instrument groups; top note G4 appears in 0.106 of notes.
- Runner-up role score: lead FX / bend lane (3.8)

All role scores:
- expressive lead / melody: 6.0
- lead FX / bend lane: 3.8
- sustain / harmony bed: 0.8
- percussion / hat-noise / auxiliary: 0.7

## Red Warrant Usage Notes

- Treat this as a role lens, not a riff copier.
- A bass candidate should show low median pitch, few instrument groups, low pitch-event ratio, and steady timing.
- A lead candidate should show wider pitch range, more pitch events, and more instrument-group/behavior variation.
- A hat/noise candidate should usually show short notes, repeated high-register hits, and restricted pitch vocabulary.
- If the report says a lane is `rapid arpeggio / register animation`, do not translate it directly into bass. Decide whether it is musical arpeggiation, tracker trickery, or parser-visible pitch churn.
- For Red Warrant Test 28A specifically, this supports our current split: bass should be stable; guitar and lead lanes should carry modulation and expressive movement.
