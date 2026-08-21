from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import KeepInFrame, Paragraph


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "pdf_v2" / "05_STORYBOARD_MJ_1_PAGE.pdf"
FONT_DIR = Path(r"C:\Windows\Fonts")

pdfmetrics.registerFont(TTFont("BoardArial", FONT_DIR / "arial.ttf"))
pdfmetrics.registerFont(TTFont("BoardArial-Bold", FONT_DIR / "arialbd.ttf"))


SCENES = [
    ("1", "SALON", "0:00–0:15", "<b>Sensoriel :</b> verrière dorée, jingles décalés, plastique neuf, herbe chaude.<br/><b>Voir :</b> Marguerite, porte Héliocell, machine.<br/><b>Appeler :</b> Maëlle présente ; Noé inspecte ; Iris reconnaît ; Sacha enquête ; Céleste observe.<br/><b>Sortie :</b> démonstration."),
    ("2", "ÉCLIPSE + FUITE", "0:15–0:40", "<b>Sensoriel :</b> nef noire, alarmes mourantes, ozone, sueur, bêtes affolées.<br/><b>Dire :</b> « La lumière ne baisse pas. Elle s'arrête. »<br/><b>Appeler :</b> Maëlle+Céleste / Marguerite ; Noé+Iris / porte ; Sacha / Lucette.<br/><b>Révéler :</b> grain noir.<br/><b>Sortie :</b> laboratoire."),
    ("3", "LABORATOIRE", "0:40–1:05", "<b>Sensoriel :</b> briques, câbles, relais cliquetants, poussière chaude, café brûlé, ozone.<br/><b>Voir :</b> machine 4 places corrigée « 5, probablement ».<br/><b>Appeler :</b> Maëlle dose ; Noé alimente ; Céleste règle ; Sacha protège ; Iris force.<br/><b>Sortie :</b> « Ding »."),
    ("4", "DÉSERT MIROIR", "1:05–1:15", "<b>Sensoriel :</b> plaques infinies, claquements secs, métal chaud, air froid, ozone.<br/><b>Voir :</b> doubles, mur d'ombre.<br/><b>Appeler :</b> Céleste trouve ; Sacha brouille ; Noé manipule.<br/><b>Révéler :</b> appareil Tiānguāng.<br/><b>Sortie :</b> élevage."),
    ("5", "ÉLEVAGE", "1:15–1:30", "<b>Sensoriel :</b> ruche lumineuse, battements humides, serre chaude, sucre brûlé, métal stérile.<br/><b>Voir :</b> alvéoles ; naissance = facture.<br/><b>Appeler :</b> Maëlle choisit ; Iris gère la garde ; Sacha prend une preuve.<br/><b>Sortie :</b> cœur."),
    ("6", "CŒUR", "1:30–1:45", "<b>Sensoriel :</b> salle ronde glacée, clics de caisse, métal stérile, ozone sec.<br/><b>Révéler :</b> occultation → Crépuscule → Europe Ouest → Zénith → phase Étoile.<br/><b>Appeler :</b> Noé retourne ; Iris prend les clés ; Céleste lit ; Sacha copie.<br/><b>Sortie :</b> rayon."),
    ("7", "SUN+ + DYSON", "1:45–2:10", "<b>Sensoriel :</b> Soleil publicitaire, musique douce, plastique propre, parfum citronné artificiel.<br/><b>Dire :</b> « À quelle heure souhaitez-vous que le jour commence ? »<br/><b>Révéler :</b> vente de lumière ; Dyson.<br/><b>Appeler :</b> Iris répond ; Céleste nomme ; Sacha prouve."),
    ("8", "ATELIER DE RIPOSTE", "2:10–2:30", "<b>Sensoriel :</b> table bancale, craie grinçante, câbles chauds, café, poussière.<br/><b>Demander :</b> source ? trajet ? prix ? nom ?<br/><b>Tour :</b> « Ma contribution, c'est… »<br/><b>Interdit :</b> proposer la solution.<br/><b>Sortie :</b> « Ça peut marcher. »"),
    ("9", "GUERRE + ZÉNITH", "2:30–3:15", "<b>Sensoriel :</b> cathédrale orbitale, validations cristallines, air filtré parfaitement inodore.<br/><b>Résistances :</b> premier rayon ; chasseurs ; Qiao.<br/><b>Appeler :</b> Céleste vise ; Noé active ; Sacha relaie ; Maëlle mobilise ; Iris affronte.<br/><b>Sortie :</b> résultat + prix."),
    ("10", "PRISE + FINALE", "3:15–3:40", "<b>Sensoriel :</b> trappe arrachée, grondement électrique, caoutchouc chaud, poussière cosmique, ozone.<br/><b>Ordre :</b> Prise → Noé → Qiao ignore → vaisseau → téléréalité → coupure → action → 10 000 ans.<br/><b>Demander :</b> comment l'invention survit-elle ?<br/><b>Fin :</b> « Vous avez fini vos conneries ? »"),
]


def draw_card(c, x, y, w, h, scene, accent):
    number, title, time, body = scene
    c.setFillColor(HexColor("#F8F5ED"))
    c.setStrokeColor(accent)
    c.setLineWidth(0.8)
    c.roundRect(x, y, w, h, 2.5 * mm, fill=1, stroke=1)

    c.setFillColor(accent)
    c.circle(x + 7 * mm, y + h - 7 * mm, 4.7 * mm, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("BoardArial-Bold", 8.5)
    c.drawCentredString(x + 7 * mm, y + h - 8.2 * mm, number)

    c.setFillColor(HexColor("#20252B"))
    c.setFont("BoardArial-Bold", 9.2)
    c.drawString(x + 14 * mm, y + h - 6.5 * mm, title)
    c.setFillColor(accent)
    c.setFont("BoardArial-Bold", 7)
    c.drawRightString(x + w - 4 * mm, y + h - 6.5 * mm, time)

    style = ParagraphStyle(
        "card",
        fontName="BoardArial",
        fontSize=7.15,
        leading=8.45,
        textColor=HexColor("#20252B"),
    )
    frame = KeepInFrame(w - 8 * mm, h - 16 * mm, [Paragraph(body, style)], mode="shrink", vAlign="TOP")
    _, used_h = frame.wrapOn(c, w - 8 * mm, h - 16 * mm)
    frame.drawOn(c, x + 4 * mm, y + h - 13 * mm - used_h)


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(OUT), pagesize=A4, pageCompression=1)
    width, height = A4

    c.setFillColor(HexColor("#EEE9DC"))
    c.rect(0, 0, width, height, fill=1, stroke=0)
    c.setFillColor(HexColor("#172E3B"))
    c.rect(0, height - 19 * mm, width, 19 * mm, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("BoardArial-Bold", 15)
    c.drawString(8 * mm, height - 9 * mm, "LA GUERRE DE L'ÉTOILE — STORYBOARD MJ")
    c.setFont("BoardArial", 7.4)
    c.drawString(8 * mm, height - 14.5 * mm, "Une page · cinq joueurs · une révélation à la fois")
    c.drawRightString(width - 8 * mm, height - 14.5 * mm, "Durée cible : 3 h 40")

    margin_x = 7 * mm
    gap_x = 4 * mm
    gap_y = 2.7 * mm
    footer_h = 25 * mm
    top_y = height - 22 * mm
    grid_h = top_y - footer_h - 5 * mm
    card_w = (width - 2 * margin_x - gap_x) / 2
    card_h = (grid_h - 4 * gap_y) / 5
    accents = [HexColor("#167C73"), HexColor("#A34B22"), HexColor("#253E78"), HexColor("#7B2D70"), HexColor("#C79016")]

    for idx, scene in enumerate(SCENES):
        col = idx // 5
        row = idx % 5
        x = margin_x + col * (card_w + gap_x)
        y = top_y - (row + 1) * card_h - row * gap_y
        draw_card(c, x, y, card_w, card_h, scene, accents[row])

    c.setFillColor(HexColor("#172E3B"))
    c.roundRect(7 * mm, 5 * mm, width - 14 * mm, 17 * mm, 2 * mm, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("BoardArial-Bold", 7.5)
    c.drawString(10 * mm, 17 * mm, "RÔLES")
    c.setFont("BoardArial", 7)
    c.drawString(28 * mm, 17 * mm, "Maëlle=loupes · Noé=machines · Céleste=ciel · Sacha=preuves · Iris=Tiānguāng")
    c.setFont("BoardArial-Bold", 7.5)
    c.drawString(10 * mm, 12 * mm, "GARDE-FOUS")
    c.setFont("BoardArial", 6.7)
    c.drawString(35 * mm, 12 * mm, "Prise seulement après Zénith · résultat de l'invention avant les extraterrestres · une bonne idée réussit")
    c.setFont("BoardArial-Bold", 7.5)
    c.drawString(10 * mm, 7.7 * mm, "ABSURDE")
    c.setFont("BoardArial", 6.35)
    c.drawString(28 * mm, 7.7 * mm, "Hors service sur batterie · personne ne franchit le feu éteint · manuel miniaturisé · mode PowerPoint · facture avant impact")

    c.showPage()
    c.save()
    print(OUT)


if __name__ == "__main__":
    main()
