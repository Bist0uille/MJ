from pathlib import Path
import importlib.util


HERE = Path(__file__).resolve()
ROOT = HERE.parents[1]
OLD_SCRIPT = HERE.parents[2] / "Sunshine" / "scripts" / "generer_guides_pdf.py"

spec = importlib.util.spec_from_file_location("sunshine_pdf_base", OLD_SCRIPT)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)

base.ROOT = ROOT
base.OUT_DIR = ROOT / "pdf_v2"


def main():
    jobs = [
        (
            "00_DOSSIER_MJ_V2_COMPLET.pdf",
            "V2 SIMPLIFIÉE — DOSSIER COMPLET",
            [
                ("00_LISEZ_MOI.md", "Canon et chemin critique"),
                ("01_GUIDE_MJ_V2.md", "Guide MJ et scénario"),
                ("02_PNJ_LIEUX_FACTIONS_V2.md", "PNJ, lieux et forces"),
                ("03_AIDES_DE_JEU_V2.md", "Aides de jeu"),
                ("04_PRETIRES_V2.md", "Cinq personnages"),
                ("05_DESCRIPTIONS_LIEUX_ET_MACHINES.md", "Descriptions à lire"),
            ],
        ),
        (
            "01_GUIDE_MJ_V2.pdf",
            "V2 SIMPLIFIÉE — GUIDE MJ",
            [
                ("00_LISEZ_MOI.md", "Canon et chemin critique"),
                ("01_GUIDE_MJ_V2.md", "Guide MJ et scénario"),
            ],
        ),
        (
            "02_AIDES_DE_JEU_V2.pdf",
            "V2 SIMPLIFIÉE — AIDES DE JEU",
            [("03_AIDES_DE_JEU_V2.md", "Documents à imprimer")],
        ),
        (
            "03_PRETIRES_V2.pdf",
            "V2 SIMPLIFIÉE — PERSONNAGES",
            [("04_PRETIRES_V2.md", "Cinq personnages")],
        ),
        (
            "04_DESCRIPTIONS_LIEUX_ET_MACHINES.pdf",
            "V2 SIMPLIFIÉE — DESCRIPTIONS À LIRE",
            [("05_DESCRIPTIONS_LIEUX_ET_MACHINES.md", "Lieux, machines et détails WTF")],
        ),
        (
            "06_EXPLICATION_COMPLETE_COHERENCE.pdf",
            "V2 — EXPLICATION COMPLÈTE ET AUDIT DE COHÉRENCE",
            [("07_EXPLICATION_COMPLETE_ET_COHERENCE.md", "Du monde initial à l'épilogue")],
        ),
    ]
    outputs = [base.build_pdf(*job) for job in jobs]
    print(f"Généré : {len(outputs)} PDF dans {base.OUT_DIR}")
    for output in outputs:
        print(output.name)


if __name__ == "__main__":
    main()
