import html
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.colors import Color, HexColor, white
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    HRFlowable,
    Image,
    ListFlowable,
    ListItem,
    LongTable,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
    XPreformatted,
)


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "pdf_guides"
FONT_DIR = Path(r"C:\Windows\Fonts")
PAGEBREAK_H1 = True

pdfmetrics.registerFont(TTFont("GuideArial", FONT_DIR / "arial.ttf"))
pdfmetrics.registerFont(TTFont("GuideArial-Bold", FONT_DIR / "arialbd.ttf"))
pdfmetrics.registerFont(TTFont("GuideArial-Italic", FONT_DIR / "ariali.ttf"))
if (FONT_DIR / "consola.ttf").exists():
    pdfmetrics.registerFont(TTFont("GuideMono", FONT_DIR / "consola.ttf"))
else:
    pdfmetrics.registerFont(TTFont("GuideMono", FONT_DIR / "cour.ttf"))


ACCENT = HexColor("#C98D13")
DARK = HexColor("#19252D")
INK = HexColor("#252A2E")
PAPER = HexColor("#F9F7F0")
PALE = HexColor("#F1E8D2")
LINE = HexColor("#CBBE9E")


def build_styles():
    return {
        "cover_title": ParagraphStyle(
            "cover_title",
            fontName="GuideArial-Bold",
            fontSize=29,
            leading=34,
            textColor=white,
            alignment=TA_CENTER,
        ),
        "cover_sub": ParagraphStyle(
            "cover_sub",
            fontName="GuideArial",
            fontSize=13,
            leading=17,
            textColor=white,
            alignment=TA_CENTER,
        ),
        "cover_body": ParagraphStyle(
            "cover_body",
            fontName="GuideArial",
            fontSize=11,
            leading=15,
            textColor=INK,
            alignment=TA_LEFT,
        ),
        "h1": ParagraphStyle(
            "h1",
            fontName="GuideArial-Bold",
            fontSize=18,
            leading=22,
            textColor=DARK,
            spaceBefore=0,
            spaceAfter=8,
            keepWithNext=True,
        ),
        "h2": ParagraphStyle(
            "h2",
            fontName="GuideArial-Bold",
            fontSize=13.2,
            leading=16,
            textColor=ACCENT,
            spaceBefore=9,
            spaceAfter=4,
            keepWithNext=True,
        ),
        "h3": ParagraphStyle(
            "h3",
            fontName="GuideArial-Bold",
            fontSize=10.5,
            leading=13,
            textColor=DARK,
            spaceBefore=6,
            spaceAfter=3,
            keepWithNext=True,
        ),
        "h4": ParagraphStyle(
            "h4",
            fontName="GuideArial-Bold",
            fontSize=9.5,
            leading=12,
            textColor=ACCENT,
            spaceBefore=4,
            spaceAfter=2,
            keepWithNext=True,
        ),
        "body": ParagraphStyle(
            "body",
            fontName="GuideArial",
            fontSize=9.2,
            leading=12.2,
            textColor=INK,
            spaceAfter=5,
            splitLongWords=True,
        ),
        "bullet": ParagraphStyle(
            "bullet",
            fontName="GuideArial",
            fontSize=9,
            leading=11.5,
            textColor=INK,
            leftIndent=2,
            spaceAfter=1.5,
        ),
        "quote": ParagraphStyle(
            "quote",
            fontName="GuideArial-Italic",
            fontSize=9.5,
            leading=12.8,
            textColor=HexColor("#3C3322"),
            leftIndent=4,
            rightIndent=4,
            spaceAfter=0,
        ),
        "code": ParagraphStyle(
            "code",
            fontName="GuideMono",
            fontSize=7.4,
            leading=9.2,
            textColor=HexColor("#182027"),
        ),
        "table": ParagraphStyle(
            "table",
            fontName="GuideArial",
            fontSize=7.6,
            leading=9.3,
            textColor=INK,
        ),
        "table_head": ParagraphStyle(
            "table_head",
            fontName="GuideArial-Bold",
            fontSize=7.7,
            leading=9.4,
            textColor=white,
        ),
        "caption": ParagraphStyle(
            "caption",
            fontName="GuideArial-Italic",
            fontSize=8,
            leading=10,
            textColor=HexColor("#5D6265"),
            alignment=TA_CENTER,
            spaceAfter=5,
        ),
    }


STY = build_styles()


def clean_symbols(text):
    replacements = {
        "⚠️": "ATTENTION —",
        "⚠": "ATTENTION —",
        "🔒": "MJ —",
        "🔊": "À LIRE —",
        "📌": "",
        "📖": "",
        "📄": "",
        "✓": "OK",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def inline_markdown(text):
    text = clean_symbols(text.strip())
    text = html.escape(text, quote=False)
    text = re.sub(r"!\[([^]]*)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\[([^]]+)\]\([^)]+\)", r"<u>\1</u>", text)
    text = re.sub(r"`([^`]+)`", r'<font name="GuideMono">\1</font>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", text)
    text = text.replace("  ", " ")
    return text


def is_table_separator(line):
    stripped = line.strip().strip("|")
    cells = [cell.strip() for cell in stripped.split("|")]
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell or "-") for cell in cells)


def paragraph_from_lines(lines):
    joined = " ".join(line.strip() for line in lines)
    return Paragraph(inline_markdown(joined), STY["body"])


def table_flow(lines, usable_width):
    rows = []
    for line in lines:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", cell or "-") for cell in cells):
            continue
        rows.append(cells)
    if not rows:
        return Spacer(1, 1)
    cols = max(len(row) for row in rows)
    normalized = [row + [""] * (cols - len(row)) for row in rows]
    data = []
    for row_idx, row in enumerate(normalized):
        style = STY["table_head"] if row_idx == 0 else STY["table"]
        data.append([Paragraph(inline_markdown(cell), style) for cell in row])
    widths = [usable_width / cols] * cols
    table = LongTable(data, colWidths=widths, repeatRows=1, splitByRow=1, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), DARK),
                ("TEXTCOLOR", (0, 0), (-1, 0), white),
                ("BACKGROUND", (0, 1), (-1, -1), colors.white),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, HexColor("#F3F0E7")]),
                ("GRID", (0, 0), (-1, -1), 0.35, LINE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return table


def quote_flow(lines, usable_width):
    clean = []
    for line in lines:
        item = line.lstrip()[1:]
        if item.startswith(" "):
            item = item[1:]
        if item.strip().startswith("###"):
            item = item.strip().lstrip("#").strip()
        clean.append(item)
    text = "<br/>".join(inline_markdown(line) for line in clean if line.strip())
    para = Paragraph(text, STY["quote"])
    table = Table([[para]], colWidths=[usable_width - 6 * mm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), PALE),
                ("LINEBEFORE", (0, 0), (0, -1), 3, ACCENT),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    return table


def code_flow(lines, usable_width):
    text = clean_symbols("\n".join(lines))
    pre = XPreformatted(html.escape(text), STY["code"])
    table = Table([[pre]], colWidths=[usable_width - 6 * mm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), HexColor("#E9EEF0")),
                ("BOX", (0, 0), (-1, -1), 0.5, HexColor("#9BA9AE")),
                ("LEFTPADDING", (0, 0), (-1, -1), 7),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    return table


def image_flow(source_path, alt, rel_path, usable_width):
    img_path = (source_path.parent / rel_path).resolve()
    if not img_path.exists():
        return Paragraph(f"[Image manquante : {inline_markdown(alt)}]", STY["caption"])
    img = Image(str(img_path))
    max_w = min(usable_width * 0.52, 92 * mm)
    max_h = 130 * mm
    scale = min(max_w / img.imageWidth, max_h / img.imageHeight)
    img.drawWidth = img.imageWidth * scale
    img.drawHeight = img.imageHeight * scale
    img.hAlign = "CENTER"
    return [img, Paragraph(inline_markdown(alt), STY["caption"])]


def markdown_to_flowables(source_path, pagebreak_h1=True):
    usable_width = A4[0] - 30 * mm
    lines = source_path.read_text(encoding="utf-8").splitlines()
    story = []
    i = 0
    h1_seen = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            i += 1
            continue

        image_match = re.fullmatch(r"!\[([^]]*)\]\(([^)]+)\)", stripped)
        if image_match:
            flows = image_flow(source_path, image_match.group(1), image_match.group(2), usable_width)
            story.extend(flows if isinstance(flows, list) else [flows])
            i += 1
            continue

        if stripped.startswith("```"):
            i += 1
            code_lines = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1
            story.extend([code_flow(code_lines, usable_width), Spacer(1, 4 * mm)])
            continue

        if stripped.startswith("|") and i + 1 < len(lines) and is_table_separator(lines[i + 1]):
            table_lines = [line]
            i += 1
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            story.extend([table_flow(table_lines, usable_width), Spacer(1, 4 * mm)])
            continue

        if stripped.startswith(">"):
            quote_lines = []
            while i < len(lines) and (lines[i].strip().startswith(">") or not lines[i].strip()):
                if lines[i].strip().startswith(">"):
                    quote_lines.append(lines[i])
                i += 1
            story.extend([quote_flow(quote_lines, usable_width), Spacer(1, 4 * mm)])
            continue

        heading = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if heading:
            level = len(heading.group(1))
            title = clean_symbols(heading.group(2))
            if level == 1 and pagebreak_h1 and h1_seen:
                story.append(PageBreak())
            if level == 1:
                h1_seen = True
            style = STY["h1"] if level == 1 else STY["h2"] if level == 2 else STY["h3"] if level == 3 else STY["h4"]
            story.append(Paragraph(inline_markdown(title), style))
            i += 1
            continue

        if stripped == "---":
            story.extend([Spacer(1, 1.5 * mm), HRFlowable(width="100%", thickness=0.6, color=LINE), Spacer(1, 2.5 * mm)])
            i += 1
            continue

        if re.match(r"^[-*]\s+", stripped):
            items = []
            while i < len(lines) and re.match(r"^\s*[-*]\s+", lines[i]):
                item_text = re.sub(r"^\s*[-*]\s+", "", lines[i])
                items.append(ListItem(Paragraph(inline_markdown(item_text), STY["bullet"]), leftIndent=8))
                i += 1
            story.extend([ListFlowable(items, bulletType="bullet", leftIndent=13, bulletFontName="GuideArial", bulletFontSize=7), Spacer(1, 2 * mm)])
            continue

        if re.match(r"^\d+\.\s+", stripped):
            items = []
            while i < len(lines) and re.match(r"^\s*\d+\.\s+", lines[i]):
                item_text = re.sub(r"^\s*\d+\.\s+", "", lines[i])
                items.append(ListItem(Paragraph(inline_markdown(item_text), STY["bullet"]), leftIndent=10))
                i += 1
            story.extend([ListFlowable(items, bulletType="1", start="1", leftIndent=16, bulletFontName="GuideArial", bulletFontSize=8), Spacer(1, 2 * mm)])
            continue

        paragraph_lines = [line]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if (
                not nxt
                or nxt.startswith("#")
                or nxt.startswith(">")
                or nxt.startswith("```")
                or nxt == "---"
                or re.match(r"^[-*]\s+", nxt)
                or re.match(r"^\d+\.\s+", nxt)
                or (nxt.startswith("|") and i + 1 < len(lines) and is_table_separator(lines[i + 1]))
                or re.fullmatch(r"!\[([^]]*)\]\(([^)]+)\)", nxt)
            ):
                break
            paragraph_lines.append(lines[i])
            i += 1
        story.append(paragraph_from_lines(paragraph_lines))

    return story


def cover_story(title, subtitle, source_names):
    title_box = Table(
        [[Paragraph("LA GUERRE DE L'ÉTOILE", STY["cover_title"])], [Paragraph(title, STY["cover_sub"])]],
        colWidths=[A4[0] - 30 * mm],
        rowHeights=[44 * mm, 25 * mm],
    )
    title_box.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), DARK),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("LINEBELOW", (0, 0), (-1, 0), 2, ACCENT),
            ]
        )
    )
    warning = Table([[Paragraph("DOCUMENT DU MAÎTRE DE JEU — CONTIENT TOUS LES SPOILERS", STY["h3"])]], colWidths=[A4[0] - 40 * mm])
    warning.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), PALE),
                ("BOX", (0, 0), (-1, -1), 1, ACCENT),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )
    source_lines = "<br/>".join(f"• {html.escape(name)}" for name in source_names)
    contents = Paragraph(f"<b>Contenu :</b><br/>{source_lines}", STY["cover_body"])
    return [Spacer(1, 18 * mm), title_box, Spacer(1, 18 * mm), warning, Spacer(1, 18 * mm), contents, PageBreak()]


def page_decor(c, doc):
    page = c.getPageNumber()
    w, h = A4
    c.saveState()
    c.setFillColor(PAPER)
    c.rect(0, 0, w, h, fill=1, stroke=0)
    if page > 1:
        c.setFillColor(DARK)
        c.rect(0, h - 11 * mm, w, 11 * mm, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("GuideArial-Bold", 7.4)
        c.drawString(15 * mm, h - 7 * mm, "LA GUERRE DE L'ÉTOILE — DOSSIER MJ — SPOILERS")
        c.setStrokeColor(ACCENT)
        c.setLineWidth(1)
        c.line(15 * mm, 10 * mm, w - 15 * mm, 10 * mm)
        c.setFillColor(HexColor("#555A5E"))
        c.setFont("GuideArial", 7)
        c.drawString(15 * mm, 6 * mm, "Sunshine — version imprimable")
        c.drawRightString(w - 15 * mm, 6 * mm, f"Page {page}")
    c.restoreState()


def build_pdf(output_name, title, sources):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    output = OUT_DIR / output_name
    doc = SimpleDocTemplate(
        str(output),
        pagesize=A4,
        rightMargin=15 * mm,
        leftMargin=15 * mm,
        topMargin=17 * mm,
        bottomMargin=15 * mm,
        title=f"La Guerre de l'Étoile — {title}",
        author="Dossier Sunshine",
        pageCompression=1,
    )
    story = cover_story(title, "Édition A4 prête à imprimer", [label for _, label in sources])
    for source_idx, (relative_path, label) in enumerate(sources):
        if source_idx:
            story.append(PageBreak())
        story.append(Paragraph(label.upper(), STY["h1"]))
        story.append(HRFlowable(width="100%", thickness=1.2, color=ACCENT))
        story.append(Spacer(1, 4 * mm))
        story.extend(markdown_to_flowables(ROOT / relative_path, pagebreak_h1=PAGEBREAK_H1))
    doc.build(story, onFirstPage=page_decor, onLaterPages=page_decor)
    return output


def main():
    jobs = [
        (
            "00_DOSSIER_MJ_COMPLET.pdf",
            "DOSSIER MJ COMPLET",
            [
                ("00_LISEZ_MOI.md", "Présentation et chemin critique"),
                ("01_GUIDE_MJ_COMPLET.md", "Guide MJ et scénario complet"),
                ("02_PNJ_LIEUX_FACTIONS.md", "PNJ, lieux, loupes et factions"),
                ("03_AIDES_DE_JEU.md", "Aides de jeu et documents"),
                ("04_PRETIRES.md", "Catalogue des prétirés"),
            ],
        ),
        (
            "01_GUIDE_MJ_SCENARIO.pdf",
            "GUIDE MJ ET SCÉNARIO",
            [
                ("00_LISEZ_MOI.md", "Présentation et chemin critique"),
                ("01_GUIDE_MJ_COMPLET.md", "Guide MJ et scénario complet"),
            ],
        ),
        (
            "02_PNJ_LIEUX_FACTIONS.pdf",
            "PNJ, LIEUX ET FACTIONS",
            [("02_PNJ_LIEUX_FACTIONS.md", "PNJ, lieux, loupes et factions")],
        ),
        (
            "03_AIDES_DE_JEU.pdf",
            "AIDES DE JEU",
            [("03_AIDES_DE_JEU.md", "Aides de jeu et documents à imprimer")],
        ),
        (
            "04_CATALOGUE_PRETIRES.pdf",
            "CATALOGUE DES PRÉTIRÉS",
            [("04_PRETIRES.md", "Les cinq personnages")],
        ),
        (
            "05_PROMPTS_VISUELS.pdf",
            "PROMPTS VISUELS",
            [("05_PROMPTS_VISUELS.md", "Portraits et prompts sans spoiler")],
        ),
        (
            "06_REGLES_PERSONNAGES.pdf",
            "RÈGLES RAPIDES DES PERSONNAGES",
            [("fiches_personnages/00_REGLES_RAPIDES.md", "Règles d20 à distribuer")],
        ),
    ]
    outputs = [build_pdf(*job) for job in jobs]
    print(f"Généré : {len(outputs)} PDF dans {OUT_DIR}")
    for output in outputs:
        print(output.name)


if __name__ == "__main__":
    main()
