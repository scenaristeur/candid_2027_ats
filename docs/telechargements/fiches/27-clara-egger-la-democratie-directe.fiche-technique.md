# 27 - Clara Egger - La Démocratie Directe

**Statut** : maquette spartiate posée — session à sauvegarder, validation par extraits.
**Tempo** : 84 BPM *(proposition, à valider)*
**Tonalité** : La mineur (Am) — bourdon *(proposition, à valider à l'oreille)*
**Signature** : 4/4
**Durée cible** : ≈ 1 min 55
**Atmosphère** : Performance, boucle, insistance
**Style** : Spoken word minimaliste, boucle rythmique
**Voix** : baryton parlé-chanté de David, E3–B3 (MIDI 64–71, convention Ableton C3 = 60).

---

## 1. Le candidat — brief du 14/11/2026

| | |
| :--- | :--- |
| **Profil** | Professeure de sciences politiques, candidate de « Solution démocratique ». |
| **Couleur politique** | Démocratie directe, transpartisane. |
| **Actions déjà menées** | A créé son mouvement en 2024 ; campagne transpartisane pour « changer les règles du jeu politique ». |
| **Programme 2027** | Une seule mesure : réviser l'article 89 de la Constitution pour permettre à 700 000 citoyens de proposer une révision constitutionnelle, soumise ensuite au référendum. |
| **Pour** | Redonner le pouvoir aux citoyens ; fatigue de la classe politique. |
| **Contre** | Une seule mesure, sans programme économique ou social ; risque de paralysie institutionnelle. |
| **Actualité** | Sa campagne porte un seul mot : référendum. |
| **Transition Marseillaise** | « Aux armes, citoyens… votez directement ! » |

> **Fiabilité** : contenu issu de `Candidats 2027.md` (compilation interne du 14/11/2026). Chaque chiffre, score et procédure doit être revérifié et **daté** avant l'enregistrement. L'album doit pouvoir dire sa date de vérité.

## 2. Ce que la chanson doit faire

- Expliquer l'article 89 et les 700 000 citoyens sans jargon.
- Dire ce qu'une seule mesure ne règle pas.
- Faire de la répétition une forme politique, pas un défaut.

## 3. Structure (en barres)

Intro boucle (8) → Couplet 1 (16) → Refrain (8) → Couplet 2 (16) → Refrain (8) → Pont (8) → Refrain final (8) → Outro (4) = 76 barres

## 4. Grille d'accords (proposition)

| Section | Grille (4 mesures) | Couleur / intention |
| :--- | :--- | :--- |
| **Couplet** | `| Am | Am | Am | Am |` | Bourdon volontaire : une seule couleur. |
| **Refrain** | `| F | G | Am | Am |` | Le refrain est une boucle parlée, presque hypnotique. |

## 5. Palette Live 12 Lite (proposition)

| Piste | Rôle | Instrument / Kit | Index |
| :--- | :--- | :--- | :--- |
| `1-Boucle` | Rythme | Drum Rack (minimal) | 0 |
| `2-Bourdon` | Fondation | Drift (drone) | 1 |
| `3-Voix` | Chant | Audio | 2 |
| `4-Doublage` | Texture | Audio (voix doublée) | 3 |

> 8 pistes maximum (Live 12 Lite). Index **0-based** ; le nom porte l'index 1-based : `1-Batterie` = index 0.

## 6. Intention de mix

Voix sèche, boucle très discrète. Le silence entre les phrases fait partie du morceau.

## 7. À vérifier avant d'enregistrer

- Le seuil exact de 700 000 citoyens et le mécanisme proposé.
- La rédaction actuelle de l'article 89.
- Le statut juridique de sa candidature et ses parrainages.

## 8. Notes de production

Morceau le plus court de l'album, avec celui de Philippot. Presque pas de mélodie : la voix porte le rythme.

## 9. Session et steps de production

> **Maquette spartiate, une session par chanson.** 5 pistes, un rôle par piste, pas de rack à
> chaînes. La forme est jouée dans **un seul clip long par piste** (176 temps) : intro 4, couplet 1,
> refrain, couplet 2, refrain, pont 4, outro 4. En cas de conflit, **c'est §9 qui fait foi**.

**Session** : `27 - Clara Egger - La Démocratie Directe.als`
**Tempo** : 84 BPM · **Tonalité de travail** : La mineur (Am) — bourdon · **Signature** : 4/4
**Forme** : 44 mesures / 176 temps — Intro 4 · Couplet 1 8 · Refrain 8 · Couplet 2 8 · Refrain 8 · Pont 4 · Outro 4
**Grille** : couplet `| Am | Am | Am | Am |` · refrain `| F | G | Am | Am |` · pont `| Am | Am | Am | Am |`

| Piste | Index | Rôle | Instrument | Réglage de maquette |
| :--- | :--- | :--- | :--- | :--- |
| `1-Boucle` | 0 | Boucle rythmique | Gen Purpose Kit (Drum Rack) | 36 kick, 37 rim, 42 hats, 38 snare discret, 49 crash |
| `2-Bourdon` | 1 | Fondation | Drift | Osc 1 sine · Osc 2 triangle · LP 0,45 · attaque 0,5 · Volume 0,40 |
| `3-Guide` | 2 | Voix parlée | Drift | Osc 1 triangle · Osc 2 off · Volume 0,70 |
| `4-Doublage` | 3 | Écho rythmique | Drift | Osc 1 triangle · LP 0,80 · Volume 0,45 |
| `5-Voix` | 4 | Chant final | Audio | vide pour l'instant |

**Niveaux** : volumes de piste 0,80 (boucle, guide), 0,60 (bourdon), 0,45 (doublage), 0,85 (voix).
Pas de Utility, pas de saturation, pas d'EQ : le silence entre les phrases fait partie du morceau.
**Validation par extraits** : `data/analyses/egger_intro_03.wav` (RMS 0,056), `egger_couplet_03.wav`
(0,159), `egger_refrain_02.wav` (0,158), `egger_pont_02.wav` (0,164), `egger_outro_02.wav`
(0,164). Peak maximal 0,559, aucun échantillon écrêté. La boucle seule sort à 0,245 de peak
(`egger_loop_only.wav`), le guide seul à 0,321 (`egger_guide_only.wav`).

### Steps

1. **Ouvrir la session** et la sauvegarder sous son nom dans le dossier du morceau.
2. **Vérifier le tempo** (84 BPM), la signature 4/4 et la tonalité de travail (Am).
3. **Garder 5 pistes** : boucle, bourdon, guide, doublage, voix. Pas de piste supplémentaire.
4. **Un clip de 176 temps par piste** dans la scène 1. Forme courte : 44 mesures, pont et outro de 4 mesures.
5. **Boucle** : kick 0/2,5, rim 1/3, hats sur les contretemps, snare discrète au refrain. Volontairement répétitive.
6. **Bourdon** : A tenu, filtre bas, attaque lente. Il change en F et G au refrain, sinon il ne bouge pas.
7. **Guide** : presque monotone, 4 notes par mesure, dans E3–B3 (64–71). C'est la voix qui porte le rythme.
8. **Doublage** : écho du guide, décalé de 0,25 temps, volume bas. Il crée la boucle vocale.
9. **Pont** : la boucle se réduit à un rim, le bourdon reste. Le silence doit s'entendre.
10. **Écouter des extraits**, pas la forme entière : intro, couplet, refrain, pont. Valider ou corriger,
    puis remplir les valeurs réelles ci-dessus.

### Garde-fous

- **5 pistes suffisent** pour cette maquette. Ne pas ajouter de piste pour un détail.
- **Pas de rack à chaînes**, pas de Surge XT : le coût CPU et le temps de réglage ne sont pas justifiés ici.
- **Une seule capture à la fois**, et vérifier le WAV (peak < 1,0) plutôt que le RMS du tool.
- **Pas de capture intégrale à ce stade** : des extraits de 8–10 s par section suffisent à valider.
- **La répétition est une forme politique**, pas un défaut : ne pas rajouter de variation pour « animer ».
- **Le silence fait partie du morceau** : ne pas remplir les trous avec de la réverb ou des nappes.
- Une maquette validée se fige : on note l'idée pour la suivante, on ne la réouvre pas.

## Paroles

Voir `PAROLES.md` : version multi-sections (différence, discours, partisans, refrain), avec
structure, base factuelle et garde-fous — notamment l'article 89 et le seuil de 700 000 citoyens.
