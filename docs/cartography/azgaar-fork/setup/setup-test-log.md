# Meridian Prime Cartography Engine Setup Test Log

**Status:** Baseline Attempt 1 / Blocked  
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
| Test date | 2026-06-20 |
| Tester | ChatGPT / Meridian Prime Cartography Engine Room |
| Host OS | Linux `0725cb61a07b`, kernel `4.4.0`, x86_64 |
| Shell / terminal | `bash` in `/mnt/data` |
| Browser | Not available / not tested in this environment |
| Fork location chosen | Local-only clone first |
| Fork / clone URL | `https://github.com/Azgaar/Fantasy-Map-Generator.git` |
| Upstream remote URL | `https://github.com/Azgaar/Fantasy-Map-Generator.git` |
| Branch tested | Not reached |
| Commit or tag tested | Not reached because clone failed before commit resolution |
| Node version | `v22.16.0`, below required `>=24.0.0` |
| Package manager | `npm 10.9.2` |
| Dependency command used | Not run |
| Dev server command used | Not run |
| Local app URL | Not created |
| Production build command used | Not run |
| Save/load test file | Not created |
| Overall result | Blocked |

---

## Fork Location Decision

Record the chosen fork strategy here.

| Option | Selected? | Notes |
|---|---|---|
| Direct fork under user account | No | Deferred until the unmodified baseline can be run in a suitable local environment. |
| Fork under project organization | No | Deferred. |
| Local-only clone first | Yes | Chosen as the safest first baseline path because it avoids creating a premature project fork. |
| Mirror into custom Meridian Prime repo later | Not yet | Revisit only after the unmodified baseline passes. |

### Decision Notes

- **Chosen path:** Local-only clone first.
- **Reason:** Safest first test. It preserves the modification gate and avoids committing to a fork location before the plain app runs.
- **Date decided:** 2026-06-20.
- **Canon effect:** None. Tooling only.

---

## Local Environment

| Check | Result | Notes |
|---|---|---|
| OS name/version | Linux `0725cb61a07b 4.4.0 #1 SMP Sun Jan 10 15:06:54 PST 2016 x86_64 GNU/Linux` | Runtime container environment. |
| CPU architecture | x86_64 |  |
| Terminal/shell | bash |  |
| Git version | `git version 2.47.3` |  |
| Node version | `v22.16.0` | Fails current Azgaar requirement of `>=24.0.0`. |
| npm version | `10.9.2` |  |
| Browser/version | Not available / not tested | App behavior and save/load could not be browser-tested. |
| Disk location of attempted clone | `/mnt/data/azgaar-baseline` | Clone failed before repo checkout. |

### Environment Commands

```bash
git --version
node --version
npm --version
python3 --version
uname -a
```

### Recorded Output

```text
/mnt/data
v22.16.0
10.9.2
git version 2.47.3
Python 3.13.5
Linux 0725cb61a07b 4.4.0 #1 SMP Sun Jan 10 15:06:54 PST 2016 x86_64 GNU/Linux
```

---

## Clone / Remote Setup

### Commands Attempted

```bash
rm -rf /mnt/data/azgaar-baseline
mkdir -p /mnt/data/azgaar-baseline
cd /mnt/data/azgaar-baseline
git clone --depth 1 https://github.com/Azgaar/Fantasy-Map-Generator.git
```

### Results

| Check | Result | Notes |
|---|---|---|
| Clone completed | Failed | Runtime shell could not resolve `github.com`. |
| `origin` remote correct | Not reached | Clone failed before repo was created. |
| `upstream` remote added | Not reached | Clone failed. |
| Working tree clean before install | Not reached | No working tree. |
| Commit SHA recorded | Not reached | No checkout. |

### Recorded Output

```text
Cloning into 'Fantasy-Map-Generator'...
fatal: unable to access 'https://github.com/Azgaar/Fantasy-Map-Generator.git/': Could not resolve host: github.com
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
| Install command used | Not run | Clone failed before dependencies could be installed. |
| Install completed | Not tested | Blocked by failed clone and Node version below requirement. |
| Warnings encountered | Not recorded | Not reached. |
| Errors encountered | Not recorded | Not reached. |
| Files changed after install | Not checked | No working tree. |

### Recorded Output

```text
Dependency installation was not attempted because the repository clone failed and the available Node version is below the required >=24.0.0.
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
| Dev server started | Not tested | Blocked by failed clone and Node version below requirement. |
| Local URL shown | Not recorded | No dev server. |
| Terminal errors | Not recorded | Not reached. |
| Browser opened app | Not tested | No dev server and no browser test available. |
| Browser console errors | Not checked | Not reached. |

### Recorded Output

```text
Development server was not attempted.
```

---

## Baseline App Behavior Test

Do not add Meridian Prime changes during this test.

| Behavior | Result | Notes |
|---|---|---|
| App loads locally | Not tested | Blocked before dev server. |
| New map generates | Not tested | Blocked before app launch. |
| Map UI responds | Not tested | Blocked before app launch. |
| Layers menu opens | Not tested | Blocked before app launch. |
| Markers layer visible / available | Not tested | Blocked before app launch. |
| Routes layer visible / available | Not tested | Blocked before app launch. |
| Zones layer visible / available | Not tested | Blocked before app launch. |
| Save `.map` works | Not tested | Blocked before app launch. |
| Reload `.map` works | Not tested | Blocked before app launch. |
| Export image/data works | Not tested | Optional, not reached. |
| No major console errors | Not checked | Browser console unavailable. |

### Save / Load Details

| Field | Value |
|---|---|
| Test map name | Not created |
| Saved file name | Not created |
| Save method used | Not reached |
| Reload method used | Not reached |
| Reload result | Not tested |
| Data loss noticed | Not checked |

### Notes

```text
App behavior could not be tested in this runtime because the repository could not be cloned, Node is below the required version, and no browser-based app session was available.
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
| Build command completed | Not tested | Blocked by failed clone and Node version below requirement. |
| TypeScript completed | Not tested | Not reached. |
| Vite build completed | Not tested | Not reached. |
| Build output created | Not checked | No working tree. |
| Warnings encountered | Not recorded | Not reached. |
| Errors encountered | Not recorded | Not reached. |

### Recorded Output

```text
Production build was not attempted.
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
| Preview server started | Not tested | Build was not run. |
| Preview URL opened | Not tested | No preview server. |
| Built app loads | Not tested | No build output. |
| New map generates in preview | Not tested | No preview server. |
| Save/load works in preview | Not tested | Optional, not reached. |

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
| Unit tests run | Not run | Blocked before dependency install. |
| Unit tests pass | Not tested |  |
| E2E tests run | Not run | Blocked before dependency install. |
| E2E tests pass | Not tested |  |
| Lint run | Not run | Blocked before dependency install. |
| Lint changed files | Not checked | No working tree. |

---

## Git Status After Baseline

Run this after install, dev, build, preview, and optional tests.

```bash
git status --short
```

### Results

| Check | Result | Notes |
|---|---|---|
| Working tree clean after baseline | Not checked | No repo checkout. |
| Expected generated files only | Not checked | No repo checkout. |
| Unexpected source changes | Not checked | No repo checkout. |

### Recorded Output

```text
git status was not available because clone failed before a working tree was created.
```

---

## Issues / Errors / Warnings

| ID | Severity | Area | Description | Status |
|---|---|---|---|---|
| SETUP-001 | Blocker | Baseline | Baseline could not complete in this runtime. | Open |
| SETUP-002 | Blocker | Node | Runtime Node version is `v22.16.0`, below current Azgaar requirement `>=24.0.0`. | Open |
| SETUP-003 | Blocker | Network / Git | Shell `git clone` failed because `github.com` could not be resolved. | Open |
| SETUP-004 | Blocker | Browser app test | No app/browser session was available, so map generation and save/load could not be tested. | Open |

---

## Baseline Verdict

Choose one after the test:

- **Pass:** unmodified fork runs locally, generates maps, saves, loads, and builds.
- **Partial:** app runs, but one or more baseline checks failed.
- **Blocked:** install or dev server cannot run yet.
- **Not Run:** baseline has not been attempted.

**Current verdict:** Blocked

### Verdict Notes

```text
Local-only clone first was chosen as the fork strategy, but the baseline could not proceed in this runtime. The shell environment cannot resolve github.com for git clone, and the installed Node version is v22.16.0 while current Azgaar package metadata requires >=24.0.0. No install, dev server, map generation, save/load, build, preview, tests, or lint commands were run. The Meridian Prime modification gate remains locked.
```

---

## Meridian Prime Modification Gate

Do not modify source code for Meridian Prime until all required baseline checks are complete.

Required before customization:

| Requirement | Status |
|---|---|
| Fork location chosen | Done: local-only clone first |
| Local clone works | Blocked: DNS/network failure resolving `github.com` |
| Node requirement met | Failed: available Node `v22.16.0`, required `>=24.0.0` |
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

Run the unmodified local baseline in an environment with:

1. GitHub network access from the shell.
2. Node `>=24.0.0`.
3. A browser available for manual or automated app testing.

Then update this file with exact results for:

- clone / remote setup
- dependency install
- dev server
- map generation
- save `.map`
- reload `.map`
- production build
- preview, if tested
- tests, if run
- final git status

Recommended next documentation update after a successful or partial local run:

`docs/cartography/azgaar-fork/schema/schema-notes.md`

Only start schema orientation after a baseline result is recorded from a suitable local environment.
