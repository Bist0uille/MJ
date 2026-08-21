# -*- coding: utf-8 -*-
"""Storyboard « Le Service du soir » — donnees des 10 scenes.

C'est le SEUL fichier a editer pour retoucher un plan.
Regle absolue du STYLE : aucune negation, aucun nom de studio, une seule cible visuelle.
Ecrire « no grain » ne fait qu'ajouter le mot « grain » au prompt.
"""

# ---------------------------------------------------------------- style

STYLE = (
    "Cinematic 3D render, feature-animation production quality, physically based "
    "materials, ray-traced global illumination, volumetric light shafts, crisp "
    "micro-detail on fabric, wood and skin, deep focus, clean sharp edges, high "
    "dynamic range, controlled saturated palette."
)

# ---------------------------------------------------------------- personnages
# Les fiches sont envoyees en reference a chaque appel : le texte sert
# a nommer les personnages dans la scene, pas a les decrire de zero.

CHARACTERS = {
    "globou": (
        "Globou, a translucent blue plasmoid with a clearly defined humanoid body, "
        "wearing a dark navy hooded cloak with worn edges, thick leather belts and "
        "pouches, leather bracers and boots. His face is smooth and featureless, bearing "
        "only two black oval eyes. His gelatinous body glows softly from within."
    ),
    "phenokyo": (
        "Phenokyo, a pale dhampir woman with very long white hair fading to crimson at "
        "the tips, sharp crimson eyes, pointed ears. She wears a black gothic corset "
        "dress with a layered skirt, black gloves, white puff sleeves, black thigh-high "
        "boots, and an armored right leg traced with glowing blue magical lines."
    ),
    "motmot": (
        "Motmot, an anthropomorphic brown otter engineer with realistic animal "
        "proportions, wearing a white shirt, red tie, dark leather apron full of tools, "
        "leather gloves, sturdy boots, several utility belts, and a glowing blue astral "
        "crystal pinned on his chest."
    ),
    "bumbur": (
        "Bumbur, a cheerful round halfling cook with curly red hair and a short beard, "
        "a flour-covered apron and a large wooden spoon, warm and busy."
    ),
}

# Fichiers de reference, relatifs au dossier Hegemonie/
REFERENCE_FILES = {
    "globou": "globou.jpeg",
    "phenokyo": "phenokyo.jpeg",
    "motmot": "motmot.jpg",      # consigne explicite : celui-ci et pas un autre
    "bumbur": "bumbur.jpeg",
}

TRIO = ["globou", "phenokyo", "motmot"]
QUATUOR = ["globou", "phenokyo", "motmot", "bumbur"]

# ---------------------------------------------------------------- scenes

SCENES = [
    {
        "id": 1,
        "slug": "dernieres_reserves",
        "titre": "Les dernières réserves",
        "refs": TRIO,
        "seed": 110_001,
        "camera": "Wide interior shot, 35mm, slightly low angle, warm single-source lantern light from the left, deep shadows in the corners.",
        "scene": (
            "The cargo hold of an old astral sailing ship, becalmed for four months. "
            "Globou, Phenokyo and Motmot sit in silence around a rough wooden table with "
            "three empty plates holding only a few crumbs. Nobody eats. Nobody speaks. "
            "In the background stands a small wooden pen holding exactly two white sheep, "
            "one ram and one ewe, quietly watching them. Every gaze in the room drifts "
            "toward the sheep. The hold is packed with ropes, barrels, crates, tools and "
            "empty supply shelves. Two handwritten signs are nailed to a beam, reading "
            "exactly: RATIONS EPUISEES and CRISTAUX EN PANNE DEPUIS 4 MOIS. "
            "The mood is heavy and calm; everyone silently understands what everyone is "
            "thinking, and nobody says it."
        ),
    },
    {
        "id": 2,
        "slug": "le_mouton_senvole",
        "titre": "Le mouton s'envole",
        "refs": TRIO,
        "seed": 110_002,
        "camera": "Wide vertical composition, 28mm, low angle looking up toward the ceiling, dust and splinters caught in the lantern beam.",
        "scene": (
            "The same cargo hold, moments later. The ewe is floating upward toward the "
            "ceiling, her body inflated to roughly twice its normal size like an "
            "overinflated wool balloon while remaining unmistakably a sheep. The wooden "
            "ceiling planks crack and splinter as she rises. Globou, Phenokyo and Motmot "
            "have shot to their feet and stare upward in complete disbelief, one chair "
            "knocked over behind them. On the floor, the ram stays exactly where he is, "
            "head tilted all the way back, watching his companion float away with an "
            "utterly baffled expression, entirely unable to process what is happening. "
            "Wood splinters hang in the air. The moment feels frozen."
        ),
    },
    {
        "id": 3,
        "slug": "la_baleine_astrale",
        "titre": "La baleine astrale",
        "refs": TRIO,
        "seed": 110_003,
        "camera": "Extreme wide cosmic shot, 24mm, the ship tiny in the lower third of the frame, the whale filling the rest. Scale is the subject of this image.",
        "scene": (
            "An immense cosmic panorama. The tiny astral sailing ship drifts through "
            "glowing astral currents beneath countless stars and nebulae. Ahead of it "
            "rises a colossal astral whale, thousands of times larger than the ship, "
            "its skin marked with faint constellations. The whale is calmly opening its "
            "enormous mouth. The posture is gentle and parental throughout, that of an "
            "adult gathering up a child, and the ship simply happens to be what is "
            "around it. Globou, Phenokyo and Motmot stand together on the deck, "
            "impossibly small, looking up."
        ),
    },
    {
        "id": 4,
        "slug": "la_ville_dans_la_baleine",
        "titre": "La ville dans la baleine",
        "refs": TRIO,
        "seed": 110_004,
        "camera": "Wide establishing shot, 24mm, eye level from the ship's gangplank, warm lantern pools against the cool blue of the vault above.",
        "scene": (
            "The heroes step off their ship and discover an entire town built inside the "
            "living whale. About forty ships are permanently moored together into a "
            "single sprawling district, linked by wooden footbridges strung between the "
            "masts. Lanterns light the streets. Small restaurants, workshops, homes, "
            "laundry lines and vegetable gardens are built directly onto the old decks. "
            "Enormous whale ribs arch high overhead like the vault of a cathedral. "
            "Giant hermit crab citizens the size of humans sit in ornate spiral shells "
            "that are bolted and sealed directly onto the decks as permanent houses: "
            "they cannot move and they never do. One of them watches the newcomers with "
            "the exact expression of a man seeing a car park in his reserved space. "
            "Everyone behaves as though living inside a whale were completely ordinary. "
            "Globou, Phenokyo and Motmot stand frozen in amazement."
        ),
    },
    {
        "id": 5,
        "slug": "a_la_bonne_etoile",
        "titre": "À la Bonne Étoile",
        "refs": QUATUOR,
        "seed": 110_005,
        "camera": "Medium wide shot from the street, 35mm, shooting through the lit windows into the warm interior, the heroes in silhouette in the foreground.",
        "scene": (
            "A lively fantasy restaurant packed with customers. A large painted wooden "
            "sign above the door reads exactly: A LA BONNE ETOILE, with a single painted "
            "star beside the words. Inside, the entire staff are octopuses: an octopus "
            "maitre d' in a waistcoat seating guests, an octopus sommelier pouring wine "
            "with several arms at once, octopus commis clearing plates. Behind the pass "
            "stands Bumbur, the only non-octopus in the building, mid-service over a "
            "steaming pot. He has just spotted the heroes through the window and is "
            "waving at them with enormous delight, as though nothing whatsoever were "
            "unusual. Globou, Phenokyo and Motmot stand outside on the street, "
            "speechless. Warm light, laughter, great jars of honey and good food."
        ),
    },
    {
        "id": 6,
        "slug": "la_centrale_des_marmottes",
        "titre": "La centrale des marmottes",
        "refs": TRIO,
        "seed": 110_006,
        "camera": "Wide industrial shot, 24mm, strong perspective down the length of the hall, cold blue daylight from above against dead machinery.",
        "scene": (
            "An enormous industrial hall stretching far into the distance, three levels "
            "of gigantic wooden wheels, belts and gears standing completely still. "
            "Hundreds of marmot workers occupy the floor. Instead of working they sit in "
            "groups drinking coffee, playing cards, chatting and napping on the "
            "machinery. Some wear engineer goggles pushed up on their heads. They hold "
            "hand-painted strike placards whose lettering is clumsy and badly spelled, "
            "the work of people who never learned to write. A row of control dials on the "
            "wall all read zero. The entire ancient astral propulsion system has stopped. "
            "Globou, Phenokyo and Motmot look tiny before the dead machinery."
        ),
    },
    {
        "id": 7,
        "slug": "le_veau_qui_ecrase",
        "titre": "Le veau qui écrase le quartier",
        "refs": TRIO,
        "seed": 110_007,
        "camera": "Wide dramatic shot, 28mm, low angle from a collapsing footbridge, dust in the light, the creature filling two thirds of the frame.",
        "scene": (
            "The lower district of the whale town. An enormous half-transformed calf "
            "fills the entire street: a creature caught midway between sheep and whale, "
            "a vast pale body with patches of wool still clinging to smooth new skin, "
            "its eyes halfway migrated toward the sides of its head. It is far too big for "
            "the space. Its slow breathing is crushing the wooden footbridges and buckling "
            "the moored hulls around it; planks snap, ropes tear, lanterns fall. "
            "The creature is simply frightened and still growing; the damage is entirely "
            "accidental. "
            "Inhabitants flee along the upper walkways carrying what they can. "
            "Globou, Phenokyo and Motmot stand on a tilting bridge in the foreground, "
            "looking up at it, tiny and helpless."
        ),
    },
    {
        "id": 8,
        "slug": "l_assemblee",
        "titre": "L'Assemblée générale",
        "refs": QUATUOR,
        "seed": 110_008,
        "camera": "Huge symmetrical cinematic composition, 24mm, from behind and above the heroes, the whole crowd facing them, blue window light from above.",
        "scene": (
            "A vast cathedral built inside the fossilised skeleton of a young whale. "
            "Immense curved ribs rise like gothic columns; soft blue light filters through "
            "stained-glass windows set with astral crystals. Huge old harpoons hang high "
            "on the bone walls, displayed like relics, tarnished with age. "
            "The entire town has gathered for an emergency assembly, split into two "
            "distinct halves: on one side, rows of giant hermit crabs sealed into "
            "ornate shells bolted permanently to the floor, unable to move, holding paper "
            "ballots; on the other, thousands of sardines suspended in floating spheres of "
            "magical water. Marmots crowd at the back, standing, hands raised. "
            "Octopus merchants and Bumbur stand at the side. Every single face is turned "
            "toward the centre, where Globou, Phenokyo and Motmot stand alone. "
            "The whole town is waiting for their answer."
        ),
    },
    {
        "id": 9,
        "slug": "le_premier_chant",
        "titre": "Le premier chant",
        "refs": TRIO,
        "seed": 110_009,
        "camera": "Wide low-angle hero shot, 28mm, looking up into the opening, strong golden backlight, long shadows thrown toward the camera.",
        "scene": (
            "The young whale, now fully transformed, opens its mouth and sings for the "
            "very first time. Ahead of it, the vast mouth of the mother whale is opening "
            "onto the astral ocean, and golden light floods in through the enormous "
            "opening, sweeping across the entire moored town. Visible rings of glowing "
            "astral energy ripple outward through the air with the sound. Loose objects, "
            "laundry, papers and lanterns lift and drift toward the light. Every "
            "inhabitant has stopped and is looking upward in complete silence. "
            "Globou, Phenokyo and Motmot stand together in the foreground, watching. "
            "This is the emotional climax of the story."
        ),
    },
    {
        "id": 10,
        "slug": "les_retrouvailles",
        "titre": "Les retrouvailles",
        "refs": TRIO,
        "seed": 110_010,
        "camera": "Extreme wide closing shot, 24mm, three-quarter rear view over the ship's stern, the two whales large in frame, deep starfield behind.",
        "scene": (
            "The endless astral currents. The young whale, fully grown into itself at "
            "last, swims joyfully alongside its enormous mother through glowing streams "
            "of starlight. The small sailing ship follows peacefully in their wake. "
            "Globou, Phenokyo and Motmot stand together at the stern rail, watching the "
            "reunion. Stars, nebulae and astral currents light the whole scene in blues "
            "and warm golds. The image should feel like hope, freedom, and the opening of "
            "a new adventure."
        ),
    },
]


def build_prompt(scene: dict) -> str:
    """Assemble le prompt final d'une scene."""
    who = "\n".join(CHARACTERS[k] for k in scene["refs"])
    return (
        f"{scene['scene']}\n\n"
        f"CHARACTERS IN THIS IMAGE (match the attached reference sheets exactly):\n{who}\n\n"
        f"CAMERA: {scene['camera']}\n\n"
        f"STYLE: {STYLE}"
    )


def scene_by_id(scene_id: int) -> dict:
    for s in SCENES:
        if s["id"] == scene_id:
            return s
    raise KeyError(f"scene {scene_id} inconnue (1..{len(SCENES)})")
