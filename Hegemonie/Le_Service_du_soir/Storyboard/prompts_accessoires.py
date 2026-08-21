# -*- coding: utf-8 -*-
"""Les 7 accessoires imprimables.

Cible visuelle DIFFERENTE des 10 scenes : ce sont des documents photographies
a plat, pas des plans de cinema. Meme discipline (une seule cible, aucune
negation), autre cible.

Aucune fiche personnage en reference : ce sont des objets.
"""

STYLE_PROPS = (
    "Flat overhead product photograph of a single physical document lying on a plain "
    "neutral surface, shot straight down, even diffuse studio lighting, the sheet "
    "filling the frame edge to edge, paper fibre and ink absorption visible at close "
    "range, crisp legible typography, realistic paper thickness and subtle surface "
    "relief, natural colour."
)

PROPS = [
    {
        "id": 1, "slug": "menu", "titre": "Le menu — À la Bonne Étoile",
        "ratio": "3:4", "seed": 220_001,
        "scene": (
            "A single printed restaurant menu card on cream laid paper, slightly worn at "
            "the corners, one small grease spot near the bottom edge. A hand-inked "
            "five-pointed star sits under the restaurant name. The layout is a classic "
            "bistro card: name, then four sections with dotted leader lines running to "
            "the prices.\n\n"
            "The card reads exactly, in this order:\n"
            '"À LA BONNE ÉTOILE"\n'
            '"— service du soir —"\n'
            '"ENTRÉES / Poulpe surprise .... 4 pa / Soupe du quartier .... 2 pa / '
            'Ancre confite (2 pers.) .... 9 pa"\n'
            '"PLATS / Mât grillé, jus court .... 11 pa / Ration de bord améliorée .... '
            '6 pa / LE RETOUR .... 14 pa"\n'
            '"FROMAGES / Le brebis affiné .... RÉSERVÉ"\n'
            '"DESSERTS / Ce qu\'il reste .... 3 pa"\n'
            '"Carte de fidélité : 10 repas = 1 offert. Réservation obligatoire."'
        ),
    },
    {
        "id": 2, "slug": "bulletin_vote", "titre": "Le bulletin de vote",
        "ratio": "3:4", "seed": 220_002,
        "scene": (
            "A paper prop for a fantasy tabletop game: a voting slip for an imaginary "
            "residents' association in a fictional floating town. Thin stock, one ink "
            "colour, ruled boxes and empty tick squares waiting to be filled, two "
            "sections separated by a horizontal line. The layout is plain and "
            "symmetrical, the work of a small association with no design budget.\n\n"
            "The slip reads exactly:\n"
            '"COPROPRIÉTÉ DU QUARTIER — ASSEMBLÉE GÉNÉRALE EXTRAORDINAIRE"\n'
            '"Chambre : [ ] propriétaires  [ ] locataires     Lot n° ____"\n'
            '"MOTION 1 — Abattage de la bête recueillie, selon la procédure de 1966.   '
            '[ ] POUR  [ ] CONTRE"\n'
            '"MOTION 2 — Mise en cause des occupants du lot 14, qui ont introduit ladite '
            'bête.   [ ] POUR  [ ] CONTRE"\n'
            '"Rappel : les deux chambres pèsent chacune 50% des voix exprimées, quel que '
            'soit le nombre de votants."\n'
            '"Les personnels logés par l\'employeur ne prennent pas part au vote."'
        ),
    },
    {
        "id": 3, "slug": "contrat_marmottes", "titre": "Le contrat des marmottes",
        "ratio": "3:4", "seed": 220_003,
        "scene": (
            "A paper prop for a fantasy tabletop game: an imaginary old work agreement on "
            "yellowed paper, typeset in small dense "
            "formal print with numbered articles, the whole sheet crowded and hard to "
            "read. The paper is worn soft along the fold lines and shows four decades of "
            "handling. At the bottom, a long row of tiny inked paw prints serves as "
            "signatures, dozens of them, pressed one after another.\n\n"
            "The contract reads exactly:\n"
            '"CONTRAT DE MISE À DISPOSITION DE FORCE MOTRICE"\n'
            '"Art. 1 — Le personnel s\'engage à assurer la rotation continue des tambours '
            'de la centrale."\n'
            '"Art. 4 — Le logement est fourni par l\'employeur. Le personnel logé ne peut '
            'se prévaloir de la qualité de locataire au sens du règlement de copropriété, '
            'et ne prend donc pas part aux votes de l\'assemblée."\n'
            '"Art. 7 — La durée quotidienne de service est fixée à treize (13) heures."\n'
            '"Art. 9 — Le personnel est informé de la destination du navire à chaque '
            'changement de cap."\n'
            '"Art. 12 — Le présent contrat est résiliable par le personnel avec un préavis '
            'de sept (7) jours."'
        ),
    },
    {
        "id": 4, "slug": "preavis_greve", "titre": "Le préavis de grève",
        "ratio": "3:4", "seed": 220_004,
        "scene": (
            "A single sheet of coarse brown paper nailed to a wooden door, photographed "
            "straight on, the nail heads visible at the top corners. The whole notice is "
            "handwritten in thick charcoal by someone who learned letters late: uneven "
            "baselines, letters of varying size, several words misspelled, one word "
            "crossed out and rewritten. The handwriting is earnest and careful.\n\n"
            "The notice reads exactly, misspellings included:\n"
            '"PRÉAVIS"\n'
            '"On cour plus."\n'
            '"On veux :"\n'
            '"— 13 heure de roue pas 18"\n'
            '"— 2 pause"\n'
            '"— que le contremaitre arette de crié « plus vite ». on entand. on cour déjà."\n'
            '"— savoir ou on va"\n'
            '"On est pas méchante. On atend."\n'
            '"Signé : les roues (toutes)"'
        ),
    },
    {
        "id": 5, "slug": "carte_six_zones", "titre": "La carte des six zones",
        "ratio": "1:1", "seed": 220_005,
        "scene": (
            "A single hand-drawn district map on thick sketch paper, ink and wash, drawn "
            "as a vertical stack of six labelled zones connected by a central line, like "
            "a cross-section of a settlement built in layers from bottom to top. Each "
            "zone is a rough box with a small drawn vignette inside it and a "
            "hand-lettered label. A large arrow runs up the left margin from bottom to "
            "top.\n\n"
            "The six zones are labelled, from bottom to top:\n"
            '"6. LE FOND" with a moored ship and a huge sleeping shape\n'
            '"5. LA GRAND-PLACE" with a lit restaurant front bearing a star\n'
            '"4. LA CENTRALE" with giant wheels and belts\n'
            '"3. LA CATHÉDRALE" with whale ribs and hanging harpoons\n'
            '"2. LE CIMETIÈRE" with broken wrecks and a small barge\n'
            '"1. L\'ÉVENT" with an opening and wind lines'
        ),
    },
    {
        "id": 6, "slug": "carte_rationnement", "titre": "La carte de rationnement",
        "ratio": "3:4", "seed": 220_006,
        "scene": (
            "A paper prop for a fantasy tabletop game: an imaginary residents' association "
            "notice on stiff pale card stock, printed with "
            "a list of five services and a tick box beside each, three boxes already "
            "crossed out in ink by hand, two still empty. A short polite paragraph closes "
            "the card, followed by a printed signature line.\n\n"
            "The card reads exactly:\n"
            '"COPROPRIÉTÉ DU QUARTIER — RATIONNEMENT — 3e JOUR"\n'
            '"Éclairage public [X]"\n'
            '"Treuils à marchandises [X]"\n'
            '"Pompes de la zone basse [X]"\n'
            '"Ascenseur de l\'Évent [ ]"\n'
            '"Chambre froide (Bonne Étoile) [ ]"\n'
            '"« Nous vous remercions de votre patience. La situation est en cours de '
            'résolution. » — le syndic"'
        ),
    },
    {
        "id": 7, "slug": "fausse_carte", "titre": "La fausse carte du quartier",
        "ratio": "3:4", "seed": 220_007,
        "scene": (
            "A single crumpled tourist map of a floating district, drawn hastily in cheap "
            "ink on thin paper that has been folded and unfolded many times, the creases "
            "worn through in two places. The drawing is confident and completely "
            "unreliable: zones in the wrong order, two districts that do not exist, a "
            "bold arrow pointing the wrong way, distances that contradict each other. A "
            "price is scrawled in the corner. It looks like it was drawn in four minutes "
            "and sold ten thousand times.\n\n"
            "Hand-lettered labels include: \"LE FOND\", \"LA GRAND-PLACE\", "
            "\"QUARTIER NEUF\", \"LES BAINS\", \"LA CENTRALE\", \"SORTIE\", "
            "\"2 pa — GARANTI\""
        ),
    },
]


def build_prop_prompt(prop: dict) -> str:
    return f"{prop['scene']}\n\nSTYLE: {STYLE_PROPS}"


def prop_by_id(prop_id: int) -> dict:
    for p in PROPS:
        if p["id"] == prop_id:
            return p
    raise KeyError(f"accessoire {prop_id} inconnu (1..{len(PROPS)})")
