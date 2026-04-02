# MJ Fallout — Assistant IA pour Maître du Jeu

Une base de connaissances structurée pour mener une campagne **Fallout: The RPG** (Modiphius, 2d20) assistée par **Claude** (Anthropic) en temps réel.

Le MJ pose des questions en langage naturel pendant la session. Claude lit les fichiers du repo, connaît l'état du monde, les PNJ, les quêtes en cours, et répond avec le bon ton, les bonnes infos, et les bonnes options narratives.

---

## La campagne : "En Fanfare, ou en Catimini"

**Lieu :** New Eden — une communauté post-apocalyptique bâtie autour d'un G.E.C.K. opérationnel, le seul documenté dans le secteur.

**Pitch :** L'Institut a infiltré la ville avec des copies synthétiques de ses habitants. Les joueurs ont libéré les prisonniers et les copies — mais maintenant, personne ne sait qui est qui. Et la Confrérie de l'Acier vient d'atterrir.

**Thèmes :** Identité, cohabitation, loyauté, bureaucratie comme violence, le droit d'exister.

**Joueurs :** 4 personnages prétirés actifs — un Super Mutant philosophe, une Goule souriante, un arnaqueur charmeur, et une initiée de la Confrérie qui a trahi les siens.

---

## Comment ça marche

### En session

Le MJ utilise Claude (via Claude Code, l'API, ou claude.ai) avec ce repo comme contexte. Il pose des questions comme :

- *"Comment jouer Paladin Voss si les joueurs la confrontent ?"*
- *"Quelles sont les options des joueurs cette nuit ?"*
- *"Génère un PNJ marchand pour la place centrale."*
- *"Quelle conséquence si les joueurs donnent le registre à Jesse ?"*

Claude lit `state/world_state.md` en priorité, puis les fichiers pertinents, et répond dans le ton de la campagne.

### Entre les sessions

Le repo sert de mémoire de campagne :

1. **Mettre à jour l'état du monde** — `state/world_state.md` + `state/npc_tracker.md` + `state/active_threads.md`
2. **Créer les notes de session** — copier `session/notes_template.md` → `session/session_0X.md`
3. **Ajouter des PNJ / lieux / événements** — utiliser les templates dans `templates/`
4. **Préparer la session suivante** — écrire ou demander à Claude de générer des propositions de scénario

### Génération d'images

Le repo contient un système de prompts pour générer des illustrations cohérentes de session en session :

- **`resources/prompt_storyboard.md`** — Fiches visuelles de chaque personnage (copier-coller), bloc style commun, table de substitutions IP (les termes Fallout que DALL-E bloque), template de composition de scène, checklist
- **`resources/storyboard_session_02.md`** — Exemple : 10 prompts prêts à l'emploi pour la session 2

Les descriptions visuelles des personnages sont figées dans les fiches. On les réutilise d'une image à l'autre pour garder la cohérence.

---

## Structure du repo

```
Fallout/
├── state/           Priorite 1 — etat actuel du monde, PNJ, quetes
├── session/         Historique des sessions + scenarios a venir
├── personnages/     Fiches des PJ (backgrounds, secrets MJ)
├── characters/      Fiches PNJ (motivations, comportement, liens)
├── locations/       Lieux cles (New Eden, Institut, ferme)
├── events/          Evenements actifs (arrivee Confrerie)
├── lore/            Reference univers (factions, monde)
├── tables/          Tables aleatoires (rencontres, butin, noms)
├── templates/       Modeles pour creer du contenu
├── rules/           Instructions pour Claude + regles de ton
└── resources/       Boite a outils, prompts image, storyboards
```

**Principe : source unique par entite.** Chaque info vit dans un seul fichier. Les autres fichiers font reference via chemin relatif, jamais de copie.

---

## Ordre de lecture pour Claude

Claude est instruit (via `rules/ai_prompt.md` et `CLAUDE.md`) de lire dans cet ordre :

1. `state/world_state.md` — qu'est-ce qui est vrai maintenant ?
2. `state/active_threads.md` — quelles quetes sont en cours ?
3. `characters/` ou `locations/` — le PNJ ou le lieu concerne
4. `rules/system_rules.md` — ton, causalite, comportement PNJ

---

## Ajouter du contenu

| Action | Comment |
|--------|---------|
| Nouveau PNJ | `templates/character_template.md` → `characters/nom.md` |
| Nouveau lieu | `templates/location_template.md` → `locations/nom.md` |
| Nouvel evenement | `templates/event_template.md` → `events/nom.md` |
| Nouvelle faction | `templates/faction_template.md` → `lore/nom.md` |
| Apres chaque session | Mettre a jour `state/` + creer `session/session_0X.md` |
| Nouveau storyboard | Utiliser les fiches de `resources/prompt_storyboard.md` |

---

## Regles 2d20 — aide-memoire

| Element | Regle |
|---------|-------|
| Succes | de <= Attribut + Competence |
| CD 1 / 2 / 3 | Simple / Difficile / Tres difficile |
| Momentum | Succes en exces → pool groupe |
| Menace | Pool MJ → complications, effets speciaux |
| Stress | Dommage mental/social (separe des PV) |

---

## Stack technique

- **Fichiers :** Markdown uniquement — lisible par humains et par IA
- **IA :** Claude (Anthropic) — via Claude Code CLI, API, ou claude.ai
- **Images :** DALL-E (ChatGPT) ou Midjourney — prompts dans `resources/`
- **Systeme de JdR :** Fallout 2d20 (Modiphius Entertainment)

---

## Licence

Usage personnel. L'univers Fallout appartient a Bethesda Softworks. Le systeme 2d20 appartient a Modiphius Entertainment. Ce repo ne contient aucun contenu sous licence — uniquement du contenu original (scenarios, PNJ, lore custom).
