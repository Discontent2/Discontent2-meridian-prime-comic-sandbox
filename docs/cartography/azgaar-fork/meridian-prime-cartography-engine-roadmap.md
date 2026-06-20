# Meridian Prime Cartography Engine Roadmap

**Callback Phrase:** Cartography Engine Roadmap  
**Status:** Sandbox Tooling Roadmap  
**Project:** Azgaar Fork / Meridian Prime Cartography Engine  
**Purpose:** Track the process of turning Azgaar Fantasy Map Generator into a Meridian Prime-aware map and story engine.  
**Current Milestone:** Phase 1, fork and run locally.  
**Do Not Canonize From This File:** This roadmap is tooling guidance, not lore canon.  

**Last Updated:** 2026-06-20  

---

## Control Panel Snapshot

| Field | Current Setting |
|---|---|
| Room | Meridian Prime Cartography Engine Room |
| Working Repo | `Discontent2/Discontent2-meridian-prime-comic-sandbox` |
| Main Canon Repo | `Discontent2/meridian-prime` |
| Canon Status | Sandbox Tooling / Non-Canon / Requires Review Before Promotion |
| Current Phase | Phase 1: Fork and Run |
| Current Goal | Get Azgaar forked, cloned, installed, and running locally before customization. |
| First Victory | A local Azgaar build runs unchanged and map generation still works. |
| Active Warning | Do not customize before the app runs locally. |
| Last Completed Step | Created `docs/cartography/azgaar-fork/setup/setup-notes.md` as a draft with verified, inferred, proposed, and untested sections. |
| Next Action | Choose fork location and run a local baseline test, then record results in `docs/cartography/azgaar-fork/setup/setup-test-log.md`. |

---

## Current Goal

Fork Azgaar or build from Azgaar-like foundations and gradually turn it into a Meridian Prime-aware cartography and story-engine tool.

The first practical goal is not a perfect Meridian Prime generator. The first practical goal is:

> Fork Azgaar and add a Meridian Prime marker/index layer without breaking anything.

The map engine should eventually support novels, comics, tabletop campaigns, 16-bit game planning, faction pressure, routes, sanctuaries, NPC pools, encounter seeds, protected mysteries, and visual development.

---

## Why Fork Over Overlays

The current strategic preference is to spend learning time on a fork or custom generator rather than manual overlay systems.

Reasons:

- Overlays can draw labels, but they do not naturally remember story pressure.
- Meridian Prime needs searchable marker metadata, not just visual symbols.
- Repo-linked map exports should become reusable by other rooms.
- Protected mysteries need guardrails inside the map data model.
- A fork can preserve terrain, rendering, editing, and save/load behavior while slowly adding Meridian Prime logic.

Core principle:

> A map without story metadata is only a picture. A Meridian Prime map needs to know why the road hurts.

---

## Strategic Decision

Current strategy:

1. Fork Azgaar or use Azgaar-inspired foundations.
2. Preserve Azgaar terrain, rendering, editing, and save/load spine where useful.
3. Add Meridian Prime-aware markers, metadata, indexes, and export receipts gradually.
4. Replace Azgaar systems only when they fight the project.
5. Delay large refactors until source structure and save/load behavior are understood.

Do not begin with a complete rewrite unless the user explicitly decides to abandon the fork approach.

---

## Phase Roadmap

### Phase 1: Fork and Run

**Goal:** Get Azgaar forked, cloned, installed, and running locally.

Tasks:

- Verify current official Azgaar repository.
- Verify license.
- Fork or clone repository.
- Install dependencies.
- Run local development server.
- Open app locally.
- Confirm map generation works.
- Create setup notes.
- Record environment issues.

Deliverables:

- `docs/cartography/azgaar-fork/README.md`
- `docs/cartography/azgaar-fork/setup/setup-notes.md`
- `docs/cartography/azgaar-fork/setup/setup-test-log.md`
- Roadmap update.
- Decision-log entry.

Rule:

> Do not customize before the app runs locally.

---

### Phase 2: Source Code Orientation

**Goal:** Understand enough of Azgaar's structure to modify it safely.

Identify where Azgaar stores or renders:

- map data
- markers
- notes
- routes
- rivers
- burgs / towns
- states
- cultures
- biomes
- heightmap
- save/load logic
- UI editors
- layer rendering
- export functions

Deliverables:

- `docs/cartography/azgaar-fork/schema/schema-notes.md`
- `docs/cartography/azgaar-fork/source-map-notes.md`
- candidate modification points
- risk notes

Rule:

> No large refactors yet. The generator is a living creature. Learn where its bones are before adding new organs.

---

### Phase 3: Meridian Prime Marker Schema

**Goal:** Add Meridian Prime-aware metadata without breaking standard map behavior.

Initial marker types:

- Sanctuary
- World Works Site
- Project Green Glove Site
- Worldskin Prototype Site
- NPC Encounter
- Boss Arena
- Route Pressure
- Protected Mystery
- Settlement
- Industrial Site
- Hydropolis District
- Craton-Adjacent Zone
- Dry Gate Rumor
- False Sanctuary
- Visual Landmark
- Music Cue Site
- Illustration Reference Site

Suggested metadata fields:

- `name`
- `marker_type`
- `status`
- `canon_risk`
- `use_tier`
- `source_file`
- `room_source`
- `faction`
- `associated_npcs`
- `associated_encounters`
- `associated_locations`
- `associated_sanctuaries`
- `protected_mystery_guardrail`
- `spoiler_visibility`
- `tags`
- `notes`
- `last_reviewed`

Example marker:

```json
{
  "name": "Soft Gate Orchard",
  "marker_type": "World Works Site",
  "status": "Sandbox",
  "canon_risk": "High",
  "use_tier": "Tier 4 Restricted",
  "source_file": "docs/story/chance-game/encounter-seeds/world-works/verdant-contact-walker-soft-gate-orchard-deployment.md",
  "faction": "World Works Corp",
  "associated_entities": ["The Verdant Contact Walker", "The Verdant Chimera"],
  "tags": ["project-green-glove", "worldskin-prototype", "false-sanctuary", "dry-gate-pressure"],
  "protected_mystery_guardrail": "Does not define Dry Gate truth."
}
```

---

### Phase 4: Search and Findability

**Goal:** Make map features searchable by Meridian Prime tags and repo links.

Search should support human-friendly names and tag-like identifiers such as:

- `verdant-contact-walker`
- `verdant-chimera`
- `project-green-glove`
- `worldskin-prototype`
- `soft-gate-orchard`
- `sanctuary`
- `world-works`
- `dry-gate-pressure`
- `hydropolis`
- `craton-adjacent`
- `false-sanctuary`
- `route-pressure`
- `boss-arena`

Deliverables:

- searchable marker metadata
- marker filters
- tag index
- repo source-file crosslinks

---

### Phase 5: Repo-Integrated Export

**Goal:** Export map data into markdown receipts and indexes the wider project can use.

Possible export files:

- `map-build-receipt.md`
- `marker-index.md`
- `world-works-site-index.md`
- `sanctuary-site-index.md`
- `boss-arena-index.md`
- `route-pressure-index.md`
- `protected-mystery-warning-index.md`
- `location-pool-import.md`
- `npc-pool-crosslinks.md`
- `music-room-map-cues.md`
- `illustration-room-map-cues.md`

Export rule:

> A map export should not only produce an image. It should produce findable lore metadata.

---

### Phase 6: Meridian Prime Generation Tables

**Goal:** Add procedural Meridian Prime flavor after the map data model is stable.

Possible generation systems:

- World Works facilities near resource or route-pressure zones
- sanctuaries in liminal terrain
- boss arenas near faction-pressure intersections
- Hydropolis districts around water / registry / actuator logic
- Craton-adjacent pressure zones
- black-market route nodes
- roadside shelters and roadhouses
- false sanctuaries
- Project Green Glove test sites
- Worldskin membrane facilities

Rule:

> Do not generate protected truths. Generate pressure, rumors, and sandbox candidates.

---

### Phase 7: Game / Tabletop / Comic Export

**Goal:** Use the cartography engine to support game maps, tabletop regions, comic issue routes, and novel travel arcs.

Possible outputs:

- 16-bit region map draft
- side-scroller level path
- tabletop hex / point-crawl map
- comic issue location sequence
- novel chapter travel path
- encounter route table
- sanctuary placement table

This phase comes later, after schema and export behavior are stable.

---

## Current Milestone

**Phase 1: Fork and Run Locally**

Current official-source verification is complete enough to draft setup notes. The next work session should choose the fork location, perform the local baseline test, and record results before any customization.

Tracking categories:

| Category | Status |
|---|---|
| Official Azgaar repo verified | Done |
| License verified | Done |
| Official wiki/static-run guidance verified | Done |
| Official `package.json` verified | Done |
| Package/source structure verified | Done |
| Fork created | Not started |
| Local clone completed | Not started |
| Dependencies installed | Not tested |
| Dev server run | Not tested |
| App opened locally | Not tested |
| Map generation confirmed | Not tested |
| Save/load confirmed | Not tested |
| Setup notes created | Done, draft / untested |
| Setup test log created | Not started |
| Decision log updated | Done |

---

## Next Action

Create the first local baseline test record:

`docs/cartography/azgaar-fork/setup/setup-test-log.md`

The test log should record:

1. Host OS and shell.
2. Node version.
3. Fork or clone URL used.
4. Exact commit or tag tested.
5. Dependency command used.
6. Dev server command used.
7. Browser used.
8. Whether a new map generated.
9. Whether save/load worked.
10. Console or terminal errors.
11. Whether production build worked.
12. Whether tests were run.
13. Whether any files changed unexpectedly.

---

## Blocked / Questions

Current blockers:

- Local development environment details are unknown.
- The user has not yet chosen whether to fork under the main user account, a project org, or a local-only clone first.
- No local installation, dev server, build, or save/load testing has been performed.

Open questions:

- What local OS and development environment will be used for the first run?
- Should the first fork remain a direct Azgaar fork, or should it be mirrored into a custom Meridian Prime repository after initial testing?
- Should map-engine work happen on `main` in the sandbox repo documentation only, or should tooling notes track a separate development branch once code begins?

---

## Decision Log

### 2026-06-20: Create Setup Notes Draft

**Decision:** Create `docs/cartography/azgaar-fork/setup/setup-notes.md` as a draft separating official static-run guidance, official package/tooling facts, inferred fork workflow, and untested local commands.

**Reason:** Azgaar's wiki static-run guidance and current `package.json` development workflow are related but not identical. Meridian Prime setup notes need labels so we do not confuse release-ZIP use with source-fork development.

**Canon effect:** None. This is tooling documentation only.

---

### 2026-06-20: Create Cartography Engine Roadmap

**Decision:** Create a dedicated roadmap file in the sandbox repo at `docs/cartography/azgaar-fork/meridian-prime-cartography-engine-roadmap.md`.

**Reason:** The Cartography Engine Room needs a stable control panel that records strategy, phase status, guardrails, and next actions.

**Canon effect:** None. This is tooling guidance only.

---

### 2026-06-20: Fork/Azgaar-Like Foundation Preferred Over Manual Overlays

**Decision:** Prefer learning to fork or build from Azgaar-like foundations instead of spending early effort on manual overlay systems.

**Reason:** Meridian Prime requires searchable story metadata, protected mystery guardrails, repo-linked marker indexes, and exportable receipts. Manual overlays would become map glitter without a memory spine.

**Canon effect:** None. This is tooling strategy only.

---

### 2026-06-20: Marker Metadata Comes Before Procedural Generation

**Decision:** Add Meridian Prime marker/index metadata before trying to procedurally generate Meridian Prime-specific content.

**Reason:** Stable save/load and searchable data matter before new generation tables. The engine must remember places safely before it starts inventing them.

**Canon effect:** None. Generated markers remain sandbox unless separately reviewed.

---

### 2026-06-20: Protected Mysteries Are Pressure, Not Truth

**Decision:** Cartography may represent protected mysteries as pressure zones, rumors, distortions, warnings, and sandbox markers, but not as confirmed truth.

**Reason:** Map tooling must not reveal or accidentally canonize restricted story answers.

**Canon effect:** Preventive guardrail.

---

## Canon Guardrails

This room must not define or reveal:

- the Core
- Dry Port truth
- Dry Gate truth
- gateway mechanics
- Contact Frame mechanics
- protected route topology
- àæonos ecosystem truth
- Absconditian truth
- Ildi's restricted truth
- Conjugate Chimera backstory
- Rob Holliday's death-chain
- the NCI assassin
- Book One answers

Maps may include:

- pressure zones
- rumor zones
- suspected sites
- World Works theories
- sandbox markers
- candidate-canon geography
- false labels
- corporate map distortions

Preferred wording:

- suspected Dry Gate pressure zone
- World Works-classified contact patch
- rumored route anomaly
- unverified gateway pressure
- protected mystery marker
- candidate-canon location
- sandbox-only geography

Avoid wording:

- true Dry Gate location
- confirmed gateway mechanism
- actual Core access point
- real Contact Frame coordinates
- confirmed àæonos ecology

---

## Repo Links

### Repositories

- Main canon repository, read-only reference: `Discontent2/meridian-prime`
- Sandbox / development repository: `Discontent2/Discontent2-meridian-prime-comic-sandbox`

### Recommended Sandbox Folder Structure

- `docs/cartography/`
- `docs/cartography/azgaar-fork/`
- `docs/cartography/azgaar-fork/roadmap/`
- `docs/cartography/azgaar-fork/setup/`
- `docs/cartography/azgaar-fork/schema/`
- `docs/cartography/azgaar-fork/decision-log/`
- `docs/cartography/azgaar-fork/map-build-logs/`
- `docs/cartography/azgaar-fork/exports/`
- `docs/cartography/azgaar-fork/marker-indexes/`
- `docs/cartography/azgaar-fork/candidate-canon/`

### Primary Roadmap File

- `docs/cartography/azgaar-fork/meridian-prime-cartography-engine-roadmap.md`

### Recommended README

- `docs/cartography/azgaar-fork/README.md`

### Optional Later Files

- `docs/cartography/azgaar-fork/decision-log/decision-log.md`
- `docs/cartography/azgaar-fork/setup/setup-notes.md`
- `docs/cartography/azgaar-fork/setup/setup-test-log.md`
- `docs/cartography/azgaar-fork/schema/schema-notes.md`
- `docs/cartography/azgaar-fork/source-map-notes.md`
- `docs/cartography/azgaar-fork/protected-mystery-map-rules.md`
- `docs/cartography/azgaar-fork/marker-indexes/marker-type-index.md`
- `docs/cartography/azgaar-fork/schema/route-pressure-schema.md`
- `docs/cartography/azgaar-fork/schema/world-works-site-schema.md`
- `docs/cartography/azgaar-fork/schema/sanctuary-site-schema.md`

---

## Known Relevant Concepts

The engine should eventually support and help find:

- Project Green Glove
- Worldskin Prototype
- The Verdant Contact Walker
- The Verdant Chimera
- Soft Gate Orchard Deployment
- World Works false sanctuaries
- Worldskin membrane sites
- suspected Dry Gate pressure zones

Relevant saved file paths to verify before duplication:

- `docs/worldbuilding/world-works/project-green-glove-worldskin-prototype.md`
- `docs/story/chance-game/npc-pool/pools/world-works-encounter-entities.md`
- `docs/story/chance-game/npc-pool/npc-master-index.md`
- `docs/story/chance-game/npc-pool/npc-tag-index.md`
- `docs/story/chance-game/encounter-seeds/world-works/verdant-contact-walker-soft-gate-orchard-deployment.md`

If any of these files do not exist, search the sandbox repo and report what is missing before creating duplicates.

---

## Integration With Existing Meridian Prime Rooms

The Cartography Engine Room should connect with:

- Story Room
- NPC Pool Generator
- Location Pool
- Sanctuary Room
- World Building Department
- Music Room
- Illustration Room
- Biome & Bestiary Room
- Comic Room
- Game / Side-Scroller Room
- Property Scout Room when map regions overlap real-world inspiration research

Map markers should be able to reference:

- NPC pool entries
- encounter seeds
- sanctuary seeds
- location seeds
- worldbuilding files
- music prompts
- illustration prompts
- candidate-canon review notes

---

## Setup Status

Setup notes now exist at:

`docs/cartography/azgaar-fork/setup/setup-notes.md`

The setup notes are a draft and are not a record of a successful local run. No local setup has been attempted from this room yet.

The draft separates:

- official static-run guidance
- official package / development-tooling facts
- inferred fork workflow
- untested local commands

Before any Meridian Prime customization, perform and document a local baseline run.

---

## What To Avoid Early

Do not start with:

- full custom climate simulation
- full Aeonos / àæonos dual-world modeling
- non-Euclidean route physics
- automatic novel plot generation
- perfect 16-bit exporter
- Dry Gate mechanics
- Contact Frame mechanics
- complete rewrite of Azgaar
- major UI refactor before understanding source

First victory:

> A fork that runs and preserves map save/load behavior.

---

## Control Panel Use

When the user says any of the following:

- Pull up the Cartography Engine Roadmap
- Where are we on the Azgaar fork roadmap?
- What is the next cartography engine step?
- Resume the Meridian Prime map engine work.
- Cartography Engine Roadmap

Use this file as the control panel and summarize:

1. Current phase.
2. Current milestone.
3. Last decision.
4. Next action.
5. Any blockers.
6. What file should be updated next.

---

## Final Operating Principle

The map engine should not merely draw Meridian Prime.

It should help Meridian Prime remember what kind of pressure each place puts on a story.
