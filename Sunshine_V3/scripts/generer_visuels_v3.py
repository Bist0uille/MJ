from pathlib import Path
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "pdf" / "06_VISUELS_A_REVELER_V3.pdf"
FONT_DIR = Path(r"C:\Windows\Fonts")
pdfmetrics.registerFont(TTFont("VisualArial", FONT_DIR / "arial.ttf"))
pdfmetrics.registerFont(TTFont("VisualArial-Bold", FONT_DIR / "arialbd.ttf"))

PAGES = [
    ("00_intro_guerre_etoile.png", "1 — LA GUERRE DE L’ÉTOILE", "Montrer avant de lire le prologue"),
    ("01_salon_opticulture.png", "2 — LE SALON D’OPTICULTURE", "Montrer après le prologue"),
    ("02_interieur_grain.png", "3 — L’INTÉRIEUR DU GRAIN", "Montrer après la miniaturisation"),
    ("03_station_zenith.png", "4 — LA STATION ZÉNITH", "Montrer à l’arrivée en orbite"),
    ("04_prise_mere.png", "5 — LA PRISE MÈRE", "Garder cachée jusqu’après la victoire terrestre"),
]


def draw_cover(c, width, height):
    c.setFillColor(HexColor("#18252D"))
    c.rect(0, 0, width, height, fill=1, stroke=0)
    c.setFillColor(HexColor("#D79A20"))
    c.circle(width * .78, height * .58, height * .23, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("VisualArial-Bold", 30)
    c.drawString(28, height - 80, "LA GUERRE DE L’ÉTOILE")
    c.setFont("VisualArial", 17)
    c.drawString(30, height - 112, "Cinq images à révéler — dans l’ordre")
    c.setFont("VisualArial-Bold", 12)
    c.drawString(30, 45, "MJ : ne laisse pas les joueurs feuilleter ce document.")


def draw_image_page(c, width, height, filename, title, moment):
    path = ROOT / "images" / filename
    with Image.open(path) as img:
        iw, ih = img.size
    footer_h = 45
    scale = min(width / iw, (height - footer_h) / ih)
    dw, dh = iw * scale, ih * scale
    x, y = (width - dw) / 2, footer_h + (height - footer_h - dh) / 2
    c.setFillColor(HexColor("#101820"))
    c.rect(0, 0, width, height, fill=1, stroke=0)
    c.drawImage(str(path), x, y, dw, dh, preserveAspectRatio=True, mask="auto")
    c.setFillColor(HexColor("#18252D"))
    c.rect(0, 0, width, footer_h, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("VisualArial-Bold", 13)
    c.drawString(20, 25, title)
    c.setFont("VisualArial", 9)
    c.drawRightString(width - 20, 25, moment)


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    size = landscape(A4)
    c = canvas.Canvas(str(OUT), pagesize=size, pageCompression=1)
    c.setTitle("La Guerre de l’Étoile — Visuels V3")
    draw_cover(c, *size)
    c.showPage()
    for page in PAGES:
        draw_image_page(c, *size, *page)
        c.showPage()
    c.save()
    print(OUT)


if __name__ == "__main__":
    main()
