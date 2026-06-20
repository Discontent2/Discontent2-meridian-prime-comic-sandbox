# Export-First / Search-Second Implementation Plan

**Status:** Phase 3 Prototype Plan / Sandbox Tooling  
**Project:** Meridian Prime Cartography Engine / Azgaar Fork  
**Related Roadmap:** `docs/cartography/azgaar-fork/meridian-prime-cartography-engine-roadmap.md`  
**Related Test:** `docs/cartography/azgaar-fork/map-build-logs/metadata-survival-test-001.md`  
**Target Local Source File:** `public/modules/ui/markers-overview.js`  
**Last Updated:** 2026-06-20  
**Do Not Canonize From This File:** This is tooling documentation, not lore canon.  

---

## Decision

Proceed with the first Meridian Prime-aware source customization in this order:

1. **Export-only first.**
2. **Search-only second.**

No marker editor UI changes yet.
No new SVG layer yet.
No `.map` save-slot changes.

---

## Reason

Metadata Survival Test 001 passed. A nested `marker.meridianPrime` object survived:

- in-memory attachment,
- `.map` save/load,
- JSON serialization/export,
- production build,
- clean working tree check.

This means the safest first prototype is to let existing marker data become more useful through export and search, rather than changing how markers are created or edited.

---

## Source Target

Initial customization target:

`public/modules/ui/markers-overview.js`

Why this file:

- It already lists `pack.markers`.
- It already searches marker `type`.
- It already exports marker CSV.
- It joins marker notes by `note.id === "marker" + i`.
- It is a narrow modification point compared to save/load, rendering, or marker generation.

---

## Step 1: Export-Only Patch

Modify only `exportMarkers()` first.

Goal:

- Preserve existing CSV behavior.
- Add Meridian Prime-aware columns when `marker.meridianPrime` exists.
- Leave blank columns when metadata does not exist.
- Do not change marker rendering, editing, generation, or save/load.

Suggested extra CSV columns:

```text
MP_SchemaVersion
MP_MarkerType
MP_Status
MP_CanonRisk
MP_UseTier
MP_SourceFile
MP_RoomSource
MP_Faction
MP_AssociatedNPCs
MP_AssociatedEncounters
MP_AssociatedLocations
MP_AssociatedSanctuaries
MP_Tags
MP_Guardrail
MP_SpoilerVisibility
MP_LastReviewed
MP_MetadataNotes
```

Pass criteria:

- Markers CSV exports successfully.
- A test marker with `metadata-survival` appears in the CSV.
- Normal markers without Meridian Prime metadata still export.
- `npm run build` exits `0`.
- `git status --short` shows only the expected modified file before commit.

---

## Step 2: Search-Only Patch

After export-only passes, extend marker overview search.

Search should include:

- marker type,
- marker icon,
- note name,
- note legend,
- `marker.meridianPrime.marker_type`,
- `marker.meridianPrime.status`,
- `marker.meridianPrime.canon_risk`,
- `marker.meridianPrime.use_tier`,
- `marker.meridianPrime.source_file`,
- `marker.meridianPrime.room_source`,
- `marker.meridianPrime.faction`,
- `marker.meridianPrime.tags`,
- `marker.meridianPrime.protected_mystery_guardrail`,
- `marker.meridianPrime.spoiler_visibility`.

Pass criteria:

- Searching `metadata-survival` finds the test marker.
- Searching `mp-test` finds the test marker.
- Searching the note name finds the test marker.
- Normal marker type search still works.
- `npm run build` exits `0`.
- `git status --short` shows only expected files before commit.

---

## Recommended Branching

Local branch name:

```bash
git checkout -b mp-marker-export-search-001
```

Suggested commits:

1. `Add Meridian Prime marker metadata CSV export`
2. `Search Meridian Prime marker metadata in overview`

---

## Guardrails

Do not modify:

- `.map` save slot order,
- `public/modules/io/save.js`,
- `public/modules/io/load.js`,
- `src/modules/markers-generator.ts`,
- `src/renderers/draw-markers.ts`,
- marker editor UI fields,
- layer toggle structure.

For this prototype, the only target should be:

`public/modules/ui/markers-overview.js`

---

## Canon Note

This implementation plan is tooling-only.

Exported metadata remains sandbox unless separately reviewed and promoted.
