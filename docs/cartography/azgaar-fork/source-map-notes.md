# Azgaar Source Map Notes

**Status:** Phase 2 Source Orientation / Sandbox Tooling  
**Project:** Meridian Prime Cartography Engine / Azgaar Fork  
**Related Roadmap:** `docs/cartography/azgaar-fork/meridian-prime-cartography-engine-roadmap.md`  
**Related Schema Notes:** `docs/cartography/azgaar-fork/schema/schema-notes.md`  
**Azgaar Baseline Commit Studied:** `9d14cf78791484ea23936aff26807fc2503b3252`  
**Last Updated:** 2026-06-20  
**Do Not Canonize From This File:** This is tooling documentation, not lore canon.  

---

## Purpose

This file maps the first relevant Azgaar source-code corridors for Meridian Prime cartography work.

Scope of this orientation pass:

- marker generation
- marker rendering
- marker editing / overview
- save/load behavior
- layer toggles and layer ordering
- export behavior

This is not an implementation plan yet. It is the candle-lit tunnel map before anyone swings a pickaxe.

---

## Baseline Status

Phase 1 baseline passed before this source-orientation pass.

Confirmed baseline facts:

- Local clone ran successfully.
- Node `v24.17.0` and npm `11.13.0` were used.
- Azgaar app opened locally at `http://localhost:5173/Fantasy-Map-Generator/`.
- A map generated.
- Markers, routes, and zones appeared in the layer panel.
- `.map` save and reload worked.
- `npm run build` returned exit code `0`.
- `git status --short` returned no output.

No Meridian Prime source customization has been made yet.

---

## Source Architecture Snapshot

Azgaar is currently a mixed-codebase application:

- Newer TypeScript source exists under `src/`.
- Legacy/public runtime modules still exist under `public/modules/`.
- Several important UI and IO systems still live in legacy JavaScript files.
- The map data model still relies heavily on globals, especially `grid`, `pack`, `notes`, and many SVG group globals.

Official architecture docs say the FMG data model is not fully consistent or fully documented, and that most map data is exposed through global namespace objects. The two central map-data objects are:

- `grid`: pre-repacking map data.
- `pack`: post-repacking map data used for most map behavior.

Meridian Prime implication:

> Additions should begin as small, low-impact metadata extensions near existing marker/export systems, not as a deep rewrite of Azgaar's data model.

---

## Source Anchors Studied

| System | Primary files | Notes |
|---|---|---|
| Marker generation | `src/modules/markers-generator.ts` | Generates `pack.markers`, default marker types, candidate cells, marker notes. |
| Marker rendering | `src/renderers/draw-markers.ts` | Renders markers from `pack.markers` into SVG elements under `#markers`. |
| Marker editing | `public/modules/ui/markers-editor.js` | Edits marker type, icon, pin, color, lock status, drag position, notes. |
| Marker overview / CSV export | `public/modules/ui/markers-overview.js` | Lists, searches, pins, locks, regenerates, deletes, and exports markers to CSV. |
| Layer control | `public/modules/ui/layers.js` | Defines presets, toggles layers, draws active layers, maps UI toggles to SVG groups. |
| Save | `public/modules/io/save.js` | Serializes the `.map` project, including SVG, notes, markers, routes, zones. |
| Load | `public/modules/io/load.js` | Parses `.map` / `.gz`, rebuilds globals, restores SVG groups, reloads markers/routes/zones. |
| JSON export | `public/modules/dynamic/export-json.js` | Exports full/minimal/pack/grid JSON; includes `pack.markers`, `pack.routes`, `pack.zones`, `notes`. |
| Image/data export | `public/modules/io/export.js` | Exports SVG, PNG, JPEG, tiles, GeoJSON; handles external marker images during SVG export. |
| Pack type orientation | `src/types/PackedGraph.ts` | `pack.markers` is currently typed as `any[]`; routes and zones have typed array entries. |

---

## Marker System Orientation

### Generation

Marker generation lives mainly in:

`src/modules/markers-generator.ts`

Key findings:

- Azgaar exposes a global `Markers` module.
- The module has configurable marker types with fields such as `type`, `icon`, `dx`, `dy`, `px`, `min`, `each`, `multiplier`, `list`, and `add`.
- `generate()` resets marker config, clears `pack.markers`, and generates all marker types.
- `regenerate()` preserves locked markers, removes unlocked markers and their notes, then regenerates types.
- `add(marker)` can either use a known configured marker type or add a custom marker directly.
- Generated markers are placed into `pack.markers`.
- Notes are connected by `id` strings like `marker${marker.i}`.

Initial marker object shape observed from generation:

```ts
{
  i: number,
  type: string,
  icon: string,
  cell: number,
  x?: number,
  y?: number,
  dx?: number,
  dy?: number,
  px?: number,
  lock?: boolean
}
```

Risk notes:

- `pack.markers` is regenerated and can be cleared by generation flows.
- Locked markers are preserved by regeneration, so Meridian Prime markers that must survive regeneration may need `lock: true` or a safer custom preservation mechanism.
- Notes attached to markers may be removed if marker ids are removed.
- Adding a marker type directly into the Azgaar generator config could make Meridian Prime data behave like normal procedural fantasy markers, which may be unsafe for protected mysteries.

Meridian Prime implication:

> The first Meridian Prime marker layer should not rely only on normal Azgaar marker generation. It should preserve metadata separately or use explicit sandbox marker creation with guardrails.

---

### Rendering

Marker rendering lives mainly in:

`src/renderers/draw-markers.ts`

Key findings:

- Rendered marker shape is simple SVG.
- `drawMarkers()` reads from `pack.markers`.
- If the marker group has `pinned` enabled, only `marker.pinned` items are rendered.
- `drawMarker(marker, rescale)` emits a marker SVG with id `marker${i}`.
- Renderer uses fields such as `i`, `icon`, `x`, `y`, `dx`, `dy`, `px`, `size`, `pin`, `fill`, and `stroke`.
- External icons are supported if `icon` starts with `http` or `data:image`.

Observed rendering-oriented marker shape:

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

Meridian Prime implication:

> The SVG renderer can likely display Meridian Prime markers without major surgery if we use existing fields. The larger question is where to store richer metadata without breaking save/load.

---

### Editing and Overview

Marker editing lives mainly in:

`public/modules/ui/markers-editor.js`

Key findings:

- Clicking a marker opens a marker editor.
- Marker editor can change marker type, icon, icon size, icon offsets, marker size, pin shape, fill, stroke, notes, and lock state.
- Dragging a marker updates marker `x`, `y`, and recalculates `cell` via `findCell(marker.x, marker.y)`.
- Marker notes are edited through `editNotes(id, id)` using marker SVG ids.

Marker overview lives mainly in:

`public/modules/ui/markers-overview.js`

Key findings:

- Overview lists `pack.markers`.
- Search currently filters only by marker `type`.
- Overview supports open editor, locate, pin, lock, remove, remove all, regenerate, and export.
- Marker CSV export currently writes: `Id,Type,Icon,Name,Note,X,Y,Latitude,Longitude`.
- CSV export joins marker data with notes by `note.id === "marker" + i`.

Meridian Prime implication:

> The marker overview is a likely first UI extension point for Meridian Prime filtering because it already searches marker types and exports marker CSV. A safe first improvement may be metadata-aware export without touching generation.

---

## Save / Load System Orientation

### Save

Save behavior lives mainly in:

`public/modules/io/save.js`

Key findings:

- `saveMap(method)` blocks save while in customization/edit mode.
- `prepareMapData()` builds the `.map` file as CRLF-delimited string sections.
- The save file includes settings, coordinates, biomes, notes, serialized SVG, grid data, pack data, markers, cell routes, routes, zones, ice, goods, markets, deals, and market cells.
- Markers are serialized via `JSON.stringify(pack.markers)`.
- Routes are serialized via `JSON.stringify(pack.routes)`.
- Zones are serialized via `JSON.stringify(pack.zones)`.
- Marker data is currently saved in the data slot after fonts/rulers and before cell routes/routes/zones.

Important current save slots from `prepareMapData()`:

| Data slot | Meaning |
|---|---|
| `data[4]` | `notes` |
| `data[5]` | serialized SVG |
| `data[35]` | `pack.markers` |
| `data[36]` | `pack.cells.routes` |
| `data[37]` | `pack.routes` |
| `data[38]` | `pack.zones` |

### Load

Load behavior lives mainly in:

`public/modules/io/load.js`

Key findings:

- Load accepts `.map`/`.gz` and can load from browser storage, file upload, Dropbox, or URL.
- Loaded result is decoded as a string, uncompressed if needed, then split by CRLF.
- Load version-checks and may auto-update old saves.
- `parseLoadedData()` rebuilds SVG and reassigns many global SVG group variables.
- `notes` are loaded from `data[4]`.
- `pack.markers` loads from `data[35]`, defaulting to `[]` if missing.
- `pack.routes` loads from `data[37]`, defaulting to `[]` if missing.
- `pack.zones` loads from `data[38]`, defaulting to `[]` if missing.
- `pack.cells.routes` loads from `data[36]`, defaulting to `{}` if missing.
- After SVG/group rebuilding, layer buttons are turned back on based on actual SVG group contents.

Meridian Prime implication:

> If Meridian Prime metadata is stored directly inside `pack.markers`, it may round-trip through `.map` save/load because markers are JSON serialized and parsed. But unknown fields need explicit testing before relying on them. A safer strategy may be `marker.mp` or `marker.meridianPrime` metadata plus a save/load regression test.

---

## Layer System Orientation

Layer behavior lives mainly in:

`public/modules/ui/layers.js`

Key findings:

- Layer presets are arrays of UI toggle ids such as `toggleMarkers`, `toggleRoutes`, and `toggleZones`.
- The `poi` preset includes markers, routes, and other visible map components.
- Presets can be saved to and restored from `localStorage`.
- `drawLayers()` conditionally calls renderers based on active layer buttons.
- Marker rendering is called by `drawLayers()` when `toggleMarkers` is on.
- Zones and routes are similarly drawn when their toggles are on.
- `getLayer(id)` maps UI toggle ids to actual SVG groups; `toggleMarkers` maps to `#markers`.
- Layer order is changed by dragging `#mapLayers`; `moveLayer()` moves the matching SVG group.

Meridian Prime implication:

> The cleanest early layer strategy is probably not to add a new SVG layer immediately. First, use existing `#markers`, `#routes`, and `#zones` while documenting Meridian Prime metadata. Add a new Meridian Prime layer only after the existing layer/toggle flow is understood well enough to preserve save/load and UI ordering.

---

## Export System Orientation

### Marker CSV Export

Marker CSV export lives in:

`public/modules/ui/markers-overview.js`

Key findings:

- Current marker CSV export writes marker id, type, icon, note name, note legend, x/y, latitude, and longitude.
- Export pulls note name and legend from `notes` using marker id.
- It does not include marker lock/pin/hidden state or any richer metadata.

Meridian Prime implication:

> This is a promising low-risk first export enhancement later: add Meridian Prime-safe metadata columns only after deciding where metadata lives.

### JSON Export

JSON export lives in:

`public/modules/dynamic/export-json.js`

Key findings:

- `exportToJson(type)` supports Full, Minimal, PackCells, and GridCells exports.
- Full export includes `info`, `settings`, `mapCoordinates`, `pack`, `grid`, `biomesData`, `notes`, and `nameBases`.
- Minimal export includes pack features, cultures, burgs, states, provinces, religions, rivers, goods, markers, markets, deals, routes, and zones.
- PackCells export includes cell-level data plus pack features, cultures, burgs, states, provinces, religions, rivers, goods, markers, markets, deals, routes, and zones.

Meridian Prime implication:

> JSON export may already carry `pack.markers` metadata if unknown marker fields survive in memory. This makes JSON export a strong candidate for repo-integrated marker receipts later.

### Image / SVG / Tile / GeoJSON Export

Image/data export lives in:

`public/modules/io/export.js`

Key findings:

- SVG/PNG/JPEG/tile export uses `getMapURL()` to clone the SVG map.
- Export handles external marker icons by converting marker image hrefs to base64 in the cloned SVG.
- Hidden/unused SVG elements may be removed during SVG export.
- GeoJSON export exists for cell geometry/data.

Meridian Prime implication:

> Visual marker rendering should survive image export if markers are visible. But protected metadata should not be embedded into visual SVG unless intentionally designed.

---

## Candidate Meridian Prime Modification Points

### Lowest-risk candidates

1. **Metadata convention only, no source changes yet**  
   Store design docs for proposed marker metadata and manually test unknown marker fields in a throwaway map.

2. **Marker CSV export extension**  
   Later, add optional Meridian Prime columns to marker CSV export if metadata lives in marker objects or notes.

3. **JSON receipt export script**  
   Later, add a Meridian Prime-specific export that reads `pack.markers`, `notes`, `pack.routes`, and `pack.zones` and creates a structured JSON/Markdown receipt.

4. **Marker overview search extension**  
   Later, allow search by type, note name, note legend, and metadata tags.

### Higher-risk candidates

1. **Changing `.map` save slot order**  
   Avoid. This can break compatibility.

2. **Changing core `pack` or `grid` shape broadly**  
   Avoid early. The data model is global and inconsistent.

3. **Adding a new layer toggle before layer system is tested**  
   Delay until existing marker/zone/route layers are mapped and regression-tested.

4. **Changing marker generation config for protected Meridian Prime concepts**  
   Avoid for now. It may create canon-risky automatic generation.

---

## Phase 2 Working Hypothesis

For the first Meridian Prime-aware prototype, prefer this shape:

```js
marker.meridianPrime = {
  schema_version: 1,
  marker_type: "Sanctuary",
  status: "Sandbox",
  canon_risk: "Medium",
  use_tier: "Tier 2 Working",
  tags: ["sanctuary", "route-pressure"],
  protected_mystery_guardrail: "Does not define protected route topology.",
  source_file: "docs/...",
  room_source: "Cartography Engine Room",
  spoiler_visibility: "public-safe"
};
```

This is only a hypothesis. It must be tested in a disposable map before becoming the schema.

Test required:

1. Add a custom marker with `marker.meridianPrime` metadata in dev console or code branch.
2. Save `.map`.
3. Reload `.map`.
4. Confirm metadata survives in `pack.markers`.
5. Export JSON.
6. Confirm metadata appears in JSON export.
7. Confirm no UI breakage.
8. Confirm `npm run build` still passes.

---

## Immediate Next Step

Create or refine:

`docs/cartography/azgaar-fork/schema/schema-notes.md`

Focus on the marker object, notes link, save slots, and safe metadata strategy.

No source customization yet.
