# Meridian Prime Reels Production Workspace

**Repository role:** persistent working memory for Meridian Prime short-form video production.

This directory stores production-specific decisions that should survive beyond any single chat session: edit maps, shot records, generation prompts, image-to-video motion directives, audio cue maps, CapCut settings, source-asset manifests, export history, and status notes.

## Boundary with the rest of the repository

- `production/reels/` = project-specific working production records.
- `docs/prompt-library/` = reusable prompt techniques worth generalizing.
- `docs/music/` = reusable or promoted music/soundtrack records.
- `docs/development/` and other lore folders = worldbuilding and candidate-canon material.
- `Discontent2/meridian-prime` = promoted canon, not experimental reel production.

## Evidence labels

Every reconstructed production package should distinguish:

1. **Recovered Exact**: wording, timing, setting, or filename recovered directly from prior work.
2. **Recovered / Approved Summary**: the prior approved decision is recoverable, but not every original word survives.
3. **Reconstructed**: rebuilt from locked decisions, final assets, or later notes. Never present reconstructed wording as the original prompt.

## Asset rule

Prefer committing text, settings, manifests, small reference images, and decision history. Do not use ordinary Git history as a dumping ground for large MP4/WAV generations. Keep original masters externally or use an appropriate large-file workflow when needed.
