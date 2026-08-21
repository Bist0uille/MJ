from pathlib import Path
import importlib.util
import shutil

HERE = Path(__file__).resolve()
ROOT = HERE.parents[1]
BASE_SCRIPT = HERE.parents[2] / "Sunshine" / "scripts" / "generer_fiches_pdf.py"

spec = importlib.util.spec_from_file_location("sunshine_character_base_v3", BASE_SCRIPT)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
base.ROOT = ROOT
base.IMG_DIR = ROOT / "images" / "personnages"
base.OUT_DIR = ROOT / "pdf" / "fiches_personnages"

if __name__ == "__main__":
    base.main()
    shutil.copyfile(
        base.OUT_DIR / "00_fiches_personnages_complet.pdf",
        ROOT / "pdf" / "06_FICHES_PERSONNAGES_V3.pdf",
    )
