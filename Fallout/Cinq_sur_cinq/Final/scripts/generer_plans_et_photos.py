from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A3, A4, landscape
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "pdf"
IMG = ROOT / "images" / "accessoires"
FONT_DIR = Path(r"C:\Windows\Fonts")

pdfmetrics.registerFont(TTFont("PlanArial", FONT_DIR / "arial.ttf"))
pdfmetrics.registerFont(TTFont("PlanArial-Bold", FONT_DIR / "arialbd.ttf"))

INK = HexColor("#1C251B")
GREEN = HexColor("#496B35")
PALE = HexColor("#F3F6EC")
GRID = HexColor("#D9DFD2")
RED = HexColor("#8A342E")


ROOMS = [
    ("RDC-01", "VESTIBULE", "Entrée et terminal", "hall"),
    ("RDC-02", "SALON", "Fauteuils et cheminée", "living"),
    ("RDC-03", "SALLE À MANGER", "Grande table", "dining"),
    ("RDC-04", "CUISINE", "Plans de travail", "kitchen"),
    ("RDC-05", "SALON DE MUSIQUE", "Piano à queue", "music"),
    ("ETG-01", "PALIER ET ESCALIER", "Distribution de l’étage", "stairs"),
    ("ETG-02", "CHAMBRE D’EVELYN", "Repos médical", "bedroom"),
    ("ETG-03", "CHAMBRE DE RICHARD", "Volet extérieur", "bedroom"),
    ("ETG-04", "BUREAU DE CLAIRE", "Bureau technique", "office"),
    ("ETG-05", "SUITE DE MARA", "Chambre privée", "bedroom"),
    ("SS-01", "CAVE ET GÉNÉRATEUR", "Installation électrique", "generator"),
    ("SS-02", "MAINTENANCE", "Atelier de service", "workshop"),
    ("SS-03", "COULOIR COUPE-FEU", "Portes de sécurité", "corridor"),
    ("SS-04", "SALLE INFORMATIQUE", "Installation centrale", "server"),
    ("SEC-01", "CONDUIT DE SERVICE", "Connexion verticale", "connector"),
    ("SEC-02", "PASSAGE TECHNIQUE", "Accès dissimulé", "connector"),
]


def line(c, x1, y1, x2, y2, color=GREEN, width=0.65, dash=None):
    c.setStrokeColor(color)
    c.setLineWidth(width)
    c.setDash(dash or [])
    c.line(x1, y1, x2, y2)
    c.setDash([])


def grid(c, x, y, w, h, step=8 * mm):
    c.setStrokeColor(GRID)
    c.setLineWidth(0.18)
    pos = x
    while pos <= x + w:
        c.line(pos, y, pos, y + h)
        pos += step
    pos = y
    while pos <= y + h:
        c.line(x, pos, x + w, pos)
        pos += step


def furniture(c, kind, x, y, w, h):
    c.setStrokeColor(GREEN)
    c.setFillColor(PALE)
    c.setLineWidth(0.65)
    cx, cy = x + w / 2, y + h / 2
    if kind == "hall":
        c.rect(x + 0.12*w, y + 0.18*h, 0.25*w, 0.13*h, fill=1)
        for i in range(5):
            c.circle(x + (0.18 + i*0.15)*w, y + 0.77*h, 1.4*mm, fill=0)
        c.rect(x + 0.70*w, y + 0.18*h, 0.15*w, 0.22*h, fill=1)
    elif kind == "living":
        c.roundRect(x + 0.16*w, y + 0.18*h, 0.58*w, 0.18*h, 2*mm, fill=1)
        c.rect(x + 0.21*w, y + 0.58*h, 0.48*w, 0.10*h, fill=1)
        c.circle(cx, cy, 8*mm, fill=0)
    elif kind == "dining":
        c.roundRect(x + 0.25*w, y + 0.25*h, 0.50*w, 0.45*h, 2*mm, fill=1)
        for dx, dy in [(0.18,0.33),(0.18,0.58),(0.82,0.33),(0.82,0.58),(0.50,0.80)]:
            c.circle(x + dx*w, y + dy*h, 3*mm, fill=0)
    elif kind == "kitchen":
        c.rect(x + 0.10*w, y + 0.15*h, 0.80*w, 0.12*h, fill=1)
        c.rect(x + 0.10*w, y + 0.27*h, 0.12*w, 0.50*h, fill=1)
        c.rect(x + 0.62*w, y + 0.48*h, 0.22*w, 0.22*h, fill=0)
    elif kind == "music":
        c.ellipse(x + 0.30*w, y + 0.24*h, x + 0.76*w, y + 0.68*h, fill=1)
        c.rect(x + 0.18*w, y + 0.40*h, 0.28*w, 0.10*h, fill=1)
        for dx, dy in [(0.34,0.25),(0.65,0.28),(0.62,0.62)]:
            c.circle(x + dx*w, y + dy*h, 1.6*mm, fill=1)
    elif kind == "stairs":
        for i in range(8):
            yy = y + (0.18 + i*0.075)*h
            c.line(x + 0.25*w, yy, x + 0.75*w, yy)
        c.line(x + 0.50*w, y + 0.18*h, x + 0.50*w, y + 0.78*h)
    elif kind == "bedroom":
        c.rect(x + 0.18*w, y + 0.20*h, 0.48*w, 0.56*h, fill=1)
        c.line(x + 0.18*w, y + 0.62*h, x + 0.66*w, y + 0.62*h)
        c.rect(x + 0.72*w, y + 0.18*h, 0.14*w, 0.18*h, fill=1)
    elif kind == "office":
        c.rect(x + 0.22*w, y + 0.48*h, 0.56*w, 0.18*h, fill=1)
        c.circle(cx, y + 0.36*h, 5*mm, fill=0)
        c.rect(x + 0.13*w, y + 0.18*h, 0.12*w, 0.56*h, fill=1)
    elif kind == "generator":
        c.rect(x + 0.18*w, y + 0.24*h, 0.64*w, 0.48*h, fill=1)
        for i in range(3):
            c.circle(x + (0.33 + i*0.17)*w, cy, 5*mm, fill=0)
        c.line(x + 0.20*w, y + 0.78*h, x + 0.80*w, y + 0.78*h)
    elif kind == "workshop":
        c.rect(x + 0.15*w, y + 0.22*h, 0.70*w, 0.15*h, fill=1)
        for i in range(4):
            c.rect(x + (0.18+i*0.16)*w, y + 0.58*h, 0.09*w, 0.12*h, fill=0)
    elif kind == "corridor":
        c.rect(x + 0.16*w, y + 0.38*h, 0.68*w, 0.24*h, fill=0)
        for i in range(4):
            xx = x + (0.22+i*0.18)*w
            c.line(xx, y + 0.38*h, xx, y + 0.62*h)
    elif kind == "server":
        for i in range(4):
            c.rect(x + (0.12+i*0.20)*w, y + 0.20*h, 0.12*w, 0.58*h, fill=1)
            for j in range(4):
                c.circle(x + (0.18+i*0.20)*w, y + (0.29+j*0.12)*h, 0.9*mm, fill=0)
    elif kind == "connector":
        c.setDash(3, 2)
        c.roundRect(x + 0.18*w, y + 0.36*h, 0.64*w, 0.28*h, 3*mm, fill=0)
        c.setDash([])
        c.line(x + 0.30*w, cy, x + 0.70*w, cy)
        c.line(x + 0.65*w, cy + 3*mm, x + 0.70*w, cy)
        c.line(x + 0.65*w, cy - 3*mm, x + 0.70*w, cy)


def draw_tile(c, x, y, w, h, code, name, subtitle, kind):
    grid(c, x, y, w, h)
    c.setStrokeColor(GREEN)
    c.setLineWidth(1)
    c.rect(x, y, w, h, fill=0, stroke=1)
    # Cut marks.
    c.setStrokeColor(INK)
    c.setLineWidth(0.35)
    c.setDash(2, 2)
    c.rect(x - 1.5*mm, y - 1.5*mm, w + 3*mm, h + 3*mm, fill=0, stroke=1)
    c.setDash([])
    c.setFillColor(GREEN)
    c.rect(x, y + h - 13*mm, w, 13*mm, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("PlanArial-Bold", 9.2)
    c.drawString(x + 4*mm, y + h - 8*mm, name)
    c.setFont("Courier-Bold", 6.3)
    c.drawRightString(x + w - 4*mm, y + h - 8*mm, code)
    c.setFillColor(INK)
    c.setFont("PlanArial", 7.2)
    c.drawString(x + 4*mm, y + h - 18*mm, subtitle)
    furniture(c, kind, x + 4*mm, y + 7*mm, w - 8*mm, h - 29*mm)
    # Neutral doorway marks: no destination names.
    c.setStrokeColor(white)
    c.setLineWidth(3)
    c.line(x + w/2 - 7*mm, y, x + w/2 + 7*mm, y)
    c.line(x + w/2 - 7*mm, y+h, x + w/2 + 7*mm, y+h)
    c.setStrokeColor(GREEN)
    c.setLineWidth(0.7)
    c.arc(x + w/2 - 7*mm, y - 7*mm, x + w/2 + 7*mm, y + 7*mm, 0, 180)


def generate_cutout_plan():
    out = canvas.Canvas(str(PDF / "12_PLAN_JOUEUR_A_DECOUPER.pdf"), pagesize=A4, pageCompression=1)
    width, height = A4
    tile_w, tile_h = 91*mm, 130*mm
    xs = [10*mm, width - 10*mm - tile_w]
    ys = [height - 15*mm - tile_h, 8*mm]
    for idx, room in enumerate(ROOMS):
        slot = idx % 4
        if slot == 0:
            out.setFillColor(white)
            out.rect(0, 0, width, height, fill=1, stroke=0)
            out.setFillColor(INK)
            out.setFont("Courier-Bold", 6.5)
            out.drawString(10*mm, height - 7*mm, "ROBCO // PLAN RÉSIDENTIEL MODULAIRE // DÉCOUPER SUR LES POINTILLÉS")
        col, row = slot % 2, slot // 2
        draw_tile(out, xs[col], ys[row], tile_w, tile_h, *room)
        if slot == 3 or idx == len(ROOMS)-1:
            out.showPage()
    out.save()


MJ_ROOMS = {
    "Vestibule": ["Hector", "registre 5/5", "première confusion"],
    "Salon": ["fausses pistes", "querelles des robots"],
    "Salle à manger": ["5 couverts", "comptine", "ordre des absences"],
    "Cuisine": ["ressources", "accès de service"],
    "Salon de musique": ["piano : 4 notes", "corde absente", "brochure HARMONY"],
    "Palier": ["Basilisk", "contrôle radiologique"],
    "Evelyn": ["CORPS", "Bonrepos", "allergie + injection"],
    "Richard": ["CORPS", "quarantaine", "sortie collective"],
    "Bureau Claire": ["badge", "horaires", "source sous le salon"],
    "Suite Mara": ["CORPS", "corde originale", "journal final"],
    "Générateur": ["CORPS ABEL", "Clovis", "remise sous tension"],
    "Maintenance": ["relais", "accès de secours"],
    "Couloir coupe-feu": ["reproduction Claire", "purge inerte"],
    "Cœur SALI": ["CORPS CLAIRE", "logs complets", "choix final"],
}


def mj_room(c, x, y, w, h, title, floor_code):
    c.setFillColor(PALE)
    c.setStrokeColor(GREEN)
    c.setLineWidth(0.8)
    c.roundRect(x, y, w, h, 2*mm, fill=1, stroke=1)
    c.setFillColor(GREEN)
    c.setFont("PlanArial-Bold", 7.6)
    c.drawString(x + 2.5*mm, y + h - 5*mm, title.upper())
    c.setFont("Courier-Bold", 5.2)
    c.drawRightString(x + w - 2.5*mm, y + h - 5*mm, floor_code)
    c.setFillColor(INK)
    c.setFont("PlanArial", 5.8)
    yy = y + h - 10*mm
    for item in MJ_ROOMS[title]:
        c.drawString(x + 3*mm, yy, "• " + item)
        yy -= 4.2*mm


def connect(c, a, b, secret=False, vertical=False):
    ax, ay = a
    bx, by = b
    line(c, ax, ay, bx, by, RED if secret else GREEN, 1.1 if secret else 0.8, [4, 2] if secret else None)
    if secret:
        c.setFillColor(RED)
        c.setFont("Courier-Bold", 5.2)
        c.drawCentredString((ax+bx)/2, (ay+by)/2 + 1.5*mm, "SECRET")


def generate_mj_plan():
    page = landscape(A3)
    out = canvas.Canvas(str(PDF / "11_PLAN_MJ_COMPLET.pdf"), pagesize=page, pageCompression=1)
    width, height = page
    out.setFillColor(white)
    out.rect(0, 0, width, height, fill=1, stroke=0)
    grid(out, 8*mm, 8*mm, width-16*mm, height-16*mm, 10*mm)
    out.setFillColor(GREEN)
    out.rect(8*mm, height-20*mm, width-16*mm, 12*mm, fill=1, stroke=0)
    out.setFillColor(white)
    out.setFont("PlanArial-Bold", 15)
    out.drawString(13*mm, height-16*mm, "MANOIR HALVHREST — PLAN MJ COMPLET")
    out.setFont("Courier-Bold", 6.5)
    out.drawRightString(width-13*mm, height-15*mm, "SPOILERS // CINQ SUR CINQ")

    rw, rh, gap = 58*mm, 28*mm, 9*mm
    xs = [15*mm + i*(rw+gap) for i in range(4)]
    y_rdc, y_etg, y_ss = 207*mm, 111*mm, 15*mm

    out.setFillColor(INK)
    out.setFont("Courier-Bold", 8)
    for label, y in [("REZ-DE-CHAUSSÉE", y_rdc+rh+4*mm), ("ÉTAGE", y_etg+rh+4*mm), ("SOUS-SOL", y_ss+rh+4*mm)]:
        out.drawString(15*mm, y, label)

    rdc = [("Vestibule","RDC-01"),("Salon","RDC-02"),("Salle à manger","RDC-03"),("Salon de musique","RDC-05")]
    etg = [("Palier","ETG-01"),("Evelyn","ETG-02"),("Richard","ETG-03"),("Suite Mara","ETG-05")]
    ss = [("Générateur","SS-01"),("Maintenance","SS-02"),("Couloir coupe-feu","SS-03"),("Cœur SALI","SS-04")]
    centers = {}
    for row, y in [(rdc,y_rdc),(etg,y_etg),(ss,y_ss)]:
        for idx, (name, code) in enumerate(row):
            mj_room(out, xs[idx], y, rw, rh, name, code)
            centers[name] = (xs[idx]+rw/2, y+rh/2)
            if idx:
                connect(out, (xs[idx-1]+rw, y+rh/2), (xs[idx], y+rh/2))

    # Side rooms.
    kitchen_xy = (xs[1], y_rdc-39*mm)
    office_xy = (xs[0], y_etg-39*mm)
    mj_room(out, *kitchen_xy, rw, rh, "Cuisine", "RDC-04")
    mj_room(out, *office_xy, rw, rh, "Bureau Claire", "ETG-04")
    centers["Cuisine"] = (kitchen_xy[0]+rw/2, kitchen_xy[1]+rh/2)
    centers["Bureau Claire"] = (office_xy[0]+rw/2, office_xy[1]+rh/2)
    connect(out, (centers["Salon"][0], y_rdc), (centers["Cuisine"][0], kitchen_xy[1]+rh))
    connect(out, (centers["Palier"][0], y_etg), (centers["Bureau Claire"][0], office_xy[1]+rh))

    # Cross-floor routes are written rather than drawn across other rooms.
    out.setFillColor(GREEN)
    out.setFont("Courier-Bold", 5.4)
    out.drawString(xs[2] + 3*mm, y_rdc + 3*mm, "ESCALIER → PALIER")
    out.drawString(xs[0] + 3*mm, y_etg + 3*mm, "ESCALIER → SALLE À MANGER")
    out.drawString(kitchen_xy[0] + 3*mm, kitchen_xy[1] + 3*mm, "ESCALIER DE SERVICE → CAVE")
    out.drawString(xs[0] + 3*mm, y_ss + 3*mm, "ESCALIER DE SERVICE → CUISINE")

    # Secret routes stay red and avoid crossing room boxes.
    connect(out, (centers["Salon de musique"][0], y_rdc), (centers["Cœur SALI"][0], y_ss+rh), secret=True)
    secret_y = y_etg - 5*mm
    line(out, office_xy[0]+rw, office_xy[1]+rh/2, office_xy[0]+rw+5*mm, secret_y, RED, 1.1, [4, 2])
    line(out, office_xy[0]+rw+5*mm, secret_y, xs[3]+rw/2, secret_y, RED, 1.1, [4, 2])
    line(out, xs[3]+rw/2, secret_y, xs[3]+rw/2, y_etg, RED, 1.1, [4, 2])
    out.setFillColor(RED)
    out.setFont("Courier-Bold", 5.2)
    out.drawString(office_xy[0]+rw+9*mm, secret_y+1.5*mm, "PASSAGE TECHNIQUE SECRET")

    # Legend and pacing strip.
    lx = 292*mm
    out.setFillColor(white)
    out.setStrokeColor(GREEN)
    out.rect(lx, 15*mm, width-lx-12*mm, 220*mm, fill=1, stroke=1)
    out.setFillColor(GREEN)
    out.setFont("PlanArial-Bold", 9)
    out.drawString(lx+5*mm, 226*mm, "ORDRE CONSEILLÉ")
    out.setFillColor(INK)
    out.setFont("PlanArial", 6.7)
    notes = [
        "1. Vestibule, salon, salle à manger",
        "2. Générateur : Abel + Clovis",
        "3. Evelyn + Bonrepos",
        "4. Richard + Basilisk",
        "5. Piano puis Mara",
        "6. Bureau/passages techniques",
        "7. Couloir coupe-feu puis cœur",
        "",
        "TRAITS PLEINS : accès ordinaires",
        "TRAITS ROUGES : passages secrets",
        "",
        "Ne poser une tuile joueur que lorsque",
        "les PJ voient réellement la pièce.",
        "Les tuiles SEC-01 et SEC-02 restent",
        "cachées jusqu’à leur découverte.",
        "",
        "COUPES : fusionner Richard/Mara si",
        "retard ; ne jamais précipiter le cœur.",
    ]
    yy = 217*mm
    for note in notes:
        out.drawString(lx+5*mm, yy, note)
        yy -= 7.2*mm
    out.showPage()
    out.save()


def generate_photo_handout():
    out = canvas.Canvas(str(PDF / "13_PHOTOS_MIROIRS.pdf"), pagesize=landscape(A4), pageCompression=1)
    width, height = landscape(A4)
    for filename in ["photo_residents_halvhrest.png", "photo_miroir_pj.png"]:
        out.setFillColor(white)
        out.rect(0, 0, width, height, fill=1, stroke=0)
        # 24 x 18 cm image area, easy to trim; no label is printed on the handout.
        x, y, w, h = 28.5*mm, 15*mm, 240*mm, 180*mm
        out.setStrokeColor(HexColor("#777777"))
        out.setLineWidth(0.35)
        out.setDash(2, 2)
        out.rect(x-2*mm, y-2*mm, w+4*mm, h+4*mm, fill=0, stroke=1)
        out.setDash([])
        out.drawImage(str(IMG / filename), x, y, width=w, height=h, preserveAspectRatio=True, anchor="c", mask="auto")
        out.showPage()
    out.save()


def main():
    PDF.mkdir(parents=True, exist_ok=True)
    generate_mj_plan()
    generate_cutout_plan()
    generate_photo_handout()
    print("Plans MJ/joueur et photographies imprimables générés.")


if __name__ == "__main__":
    main()
