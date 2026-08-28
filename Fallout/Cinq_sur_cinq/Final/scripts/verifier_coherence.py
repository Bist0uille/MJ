from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "00_LISEZ_MOI.md", "01_TRAME_MAITRE_COMPLETE.md",
    "02_CONDUITE_MJ.md", "03_SCENES_DIALOGUES_ET_INDICES.md",
    "04_STORYBOARD_MJ_1_PAGE.md", "05_INTRO_ET_OUTRO_A_LIRE.md",
    "06_COMBAT_ET_TENSION_ULTRA_SIMPLE.md", "07_REGLES_ET_STATS.md",
    "08_ACCESSOIRES_A_IMPRIMER.md", "09_AMBIANCE_SONORE.md",
]

EXPECTED_AUDIO = [
    "01_HARMONY_QUATRE_NOTES.mp3",
    "02_HARMONY_CINQ_NOTES_CONTROLE.mp3",
    "03_CINQUIEME_NOTE_SEULE.mp3",
    "04_HARMONY_QUATRE_NOTES_BOUCLE.mp3",
]

REQUIRED_PHRASES = {
    "01_TRAME_MAITRE_COMPLETE.md": ["Abel Mercer", "Richard Halvhrest", "Dr Evelyn Ward", "Claire Bell", "Mara Halvhrest", "HARMONY™"],
    "03_SCENES_DIALOGUES_ET_INDICES.md": ["Mes habitants sont morts", "Vous n’êtes pas eux", "Abel", "SOMNEX-R", "Richard", "Mara", "reproduction de Claire"],
    "08_ACCESSOIRES_A_IMPRIMER.md": ["PROFILS RÉSIDENTS ENREGISTRÉS : 5/5", "SOMNEX-R", "PRIORITÉ SUPÉRIEURE", "DÉCÈS ENREGISTRÉS : 0"],
}

FORBIDDEN = [
    r"cycle\s+84[0-9]",
    r"capsule\s+médicale",
    r"violence\s+conjugale",
    r"cette maison finira par nous tuer",
    r"ne laisse surtout pas cette machine me médicamenter",
    r"profils résidents enregistrés\s*:\s*6",
]

EXPECTED_PDFS = [
    "01_TRAME_MAITRE_COMPLETE.pdf", "02_CONDUITE_MJ.pdf",
    "03_SCENES_DIALOGUES_ET_INDICES.pdf", "04_STORYBOARD_MJ_1_PAGE.pdf",
    "05_INTRO_ET_OUTRO_A_LIRE.pdf", "06_COMBAT_ET_TENSION_ULTRA_SIMPLE.pdf",
    "07_REGLES_ET_STATS.pdf", "08_ACCESSOIRES_MIS_EN_PAGE.pdf",
    "09_AMBIANCE_SONORE.pdf", "10_FICHES_PERSONNAGES_NB.pdf",
    "11_PLAN_MJ_COMPLET.pdf", "12_PLAN_JOUEUR_A_DECOUPER.pdf",
    "13_PHOTOS_MIROIRS.pdf",
]

EXPECTED_IMAGES = [
    "images/personnages/zora_fusible_vale.png",
    "images/personnages/anatole_trois_murs_duroc.png",
    "images/personnages/nell_deux_coups_rainer.png",
    "images/personnages/dr_lazare_bonbon_miette.png",
    "images/personnages/rook_tout_doux.png",
    "images/robots/monsieur_hector.png",
    "images/robots/mademoiselle_bonrepos.png",
    "images/robots/clovis_boulon_13.png",
    "images/robots/colonel_basilisk.png",
    "images/storyboard/01_arrivee_manoir.png",
    "images/storyboard/02_abel_generateur.png",
    "images/storyboard/03_evelyn_bonrepos.png",
    "images/storyboard/04_richard_quarantaine.png",
    "images/storyboard/05_piano_harmony.png",
    "images/storyboard/06_coeur_sali.png",
    "images/accessoires/photo_residents_halvhrest.png",
    "images/accessoires/photo_miroir_pj.png",
]


def main():
    errors = []
    warnings = []
    for filename in REQUIRED_FILES:
        if not (ROOT / filename).exists():
            errors.append(f"Fichier absent : {filename}")
    corpus = "\n".join((ROOT / filename).read_text(encoding="utf-8") for filename in REQUIRED_FILES if (ROOT / filename).exists())
    for filename, phrases in REQUIRED_PHRASES.items():
        text = (ROOT / filename).read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase.casefold() not in text.casefold():
                errors.append(f"Manque dans {filename} : {phrase}")
    for pattern in FORBIDDEN:
        if re.search(pattern, corpus, flags=re.IGNORECASE):
            errors.append(f"Élément interdit : {pattern}")
    characters = sorted((ROOT / "fiches_personnages").glob("0[1-5]_*.md"))
    if len(characters) != 5:
        errors.append(f"Nombre de prétirés : {len(characters)} au lieu de 5")
    for character in characters:
        text = character.read_text(encoding="utf-8")
        for field in ["**PV", "## Ce que tu veux", "**Question finale :**"]:
            if field not in text:
                errors.append(f"Champ manquant dans {character.name} : {field}")
        if "**Compétences :**" not in text and "**Spécialités :**" not in text:
            errors.append(f"Champ manquant dans {character.name} : compétences ou spécialités")
        if re.search(r"\bSALI\b|SALI-CENTRAL", text, flags=re.IGNORECASE):
            errors.append(f"Spoiler SALI dans {character.name}")
    player_corpus = "\n".join(character.read_text(encoding="utf-8") for character in characters)
    if re.search(r"\bSacha\b|\bSasha\b", player_corpus, flags=re.IGNORECASE):
        errors.append("Un ancien prénom Sacha/Sasha subsiste dans les prétirés")
    registry = (ROOT / "08_ACCESSOIRES_A_IMPRIMER.md").read_text(encoding="utf-8").split("# 2 —", 1)[0]
    if re.search(r"accès\s+(?:domestique|médical|maintenance|principal)", registry, flags=re.IGNORECASE):
        errors.append("Le registre public contient encore des droits d'accès")
    for filename in EXPECTED_PDFS:
        if not (ROOT / "pdf" / filename).exists():
            errors.append(f"PDF absent : {filename}")
    for relative_path in EXPECTED_IMAGES:
        if not (ROOT / relative_path).exists():
            errors.append(f"Image absente : {relative_path}")
    for filename in EXPECTED_AUDIO:
        if not (ROOT / "audio" / filename).exists():
            warnings.append(f"Audio local absent : {filename}")
    if errors:
        print("ÉCHEC DE COHÉRENCE")
        for error in errors:
            print("-", error)
        raise SystemExit(1)
    for warning in warnings:
        print("AVERTISSEMENT —", warning)
    print("OK — cinq PJ, cinq morts, mystère progressif, accessoires, PDF et images présents.")


if __name__ == "__main__":
    main()
