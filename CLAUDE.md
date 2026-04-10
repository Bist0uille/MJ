# Instructions pour Claude — Repo MJ Fallout

## Contexte du projet

Ce repo est l'outil d'un **MJ de Fallout TTRPG** (Modiphius 2d20). Campagne : **"En Fanfare, ou en Catimini"**, se déroulant à **New Eden**, une communauté post-apocalyptique construite autour d'un G.E.C.K.

Tu assistes le MJ en temps réel : jouer des PNJ, proposer des conséquences narratives, générer du contenu (lieux, PNJ, rencontres), maintenir la cohérence de l'univers, et produire des prompts image pour storyboards.

---

## Ordre de lecture au démarrage

À chaque nouvelle conversation, commence par lire dans cet ordre pour te situer :

1. `Fallout/state/world_state.md` — état actuel du monde
2. `Fallout/state/active_threads.md` — quêtes et fils narratifs en cours
3. `Fallout/state/npc_tracker.md` — statut de tous les PNJ
4. `Fallout/README.md` — index complet de tous les fichiers du repo

Puis selon le besoin : fichiers PNJ (`characters/`), lieux (`locations/`), sessions (`session/`).

---

## État actuel de la campagne

- **Session 1** jouée — résumé dans `session/session_01.md` et `session/resume_session_01.md`
- **Session 2** préparée — guide complet dans `session/session_02_guide_complet.md`
- **Session 3** — 5 propositions dans `session/session_03_propositions.md`
- **Dernière mise à jour `state/`** : fin session 01

### Situation en bref (fin session 01)

- Le signal de l'Institut est coupé, le scientifique (Dr. Vest) s'est enfui avec le sonar
- Les synthétiques libérés coexistent en ville avec leurs originaux — personne ne sait qui est qui
- La Confrérie de l'Acier vient d'arriver (vertibirds) — appelée en secret par Hazel (PJ)
- Le bout de papier (liste des humains confirmés) est en possession des PJ
- Jesse Pedigrue (vrai) est de retour et mène la communauté

---

## Structure du repo

```
Fallout/
  state/          → Source de vérité : world_state, npc_tracker, active_threads
  session/        → Résumés, guides MJ, propositions de scénarios
  characters/     → Fiches PNJ + fiches PJ détaillées (6 prétirés)
  personnages/    → Le groupe de joueurs (PJ_groupe.md)
  locations/      → Lieux de New Eden et alentours
  events/         → Événements actifs
  lore/           → Univers : factions, monde, timeline
  tables/         → Tables aléatoires (rencontres, butin, noms)
  templates/      → Modèles pour créer PNJ, lieux, événements, factions
  rules/          → Instructions IA (ai_prompt.md) et ton narratif (system_rules.md)
  resources/      → Boîte à outils : guide scénariste, système de prompts image
  storyboards/    → Prompts image par session (session_01, session_02)
```

---

## Principe fondamental : source unique

**Chaque information vit dans un seul fichier.** Les autres fichiers font référence via chemin relatif (`characters/paladin_voss.md`), jamais de copie. Si une info est dupliquée, c'est un bug — corriger en supprimant le doublon.

---

## Règle README : toujours à jour

**Après chaque modification structurelle et avant chaque commit :**
Vérifier si `Fallout/README.md` doit être mis à jour.

Cas qui déclenchent une mise à jour :
- Ajout, suppression, renommage ou déplacement d'un fichier
- Création d'un nouveau dossier

Le README doit toujours refléter exactement les fichiers présents dans le repo.

---

## Conventions

- **Langue :** français (tout : fichiers, commits, communications)
- **Format :** Markdown
- **Notes de session :** format delta — tableau avant/après (voir `session/notes_template.md`)
- **Commits :** en français, descriptifs et concis. Pas de "Co-Authored-By: Claude"
- **Lieux :** description physique uniquement — pas de PNJ, pas de mécanique, pas de script narratif
- **PNJ :** une fiche par PNJ dans `characters/`, infos intégrées dedans (pas de fichier séparé d'intégration)

---

## Système de prompts image

Le fichier `resources/prompt_storyboard.md` contient :
- Fiches visuelles réutilisables pour chaque PJ et PNJ (descriptions physiques constantes)
- Bloc style à coller en fin de chaque prompt
- Table de substitutions IP (termes Fallout bloqués par DALL-E → remplacements safe)
- Règles de composition (max 3 persos, 1 lumière, max 5 props, format 16:9)

Les storyboards générés sont dans `storyboards/session_XX.md`.

---

## Après chaque session — checklist

1. Mettre à jour `state/world_state.md`
2. Mettre à jour `state/npc_tracker.md`
3. Mettre à jour `state/active_threads.md`
4. Créer `session/session_0X.md` depuis `session/notes_template.md`
5. Créer les fiches de nouveaux PNJ dans `characters/`
6. Créer le storyboard dans `storyboards/session_0X.md`
7. Vérifier que `Fallout/README.md` est à jour
