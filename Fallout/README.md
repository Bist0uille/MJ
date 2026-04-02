# Assistant MJ — Fallout: The RPG (Modiphius 2d20)

## Comment utiliser Claude comme assistant en partie

Pendant ta session, tu peux me demander directement :

### Génération à la volée
- "Génère un PNJ marchand hostile"
- "Donne-moi une rencontre aléatoire dans une zone irradiée"
- "Invente un nom pour un raider féminin"
- "Quel butin dans un bunker militaire abandonné ?"

### Aide aux règles 2d20
- "Rappelle-moi comment fonctionne le stress en combat"
- "Quelles compétences pour crocheter une serrure ?"
- "Comment gérer les munitions AP ?"

### Improvisation narrative
- "Mes joueurs vont dans une direction que j'avais pas prévue, aide-moi"
- "Invente un rebondissement pour cette quête"
- "Décris l'ambiance d'une ville fantôme des années 2180"

---

## Structure des fichiers

```
Fallout/
├── lore/
│   ├── monde.md         → Timeline, Grande Guerre, ambiance
│   └── factions.md      → Factions majeures et mineures
├── personnages/
│   ├── PNJ_template.md  → Modèle pour créer un PNJ rapidement
│   └── PJ_groupe.md     → Fiche du groupe de joueurs
├── tables/
│   ├── rencontres.md    → Tables de rencontres aléatoires
│   ├── butin.md         → Tables de butin
│   └── noms.md          → Générateur de noms
└── session/
    ├── notes_template.md   → Template notes de session
    └── scenario_vierge.md  → Structure pour préparer un scénario
```

---

## Rappel rapide 2d20

| Action | Difficulté de base |
|--------|-------------------|
| Tâche simple | 1 succès (CD 1) |
| Tâche complexe | 2 succès (CD 2) |
| Tâche difficile | 3+ succès (CD 3+) |

**Succès** = dé ≤ Attribut + Compétence  
**Complication** = résultat 20  
**Momentum** = succès en excès, partagés dans le pool du groupe  
**Menace** = pool du MJ, généré par complications ou actions des joueurs
