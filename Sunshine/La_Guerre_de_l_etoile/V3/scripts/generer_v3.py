from pathlib import Path
import importlib.util

HERE = Path(__file__).resolve()
ROOT = HERE.parents[1]
BASE_SCRIPT = HERE.parents[2] / "Sunshine" / "scripts" / "generer_guides_pdf.py"

spec = importlib.util.spec_from_file_location("sunshine_pdf_base_v3", BASE_SCRIPT)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
base.ROOT = ROOT
base.OUT_DIR = ROOT / "pdf"
base.PAGEBREAK_H1 = False


def main():
    jobs = [
        (
            "00_DOSSIER_MJ_COMPLET_V3.pdf",
            "V3 — DOSSIER MJ COMPLET",
            [
                ("00_LISEZ_MOI.md", "Mode d’emploi et impression"),
                ("01_CANON_DEFINITIF_V3.md", "Canon définitif"),
                ("03_GUIDE_MJ_TABLE_V3.md", "Guide de table"),
                ("04_PNJ_ET_DISCOURS_V3.md", "PNJ et discours"),
                ("05_LIEUX_ET_MACHINES_V3.md", "Lieux et machines"),
                ("10_HISTOIRE_COMPLETE_V3.md", "Histoire complète — récit témoin"),
                ("07_CINQ_PERSONNAGES_MJ.md", "Mémo des cinq personnages"),
            ],
        ),
        (
            "01_GUIDE_MJ_TABLE_V3.pdf",
            "V3 — GUIDE MJ DE TABLE",
            [
                ("00_LISEZ_MOI.md", "Mode d’emploi"),
                ("03_GUIDE_MJ_TABLE_V3.md", "Déroulé complet"),
            ],
        ),
        (
            "03_PNJ_ET_DISCOURS_V3.pdf",
            "V3 — PNJ ET DISCOURS",
            [("04_PNJ_ET_DISCOURS_V3.md", "Interprétation et révélations")],
        ),
        (
            "04_LIEUX_ET_MACHINES_V3.pdf",
            "V3 — LIEUX ET MACHINES",
            [("05_LIEUX_ET_MACHINES_V3.md", "Descriptions à lire")],
        ),
        (
            "05_ACCESSOIRES_JOUEURS_V3.pdf",
            "V3 — ACCESSOIRES JOUEURS",
            [("06_ACCESSOIRES_A_IMPRIMER_V3.md", "Documents à découper et révéler")],
        ),
        (
            "07_CANON_DEFINITIF_V3.pdf",
            "V3 — CANON ET COHÉRENCE",
            [("01_CANON_DEFINITIF_V3.md", "Explication définitive")],
        ),
        (
            "08_REGLES_JOUEURS_V3.pdf",
            "V3 — RÈGLES JOUEURS",
            [("fiches_personnages/00_REGLES_RAPIDES.md", "Règles rapides")],
        ),
        (
            "10_HISTOIRE_COMPLETE_V3.pdf",
            "V3 — HISTOIRE COMPLÈTE",
            [("10_HISTOIRE_COMPLETE_V3.md", "Récit intégral avant préparation MJ")],
        ),
    ]
    outputs = [base.build_pdf(*job) for job in jobs]
    for output in outputs:
        print(output)


if __name__ == "__main__":
    main()
