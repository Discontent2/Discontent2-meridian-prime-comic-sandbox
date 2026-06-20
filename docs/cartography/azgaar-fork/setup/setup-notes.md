# Meridian Prime Cartography Engine Setup Notes

**Status:** Draft / Untested  
**Project:** Azgaar Fork / Meridian Prime Cartography Engine  
**Repository Scope:** `Discontent2/Discontent2-meridian-prime-comic-sandbox` documentation only  
**Related Roadmap:** `docs/cartography/azgaar-fork/meridian-prime-cartography-engine-roadmap.md`  
**Last Updated:** 2026-06-20  
**Do Not Canonize From This File:** This is tooling documentation, not lore canon.  

---

## Purpose

This file records current setup findings for the Azgaar Fantasy Map Generator fork path before any Meridian Prime customization begins.

The goal is to separate:

1. Official static-run guidance.
2. Official package / development-tooling facts.
3. Our inferred fork workflow.
4. Untested local commands.

This file is deliberately cautious. It is a workbench note, not a victory banner.

---

## Source Status Summary

| Area | Status | Notes |
|---|---|---|
| Official repository | Verified | `Azgaar/Fantasy-Map-Generator`, branch `master`. |
| Live app | Verified | README points to `https://azgaar.github.io/Fantasy-Map-Generator`. |
| Wiki local-run guidance | Verified | Wiki page says to download release source files and run a local web server. Last visible edit: 2024-09-12. |
| License | Verified | MIT License. |
| Package metadata | Verified | `package.json` on `master` currently reports version `2.0.0`. |
| Development toolchain | Verified from `package.json` | Vite, TypeScript, Vitest, Playwright, Biome, simple-git-hooks. |
| Local install | Not tested | No `npm install` has been run by this room. |
| Dev server | Not tested | No `npm run dev` has been run by this room. |
| Static local server | Not tested | No Python, PHP, or VS Code Live Server run has been performed by this room. |
| Save/load behavior | Not tested | Must be tested before any customization. |

---

## Official Static-Run Guidance

**Source:** Official Azgaar wiki page, `Run FMG locally`  
**Source URL:** `https://github.com/Azgaar/Fantasy-Map-Generator/wiki/Run-FMG-locally`  
**Last visible wiki edit:** 2024-09-12  

The wiki describes a simple local-run path for the Generator:

1. Download the latest available release source code ZIP from the Releases page.
2. Unzip all files from the downloaded archive.
3. Start a local web server.
4. Open the local app in a browser.

The wiki lists three static/local server options:

### VS Code Live Server

The wiki recommends VS Code Live Server for developers who want live reload when files change.

### Python server

The wiki lists Python's built-in HTTP server as a simple option.

For non-Windows systems, the wiki gives this pattern:

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000/
```

For Windows, the wiki mentions a `run_python_server.bat` file in the Fantasy Map Generator folder.

### PHP server

The wiki lists PHP's built-in server as another option.

For non-Windows systems, the wiki gives this pattern:

```bash
php -S localhost:3000
```

Then open:

```text
http://localhost:3000/
```

For Windows, the wiki mentions a `run_php_server.bat` file in the Fantasy Map Generator folder.

### Static-Run Interpretation

This static-run path appears suitable for:

- opening a downloaded release locally
- checking how the app behaves as a user-facing web app
- inspecting baseline UI behavior
- basic map generation smoke tests

This path may not be sufficient for source-level fork development, because the current repository also contains modern package scripts and build tooling.

---

## Official Package / Development-Tooling Facts

**Source:** Official `package.json` on `master`  
**Source URL:** `https://github.com/Azgaar/Fantasy-Map-Generator/blob/master/package.json`  

Current verified package facts:

| Field | Value |
|---|---|
| Package name | `fantasy-map-generator` |
| Version | `2.0.0` |
| License | `MIT` |
| Author | `Azgaar` |
| Main entry | `main.js` |
| Repository | `git+https://github.com/Azgaar/Fantasy-Map-Generator.git` |
| Node engine | `>=24.0.0` |

Current verified scripts:

| Script | Command |
|---|---|
| `dev` | `vite` |
| `build` | `tsc && vite build` |
| `preview` | `vite preview` |
| `test` | `vitest` |
| `test:e2e` | `playwright test` |
| `lint` | `biome check --write` |
| `prepare` | `simple-git-hooks` |

Current verified development dependencies include:

- `@biomejs/biome`
- `@playwright/test`
- `@types/d3`
- `@types/node`
- `@vitest/browser`
- `@vitest/browser-playwright`
- `playwright`
- `simple-git-hooks`
- `typescript`
- `vite`
- `vitest`

Current verified runtime dependencies include:

- `alea`
- `d3`
- `delaunator`
- `driver.js`
- `lineclip`
- `polylabel`
- `three`

### Package-Tooling Interpretation

The `package.json` path appears to be the correct starting point for actual source development because it exposes a Vite dev server, TypeScript build, tests, E2E tests, and linting.

This has not yet been tested locally.

---

## Official License Facts

**Source:** Official `LICENSE` file on `master`  
**Source URL:** `https://github.com/Azgaar/Fantasy-Map-Generator/blob/master/LICENSE`  

The license is MIT.

The license permits use, copying, modification, merging, publication, distribution, sublicensing, and sale of copies, provided the copyright and permission notice are included.

The license also states that derivative works from the original software may be produced without restrictions, including created maps, map images, screenshots, videos, and other materials.

### License Interpretation

The license appears compatible with a Meridian Prime fork, provided required copyright and permission notices are preserved.

This is a tooling note, not legal advice.

---

## Official Repository / Source-Structure Facts

**Source:** Official GitHub repository on `master`  
**Source URL:** `https://github.com/Azgaar/Fantasy-Map-Generator`  

Current verified top-level items include:

- `.claude/`
- `.docker/`
- `.github/`
- `docs/`
- `public/`
- `scripts/`
- `src/`
- `tests/`
- `Dockerfile`
- `LICENSE`
- `README.md`
- `main.js`
- `package-lock.json`
- `package.json`
- `playwright.config.ts`
- `tsconfig.json`
- `vite.config.ts`
- Vitest config files

Current verified `src/` structure includes:

- `controllers/`
- `modules/`
- `renderers/`
- `types/`
- `utils/`
- `index.html`
- `test-setup.ts`

Current verified `public/` structure includes:

- `charges/`
- `components/`
- `config/`
- `heightmaps/`
- `images/`
- `libs/`
- `modules/`
- `styles/`
- `main.js`
- `manifest.webmanifest`
- `sw.js`
- `versioning.js`

### Source-Structure Interpretation

The repository appears to be in a transition state between legacy/public application code and newer `src/` TypeScript/Vite structure.

This matters for Meridian Prime because we should avoid assuming all behavior lives in `src/`. We need source-orientation notes before changing markers, save/load, or exports.

---

## Version / Release Ambiguity Note

A prior release-page view showed a `v1.124 [Economy]` release line, while the current official `package.json` on `master` reports version `2.0.0`.

Working interpretation:

- Treat `package.json` on `master` as the source of truth for current development setup.
- Treat Releases as source of truth for downloadable release snapshots.
- Record the exact commit or release tag before testing locally.

Do not mix release-ZIP static instructions and `master` package instructions without labeling which path is being tested.

---

## Our Inferred Fork Workflow

This section is proposed by the Meridian Prime Cartography Engine Room. It is not official Azgaar guidance.

### Goal

Create a safe local development baseline before adding Meridian Prime marker metadata.

### Proposed workflow

1. Fork `Azgaar/Fantasy-Map-Generator` into the user's GitHub account or chosen project account.
2. Clone the fork locally.
3. Record the upstream remote as `upstream`.
4. Use Node `>=24.0.0`, because current `package.json` requires it.
5. Install dependencies using `npm install` or `npm ci` depending on whether the lockfile should be treated as authoritative.
6. Run the Vite dev server using the package script.
7. Open the local app.
8. Generate a fresh map.
9. Save a `.map` file.
10. Reload the `.map` file.
11. Export at least one image or data artifact if available.
12. Record any warnings, build issues, browser errors, save/load issues, or dependency problems.
13. Do not customize until baseline map generation and save/load behavior are confirmed.

### Why this workflow

The Meridian Prime fork will eventually touch marker metadata, search, export, and possibly save/load behavior. That means the first proof must be boring and sturdy:

> The unmodified fork runs, generates maps, saves maps, and loads maps.

Only after that should we add Meridian Prime-specific code.

---

## Untested Local Commands

These commands are plausible based on official repo/package structure, but they are not yet tested by this room.

### Clone fork

Replace placeholders before use.

```bash
git clone https://github.com/<your-account>/Fantasy-Map-Generator.git
cd Fantasy-Map-Generator
```

### Add upstream remote

```bash
git remote add upstream https://github.com/Azgaar/Fantasy-Map-Generator.git
git remote -v
```

### Check Node version

```bash
node --version
```

Expected requirement from `package.json`:

```text
>=24.0.0
```

### Install dependencies

Option A, lockfile-respecting install:

```bash
npm ci
```

Option B, normal install:

```bash
npm install
```

Use only one for the first test session, then record which one was used.

### Run development server

```bash
npm run dev
```

Expected package script:

```text
vite
```

### Build production output

```bash
npm run build
```

Expected package script:

```text
tsc && vite build
```

### Preview production output

```bash
npm run preview
```

Expected package script:

```text
vite preview
```

### Run tests

```bash
npm test
```

Expected package script:

```text
vitest
```

### Run E2E tests

```bash
npm run test:e2e
```

Expected package script:

```text
playwright test
```

### Run lint

```bash
npm run lint
```

Expected package script:

```text
biome check --write
```

Note: `lint` may modify files because the script uses `--write`. Do not run it casually on a dirty working tree.

---

## Baseline Test Checklist

Use this before any Meridian Prime customization.

| Test | Result | Notes |
|---|---|---|
| Node version meets requirement | Not tested |  |
| Dependencies install | Not tested |  |
| Dev server starts | Not tested |  |
| App opens in browser | Not tested |  |
| New map generates | Not tested |  |
| Map save works | Not tested |  |
| Map load works | Not tested |  |
| Console errors checked | Not tested |  |
| Production build works | Not tested |  |
| Preview works | Not tested |  |
| Unit tests run | Not tested |  |
| E2E tests run | Not tested |  |
| Lint behavior understood | Not tested |  |

---

## Meridian Prime Modification Gate

Do not modify Azgaar source code until these are true:

1. The unmodified fork runs locally.
2. New map generation works.
3. Save/load behavior works.
4. Source orientation has identified where markers, notes, save/load, and exports live.
5. A branch strategy has been chosen.
6. A backup or clean baseline commit exists.

The first Meridian Prime modification should be small:

> Add a Meridian Prime marker/index layer without breaking existing markers or save/load behavior.

---

## Next Recommended Documentation Files

After the first local test session, create or update:

- `docs/cartography/azgaar-fork/setup/setup-test-log.md`
- `docs/cartography/azgaar-fork/schema/schema-notes.md`
- `docs/cartography/azgaar-fork/source-map-notes.md`
- `docs/cartography/azgaar-fork/decision-log/decision-log.md`

---

## Current Recommendation

For the next session:

1. Choose where the fork will live.
2. Clone it locally.
3. Confirm Node `>=24.0.0`.
4. Try the package-tooling path first: `npm ci` or `npm install`, then `npm run dev`.
5. Record everything in a setup test log.
6. Keep the static wiki method as a fallback or comparison path for running a downloaded release.

No Meridian Prime code changes yet.

The beast must breathe before we tattoo its scales.
