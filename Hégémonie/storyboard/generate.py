#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genere le storyboard du one-shot via fal.ai (Nano Banana 2 Edit).

Calque sur la convention maison IA_avatar/pipeline/generate_fal_kling_batch.py :
  - load_key() lit FAL_KEY dans l'env, sinon dans un .env connu
  - le cout estime est imprime en JSON AVANT tout appel
  - rien n'est depense sans --confirm-spend

Usage :
    python generate.py --scene 1                      # dry-run, n'appelle rien
    python generate.py --scene 1 --confirm-spend      # genere la scene 1
    python generate.py --all --confirm-spend          # genere les 10
    python generate.py --all --resolution 1k --confirm-spend
    python generate.py --scene 7 --seed 42 --confirm-spend   # re-roll d'un plan
"""

import argparse
import base64
import json
import mimetypes
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
HEGEMONIE = HERE.parent
INFORMATIQUE = HEGEMONIE.parents[1]          # .../Desktop/Informatique
OUT = HERE / "out"

sys.path.insert(0, str(HERE))
from prompts import (  # noqa: E402
    REFERENCE_FILES, SCENES, build_prompt, scene_by_id,
)

MODEL = "fal-ai/nano-banana-2/edit"

# fal : $0.08 / image en 1K, x1.5 en 2K, x2 en 4K
COST_PER_IMAGE_USD_1K = 0.08
RESOLUTION_MULTIPLIER = {"1k": 1.0, "2k": 1.5, "4k": 2.0}

# .env susceptibles de contenir la cle, dans l'ordre de recherche
ENV_CANDIDATES = [
    INFORMATIQUE / "COACH" / ".env",
    INFORMATIQUE / "IA_avatar" / ".env",
    HEGEMONIE / ".env",
]


def load_key() -> str:
    for name in ("FAL_KEY", "key_api_fal.ai"):
        value = os.environ.get(name)
        if value:
            return value.strip()
    for env_path in ENV_CANDIDATES:
        if not env_path.exists():
            continue
        for raw in env_path.read_text(encoding="utf-8", errors="ignore").splitlines():
            if "=" not in raw or raw.lstrip().startswith("#"):
                continue
            name, value = raw.split("=", 1)
            if name.strip() in {"FAL_KEY", "key_api_fal.ai"} and value.strip():
                return value.strip().strip('"').strip("'")
    raise SystemExit(
        "Cle fal.ai absente. Attendue dans $FAL_KEY ou dans :\n  "
        + "\n  ".join(str(p) for p in ENV_CANDIDATES)
    )


def data_uri(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "image/jpeg"
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode("ascii")


def reference_paths(scene: dict) -> list[Path]:
    paths = []
    for key in scene["refs"]:
        p = HEGEMONIE / REFERENCE_FILES[key]
        if not p.exists():
            raise SystemExit(f"Fiche de reference introuvable : {p}")
        paths.append(p)
    return paths


def estimate(scenes: list[dict], resolution: str) -> dict:
    unit = COST_PER_IMAGE_USD_1K * RESOLUTION_MULTIPLIER[resolution]
    return {
        "model": MODEL,
        "images": len(scenes),
        "resolution": resolution,
        "cost_per_image_usd": round(unit, 4),
        "estimated_total_usd": round(unit * len(scenes), 2),
        "scenes": [{"id": s["id"], "titre": s["titre"], "seed": s["seed"],
                    "refs": s["refs"]} for s in scenes],
        "output_dir": str(OUT),
    }


def log_run(entry: dict) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / "runs.jsonl").open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry, ensure_ascii=False) + "\n")


def generate_one(fal_client, scene: dict, resolution: str, seed: int | None) -> Path:
    refs = reference_paths(scene)
    prompt = build_prompt(scene)
    used_seed = seed if seed is not None else scene["seed"]

    args = {
        "prompt": prompt,
        "image_urls": [data_uri(p) for p in refs],
        "num_images": 1,
        "output_format": "png",
        "aspect_ratio": "16:9",
        "resolution": resolution.upper(),
        "seed": used_seed,
    }

    print(f"  -> appel fal ({len(refs)} references, seed {used_seed})...", flush=True)
    started = time.time()
    handle = fal_client.submit(MODEL, arguments=args)
    result = handle.get()

    images = result.get("images") or []
    if not images:
        raise SystemExit(f"Reponse fal sans image : {json.dumps(result)[:500]}")

    url = images[0].get("url")
    if not url:
        raise SystemExit(f"Image sans url : {json.dumps(images[0])[:300]}")

    OUT.mkdir(parents=True, exist_ok=True)
    dest = OUT / f"{scene['id']:02d}_{scene['slug']}.png"

    if url.startswith("data:"):
        dest.write_bytes(base64.b64decode(url.split(",", 1)[1]))
    else:
        import urllib.request
        with urllib.request.urlopen(url) as resp:
            dest.write_bytes(resp.read())

    elapsed = round(time.time() - started, 1)
    unit = COST_PER_IMAGE_USD_1K * RESOLUTION_MULTIPLIER[resolution]
    log_run({
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "scene_id": scene["id"], "titre": scene["titre"], "slug": scene["slug"],
        "model": MODEL, "resolution": resolution, "seed": used_seed,
        "refs": scene["refs"], "cost_usd": round(unit, 4),
        "seconds": elapsed, "output": str(dest.relative_to(HERE)),
    })
    print(f"  OK  {dest.name}  ({dest.stat().st_size // 1024} Ko, {elapsed}s)", flush=True)
    return dest


def main() -> int:
    ap = argparse.ArgumentParser(description="Storyboard « Le Service du soir »")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--scene", type=int, help="numero de scene (1-10)")
    g.add_argument("--scenes", help="plage ou liste, ex. 2-10 ou 3,5,7")
    g.add_argument("--all", action="store_true", help="les 10 scenes")
    ap.add_argument("--resolution", choices=list(RESOLUTION_MULTIPLIER), default="2k")
    ap.add_argument("--seed", type=int, default=None, help="surcharge le seed de la scene")
    ap.add_argument("--confirm-spend", action="store_true",
                    help="obligatoire pour depenser reellement")
    args = ap.parse_args()

    if args.all:
        scenes = SCENES
    elif args.scenes:
        wanted = []
        for chunk in args.scenes.split(","):
            chunk = chunk.strip()
            if "-" in chunk:
                a, b = chunk.split("-", 1)
                wanted.extend(range(int(a), int(b) + 1))
            elif chunk:
                wanted.append(int(chunk))
        scenes = [scene_by_id(i) for i in sorted(set(wanted))]
    else:
        scenes = [scene_by_id(args.scene)]
    plan = estimate(scenes, args.resolution)
    print(json.dumps(plan, ensure_ascii=False, indent=2), flush=True)

    if not args.confirm_spend:
        print("\n[dry-run] Rien n'a ete depense. "
              "Relance avec --confirm-spend pour generer.", flush=True)
        return 0

    os.environ["FAL_KEY"] = load_key()
    import fal_client  # noqa: E402  (apres avoir pose la cle)

    print(f"\nGeneration de {len(scenes)} image(s) en {args.resolution}...\n", flush=True)
    done = []
    for scene in scenes:
        print(f"[{scene['id']:02d}] {scene['titre']}", flush=True)
        done.append(generate_one(fal_client, scene, args.resolution, args.seed))

    unit = COST_PER_IMAGE_USD_1K * RESOLUTION_MULTIPLIER[args.resolution]
    print(f"\n{len(done)} image(s) dans {OUT}")
    print(f"Cout reel : ${round(unit * len(done), 2)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
