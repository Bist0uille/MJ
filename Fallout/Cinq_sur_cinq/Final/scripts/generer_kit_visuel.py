from pathlib import Path
import html
import re

from PIL import Image as PILImage
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.platypus import KeepInFrame, Paragraph, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "pdf"
CHAR_PDF = PDF / "fiches_personnages"
FONT_DIR = Path(r"C:\Windows\Fonts")

pdfmetrics.registerFont(TTFont("CinqArial", FONT_DIR / "arial.ttf"))
pdfmetrics.registerFont(TTFont("CinqArial-Bold", FONT_DIR / "arialbd.ttf"))
pdfmetrics.registerFont(TTFont("CinqArial-Italic", FONT_DIR / "ariali.ttf"))

CHARACTERS = [
    ("01_ZORA_FUSIBLE_VALE.md", "zora_fusible_vale.png"),
    ("02_ANATOLE_TROIS_MURS_DUROC.md", "anatole_trois_murs_duroc.png"),
    ("03_NELL_DEUX_COUPS_RAINER.md", "nell_deux_coups_rainer.png"),
    ("04_DR_LAZARE_BONBON_MIETTE.md", "dr_lazare_bonbon_miette.png"),
    ("05_ROOK_TOUT_DOUX.md", "rook_tout_doux.png"),
]

CHARACTER_CARDS = {
    "01_ZORA_FUSIBLE_VALE.md": {
        "code": "ROB-61/FUSIBLE", "role": "MÉCANO ET BIDOUILLEUSE ROBOTIQUE", "armor": "1 / 1",
        "traits": ["Elle parle aux machines comme à des personnes.", "Elle est curieuse avant d’être prudente.", "Elle plaisante dès qu’elle culpabilise."],
        "quote": "« Chut. Elle essaie de nous dire quelque chose. »",
        "past": "Elle a quitté l’Abri 61 après avoir accidentellement poussé un robot matrimonial à épouser tous les grille-pain.",
        "goal": "Trouver une invention digne de son talent.",
        "secret": "Son Pip-Boy Gérard fonctionne grâce à une pièce volée au superviseur de son Abri.",
        "gear": ["Bernadette — laser, 4 dés de dégâts, 18 charges", "Pip-Boy Gérard + holotape RobCo périmée", "Trousse de précision + multimètre", "Consignation électrique + bobine de cuivre", "Grenade à impulsion artisanale", "1 stimpak + 2 cellules à fusion"],
        "moves": ["Reconnaître l’usage et l’état d’un système RobCo.", "Sécuriser ou contourner un circuit.", "Parler technique avec un robot pour le faire hésiter."],
        "question": "Est-ce que tout ce qui est cassé mérite d’être réparé ?",
    },
    "02_ANATOLE_TROIS_MURS_DUROC.md": {
        "code": "CHANTIER-2074/3M", "role": "GOULE, DÉMOLISSEUR ET OUVREUR DE ROUTE", "armor": "2 / 1",
        "traits": ["Il mesure les problèmes en coups de masse.", "Il râle, mais reste toujours le premier à aider.", "Il raconte ses erreurs de chantier comme des victoires tactiques."],
        "quote": "« Une porte fermée, c’est un mur qui manque d’ambition. »",
        "past": "Avant la Guerre, Anatole sécurisait les chantiers qui avaient déjà mal tourné. Depuis, il déplace ce qui refuse de bouger.",
        "goal": "Garder le groupe ensemble et toujours laisser un chemin de retour.",
        "secret": "Il a gagné son surnom en abattant trois mauvais murs parce qu’il lisait le plan à l’envers.",
        "gear": ["La Délicatesse — masse, 5 dés de dégâts", "Pied-de-biche, marteau et burin", "3 coins de porte en acier", "Corde de 15 m + poulie manuelle", "Craies, sangles + lampe de casque", "Compteur Geiger + 1 Rad-X + 1 stimpak"],
        "moves": ["Caler, retenir ou forcer une porte repérée.", "Installer une corde ou un point d’appui.", "Protéger un allié qui manipule un mécanisme dangereux."],
        "question": "Quand un lieu enferme des gens, faut-il encore le réparer ?",
    },
    "03_NELL_DEUX_COUPS_RAINER.md": {
        "code": "ÉCLAIREUR/2-COUPS", "role": "ÉCLAIREUSE ET SPÉCIALISTE DES SORTIES", "armor": "2 / 2",
        "traits": ["Elle repère les sorties avant de dire bonjour.", "Elle est pragmatique et sèche, jamais cruelle gratuitement.", "Elle ne s’assoit jamais dos à une porte."],
        "quote": "« Je vous avais dit de garder une sortie. »",
        "past": "Elle guide les convois dangereux et collectionne quarante-sept clés inutiles, certaine que l’une finira par servir.",
        "goal": "Garder le groupe vivant, quoi qu’il arrive.",
        "secret": "Elle a abandonné son frère blessé pour sauver un convoi.",
        "gear": ["Premier Avis — carabine, 5 dés de dégâts", "Dernier Avis — 10 mm, 4 dés de dégâts", "47 clés + nécessaire de crochetage", "Miroir télescopique + caméra à câble", "Corde de 20 m + grappin", "2 fumigènes + 1 Rad-X + 1 stimpak"],
        "moves": ["Repérer une sortie réellement praticable.", "Observer une pièce dangereuse sans y entrer.", "Préparer un itinéraire sûr pour tout le groupe."],
        "question": "Peut-on abandonner quelqu’un pour sauver tout le groupe ?",
    },
    "04_DR_LAZARE_BONBON_MIETTE.md": {
        "code": "MÉDICAL/BONBON", "role": "MÉDECIN DE TERRAIN BEAUCOUP TROP AIMABLE", "armor": "1 / 1",
        "traits": ["Il commence chaque diagnostic par la bonne nouvelle.", "Il demande toujours la permission avant de soigner.", "Il donne un bonbon même aux cadavres."],
        "quote": "« La bonne nouvelle, c’est que vous êtes encore vivant. »",
        "past": "Il soigne tout ce qui respire — et reste professionnel avec ce qui ne respire plus.",
        "goal": "Soigner le groupe sans décider à la place des blessés.",
        "secret": "Son titre de docteur est inventé : il a appris dans des manuels et sur le terrain.",
        "gear": ["Pistolet 9 mm, 3 dés de dégâts", "Sac médical + scanner de diagnostic", "3 stimpaks + 2 Rad-X + 1 RadAway", "Antidote large spectre + charbon actif", "Oxygène portable + 2 masques", "23 bonbons, dont un “urgence absolue”"],
        "moves": ["Identifier sans jet une cause médicale visible.", "Fabriquer un antidote ou une réserve d’air.", "Signaler qu’un traitement est dangereux pour le patient."],
        "question": "Soigner sans consentement, est-ce déjà faire violence ?",
    },
    "05_ROOK_TOUT_DOUX.md": {
        "code": "MUTANT/TOUT-DOUX", "role": "PROTECTEUR, PORTEUR ET EXPERT EN POLITESSE", "armor": "3 / 2",
        "traits": ["Il chuchote pour ne pas effrayer les humains.", "Il dit pardon avant d’enfoncer une porte.", "Il protège d’abord et réfléchit ensuite."],
        "quote": "« Pardon. Je vais devoir casser la porte. »",
        "past": "Ce géant applique très sérieusement les conseils du Parfait petit hôte, un manuel pour enfants trouvé dans un hôtel en ruine.",
        "goal": "Veiller sur le groupe sans lui donner d’ordres.",
        "secret": "Il sait à peine lire : il connaît douze pages par cœur et invente tout le reste.",
        "gear": ["S’il-vous-plaît — masse, 6 dés de dégâts", "Chaîne de 5 m + gros mousquetons", "Cale de voie ferrée", "Couverture anti-feu + extincteur", "Masque filtrant à sa taille", "Sac de portage + 2 stimpaks + 3 eaux"],
        "moves": ["Prendre à la place d’un allié les dégâts d’une attaque, une fois par scène.", "Forcer ou retenir une porte.", "Porter deux personnes pendant une évacuation."],
        "question": "Protéger, est-ce décider à la place de l’autre ?",
    },
}

ROBOT_DATA = [
    ("MONSIEUR HECTOR", "Majordome — l'étiquette avant l'apocalypse", "monsieur_hector.png"),
    ("MADEMOISELLE BONREPOS", "Infirmière — le repos est obligatoire", "mademoiselle_bonrepos.png"),
    ("CLOVIS BOULON-13", "Maintenance — toute catastrophe exige un formulaire", "clovis_boulon_13.png"),
    ("COLONEL BASILISK", "Sécurité — chaque couloir est un front", "colonel_basilisk.png"),
]

STORYBOARD = [
    ("0:00 — LA TEMPÊTE", "Exactement cinq voyageurs entrent. Au passage du dernier, la porte se verrouille et le piano joue quatre notes.", "01_arrivee_manoir.png"),
    ("0:30 — ABEL", "La coupure était correcte. Une autorité inconnue a rétabli le courant. Faire immédiatement rejouer le danger.", "02_abel_generateur.png"),
    ("1:10 — EVELYN", "Bracelet, injection et registre convergent. Bonrepos croit encore avoir réussi son soin.", "03_evelyn_bonrepos.png"),
    ("1:50 — RICHARD", "Les masques, la corde et les couvertures prouvent qu'il préparait une sortie collective.", "04_richard_quarantaine.png"),
    ("2:30 — HARMONY™", "Une corde manque. Les quatre notes n'ont aucun effet et les robots poursuivent leurs tâches.", "05_piano_harmony.png"),
    ("3:20 — LE CŒUR", "Claire est morte près du levier. Les heures complètes révèlent enfin SALI et innocentent l'ingénieure.", "06_coeur_sali.png"),
]

BODY = ParagraphStyle("body", fontName="CinqArial", fontSize=8.1, leading=9.7, textColor=HexColor("#181818"))
SMALL = ParagraphStyle("small", parent=BODY, fontSize=7.3, leading=8.6)
SECTION = ParagraphStyle("section", fontName="CinqArial-Bold", fontSize=8.8, leading=10, textColor=HexColor("#111111"), spaceBefore=2, spaceAfter=2)
TITLE = ParagraphStyle("title", fontName="CinqArial-Bold", fontSize=15, leading=17, textColor=HexColor("#111111"))
SUB = ParagraphStyle("sub", fontName="CinqArial", fontSize=8.5, leading=10, textColor=HexColor("#333333"))
MONO = ParagraphStyle("mono", fontName="Courier", fontSize=8.2, leading=10, textColor=HexColor("#111111"))
ACCESSORY_TITLE = ParagraphStyle("accessory-title", fontName="CinqArial-Bold", fontSize=6.6, leading=7.2,
                                 textColor=HexColor("#111111"), spaceBefore=0, spaceAfter=1)
ACCESSORY_BODY = ParagraphStyle("accessory-body", fontName="Courier", fontSize=6.0, leading=6.8,
                                textColor=HexColor("#111111"))


def inline(text):
    safe = html.escape(text.strip())
    safe = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", safe)
    safe = re.sub(r"\*(.+?)\*", r"<i>\1</i>", safe)
    return safe


def parse_character(path):
    text = path.read_text(encoding="utf-8")
    title = re.search(r"^# (.+)$", text, flags=re.MULTILINE).group(1)
    split = re.split(r"^## (.+)$", text, flags=re.MULTILINE)
    intro = split[0].splitlines()[1:]
    sections = {split[i].strip(): split[i + 1].strip() for i in range(1, len(split), 2)}
    metadata = "<br/>".join(inline(line) for line in intro if line.strip())
    if " — " in title:
        name, role = title.split(" — ", 1)
    else:
        name, role = title, ""
    return {"name": name, "role": role, "metadata": metadata, "sections": sections}


def flow_for_section(label, content, style=BODY):
    flow = [Paragraph(label.upper(), SECTION)]
    paragraphs = []
    current = []
    for line in content.splitlines():
        stripped = line.strip()
        if not stripped:
            if current:
                paragraphs.append(" ".join(current))
                current = []
            continue
        if stripped.startswith("- "):
            if current:
                paragraphs.append(" ".join(current))
                current = []
            paragraphs.append("• " + stripped[2:])
        else:
            current.append(stripped)
    if current:
        paragraphs.append(" ".join(current))
    for para in paragraphs:
        flow.append(Paragraph(inline(para), style))
        flow.append(Spacer(1, 1.2 * mm))
    return flow


def draw_frame(c, x, y, w, h, width=0.65):
    c.setStrokeColor(HexColor("#333333"))
    c.setLineWidth(width)
    c.rect(x, y, w, h, fill=0, stroke=1)


def draw_flow(c, x, y, w, h, flow):
    kif = KeepInFrame(w, h, flow, mode="shrink", vAlign="TOP")
    _, used = kif.wrapOn(c, w, h)
    kif.drawOn(c, x, y + h - used)


def portrait_reader(path, grayscale=False):
    if not grayscale:
        return str(path)
    image = PILImage.open(path).convert("L").convert("RGB")
    return ImageReader(image)


def parse_profile(md_name):
    raw = (ROOT / "fiches_personnages" / md_name).read_text(encoding="utf-8")
    plain = raw.replace("**", "")
    lines = [line.strip() for line in plain.splitlines()]
    special_line = next(line for line in lines if re.match(r"^S\s+\d+", line))
    special = re.findall(r"\b([SPECIAlL])\s+(\d+)", special_line, flags=re.IGNORECASE)
    derived_line = next(line for line in lines if re.match(r"^PV\s+\d+", line))
    derived = {key: value for key, value in re.findall(r"(PV|Initiative|Défense)\s+(\d+)", derived_line)}
    specialty_line = next((line.split(":", 1)[1].strip() for line in lines if line.startswith("Spécialités")), None)
    if specialty_line is not None:
        specialty_skills = [item.strip().rstrip(".") + " TAG" for item in specialty_line.split(",")]
        ordinary_line = next(line.split(":", 1)[1].strip() for line in lines if line.startswith("Autres compétences"))
        skills = specialty_skills + [item.strip().rstrip(".") for item in ordinary_line.split(",")]
    else:
        skill_line = next(line.split(":", 1)[1].strip() for line in lines if line.startswith("Compétences"))
        skills = [item.strip().rstrip(".") for item in skill_line.split(",")]
    perk_line = next(line.split(":", 1)[1].strip() for line in lines if line.startswith("Atouts")).rstrip(".")
    perks = [item.strip() for item in perk_line.split(";")]
    return special, derived, skills, perks


def simple_box(c, x, y, w, h, label, accent, fill=None):
    if fill is not None:
        c.setFillColor(fill)
        c.rect(x, y, w, h, fill=1, stroke=0)
    c.setStrokeColor(accent)
    c.setLineWidth(0.85)
    c.rect(x, y, w, h, fill=0, stroke=1)
    c.setFillColor(accent)
    c.setFont("Courier-Bold", 6.4)
    c.drawString(x + 2.5 * mm, y + h - 4.2 * mm, label)


def bullet_flow(items, size=8.2, leading=10):
    style = ParagraphStyle("card-bullets", fontName="CinqArial", fontSize=size, leading=leading,
                           textColor=HexColor("#151815"), leftIndent=0, firstLineIndent=0)
    return [Paragraph("• " + html.escape(item), style) for item in items]


def draw_para(c, paragraph, x, y, w, h):
    paragraph.wrapOn(c, w, h)
    paragraph.drawOn(c, x, y)


def draw_character_page(c, md_name, image_name, grayscale=False, page_no=None):
    width, height = A4
    data = parse_character(ROOT / "fiches_personnages" / md_name)
    card = CHARACTER_CARDS[md_name]
    special, derived, skills, perks = parse_profile(md_name)
    image_path = ROOT / "images" / "personnages" / image_name
    accent = HexColor("#202820") if grayscale else HexColor("#496B35")
    pale = HexColor("#F2F2F2") if grayscale else HexColor("#F2F6E8")
    dark = HexColor("#131713")
    c.setFillColor(white)
    c.rect(0, 0, width, height, fill=1, stroke=0)

    # Fallout/Pip-Boy inspired header: terminal typography, registration code,
    # angular corners and restrained olive accents remain cheap to print.
    c.setFillColor(accent)
    c.rect(9 * mm, height - 15 * mm, width - 18 * mm, 6 * mm, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Courier-Bold", 7.2)
    c.drawString(12 * mm, height - 12.7 * mm, "VAULT-TEC // DOSSIER DE SURVIE // CINQ SUR CINQ")
    c.drawRightString(width - 12 * mm, height - 12.7 * mm, card["code"])
    c.setFillColor(dark)
    c.setFont("CinqArial-Bold", 17)
    c.drawString(10 * mm, height - 25 * mm, data["name"])
    c.setFont("Courier-Bold", 7.6)
    c.setFillColor(accent)
    c.drawString(10 * mm, height - 31 * mm, card["role"])
    c.drawRightString(width - 10 * mm, height - 25 * mm, "NIVEAU 04")
    c.setLineWidth(1.2)
    c.line(10 * mm, height - 34 * mm, width - 10 * mm, height - 34 * mm)

    portrait_x, portrait_y, portrait_w, portrait_h = 9 * mm, 153 * mm, 59 * mm, 105 * mm
    simple_box(c, portrait_x, portrait_y, portrait_w, portrait_h, "IDENTIFICATION VISUELLE", accent)
    c.drawImage(portrait_reader(image_path, grayscale), portrait_x + 1.2 * mm, portrait_y + 1.2 * mm,
                width=portrait_w - 2.4 * mm, height=portrait_h - 8 * mm,
                preserveAspectRatio=True, anchor="c", mask="auto")

    # Personality is the first thing the player reads.
    right_x, right_w = 72 * mm, 129 * mm
    simple_box(c, right_x, 202 * mm, right_w, 56 * mm, "PERSONNALITÉ // JOUE-LE COMME ÇA", accent, pale)
    draw_flow(c, right_x + 4 * mm, 207 * mm, right_w - 8 * mm, 42 * mm,
              bullet_flow(card["traits"], 9.1, 11.4) + [Spacer(1, 2 * mm),
              Paragraph(f"<b>{html.escape(card['quote'])}</b>", ParagraphStyle("quote-card", parent=BODY, fontSize=9, leading=11, textColor=accent))])

    # Seven discrete SPECIAL counters.
    simple_box(c, right_x, 163 * mm, right_w, 35 * mm, "SPECIAL", accent)
    cell_w = 15.6 * mm
    gap = 2 * mm
    sx = right_x + 4 * mm
    for idx, (letter, value) in enumerate(special):
        bx = sx + idx * (cell_w + gap)
        c.setStrokeColor(accent)
        c.setLineWidth(0.8)
        c.roundRect(bx, 168 * mm, cell_w, 20 * mm, 2 * mm, fill=0, stroke=1)
        c.setFillColor(accent)
        c.setFont("Courier-Bold", 9)
        c.drawCentredString(bx + cell_w / 2, 181.5 * mm, letter.upper())
        c.setFont("CinqArial-Bold", 15)
        c.drawCentredString(bx + cell_w / 2, 171.5 * mm, value)

    # Derived statistics are three independent counters, never a paragraph.
    labels = [("PV", derived["PV"]), ("INITIATIVE", derived["Initiative"]),
              ("DÉFENSE", derived["Défense"]), ("ARMURE PHY / ÉNER", card["armor"])]
    stat_w = 30 * mm
    for idx, (label, value) in enumerate(labels):
        bx = right_x + idx * (stat_w + 3 * mm)
        simple_box(c, bx, 145 * mm, stat_w, 14 * mm, label, accent, pale)
        c.setFillColor(dark)
        c.setFont("CinqArial-Bold", 13)
        c.drawRightString(bx + stat_w - 3 * mm, 149 * mm, value)

    # Three specialties first, then the ordinary skills. No unexplained TAG jargon.
    simple_box(c, right_x, 100 * mm, right_w, 41 * mm, "COMPÉTENCES", accent)
    specialties = [re.sub(r"\s+TAG$", "", skill) for skill in skills if skill.endswith("TAG")]
    ordinary = [skill for skill in skills if not skill.endswith("TAG")]
    c.setFillColor(accent)
    c.setFont("Courier-Bold", 6.2)
    c.drawString(right_x + 4 * mm, 133.5 * mm, "SPÉCIALITÉS // D20 INFÉRIEUR OU ÉGAL AU SCORE = 2 RÉUSSITES")
    spec_w = 38 * mm
    for idx, skill in enumerate(specialties):
        match = re.match(r"(.+?)\s+(\d+)$", skill)
        name, value = match.groups()
        bx = right_x + (4 + idx * 41) * mm
        c.setFillColor(pale)
        c.setStrokeColor(accent)
        c.roundRect(bx, 119 * mm, spec_w, 11 * mm, 1.5 * mm, fill=1, stroke=1)
        c.setFillColor(dark)
        c.setFont("CinqArial-Bold", 7.2)
        c.drawString(bx + 2 * mm, 123 * mm, name.upper())
        c.setFont("CinqArial-Bold", 11)
        c.drawRightString(bx + spec_w - 2 * mm, 122 * mm, value)
    c.setFillColor(accent)
    c.setFont("Courier-Bold", 6.2)
    c.drawString(right_x + 4 * mm, 114.5 * mm, "AUTRES")
    ordinary_text = "     ".join(ordinary)
    draw_para(c, Paragraph(html.escape(ordinary_text), ParagraphStyle("ordinary-skills", fontName="CinqArial", fontSize=7.4, leading=8, textColor=dark)),
              right_x + 22 * mm, 112.5 * mm, right_w - 26 * mm, 7 * mm)
    c.setStrokeColor(accent)
    c.line(right_x + 4 * mm, 109 * mm, right_x + right_w - 4 * mm, 109 * mm)
    perk_text = "ATOUTS  //  " + "  •  ".join(perks)
    draw_para(c, Paragraph(html.escape(perk_text), ParagraphStyle("perks", fontName="Courier-Bold", fontSize=6.8, leading=8, textColor=accent)),
              right_x + 4 * mm, 102.5 * mm, right_w - 8 * mm, 7 * mm)

    # The rest is deliberately terse: one glance, one play hook.
    simple_box(c, 9 * mm, 116 * mm, 59 * mm, 33 * mm, "PARCOURS", accent)
    draw_flow(c, 12 * mm, 120 * mm, 53 * mm, 21 * mm, [Paragraph(html.escape(card["past"]), SMALL)])
    simple_box(c, 9 * mm, 78 * mm, 59 * mm, 34 * mm, "OBJECTIF", accent, pale)
    draw_flow(c, 12 * mm, 82 * mm, 53 * mm, 21 * mm, [Paragraph(html.escape(card["goal"]), BODY)])
    simple_box(c, 9 * mm, 39 * mm, 59 * mm, 35 * mm, "SECRET", accent)
    draw_flow(c, 12 * mm, 43 * mm, 53 * mm, 22 * mm, [Paragraph(html.escape(card["secret"]), SMALL)])

    simple_box(c, right_x, 49 * mm, right_w, 47 * mm, "ÉQUIPEMENT UTILE", accent)
    inv_style = ParagraphStyle("inventory-card", fontName="CinqArial", fontSize=7.6, leading=9, textColor=dark)
    for idx, item in enumerate(card["gear"]):
        col = idx % 2
        row = idx // 2
        draw_para(c, Paragraph("— " + html.escape(item), inv_style),
                  right_x + (4 + col * 63) * mm, (82 - row * 10.5) * mm, 59 * mm, 9 * mm)

    simple_box(c, right_x, 17 * mm, right_w, 28 * mm, "TES 3 COUPS DE POUCE", accent, pale)
    draw_flow(c, right_x + 4 * mm, 20 * mm, right_w - 8 * mm, 18 * mm, bullet_flow(card["moves"], 7.7, 9))
    simple_box(c, 9 * mm, 17 * mm, 59 * mm, 18 * mm, "DILEMME", accent, pale)
    draw_flow(c, 12 * mm, 19 * mm, 53 * mm, 10 * mm,
              [Paragraph(html.escape(card["question"]), ParagraphStyle("dilemma", parent=SMALL, fontSize=6.9, leading=8))])

    c.setStrokeColor(accent)
    c.setLineWidth(0.35)
    c.line(9 * mm, 13 * mm, width - 9 * mm, 13 * mm)
    c.setFillColor(accent)
    c.setFont("Courier", 6.5)
    c.setFont("Courier", 5.9)
    c.drawString(9 * mm, 10 * mm, "SPÉCIALITÉ : D20 INFÉRIEUR OU ÉGAL AU SCORE = 2 RÉUSSITES")
    c.drawString(9 * mm, 7 * mm, "DÉ DE DÉGÂTS : 1 = 1 DÉGÂT ; 2 = 2 DÉGÂTS ; 3-4 = 0 ; 5-6 = 1 DÉGÂT + EFFET")
    c.drawString(9 * mm, 4 * mm, "TENSION PERSONNELLE  [ ] [ ] [ ] [ ]     PA DU GROUPE  [ ] [ ] [ ]")
    if page_no:
        c.drawRightString(width - 9 * mm, 4 * mm, f"DOSSIER {page_no}/5")


def generate_character_sheets():
    PDF.mkdir(parents=True, exist_ok=True)
    combined_nb = canvas.Canvas(str(PDF / "10_FICHES_PERSONNAGES_NB.pdf"), pagesize=A4, pageCompression=1)
    combined_nb.setTitle("Cinq sur cinq — cinq prétirés — impression N&B")
    for idx, (md_name, image_name) in enumerate(CHARACTERS, 1):
        draw_character_page(combined_nb, md_name, image_name, True, idx)
        combined_nb.showPage()
    combined_nb.save()


def generate_robot_book():
    out = canvas.Canvas(str(PDF / "03B_PORTRAITS_ROBOTS.pdf"), pagesize=A4, pageCompression=1)
    width, height = A4
    for idx, (name, subtitle, filename) in enumerate(ROBOT_DATA, 1):
        out.setFillColor(white)
        out.rect(0, 0, width, height, fill=1, stroke=0)
        out.setFont("Courier-Bold", 8)
        out.setFillColor(HexColor("#111111"))
        out.drawString(12 * mm, height - 10 * mm, "ROBCO DOMESTIC STAFF // IDENTIFICATION")
        out.setStrokeColor(HexColor("#222222"))
        out.line(12 * mm, height - 13 * mm, width - 12 * mm, height - 13 * mm)
        image_path = ROOT / "images" / "robots" / filename
        out.drawImage(str(image_path), 22 * mm, 43 * mm, width=width - 44 * mm, height=height - 66 * mm,
                      preserveAspectRatio=True, anchor="c", mask="auto")
        out.setFont("CinqArial-Bold", 17)
        out.drawCentredString(width / 2, 31 * mm, name)
        out.setFont("CinqArial-Italic", 9.5)
        out.drawCentredString(width / 2, 24 * mm, subtitle)
        out.setFont("Courier", 6.5)
        out.drawRightString(width - 12 * mm, 7 * mm, f"{idx}/4")
        out.showPage()
    out.save()


def generate_storyboard():
    page_size = landscape(A4)
    out = canvas.Canvas(str(PDF / "02B_STORYBOARD_ILLUSTRE.pdf"), pagesize=page_size, pageCompression=1)
    width, height = page_size
    for page_idx in range(3):
        out.setFillColor(white)
        out.rect(0, 0, width, height, fill=1, stroke=0)
        out.setFont("Courier-Bold", 9)
        out.setFillColor(HexColor("#111111"))
        out.drawString(10 * mm, height - 9 * mm, "CINQ SUR CINQ // STORYBOARD MJ ILLUSTRÉ")
        out.setStrokeColor(HexColor("#222222"))
        out.line(10 * mm, height - 12 * mm, width - 10 * mm, height - 12 * mm)
        for col in range(2):
            title, caption, filename = STORYBOARD[page_idx * 2 + col]
            x = 10 * mm + col * 143 * mm
            y = 33 * mm
            w = 134 * mm
            h = 145 * mm
            draw_frame(out, x, y, w, h)
            out.drawImage(str(ROOT / "images" / "storyboard" / filename), x + 2 * mm, y + 37 * mm,
                          width=w - 4 * mm, height=h - 41 * mm, preserveAspectRatio=True, anchor="c", mask="auto")
            draw_flow(out, x + 4 * mm, y + 5 * mm, w - 8 * mm, 29 * mm,
                      [Paragraph(title, SECTION), Paragraph(caption, SMALL)])
        out.setFont("Courier", 6.5)
        out.drawRightString(width - 10 * mm, 7 * mm, f"{page_idx + 1}/3")
        out.showPage()
    out.save()


def split_accessories():
    text = (ROOT / "08_ACCESSOIRES_A_IMPRIMER.md").read_text(encoding="utf-8")
    chunks = re.split(r"^# (\d+ — .+)$", text, flags=re.MULTILINE)
    cards = []
    for i in range(1, len(chunks), 2):
        title = chunks[i].strip()
        body = chunks[i + 1].strip()
        if title.startswith("19 —"):
            sub = re.split(r"^## (.+)$", body, flags=re.MULTILINE)
            for j in range(1, len(sub), 2):
                cards.append((f"CARTE DE RÔLE — {sub[j].strip()}", sub[j + 1].strip(), False))
        elif title.startswith("20 —"):
            cards.append((title, body, False))
        else:
            cards.append((title, body, False))
    return cards


def clean_accessory_body(body):
    lines = []
    for line in body.splitlines():
        stripped = line.strip()
        if stripped in {"```", "```text", "---"}:
            continue
        stripped = stripped.lstrip("> ")
        stripped = re.sub(r"^##+\s*", "", stripped)
        stripped = stripped.replace("**", "").replace("`", "")
        if stripped:
            lines.append(stripped)
    return "<br/>".join(html.escape(line) for line in lines)


def draw_accessory_card(c, x, y, w, h, title, body):
    draw_frame(c, x, y, w, h, 0.9)
    c.setFillColor(HexColor("#111111"))
    c.setFont("Courier-Bold", 4.3)
    c.drawString(x + 2.5 * mm, y + h - 4 * mm, "ROBCO ARCHIVE // DOCUMENT DE TABLE")
    c.setStrokeColor(HexColor("#555555"))
    c.line(x + 2.5 * mm, y + h - 5.5 * mm, x + w - 2.5 * mm, y + h - 5.5 * mm)
    for rx in (x + 2 * mm, x + w - 2 * mm):
        for ry in (y + 2 * mm, y + h - 2 * mm):
            c.circle(rx, ry, 0.7 * mm, fill=0, stroke=1)
    flow = [Paragraph(title, ACCESSORY_TITLE), Spacer(1, 0.5 * mm),
            Paragraph(clean_accessory_body(body), ACCESSORY_BODY)]
    draw_flow(c, x + 2.5 * mm, y + 2.5 * mm, w - 5 * mm, h - 9.5 * mm, flow)


def generate_accessories():
    cards = split_accessories()
    out = canvas.Canvas(str(PDF / "08_ACCESSOIRES_MIS_EN_PAGE.pdf"), pagesize=A4, pageCompression=1)
    width, height = A4
    margin = 8 * mm
    gap_x = 4 * mm
    gap_y = 3 * mm
    card_w = (width - 2 * margin - gap_x) / 2
    card_h = (height - 2 * margin - 3 * gap_y) / 4
    slot = 0
    for title, body, full_page in cards:
        if full_page:
            if slot:
                out.showPage()
                slot = 0
            out.setFillColor(white)
            out.rect(0, 0, width, height, fill=1, stroke=0)
            draw_accessory_card(out, margin, margin, width - 2 * margin, height - 2 * margin, title, body)
            out.showPage()
            continue
        if slot == 0:
            out.setFillColor(white)
            out.rect(0, 0, width, height, fill=1, stroke=0)
        col = slot % 2
        row = slot // 2
        x = margin + col * (card_w + gap_x)
        y = height - margin - card_h - row * (card_h + gap_y)
        draw_accessory_card(out, x, y, card_w, card_h, title, body)
        slot += 1
        if slot == 8:
            out.showPage()
            slot = 0
    if slot:
        out.showPage()
    out.save()


def main():
    PDF.mkdir(parents=True, exist_ok=True)
    generate_character_sheets()
    generate_accessories()
    print("Kit visuel généré : fiches N&B et accessoires actifs.")


if __name__ == "__main__":
    main()
