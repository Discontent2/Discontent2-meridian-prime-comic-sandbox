# Internet Access Roadmap Addendum

**Status:** Future Deployment / Access Roadmap Addendum  
**Project:** Meridian Prime Cartography Engine / Azgaar Fork  
**Related Roadmap:** `docs/cartography/azgaar-fork/meridian-prime-cartography-engine-roadmap.md`  
**Related Checkpoint:** `docs/cartography/azgaar-fork/checkpoints/where-we-were-2026-06-20-export-first-pause.md`  
**Last Updated:** 2026-06-20  
**Do Not Canonize From This File:** This is tooling documentation, not lore canon.  

---

## Purpose

Preserve the future plan for turning the current local-only Azgaar development setup into an internet-accessible Meridian Prime cartography tool.

Current state:

```text
local laptop -> localhost Vite dev server -> Azgaar app
```

Future goal:

```text
private Meridian Prime Azgaar fork -> build output -> hosted web app -> load/save .map files while away from main computer
```

---

## Current Access Model

The current working version is an intranet/local development setup:

- Source lives on the user's Pop!_OS machine.
- App runs through `npm run dev`.
- Browser opens `http://localhost:5173/Fantasy-Map-Generator/`.
- `.map` files are saved and loaded manually.
- Metadata survival was proven locally with `marker.meridianPrime`.

This is good for development, but not enough for working away from the computer.

---

## Recommended Future Access Model

The recommended long-term path is a **static internet deployment** of a private Meridian Prime fork.

Concept:

```text
Meridian Prime Azgaar fork
  -> npm run build
  -> dist/
  -> static host
  -> private internet-accessible map tool
```

Preferred hosting candidates:

- GitHub Pages
- Cloudflare Pages
- Netlify
- Vercel

Recommended initial host decision:

> Decide after the Meridian Prime source fork exists and export/search patches are stable.

---

## Why Static Deployment Is Preferred

Azgaar is primarily a browser-side app. That means a built version can likely be hosted as static files without running a custom backend at first.

Benefits:

- Works away from the local computer.
- Avoids exposing the user's laptop directly to the internet.
- Keeps deployment separate from local development.
- Fits the current Vite build flow.
- Allows simple rollback if a deployment breaks.

Current rule:

> Do not deploy protected Meridian Prime material publicly until repo, site, map files, and exports are reviewed for spoiler safety.

---

## Important Limitation: Map Files Do Not Sync Yet

An internet-accessible app does not automatically create cloud save/sync.

Initial remote workflow would likely be:

```text
open hosted tool
load .map file from local device, cloud drive, or downloaded storage
edit map
save .map file
store/upload it again manually
```

This is acceptable for early remote use.

Later improvements may include:

- Dropbox workflow
- Google Drive workflow
- GitHub-backed map receipt export
- manual upload/download conventions
- private map archive folder
- automated marker receipt exports

---

## Temporary Alternative: Tunnel Access

A temporary remote-access option is to run the app on the laptop and expose it through a secure tunnel.

Possible use:

```text
laptop running npm run dev
secure tunnel URL
remote browser opens the tunnel URL
```

Benefits:

- Fast temporary testing.
- No static deployment pipeline required.

Drawbacks:

- Laptop must be on.
- Dev server must be running.
- Home internet must cooperate.
- Security must be configured carefully.
- Not ideal as a permanent project workflow.

Recommendation:

> Use tunnel access only for temporary testing, not as the final Meridian Prime cartography deployment.

---

## Deployment Roadmap

### Stage 1: Finish Local Prototype Patch

Complete current local implementation sequence:

1. Export-only patch in `public/modules/ui/markers-overview.js`.
2. Test marker CSV export with `metadata-survival` marker.
3. Build with exit code `0`.
4. Confirm expected git status.
5. Then perform search-only patch.
6. Build and test again.

No internet deployment yet.

---

### Stage 2: Create Proper Project Fork / Repo Strategy

Decide where the source code should live:

- direct fork of `Azgaar/Fantasy-Map-Generator`, or
- custom Meridian Prime repo containing the forked app, or
- private project fork with protected access.

Decision needed before deployment:

> The hosted app should be built from a controlled Meridian Prime fork, not from an ad hoc local-only folder.

---

### Stage 3: Static Build Verification

Verify the static production build locally:

```bash
npm run build
npm run preview
```

Checks:

- app opens from built output,
- map generation works,
- `.map` save/load works,
- marker metadata survives,
- marker CSV export works,
- JSON export works,
- no broken asset paths.

---

### Stage 4: Private Static Deployment

Deploy the built app to one static host.

Candidates:

- GitHub Pages
- Cloudflare Pages
- Netlify
- Vercel

Initial deployment should be treated as:

```text
private tool deployment / not public lore publication
```

Required checks:

- hosted URL opens,
- app generates map,
- `.map` save/load works through browser downloads/uploads,
- metadata survival still works,
- marker CSV/JSON export works,
- no protected lore is bundled into public-facing files.

---

### Stage 5: Remote Map File Workflow

Choose a map-file workflow for working away from the main computer.

Initial recommendation:

```text
manual .map file workflow first
```

Possible convention:

```text
Meridian-Prime-Maps/
  active/
  archive/
  exports/
  receipts/
```

Later options:

- cloud storage sync,
- Dropbox integration,
- GitHub issue/PR receipt attachments,
- GitHub-backed export folder,
- Drive/Dropbox map vault.

---

### Stage 6: Access Control / Spoiler Safety

Before any permanent hosted deployment, decide:

- Is the repo public or private?
- Is the hosted app public or private?
- Can exported JSON contain protected metadata?
- Are map files stored separately from the app?
- Should test maps use fake/sandbox-only data?
- Does the app bundle any protected Meridian Prime content?

Default safety policy:

> Online app may be public only if it contains no protected Meridian Prime material. Map files and exports should be treated as private until reviewed.

---

### Stage 7: Future Cloud Save / Repo Export

Only after static deployment is stable, consider deeper integrations:

- save markers to a repo-linked export format,
- create Markdown marker receipts,
- export marker index files,
- push map receipts into the sandbox repo,
- sync map archives through cloud storage,
- eventually create a dedicated Meridian Prime map vault.

This is later. Do not let cloud sync delay the first safe deployment.

---

## Recommended Order Relative To Current Work

Do not jump to deployment immediately.

Current order should remain:

1. Finish export-only local patch.
2. Finish search-only local patch.
3. Confirm build and clean working tree.
4. Decide fork/repo strategy.
5. Then begin internet deployment planning.

---

## Callback Summary

If the user asks about working on the map tool away from the computer, summarize this addendum:

> The recommended path is a private static internet deployment of the Meridian Prime Azgaar fork. First finish export/search locally, then create a controlled fork/repo, verify `npm run build`, deploy the built `dist/` to a static host, and use manual `.map` files at first. Cloud sync comes later. Avoid exposing the laptop directly except for temporary tunnel testing.

---

## Canon Safety

This file is deployment/tooling guidance only.

It does not create canon geography, reveal protected story mechanics, or authorize public release of protected Meridian Prime map data.
