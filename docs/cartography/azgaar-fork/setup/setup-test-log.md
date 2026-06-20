# Meridian Prime Cartography Engine Setup Test Log

**Status:** Baseline Test Log / Not Yet Run  
**Project:** Azgaar Fork / Meridian Prime Cartography Engine  
**Repository Scope:** `Discontent2/Discontent2-meridian-prime-comic-sandbox` documentation only  
**Related Roadmap:** `docs/cartography/azgaar-fork/meridian-prime-cartography-engine-roadmap.md`  
**Related Setup Notes:** `docs/cartography/azgaar-fork/setup/setup-notes.md`  
**Last Updated:** 2026-06-20  
**Do Not Canonize From This File:** This is tooling documentation, not lore canon.  

---

## Purpose

This file records the first unmodified Azgaar fork baseline test before any Meridian Prime customization begins.

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

## Baseline Run Summary

| Field | Value |
|---|---|
| Test date | Not run |
| Tester | Not recorded |
| Host OS | Not recorded |
| Shell / terminal | Not recorded |
| Browser | Not recorded |
| Fork location chosen | Not chosen |
| Fork / clone URL | Not recorded |
| Upstream remote URL | `https://github.com/Azgaar/Fantasy-Map-Generator.git` |
| Branch tested | Not recorded |
| Commit or tag tested | Not recorded |
| Node version | Not recorded |
| Package manager | Not recorded |
| Dependency command used | Not run |
| Dev server command used | Not run |
| Local app URL | Not recorded |
| Production build command used | Not run |
| Save/load test file | Not recorded |
| Overall result | Not run |

---

## Fork Location Decision

Record the chosen fork strategy here.

| Option | Selected? | Notes |
|---|---|---|
| Direct fork under user account | Not selected |  |
| Fork under project organization | Not selected |  |
| Local-only clone first | Not selected |  |
| Mirror into custom Meridian Prime repo later | Not selected |  |

### Decision Notes

- **Chosen path:** Not chosen.
- **Reason:** Not recorded.
- **Date decided:** Not recorded.
- **Canon effect:** None. Tooling only.

---

## Local Environment

| Check | Result | Notes |
|---|---|---|
| OS name/version | Not recorded | Example: Windows 11, macOS, Ubuntu. |
| CPU architecture | Not recorded | Example: x64, arm64. |
| Terminal/shell | Not recorded | Example: PowerShell, Git Bash, zsh, bash. |
| Git version | Not recorded |  |
| Node version | Not recorded | Required by current `package.json`: `>=24.0.0`. |
| npm version | Not recorded |  |
| Browser/version | Not recorded |  |
| Disk location of clone | Not recorded |  |

### Environment Commands

```bash
git --version
node --version
npm --version
```

---

## Clone / Remote Setup

### Commands Attempted

```bash
# Replace placeholder before use
git clone https://github.com/<your-account>/Fantasy-Map-Generator.git
cd Fantasy-Map-Generator
git remote add upstream https://github.com/Azgaar/Fantasy-Map-Generator.git
git remote -v
git status
git rev-parse HEAD
```

### Results

| Check | Result | Notes |
|---|---|---|
| Clone completed | Not tested |  |
| `origin` remote correct | Not tested |  |
| `upstream` remote added | Not tested |  |
| Working tree clean before install | Not tested |  |
| Commit SHA recorded | Not tested |  |

### Recorded Output

```text
Paste relevant terminal output here.
```

---

## Dependency Install Test

Use one install path for the first test and record which one was used.

### Option A: Lockfile-respecting install

```bash
npm ci
```

### Option B: Normal install

```bash
npm install
```

### Results

| Check | Result | Notes |
|---|---|---|
| Install command used | Not run |  |
| Install completed | Not tested |  |
| Warnings encountered | Not recorded |  |
| Errors encountered | Not recorded |  |
| Files changed after install | Not checked | Run `git status`. |

### Recorded Output

```text
Paste relevant terminal output here.
```

---

## Development Server Test

### Command

```bash
npm run dev
```

### Results

| Check | Result | Notes |
|---|---|---|
| Dev server started | Not tested |  |
| Local URL shown | Not recorded | Example: `http://localhost:5173/`. |
| Terminal errors | Not recorded |  |
| Browser opened app | Not tested |  |
| Browser console errors | Not checked |  |

### Recorded Output

```text
Paste relevant terminal and browser-console output here.
```

---

## Baseline App Behavior Test

Do not add Meridian Prime changes during this test.

| Behavior | Result | Notes |
|---|---|---|
| App loads locally | Not tested |  |
| New map generates | Not tested |  |
| Map UI responds | Not tested | Pan/zoom/edit basics if practical. |
| Layers menu opens | Not tested |  |
| Markers layer visible / available | Not tested |  |
| Routes layer visible / available | Not tested |  |
| Zones layer visible / available | Not tested |  |
| Save `.map` works | Not tested |  |
| Reload `.map` works | Not tested |  |
| Export image/data works | Not tested | Optional if available. |
| No major console errors | Not checked |  |

### Save / Load Details

| Field | Value |
|---|---|
| Test map name | Not recorded |
| Saved file name | Not recorded |
| Save method used | Not recorded |
| Reload method used | Not recorded |
| Reload result | Not tested |
| Data loss noticed | Not checked |

### Notes

```text
Record app behavior here.
```

---

## Production Build Test

### Command

```bash
npm run build
```

### Results

| Check | Result | Notes |
|---|---|---|
| Build command completed | Not tested |  |
| TypeScript completed | Not tested | Expected script includes `tsc`. |
| Vite build completed | Not tested |  |
| Build output created | Not checked |  |
| Warnings encountered | Not recorded |  |
| Errors encountered | Not recorded |  |

### Recorded Output

```text
Paste relevant build output here.
```

---

## Preview Test

### Command

```bash
npm run preview
```

### Results

| Check | Result | Notes |
|---|---|---|
| Preview server started | Not tested |  |
| Preview URL opened | Not tested |  |
| Built app loads | Not tested |  |
| New map generates in preview | Not tested |  |
| Save/load works in preview | Not tested | Optional. |

---

## Test Commands

These are optional for the first local baseline, but record them if run.

### Unit / browser tests

```bash
npm test
```

### End-to-end tests

```bash
npm run test:e2e
```

### Lint

```bash
npm run lint
```

Warning: current setup notes say `npm run lint` maps to `biome check --write`, so it may modify files. Run only on a clean tree or a disposable branch.

### Results

| Check | Result | Notes |
|---|---|---|
| Unit tests run | Not run |  |
| Unit tests pass | Not tested |  |
| E2E tests run | Not run |  |
| E2E tests pass | Not tested |  |
| Lint run | Not run |  |
| Lint changed files | Not checked |  |

---

## Git Status After Baseline

Run this after install, dev, build, preview, and optional tests.

```bash
git status --short
```

### Results

| Check | Result | Notes |
|---|---|---|
| Working tree clean after baseline | Not checked |  |
| Expected generated files only | Not checked |  |
| Unexpected source changes | Not checked |  |

### Recorded Output

```text
Paste `git status --short` output here.
```

---

## Issues / Errors / Warnings

| ID | Severity | Area | Description | Status |
|---|---|---|---|---|
| SETUP-001 | TBD | TBD | No baseline run has been performed yet. | Open |

---

## Baseline Verdict

Choose one after the test:

- **Pass:** unmodified fork runs locally, generates maps, saves, loads, and builds.
- **Partial:** app runs, but one or more baseline checks failed.
- **Blocked:** install or dev server cannot run yet.
- **Not Run:** baseline has not been attempted.

**Current verdict:** Not Run

### Verdict Notes

```text
Record final baseline verdict here.
```

---

## Meridian Prime Modification Gate

Do not modify source code for Meridian Prime until all required baseline checks are complete.

Required before customization:

| Requirement | Status |
|---|---|
| Fork location chosen | Not done |
| Local clone works | Not tested |
| Node requirement met | Not tested |
| Dependencies install | Not tested |
| Dev server runs | Not tested |
| App opens locally | Not tested |
| New map generates | Not tested |
| Save/load works | Not tested |
| Build works | Not tested |
| Source-orientation notes started | Not started |
| Clean baseline commit or branch exists | Not done |

First allowed Meridian Prime code change after gate:

> Add a Meridian Prime marker/index layer without breaking existing markers or save/load behavior.

---

## Next Action

Choose the fork location and run the unmodified local baseline. Then update this file with exact results.

Recommended next documentation update after test:

`docs/cartography/azgaar-fork/schema/schema-notes.md`

Only start schema orientation after the baseline result is recorded.
