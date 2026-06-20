# Meridian Prime Cartography Engine Decision Log

**Status:** Sandbox Tooling Decision Log  
**Project:** Azgaar Fork / Meridian Prime Cartography Engine  
**Related Roadmap:** `docs/cartography/azgaar-fork/meridian-prime-cartography-engine-roadmap.md`  
**Last Updated:** 2026-06-20  
**Do Not Canonize From This File:** This is tooling documentation, not lore canon.  

---

## 2026-06-20: Phase 2 Orientation Notes Created

**Decision:** Create Phase 2 source-orientation notes before any Meridian Prime source customization.

**Files created:**

- `docs/cartography/azgaar-fork/source-map-notes.md`
- `docs/cartography/azgaar-fork/schema/schema-notes.md`

**Reason:** Azgaar's marker, save/load, layer, and export systems must be mapped before any Meridian Prime marker metadata or export behavior is added.

**Key finding:** The first safe question is not "how do we code the Meridian Prime marker system?" It is "does nested Meridian Prime metadata attached to a marker survive save/load and JSON export?"

**Next action:** Run the metadata survival test described in `schema-notes.md`.

**Canon effect:** None. This is tooling documentation only.

---

## 2026-06-20: Baseline Attempt 3 Passed

**Decision:** Treat the unmodified Azgaar baseline as passed.

**Reason:** The user successfully cloned Azgaar, ran the dev server, opened the app locally, generated a map, confirmed marker/route/zone layer availability, saved and reloaded a `.map` file, built with exit code `0`, and confirmed a clean working tree.

**Result:** Phase 1 is complete enough to begin Phase 2 source code orientation.

**Canon effect:** None. This is tooling documentation only.
