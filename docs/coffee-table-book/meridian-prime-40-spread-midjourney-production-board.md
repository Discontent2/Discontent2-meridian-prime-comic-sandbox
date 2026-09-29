# Meridian Prime — 40-Spread Midjourney Production Board

**Status:** Sandbox Editorial Production / Non-Canon Until Promoted  
**Repository:** `Discontent2/Discontent2-meridian-prime-comic-sandbox`  
**Parent Plan:** `docs/coffee-table-book/meridian-prime-80-page-spread-plan.md`  
**Working Title:** *MERIDIAN PRIME: The Road Remembers*  
**Format:** 80 interior pages / 40 editorial spreads  
**Primary Use:** Midjourney generation board, art direction, canon control, caption planning, visual continuity  
**Created:** 2026-09-28  

---

# Production Method

## Photographic Thesis

The book should look as though an unusually patient expedition photographer traveled Meridian Prime with access to routes, cities, workers, machines, restricted thresholds, and occasionally evidence they should not have possessed.

The target is **editorial expedition photography**, not concept art.

Use three photographic modes:

1. **Medium-format environmental photography**  
   Landscapes, architecture, threshold images, large machines. Deliberate composition, fine detail, slow observation, restrained perspective distortion.

2. **35mm documentary reportage**  
   Workers, cities, camps, streets, interiors, human-scale moments. Slight imperfection, motion residue, available light, objects partly interrupting the frame.

3. **Evidence photography**  
   W.A.S., cryptids, uncertain sightings. Telephoto compression, imperfect focus, degraded media, archive contact-sheet logic, ambiguous subject scale.

## Global Visual Lock

Across the whole book preserve:

- crushed blacks
- midnight navy / blue-black foundations
- spectral cobalt and cyan in cold environments
- rare ember-red practical accents
- dirty amber work light
- mineral haze, fog, condensation, vapor, dust
- material realism: wet stone, crystal dust, oxidized steel, worn cloth, cables, pressure plumbing
- monumental scale with people and machines often kept small
- practical light sources rather than invisible studio lighting
- working surfaces rather than polished sci-fi
- one strong visual idea per image
- beauty that never removes danger

Avoid:

- glossy generic science fiction
- heroic character posing
- generic fantasy
- clean utopian futurism on the surface
- excessive neon
- videogame key-art composition
- centered poster characters unless the spread specifically calls for a portrait
- over-sharpened HDR
- text baked into images unless deliberately treated as unreadable archival texture

## Midjourney Parameter Baseline

Current Midjourney controls support aspect ratio with `--ar`, stylization with `--s`, exclusions with `--no`, and Style References for visual continuity.

For this project:

- **Canon-heavy images:** generally `--s 40–90`
- **Atmospheric / abstract images:** generally `--s 100–180`
- **Do not use high chaos by default.**
- Add approved images later as Style References rather than overloading prompts with style adjectives.
- Do not bake final captions, signs, archive labels, or body text into generated art. Add typography in layout.

## Spread Crop Rule

A double-page spread has a dangerous center gutter.

For all full-bleed `2:1` images:

- keep faces out of the central 12% unless the composition intentionally bridges the gutter
- do not place small critical objects exactly at center
- keep vehicles crossing the gutter large enough that losing a narrow slice does not break their silhouette
- reserve lower corners or outer thirds for captions when possible

## Consistency Reference Protocol

Once the first successful generations are selected, establish these reference anchors:

**REF-A — Global Cold World**  
Selected output from Spread 01, 03, or 06. Use for overall blacks, cobalt atmosphere, grain, contrast, and practical red/amber lights.

**REF-B — Red Umbrielor**  
Approved Spread 07. Use whenever 289 appears later.

**REF-C — 409**  
Approved Spread 08. Use whenever 409 appears later.

**REF-D — Traverse Town / MITE II**  
Approved Spread 09 or 33. Use for Mod geometry, spacing, lights, and convoy scale.

**REF-E — Hydropolis**  
Approved Spread 18. Use for black glass, magenta rail-light, canal architecture, wet atmosphere.

**REF-F — Antisapien**  
Approved Spread 20. Use for skin tone, eyes, facial anatomy, and portrait realism.

**REF-G — Contact Frame**  
Approved Spread 21. Use for any later true Àæonos-origin visitor.

**REF-H — Craton Gate / Interior**  
Approved Spread 23 and/or 24. Use for climate contrast, borer reuse, brass Aeonolacertian additions, wet quartz, and humid light.

**REF-I — Aeonolacertian Civilian Anatomy**  
Approved Spread 25. Use for later Aeonolacertian crowds, tails, hands, feet, faces, clothing, and body-plan variety.

**REF-J — W.A.S. Archive**  
Approved Spread 37. Use only for the apocryphal / evidence section.

---

# SECTION I — THE PROMISED WORLD

## Spread 01 — Pages 1–2
# Before the Map

**Canon Status:** Visual-development framing.

### Midjourney-Ready Prompt
```
an almost empty documentary landscape photograph on Meridian Prime before dawn, near-total blackness, a razor-thin mineral horizon crossing the lower third, cold cobalt haze barely separating ground from sky, one tiny distant red route beacon glowing alone, crystalline dust catching almost no light, enormous negative space, severe quiet, believable alien geology, expedition photography, subtle natural color-negative film grain, deep blacks with detail preserved, no visible people, no spectacle --ar 2:1 --s 120
```

### Aspect Ratio
`2:1` full bleed.

### Camera / Lens
6x7 medium-format environmental photograph, 80mm normal lens, tripod-height camera, horizon deliberately low.

### Lighting
Pre-dawn ambient cobalt only; one red practical beacon. No moonbeam or cinematic key light.

### Canon Constraints
- Meridian Prime should read as mineral, cold, pressure-haunted.
- Do not imply a specific protected location.
- Red is a tiny signal, not ambient illumination.

### Negative Prompt
```
--no starscape spectacle, giant moon, city skyline, spacecraft, person, fantasy mountains, neon, bright daylight, text, logo, lens flare
```

### Caption
**Before the map, there is only the route.**

### Consistency References
- `docs/visual-development/visual-style-guide.md`
- `production/reels/meridian-prime-reel-01/visual-language.md`
- Becomes candidate **REF-A**.

---

## Spread 02 — Pages 3–4
# The Promised World

**Canon Status:** Main canon.

### Midjourney-Ready Prompt
```
high-altitude orbital documentary photograph of Aeonos, the world humans call Meridian Prime, curved planetary limb filling most of the frame, layered cobalt atmosphere, fractured pale mineral continents, dark basin systems, cloud bands and weather obscuring geography, no Earth-like blue-marble perfection, a tiny almost-lost artificial object in high orbit hinting at the Lodestar without dominating the image, observational scientific photography with poetic scale, realistic planetary light scattering, fine film grain --ar 2:1 --s 90
```

### Aspect Ratio
`2:1`.

### Camera / Lens
Long orbital survey framing, equivalent 120–180mm compression.

### Lighting
Natural stellar side-light; atmospheric limb glow restrained.

### Canon Constraints
- Aeonos is Meridian Prime / Kepler-1649c.
- Do not depict àæonos as a visible duplicate nearby.
- The Lodestar is present but not yet visually explained.

### Negative Prompt
```
--no Earth, blue marble, ringed planet, two identical planets, fantasy continents, giant spaceship foreground, star destroyer, glowing magic, text
```

### Caption
**The mission name became the name of the world.**

### Consistency References
- `docs/meridian-prime-bible.md`
- REF-A for grade once established.

---

## Spread 03 — Pages 5–6
# The Star That Moves

**Canon Status:** Main canon.

### Midjourney-Ready Prompt
```
night documentary photograph from the surface of Meridian Prime, tiny lived-in settlement and industrial roofs along the bottom edge, cold black-blue sky dominating the spread, the Lodestar crossing overhead as an immense distant generation ship whose scale reads through length and repeated red blinking navigation lights rather than close detail, artificial star becoming recognizable as a vessel, thin cloud and mineral haze partly obscuring it, ordinary people outside only as tiny silhouettes looking up or continuing work, awe mixed with surveillance, restrained realistic optics, expedition photojournalism --ar 2:1 --s 80
```

### Aspect Ratio
`2:1`.

### Camera / Lens
35mm camera, 50mm lens, low horizon, long exposure short enough to keep the Lodestar readable.

### Lighting
Settlement practicals, red orbital lights, faint cold sky. No dramatic searchlights.

### Canon Constraints
- The Lodestar remains active in orbit.
- It must read as founding vessel and current corporate citadel, not wreckage.
- Red blinking lights are a defining surface image.

### Negative Prompt
```
--no crashed ship, spaceship hovering over town, attack beams, laser fire, giant moon, utopian city, cyberpunk billboard, fantasy stars, readable signage
```

### Caption
**The ark became a boardroom. The cradle became a throne.**

### Consistency References
- `docs/meridian-prime-bible.md`
- REF-A candidate.

---

## Spread 04 — Pages 7–8
# Two Worlds

**Canon Status:** Main canon cosmology.

### Midjourney-Ready Prompt
```
restrained scientific-imaging tableau suggesting two quantum-entangled worlds without depicting them as mirror copies, one matter-world planetary surface rendered through mineral topography and atmospheric data, one separate anti-matter counterpart represented through interference imaging, black-glass signal structure and spectral magenta-teal data traces, asymmetrical compositions linked by fine resonance bands and discontinuous visual echoes, documentary observatory aesthetic rather than fantasy cosmic art, dark field, elegant ambiguity, no literal portal --ar 2:1 --s 150
```

### Aspect Ratio
`2:1`.

### Camera / Lens
Not literal camera photography. Treat as observatory composite / scientific plate.

### Lighting
Data-derived luminous accents over deep black.

### Canon Constraints
- Aeonos and àæonos are entangled, not identical.
- Distinct geography and histories.
- Do not establish gateway mechanics.
- Magenta / teal can imply àæonos signal culture without turning it into magic.

### Negative Prompt
```
--no mirror planets, yin yang planets, wormhole, portal ring, fantasy nebula, magical energy beam, duplicate continents, collision, explosion, text
```

### Caption
**Entanglement creates connection, not sameness.**

### Consistency References
- `docs/meridian-prime-bible.md`
- `docs/cosmology/core-boundary-map.md`
- Later Hydropolis / signal imagery should echo this subtly.

---

## Spread 05 — Pages 9–10
# Arrival Still Happens Every Day

**Canon Status:** Main canon.

### Midjourney-Ready Prompt
```
aging but exceptionally maintained colonization-era shuttle descending toward Prime Ops Space Port on Meridian Prime, rugged elegant reusable spacecraft with visible heat wear, repaired panels and old mission-era engineering, cold industrial landing complex below, vapor and blown mineral dust folding around landing gear, ground crews tiny for scale, no sleek luxury styling, documentary aviation photography from a safe distant service road, history functioning as daily infrastructure --ar 2:1 --s 70
```

### Aspect Ratio
`2:1`.

### Camera / Lens
35mm photojournalism, 135mm telephoto, compressed landing environment.

### Lighting
Cold morning overcast with warm landing / runway practicals.

### Canon Constraints
- Original Lodestar shuttles remain in use.
- Old but exceptionally well built.
- Prime Ops is controlled, functional, and bureaucratic.
- Shuttle should feel maintained, not museum-clean.

### Negative Prompt
```
--no rocket launch fireball, futuristic chrome, private jet, space fighter, military attack, airport terminal glamour, pristine surfaces, fantasy spacecraft
```

### Caption
**Every shuttle launch is commute and communion.**

### Consistency References
- `docs/meridian-prime-bible.md`
- REF-A.

---

# SECTION II — THE ROAD DOWN

## Spread 06 — Pages 11–12
# Prime Ops

**Canon Status:** Main canon.

### Midjourney-Ready Prompt
```
pre-dawn documentary photograph inside Prime Ops surface staging yards, tracked Traverse tractors idling in cold fog, fuel operations, bundled route crews crossing between machines, maintenance gantries, controlled signage shapes without readable text, frost on steel, vapor from exhaust and heated lines, dirty amber work lamps against cobalt darkness, official bureaucracy expressed through lanes, barriers and standardized equipment, field workers already scuffing the order, candid expedition photojournalism, no heroic posing --ar 2:1 --s 65
```

### Aspect Ratio
`2:1`.

### Camera / Lens
35mm reportage, 35mm lens, shoulder height, foreground obstruction from machinery edge.

### Lighting
Pre-dawn cobalt; amber sodium / work lamps; limited red indicators.

### Canon Constraints
- Prime Ops = central operational departure hub.
- Official, useful, controlling.
- Surface human tech should retain degraded dieselpunk / industrial logic.

### Negative Prompt
```
--no futuristic airport, spotless hangar, luxury sci-fi, army parade, steampunk cosplay, hero lineup, bright daylight, neon city
```

### Caption
**The route begins where procedure becomes weather.**

### Consistency References
- `docs/traverse-system.md`
- `docs/visual-development/visual-style-guide.md`
- Candidate REF-A if strongest cold-world result.

---

## Spread 07 — Pages 13–14
# 289

**Canon Status:** Planning canon / visual-development authority.

### Midjourney-Ready Prompt
```
industrial documentary portrait of Red Umbrielor, Traverse tractor call number 289, enormous articulated four-track survival machine parked alone before departure, scarred red paint, broad heavy stance, multidirectional front blade, work-worn saddle tanks, frost, oil staining, field repairs, dense functional cab, number 289 visible only on the side engine compartment, RED UMBRIELOR marking above the rear tracks on the saddle-tank area, old but meticulously kept alive, no driver posing, tiny mechanic partly hidden near a track for scale, 6x7 medium-format machinery photography --ar 2:1 --s 55
```

### Aspect Ratio
`2:1`.

### Camera / Lens
6x7 medium format, 75mm lens, slightly low but not heroic; three-quarter side view preserving markings.

### Lighting
Flat cold dawn with weak amber cab glow. Frost highlights rather than studio rim light.

### Canon Constraints
- 289 is call number.
- Red Umbrielor is the machine name.
- Massive tracked industrial Quadtrack logic.
- Scarred red paint, maintained rather than pristine.
- Front blade required.
- Do not make it pull the entire convoy in this portrait.
- Avoid unresolved model-number conflict in visible text.

### Negative Prompt
```
--no tank turret, weapons, monster truck, Mad Max spikes, locomotive, wheels, showroom polish, luxury cab, giant logo, snowplow truck, driver portrait
```

### Caption
**289. Old enough to complain. Too necessary to retire.**

### Consistency References
- `docs/equipment/mite-ii-convoy-structure.md`
- `docs/visual-development/red-umbrielor-and-traverse-vehicles.md`
- `docs/comics/mite-ii-convoy-structure-review.md`
- Establish **REF-B**.

---

## Spread 08 — Pages 15–16
# The Machine That Reads First

**Canon Status:** MITE II planning canon.

### Midjourney-Ready Prompt
```
documentary field photograph of lead sensor tractor 409 moving alone across crystalline regolith, compact red NCI-modded tracked groomer body, wide tracks, front blade carrying a very long 20-foot ground-penetrating-radar boom extending far ahead, GPR unit at boom tip, support mast and cable visibly functional, no trailer, immense empty mineral terrain emphasizing how far ahead the sensor reaches, tiny drifting crystal dust, competent improvised engineering rather than sleek reconnaissance vehicle, lateral composition with boom slicing across the frame --ar 2:1 --s 55
```

### Aspect Ratio
`2:1`.

### Camera / Lens
6x7 or 35mm, 85–100mm lens from slight distance, side profile.

### Lighting
Cold low-angle morning light; weak route lamps if needed.

### Canon Constraints
- 409 has no name / nickname.
- Pulls nothing.
- Compact tracked crystal groomer.
- GPR boom is defining silhouette feature.
- Not a tank or snowmobile.

### Negative Prompt
```
--no trailer, cargo train, weapons, tank, radar dish on roof, futuristic scout car, wheels, snowmobile, nickname lettering, giant 409 repeated everywhere
```

### Caption
**409 reads the ground before the heavier machines believe it.**

### Consistency References
- `docs/equipment/mite-ii-convoy-structure.md`
- `docs/comics/mite-ii-convoy-structure-review.md`
- Establish **REF-C**.

---

## Spread 09 — Pages 17–18
# Traverse Town

**Canon Status:** Planning / production canon.

### Midjourney-Ready Prompt
```
elevated documentary photograph at blue hour of MITE II parked into Traverse Town formation, two long parallel rows of heavy red modular container-based Traverse modules, a wide central tractor alley between them, tracked tractors still clearly part of the working layout, module-mounted work lights only, black fuel bladders remaining at the train tails, tongues and drawbars visibly connecting modules, cold mineral ground, frost and vapor, a temporary town made entirely from a convoy without becoming a permanent base, small crew figures moving between equipment --ar 2:1 --s 60
```

### Aspect Ratio
`2:1`.

### Camera / Lens
Elevated 6x7 medium format, 55mm wide-normal lens, oblique overhead rather than drone-vertical.

### Lighting
Blue hour, dirty amber Mod lights, isolated red markers.

### Canon Constraints
- Two parallel Mod rows.
- Central tractor alley.
- Mods remain on tracked platforms, not unloaded onto ground.
- Lights attached to Mods, no decorative street lamps.
- Fuel tails remain connected.
- Traverse Town is a parked working convoy, not a base.

### Negative Prompt
```
--no tents, permanent buildings, mining colony, streetlights, unloaded shipping containers, railroad tracks, train station, festival camp, military base
```

### Caption
**At the end of shift, the convoy becomes a town without ever stopping being a machine.**

### Consistency References
- `docs/comics/traverse-town-layout-guide.md`
- `docs/equipment/mite-ii-convoy-structure.md`
- Establish **REF-D**.

---

## Spread 10 — Pages 19–20
# The Prime Plateau

**Canon Status:** Main canon.

### Midjourney-Ready Prompt
```
vast medium-format landscape photograph from the Prime Plateau on Meridian Prime, wind-carved crystal shelf in the foreground, route infrastructure tiny along the edge, immense canyon system dropping toward lower basins, weather layer rolling below camera elevation so the viewer looks over cloud and fog toward distant mineral country, cold blue-gray atmosphere, no postcard beauty, sense of logistics and consequence, one convoy parked as nearly invisible scale markers --ar 2:1 --s 80
```

### Aspect Ratio
`2:1`.

### Camera / Lens
6x7 medium format, 45mm wide lens, horizon high enough to show descent.

### Lighting
High cold overcast with pockets of light in distant basin.

### Canon Constraints
- Plateau is mid-elevation staging shelf.
- Connects high Prime Ops / Great Cut / lower Dry Circuit sphere.
- Keep exact route topology noncommittal where canon remains flexible.

### Negative Prompt
```
--no alpine Earth valley, fantasy castle, huge city, tropical jungle foreground, magical cliffs, floating islands, dramatic sunbeams
```

### Caption
**Here the Dry Circuit stops being a line on a map.**

### Consistency References
- `docs/locations/prime-plateau.md`
- `docs/cartography/planetary-route-topology.md`
- REF-A.

---

## Spread 11 — Pages 21–22
# Charterhold

**Canon Status:** Main canon.

### Midjourney-Ready Prompt
```
candid 35mm street photograph in Charterhold, capital of the Bought Nation, fog-wet industrial civic street beneath a cargo gantry, patched roofs, archive building mixed with repair yards and route infrastructure, ordinary workers in practical cold workwear moving through frame, old civic banners and mural surfaces without readable generated text, wet metal, cloud-rainforest vegetation pressing around the city edges, Prime Ops order beside NCI improvisation, no monumental government palace --ar 2:1 --s 65
```

### Aspect Ratio
`2:1`.

### Camera / Lens
35mm camera, 35mm lens, eye level, slight foreground occlusion.

### Lighting
Diffuse fog daylight, warm shop interiors.

### Canon Constraints
- Charterhold = staging capital, not marble capital.
- Prime Plateau / cloud-rainforest geography.
- Government, repair, contractor, archive, and route functions coexist.

### Negative Prompt
```
--no marble capitol, skyscraper downtown, medieval city, pristine solarpunk, cyberpunk neon, fantasy market, parade, hero subject
```

### Caption
**A capital built from promises someone else tried to turn into receipts.**

### Consistency References
- `docs/locations/charterhold.md`
- `docs/visual-development/visual-style-guide.md`

---

## Spread 12 — Pages 23–24
# Remembrance Yard

**Canon Status:** Main canon location detail.

### Midjourney-Ready Prompt
```
quiet documentary photograph in Charterhold Remembrance Yard, route-death markers and name walls receding into thick cold fog, modest memorial materials mixed with old machine parts and route markers, one bundled person standing off-center with back partly turned, no ceremonial pose, wet paving and condensation, soft ambient gray-blue, grief expressed through scale and absence rather than spectacle, fine 35mm grain --ar 2:1 --s 55
```

### Aspect Ratio
`2:1`.

### Camera / Lens
35mm, 50mm lens, eye level.

### Lighting
Fog-diffused daylight, no theatrical spotlight.

### Canon Constraints
- Memorializes lost migrants, route workers, snowfield crews, charter families.
- Keep identities generic unless a later layout caption names someone.
- No Book One protected mystery reveals.

### Negative Prompt
```
--no cemetery crosses, gothic graveyard, angel statues, military honor guard, readable names, dramatic crying closeup, fantasy memorial
```

### Caption
**The route keeps names longer than the paperwork does.**

### Consistency References
- `docs/locations/charterhold.md`
- Global 35mm reportage look.

---

## Spread 13 — Pages 25–26
# Ledger Falls

**Canon Status:** Main canon.

### Midjourney-Ready Prompt
```
wide documentary photograph of Ledger Falls on the Prime Plateau border, roaring cataract cutting through a cloud rainforest logging town, moss-slick saw gantries, wet timber cranes, tiered mill platforms, worker housing on stilts above flood-prone ground, fog and spray swallowing the upper canopy, heavy industrial timber work embedded in living cloudforest, people small and busy, practical diesel machinery, beautiful and morally complicated rather than picturesque --ar 2:1 --s 75
```

### Aspect Ratio
`2:1`.

### Camera / Lens
6x7 medium format, 55mm lens from elevated opposite bank.

### Lighting
Overcast with diffused bright cataract mist; scattered warm mill lamps.

### Canon Constraints
- Border logging town, not national capital.
- Cataracts, cloudwood economy, permit conflict, worker stilts.
- Cloud rainforest should look native to Meridian Prime, not Pacific Northwest stock imagery.

### Negative Prompt
```
--no lumberjack nostalgia, rustic Earth mill, medieval watermill, fantasy waterfall city, pristine eco-resort, neon, sunny postcard
```

### Caption
**At Ledger Falls, the forest is protected, leased, necessary, sacred, and stolen at the same time.**

### Consistency References
- `docs/locations/ledger-falls.md`
- `docs/worldbuilding/ecology/prime-plateau-cloud-rainforest.md`

---

## Spread 14 — Pages 27–28
# The Green Line

**Canon Status:** Main canon conflict with ecology support.

### Midjourney-Ready Prompt
```
environmental documentary portrait of a single enormous Cloudwood tree at the disputed Green Line outside Ledger Falls, crystal-veined bark disappearing upward into fog canopy, small corporate cut-number marking on the trunk beside a separate handmade memorial marker, several workers at the base rendered tiny for scale, wet root system crossing damaged route surface, logging equipment waiting outside frame rather than dominating, moral tension contained in one tree, medium-format detail and restrained color --ar 2:1 --s 70
```

### Aspect Ratio
`2:1`.

### Camera / Lens
6x7, 65mm lens, low-to-normal perspective preserving full trunk scale.

### Lighting
Soft wet forest light, slight warm reflection from nearby machinery.

### Canon Constraints
- Green Line is contested legal / ecological boundary.
- Cloudwood is valuable and politically loaded.
- Memorial marking and cut marking coexist.
- Do not resolve who is legally correct.

### Negative Prompt
```
--no Earth redwood, magical glowing tree, elves, chainsaw hero, clearcut wasteland, protest signs with readable text, fantasy runes
```

### Caption
**Some trees carry two names: the one on the permit and the one people refuse to lose.**

### Consistency References
- `docs/locations/ledger-falls.md`
- `docs/worldbuilding/ecology/meridian-prime-megaflora.md` for development support.

---

## Spread 15 — Pages 29–30
# The Great Cut

**Canon Status:** Main canon geography; optional development ecology.

### Midjourney-Ready Prompt
```
immense documentary landscape of a Meridian Prime Traverse descending the Great Cut, tracked convoy tiny on switchback shelves carved into mineral canyon walls, black and cobalt depth, fog moving through vertical space, occasional giant fernlike resonant canyon plants and rope-like hanging root systems used only as subtle native ecology, no action scene, danger conveyed through exposure and scale, medium-format expedition photography, route markers barely visible --ar 2:1 --s 85
```

### Aspect Ratio
`2:1`.

### Camera / Lens
6x7, 100mm lens from opposite canyon wall to compress switchbacks.

### Lighting
Cold indirect canyon light with dirty amber vehicle lamps.

### Canon Constraints
- Great Cut / canyon naming remains partly expandable.
- Traverse uses tracked crawlers, not trains.
- Echo Fern / Cataract Beard details are development material only and may be omitted if strict canon edition is required.

### Negative Prompt
```
--no railroad, train, paved highway, Earth Grand Canyon, fantasy rope bridges, flying vehicles, giant monster attack, bright sun
```

### Caption
**Down is not a direction here. It is a procedure.**

### Consistency References
- `docs/locations/prime-plateau.md`
- `docs/worldbuilding/ecology/meridian-prime-megaflora.md` optional.
- REF-D for vehicle scale if MITE II specifically depicted.

---

## Spread 16 — Pages 31–32
# When the Road Becomes Water

**Canon Status:** Main canon seasonal logic.

### Midjourney-Ready Prompt
```
paired documentary landscape presented as one coherent diptych, the same Meridian Prime canyon route in two seasonal states from nearly identical camera position: left side dry-season Traverse road on exposed switchbacks and mineral channels, right side cataract season with violent water occupying those same channels and cutting across the former road geometry, identical cliff landmarks prove it is the same place, restrained scientific expedition photography, no fantasy transformation effect --ar 2:1 --s 70
```

### Aspect Ratio
`2:1`.

### Camera / Lens
Matched 6x7 viewpoints, 65mm lens.

### Lighting
Similar overcast light in both halves to emphasize geographic change, not time-of-day change.

### Canon Constraints
- Seasonal transformation is fundamental.
- Roads can become water routes / hazards.
- Do not imply magical instant transformation.

### Negative Prompt
```
--no split-screen special effects, magical morphing, before-after labels, text, tsunami city destruction, fantasy waterfall, tropical river
```

### Caption
**On Meridian Prime, a road is sometimes only the dry-season name for a river.**

### Consistency References
- `docs/cartography/seasonal-map-logic.md`
- `docs/locations/prime-plateau.md`

---

# SECTION III — WHERE THE WATER REMEMBERS

## Spread 17 — Pages 33–34
# The Mirror Basin, Dry

**Canon Status:** Main canon.

### Midjourney-Ready Prompt
```
vast dry-season documentary landscape of the Mirror Basin containing Hydropolis, exposed hydrocrystal flats extending to the horizon, dry mirror canals cut through pale mineral crust, black-veined root plates and buried infrastructure exposed where water once stood, distant black-glass towers and rail structures shimmering through heat and mineral haze, almost no people visible, alien lowland basin that clearly remembers being underwater, medium-format environmental photography --ar 2:1 --s 85
```

### Aspect Ratio
`2:1`.

### Camera / Lens
6x7, 65mm lens, high but ground-based viewpoint.

### Lighting
Hard dry daylight filtered by mineral haze; keep blacks deep.

### Canon Constraints
- Hydropolis / Mirror Basin changes shape with wet-dry cycle.
- Do not turn dry season into abandoned-city apocalypse.
- City is active, merely spatially transformed.

### Negative Prompt
```
--no desert Dubai, ruined apocalypse city, sand dunes, generic salt flat, cyberpunk neon rain, abandoned skyscrapers, fantasy crystal castle
```

### Caption
**The water leaves. The city does not.**

### Consistency References
- `docs/locations/hydropolis.md`
- Builds toward REF-E.

---

## Spread 18 — Pages 35–36
# Hydropolis

**Canon Status:** Main canon.

### Midjourney-Ready Prompt
```
wet-season Hydropolis at nightfall, a seasonal Antisapien canal and tower city rising from the flooded Mirror Basin, black-glass towers reflected in dark water, magenta rail-light running beneath canal edges and through infrastructure, signal spires, black-glass barges, floating courts and layered walkways, blue-skinned residents small within the city, teal optical accents rare and precise, humid haze, rain and water reflections controlled rather than neon overload, sophisticated cyberpunk civilization built from water memory and signal politics, medium-format documentary cityscape --ar 2:1 --s 85
```

### Aspect Ratio
`2:1`.

### Camera / Lens
6x7 medium format, 55mm lens from elevated canal-side position.

### Lighting
Blue-black wet atmosphere; magenta rail-light; sparse teal signal highlights; warm interiors minimal.

### Canon Constraints
- Hydropolis = Antisapien-controlled redoubt.
- Wet season = canal / tower / barge / floating-court city.
- Black glass + magenta rail-light are core motifs.
- Not World Works territory.
- Not generic rainy cyberpunk metropolis.

### Negative Prompt
```
--no Tokyo, Times Square, hologram ads, flying cars, Blade Runner imitation, human-majority crowd, fantasy towers, rainbow neon, pointed ears
```

### Caption
**Hydropolis is a place, a network, a season, and a refusal.**

### Consistency References
- `docs/locations/hydropolis.md`
- `docs/visual-development/visual-style-guide.md`
- Establish **REF-E**.

---

## Spread 19 — Pages 37–38
# After the Water Leaves

**Canon Status:** Main canon.

### Midjourney-Ready Prompt
```
dry-season Hydropolis from a viewpoint that clearly belongs to the same city as the wet-season reference: black-glass towers now standing above exposed crystal flats, empty mirror canals revealing rail tunnels, server access ribs, sealed vault entrances and infrastructure that was submerged or water-adjacent during wet season, small blue-skinned Antisapien residents using dry corridors and lower routes, magenta signal lines still active but less reflected, documentary architectural photography, dry mineral haze --ar 2:1 --s 65
```

### Aspect Ratio
`2:1`.

### Camera / Lens
Match Spread 18 lens family where possible, 55–65mm.

### Lighting
Dry late afternoon; black glass remains rich; magenta practicals modest.

### Canon Constraints
- Same civilization, different seasonal geometry.
- Dry season exposes lower infrastructure.
- Hydropolis remains active.
- Use REF-E strongly once available.

### Negative Prompt
```
--no abandoned ruins, post-apocalypse, sand-covered city, human-only crowd, generic desert cyberpunk, destroyed towers, giant holograms
```

### Caption
**In dry season, Hydropolis turns its underside into streets.**

### Consistency References
- `docs/locations/hydropolis.md`
- **REF-E** mandatory once established.

---

## Spread 20 — Pages 39–40
# Signal-Band Citizen

**Canon Status:** Main canon species portrait.

### Midjourney-Ready Prompt
```
intimate documentary portrait of an adult Antisapien citizen of Hydropolis, clearly blue skin with natural pore and skin texture, black irises, precise magenta pupils, teal tapetum lucidum catching a small off-axis light, ordinary culturally specific dark technical clothing with restrained signal-band detail, no pointed ears, no undead traits, no fantasy jewelry overload, calm intelligent expression looking slightly past camera, minimal black-glass and wet-city background falling out of focus, editorial 85mm portrait, candid dignity rather than fashion pose --ar 4:5 --s 50
```

### Aspect Ratio
`4:5` portrait placed asymmetrically across the spread with caption / negative space on the opposite page.

### Camera / Lens
35mm full-frame equivalent, 85mm portrait lens at f/2.8.

### Lighting
Soft window / canal light, small teal retinal catch from practical source, black background.

### Canon Constraints
- Blue skin.
- Black irises.
- Magenta pupils.
- Teal tapetum lucidum.
- No elf / orc / zombie coding.
- Antisapiens are matter-compatible; do not put this ordinary citizen inside a Contact Frame.

### Negative Prompt
```
--no pointed ears, elf, orc, zombie, corpse, glowing entire eyes, cyan skin, purple skin, vampire, fantasy armor, beauty glamour retouching, face tattoos unless later specified
```

### Caption
**The human record calls them Antisapiens. Hydropolis has older arguments about the name.**

### Consistency References
- `docs/species-guide.md`
- `docs/locations/hydropolis.md`
- Establish **REF-F**.

---

## Spread 21 — Pages 41–42
# A Visitor Who Cannot Touch the World

**Canon Status:** Main canon.

### Midjourney-Ready Prompt
```
documentary photograph of a true Àæonos-origin conjugate-life visitor moving through ordinary Hydropolis inside a Conjugate Contact Frame, the frame is a matter-built pressure-world containment body rather than a fabric spacesuit, nested hard shell, sealed articulated joints, visible field rings and containment ribs, radiation-scored panels, a subtle suspended inner presence separated from the exterior by non-contact layers, black-glass canal architecture and blue-skinned Antisapien pedestrians treating the visitor as rare but real, poignant physical distance without melodrama, realistic industrial engineering --ar 2:1 --s 60
```

### Aspect Ratio
`2:1`.

### Camera / Lens
35mm reportage, 50mm lens, observer distance 5–8 meters.

### Lighting
Hydropolis wet practicals; magenta reflections on matter shell; no magical glow aura.

### Canon Constraints
- Contact Frame exterior is matter-compatible.
- Visitor never directly touches matter.
- Nested shell / field-separated habitat.
- Not ordinary clothing or simple spacesuit.
- Ordinary Antisapiens nearby do not require frames.

### Negative Prompt
```
--no transparent bubble helmet, astronaut suit, robot person, magical force field, antimatter explosion, exposed alien touching people, fantasy exoskeleton, sleek superhero armor
```

### Caption
**A Contact Frame is a treaty with physics.**

### Consistency References
- `docs/cosmology/conjugate-contact-frames.md`
- REF-E for Hydropolis.
- REF-F for nearby Antisapiens.
- Establish **REF-G**.

---

# SECTION IV — THE MOUNTAIN THAT REFUSED

## Spread 22 — Pages 43–44
# Blackstep

**Canon Status:** Main canon.

### Midjourney-Ready Prompt
```
wet-season documentary landscape of the Blackstep Province surrounding the Anticlinal Craton, black volcanic terraces and columnar basalt rising from dark water as controlled reef-like approaches, narrow docking channels, hidden shoals, wave wash over stepped lava benches, the distant geode mass of the Craton beyond, a few small work boats or cargo craft waiting outside permitted landing points, severe sacred border rather than open harbor, mineral storm haze, medium-format photography --ar 2:1 --s 80
```

### Aspect Ratio
`2:1`.

### Camera / Lens
6x7, 90mm lens from approaching vessel / high basalt terrace.

### Lighting
Wet gray daylight; black basalt; sparse amber dock practicals.

### Canon Constraints
- Blackstep becomes Craton wet-season threshold / docking system.
- Craton controls true docks.
- No easy beaches.
- Do not make it World Works-controlled.

### Negative Prompt
```
--no tropical beach, marina, resort harbor, lighthouse postcard, fantasy castle port, clean shipping terminal, giant naval fleet
```

### Caption
**The water rises. Refusal changes shape.**

### Consistency References
- `docs/locations/blackstep-province.md`
- Leads into REF-H.

---

## Spread 23 — Pages 45–46
# The Eastern Borer Gate

**Canon Status:** Main canon concept + sandbox visual-development treatment.

### Midjourney-Ready Prompt
```
colossal abandoned World Works tunnel-boring machine embedded permanently in the exposed crystal wall of the Anticlinal Craton, circular cutter head transformed into a sovereign Aeonolacertian gate, ancient industrial teeth and bolt rings still visible beneath brass repairs, copper pressure pipes, scaffold terraces, guard platforms, route lights, cultural banners and pressure-engineering ornament, cold dry mineral flats and diesel cargo rigs outside, humid green-gold mist and wet quartz visible through the gate inside, tiny saurian guards and visitors for scale, documentary architectural photograph, the machine has been defeated and culturally reclaimed --ar 2:1 --s 75
```

### Aspect Ratio
`2:1`.

### Camera / Lens
6x7 medium format, 50mm lens, broad frontal three-quarter threshold view.

### Lighting
Cold exterior side light; warm humid interior glow, both practical / environmental.

### Canon Constraints
- Aeonolacertians control the gate.
- World Works breached; did not successfully own the Craton.
- Aeonolacertian additions must look culturally mature and engineered.
- Do not use Red Umbrielor / MITE II unless explicitly required.
- No portal mechanics.

### Negative Prompt
```
--no active drill boring, fantasy gate, castle doors, glowing portal, stargate, clean mining facility, human soldiers controlling entrance, dinosaur theme park
```

### Caption
**World Works made the hole. The Craton kept the threshold.**

### Consistency References
- `docs/locations/anticlinal-craton.md`
- `docs/visual-development/anticlinal-craton-visual-descriptions.md`
- Establish **REF-H**.

---

## Spread 24 — Pages 47–48
# First Breath Inside

**Canon Status:** Craton canon foundation + visual-development treatment.

### Midjourney-Ready Prompt
```
view from inside the dark rusted mouth of an old borer tunnel looking into the Anticlinal Craton interior, foreground cold industrial iron, mineral dust, condensation and Aeonolacertian brass repairs framing the image, beyond it a vast humid geode world of wet quartz facets, tropical green vegetation, pressure-fed springs, mist columns, copper and brass walkways, civic terraces and distant saurian inhabitants, warm vapor gold and jade shadow replacing the cold exterior palette, beautiful but politically sovereign and physically dangerous, expedition photography --ar 2:1 --s 85
```

### Aspect Ratio
`2:1`.

### Camera / Lens
6x7, 45mm lens, camera placed just inside tunnel shade.

### Lighting
Dark cold foreground, luminous humid interior. No magical volumetric god rays.

### Canon Constraints
- Craton = re-rooted Aeonolacertian homeland on Meridian Prime.
- Warm, wet interior contrasts cold pressure-world exterior.
- Not paradise; not lost-world fantasy.
- Do not explain Stone Heart / Core / Dry Port.

### Negative Prompt
```
--no fantasy jungle cave, dinosaurs wandering wild, elves, glowing portal, paradise resort, ancient temple ruin, smooth sci-fi city, human colony
```

### Caption
**The cold world ends at an old wound. A hotter one begins beyond it.**

### Consistency References
- `docs/visual-development/anticlinal-craton-visual-descriptions.md`
- **REF-H**.

---

## Spread 25 — Pages 49–50
# A City Is a Body

**Canon Status:** Canon technology / Aeonolacertian visual system.

### Midjourney-Ready Prompt
```
candid documentary photograph inside an everyday Aeonolacertian civic district within the Craton, massive exposed radiator coils and pressure pipes maintaining warm humid air, fully saurian upright tool-using citizens of multiple morph types moving through ordinary life: engineers, elders, workers, children, traders, all with tails and nonhuman saurian faces, four-fingered clawed hands and four-toed clawed feet, culturally specific workwear and civic garments, brass copper steam-dark bronze and wet stone, no one posing as a warrior, sophisticated technology hidden inside pressure-era forms, lived-in public space --ar 2:1 --s 55
```

### Aspect Ratio
`2:1`.

### Camera / Lens
35mm reportage, 35mm lens, eye level adjusted to mixed body heights.

### Lighting
Warm 10-K’al civic heat feel: amber pressure light, steam diffusion, wet highlights.

### Canon Constraints
- Aeonolacertians are fully saurian people, not humans with scales.
- Universal tails.
- Four-fingered clawed hands; four-toed clawed feet.
- Multiple saurian morph types can coexist.
- Advanced technology appears brass / pressure / analog rather than crude.
- Civilian scene, not military tableau.

### Negative Prompt
```
--no human faces with scales, lizard masks, fantasy lizardfolk, dinosaur monsters, medieval armor, warrior lineup, cavemen, theme park, generic steampunk cosplay
```

### Caption
**A city is a body. A boiler is a heart. A corridor is a vein.**

### Consistency References
- `docs/species-guide.md`
- `docs/technology.md`
- `docs/visual-development/visual-style-guide.md`
- Establish **REF-I**.

---

## Spread 26 — Pages 51–52
# Red Glass Geodeum

**Canon Status:** Owner-approved Geodeum canon + visual development.

### Midjourney-Ready Prompt
```
wide documentary photograph inside a hematoid-quartz Craton Geodeum, enormous red-glass mineral bowl with seating carved into crystal shelves, smoky orange and blood-black quartz, brass safety rails, pressure vents, old ceremonial channels and modern staging infrastructure, mixed Aeonolacertian crowd with a few Meridian visitors, physically piloted industrial combat machines or modified construction rigs waiting at arena edge without fighting yet, atmosphere of trial, spectacle and political consequence rather than sports entertainment, dark red ambient mineral glow with practical arena lamps --ar 2:1 --s 75
```

### Aspect Ratio
`2:1`.

### Camera / Lens
6x7, 50mm lens from upper seating tier.

### Lighting
Red mineral bounce, smoky amber practicals, deep black recesses.

### Canon Constraints
- Geodeum is public contest / judgment architecture.
- Not merely a crystal cave or sports arena.
- Machines physically piloted / embodied danger.
- Nonhuman spatial design must accommodate saurian bodies and tails.
- Do not define complete Craton law.

### Negative Prompt
```
--no Roman colosseum copy, fantasy gladiators, robot battle TV show, remote drones, laser arena, clean esports stadium, human-majority crowd
```

### Caption
**A Geodeum is where conflict stops being private and becomes stone.**

### Consistency References
- `docs/worldbuilding/craton/craton-geodeums.md`
- `docs/visual-development/anticlinal-craton-visual-descriptions.md`
- REF-H and REF-I.

---

## Spread 27 — Pages 53–54
# The Stone Heart

**Canon Status:** Protected mystery.

### Midjourney-Ready Prompt
```
extreme long-distance documentary photograph deep within the Anticlinal Craton, humid swamp or pressure-fed wetland in foreground, tiny narrow boats and saurian figures barely visible for scale, beyond heavy mist a mountain-sized ambiguous form known only as the Stone Heart / Thunder Egg, partly obscured by vegetation and geode vapor, shape suggestive of immense geology but impossible to classify, no visible doorway, no machinery explanation, no glowing core, visual emphasis on distance, reverence and uncertainty, long-lens expedition photography --ar 2:1 --s 110
```

### Aspect Ratio
`2:1`.

### Camera / Lens
400mm-equivalent telephoto compression from very far away.

### Lighting
Humid diffuse interior light, faint mineral red / gold traces, no spotlight.

### Canon Constraints
- Do not solve what the Stone Heart is.
- Do not show it as gateway, battery, machine, egg literally hatching, or Core device.
- Scale should be undeniable; function should be unknowable.

### Negative Prompt
```
--no portal, giant mechanical heart, reactor, doorway, spaceship, monster egg, glowing energy core, temple entrance, explanatory diagram
```

### Caption
**Some landmarks become smaller when explained. This one has not been explained.**

### Consistency References
- `docs/locations/anticlinal-craton.md`
- `docs/visual-development/anticlinal-craton-visual-descriptions.md`
- REF-H for Craton atmosphere.

---

# SECTION V — MAPS THAT DISAGREE

## Spread 28 — Pages 55–56
# Eschar, Dry

**Canon Status:** Main canon.

### Midjourney-Ready Prompt
```
dry-season environmental photograph of the Eschar Slough appearing almost dead: black scabland crust, salt-white channel beds, flood-scoured stone ribs, hydrocrystal reef forms stranded above ground, cracked basin flats, hidden cuts and sink pockets, almost no visible settlement, one suspicious distant track line hinting that people use this supposedly useless territory, hard mineral air and black-glass fragments, medium-format survey photography --ar 2:1 --s 75
```

### Aspect Ratio
`2:1`.

### Camera / Lens
6x7, 65mm lens, high ground but not aerial.

### Lighting
Dry hard daylight with deep black scabland shadows.

### Canon Constraints
- Eschar Slough = dry-season scabland / Free Scab homeland system.
- Do not reveal exact Scab Cathedral position.
- Territory should seem low-value / hostile to outsiders.

### Negative Prompt
```
--no Sahara dunes, volcanic lava flow, visible pirate city, fantasy wasteland, skull decorations, Mad Max convoy, tropical swamp
```

### Caption
**Official maps call it bad ground. Bad ground is where other people learn to live.**

### Consistency References
- `docs/locations/eschar-slough.md`

---

## Spread 29 — Pages 57–58
# Eschar, Wet

**Canon Status:** Main canon.

### Midjourney-Ready Prompt
```
wet-season documentary landscape of the same Eschar Slough geography transformed into a hostile island-and-channel system, black stone ribs now islands, dark water filling former dry channels, black-glass shoals and hydrocrystal reefs under the surface, small concealed Free Scab boats or cargo craft slipping through difficult passages, false beacon lights distant in storm haze, no obvious grand pirate fortress, seasonal geography itself providing concealment, medium-format maritime expedition photograph --ar 2:1 --s 80
```

### Aspect Ratio
`2:1`.

### Camera / Lens
6x7, 90mm lens from low vessel deck.

### Lighting
Stormy wet gray / blue-black with sparse false-beacon red or amber points.

### Canon Constraints
- Wet season = pirate archipelago / channel system.
- Same geography as Spread 28.
- Scab Cathedral remains hidden / unresolved.
- Free Scabs are not cartoon pirates.

### Negative Prompt
```
--no pirate galleons, skull flags, Caribbean islands, tropical palms, huge fortress reveal, fantasy ships, neon cyberpunk harbor
```

### Caption
**In wet season, the bandit country learns to float.**

### Consistency References
- `docs/locations/eschar-slough.md`
- Match landmarks from Spread 28 if possible.

---

## Spread 30 — Pages 59–60
# Every Map Is an Argument

**Canon Status:** Main canon principle.

### Midjourney-Ready Prompt
```
overhead documentary still life on a scratched field table, four physically different Meridian Prime maps of roughly the same region laid partly over one another: a clean bureaucratic Prime Ops route chart, a grease-pencil corrected Traverse / NCI field map, a black-glass and signal-layer Hydropolis chart, and a partial Craton map tradition represented through restricted mineral tokens and pressure marks, coffee mug, gloves, compass-like instruments and damp corners, maps visibly disagree through route lines and hazard symbols but no readable generated paragraphs, tactile archival realism, available work light --ar 2:1 --s 45
```

### Aspect Ratio
`2:1`.

### Camera / Lens
Top-down 35mm / medium-format still-life, 50mm equivalent.

### Lighting
Single warm work lamp with cool ambient edge light.

### Canon Constraints
- Maps are political, seasonal, ecological, incomplete.
- Do not make one map obviously “correct.”
- Do not label protected mysteries.
- Final real typography / legend added later in layout.

### Negative Prompt
```
--no readable fake paragraphs, treasure map, fantasy parchment, GPS tablet only, holographic globe, magical runes, perfect clean cartography
```

### Caption
**A map on Meridian Prime is not a picture of land. It is an argument about what can still be survived.**

### Consistency References
- `docs/cartography/seasonal-map-logic.md`
- `docs/cartography/planetary-route-topology.md`

---

## Spread 31 — Pages 61–62
# Things That Move the Map

**Canon Status:** Sandbox candidate-canon ecology.

### Midjourney-Ready Prompt
```
long-lens wildlife photograph on Meridian Prime highlands, a herd of Glassback Mammoths crossing a crystalline route, massive shaggy low-slung herbivores with translucent mineral plates along spine and shoulders, plates catching cold light without glowing magically, herd weight fracturing brittle crystal crust, a tiny stopped tracked convoy far behind waiting for the animals to clear the route, windblown mineral dust and cold ridge atmosphere, serious natural-history photography, plausible anatomy and herd behavior --ar 2:1 --s 70
```

### Aspect Ratio
`2:1`.

### Camera / Lens
400mm wildlife telephoto from safe distance.

### Lighting
Cold side-light through blowing dust; mineral plates translucent only at edges.

### Canon Constraints
- **Candidate canon only.**
- Do not present as settled canon without later promotion.
- Animals are road hazards / ecological actors, not fantasy mounts.
- No riders.

### Negative Prompt
```
--no elephant copy, mammoth tusk cliché, glowing crystal monster, riders, battle, fantasy beast armor, dinosaur, cute baby focus, safari vehicle
```

### Caption
**Some hazards move because they are alive. Some animals matter because they move the hazard.**

### Consistency References
- `docs/worldbuilding/ecology/meridian-prime-megafauna.md`
- `docs/cartography/seasonal-map-logic.md`
- Production tag: **CANDIDATE CANON / DO NOT SILENTLY PROMOTE**.

---

## Spread 32 — Pages 63–64
# Things That Digest It

**Canon Status:** Sandbox development ecology.

### Midjourney-Ready Prompt
```
macro-to-medium documentary photograph of abandoned Meridian Prime route infrastructure being consumed from below by Glassrot-like fungal veins, pale milky mycelial threads visible through cracked crystal and corroded metal, old route marker leaning as subsurface material fails, faint wet mineral textures and small fruiting structures, no grotesque body horror, fungus feels ecological and structurally dangerous rather than magical, realistic field-science photography with shallow depth transitioning to broken roadway behind --ar 2:1 --s 65
```

### Aspect Ratio
`2:1`.

### Camera / Lens
100mm macro / short telephoto, low ground level.

### Lighting
Overcast cool daylight, subtle bounced work lamp if needed.

### Canon Constraints
- **Development ecology only.**
- Fungi should indicate decay, route failure, and hidden feeding processes.
- Do not imply all fungi behave this way.
- No protected mystery explanation.

### Negative Prompt
```
--no glowing fantasy mushrooms, giant toadstools, zombie infection, gore, alien eggs, psychedelic rainbow, magical spores
```

### Caption
**Fungi mark where the map has begun to digest itself.**

### Consistency References
- `docs/worldbuilding/ecology/meridian-prime-megafungi.md`
- `docs/cartography/seasonal-map-logic.md`
- Production tag: **DEVELOPMENT APOCRYPHA**.

---

# SECTION VI — ON TRAVERSE

## Spread 33 — Pages 65–66
# MITE II

**Canon Status:** Planning canon.

### Midjourney-Ready Prompt
```
very wide documentary expedition photograph of the complete MITE II working convoy crossing immense crystalline terrain, 409 visibly far ahead as the compact sensor groomer with forward GPR boom and no trailer, 289 Red Umbrielor behind as the heavy command / life-support tractor pulling its own connected red Mod train and black fuel tail, 287 Discovery as a separate used crawler repair tractor pulling the second Mod train, clear spacing between machine roles, no train tracks, machines tiny against the landscape, cold haze and route flags, procedural movement rather than heroic charge --ar 2:1 --s 55
```

### Aspect Ratio
`2:1`.

### Camera / Lens
6x7, 180mm telephoto from distant ridge to compress full convoy relationship.

### Lighting
Cold morning; amber headlights; red machines subdued by distance.

### Canon Constraints
- 409 leads and pulls nothing.
- Red Umbrielor does not pull whole convoy.
- Discovery is separate repair / storage spine.
- Two Mod trains.
- Black fuel bladders.
- Crawler convoy, never railroad train.

### Negative Prompt
```
--no locomotive, rails, one giant tractor towing everything, military convoy, tanks, wheeled semi trucks, Mad Max, futuristic hover vehicles
```

### Caption
**409 reads the route. Red Umbrielor commands the work. Discovery keeps it alive.**

### Consistency References
- REF-B, REF-C, REF-D mandatory.
- `docs/equipment/mite-ii-convoy-structure.md`
- `docs/comics/mite-ii-convoy-structure-review.md`

---

## Spread 34 — Pages 67–68
# Set the Tap

**Canon Status:** MITE II production logic.

### Midjourney-Ready Prompt
```
night documentary photograph inside Traverse Town, Aquifer Drill operating from the kitchen-side / tongue area of the Comms-Kitchen Mod, bundled crew handling hoses and checking water infrastructure, steam and condensation rising into blue-black cold, two parallel Mod rows implied beyond, module-mounted work lights only, scratched red container surfaces, tracked platforms, tools wet with melt and mineral water, intimate field survival rather than futuristic technology demonstration, 35mm reportage --ar 2:1 --s 50
```

### Aspect Ratio
`2:1`.

### Camera / Lens
35mm, 35mm lens, close working distance with partial foreground machinery.

### Lighting
Dirty amber Mod lamps, cold blue darkness, small red equipment indicators.

### Canon Constraints
- Aquifer Drill attached / integrated at Comms-Kitchen Mod.
- Field phrase: “Set the tap.”
- No freestanding decorative light towers.
- Traverse Town geometry remains coherent.

### Negative Prompt
```
--no drilling rig tower, oil derrick, tent camp, floodlight stadium, sci-fi water replicator, clean laboratory, miners posing
```

### Caption
**Set the tap. Water first, philosophy later.**

### Consistency References
- `docs/comics/traverse-town-layout-guide.md`
- REF-D.

---

## Spread 35 — Pages 69–70
# End of Shift

**Canon Status:** Canon-consistent invented documentary scene.

### Midjourney-Ready Prompt
```
quiet interior still-life photograph inside a working Meridian Prime Traverse module after shift, wet insulated gloves hanging near a heater, scratched metal mugs, grease-pencil route notes and folded maps, condensation running down a small window, heavy boots drying under a bench, patched cables, old fasteners, one empty seat, dirty amber heater glow surrounded by deep blue-black shadow, no people, evidence of exhaustion through objects only, intimate 35mm documentary realism, fine grain --ar 2:1 --s 45
```

### Aspect Ratio
`2:1`.

### Camera / Lens
35mm, 50mm lens, waist-height still-life framing.

### Lighting
Only practical heater / work light and weak blue window light.

### Canon Constraints
- Human surface / Traverse technology is used, patched, practical.
- Avoid specific character relics unless approved.
- Do not accidentally imply Rob / Tenet protected story beats.

### Negative Prompt
```
--no cozy cabin, luxury RV, futuristic spaceship interior, rustic Earth camping, visible person, romantic candlelight, readable long text
```

### Caption
**The glamorous part of a Traverse is mostly drying things before they freeze.**

### Consistency References
- `docs/visual-development/visual-style-guide.md`
- REF-D for materials and palette.

---

## Spread 36 — Pages 71–72
# The Road Is Lying

**Canon Status:** Seasonal canon / visual-development synthesis.

### Midjourney-Ready Prompt
```
documentary field photograph from inside or immediately beside a Traverse during a Meridian Prime haboon, near-zero visibility in mineral dust and moisture, route flags disappearing into particulate darkness, one tracked tractor reduced to a black silhouette with dirty amber headlights, tiny red marker lamps suspended in the haze, ground and sky nearly indistinguishable, no monster visible, danger comes from losing the route itself, restrained shutter blur from airborne grit, oppressive blue-black and rust-gray palette --ar 2:1 --s 90
```

### Aspect Ratio
`2:1`.

### Camera / Lens
35mm, 50mm lens, protected handheld position.

### Lighting
Headlights diffused in storm; red markers; no ambient spectacle.

### Canon Constraints
- Haboon season can create low visibility / route danger.
- No protected mystery needs to be revealed.
- Machines should remain tracked industrial equipment.

### Negative Prompt
```
--no tornado, lightning storm spectacle, monster silhouette, sandworm, laser lights, orange Mars dust only, military battle, train
```

### Caption
**Every crew eventually reaches the moment when the map, the instruments, and the road disagree.**

### Consistency References
- `docs/cartography/seasonal-map-logic.md`
- `production/reels/meridian-prime-reel-01/visual-language.md`
- REF-A / REF-D.

---

# SECTION VII — THINGS THE ROAD SAYS HAPPENED

## Spread 37 — Pages 73–74
# W.A.S.

**Canon Status:** SANDBOX / NON-CANON UNTIL PROMOTED.

### Midjourney-Ready Prompt
```
recovered expedition archive contact-sheet aesthetic from an old Meridian Prime Traverse incident, several imperfect frames presented as photographed physical prints on a dark evidence table: an earlier heavy tracked W.A.S. convoy in cold route terrain, a damaged group image of a competent mixed expedition crew before disaster, a distant red relay beacon, one frame partially fogged or chemically damaged, industrial survival gear and old route equipment, no monster reveal, analog archive degradation, scratches, exposure variation, ominous but procedural, leave all text and file numbers blank for later layout --ar 2:1 --s 55
```

### Aspect Ratio
`2:1`.

### Camera / Lens
Generated as archival-object still life containing mixed 35mm expedition frames.

### Lighting
Single evidence-table lamp; cold reflected image tones.

### Canon Constraints
- W.A.S. = World Aperture Survey Traverse in sandbox development.
- This image must visually announce uncertainty / archival distance.
- Do not present W.A.S. as confirmed main-canon history.
- Do not bake readable official claims into the image.
- Do not reveal transformations yet.

### Negative Prompt
```
--no confirmed government seal, readable report text, monster lineup, gore, fantasy expedition, modern smartphone, clean digital collage, heroic team poster
```

### Caption
**Recovered file fragment. Provenance unresolved.**

### Consistency References
- `docs/comics/was-case-traverse-naming-lock.md`
- `docs/comics/was-traverse-comic-pitch.md`
- `docs/comics/was-traverse-issue-01-art-direction-bible.md`
- Establish **REF-J**.

---

## Spread 38 — Pages 75–76
# The Cairn Hound

**Canon Status:** SANDBOX / NON-CANON UNTIL PROMOTED.

### Midjourney-Ready Prompt
```
distant telephoto evidence photograph on a high snowy Meridian Prime ridge, the Cairn Hound standing beside a rebuilt route cairn and looking away from camera, tall gaunt intelligent mountain-dog humanoid silhouette with real canine face rather than human face, long ears and sharp muzzle, tattered modern technical mountaineering shell, expedition trousers, old climbing harness, rope and carabiners, smoky blue-white and occasional redglass crystal growth emerging through shoulders and gear, frightening but calm, tiny against immense mountains, imperfect atmospheric focus as if photographed unexpectedly from far away --ar 2:1 --s 60
```

### Aspect Ratio
`2:1`.

### Camera / Lens
600mm-equivalent telephoto, slightly underexposed, atmospheric compression.

### Lighting
Flat high-altitude overcast, reflective eyes only if plausible at angle.

### Canon Constraints
- Sparky / Cairn Hound is sandbox cryptid development only.
- Canine face, not generic werewolf.
- Mountaineering gear remains visible.
- Crystal growth is body transformation, not armor.
- Solitary, wary, not attack pose.

### Negative Prompt
```
--no werewolf attack, human woman face, fantasy wolf warrior, gore, snarling monster closeup, bodybuilder, medieval armor, pet dog, cute mascot
```

### Caption
**Field name: Cairn Hound. Identification disputed. Do not follow the howl uphill.**

### Consistency References
- `docs/cryptids/007-the-cairn-hound-sparky.md`
- **REF-J** for evidence treatment.
- Production tag: **APOCRYPHAL / NOT MAIN CANON**.

---

## Spread 39 — Pages 77–78
# Do Not Follow the Light

**Canon Status:** SANDBOX / NON-CANON UNTIL PROMOTED.

### Midjourney-Ready Prompt
```
extremely sparse night evidence photograph on an abandoned Meridian Prime route, broken relay mast leaning over pale blue fog, one red beacon still blinking though no active station should remain, black sky occupying most of frame, a tiny distant ambiguous upright silhouette near infrastructure that could be Rookmask Jack or could be damaged equipment, no readable face, no clear monster confirmation, old route flags pointing in contradictory directions, long telephoto grain, underexposed blacks, archival unease rather than horror poster --ar 2:1 --s 75
```

### Aspect Ratio
`2:1`.

### Camera / Lens
300–400mm telephoto, handheld / braced, slight focus uncertainty.

### Lighting
Red relay beacon, pale blue fog, minimal dirty amber from distant equipment.

### Canon Constraints
- Keep identity unresolved.
- If silhouette implies Rookmask Jack, use black-alloy / bird-beak-mask language only subtly.
- No definite transformation proof.
- W.A.S. section remains apocryphal.
- Do not introduce C.A.S.E. unless later editorially chosen.

### Negative Prompt
```
--no monster closeup, glowing red eyes filling frame, plague doctor portrait, horror movie poster, gore, attack, readable warning sign, supernatural ghost glow
```

### Caption
**The field rule is older than the file: do not follow a light that has no reason to be working.**

### Consistency References
- `docs/comics/was-traverse-issue-01-art-direction-bible.md`
- `docs/cryptids/001-rookmask-jack-infrastructure-body-revision.md`
- **REF-J**.

---

# SECTION VIII — CONTINUITY

## Spread 40 — Pages 79–80
# Control Over Continuity

**Canon Status:** Main canon.

### Midjourney-Ready Prompt
```
quiet final documentary double-spread on Meridian Prime at night, a small isolated sanctuary or route settlement in the lower third, several exhausted travelers resting near practical shelter lights without posing, machines dark and cooling nearby, black mineral landscape fading into cobalt distance, above everything the Lodestar crosses the sky as the same distant enormous artificial star-vessel seen earlier, repeated red navigation lights unmistakable, no crisis, no explanation, calm image made uneasy by context, fine natural grain and deep blacks, visual echo of the opening spreads --ar 2:1 --s 70
```

### Aspect Ratio
`2:1`.

### Camera / Lens
6x7 or high-quality 35mm, 50mm lens, low horizon echoing Spread 03.

### Lighting
Tiny warm sanctuary practicals, cold sky, Lodestar red lights.

### Canon Constraints
- Return to indisputable main canon after W.A.S. sequence.
- Lodestar remains active and unchanged.
- Sanctuary should be generic unless later tied to a canon location.
- Do not imply the resting figures know the truths suggested by the book.
- No closing explosion / revelation.

### Negative Prompt
```
--no spaceship attack, beam, crash, giant logo, triumphant hero silhouettes, sunrise, fantasy stars, city skyline, monster, readable text
```

### Caption
**Control over Continuity.**

### Consistency References
- `docs/meridian-prime-bible.md`
- REF-A.
- Match Lodestar design / scale from Spread 03.
- Echo composition from Spread 01 and Spread 03.

---

# Generation Order

Do **not** generate the book strictly page-by-page. Establish anchors first.

Recommended order:

1. Spread 01 — global cold-world grade
2. Spread 07 — Red Umbrielor
3. Spread 08 — 409
4. Spread 09 — Traverse Town
5. Spread 18 — Hydropolis
6. Spread 20 — Antisapien portrait
7. Spread 21 — Contact Frame
8. Spread 23 — Craton gate
9. Spread 25 — Aeonolacertian civilian anatomy
10. Spread 37 — W.A.S. archive treatment

After those ten are approved, use them as consistency references for the remaining thirty.

## Sequence B — Expand Each World

Then generate:

- 02, 03, 04, 05, 06
- 10 through 17
- 19
- 22, 24, 26, 27
- 28 through 36
- 38, 39, 40

This keeps visual drift from multiplying before the major recurring systems are locked.

---

# Production Tracking Fields

For each spread, record:

- Generation date
- Prompt version
- Midjourney job ID
- Seed if useful
- Approved / revise / reject
- Style Reference(s) used
- Image Reference(s) used
- Canon review status
- Continuity issues
- Selected upscale filename
- Final crop filename
- Caption status
- Layout status

Suggested selected-file naming:

`MP_CTB_S01_before-the-map_v01.png`  
`MP_CTB_S07_red-umbrielor_v01.png`  
`MP_CTB_S18_hydropolis-wet_v01.png`

---

# Final Production Principle

The image set should not feel like forty commissions from forty different science-fiction portfolios.

It should feel like one photographer kept going.

The photographer changes lenses.

The weather changes.

The political jurisdiction changes.

The evidence quality changes.

The world does not stop being Meridian Prime.
