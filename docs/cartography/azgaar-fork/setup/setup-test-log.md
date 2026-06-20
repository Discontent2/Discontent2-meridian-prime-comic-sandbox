# Meridian Prime Cartography Engine Setup Test Log

**Status:** Baseline Attempt 3 / Passed  
**Project:** Azgaar Fork / Meridian Prime Cartography Engine  
**Repository Scope:** `Discontent2/Discontent2-meridian-prime-comic-sandbox` documentation only  
**Related Roadmap:** `docs/cartography/azgaar-fork/meridian-prime-cartography-engine-roadmap.md`  
**Related Setup Notes:** `docs/cartography/azgaar-fork/setup/setup-notes.md`  
**Last Updated:** 2026-06-20  
**Do Not Canonize From This File:** This is tooling documentation, not lore canon.  

---

## Purpose

This file records attempts to run the unmodified Azgaar fork baseline before any Meridian Prime customization begins.

The goal is to prove the plain fork can breathe before we attach story-engine organs:

1. Fork or clone location is chosen.
2. Local environment is recorded.
3. Dependencies install.
4. Development server runs.
5. App opens locally.
6. New map generation works.
7. Save/load works.
8. Production build works.
9. Any errors, warnings, or unexpected file changes are captured.

No Meridian Prime source changes should happen until this baseline is complete.

---

## Baseline Attempt 3 Summary

| Field | Value |
|---|---|
| Test date | 2026-06-20 |
| Tester | User on local Pop!_OS machine with ChatGPT guidance |
| Host OS | Pop!_OS / Linux, exact version not recorded |
| Shell / terminal | bash terminal |
| Browser | Firefox or Chromium-family browser, exact version not recorded |
| Fork location chosen | Local-only source baseline first |
| Folder used | `/home/tenet/meridian-cartography-baseline/Fantasy-Map-Generator` |
| Git clone URL | `https://github.com/Azgaar/Fantasy-Map-Generator.git` |
| Branch tested | Local clone branch, exact branch name not recorded |
| Commit tested | `9d14cf78791484ea23936aff26807fc2503b3252` |
| Node version | `v24.17.0`, meets required `>=24.0.0` |
| Package manager | `npm 11.13.0` |
| Git version | `git version 2.34.1` from earlier screenshot |
| Dependency command used | `npm ci`, implied successful enough for dev/build; full output not captured |
| Dev server command used | `npm run dev` |
| Local app URL | `http://localhost:5173/Fantasy-Map-Generator/` |
| Production build command used | `npm run build` |
| Save/load test file | `.map` file saved and reloaded; filename not recorded |
| Final `git status --short` | Clean / returned no output |
| Overall result | Passed |

---

## Attempt 3 Progress

| Check | Result | Notes |
|---|---|---|
| Node installed | Pass | Installed through nvm. |
| Node requirement met | Pass | `node --version` reported `v24.17.0`. |
| npm available | Pass | `npm --version` reported `11.13.0`. |
| Baseline folder created | Pass | `/home/tenet/meridian-cartography-baseline`. |
| Direct `git clone` | Pass | Source acquired from GitHub after phone/laptop restart and restored GitHub access. |
| Commit recorded | Pass | `git rev-parse HEAD` returned `9d14cf78791484ea23936aff26807fc2503b3252`. |
| Dependency install | Pass | `npm ci` was part of the successful baseline flow; exact output not captured. |
| Dev server | Pass | `npm run dev` launched local app. |
| App opens locally | Pass | Browser displayed Azgaar at `localhost:5173/Fantasy-Map-Generator/`. |
| New map generates | Pass | Generated map visible in browser. |
| Map UI responds | Pass | Layers panel opened and map displayed. |
| Markers layer visible / available | Pass | Markers visible in layer panel. |
| Routes layer visible / available | Pass | Routes visible in layer panel. |
| Zones layer visible / available | Pass | Zones visible in layer panel. |
| Save `.map` works | Pass | User confirmed save/reload flow. |
| Reload `.map` works | Pass | User confirmed reload. |
| Production build | Pass | `npm run build` completed and `echo $?` returned `0`. |
| Final git status | Pass | `git status --short` returned nothing. |
| Lint | Not run | Intentionally skipped because current lint script may write changes. |
| Unit/E2E tests | Not run | Optional for this baseline; not required to unlock Phase 2 orientation. |

---

## Fork Location Decision

| Option | Selected? | Notes |
|---|---|---|
| Direct fork under user account | No | Deferred until after unmodified baseline passed. |
| Fork under project organization | No | Deferred. |
| Local-only clone/source baseline first | Yes | Chosen as the safest first baseline path because it avoids creating a premature project fork. |
| Mirror into custom Meridian Prime repo later | Not yet | Revisit after Phase 2 source orientation. |

### Decision Notes

- **Chosen path:** Local-only baseline first.
- **Reason:** Safest first test. It preserved the modification gate and avoided committing to a fork location before the plain app ran.
- **Date decided:** 2026-06-20.
- **Canon effect:** None. Tooling only.

---

## Local Environment

| Check | Result | Notes |
|---|---|---|
| OS name/version | Pop!_OS / Linux, exact version not recorded | Prompt shows `tenet@pop-os`. |
| CPU architecture | Not recorded |  |
| Terminal/shell | bash terminal |  |
| Git version | `git version 2.34.1` | From earlier local screenshot. |
| Node version | `v24.17.0` | Meets current Azgaar requirement `>=24.0.0`. |
| npm version | `11.13.0` | Installed with Node through nvm. |
| Browser/version | Browser available, exact version not recorded | Successfully opened local app. |
| Disk location of successful baseline | `/home/tenet/meridian-cartography-baseline/Fantasy-Map-Generator` |  |

### Environment Commands Used

```bash
node --version
npm --version
git --version
mkdir -p "$HOME/meridian-cartography-baseline"
cd "$HOME/meridian-cartography-baseline"
pwd
```

### Recorded Output

```text
node --version -> v24.17.0
npm --version -> 11.13.0
pwd -> /home/tenet/meridian-cartography-baseline
git --version -> git version 2.34.1
```

---

## Clone / Source Setup

### Commands Attempted

```bash
cd "$HOME/meridian-cartography-baseline"
rm -rf Fantasy-Map-Generator Fantasy-Map-Generator-master azgaar.zip
git clone https://github.com/Azgaar/Fantasy-Map-Generator.git
cd Fantasy-Map-Generator
git status
git rev-parse HEAD
```

### Results

| Check | Result | Notes |
|---|---|---|
| `git clone` completed | Pass | GitHub access worked after phone/laptop restart. |
| `origin` remote correct | Not explicitly recorded | Source URL was direct Azgaar repo clone. |
| `upstream` remote added | Not needed yet | Local baseline only. |
| Working tree clean before install | Pass | `git status --short` returned no output in visible terminal. |
| Commit SHA recorded | Pass | `9d14cf78791484ea23936aff26807fc2503b3252`. |

### Recorded Output

```text
git rev-parse HEAD
9d14cf78791484ea23936aff26807fc2503b3252
```

---

## Dependency Install Test

### Command

```bash
npm ci
```

### Results

| Check | Result | Notes |
|---|---|---|
| Install command used | Pass | `npm ci` was used in the successful baseline flow. |
| Install completed | Pass | App and production build ran afterward, so dependencies were available. |
| Warnings encountered | Not recorded | Exact install output not captured. |
| Errors encountered | None recorded | No blocking install error reported. |
| Files changed after install | Pass | Final `git status --short` returned no output. |

---

## Development Server Test

### Command

```bash
npm run dev
```

### Results

| Check | Result | Notes |
|---|---|---|
| Dev server started | Pass | Local app opened in browser. |
| Local URL shown | Pass | `http://localhost:5173/Fantasy-Map-Generator/`. |
| Terminal errors | None blocking observed | Exact dev-server output not captured. |
| Browser opened app | Pass | Screenshot showed Azgaar running. |
| Browser console errors | Not checked | Not required for Phase 1 baseline unless visible/blocking. |

---

## Baseline App Behavior Test

Do not add Meridian Prime changes during this test.

| Behavior | Result | Notes |
|---|---|---|
| App loads locally | Pass | Browser showed local Azgaar instance. |
| New map generates | Pass | Map visible in browser. |
| Map UI responds | Pass | Layers menu opened. |
| Layers menu opens | Pass | Layer panel visible. |
| Markers layer visible / available | Pass | Markers listed in layer panel. |
| Routes layer visible / available | Pass | Routes listed in layer panel. |
| Zones layer visible / available | Pass | Zones listed in layer panel. |
| Save `.map` works | Pass | User confirmed. |
| Reload `.map` works | Pass | User confirmed reload. |
| Export image/data works | Not tested | Optional and not required for Phase 1 baseline. |
| No major console errors | Not checked | No blocking browser issue observed. |

### Save / Load Details

| Field | Value |
|---|---|
| Test map name | Not recorded |
| Saved file name | Not recorded |
| Save method used | Azgaar UI Save button |
| Reload method used | Azgaar UI Load button |
| Reload result | Pass |
| Data loss noticed | None reported |

---

## Production Build Test

### Command

```bash
npm run build
```

### Results

| Check | Result | Notes |
|---|---|---|
| Build command completed | Pass | `echo $?` returned `0`. |
| TypeScript completed | Pass | Script is `tsc && vite build`; exit code was `0`. |
| Vite build completed | Pass | Exit code was `0`. |
| Build output created | Not directly inspected | Exit code indicates success. |
| Warnings encountered | Yes | Vite printed script-bundling warnings for non-module scripts. |
| Errors encountered | None blocking | Exit code was `0`. |

### Recorded Output

```text
npm run build
fantasy-map-generator@2.0.0 build
tsc && vite build
vite v8.0.16 building client environment for production...
[Warnings about scripts in index.html that cannot be bundled without type="module" attribute]
echo $? -> 0
```

---

## Preview Test

### Intended command

```bash
npm run preview
```

### Results

| Check | Result | Notes |
|---|---|---|
| Preview server started | Not tested | Optional for Phase 1 baseline. |
| Preview URL opened | Not tested |  |
| Built app loads | Not tested |  |
| New map generates in preview | Not tested |  |
| Save/load works in preview | Not tested | Optional. |

---

## Test Commands

These are optional for the first local baseline, but record them if run.

```bash
npm test
npm run test:e2e
npm run lint
```

Warning: current setup notes say `npm run lint` maps to `biome check --write`, so it may modify files. Run only on a clean tree or a disposable branch.

### Results

| Check | Result | Notes |
|---|---|---|
| Unit tests run | Not run | Optional for this baseline. |
| Unit tests pass | Not tested |  |
| E2E tests run | Not run | Optional for this baseline. |
| E2E tests pass | Not tested |  |
| Lint run | Not run | Intentionally skipped because it may modify files. |
| Lint changed files | Not checked | Lint not run. |

---

## Git Status After Baseline

### Command

```bash
git status --short
```

### Results

| Check | Result | Notes |
|---|---|---|
| Working tree clean after baseline | Pass | Command returned no output. |
| Expected generated files only | Pass | No files shown. |
| Unexpected source changes | Pass | None. |

### Recorded Output

```text
git status --short -> [no output]
```

---

## Issues / Errors / Warnings

| ID | Severity | Area | Description | Status |
|---|---|---|---|---|
| SETUP-001 | Resolved | Baseline | Baseline completed successfully on Attempt 3. | Closed |
| SETUP-002 | Resolved | Node | Node was upgraded to `v24.17.0`, satisfying current Azgaar requirement `>=24.0.0`. | Closed |
| SETUP-003 | Resolved | Network / Git | Direct GitHub access recovered after phone/laptop restart. | Closed |
| SETUP-004 | Resolved | Network / Source ZIP | ZIP fallback no longer needed because direct clone worked. | Closed |
| SETUP-005 | Resolved | Browser app test | Local app opened, generated a map, saved, and reloaded. | Closed |
| SETUP-006 | Warning | Build | Vite printed non-blocking warnings about scripts in `index.html` that cannot be bundled without `type="module"`. | Open / Watch |

---

## Baseline Verdict

Choose one after the test:

- **Pass:** unmodified fork runs locally, generates maps, saves, loads, and builds.
- **Partial:** app runs, but one or more baseline checks failed.
- **Blocked:** install or dev server cannot run yet.
- **Not Run:** baseline has not been attempted.

**Current verdict:** Pass

### Verdict Notes

```text
Attempt 3 passed. The user restored GitHub access by restarting phone and laptop, cloned the unmodified Azgaar repository, confirmed Node v24.17.0 and npm 11.13.0, opened the local Vite app at localhost:5173/Fantasy-Map-Generator/, generated a map, confirmed marker/route/zone layers are available, saved and reloaded a .map file, ran npm run build with exit code 0, and confirmed git status --short returned no output. The unmodified baseline is now good enough to unlock Phase 2: Source Code Orientation. No Meridian Prime source customization has been made yet.
```

---

## Baseline Attempt 2 Archive

Attempt 2 ran on the user's local Pop!_OS machine before restarting phone/laptop.

| Field | Value |
|---|---|
| Test date | 2026-06-20 |
| Host OS | Pop!_OS / Linux, exact version not recorded |
| Folder used | `/home/tenet/meridian-cartography-baseline` |
| Node version | `v24.17.0` |
| npm version | `11.13.0` |
| Overall result | Blocked |

Attempt 2 blockers:

- Direct `github.com:443` was unreachable.
- IPv4-only GitHub request also failed.
- `codeload.github.com:443` was unreachable.
- Source tree could not be acquired.

---

## Baseline Attempt 1 Archive

Attempt 1 ran in the assistant runtime, not on the user's local Pop!_OS machine.

| Field | Value |
|---|---|
| Test date | 2026-06-20 |
| Host OS | Linux `0725cb61a07b`, kernel `4.4.0`, x86_64 |
| Shell / terminal | `bash` in `/mnt/data` |
| Browser | Not available / not tested in that environment |
| Fork location chosen | Local-only clone first |
| Fork / clone URL | `https://github.com/Azgaar/Fantasy-Map-Generator.git` |
| Node version | `v22.16.0`, below required `>=24.0.0` |
| Package manager | `npm 10.9.2` |
| Overall result | Blocked |

Attempt 1 blockers:

- Runtime shell could not resolve `github.com` for `git clone`.
- Runtime Node version was below requirement.
- No browser/app session was available.

---

## Meridian Prime Modification Gate

The Phase 1 baseline gate is now **passed**, but source customization should still wait until Phase 2 orientation identifies the safest modification points.

Required before customization:

| Requirement | Status |
|---|---|
| Fork location chosen | Done: local-only baseline first |
| Local/source checkout works | Done |
| Node requirement met | Done: `v24.17.0` |
| Dependencies install | Done enough for dev/build; exact output not captured |
| Dev server runs | Done |
| App opens locally | Done |
| New map generates | Done |
| Save/load works | Done |
| Build works | Done |
| Source-orientation notes started | Not started |
| Clean baseline commit or branch exists | Done: clean working tree at commit `9d14cf78791484ea23936aff26807fc2503b3252` |

First allowed Meridian Prime code change after Phase 2 orientation:

> Add a Meridian Prime marker/index layer without breaking existing markers or save/load behavior.

---

## Next Action

Begin Phase 2: Source Code Orientation.

Create or update:

`docs/cartography/azgaar-fork/schema/schema-notes.md`

and/or:

`docs/cartography/azgaar-fork/source-map-notes.md`

Phase 2 should identify where Azgaar stores or renders:

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

Do not customize yet. First learn where the bones are.
