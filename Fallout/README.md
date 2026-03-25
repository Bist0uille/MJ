# Assistant MJ — En Fanfare, ou en Catimini
## Fallout: The RPG (Modiphius 2d20) — Campagne New Eden

> Ce dossier est la base de données de la campagne.
> Claude lit ces fichiers pour assister le MJ en temps réel pendant les sessions.

---

## Utilisation rapide en session

- *"Quel est l'état actuel de New Eden ?"*
- *"Comment jouer Paladin Voss si les joueurs la confrontent ?"*
- *"Rappelle-moi ce que Vest peut offrir aux joueurs."*
- *"Quelles sont les options des joueurs cette nuit ?"*
- *"Résume ce qui s'est passé en session 1."*

**Fichiers prioritaires :** `state/world_state.md` → `state/active_threads.md` → fichier PNJ/lieu concerné

---

## Structure

```
Fallout/
│
├── state/                      ← PRIORITÉ 1 — lire en premier
│   ├── world_state.md          État actuel de New Eden, statut de chaque élément clé
│   └── active_threads.md       Quêtes actives, décisions joueurs, menaces, mystères
│
├── session/                    ← Historique et préparation des sessions
│   ├── session_01.md           Résumé session 1 — "En Fanfare, ou en Catimini"
│   ├── session_02_propositions.md   Guide session 2 — "Les Couleurs qu'on Arbore"
│   ├── session_03_propositions.md   5 propositions post-crise Confrérie
│   ├── notes_template.md       Modèle de notes de session
│   └── scenario_vierge.md      Modèle de scénario vierge
│
├── personnages/                ← Fiche groupe joueurs
│   └── PJ_groupe.md            Les 6 prétirés avec backgrounds, connexions, secrets MJ
│
├── characters/                 ← PNJ nommés
│   ├── jesse_pedigrue.md       Maire de New Eden — symbole de la réconciliation
│   ├── paladin_voss.md         Confrérie de l'Acier — commandante locale
│   ├── scribe_kern.md          Confrérie — technicien, danger sur le G.E.C.K.
│   ├── dr_rolan_vest.md        Scientifique Institut — architecte de l'expérience
│   │
│   ├── augusta_byron.md        PJ — Génie informatique, Abri 75
│   ├── tommy_doyle.md          PJ — Survivant, Diamond City
│   ├── bailey_tout_sourire.md  PJ — Goule, logistique clinique
│   ├── vieux_colosse.md        PJ — Super Mutant, 200 ans d'existence
│   ├── hazel_johnson.md        PJ — Initiée Confrérie, soigneuse
│   └── marvin.md               PJ — Mister Handy, observateur
│
├── locations/                  ← Lieux clés
│   └── new_eden.md             La communauté — G.E.C.K., place centrale, clinique
│
├── events/                     ← Événements actifs
│   └── arrivee_vertibirds.md   L'arrivée de la Confrérie — structure session 2
│
├── lore/                       ← Référence univers Fallout
│   ├── monde.md                Timeline, zones, créatures, économie (référence → new_eden.md pour le contexte)
│   └── factions.md             Vue d'ensemble des factions (lore général)
│
├── tables/                     ← Tables aléatoires
│   ├── rencontres.md
│   ├── butin.md
│   └── noms.md
│
├── templates/                  ← Modèles réutilisables
│   ├── character_template.md
│   ├── location_template.md
│   ├── faction_template.md
│   ├── event_template.md
│   └── session_template.md     (redirect → session/notes_template.md)
│
├── rules/                      ← Règles et instructions
│   ├── ai_prompt.md            Instructions pour Claude en session
│   └── system_rules.md         Ton, causalité, comportement PNJ
│
└── resources/                  ← Ressources générales
    └── README.md
```

---

## Rappel règles 2d20 (Modiphius)

| Élément | Règle |
|---------|-------|
| Succès | dé ≤ Attribut + Compétence |
| CD 1 / 2 / 3 | Simple / Difficile / Très difficile |
| Momentum | Succès en excès → pool groupe |
| Menace | Pool MJ → complications, effets spéciaux |
| Stress | Dommage mental/social (séparé des PV) |

---

## Ajouter du contenu

- **Nouveau PNJ :** copier `templates/character_template.md` → `characters/nom.md`
- **Nouveau lieu :** copier `templates/location_template.md` → `locations/nom.md`
- **Nouvel événement :** copier `templates/event_template.md` → `events/nom.md`
- **Après chaque session :** mettre à jour `state/world_state.md` + `state/active_threads.md` + créer `session/session_0X.md`
