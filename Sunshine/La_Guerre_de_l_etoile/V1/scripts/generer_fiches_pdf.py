from pathlib import Path

from reportlab.lib.colors import Color, HexColor, white
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import KeepInFrame, Paragraph, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[1]
IMG_DIR = ROOT / "images" / "personnages"
OUT_DIR = ROOT / "pdf_personnages"

FONT_DIR = Path(r"C:\Windows\Fonts")
pdfmetrics.registerFont(TTFont("SunArial", FONT_DIR / "arial.ttf"))
pdfmetrics.registerFont(TTFont("SunArial-Bold", FONT_DIR / "arialbd.ttf"))
pdfmetrics.registerFont(TTFont("SunArial-Italic", FONT_DIR / "ariali.ttf"))


CHARACTERS = [
    {
        "file": "01_maelle_prisme.pdf",
        "image": "maelle_prisme.png",
        "name": "MAËLLE « SIFFLET » PRISME",
        "role": "Bergère de loupes — championne junior de courbure",
        "quote": "Une loupe ne brûle jamais quelqu'un sans raison.",
        "accent": "#167C73",
        "visible": (
            "Lunettes de soudeur sur le front, sifflet autour du cou : tu prétends connaître "
            "le prénom des huit mille loupes de l'exploitation familiale. Tu es venue présenter "
            "Marguerite II au concours de courbure."
        ),
        "stats": {"Force": 1, "Adresse": 1, "Technique": 0, "Science": 0, "Influence": 3, "Opticulture": 3},
        "signature": (
            "<b>LE GRAND RAPPEL — 1 fois, sans jet.</b> Toutes les loupes présentes t'obéissent "
            "immédiatement, y compris les gardes-loupes. Décris le chant ou le geste reconnu."
        ),
        "burst": (
            "<b>JE CONNAIS SON NOM — 1 Éclat.</b> Face à une créature optique, le MJ révèle "
            "ce qu'elle veut, ce qu'elle craint et ce qui gagnerait sa confiance."
        ),
        "lever": (
            "<b>L'APPEL DU TROUPEAU.</b> Attire, calme ou fais suivre une lumière simple aux loupes "
            "domestiquées proches. Elles restent des animaux et ne comprennent pas un plan complexe."
        ),
        "gear": "Sifflet à six tons ; 3 gels lumineux ; gant anti-focale ; laisse variable ; lunettes renforcées ; cloche de Marguerite.",
        "secret": (
            "Marguerite appartient à la dernière génération autorisée. Ta famille ne peut pas racheter "
            "une souche fertile : tu as modifié sa date de naissance et Iris a effacé l'alerte. Si cela "
            "se sait, l'exploitation peut perdre tout son troupeau."
        ),
        "links": (
            "<b>Noé :</b> il a sauvé votre serre. <b>Iris :</b> elle a effacé l'alerte mais sa famille "
            "écrit les règles. <b>Sacha :</b> il sait que l'exploitation va mal."
        ),
        "dilemma": "Sauver les loupes peut-il justifier la disparition du métier de ta famille ?",
        "atelier": "Observe les besoins des créatures, gagne leur confiance ou détourne leur attention.",
    },
    {
        "file": "02_noe_volt.pdf",
        "image": "noe_volt.png",
        "name": "NOÉ « LA MANIVELLE » VOLT",
        "role": "Mécano rétrograde — ennemi officiel du progrès",
        "quote": "Si ça nécessite une mise à jour, ce n'est pas un outil.",
        "accent": "#A34B22",
        "visible": (
            "Ta ceinture contient tournevis, clés, ficelle, poignée et marteau : des objets presque "
            "subversifs dans une ville sans mécanisme manuel. Tu es au Salon pour empêcher la "
            "machine de Solarius d'exploser."
        ),
        "stats": {"Force": 1, "Adresse": 3, "Technique": 3, "Science": 1, "Influence": 0, "Opticulture": 0},
        "signature": (
            "<b>IL Y A TOUJOURS UNE POIGNÉE — 1 fois, sans jet.</b> Révèle un accès manuel, une "
            "alimentation oubliée ou un mécanisme physique permettant de contourner un blocage."
        ),
        "burst": (
            "<b>PAS BESOIN DE PHOTONS — 1 Éclat.</b> Fais fonctionner une machine sans son énergie "
            "normale le temps d'une action importante. Ensuite, elle casse, chauffe ou exige un effort continu."
        ),
        "lever": (
            "<b>FONCTIONNEMENT MANUEL.</b> Avec du temps et des pièces, ajoute un contrôle, une alimentation "
            "ou un déverrouillage manuel. Il sera lent, bruyant et parfois actionné en continu."
        ),
        "gear": "Manivelle universelle ; lampe à dynamo ; câble de cuivre ; clés ; plan papier d'Héliopolis ; marteau décoratif.",
        "secret": (
            "Lors d'un exercice, tu as découvert que presque tous les secours dépendent du réseau central. "
            "On t'a ordonné de te taire pour protéger le label zéro panne. Tu as seulement conservé "
            "tes souvenirs et ton plan papier annoté."
        ),
        "links": (
            "<b>Maëlle :</b> elle respecte ta manivelle. <b>Iris :</b> tu l'interroges sur les secours. "
            "<b>Sacha :</b> son article sur tes poignées a obtenu douze lecteurs."
        ),
        "dilemma": "Veux-tu sauver une civilisation technologique dont tu rêves de prouver l'échec ?",
        "atelier": "Cherche ce qui bouge réellement : moteur, verrou, câble, charnière ou alimentation.",
    },
    {
        "file": "03_iris_qiao.pdf",
        "image": "iris_qiao.png",
        "name": "IRIS QIAO — « SON ALTESSE SOLAIRE »",
        "role": "Héritière Héliocell — princesse du Soleil",
        "quote": "Ce n'est pas un privilège. C'est une phase de test premium.",
        "accent": "#C79016",
        "visible": (
            "Ton uniforme autoéclairé et ton ombrelle photovoltaïque ne connaissent jamais une mauvaise "
            "lumière. Tu inaugures le pavillon Héliocell au nom de ta tante Qiao Wen, directrice de Tiānguāng."
        ),
        "stats": {"Force": 0, "Adresse": 1, "Technique": 3, "Science": 1, "Influence": 3, "Opticulture": 0},
        "signature": (
            "<b>PRIORITÉ ABSOLUE — 1 fois, sans jet.</b> Une machine, un employé ou un système "
            "Tiānguāng te reconnaît comme membre de la famille Qiao et exécute ton ordre avant vérification."
        ),
        "burst": (
            "<b>CLAUSE PREMIUM — 1 Éclat.</b> Révèle un privilège ou une procédure interne donnant "
            "temporairement accès à un lieu, une information ou un service réservé."
        ),
        "lever": (
            "<b>LE CARNET D'ADRESSES QIAO.</b> Obtiens d'un contact Tiānguāng une information, une livraison "
            "ou un accès raisonnable. La demande laisse ton nom et crée une faveur familiale."
        ),
        "gear": "Badge exécutif ; terminal sécurisé ; ombrelle photovoltaïque ; uniforme autoéclairé ; services premium ; canal familial.",
        "secret": (
            "Ta tante te fait inaugurer une gamme sans t'avoir donné son dossier technique complet. Tu as "
            "accepté pour ne pas paraître indigne. Tu as aussi effacé l'alerte sur la licence de Marguerite."
        ),
        "links": (
            "<b>Maëlle :</b> elle ignore ce que tu as risqué. <b>Noé :</b> son mépris ressemble parfois "
            "à une vérité. <b>Sacha :</b> tu lui as transmis un document anonyme."
        ),
        "dilemma": "Jusqu'où peux-tu aller contre Qiao Wen, la femme qui t'a élevée ?",
        "atelier": "Demande qui commande, quelle procédure s'applique et quel privilège peut ouvrir la porte.",
    },
    {
        "file": "04_sacha_miro.pdf",
        "image": "sacha_miro.png",
        "name": "SACHA MIRO",
        "role": "Pirate-journaliste — miroir sur pattes",
        "quote": "Si personne ne voulait que ça sorte, ça mérite probablement de sortir.",
        "accent": "#7B2D70",
        "visible": (
            "Ta veste est cousue de miroirs pliables et tu enregistres chaque conversation par politesse "
            "historique. Tu couvres le Salon pour le journal de l'école — officiellement."
        ),
        "stats": {"Force": 0, "Adresse": 3, "Technique": 1, "Science": 0, "Influence": 3, "Opticulture": 1},
        "signature": (
            "<b>PUBLICATION MIROIR — 1 fois, sans jet.</b> Envoie une preuve ou un message à une rédaction, "
            "une communauté ou une personne nommée avant son blocage. Sa portée dépend de la preuve."
        ),
        "burst": (
            "<b>SOURCE CONFIDENTIELLE — 1 Éclat.</b> Révèle un contact, une fréquence ou une information "
            "préparée avant la partie. Le MJ peut demander ce que tu as promis en échange."
        ),
        "lever": (
            "<b>LE LIBRE RAYON.</b> Ce petit réseau peut ouvrir une communication, détourner brièvement un "
            "signal existant ou fournir une information. Il ne peut rien créer ni couvrir toute la planète."
        ),
        "gear": "Caméra à dynamo ; veste à miroirs ; miroir télescopique ; fréquence pirate ; 3 faux badges ; enregistreur mécanique.",
        "secret": (
            "Le capitaine Miro est ton oncle. Iris t'a déjà transmis anonymement un document interne sans "
            "grand intérêt apparent. Tu as reconnu sa manière d'écrire, mais tu ne lui as jamais dit."
        ),
        "links": (
            "<b>Maëlle :</b> tu sais que son exploitation va mal. <b>Noé :</b> ton article lui a valu douze lecteurs. "
            "<b>Iris :</b> ta meilleure source et ton amie."
        ),
        "dilemma": "Jusqu'où exposeras-tu tes proches pour une vérité que personne ne lira peut-être ?",
        "atelier": "Conserve les preuves, choisis qui doit les recevoir et mesure le risque de leur publication.",
    },
    {
        "file": "05_celeste_azoulay.pdf",
        "image": "celeste_azoulay.png",
        "name": "CÉLESTE « PARALLAXE » AZOULAY",
        "role": "Astronome de terrain — cartographe orbitale",
        "quote": "Le ciel ne ment jamais. Les gens qui vendent ses cartes, davantage.",
        "accent": "#253E78",
        "visible": (
            "Tu portes un planisphère mécanique sur le dos et corriges les gens lorsqu'ils disent que le "
            "Soleil se lève. Tu présentes au Salon une conférence de 192 diapositives sur le guidage stellaire des loupes."
        ),
        "stats": {"Force": 0, "Adresse": 3, "Technique": 1, "Science": 3, "Influence": 0, "Opticulture": 1},
        "signature": (
            "<b>LE CIEL NE MENT PAS — 1 fois, sans jet.</b> Détermine la position, la direction ou la "
            "trajectoire d'un phénomène. Le MJ donne les mesures exactes ; sa cause reste à découvrir."
        ),
        "burst": (
            "<b>JE L'AVAIS PRÉDIT — 1 Éclat.</b> Révèle que tu avais prévu le phénomène et préparé "
            "l'instrument, la carte ou le calcul précisément utile."
        ),
        "lever": (
            "<b>LES COLLÈGUES DE L'OBSERVATOIRE.</b> Quelques astronomes peuvent confirmer une observation, "
            "compléter une carte ou effectuer un calcul, à partir de données observables et avec du temps."
        ),
        "gear": "Planisphère dorsal ; sextant ; lunettes à 6 filtres ; cartes papier ; mini-télescope ; craie et ficelle de calcul.",
        "secret": (
            "Certains régulateurs climatiques changent parfois d'orientation sans raison météorologique. "
            "Tu n'as pas de preuve : seulement des heures et des angles trop réguliers pour être accidentels."
        ),
        "links": (
            "<b>Maëlle :</b> ses loupes suivent tes cartes. <b>Noé :</b> il fabrique tes instruments. "
            "<b>Iris :</b> sa famille a refusé tes recherches. <b>Sacha :</b> il a publié ta théorie."
        ),
        "dilemma": "Que risques-tu pour prouver une anomalie que personne d'autre ne prend au sérieux ?",
        "atelier": "Mesure avant d'interpréter : position, durée, angle et répétition.",
    },
]


def styles(accent):
    return {
        "section": ParagraphStyle(
            "section",
            fontName="SunArial-Bold",
            fontSize=9.6,
            leading=11.2,
            textColor=accent,
            spaceBefore=3.2,
            spaceAfter=1.6,
        ),
        "body": ParagraphStyle(
            "body",
            fontName="SunArial",
            fontSize=8.8,
            leading=10.7,
            textColor=HexColor("#20252B"),
            alignment=TA_LEFT,
            spaceAfter=2.3,
        ),
        "small": ParagraphStyle(
            "small",
            fontName="SunArial",
            fontSize=8.1,
            leading=9.7,
            textColor=HexColor("#20252B"),
            spaceAfter=2,
        ),
        "quote": ParagraphStyle(
            "quote",
            fontName="SunArial-Italic",
            fontSize=10.8,
            leading=13,
            textColor=accent,
            alignment=TA_CENTER,
            spaceAfter=5,
        ),
        "secret": ParagraphStyle(
            "secret",
            fontName="SunArial",
            fontSize=8.3,
            leading=10,
            textColor=HexColor("#341D22"),
        ),
    }


def section(flow, sty, title, text, body_style="body"):
    flow.append(Paragraph(title.upper(), sty["section"]))
    flow.append(Paragraph(text, sty[body_style]))


def draw_character_page(c, char, page_number=None):
    width, height = A4
    accent = HexColor(char["accent"])
    pale = Color(accent.red, accent.green, accent.blue, alpha=0.10)
    sty = styles(accent)

    c.setFillColor(HexColor("#F7F4EC"))
    c.rect(0, 0, width, height, fill=1, stroke=0)

    c.setFillColor(accent)
    c.rect(0, height - 28 * mm, width, 28 * mm, fill=1, stroke=0)
    c.setFillColor(Color(1, 1, 1, alpha=0.09))
    c.circle(width - 15 * mm, height - 7 * mm, 25 * mm, fill=1, stroke=0)
    c.circle(width - 37 * mm, height - 22 * mm, 9 * mm, fill=1, stroke=0)

    c.setFillColor(white)
    c.setFont("SunArial-Bold", 18)
    c.drawString(9 * mm, height - 12 * mm, char["name"])
    c.setFont("SunArial", 9.2)
    c.drawString(9 * mm, height - 20 * mm, char["role"])

    left_x = 9 * mm
    left_w = 64 * mm
    right_x = 78 * mm
    right_w = width - right_x - 9 * mm
    portrait_h = 96 * mm
    portrait_y = height - 31 * mm - portrait_h

    c.setStrokeColor(accent)
    c.setLineWidth(1.2)
    c.rect(left_x - 0.6 * mm, portrait_y - 0.6 * mm, left_w + 1.2 * mm, portrait_h + 1.2 * mm, fill=0, stroke=1)
    c.drawImage(
        str(IMG_DIR / char["image"]),
        left_x,
        portrait_y,
        width=left_w,
        height=portrait_h,
        preserveAspectRatio=True,
        anchor="c",
        mask="auto",
    )

    left_flow = [Paragraph("DOMAINES", sty["section"])]
    stats_data = []
    stat_items = list(char["stats"].items())
    for idx in range(0, 6, 2):
        row = []
        for name, value in stat_items[idx : idx + 2]:
            row.extend([name, f"+{value}"])
        stats_data.append(row)
    table = Table(stats_data, colWidths=[22 * mm, 7 * mm, 22 * mm, 7 * mm], rowHeights=7.2 * mm)
    table.setStyle(
        TableStyle(
            [
                ("FONTNAME", (0, 0), (-1, -1), "SunArial"),
                ("FONTNAME", (1, 0), (1, -1), "SunArial-Bold"),
                ("FONTNAME", (3, 0), (3, -1), "SunArial-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 7.4),
                ("TEXTCOLOR", (1, 0), (1, -1), accent),
                ("TEXTCOLOR", (3, 0), (3, -1), accent),
                ("BACKGROUND", (0, 0), (-1, -1), HexColor("#ECE8DD")),
                ("BOX", (0, 0), (-1, -1), 0.35, accent),
                ("INNERGRID", (0, 0), (-1, -1), 0.25, HexColor("#CFC8B8")),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("ALIGN", (1, 0), (1, -1), "CENTER"),
                ("ALIGN", (3, 0), (3, -1), "CENTER"),
                ("LEFTPADDING", (0, 0), (-1, -1), 3),
                ("RIGHTPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    left_flow.extend([table, Spacer(1, 2.2 * mm)])
    section(left_flow, sty, "États", "□ Secoué·e &nbsp;&nbsp; □ Blessé·e<br/>□ Hors d'action", "small")
    section(left_flow, sty, "Éclat", "□ Éclat", "small")
    section(left_flow, sty, "Équipement", char["gear"], "small")
    notes_top = 88 * mm
    flow_bottom = notes_top + 4 * mm
    left_available_h = portrait_y - flow_bottom - 2 * mm
    kif_left = KeepInFrame(left_w, left_available_h, left_flow, mode="shrink", vAlign="TOP")
    _, left_content_h = kif_left.wrapOn(c, left_w, left_available_h)
    kif_left.drawOn(c, left_x, flow_bottom + left_available_h - left_content_h)

    right_flow = [Paragraph(f'« {char["quote"]} »', sty["quote"])]
    section(right_flow, sty, "Ce que les autres voient", char["visible"])
    section(right_flow, sty, "Capacité signature", char["signature"])
    section(right_flow, sty, "Coup d'Éclat", char["burst"])
    section(right_flow, sty, "Atout personnel", char["lever"])

    secret_title = Paragraph("TON SECRET — NE LE LIS PAS AUX AUTRES", sty["section"])
    secret_text = Paragraph(char["secret"], sty["secret"])
    secret_table = Table([[secret_title], [secret_text]], colWidths=[right_w - 4 * mm])
    secret_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), pale),
                ("BOX", (0, 0), (-1, -1), 0.7, accent),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    right_flow.extend([secret_table, Spacer(1, 2 * mm)])
    section(right_flow, sty, "Liens", char["links"], "small")
    section(right_flow, sty, "Dilemme", f'<b>{char["dilemma"]}</b>')
    section(right_flow, sty, "Ta façon d'agir", char["atelier"])

    right_y = flow_bottom
    right_h = height - 31 * mm - right_y
    kif_right = KeepInFrame(right_w, right_h, right_flow, mode="shrink", vAlign="TOP")
    _, right_content_h = kif_right.wrapOn(c, right_w, right_h)
    kif_right.drawOn(c, right_x, right_y + right_h - right_content_h)

    notes_x = 9 * mm
    notes_y = 13 * mm
    notes_w = width - 18 * mm
    notes_h = 72 * mm
    c.setFillColor(Color(accent.red, accent.green, accent.blue, alpha=0.035))
    c.setStrokeColor(accent)
    c.setLineWidth(0.6)
    c.roundRect(notes_x, notes_y, notes_w, notes_h, 2 * mm, fill=1, stroke=1)
    c.setFillColor(accent)
    c.setFont("SunArial-Bold", 8.5)
    c.drawString(notes_x + 4 * mm, notes_y + notes_h - 7 * mm, "NOTES DE PARTIE")
    c.setStrokeColor(Color(accent.red, accent.green, accent.blue, alpha=0.30))
    for line_idx in range(1, 8):
        line_y = notes_y + notes_h - (7 + line_idx * 8) * mm
        c.line(notes_x + 4 * mm, line_y, notes_x + notes_w - 4 * mm, line_y)

    c.setStrokeColor(accent)
    c.setLineWidth(0.5)
    c.line(9 * mm, 7 * mm, width - 9 * mm, 7 * mm)
    c.setFillColor(HexColor("#555A60"))
    c.setFont("SunArial", 6.5)
    footer = "LA GUERRE DE L'ÉTOILE — FICHE JOUEUR — 1 PAGE A4"
    c.drawString(9 * mm, 3.7 * mm, footer)
    if page_number is not None:
        c.drawRightString(width - 9 * mm, 3.7 * mm, f"{page_number}/5")


def generate_individual(char):
    path = OUT_DIR / char["file"]
    c = canvas.Canvas(str(path), pagesize=A4, pageCompression=1)
    c.setTitle(f"La Guerre de l'Étoile — {char['name']}")
    draw_character_page(c, char)
    c.showPage()
    c.save()


def generate_booklet():
    path = OUT_DIR / "00_fiches_personnages_complet.pdf"
    c = canvas.Canvas(str(path), pagesize=A4, pageCompression=1)
    c.setTitle("La Guerre de l'Étoile — Fiches personnages")
    for idx, char in enumerate(CHARACTERS, start=1):
        draw_character_page(c, char, idx)
        c.showPage()
    c.save()


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for char in CHARACTERS:
        generate_individual(char)
    generate_booklet()
    print(f"Généré : {len(CHARACTERS)} fiches individuelles + 1 recueil dans {OUT_DIR}")


if __name__ == "__main__":
    main()
