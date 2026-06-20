# Meridian Prime Cartography Engine Setup Test Log

**Status:** Baseline Attempt 2 / Blocked  
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

## Baseline Attempt 2 Summary

| Field | Value |
|---|---|
| Test date | 2026-06-20 |
| Tester | User on local Pop!_OS machine with ChatGPT guidance |
| Host OS | Pop!_OS / Linux, exact version not recorded |
| Shell / terminal | bash terminal |
| Browser | Available, but app not reached yet |
| Fork location chosen | Local-only source baseline first |
| Folder used | `/home/tenet/meridian-cartography-baseline` |
| Git clone URL | `https://github.com/Azgaar/Fantasy-Map-Generator.git` |
| Source ZIP URL attempted | `https://codeload.github.com/Azgaar/Fantasy-Map-Generator/zip/refs/heads/master` |
| Branch tested | Not reached |
| Commit or tag tested | Not reached because source download failed before checkout/extract |
| Node version | `v24.17.0`, meets required `>=24.0.0` |
| Package manager | `npm 11.13.0` |
| Git version | `git version 2.34.1` from earlier screenshot |
| Dependency command used | Not run |
| Dev server command used | Not run |
| Local app URL | Not created |
| Production build command used | Not run |
| Save/load test file | Not created |
| Overall result | Blocked |

---

## Attempt 2 Progress

| Check | Result | Notes |
|---|---|---|
| Node installed | Pass | Installed through nvm. |
| Node requirement met | Pass | `node --version` reported `v24.17.0`. |
| npm available | Pass | `npm --version` reported `11.13.0`. |
| Baseline folder created | Pass | `/home/tenet/meridian-cartography-baseline`. |
| Direct `git clone` | Blocked | Could not connect to `github.com` port 443. |
| `curl -I https://github.com` | Blocked | Could not connect to `github.com` port 443. |
| `curl -4 -I https://github.com` | Blocked | IPv4-only request also failed, so this is not just an IPv6 preference issue. |
| Source ZIP via `codeload.github.com` | Blocked | Could not connect to `codeload.github.com` port 443. |
| Dependency install | Not tested | Source tree unavailable. |
| Dev server | Not tested | Source tree unavailable. |
| Map generation | Not tested | App not launched. |
| Save/load | Not tested | App not launched. |
| Production build | Not tested | Source tree unavailable. |

---

## Fork Location Decision

| Option | Selected? | Notes |
|---|---|---|
| Direct fork under user account | No | Deferred until the unmodified baseline can be run. |
| Fork under project organization | No | Deferred. |
| Local-only clone/source baseline first | Yes | Chosen as the safest first baseline path because it avoids creating a premature project fork. |
| Mirror into custom Meridian Prime repo later | Not yet | Revisit only after the unmodified baseline passes. |

### Decision Notes

- **Chosen path:** Local-only baseline first.
- **Reason:** Safest first test. It preserves the modification gate and avoids committing to a fork location before the plain app runs.
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
| Browser/version | Available, not recorded | App not reached yet. |
| Disk location of attempted baseline | `/home/tenet/meridian-cartography-baseline` | Folder exists. |

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
git clone https://github.com/Azgaar/Fantasy-Map-Generator.git
curl -I https://github.com
curl -4 -I https://github.com
curl -L -o azgaar.zip https://codeload.github.com/Azgaar/Fantasy-Map-Generator/zip/refs/heads/master
```

### Results

| Check | Result | Notes |
|---|---|---|
| `git clone` completed | Failed | Direct `github.com` connection blocked. |
| `origin` remote correct | Not reached | Clone failed before repo was created. |
| `upstream` remote added | Not reached | Clone failed. |
| Source ZIP downloaded | Failed | `codeload.github.com` also blocked. |
| Working tree clean before install | Not reached | No working tree. |
| Commit SHA recorded | Not reached | No checkout or extracted source tree. |

### Recorded Output

```text
fatal: unable to access 'https://github.com/Azgaar/Fantasy-Map-Generator.git/': Failed to connect to github.com port 443: Network is unreachable
curl: (7) Failed to connect to github.com port 443 after 45 ms: Network is unreachable
curl: (7) Failed to connect to github.com port 443 after 35 ms: Network is unreachable
curl: (7) Failed to connect to codeload.github.com port 443 after 47 ms: Network is unreachable
```

---

## Dependency Install Test

### Intended command

```bash
npm ci
```

### Results

| Check | Result | Notes |
|---|---|---|
| Install command used | Not run | Source tree unavailable. |
| Install completed | Not tested | Blocked by GitHub/codeload network access. |
| Warnings encountered | Not recorded | Not reached. |
| Errors encountered | Not recorded | Not reached. |
| Files changed after install | Not checked | No working tree. |

---

## Development Server Test

### Intended command

```bash
npm run dev
```

### Results

| Check | Result | Notes |
|---|---|---|
| Dev server started | Not tested | Source tree unavailable. |
| Local URL shown | Not recorded | No dev server. |
| Terminal errors | Not recorded | Not reached. |
| Browser opened app | Not tested | No dev server. |
| Browser console errors | Not checked | Not reached. |

---

## Baseline App Behavior Test

Do not add Meridian Prime changes during this test.

| Behavior | Result | Notes |
|---|---|---|
| App loads locally | Not tested | Blocked before source acquisition. |
| New map generates | Not tested | Blocked before app launch. |
| Map UI responds | Not tested | Blocked before app launch. |
| Layers menu opens | Not tested | Blocked before app launch. |
| Markers layer visible / available | Not tested | Blocked before app launch. |
| Routes layer visible / available | Not tested | Blocked before app launch. |
| Zones layer visible / available | Not tested | Blocked before app launch. |
| Save `.map` works | Not tested | Blocked before app launch. |
| Reload `.map` works | Not tested | Blocked before app launch. |
| Export image/data works | Not tested | Optional, not reached. |
| No major console errors | Not checked | Browser console not reached. |

---

## Production Build Test

### Intended command

```bash
npm run build
```

### Results

| Check | Result | Notes |
|---|---|---|
| Build command completed | Not tested | Source tree unavailable. |
| TypeScript completed | Not tested | Not reached. |
| Vite build completed | Not tested | Not reached. |
| Build output created | Not checked | No working tree. |
| Warnings encountered | Not recorded | Not reached. |
| Errors encountered | Not recorded | Not reached. |

---

## Preview Test

### Intended command

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

```bash
npm test
npm run test:e2e
npm run lint
```

Warning: current setup notes say `npm run lint` maps to `biome check --write`, so it may modify files. Run only on a clean tree or a disposable branch.

### Results

| Check | Result | Notes |
|---|---|---|
| Unit tests run | Not run | Source tree unavailable. |
| Unit tests pass | Not tested |  |
| E2E tests run | Not run | Source tree unavailable. |
| E2E tests pass | Not tested |  |
| Lint run | Not run | Source tree unavailable. |
| Lint changed files | Not checked | No working tree. |

---

## Git Status After Baseline

### Intended command

```bash
git status --short
```

### Results

| Check | Result | Notes |
|---|---|---|
| Working tree clean after baseline | Not checked | No repo checkout. |
| Expected generated files only | Not checked | No repo checkout. |
| Unexpected source changes | Not checked | No repo checkout. |

---

## Issues / Errors / Warnings

| ID | Severity | Area | Description | Status |
|---|---|---|---|---|
| SETUP-001 | Blocker | Baseline | Baseline could not complete yet. | Open |
| SETUP-002 | Resolved | Node | Node was upgraded to `v24.17.0`, satisfying current Azgaar requirement `>=24.0.0`. | Closed |
| SETUP-003 | Blocker | Network / Git | Direct `github.com:443` is unreachable from the local machine. | Open |
| SETUP-004 | Blocker | Network / Source ZIP | `codeload.github.com:443` is unreachable from the local machine. | Open |
| SETUP-005 | Blocker | Browser app test | No app/browser session was available because source acquisition failed. | Open |

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
Attempt 2 improved the environment by installing Node v24.17.0 and npm 11.13.0 through nvm, satisfying the current Azgaar Node requirement. The baseline remains blocked because both direct git clone from github.com and source ZIP download from codeload.github.com fail with network-unreachable errors. No dependency install, dev server, map generation, save/load, build, preview, tests, or lint commands were run. The Meridian Prime modification gate remains locked.
```

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

Do not modify source code for Meridian Prime until all required baseline checks are complete.

Required before customization:

| Requirement | Status |
|---|---|
| Fork location chosen | Done: local-only baseline first |
| Local/source checkout works | Blocked: `github.com` and `codeload.github.com` unreachable |
| Node requirement met | Done: `v24.17.0` |
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

Source acquisition must be solved before the baseline can continue.

Recommended next route:

1. Use a different network temporarily, such as a phone hotspot, Ethernet, or VPN.
2. Retry direct clone:

```bash
cd "$HOME/meridian-cartography-baseline"
git clone https://github.com/Azgaar/Fantasy-Map-Generator.git
```

3. If direct clone remains blocked but browser download works, manually download the source ZIP in the browser and extract it into `/home/tenet/meridian-cartography-baseline`.
4. Only after the source tree exists, run:

```bash
cd "$HOME/meridian-cartography-baseline/Fantasy-Map-Generator"
npm ci
npm run dev
```

If using a ZIP extraction, the directory may be:

```bash
cd "$HOME/meridian-cartography-baseline/Fantasy-Map-Generator-master"
```

Then test map generation, save `.map`, reload `.map`, and run `npm run build`.

Only start schema orientation after a baseline result is recorded from a source tree that actually runs.
