# Système de Prompts Storyboard — New Eden

> Fiches visuelles réutilisables pour générer des images cohérentes session après session.
> Copier-coller les blocs personnages + le bloc style dans chaque prompt.

---

## RÈGLES DE COMPOSITION

1. **Max 3 personnages bien décrits par image.** Au-delà, les visages deviennent génériques.
2. **1 source de lumière dominante par scène.** Pas de contradictions (pas "harsh sunlight" + "moonlit").
3. **Max 4-5 éléments d'environnement.** Trop de props = image générique.
4. **Toujours terminer par le BLOC STYLE.**
5. **Ne jamais utiliser les termes IP** (voir section Substitutions).
6. **Format : paysage 16:9** — toujours préciser en fin de prompt.

---

## BLOC STYLE (à coller à la fin de chaque prompt)

```
cinematic digital oil painting, retro-futuristic 1950s-inspired post-apocalyptic aesthetic, painterly brushwork with visible texture, dramatic cinematic lighting, muted earthy palette dominated by amber rust and ochre, highly detailed character faces and textures, movie concept art quality, landscape format 16:9
```

Pour Midjourney : ajouter `--ar 16:9` après le prompt.

---

## SUBSTITUTIONS IP — Termes interdits et remplacements

Ne JAMAIS utiliser ces termes dans un prompt DALL-E (blocage IP protégée) :

| Terme interdit | Remplacement |
|---------------|-------------|
| Fallout | *(ne pas nommer — décrire l'esthétique directement)* |
| Brotherhood of Steel | *militarized tech-religious order in heavy steel power armor* |
| Super Mutant | *massive bald heavily mutated humanoid with olive-green leathery skin* |
| Nuka-Cola | *retro 1950s-style soda bottles / red-and-white soda vending machine* |
| Vault-Tec | *underground bunker corporation* |
| Vault (abri) | *underground bunker / sealed survival shelter* |
| Institute | *sterile white underground sci-fi laboratory* |
| Vertibird | *military VTOL aircraft / tiltrotor gunship* |
| Stimpak | *orange-and-white medical auto-injector syringe* |
| RadAway | *IV medical bag with radiation treatment fluid* |
| Mentats | *retro tin of stimulant pills* |
| Power Armor | *heavy weathered steel power armor* (OK sans "T-45/T-60/X-01") |
| Pip-Boy | *retro wrist-mounted computer terminal* |
| Deathclaw | *massive armored bipedal reptilian predator* |
| Brahmin | *two-headed mutant cow* |
| Rad / Rads | *radiation* |
| Ghoul (parfois bloqué) | *radiation-scarred human with decomposed cracked skin* |

---

## FICHES VISUELLES — PERSONNAGES JOUEURS

### PJ-01 : VIEUX COLOSSE

```
a massive bald heavily mutated humanoid with olive-green leathery deeply furrowed skin, enormous muscular build, wearing simple wrapped earth-tone cloth robes, huge hands, calm contemplative expression, towers over everyone by two heads
```

**Copie synthétique :**
```
an ordinary-sized confused human man with brown hair, same calm contemplative gaze as the mutant but in a completely different body, wearing similar earth-tone cloth robes
```

**Props récurrents :** vieux livre ouvert, décombres de mur (son poste d'observation)

---

### PJ-02 : BAILEY TOUT SOURIRE

```
a radiation-scarred ghoul with cracked pale gray decomposed skin, almost completely bald round smooth skull with only a few sparse wisps of hair, kind gentle eyes, permanent wide Glasgow smile with knife-cut mouth corners exposing teeth — the only unsettling feature on an otherwise warm face, wearing a stained dirty apron over dark green hoodie, stethoscope around neck
```

**Copie synthétique :**
```
a healthy young human woman with soft kind features, normal mouth that smiles by choice, wearing a clean version of the same apron over a green hoodie, stethoscope around neck
```

**Props récurrents :** comptoir de clinique, fournitures médicales

---

### PJ-03 : TOMMY "JOYEUX" DOYLE

```
a human male with short dark wavy hair under a worn wide-brim leather hat, strong jaw, charming asymmetrical smirk, wearing layered scavenged dark brown and green tactical armor
```

**Copie synthétique :**
```
his perfect identical double — same hat, same smirk, same posture, indistinguishable
```

**Props récurrents :** cartes à jouer, comptoir d'échange

---

### PJ-04 : HAZEL JOHNSON

```
a human female with dark brown hair pulled back loosely, tired but determined expression, wearing heavily weathered rust-orange steel power armor with a large gear cog insignia on the shoulder pauldron, red cross medic armband, medical kit at her hip
```

**Copie synthétique :**
```
her perfect identical double — same face, same weathered armor, same exhaustion in the eyes
```

**Props récurrents :** kit médical, brassard croix rouge

---

## FICHES VISUELLES — PNJ

### PNJ-01 : JESSE PEDIGRUE (maire)

```
a charismatic middle-aged man with a three-month beard, torn prisoner rags (post-captivity) OR simple worn civilian clothes (in town), warm confident smile, natural leader posture, often standing elevated — on a truck bed or a stage
```

**Props récurrents :** pick-up rouillé, estrade improvisée

---

### PNJ-02 : PALADIN CENDRA VOSS (Confrérie)

```
a tall 44-year-old woman in gray-and-blue heavy steel power armor, visor raised, ordinary face — neither beautiful nor frightening, right glove removed (her nervous tic when speaking), left glove still on
```

**Props récurrents :** registre/liste de noms, tente militaire

---

### PNJ-03 : SCRIBE ELIAS KERN (Confrérie)

```
a young 26-year-old man in a simple scribe uniform (no armor), notebook under one arm, camera hanging around his neck, a measurement device with dials in hand, looks like a student heading to class rather than a soldier
```

**Props récurrents :** carnet, appareil photo, appareil de mesure

---

### PNJ-04 : DR. ROLAN VEST (scientifique Institut)

```
a small man with round glasses, pristine immaculate white lab coat even in the wasteland, holding a laptop, constantly taking notes, meticulous unsettling calm demeanor
```

**Props récurrents :** ordinateur portable, appareil sonar (cylindre métallique avec cadrans)

---

### PNJ-05 : JOSEPH (goule, prisonnier)

```
a lucid radiation-scarred ghoul, elderly, confused vacant expression, wrists bound to a clinic chair, frail build
```

---

### PNJ-06 : GÉRALDINE (brahmine)

```
a two-headed mutant cow, free and unburdened, trotting along a wasteland road, looking relieved
```

---

### PNJ-07 : MIMIMATI (amante de Hazel)

```
a young woman, returned from captivity, searching expression, looking for someone in a crowd
```

---

## TEMPLATE DE SCÈNE

Utiliser cette structure pour composer un prompt de storyboard :

```
[LIEU — 1-2 lignes de décor et lumière]

[PERSONNAGE PRINCIPAL — coller le bloc fiche + action/émotion spécifique à la scène]

[PERSONNAGE SECONDAIRE — coller le bloc fiche + action/émotion]

[ÉLÉMENTS D'ENVIRONNEMENT — max 4-5 props contextuels]

[AMBIANCE — 1 ligne de mood/atmosphère]

[BLOC STYLE]
```

### Exemple : "Jesse parle à Voss dans la tente"

```
Inside a military field tent at night, canvas walls, harsh white portable lamp casting sharp shadows on a folding table covered in documents,

a charismatic middle-aged man with a three-month beard, simple worn civilian clothes, standing with arms open, palms up, earnest pleading expression, speaking passionately,

facing him across the table: a tall 44-year-old woman in gray-and-blue heavy steel power armor, visor raised, ordinary face, right glove removed and held in her left hand, listening with a guarded unreadable expression,

a list of names on the table between them, a radio unit crackling in the corner, two armed soldiers in power armor standing at the tent entrance,

tense negotiation atmosphere, two leaders measuring each other,

cinematic digital oil painting, retro-futuristic 1950s-inspired post-apocalyptic aesthetic, painterly brushwork with visible texture, dramatic cinematic lighting, muted earthy palette dominated by amber rust and ochre, highly detailed character faces and textures, movie concept art quality, landscape format 16:9
```

---

## CHECKLIST AVANT ENVOI D'UN PROMPT

- [ ] Aucun terme IP interdit (vérifier la table de substitutions)
- [ ] Max 3 personnages décrits en détail
- [ ] 1 seule source de lumière dominante, pas de contradiction
- [ ] Max 4-5 éléments d'environnement
- [ ] Bloc style collé à la fin
- [ ] Format 16:9 mentionné
- [ ] Pas d'instructions abstraites impossibles à rendre ("same soul", "uncanny doubling")
- [ ] Descriptions physiques concrètes uniquement (pas d'émotions invisibles)
