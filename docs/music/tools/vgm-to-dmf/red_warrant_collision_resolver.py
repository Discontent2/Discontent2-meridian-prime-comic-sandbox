#!/usr/bin/env python3
"""Role-aware collision reducer for Red Warrant VGM-to-DMF pipeline.

Input:  <prefix>_quantized_grid.json from red_warrant_grid_quantizer.py
Output: <prefix>_resolved_grid.json plus dropped-event and markdown reports.

This compact repo copy mirrors the working artifact behavior: keep one note per
channel/row, score collisions by inferred channel role, and preserve pitch events
mostly for lead/harmony/arpeggio lanes.
"""
from __future__ import annotations

import argparse, csv, json, math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

CHANNELS = ["FM1", "FM2", "FM3", "FM4", "FM5", "FM6"]
DEFAULT_ROLES = {
    "FM1": "bass / low pedal",
    "FM2": "rhythm / rapid pulse",
    "FM3": "rhythm / rapid pulse",
    "FM4": "expressive lead / melody",
    "FM5": "percussion / hat-noise / auxiliary",
    "FM6": "percussion / hat-noise / auxiliary",
}

def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))

def fnum(x: Any, default: float = 0.0) -> float:
    try:
        if x in ("", None): return default
        return float(x)
    except Exception:
        return default

def note_midi(ev: Dict[str, Any]) -> Optional[int]:
    m = ev.get("midi_note")
    if m in ("", None): return None
    try: return int(round(float(m)))
    except Exception: return None

def duration_rows(ev: Dict[str, Any]) -> int:
    try: return max(1, int(ev.get("end_row", ev.get("start_row", 0))) - int(ev.get("start_row", 0)))
    except Exception: return 1

def classify(role: str) -> str:
    r = (role or "").lower()
    if "bass" in r or "low pedal" in r: return "bass"
    if "lead" in r or "melody" in r or "bend" in r: return "lead"
    if "percussion" in r or "hat" in r or "noise" in r or "drum" in r: return "percussion"
    if "arpeggio" in r: return "arpeggio"
    if "rhythm" in r or "pulse" in r: return "rhythm"
    if "sustain" in r or "harmony" in r: return "harmony"
    return "unknown"

def load_roles(path: Optional[Path]) -> Dict[str, str]:
    roles = dict(DEFAULT_ROLES)
    if not path or not path.exists(): return roles
    data = load_json(path)
    for ch in data.get("channels", []):
        if ch.get("channel") in roles and ch.get("role"):
            roles[ch["channel"]] = ch["role"]
    for name, role in data.get("channel_roles", {}).items():
        if name in roles: roles[name] = str(role)
    return roles

def score_note(ev: Dict[str, Any], role_kind: str) -> Tuple[float, List[str]]:
    m, vel, dur = note_midi(ev), fnum(ev.get("velocity"), 96), duration_rows(ev)
    err, src = abs(fnum(ev.get("row_error_seconds"), 0.0)), fnum(ev.get("source_index"), 0.0)
    score, reasons = 0.0, []
    grid = max(0.0, 1.0 - err * 100.0); score += grid; reasons.append(f"grid={grid:.3f}")
    vs = min(1.5, max(0.0, vel / 127.0 * 1.5)); score += vs; reasons.append(f"vel={vs:.3f}")
    if role_kind == "bass":
        if m is not None:
            low = min(3.5, max(0.0, (72 - m) / 24.0)); score += low; reasons.append(f"low={low:.3f}")
            if m <= 48: score += 1.0; reasons.append("bass_register=1")
        score += min(1.0, dur / 8.0)
    elif role_kind == "lead":
        if m is not None and 48 <= m <= 84: score += 1.5; reasons.append("lead_register=1.5")
        if m is not None and 60 <= m <= 78: score += 0.8; reasons.append("lead_sweet=0.8")
        score += min(1.5, dur / 6.0)
        if ev.get("instrument_group_id"): score += 0.4
    elif role_kind == "percussion":
        short = max(0.0, 1.5 - dur * 0.25); score += short; reasons.append(f"short={short:.3f}")
        if m is not None and m >= 60: score += 0.8
    elif role_kind == "rhythm":
        if m is not None and 36 <= m <= 72: score += 1.2
        score += max(0.0, 1.0 - abs(dur - 1) * 0.2)
    elif role_kind == "arpeggio":
        if m is not None: score += min(2.0, max(0.0, (m - 48) / 24.0))
        score += max(0.0, 1.0 - abs(dur - 1) * 0.25)
    elif role_kind == "harmony":
        score += min(2.0, dur / 8.0)
        if m is not None and 40 <= m <= 76: score += 0.8
    else:
        score += max(0.0, 1.0 - src * 0.0001)
    score += max(0.0, 0.1 - src * 0.000001)
    return score, reasons

def pick(events: List[Dict[str, Any]], role_kind: str) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    scored = [(score_note(e, role_kind), e) for e in events]
    scored.sort(key=lambda x: (-x[0][0], fnum(x[1].get("source_index")), x[1].get("event_index", 0)))
    win = dict(scored[0][1]); win["_resolver_score"] = round(scored[0][0][0], 6); win["_resolver_reasons"] = scored[0][0][1]
    drop = []
    for (score, reasons), ev in scored[1:]:
        d = dict(ev); d["_resolver_score"] = round(score, 6); d["_resolver_reasons"] = reasons
        d["_dropped_reason"] = f"lost_same_row_collision_to_event_{win.get('event_index')}"; drop.append(d)
    return win, drop

def resolve(q: Dict[str, Any], roles: Dict[str, str]) -> Dict[str, Any]:
    notes = [e for e in q.get("events", []) if e.get("kind") == "note"]
    pitches = [e for e in q.get("events", []) if e.get("kind") == "pitch"]
    buckets = defaultdict(list)
    for e in notes: buckets[(int(e["channel"]), int(e["start_row"]))].append(e)
    kept, dropped, stats = [], [], defaultdict(Counter)
    for (ch, row), evs in buckets.items():
        name = evs[0].get("channel_name") or CHANNELS[ch]
        role_kind = classify(roles.get(name, DEFAULT_ROLES.get(name, "unknown")))
        stats[name]["input_notes"] += len(evs)
        if len(evs) == 1:
            w = dict(evs[0]); w["_resolver_reasons"] = ["no_collision"]; kept.append(w)
        else:
            w, d = pick(evs, role_kind); kept.append(w); dropped.extend(d); stats[name]["dropped_note_collisions"] += len(d)
        stats[name]["kept_notes"] += 1
    pitch_buckets = defaultdict(list)
    for e in pitches: pitch_buckets[(int(e["channel"]), int(e["start_row"]))].append(e)
    kept_pitch, dropped_pitch = [], []
    for (ch, row), evs in pitch_buckets.items():
        name, role_kind = CHANNELS[ch], classify(roles.get(CHANNELS[ch], DEFAULT_ROLES.get(CHANNELS[ch], "unknown")))
        stats[name]["input_pitch_events"] += len(evs)
        if role_kind not in ("lead", "harmony", "arpeggio"):
            for e in evs:
                d = dict(e); d["_dropped_reason"] = "pitch_removed_for_non_expressive_role"; dropped_pitch.append(d)
            stats[name]["dropped_pitch_events"] += len(evs); continue
        evs.sort(key=lambda e: (-abs(fnum(e.get("cents"))), abs(fnum(e.get("row_error_seconds"))), fnum(e.get("source_index"))))
        kept_pitch.append(dict(evs[0])); stats[name]["kept_pitch_events"] += 1
        for e in evs[1:]:
            d = dict(e); d["_dropped_reason"] = f"pitch_collision_lost_to_event_{evs[0].get('event_index')}"; dropped_pitch.append(d)
        stats[name]["dropped_pitch_events"] += max(0, len(evs)-1)
    out_events = kept + kept_pitch
    out_events.sort(key=lambda e: (int(e["channel"]), int(e["start_row"]), 0 if e.get("kind") == "note" else 1, e.get("source_index", 0)))
    for i, e in enumerate(out_events): e["resolved_event_index"] = i
    out = dict(q); out["format"] = "red_warrant_resolved_grid_v1"; out["source_format"] = q.get("format")
    out["events"] = out_events; out["dropped_events"] = dropped + dropped_pitch; out["roles"] = roles
    out["stats"] = dict(q.get("stats", {})); out["stats"]["resolver"] = {
        "input_events": len(notes)+len(pitches), "input_notes": len(notes), "input_pitch_events": len(pitches),
        "resolved_events": len(out_events), "kept_notes": len(kept), "kept_pitch_events": len(kept_pitch),
        "dropped_events": len(dropped)+len(dropped_pitch), "dropped_note_collisions": len(dropped),
        "dropped_pitch_events": len(dropped_pitch), "role_stats": {k: dict(v) for k, v in stats.items()}}
    return out

def write_outputs(result: Dict[str, Any], out_dir: Path, prefix: str) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"{prefix}_resolved_grid.json").write_text(json.dumps({k:v for k,v in result.items() if k != "dropped_events"}, indent=2), encoding="utf-8")
    (out_dir / f"{prefix}_resolved_dropped_events.json").write_text(json.dumps(result.get("dropped_events", []), indent=2), encoding="utf-8")
    st = result["stats"]["resolver"]
    lines = [f"# {prefix} Collision Resolver Report", "", f"- Input events: `{st['input_events']}`", f"- Resolved events: `{st['resolved_events']}`", f"- Dropped events: `{st['dropped_events']}`", "", "| Channel | Role | Input Notes | Kept Notes | Dropped Notes | Input Pitch | Kept Pitch | Dropped Pitch |", "|---|---|---:|---:|---:|---:|---:|---:|"]
    for ch in CHANNELS:
        rs = st.get("role_stats", {}).get(ch, {})
        lines.append(f"| {ch} | {result['roles'].get(ch, DEFAULT_ROLES[ch])} | {rs.get('input_notes',0)} | {rs.get('kept_notes',0)} | {rs.get('dropped_note_collisions',0)} | {rs.get('input_pitch_events',0)} | {rs.get('kept_pitch_events',0)} | {rs.get('dropped_pitch_events',0)} |")
    (out_dir / f"{prefix}_collision_resolver_report.md").write_text("\n".join(lines), encoding="utf-8")

def main() -> int:
    ap = argparse.ArgumentParser(description="Resolve quantized-grid collisions using channel-role heuristics.")
    ap.add_argument("quantized_grid", type=Path); ap.add_argument("--role-report", type=Path, default=None)
    ap.add_argument("--out-dir", type=Path, default=Path("red_warrant_resolved")); ap.add_argument("--prefix")
    args = ap.parse_args(); prefix = args.prefix or args.quantized_grid.stem.replace("_quantized_grid", "")
    result = resolve(load_json(args.quantized_grid), load_roles(args.role_report)); write_outputs(result, args.out_dir, prefix)
    st = result["stats"]["resolver"]
    print(f"Wrote {args.out_dir / (prefix + '_resolved_grid.json')}")
    print(f"Input events: {st['input_events']}"); print(f"Resolved events: {st['resolved_events']}"); print(f"Dropped events: {st['dropped_events']}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
