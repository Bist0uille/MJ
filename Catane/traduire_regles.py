"""Crée une version française de travail du livret fourni par l'utilisateur.

Le script conserve les fonds et illustrations, retire uniquement les objets texte
anglais, puis replace une traduction française dans les mêmes zones.
"""

from __future__ import annotations

import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "agot_base_rules_2018.pdf"
OUTPUT = ROOT / "Catan_Le_Trone_de_Fer_Regles_FR.pdf"
CACHE_FILE = ROOT / "traductions_cache.json"

FONT_REGULAR = r"C:\Windows\Fonts\arial.ttf"
FONT_BOLD = r"C:\Windows\Fonts\arialbd.ttf"


TERM_FIXES = {
    "la Confrérie de la Garde": "les Frères Jurés de la Garde",
    "La Confrérie de la Garde": "Les Frères Jurés de la Garde",
    "Brotherhood of the Watch": "Frères Jurés de la Garde",
    "le Cadeau": "le Don",
    "Le Cadeau": "Le Don",
    "les Crocs de Givre": "Crocgivre",
    "Les Crocs de Givre": "Crocgivre",
    "les Dents de Givre": "Crocgivre",
    "Les Dents de Givre": "Crocgivre",
    "gardiens": "gardes",
    "Gardiens": "Gardes",
    "colonies": "avant-postes",
    "Colonies": "Avant-postes",
    "colonie": "avant-poste",
    "Colonie": "Avant-poste",
    "donjons": "forteresses",
    "Donjons": "Forteresses",
    "donjon": "forteresse",
    "Donjon": "Forteresse",
    "barbares": "sauvageons",
    "Barbares": "Sauvageons",
    "barbare": "sauvageon",
    "Barbare": "Sauvageon",
    "voleur Tormund": "Tormund le Voleur",
    "Tormund le voleur": "Tormund le Voleur",
    "Frostfangs": "Crocgivre",
    "Frontfangs": "Crocgivre",
    "l'offre": "la réserve",
    "L'offre": "La réserve",
    "règlements": "avant-postes",
    "Règlements": "Avant-postes",
    "règlement": "avant-poste",
    "Règlement": "Avant-poste",
    "un garder": "une forteresse",
    "des sauvages": "des sauvageons",
    "les sauvages": "les sauvageons",
    "Les sauvages": "Les sauvageons",
}


def clean_source(text: str) -> str:
    text = text.replace("\U000f2002", "◆").replace("\u0001", "")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text).strip()
    # Certains titres possèdent une ombre qui est extraite comme un doublon.
    words = text.split()
    if len(words) >= 4 and len(words) % 2 == 0:
        half = len(words) // 2
        if words[:half] == words[half:]:
            text = " ".join(words[:half])
    return text


def should_translate(text: str) -> bool:
    if not text or text.startswith("©"):
        return False
    if re.fullmatch(r"[\dA-E+★◆\s.,:;()&/-]+", text):
        return False
    return bool(re.search(r"[A-Za-z]", text))


def translate(text: str, cache: dict[str, str]) -> str:
    if text in cache:
        return cache[text]
    query = urllib.parse.urlencode(
        {"client": "gtx", "sl": "en", "tl": "fr", "dt": "t", "q": text}
    )
    url = "https://translate.googleapis.com/translate_a/single?" + query
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=25) as response:
                payload = json.loads(response.read().decode("utf-8"))
            translated = "".join(item[0] for item in payload[0] if item and item[0])
            for old, new in TERM_FIXES.items():
                translated = translated.replace(old, new)
            translated = translated.replace(" ◆ ", " ◆ ").strip()
            cache[text] = translated
            return translated
        except Exception:
            if attempt == 3:
                raise
            time.sleep(1.2 * (attempt + 1))


def polish_translation(text: str) -> str:
    for old, new in TERM_FIXES.items():
        text = text.replace(old, new)
    # Le pictogramme privé du PDF original n'est pas présent dans Arial.
    text = text.replace("◆", "*")
    return text


def block_text(block: dict) -> str:
    lines = []
    for line in block.get("lines", []):
        value = "".join(span.get("text", "") for span in line.get("spans", []))
        if value.strip():
            lines.append(value.rstrip())
    return clean_source("\n".join(lines))


def block_style(block: dict) -> tuple[float, bool, tuple[float, float, float], int]:
    spans = [span for line in block.get("lines", []) for span in line.get("spans", [])]
    sizes = [float(span.get("size", 8)) for span in spans if span.get("text", "").strip()]
    size = max(sizes) if sizes else 8.0
    fonts = " ".join(str(span.get("font", "")) for span in spans).lower()
    bold = any(token in fonts for token in ("bold", "black", "semibold")) or size >= 11
    color_value = next((span.get("color", 0) for span in spans if span.get("text", "").strip()), 0)
    color = fitz.sRGB_to_pdf(int(color_value))
    direction = block.get("lines", [{}])[0].get("dir", (1.0, 0.0)) if block.get("lines") else (1.0, 0.0)
    rotate = 90 if abs(direction[1]) > 0.8 else 0
    return size, bold, color, rotate


def place_text(page: fitz.Page, rect: fitz.Rect, text: str, size: float,
               bold: bool, color: tuple[float, float, float], rotate: int) -> bool:
    fontname = "FRBold" if bold else "FRRegular"
    # Le français est souvent plus long : on commence légèrement sous la taille d'origine.
    current = min(size * 0.93, 15.5)
    minimum = 4.15
    align = fitz.TEXT_ALIGN_LEFT
    while current >= minimum:
        result = page.insert_textbox(
            rect,
            text,
            fontsize=current,
            fontname=fontname,
            color=color,
            lineheight=1.02,
            align=align,
            rotate=rotate,
            overlay=True,
        )
        if result >= 0:
            return True
        current -= 0.25
    # Dernier recours pour les minuscules légendes très contraintes.
    page.insert_textbox(
        rect,
        text,
        fontsize=minimum,
        fontname=fontname,
        color=color,
        lineheight=0.95,
        rotate=rotate,
        overlay=True,
    )
    return False


def main() -> None:
    cache = json.loads(CACHE_FILE.read_text(encoding="utf-8")) if CACHE_FILE.exists() else {}
    doc = fitz.open(SOURCE)
    page_jobs: list[list[dict]] = []
    total = 0

    for page in doc:
        jobs = []
        for block in page.get_text("dict").get("blocks", []):
            if block.get("type") != 0:
                continue
            text = block_text(block)
            if not should_translate(text):
                continue
            size, bold, color, rotate = block_style(block)
            jobs.append({
                "rect": fitz.Rect(block["bbox"]),
                "source": text,
                "size": size,
                "bold": bold,
                "color": color,
                "rotate": rotate,
            })
        page_jobs.append(jobs)
        total += len(jobs)

    done = 0
    for page_number, jobs in enumerate(page_jobs, 1):
        for job in jobs:
            job["translation"] = translate(job["source"], cache)
            done += 1
            if done % 20 == 0 or done == total:
                CACHE_FILE.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")
                print(f"Traduction : {done}/{total}", flush=True)

    for page, jobs in zip(doc, page_jobs):
        for job in jobs:
            page.add_redact_annot(job["rect"], fill=None)
        page.apply_redactions(images=0, graphics=0, text=0)
        page.insert_font(fontname="FRRegular", fontfile=FONT_REGULAR)
        page.insert_font(fontname="FRBold", fontfile=FONT_BOLD)
        for job in jobs:
            place_text(
                page, job["rect"], polish_translation(job["translation"]), job["size"],
                job["bold"], job["color"], job["rotate"],
            )

    metadata = doc.metadata or {}
    metadata["title"] = "Catan : Le Trône de Fer — Règles en français"
    metadata["subject"] = "Version française de travail réalisée à partir du livret fourni"
    doc.set_metadata(metadata)
    if OUTPUT.exists():
        OUTPUT.unlink()
    doc.save(OUTPUT, garbage=4, deflate=True, clean=True)
    print(f"PDF créé : {OUTPUT}", flush=True)


if __name__ == "__main__":
    main()
