# Instructions pour Claude — Repo MJ Fallout

## Règle principale : README toujours à jour

**Après chaque modification de fichier et avant chaque commit :**
Vérifier si `Fallout/README.md` doit être mis à jour.

Cas qui déclenchent une mise à jour du README :
- Ajout d'un fichier dans `locations/`, `characters/`, `events/`, `session/`, `lore/`, `tables/`, `templates/`
- Suppression d'un fichier existant référencé dans le README
- Renommage ou déplacement d'un fichier
- Création d'un nouveau dossier

Le README doit toujours refléter exactement les fichiers présents dans le repo.
Ne jamais committer une modification structurelle sans avoir vérifié et mis à jour le README si besoin.

---

## Structure du projet

Campagne Fallout TTRPG (Modiphius 2d20) — "En Fanfare, ou en Catimini"
Dossier principal : `Fallout/`

Principe : **source unique par entité**. Chaque information vit dans un seul fichier.
Les autres fichiers référencent via chemin (`/characters/paladin_voss.md`), jamais de copie.

---

## Conventions

- Langue : français
- Format : Markdown
- Notes de session : format delta (tableau avant/après dans `session/notes_template.md`)
- Pas de "Co-Authored-By: Claude" dans les commits
- Commits en français, descriptifs et concis
