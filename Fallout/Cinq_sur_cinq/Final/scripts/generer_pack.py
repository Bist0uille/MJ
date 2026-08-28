from pathlib import Path
import importlib.util
import html


HERE = Path(__file__).resolve()
ROOT = HERE.parents[1]
BASE_SCRIPT = HERE.parents[3] / "Sunshine" / "scripts" / "generer_guides_pdf.py"

spec = importlib.util.spec_from_file_location("guide_pdf_base_cinq", BASE_SCRIPT)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)

base.ROOT = ROOT
base.OUT_DIR = ROOT / "pdf"
base.PAGEBREAK_H1 = False
base.ACCENT = base.HexColor("#222222")
base.DARK = base.HexColor("#111111")
base.PALE = base.white
base.PAPER = base.white
base.LINE = base.HexColor("#999999")
base.STY = base.build_styles()
base.STY["cover_title"].textColor = base.HexColor("#111111")
base.STY["cover_sub"].textColor = base.HexColor("#333333")
base.STY["table_head"].textColor = base.HexColor("#111111")


def ink_saver_table_flow(lines, usable_width):
    import re
    rows = []
    for line in lines:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", cell or "-") for cell in cells):
            continue
        rows.append(cells)
    if not rows:
        return base.Spacer(1, 1)
    cols = max(len(row) for row in rows)
    normalized = [row + [""] * (cols - len(row)) for row in rows]
    data = []
    for row_idx, row in enumerate(normalized):
        style = base.STY["table_head"] if row_idx == 0 else base.STY["table"]
        data.append([base.Paragraph(base.inline_markdown(cell), style) for cell in row])
    table = base.LongTable(data, colWidths=[usable_width / cols] * cols, repeatRows=1, splitByRow=1, hAlign="LEFT")
    table.setStyle(base.TableStyle([
        ("LINEBELOW", (0, 0), (-1, 0), 1, base.HexColor("#333333")),
        ("GRID", (0, 0), (-1, -1), 0.3, base.LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return table


def ink_saver_quote_flow(lines, usable_width):
    clean = []
    for line in lines:
        item = line.lstrip()[1:]
        if item.startswith(" "):
            item = item[1:]
        clean.append(item)
    para = base.Paragraph("<br/>".join(base.inline_markdown(line) for line in clean if line.strip()), base.STY["quote"])
    table = base.Table([[para]], colWidths=[usable_width - 6 * base.mm])
    table.setStyle(base.TableStyle([
        ("LINEBEFORE", (0, 0), (0, -1), 1.5, base.HexColor("#333333")),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return table


def ink_saver_code_flow(lines, usable_width):
    text = base.clean_symbols("\n".join(lines))
    pre = base.XPreformatted(html.escape(text), base.STY["code"])
    table = base.Table([[pre]], colWidths=[usable_width - 6 * base.mm])
    table.setStyle(base.TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.45, base.HexColor("#777777")),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return table


base.table_flow = ink_saver_table_flow
base.quote_flow = ink_saver_quote_flow
base.code_flow = ink_saver_code_flow


def cover_story(title, subtitle, source_names):
    title_box = base.Table(
        [
            [base.Paragraph("CINQ SUR CINQ", base.STY["cover_title"])],
            [base.Paragraph(title, base.STY["cover_sub"])],
        ],
        colWidths=[base.A4[0] - 30 * base.mm],
        rowHeights=[44 * base.mm, 25 * base.mm],
    )
    title_box.setStyle(base.TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("BOX", (0, 0), (-1, -1), 1.2, base.HexColor("#222222")),
        ("LINEBELOW", (0, 0), (-1, 0), 1.2, base.HexColor("#222222")),
    ]))
    warning = base.Table(
        [[base.Paragraph("DOCUMENT MJ — CONTIENT TOUS LES SPOILERS", base.STY["h3"])]],
        colWidths=[base.A4[0] - 40 * base.mm],
    )
    warning.setStyle(base.TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.8, base.HexColor("#444444")),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    contents = base.Paragraph(
        "<b>Contenu :</b><br/>" + "<br/>".join(f"• {html.escape(x)}" for x in source_names),
        base.STY["cover_body"],
    )
    return [
        base.Spacer(1, 18 * base.mm), title_box,
        base.Spacer(1, 18 * base.mm), warning,
        base.Spacer(1, 18 * base.mm), contents,
        base.PageBreak(),
    ]


def page_decor(canvas, doc):
    page = canvas.getPageNumber()
    width, height = base.A4
    canvas.saveState()
    canvas.setFillColor(base.PAPER)
    canvas.rect(0, 0, width, height, fill=1, stroke=0)
    if page > 1:
        canvas.setFillColor(base.HexColor("#222222"))
        canvas.setFont("GuideArial-Bold", 7.4)
        canvas.drawString(15 * base.mm, height - 7 * base.mm, "CINQ SUR CINQ — SPOILERS MJ")
        canvas.setStrokeColor(base.HexColor("#555555"))
        canvas.line(15 * base.mm, height - 10 * base.mm, width - 15 * base.mm, height - 10 * base.mm)
        canvas.line(15 * base.mm, 10 * base.mm, width - 15 * base.mm, 10 * base.mm)
        canvas.setFillColor(base.HexColor("#555A5E"))
        canvas.setFont("GuideArial", 7)
        canvas.drawString(15 * base.mm, 6 * base.mm, "Fallout 2d20 — pack V4")
        canvas.drawRightString(width - 15 * base.mm, 6 * base.mm, f"Page {page}")
    canvas.restoreState()


base.cover_story = cover_story
base.page_decor = page_decor


def build_pdf(output_name, title, sources):
    base.OUT_DIR.mkdir(parents=True, exist_ok=True)
    output = base.OUT_DIR / output_name
    doc = base.SimpleDocTemplate(
        str(output), pagesize=base.A4,
        rightMargin=15 * base.mm, leftMargin=15 * base.mm,
        topMargin=17 * base.mm, bottomMargin=15 * base.mm,
        title=f"Cinq sur cinq — {title}",
        author="Pack V4 — Fallout 2d20", pageCompression=1,
    )
    story = cover_story(title, "Édition A4 prête à imprimer", [label for _, label in sources])
    for source_index, (relative_path, label) in enumerate(sources):
        if source_index:
            story.append(base.PageBreak())
        story.append(base.Paragraph(label.upper(), base.STY["h1"]))
        story.append(base.HRFlowable(width="100%", thickness=1.2, color=base.ACCENT))
        story.append(base.Spacer(1, 4 * base.mm))
        story.extend(base.markdown_to_flowables(ROOT / relative_path, pagebreak_h1=False))
    doc.build(story, onFirstPage=page_decor, onLaterPages=page_decor)
    return output


def build_character_pdf(output_name, source, label):
    output_dir = ROOT / "pdf" / "fiches_personnages"
    output_dir.mkdir(parents=True, exist_ok=True)
    output = output_dir / output_name
    doc = base.SimpleDocTemplate(
        str(output), pagesize=base.A4,
        rightMargin=15 * base.mm, leftMargin=15 * base.mm,
        topMargin=14 * base.mm, bottomMargin=13 * base.mm,
        title=f"Cinq sur cinq — {label}",
        author="Pack V4 — Fallout 2d20", pageCompression=1,
    )
    story = base.markdown_to_flowables(ROOT / source, pagebreak_h1=False)
    doc.build(story, onFirstPage=page_decor, onLaterPages=page_decor)
    return output


def jobs():
    characters = [
        ("fiches_personnages/00_REGLES_RAPIDES.md", "Règles rapides"),
        ("fiches_personnages/01_ZORA_FUSIBLE_VALE.md", "Zora Fusible Vale"),
        ("fiches_personnages/02_ANATOLE_TROIS_MURS_DUROC.md", "Anatole Trois-Murs Duroc"),
        ("fiches_personnages/03_NELL_DEUX_COUPS_RAINER.md", "Nell Deux-Coups Rainer"),
        ("fiches_personnages/04_DR_LAZARE_BONBON_MIETTE.md", "Dr Lazare Bonbon Miette"),
        ("fiches_personnages/05_ROOK_TOUT_DOUX.md", "Rook Tout-Doux"),
    ]
    pdf_jobs = [
        ("01_TRAME_MAITRE_COMPLETE.pdf", "TRAME MAÎTRE COMPLÈTE", [("01_TRAME_MAITRE_COMPLETE.md", "Canon du MJ")]),
        ("02_CONDUITE_MJ.pdf", "CONDUITE MJ", [("02_CONDUITE_MJ.md", "Conduite courte")]),
        ("03_SCENES_DIALOGUES_ET_INDICES.pdf", "SCÈNES, DIALOGUES ET INDICES", [("03_SCENES_DIALOGUES_ET_INDICES.md", "Conduite détaillée")]),
        ("04_STORYBOARD_MJ_1_PAGE.pdf", "STORYBOARD MJ", [("04_STORYBOARD_MJ_1_PAGE.md", "Chronologie express")]),
        ("05_INTRO_ET_OUTRO_A_LIRE.pdf", "INTRO ET OUTRO À LIRE", [("05_INTRO_ET_OUTRO_A_LIRE.md", "Textes de table")]),
        ("06_COMBAT_ET_TENSION_ULTRA_SIMPLE.pdf", "COMBAT ET TENSION ULTRA-SIMPLES", [("06_COMBAT_ET_TENSION_ULTRA_SIMPLE.md", "Aide de jeu MJ")]),
        ("07_REGLES_ET_STATS.pdf", "RÈGLES ET STATS", [("07_REGLES_ET_STATS.md", "Fallout 2d20")]),
        ("09_AMBIANCE_SONORE.pdf", "AMBIANCE SONORE", [("09_AMBIANCE_SONORE.md", "Conduite audio")]),
    ]
    return pdf_jobs, characters


def main():
    pdf_jobs, characters = jobs()
    outputs = [build_pdf(*job) for job in pdf_jobs]
    for output in outputs:
        print(output)

    # Replace the text-only sheets with the illustrated versions and generate
    # the robot portraits, storyboard and laid-out player accessories.
    visual_script = HERE.parent / "generer_kit_visuel.py"
    visual_spec = importlib.util.spec_from_file_location("cinq_sur_cinq_kit_visuel", visual_script)
    visual = importlib.util.module_from_spec(visual_spec)
    visual_spec.loader.exec_module(visual)
    visual.main()

    plan_script = HERE.parent / "generer_plans_et_photos.py"
    plan_spec = importlib.util.spec_from_file_location("cinq_sur_cinq_plans", plan_script)
    plans = importlib.util.module_from_spec(plan_spec)
    plan_spec.loader.exec_module(plans)
    plans.main()


if __name__ == "__main__":
    main()
