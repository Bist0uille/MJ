from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "pdf" / "02_STORYBOARD_MJ_1_PAGE_V3.pdf"
FONT_DIR = Path(r"C:\Windows\Fonts")
pdfmetrics.registerFont(TTFont("BoardArial", FONT_DIR / "arial.ttf"))
pdfmetrics.registerFont(TTFont("BoardArial-Bold", FONT_DIR / "arialbd.ttf"))

BODY = ParagraphStyle("body", fontName="BoardArial", fontSize=5.8, leading=7.1, textColor=HexColor("#20262A"))
HEAD = ParagraphStyle("head", fontName="BoardArial-Bold", fontSize=6.2, leading=7.2, textColor=white)

ROWS = [
    ("0:00", "<b>SALON</b><br/>Réunir le Groupe Soleil", "Verrière dorée, bêlements cristallins, annonces polies, caramel chaud, ozone.", "Concours ; Héliocell ; Lucette ; badge commun. Chacun se présente.", "Maëlle : Marguerite. Noé : machine. Iris : discours. Sacha : preuve. Céleste : ciel faux."),
    ("0:20", "<b>CRÉPUSCULE</b><br/>Choisir dans l’urgence", "Soleil tranché, silence aspiré, alarmes molles, plastique chaud, laine.", "Ombre artificielle ; stockage verrouillé. Jouer deux urgences.", "Céleste mesure. Noé ouvre. Maëlle calme. Iris ordonne. Sacha conserve."),
    ("0:45", "<b>GRAIN</b><br/>Donner une piste physique", "Trottoir froid, lampe grinçante, poussière métallique, reflet vertical, silence.", "Grain noir plat ; pivote vers la lampe et vise le ciel. Solarius l’emporte.", "Maëlle lit. Céleste vise. Sacha filme. Noé isole. Iris reconnaît une logique."),
    ("1:00", "<b>LABO</b><br/>Décider d’entrer", "Cuivre humide, bocaux lumineux, pompes asthmatiques, craie, café brûlé.", "Grain artificiel, actif, trop petit. Lucette garde un rayon. Miniaturiseur + rappel.", "Noé stabilise. Céleste règle. Maëlle rassure. Iris accède. Sacha enregistre."),
    ("1:20", "<b>DANS LE GRAIN</b><br/>Comprendre", "Désert noir, doubles précoces, chœurs radio, chaleur sèche, goût de pile.", "Six bandelettes : occultation ; Crépuscule ; Héliopolis ; Europe ; Zénith ; Étoile. Zéro alien.", "Une action de domaine chacun ; finir par la fuite du cœur."),
    ("2:00", "<b>QIAO + ATELIER</b><br/>Inventer", "Atelier sombre, outils au sol, voix lointaines, huile, peur.", "Qiao assume SUN+. 10 min : déclencher, propager, sécuriser.", "Tour : « Ma contribution… » Loupes ; machines ; ciel ; preuves/signal ; accès."),
    ("2:30", "<b>ZÉNITH</b><br/>Gagner contre Qiao", "Terre immense, coque vibrante, bips feutrés, air recyclé, métal.", "35 786 km. Verrou physique. Argument incendie. Montrer le retour du jour avant twist.", "Iris répond à Qiao. Priorité aux jetons non retournés."),
    ("3:10", "<b>PRISE MÈRE</b><br/>Changer d’échelle", "Câble-tunnel, ozone violet, grondement grave, matière hésitante, poussière chaude.", "« Ce n’est pas à nous. » Vrrr-7 : émission, caméras, énergie cachée, coupure.", "Noé identifie. Sacha diffuse. Tous sauvent l’héritage de la riposte."),
    ("3:30", "<b>314 ANS</b><br/>Rendre les choix durables", "Moulin nocturne, dynamos râpeuses, soupe fumée, laine, charbon froid.", "Monde fragmenté mais vivant. Groupe Soleil devenu légende. Retour de Vrrr-7.", "À chacun : « Qu’est devenu ton héritage ? »"),
]


def p(text, style=BODY):
    return Paragraph(text, style)


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    width, height = landscape(A4)
    c = canvas.Canvas(str(OUT), pagesize=(width, height), pageCompression=1)
    c.setTitle("La Guerre de l’Étoile — Storyboard MJ V3")
    c.setFillColor(HexColor("#F8F5EC"))
    c.rect(0, 0, width, height, fill=1, stroke=0)
    c.setFillColor(HexColor("#18252D"))
    c.rect(0, height - 18 * mm, width, 18 * mm, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("BoardArial-Bold", 16)
    c.drawString(9 * mm, height - 10 * mm, "LA GUERRE DE L’ÉTOILE — STORYBOARD MJ V3")
    c.setFont("BoardArial", 7.5)
    c.drawRightString(width - 9 * mm, height - 10 * mm, "1 image + 1 information + 1 choix")

    headers = ["TEMPS", "SCÈNE / BUT", "ENDROIT — SON — ODEUR", "À DIRE / RÉVÉLER", "INTERPELLATIONS"]
    data = [[p(x, HEAD) for x in headers]]
    data += [[p(cell) for cell in row] for row in ROWS]
    table = Table(data, colWidths=[16*mm, 39*mm, 58*mm, 76*mm, 87*mm], rowHeights=[8*mm] + [16.5*mm]*len(ROWS))
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), HexColor("#B87912")),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [white, HexColor("#EFEADD")]),
        ("GRID", (0,0), (-1,-1), .35, HexColor("#BBAF92")),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING", (0,0), (-1,-1), 3),
        ("RIGHTPADDING", (0,0), (-1,-1), 3),
        ("TOPPADDING", (0,0), (-1,-1), 2),
        ("BOTTOMPADDING", (0,0), (-1,-1), 2),
    ]))
    tw, th = table.wrap(width - 18*mm, height)
    table.drawOn(c, 9*mm, height - 21*mm - th)

    c.setFillColor(HexColor("#18252D"))
    c.setFont("BoardArial-Bold", 7)
    c.drawString(9*mm, 7*mm, "SI TU BLOQUES : Solarius reformule les faits déjà trouvés, jamais la solution.")
    c.drawRightString(width - 9*mm, 7*mm, "Ordre sacré : victoire visible → Prise Mère → Vrrr-7 → 314 ans")
    c.showPage()
    c.save()
    print(OUT)


if __name__ == "__main__":
    main()

