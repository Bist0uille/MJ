# Storyboard — Le Service du soir

10 images pour le one-shot, générées via **fal.ai / Nano Banana 2 Edit**, avec les fiches de personnages passées en référence sur chaque appel.

---

## Pourquoi ça remplace ChatGPT web

| Problème du web | Correctif ici |
|---|---|
| Le bloc style contenait **9 négations** (`no film grain`, `no watercolor`, `no blur`…). Le modèle n'a pas de canal négatif : ces textures sales étaient simplement **nommées** dans le prompt | **Zéro négation de style.** Vérifié par lint |
| `Weta Workshop concept art` et `ILM` sont des références de **peinture** — la cause directe du rendu pictural | Supprimés. **Une seule cible visuelle** : rendu 3D de film d'animation |
| `Unreal Engine 5` + `photorealistic CGI` + `concept art` = trois directions incompatibles | Une seule direction cohérente |
| `8K`, `ultra sharp focus` : bruit de tokens sans effet | Supprimés, remplacés par du **langage caméra** réel (valeur de plan, focale, source de lumière) |
| Pas de seed, pas de résolution, recompression en sortie | **Seed fixe par scène**, résolution au choix, PNG brut |
| Cohérence obtenue par la phrase *« always identical to the reference sheet »* | Les **fiches sont réellement envoyées** en image de référence à chaque appel |

---

## Utilisation

Le venv à utiliser est celui d'`IA_avatar` (il a déjà `fal_client`) :

```
PY="/c/Users/aigen/Desktop/Informatique/IA_avatar/.venv-fal/Scripts/python.exe"
```

### Voir le plan sans rien dépenser
```bash
$PY generate.py --all
```
Affiche le JSON d'estimation (images, résolution, coût) et s'arrête. **C'est le comportement par défaut.**

### Générer une seule scène
```bash
$PY generate.py --scene 1 --confirm-spend
```

### Générer les dix
```bash
$PY generate.py --all --confirm-spend
```

### Refaire un plan qui ne va pas
Même seed → même image. Pour obtenir autre chose, change le seed :
```bash
$PY generate.py --scene 7 --seed 99 --confirm-spend
```
Si le nouveau tirage est le bon, reporte `99` dans `prompts.py` pour le figer.

### Moins cher
```bash
$PY generate.py --all --resolution 1k --confirm-spend
```

---

## Coût

**$0.08 par image en 1K**, ×1,5 en 2K, ×2 en 4K.

| | Images | Coût |
|---|---|---|
| Test — une scène en 2K | 1 | $0.12 |
| **Les 10 en 2K** *(défaut)* | 10 | **$1.20** |
| Les 10 en 1K | 10 | $0.80 |
| Les 10 en 4K | 10 | $1.60 |

**Rien n'est dépensé sans `--confirm-spend`.** Le coût réel de chaque image est journalisé dans `out/runs.jsonl`.

---

## Fichiers

| | |
|---|---|
| **`prompts.py`** | **Le seul fichier à éditer.** Bloc style, descriptions des personnages, les 10 scènes avec seed, caméra et références |
| `generate.py` | Appel fal, téléchargement, journal. Convention reprise de `IA_avatar/pipeline/generate_fal_kling_batch.py` |
| `PROMPTS.md` | Les 10 prompts assemblés, en clair, copiables ailleurs. **Régénéré depuis `prompts.py`, ne pas éditer à la main** |
| `out/` | Les images, nommées `01_dernieres_reserves.png`… |
| `out/runs.jsonl` | Une ligne par génération : scène, seed, coût, durée |

Les fiches de référence sont dans le dossier parent : `globou.jpeg`, `phenokyo.jpeg`, **`motmot.jpg`**, `bumbur.jpeg`.

---

## Les 10 scènes

| # | Titre | Personnages |
|---|---|---|
| 1 | Les dernières réserves | trio |
| 2 | Le mouton s'envole | trio |
| 3 | La baleine astrale | trio |
| 4 | La ville dans la baleine | trio |
| 5 | À la Bonne Étoile | trio + Bumbur |
| 6 | La centrale des marmottes | trio |
| 7 | Le veau qui écrase le quartier | trio |
| 8 | L'Assemblée générale | trio + Bumbur |
| 9 | Le premier chant | trio |
| 10 | Les retrouvailles | trio |

### Recalage sur la v3 du scénario

Les scènes d'origine avaient dérivé. Corrections apportées :

- **Scène 5** — « Chez Bumbur » → **À la Bonne Étoile**, enseigne au bon nom, et **tout le personnel est composé de poulpes** (Bumbur est le seul non-poulpe de l'établissement).
- **Scène 7** — le bébé baleine endormi dans la cathédrale était l'erreur principale : la cathédrale **est** le squelette du veau mort de 1966. La scène devient **le veau vivant qui écrase le quartier**, le plan qui manquait.
- **Scène 8** — l'Assemblée se tient **dans la cathédrale**, donc dans ce squelette, **sous les grands harpons** de 1966 accrochés au mur. Assemblée bicamérale : bernard-l'ermite propriétaires scellés au pont d'un côté, sardines locataires en sphères d'eau de l'autre.
- **Scène 4** — les bernard-l'ermite sont **scellés au pont**, pas en train de se promener avec leur coquille. Ils ne peuvent pas bouger, c'est tout leur personnage.
- **Scène 2** — c'est **la femelle** qui décolle, et **le mâle la regarde**.
- **Scène 6** — les pancartes de grève sont **mal écrites et pleines de fautes** : les marmottes ne savent pas écrire.
