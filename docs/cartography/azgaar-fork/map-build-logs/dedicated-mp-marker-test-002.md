# Dedicated Meridian Prime Marker Test 002

**Status:** Passed  
**Project:** Meridian Prime Cartography Engine / Azgaar Fork  
**Test Type:** Dedicated Marker Protocol / Visible Search + Structured Metadata  
**Related Tests:**
- `docs/cartography/azgaar-fork/map-build-logs/metadata-survival-test-001.md`
- `docs/cartography/azgaar-fork/map-build-logs/visible-export-panel-test-001.md`

**Last Updated:** 2026-06-20  
**Do Not Canonize From This File:** This is tooling documentation, not lore canon.  

---

## Purpose

Test a cleaner Meridian Prime marker protocol:

1. Create a dedicated Azgaar marker for Meridian Prime use.
2. Use visible Azgaar fields for human-facing search and editing.
3. Attach nested `marker.meridianPrime` metadata for structured export/tooling.
4. Save and reload the map.
5. Confirm both visible marker search and nested metadata survive.

---

## Reason for Protocol Change

The earlier search-only source patch targeted `public/modules/ui/markers-overview.js`, but runtime testing showed that patching the hidden/secondary overview route was not the best first usability path.

The user discovered a better convention:

> Create a dedicated Meridian Prime marker instead of hiding Meridian Prime metadata on a generated Azgaar marker type such as `volcanoes`.

This allows Azgaar's existing visible marker type search to work without source customization.

---

## Marker Created

Dedicated marker id observed in the UI:

```text
marker69
```

Visible Azgaar marker type:

```text
mp-metadata-test
```

Note name:

```text
MP Metadata Survival Test 002
```

Note body:

```text
Tags: mp-test, metadata-survival, test-002

Status: Sandbox

Canon risk: Low

Guardrail: Test only. No canon.
```

Nested marker metadata attached in browser console:

```js
marker.meridianPrime = {
  schema_version: 1,
  marker_type: "Metadata Survival Test 002",
  status: "Sandbox",
  canon_risk: "Low",
  use_tier: "Test Only",
  room_source: "Cartography Engine Room",
  tags: ["mp-test", "metadata-survival", "test-002"],
  protected_mystery_guardrail: "Test only. No canon.",
  spoiler_visibility: "public-safe",
  last_reviewed: "2026-06-20"
};
```

---

## Checks Performed

The user confirmed:

| Check | Result | Notes |
|---|---|---|
| Console attach to marker `69` | Pass | Both direct marker lookup and tag lookup returned objects. |
| `.map` save/load | Pass | Metadata survived after saving and loading the map. |
| Direct metadata lookup after reload | Pass | `pack.markers.find(m => m.i === 69).meridianPrime` returned an object. |
| Tag lookup after reload | Pass | `pack.markers.find(m => m.meridianPrime?.tags?.includes("test-002"))` returned an object. |
| Visible marker search by type | Pass | `mp-metadata-test` worked in the Markers panel. |
| Visible search by metadata phrase | Pass | `metadata-survival` also worked according to user confirmation. |

---

## Verdict

**Passed.**

The cleanest early Meridian Prime marker protocol is:

1. Use a dedicated Azgaar marker per Meridian Prime point.
2. Put a searchable Meridian Prime type in the visible marker `type` field.
3. Put human-readable metadata and tags in the marker note.
4. Store structured metadata in `marker.meridianPrime`.
5. Use the visible Export map data panel for GeoJSON markers and Minimal JSON exports.

---

## Recommended Working Convention

For each Meridian Prime point, use:

```text
Marker type: mp-[short-purpose]
Note name: MP [clear title]
Note body:
  Tags: [comma-separated tags]
  Status: Sandbox / Candidate Canon / Canon Review Needed
  Canon risk: Low / Medium / High
  Guardrail: [short safety note]
```

And attach a matching structured payload:

```js
marker.meridianPrime = {
  schema_version: 1,
  marker_type: "...",
  status: "Sandbox",
  canon_risk: "Low",
  use_tier: "...",
  room_source: "Cartography Engine Room",
  tags: ["..."],
  protected_mystery_guardrail: "...",
  spoiler_visibility: "public-safe",
  last_reviewed: "YYYY-MM-DD"
};
```

---

## Source Code Status

No source customization is required for this protocol.

If any local search patch remains, it should not be committed unless specifically revived later.

Recommended local check:

```bash
git status --short
```

Expected clean result:

```text
# no output
```

---

## Next Recommended Step

Create a small reusable console helper for adding/updating Meridian Prime metadata on the currently selected or specified marker.

Possible helper goals:

- prompt for marker id,
- set visible marker type,
- update note name/body,
- attach `marker.meridianPrime`,
- print verification commands,
- keep all changes inside map data, not source code.

---

## Canon Safety

This test is tooling-only.

It does not canonize the marker, map location, geography, route, faction relationship, protected mystery, or story truth.
