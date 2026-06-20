# Visible Export Panel Test 001

**Status:** Passed  
**Project:** Meridian Prime Cartography Engine / Azgaar Fork  
**Test Type:** Export Route Verification / Visible Map Data Export Panel  
**Related Test:** `docs/cartography/azgaar-fork/map-build-logs/metadata-survival-test-001.md`  
**Related Plan:** `docs/cartography/azgaar-fork/implementation/export-first-search-second-plan.md`  
**Last Updated:** 2026-06-20  
**Do Not Canonize From This File:** This is tooling documentation, not lore canon.  

---

## Purpose

Verify whether Meridian Prime marker metadata can be exported through the visible Azgaar **Export map data** panel, rather than relying on the harder-to-access marker table CSV export.

---

## Context

A local branch existed for the first source customization:

```text
mp-marker-export-search-001
```

The file below had been modified locally and built successfully:

```text
public/modules/ui/markers-overview.js
```

However, the user discovered that the practical visible export route is the main **Export map data** dialog, not the marker table CSV pathway.

---

## Visible Export Options Tested

From the map UI:

```text
Options / bottom toolbar -> Export -> Export map data
```

The visible export panel offered:

- image export: SVG, PNG, JPEG, tiles,
- GeoJSON export: cells, routes, rivers, markers, zones,
- JSON export: full, minimal, pack cells, grid cells.

The user tested:

1. **Export to GeoJSON -> markers**
2. **Export to JSON -> minimal**

---

## Results

| Export Route | Result | Notes |
|---|---|---|
| GeoJSON markers | Pass | Downloaded export contained `metadata-survival`. |
| Minimal JSON | Pass | Downloaded export contained `metadata-survival`. |

---

## Verdict

**Passed.**

The visible export panel can already export Meridian Prime marker metadata through GeoJSON markers and Minimal JSON when the marker contains nested `marker.meridianPrime` metadata.

---

## Implication

The original export-only source patch to the hidden/secondary marker table CSV export is not required for the first useful export route.

Recommended next local action:

1. Do not commit the current `markers-overview.js` CSV patch yet.
2. Revert the unneeded local edit unless the user specifically wants marker-table CSV export later.
3. Treat visible export panel support as the first export success.
4. Move next to **search-only** customization, or create a dedicated, visible Meridian Prime export button later.

---

## Recommended Local Cleanup

If no longer pursuing marker table CSV immediately, return local source to clean state:

```bash
git restore public/modules/ui/markers-overview.js
git status --short
```

Expected result after restore:

```text
clean working tree
```

Then proceed to the next source customization only after choosing a search target.

---

## Updated Route Priority

New export route priority:

1. Visible Export Panel: GeoJSON markers and Minimal JSON.
2. Future Meridian Prime dedicated export/receipt.
3. Marker table CSV export only if needed later.

---

## Canon Safety

This test verifies tooling behavior only.

It does not canonize any map data, location, route, marker, faction, protected mystery, or story truth.
