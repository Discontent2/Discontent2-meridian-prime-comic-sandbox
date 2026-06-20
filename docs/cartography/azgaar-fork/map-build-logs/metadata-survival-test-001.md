# Metadata Survival Test 001

**Status:** Passed  
**Project:** Meridian Prime Cartography Engine / Azgaar Fork  
**Test Type:** Phase 2 Source Orientation / Map Data Survival Test  
**Azgaar Baseline Commit:** `9d14cf78791484ea23936aff26807fc2503b3252`  
**Local Test Folder:** `/home/tenet/meridian-cartography-baseline/Fantasy-Map-Generator`  
**Last Updated:** 2026-06-20  
**Do Not Canonize From This File:** This is tooling documentation, not lore canon.  

---

## Purpose

Test whether a nested Meridian Prime metadata object attached to an Azgaar marker survives:

1. in-memory attachment,
2. `.map` save and reload,
3. JSON serialization / export,
4. production build,
5. clean working tree verification.

No source code was customized for this test.

---

## Metadata Shape Tested

```js
marker.meridianPrime = {
  schema_version: 1,
  marker_type: "Metadata Survival Test",
  status: "Sandbox",
  canon_risk: "Low",
  use_tier: "Test Only",
  room_source: "Cartography Engine Room",
  tags: ["mp-test", "metadata-survival"],
  protected_mystery_guardrail: "Test only. No canon. Does not define protected truth.",
  spoiler_visibility: "public-safe",
  last_reviewed: "2026-06-20"
};
```

A temporary marker note was also attached using the standard Azgaar marker-note id convention:

```js
notes.push({
  id: `marker${marker.i}`,
  name: "MP Metadata Survival Test",
  legend: "Temporary map-data test marker. Not canon."
});
```

---

## Results

| Check | Result | Notes |
|---|---|---|
| In-memory console attach | Pass | Console confirmed metadata was attached to marker `0`. |
| Console lookup after attach | Pass | `pack.markers.find(m => m.meridianPrime?.tags?.includes("mp-test"))?.meridianPrime` returned the metadata object. |
| `.map` save | Pass | User confirmed save completed. |
| `.map` reload | Pass | User confirmed metadata survived after loading the saved `.map`. |
| JSON serialization check | Pass | `JSON.stringify({ markers: pack.markers, notes }).includes("metadata-survival")` returned `true`. |
| Exported JSON check | Pass | User confirmed `metadata-survival` was present in exported JSON. |
| Production build | Pass | `npm run build` exit code was `0`. |
| Final git status | Pass | `git status --short` returned nothing. |

---

## Verdict

**Passed.**

Nested Meridian Prime metadata attached as `marker.meridianPrime` survived save/load and appeared in JSON export without source-code changes, build failure, or working tree changes.

---

## Implications

The first Meridian Prime-aware prototype can safely assume, pending continued regression testing, that marker-level metadata can live inside a nested marker field:

```js
marker.meridianPrime
```

This supports a low-risk first customization path:

1. Extend marker search/export behavior to recognize `marker.meridianPrime`.
2. Avoid changing `.map` slot order.
3. Avoid creating a new layer until existing marker/route/zone layer behavior is further tested.
4. Continue using existing marker rendering fields for visual display.

---

## Recommended Next Step

Choose the first source customization path:

### Option A: Export-only first

Add Meridian Prime-aware columns to marker CSV or a separate Meridian Prime marker receipt export.

Pros:

- Lowest UI risk.
- Immediately useful for repo-integrated indexes.
- Does not require changing marker editor behavior.

### Option B: Search-only first

Extend marker overview search to search type, note name, note legend, and `marker.meridianPrime.tags`.

Pros:

- Makes maps easier to use during development.
- Small modification point.

### Option C: Metadata editor first

Add UI fields for Meridian Prime metadata.

Pros:

- More comfortable long-term editing.

Risks:

- Highest early UI risk because marker editor is legacy JavaScript and already manages many fields.

Recommended first source change:

> Export-only first, then search-only.

---

## Guardrail

This test does not canonize any location, marker, faction relationship, route, protected mystery, or story truth.

The tested metadata is sandbox tooling metadata only.
