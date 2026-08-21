from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

required = {
    "01_CANON_DEFINITIF_V3.md": [
        "2187",
        "2501",
        "35 786 km",
        "42 164 km",
        "Déclencher",
        "Propager",
        "Sécuriser",
        "314 ans",
        "coupleur déphasé",
    ],
    "03_GUIDE_MJ_TABLE_V3.md": [
        "un seul Éclat",
        "Le stand de Solarius et Lucette",
        "L’enclos de Marguerite",
        "Dans un petit cratère du trottoir repose un grain noir parfaitement plat",
        "Ce n’est pas à nous",
        "Vous êtes nuls. Bon. On coupe.",
    ],
    "05_LIEUX_ET_MACHINES_V3.md": [
        "L’ENCLOS DE MARGUERITE",
        "LE STAND B-17 DE SOLARIUS",
        "L’ATELIER DE RIPOSTE",
        "LA BAIE DE COMMANDE DE ZÉNITH",
    ],
    "10_HISTOIRE_COMPLETE_V3.md": [
        "PROLOGUE — À LIRE AUX JOUEURS",
        "Nous sommes en **2187**",
        "Héliopolis",
        "opticulture",
        "Tiānguāng",
        "Marguerite détestait les concours.",
        "Trois cent quatorze ans plus tard",
    ],
    "06_ACCESSOIRES_A_IMPRIMER_V3.md": [
        "OCCULTATION TERRITORIALE",
        "ZONE SUIVANTE : EUROPE OUEST",
        "COMMANDE : STATION ZÉNITH",
        "PROCHAINE PHASE : ÉTOILE",
    ],
}

forbidden = [
    r"74[,.]8",
    r"\bBasile\b",
    r"Contre-Lumière",
    r"dix mille",
    r"10\s?000 ans",
    r"Résistance 1\s*[—-]\s*Le premier rayon",
    r"copie d.un rapport",
    r"commences? avec deux Éclats",
]


def main():
    errors = []
    markdown = {p.name: p.read_text(encoding="utf-8") for p in ROOT.rglob("*.md")}
    corpus = "\n".join(markdown.values())

    for filename, phrases in required.items():
        text = (ROOT / filename).read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                errors.append(f"Manque dans {filename}: {phrase}")

    for pattern in forbidden:
        if re.search(pattern, corpus, flags=re.IGNORECASE):
            errors.append(f"Ancien élément encore présent: {pattern}")

    character_files = sorted((ROOT / "fiches_personnages").glob("0[1-5]_*.md"))
    if len(character_files) != 5:
        errors.append(f"Nombre de fiches personnages: {len(character_files)} au lieu de 5")
    for character_file in character_files:
        text = character_file.read_text(encoding="utf-8")
        if text.count("- [ ] Éclat") != 1:
            errors.append(f"Nombre d’Éclats incorrect dans {character_file.name}")

    expected_images = [
        "00_intro_guerre_etoile.png",
        "01_salon_opticulture.png",
        "02_interieur_grain.png",
        "03_station_zenith.png",
        "04_prise_mere.png",
    ]
    for filename in expected_images:
        if not (ROOT / "images" / filename).exists():
            errors.append(f"Image absente: {filename}")

    expected_pdfs = [
        "00_DOSSIER_MJ_COMPLET_V3.pdf",
        "01_GUIDE_MJ_TABLE_V3.pdf",
        "02_STORYBOARD_MJ_1_PAGE_V3.pdf",
        "03_PNJ_ET_DISCOURS_V3.pdf",
        "04_LIEUX_ET_MACHINES_V3.pdf",
        "05_ACCESSOIRES_JOUEURS_V3.pdf",
        "06_FICHES_PERSONNAGES_V3.pdf",
        "06_VISUELS_A_REVELER_V3.pdf",
        "07_CANON_DEFINITIF_V3.pdf",
        "08_REGLES_JOUEURS_V3.pdf",
        "10_HISTOIRE_COMPLETE_V3.pdf",
    ]
    for filename in expected_pdfs:
        if not (ROOT / "pdf" / filename).exists():
            errors.append(f"PDF absent: {filename}")

    if errors:
        print("ÉCHEC DE COHÉRENCE")
        for error in errors:
            print("-", error)
        raise SystemExit(1)

    print("OK — canon V3, un Éclat par personnage, lieux, récit, cinq images et PDF attendus présents.")


if __name__ == "__main__":
    main()
