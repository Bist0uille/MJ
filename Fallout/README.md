# Base de données campagne — En Fanfare, ou en Catimini

> Ce dossier est la source de vérité de la campagne.
> Claude lit ces fichiers pour assister le MJ en temps réel.
> Tout ce qui est vrai dans le monde de New Eden est écrit ici.

---

## Utilisation rapide en session

Exemples de questions à poser à Claude avec ce repo en contexte :

| Besoin | Question |
|--------|----------|
| État du monde | *"Quel est l'état actuel de New Eden ?"* |
| Jouer un PNJ | *"Comment jouer Paladin Voss si les joueurs la confrontent ?"* |
| Options narratives | *"Quelles sont les options des joueurs cette nuit ?"* |
| Conséquence | *"Que se passe-t-il si les PJ donnent le registre à Jesse ?"* |
| PNJ à la volée | *"Génère un marchand itinérant pour la place centrale."* |
| Résumé | *"Résume ce qui s'est passé en session 1."* |
| Tirage aléatoire | *"Tire une rencontre de Wasteland pour la zone nord."* |

**Ordre de lecture prioritaire :** `state/world_state.md` → `state/active_threads.md` → fichier PNJ ou lieu concerné → `rules/system_rules.md`

---

## État de la campagne

| Élément | Statut |
|---------|--------|
| Session 1 | Jouée — résumé dans `session/session_01.md` |
| Session 2 | Préparée — guide complet dans `session/session_02_guide_complet.md` |
| Session 3 | 5 propositions dans `session/session_03_propositions.md` |
| Dernière mise à jour `state/` | Fin session 01 |

---

## Structure des dossiers

### `state/` — L'état du monde (lire en premier)

| Fichier | Contenu |
|---------|---------|
| `world_state.md` | État actuel de New Eden — G.E.C.K., signal, synthétiques, Confrérie |
| `npc_tracker.md` | Tableau de statut de tous les PNJ — vivant/mort, localisation, disposition |
| `active_threads.md` | Quêtes actives, décisions en attente, mystères ouverts |

### `session/` — Historique et préparation

| Fichier | Contenu |
|---------|---------|
| `session_01.md` | Résumé session 1 — format delta (avant/après) |
| `resume_session_01.md` | Résumé narratif complet de la session 1 — pour relecture ou récap joueurs |
| `session_02_guide_complet.md` | Guide MJ détaillé session 2 "Les Couleurs qu'on Arbore" — scènes, dialogues, mécanique, les 3 aubes possibles |
| `session_02_propositions.md` | Version condensée du scénario session 2 (Confrérie) |
| `session_02_propositions_bis.md` | Scénario alternatif session 2 "Ce qu'on t'a pris" (crise interne, sans Confrérie) |
| `session_03_propositions.md` | 5 propositions pour la suite — diplomatie, identité, traque, trahison, reconstruction |
| `pretires_integration.md` | Supplément MJ — crochets scénaristiques, questions de fête, fractures identitaires de chaque prétirés |
| `notes_template.md` | Modèle de prise de notes post-session |
| `scenario_vierge.md` | Modèle de scénario vierge |

### `personnages/` — Le groupe de joueurs

| Fichier | Contenu |
|---------|---------|
| `PJ_groupe.md` | Les 6 prétirés — backgrounds, connexions, secrets MJ, état post-session 1 |

### `characters/` — PNJ et fiches PJ détaillées

**PNJ :**

| Fichier | Rôle |
|---------|------|
| `jesse_pedigrue.md` | Maire de New Eden — symbole de la réconciliation |
| `joseph.md` | Goule lucide — premier cas de dégradation, ligoté à la clinique |
| `theresa.md` | Goule lucide — morte session 01, membre fondatrice |
| `paladin_voss.md` | Confrérie de l'Acier — commandante locale, 44 ans, test d'empathie |
| `scribe_kern.md` | Confrérie — technicien, obsédé par le G.E.C.K. |
| `dr_rolan_vest.md` | Scientifique Institut — architecte de l'expérience, en fuite avec le sonar |

**PJ (fiches détaillées) :**

| Fichier | Personnage |
|---------|-----------|
| `vieux_colosse.md` | Super Mutant, 200 ans, philosophe, bâtisseur de la muraille nord |
| `bailey_tout_sourire.md` | Goule, logistique clinique, sourire de Glasgow permanent |
| `tommy_doyle.md` | Survivant de Diamond City, arnaqueur charmeur, comptoir d'échange |
| `hazel_johnson.md` | Initiée Confrérie, soigneuse, a appelé la Confrérie en secret |
| `augusta_byron.md` | Génie informatique, Abri 75, a câblé le générateur |
| `marvin.md` | Mister Handy, observateur, suit le signal de l'Institut |

### `locations/` — Lieux clés

| Fichier | Lieu |
|---------|------|
| `new_eden.md` | La communauté — G.E.C.K., place centrale, muraille nord, vue d'ensemble |
| `clinique.md` | Centre médical — réception, salles de soins, bureau du médecin |
| `parc.md` | Espace vert — fontaine, arbre aux noms, bancs |
| `comptoir_commercial.md` | Marché communautaire — comptoir principal + comptoir informel de Tommy |
| `bar.md` | Bar — comptoir, jukebox, salle de la Fête des Fondateurs |
| `grotte_vieux_colosse.md` | Cavité naturelle — 200 ans d'occupation solitaire, livres anciens |
| `ferme_joseph_theresa.md` | Ferme en périphérie — scène de crime session 01 |
| `complexe_institut.md` | Installation souterraine de l'Institut — neutralisée en session 01 |

### `events/` — Événements actifs

| Fichier | Événement |
|---------|-----------|
| `arrivee_vertibirds.md` | L'arrivée de la Confrérie sur New Eden — structure de la session 2 |

### `lore/` — Référence univers

| Fichier | Contenu |
|---------|---------|
| `monde.md` | Timeline, zones géographiques, créatures, économie du Wasteland |
| `factions.md` | Vue d'ensemble des factions (Confrérie, Institut, Raiders, etc.) |

### `tables/` — Tables aléatoires

| Fichier | Usage |
|---------|-------|
| `rencontres.md` | Rencontres aléatoires par zone |
| `butin.md` | Loot et récompenses |
| `noms.md` | Noms de PNJ générés |

### `templates/` — Modèles réutilisables

| Template | Pour créer |
|----------|-----------|
| `character_template.md` | Un nouveau PNJ → `characters/nom.md` |
| `location_template.md` | Un nouveau lieu → `locations/nom.md` |
| `event_template.md` | Un nouvel événement → `events/nom.md` |
| `faction_template.md` | Une nouvelle faction → `lore/nom.md` |
| `session_template.md` | Redirige vers `session/notes_template.md` |

### `rules/` — Instructions IA et ton narratif

| Fichier | Contenu |
|---------|---------|
| `ai_prompt.md` | Comment Claude doit se comporter en session — priorités, formats, interdits |
| `system_rules.md` | Ton narratif, causalité, comportement des PNJ |

### `resources/` — Boîte à outils

| Fichier | Contenu |
|---------|---------|
| `README.md` | Index des ressources externes + liens utiles communauté Fallout 2d20 |
| `boite_a_outils_scenariste.md` | Guide de conception de scénarios Fallout — formule narrative, construction de lieux, PNJ, dilemmes |
| `prompt_storyboard.md` | Système de prompts image — fiches visuelles personnages, bloc style, substitutions IP, template de scène |
| `storyboard_session_02.md` | 10 prompts storyboard prêts à l'emploi pour la session 2 |

---

## Après chaque session — checklist

1. Mettre à jour `state/world_state.md` avec les changements d'état
2. Mettre à jour `state/npc_tracker.md` — nouveaux PNJ, morts, déplacements
3. Mettre à jour `state/active_threads.md` — quêtes résolues, nouvelles menaces
4. Créer `session/session_0X.md` à partir de `session/notes_template.md`
5. Créer les fiches de nouveaux PNJ rencontrés dans `characters/`
6. Vérifier que ce README reflète les fichiers ajoutés

---

## Principe fondamental

**Source unique par entité.** Chaque information vit dans un seul fichier. Les autres fichiers font référence via chemin relatif (`/characters/paladin_voss.md`), jamais de copie. Si une info est dupliquée, c'est un bug.
