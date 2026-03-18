# Assistant MJ — Fallout: The RPG (Modiphius 2d20)

> Ce dossier est la base de données de ta campagne Fallout.
> Claude lit ces fichiers pour t'assister en temps réel pendant les sessions.

---

## Utilisation rapide en session

Envoie directement ta demande :
- *"Génère un PNJ marchand à Portail-Sud"*
- *"Quelle conséquence si les joueurs brûlent le blocus ?"*
- *"Décris l'arrivée à Greyfall la nuit"*
- *"Tire une rencontre dans le Wasteland ouvert"*
- *"Résume l'état du monde actuel"*

**Fichiers prioritaires :** `state/world_state.md` → `state/active_threads.md` → faction/lieu concerné

---

## Structure

```
Fallout/
│
├── state/                   ← PRIORITÉ 1 — lire en premier
│   ├── world_state.md       État actuel du monde, factions, conflits
│   └── active_threads.md    Quêtes actives, décisions joueurs, menaces
│
├── rules/                   ← PRIORITÉ 2 — logique narrative
│   ├── ai_prompt.md         Instructions pour Claude en session
│   └── system_rules.md      Ton, causalité, comportement PNJ
│
├── factions/                ← Fiches détaillées par faction
│   ├── fils_du_cendre.md
│   └── ligue_marchands.md
│
├── characters/              ← PNJ nommés
│   ├── hendrick_cole.md
│   ├── silas_vorne.md
│   └── nora_sept_fers.md
│
├── locations/               ← Lieux clés
│   ├── portail_sud.md
│   └── greyfall.md
│
├── events/                  ← Conflits et événements actifs
│   └── blocus_route7.md
│
├── sessions/                ← Historique des sessions
│   ├── session_01.md        Exemple rempli
│   ├── notes_template.md
│   └── scenario_vierge.md
│
├── lore/                    ← Référence univers Fallout
│   ├── monde.md             Timeline, zones, créatures, économie
│   └── factions.md          Vue d'ensemble des factions (lore général)
│
├── personnages/             ← Fiche groupe joueurs
│   └── PJ_groupe.md
│
├── tables/                  ← Tables aléatoires
│   ├── rencontres.md
│   ├── butin.md
│   └── noms.md
│
├── templates/               ← Modèles réutilisables
│   ├── faction_template.md
│   ├── location_template.md
│   ├── character_template.md
│   ├── event_template.md
│   └── session_template.md
│
└── resources/               ← PDFs, scénarios, ressources externes
    └── (ajouter ici tes fichiers)
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
- **Nouvelle faction :** copier `templates/faction_template.md` → `factions/nom.md`
- **Nouvel événement :** copier `templates/event_template.md` → `events/nom.md`
- **Après chaque session :** mettre à jour `state/world_state.md` + `state/active_threads.md`
- **Ressources externes :** déposer dans `resources/`
