from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "page_5_fond_sans_texte.png"
OUTPUT = ROOT / "page_5_test_hybride_fr.png"

GEORGIA = r"C:\Windows\Fonts\georgia.ttf"
GEORGIA_BOLD = r"C:\Windows\Fonts\georgiab.ttf"
GEORGIA_ITALIC = r"C:\Windows\Fonts\georgiai.ttf"
ARIAL_BOLD = r"C:\Windows\Fonts\arialbd.ttf"

BROWN = (65, 43, 31)
BLUE = (30, 77, 145)
RED = (206, 30, 38)
BLACK = (28, 26, 24)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_width):
    paragraphs = text.split("\n")
    lines = []
    for paragraph in paragraphs:
        if not paragraph:
            lines.append("")
            continue
        words = paragraph.split()
        current = words[0]
        for word in words[1:]:
            trial = current + " " + word
            if draw.textlength(trial, font=fnt) <= max_width:
                current = trial
            else:
                lines.append(current)
                current = word
        lines.append(current)
    return lines


def draw_box(draw, box, text, font_path, max_size, min_size=10, fill=BLACK,
             spacing_ratio=0.24, align="left"):
    x0, y0, x1, y1 = box
    for size in range(max_size, min_size - 1, -1):
        fnt = font(font_path, size)
        lines = wrap(draw, text, fnt, x1 - x0)
        spacing = max(2, int(size * spacing_ratio))
        line_height = fnt.getbbox("Ag")[3] - fnt.getbbox("Ag")[1]
        total = len(lines) * line_height + max(0, len(lines) - 1) * spacing
        if total <= y1 - y0:
            draw.multiline_text((x0, y0), "\n".join(lines), font=fnt, fill=fill,
                                spacing=spacing, align=align)
            return size
    return min_size


def label(draw, xy, text, anchor="mm", size=17, align="center"):
    fnt = font(ARIAL_BOLD, size)
    draw.multiline_text(xy, text, font=fnt, fill=RED, anchor=anchor,
                        align=align, spacing=1, stroke_width=3,
                        stroke_fill=(255, 255, 255))


im = Image.open(SOURCE).convert("RGB")
draw = ImageDraw.Draw(im)

title = "RÈGLES DES FRÈRES JURÉS DE LA GARDE"
flavor = (
    "Vous êtes le bouclier contre les ténèbres. Vous formez l’arrière-garde des trônes du Sud. "
    "Vous êtes la Garde de Nuit ! Vous ne jouez pas au jeu des trônes : vous êtes la seule force "
    "qui retient les sauvageons tentant de migrer vers les terres plus chaudes du Sud. Car l’hiver vient…\n"
    "Vos frères de la Garde de Nuit reconnaissent en vous un chef naturel. Vous supervisez un petit "
    "groupe dans ses tâches quotidiennes. Il vous incombe de veiller à ce que les défenses du Mur soient "
    "correctement occupées par des gardes. Pour y parvenir, vous devez assurer un approvisionnement régulier "
    "en ressources provenant des modestes avant-postes, des forteresses et des routes du Don. Si vous "
    "accomplissez bien votre tâche, vous deviendrez le nouveau Lord Commandant."
)
important = (
    "Important : les règles des Frères Jurés de la Garde utilisent toutes les règles du jeu de base, "
    "avec les modifications suivantes :"
)
left_heading = "LE MUR, LE DON ET LES SAUVAGEONS"
left_body = (
    "Le plateau représente la région du nord de Westeros où se trouvent le Mur et le Don. Le Mur protège "
    "les royaumes du sud, tandis que le Don fournit les gardes qui le défendent. Le plateau est constitué "
    "des hexagones de terrain du Don et des pièces de cadre qui les maintiennent ensemble. Le cadre comporte, "
    "au nord du Mur, des emplacements pour les zones de clan, les camps, les sentiers et les clairières.\n"
    "Les sauvageons commencent la partie dans une région appelée Crocgivre. Pendant la partie, certaines "
    "actions (comme construire un avant-poste) déclenchent leur migration. Ils migrent de Crocgivre vers les "
    "zones de clan où ils se préparent dans des camps. Ensuite, ils suivent un sentier depuis un camp jusqu’à "
    "une clairière au pied du Mur. Lorsqu’une clairière contient plus de sauvageons que la section de Mur "
    "correspondante ne compte de gardes, les sauvageons franchissent le Mur et entrent dans le Don. Si les "
    "camps d’une zone de clan sont trop remplis, les sauvageons se ruent vers le Mur.\n"
    "Sur l’illustration ci-dessous, nous indiquons toutes les zones importantes pour le déplacement des "
    "sauvageons. Les flèches noires désignent des zones précises ; les flèches bleues montrent le sens général "
    "de leur déplacement."
)
right_heading = "CONSTRUCTION DU PLATEAU"
right_body = (
    "Pour votre première partie des Frères Jurés de la Garde, nous vous conseillons d’utiliser la « Mise en "
    "place standard des Frères Jurés de la Garde » figurant au dos de ce livret.\n"
    "Commencez par assembler le cadre. Créez ensuite le Don en plaçant les hexagones de terrain dans le cadre "
    "comme indiqué. Utilisez les 21 hexagones à 4 joueurs, ou 16 hexagones à 3 joueurs. Enfin, placez les pions "
    "numérotés sur les hexagones désignés, comme illustré.\n"
    "Remarque : un plateau variable (hexagones disposés au hasard) peut être amusant et plus difficile. Vous "
    "pourrez explorer de nouvelles stratégies à chaque partie. Lorsque vous mélangez les hexagones, ne mélangez "
    "jamais les pions numérotés. Les règles correspondantes figurent dans le Guide de référence, aux entrées "
    "« Mise en place variable » et « Phase de mise en place »."
)

# Titre : ombre brune légère, puis lettres brunes.
title_font = font(ARIAL_BOLD, 31)
tw = draw.textlength(title, font=title_font)
tx = (im.width - tw) / 2
draw.text((tx + 2, 64), title, font=title_font, fill=(190, 180, 172))
draw.text((tx, 61), title, font=title_font, fill=BROWN)

draw_box(draw, (64, 116, 1025, 294), flavor, GEORGIA_ITALIC, 16, 13, RED, 0.18)
draw_box(draw, (64, 302, 1025, 334), important, GEORGIA_BOLD, 14, 12, BLACK, 0.12)

draw_box(draw, (64, 344, 518, 392), left_heading, ARIAL_BOLD, 24, 19, BLUE, 0.05)
draw_box(draw, (64, 397, 518, 874), left_body, GEORGIA, 17, 13, BLACK, 0.18)

draw_box(draw, (559, 344, 1024, 384), right_heading, ARIAL_BOLD, 24, 19, BLUE, 0.05)
draw_box(draw, (559, 397, 1024, 868), right_body, GEORGIA, 17, 13, BLACK, 0.18)

# Légendes de la carte : mêmes tons rouges et contour blanc que le livret.
label(draw, (258, 960), "3 ZONES DE CLAN", size=17)
label(draw, (150, 1010), "CROCGIVRE", size=17)
label(draw, (235, 1064), "CAMP DE\nTORMUND", size=16)
label(draw, (220, 1180), "LE MUR EST COMPOSÉ\nDE 4 SECTIONS", size=15)
label(draw, (855, 945), "5 CAMPS\nPAR ZONE DE CLAN", size=15)
label(draw, (891, 1004), "6 SENTIERS\nNUMÉROTÉS DE 1 À 8", size=15)
label(draw, (915, 1064), "4 CLAIRIÈRES", size=16)
label(draw, (958, 1130), "PISTE DES BRÈCHES\nDU MUR", size=15)
label(draw, (860, 1240), "5 EMPLACEMENTS DE GARDE\nPAR SECTION DU MUR", size=14)
label(draw, (680, 1328), "LE DON", size=17)

im.save(OUTPUT, quality=95)
print(OUTPUT)
