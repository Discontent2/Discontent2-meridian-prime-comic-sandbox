# Azgaar Schema Notes

**Status:** Phase 2 Schema Orientation / Sandbox Tooling  
**Project:** Meridian Prime Cartography Engine / Azgaar Fork  
**Related Roadmap:** `docs/cartography/azgaar-fork/meridian-prime-cartography-engine-roadmap.md`  
**Related Source Map:** `docs/cartography/azgaar-fork/source-map-notes.md`  
**Azgaar Baseline Commit Studied:** `9d14cf78791484ea23936aff26807fc2503b3252`  
**Last Updated:** 2026-06-20  
**Do Not Canonize From This File:** This is tooling documentation, not lore canon.  

---

## Purpose

This file captures the first schema/data-flow orientation for Azgaar systems relevant to a Meridian Prime-aware cartography engine.

Focus areas:

- `pack` and `grid`
- `pack.markers`
- marker notes
- save/load slots
- layers and SVG groups
- export formats
- proposed Meridian Prime metadata shape

This file does not authorize implementation yet. It is a schema lantern, not a source-code pickaxe.

---

## High-Level Data Model

Azgaar currently uses two central global data objects:

| Object | Role |
|---|---|
| `grid` | Pre-repacking map data, based on the original jittered grid / Voronoi structure. |
| `pack` | Post-repacking map data used by most map behavior and most features. |

For Meridian Prime work, `pack` is the first object to understand because markers, routes, zones, burgs, states, cultures, rivers, and many editable map features live there.

Relevant `pack` members from source/type orientation:

```ts
pack.features
pack.cultures
pack.burgs
pack.states
pack.provinces
pack.religions
pack.rivers
pack.markers
pack.routes
pack.zones
pack.goods
pack.markets
pack.deals
pack.cells.routes
```

Important caution:

> `pack.markers` is currently typed as `any[]` in `src/types/PackedGraph.ts`, which gives flexibility but also means we need our own metadata discipline.

---

## Marker Schema Orientation

### Observed generated marker fields

From `src/modules/markers-generator.ts`, generated marker data uses fields like:

```ts
{
  i: number,
  type: string,
  icon: string,
  cell: number,
  x: number,
  y: number,
  dx?: number,
  dy?: number,
  px?: number,
  lock?: boolean
}
```

Generation behavior:

- `Markers.generate()` clears `pack.markers` before generating.
- `Markers.regenerate()` preserves locked markers and removes unlocked markers.
- `Markers.add(marker)` can add configured or custom markers.
- Marker ids are numeric `i` values.
- Marker SVG ids are `marker${i}`.
- Marker notes use matching ids such as `marker12`.

### Observed rendered marker fields

From `src/renderers/draw-markers.ts`, rendering expects or supports fields like:

```ts
{
  i: number,
  icon: string,
  x: number,
  y: number,
  name?: string,
  type?: string,
  dx?: number,
  dy?: number,
  px?: number,
  size?: number,
  pin?: string,
  fill?: string,
  stroke?: string,
  pinned?: boolean,
  hidden?: boolean
}
```

Rendering behavior:

- `drawMarkers()` reads `pack.markers`.
- If the marker layer is set to show only pinned markers, only `marker.pinned` entries render.
- `drawMarker(marker)` creates an SVG element with id `marker${i}`.
- External marker icons are allowed if `icon` starts with `http` or `data:image`.

### Observed UI-editable marker fields

From marker editor and overview behavior, marker UI can modify:

```ts
type
icon
px
dx
dy
size
pin
fill
stroke
lock
pinned
x
y
cell
```

Marker position changes:

- Dragging updates `marker.x` and `marker.y`.
- Dragging recalculates `marker.cell` via `findCell(marker.x, marker.y)`.

Marker notes:

- Marker notes are not embedded in the marker object by default.
- They live in the global `notes` array.
- Marker note id convention is `note.id === "marker" + marker.i`.

---

## Marker Notes Schema

Observed use:

```js
notes.push({
  id: "marker12",
  name: "Example Name",
  legend: "Example note text."
});
```

Important behavior:

- Removing a marker often removes matching notes.
- Marker CSV export joins marker data to notes by marker id.
- Save/load serializes and restores `notes` separately from `pack.markers`.

Meridian Prime implication:

> Notes are useful for human-readable marker text, but protected metadata should not live only in `notes.legend`. A structured metadata field is safer for search/export and less likely to become prose soup.

---

## Save / Load Slot Orientation

Azgaar `.map` data is a CRLF-delimited list of sections.

Important observed slots:

| Slot | Meaning |
|---|---|
| `data[0]` | version/license/date/seed/width/height/map id params |
| `data[1]` | settings |
| `data[2]` | map coordinates |
| `data[3]` | biomes |
| `data[4]` | `notes` |
| `data[5]` | serialized SVG |
| `data[6]` | grid general data |
| `data[12]` | `pack.features` |
| `data[13]` | `pack.cultures` |
| `data[14]` | `pack.states` |
| `data[15]` | `pack.burgs` |
| `data[29]` | `pack.religions` |
| `data[30]` | `pack.provinces` |
| `data[32]` | `pack.rivers` |
| `data[35]` | `pack.markers` |
| `data[36]` | `pack.cells.routes` |
| `data[37]` | `pack.routes` |
| `data[38]` | `pack.zones` |
| `data[39]` | `pack.ice` |
| `data[41]` | `pack.goods` |
| `data[42]` | `pack.markets` |
| `data[43]` | `pack.deals` |

Save/load caution:

> Do not change existing slot order. Slot order is part of `.map` compatibility.

Meridian Prime implication:

- Unknown marker object fields may survive save/load because `pack.markers` is JSON-stringified and parsed.
- This must be tested before relying on it.
- If unknown fields survive, a nested marker metadata object is preferable to many top-level custom fields.

---

## Layer Schema / SVG Group Orientation

Layer state uses two connected concepts:

1. UI layer toggle ids, such as `toggleMarkers`, `toggleRoutes`, `toggleZones`.
2. SVG groups, such as `#markers`, `#routes`, `#zones`.

Observed mappings include:

| Toggle id | SVG group |
|---|---|
| `toggleMarkers` | `#markers` |
| `toggleRoutes` | `#routes` |
| `toggleZones` | `#zones` |
| `toggleLabels` | `#labels` |
| `toggleBurgIcons` | `#icons` |
| `toggleStates` | `#regions` |
| `toggleBorders` | `#borders` |

Layer presets are arrays of toggle ids.

The `poi` preset includes:

```js
toggleBorders
toggleBurgIcons
toggleHeight
toggleIce
toggleLakes
toggleMarkers
toggleRivers
toggleRoutes
toggleScaleBar
toggleVignette
```

The layer system determines current state mainly through UI button classes and SVG contents.

Meridian Prime implication:

> Existing markers/routes/zones layers should be used first. A new Meridian Prime layer can come later, after the toggle/preset/SVG-order behavior is mapped and regression-tested.

---

## Export Schema Orientation

### Marker CSV Export

Current marker CSV columns:

```text
Id,Type,Icon,Name,Note,X,Y,Latitude,Longitude
```

Source behavior:

- Iterates over `pack.markers`.
- Joins note name/legend through `notes.find(note => note.id === "marker" + i)`.
- Writes lat/lon via `getLatitude(y, 2)` and `getLongitude(x, 2)`.

Meridian Prime potential:

Add later columns such as:

```text
MP_Status,MP_MarkerType,MP_CanonRisk,MP_UseTier,MP_Tags,MP_SourceFile,MP_Guardrail
```

Only after metadata survival is tested.

---

### JSON Export

Current JSON export types:

| Export type | Contents |
|---|---|
| Full | info, settings, mapCoordinates, pack, grid, biomesData, notes, nameBases |
| Minimal | info, settings, mapCoordinates, selected pack arrays/objects, biomesData, notes, nameBases |
| PackCells | info, cell-level pack data plus pack features, cultures, burgs, states, provinces, religions, rivers, goods, markers, markets, deals, routes, zones |
| GridCells | info and grid cell data |

Important fields already included in JSON exports:

```js
pack.markers
pack.routes
pack.zones
notes
```

Meridian Prime implication:

> A future Meridian Prime receipt exporter may use the existing JSON export path as a model, or add a narrow custom exporter that writes only markers/routes/zones/notes plus Meridian Prime metadata.

---

### Visual Export

Visual export includes:

- SVG
- PNG
- JPEG
- PNG tiles
- GeoJSON cells

Observed marker export detail:

- SVG export clones the map SVG.
- It converts external marker icons to base64 for exported SVG.
- Hidden/unused groups can be removed from exported SVG.

Meridian Prime implication:

> Visual export should show Meridian Prime markers if they are visible in `#markers`, but protected metadata should not be embedded into SVG visual output unless intentionally designed.

---

## Proposed Meridian Prime Marker Metadata Shape

Preferred first test shape:

```js
marker.meridianPrime = {
  schema_version: 1,
  marker_type: "Sanctuary",
  status: "Sandbox",
  canon_risk: "Medium",
  use_tier: "Tier 2 Working",
  source_file: "docs/...",
  room_source: "Cartography Engine Room",
  faction: "World Works Corp",
  associated_npcs: [],
  associated_encounters: [],
  associated_locations: [],
  associated_sanctuaries: [],
  protected_mystery_guardrail: "Does not define protected truth.",
  spoiler_visibility: "public-safe",
  tags: ["sanctuary", "route-pressure"],
  notes: "Tooling-only metadata note.",
  last_reviewed: "2026-06-20"
};
```

Reason for nested object:

- Keeps Meridian Prime data namespaced.
- Avoids cluttering Azgaar marker top-level fields.
- Makes export/search easier.
- Makes cleanup easier if the approach is abandoned.

Caution:

- Must test whether nested unknown fields survive `.map` save/load.
- Must test whether nested unknown fields survive JSON export.
- Must test marker editor behavior after metadata is attached.

---

## Metadata Survival Test Plan

Do this in a disposable test map or feature branch only.

1. Open local Azgaar dev instance.
2. Create or select one marker.
3. In dev console, attach:

```js
pack.markers[0].meridianPrime = {
  schema_version: 1,
  marker_type: "Test Marker",
  status: "Sandbox",
  canon_risk: "Low",
  tags: ["mp-test"],
  protected_mystery_guardrail: "Test only. No canon."
};
```

4. Save `.map`.
5. Reload the saved `.map`.
6. Check:

```js
pack.markers[0].meridianPrime
```

7. Export Minimal JSON.
8. Confirm the metadata appears under `pack.markers`.
9. Run `npm run build`.
10. Confirm `git status --short` is clean.

Pass condition:

> Nested marker metadata survives save/load and JSON export without breaking UI or build.

Fail condition:

> Metadata disappears, breaks marker editor/overview, breaks save/load, or causes build/runtime errors.

---

## Candidate Receipt Fields

A Meridian Prime marker receipt can eventually normalize data into:

```yaml
name: Soft Gate Orchard
azgaar_marker_id: marker12
marker_type: World Works Site
status: Sandbox
canon_risk: High
use_tier: Tier 4 Restricted
source_file: docs/story/chance-game/encounter-seeds/world-works/verdant-contact-walker-soft-gate-orchard-deployment.md
room_source: Cartography Engine Room
faction: World Works Corp
associated_entities:
  - The Verdant Contact Walker
  - The Verdant Chimera
protected_mystery_guardrail: Does not define Dry Gate truth.
spoiler_visibility: restricted
x: 123.4
y: 567.8
latitude: 12.34
longitude: -56.78
tags:
  - project-green-glove
  - worldskin-prototype
  - false-sanctuary
  - dry-gate-pressure
```

This should be generated from map data, not hand-maintained where possible.

---

## Risks

| Risk | Why it matters | Avoidance |
|---|---|---|
| Breaking `.map` compatibility | Save/load slots are positional. | Do not change existing slot order. |
| Metadata loss | Unknown marker fields might not survive every operation. | Run survival test before relying on metadata. |
| Marker regeneration deletion | Unlocked generated markers can be removed. | Use locked markers or separate metadata index. |
| Notes coupling | Notes are separate from markers and removed by marker deletion. | Do not store structured metadata only in notes. |
| Protected truth leakage | Maps can accidentally canonize secrets. | Use pressure/rumor wording and guardrails. |
| UI clutter | Adding too much to marker editor early can destabilize legacy UI. | Start with export/search before editor changes. |

---

## Phase 2 Conclusion

The early safe path is:

1. Keep using Azgaar's existing `#markers`, `#routes`, and `#zones` layers.
2. Test nested metadata inside `pack.markers`.
3. Extend export/search only after survival is proven.
4. Avoid changing `.map` slot order.
5. Avoid new generation tables until the marker schema is stable.

No source customization yet.
