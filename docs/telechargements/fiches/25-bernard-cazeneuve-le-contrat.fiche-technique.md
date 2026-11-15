# 25 - Bernard Cazeneuve - Le Contrat

**Statut** : maquette spartiate posée — session à sauvegarder, validation par extraits.
**Tempo** : 70 BPM *(proposition, à valider)*
**Tonalité** : La mineur (Am) *(proposition, à valider à l'oreille)*
**Signature** : 4/4
**Durée cible** : ≈ 2 min 45
**Atmosphère** : Notarial, grave, un peu austère
**Style** : Musique de chambre, piano et violoncelle
**Voix** : baryton parlé-chanté de David, E3–B3 (MIDI 64–71, convention Ableton C3 = 60).

---

## 1. Le candidat — brief du 14/11/2026

| | |
| :--- | :--- |
| **Profil** | Ancien Premier ministre socialiste (2016–2017), ancien ministre de l'Intérieur. |
| **Couleur politique** | Gauche de gouvernement, fermeté républicaine. |
| **Actions déjà menées** | Ministre de l'Intérieur pendant les attentats de 2015–2016, Premier ministre ; candidature annoncée dans Le Figaro le 28 avril 2026, puis « Lettre aux Français » en juillet ; décline la primaire socialiste. |
| **Programme 2027** | Trois chantiers : éducation et santé ; modernisation des institutions ; sécurité. Le site ajoute la baisse des impôts de production financée par la réduction des aides fiscales, la protection des transitions professionnelles, l'allongement de la durée de cotisation plutôt que l'âge légal, et la santé mentale comme grande cause nationale. |
| **Pour** | Gauche de gouvernement, sérieuse et républicaine, sans compromis avec LFI. |
| **Contre** | Positionnement perçu comme une difficulté à se renouveler ; divise la gauche modérée avec Glucksmann et la gauche sociale-démocrate. |
| **Actualité** | Son « contrat » est une lettre aux Français, pas encore un programme chiffré. |
| **Transition Marseillaise** | « Tremblez, tyrans… et électeurs ! » |

> **Fiabilité** : contenu issu de `Candidats 2027.md` (compilation interne du 14/11/2026). Chaque chiffre, score et procédure doit être revérifié et **daté** avant l'enregistrement. L'album doit pouvoir dire sa date de vérité.

## 2. Ce que la chanson doit faire

- Lire le « contrat » comme un acte politique : que signe-t-on exactement ?
- Rappeler l'expérience de l'Intérieur sans en faire un argument d'autorité.
- Montrer la fragmentation de la gauche modérée.

## 3. Structure (en barres)

Intro piano (8) → Couplet 1 (16) → Refrain (8) → Couplet 2 (16) → Refrain (8) → Pont (8) → Refrain final (8) → Outro (8) = 80 barres

## 4. Grille d'accords (proposition)

| Section | Grille (4 mesures) | Couleur / intention |
| :--- | :--- | :--- |
| **Couplet** | `| Am | F | C | G |` | Chambre, respiration lente. |
| **Refrain** | `| F | C | G | Am |` | Le refrain reste grave, sans éclat. |

## 5. Palette Live 12 Lite (proposition)

| Piste | Rôle | Instrument / Kit | Index |
| :--- | :--- | :--- | :--- |
| `1-Piano` | Harmonie | Drift (piano) | 0 |
| `2-Violoncelle` | Mélodie | Drift (cello) | 1 |
| `3-Contrebasse` | Fondation | Drift (basse acoustique) | 2 |
| `4-Voix` | Chant | Audio | 3 |
| `5-Souffle` | Texture | Simpler (souffle) | 4 |

> 8 pistes maximum (Live 12 Lite). Index **0-based** ; le nom porte l'index 1-based : `1-Batterie` = index 0.

## 6. Intention de mix

Très peu de compression, beaucoup de dynamique. Voix nue au couplet ; violoncelle qui répond, jamais qui double.

## 7. À vérifier avant d'enregistrer

- Le contenu exact des trois chantiers.
- Sa position sur la primaire socialiste et le nombre de parrainages.
- Les attentats de 2015–2016 : ne citer que des faits établis.

## 8. Notes de production

Le morceau doit finir sur une question, pas sur une conclusion : c'est un contrat non signé.

## 9. Session et steps de production

> **Maquette spartiate, une session par chanson.** 6 pistes, un rôle par piste, pas de rack à
> chaînes. La forme est jouée dans **un seul clip long par piste** (192 temps) : intro 4, couplet 1,
> refrain, couplet 2, refrain, pont 4, refrain final 4, outro 4. En cas de conflit, **c'est §9 qui fait foi**.

**Session** : `25 - Bernard Cazeneuve - Le Contrat.als`
**Tempo** : 70 BPM · **Tonalité de travail** : La mineur (Am) · **Signature** : 4/4
**Forme** : 48 mesures / 192 temps — Intro 4 · Couplet 1 8 · Refrain 8 · Couplet 2 8 · Refrain 8 · Pont 4 · Refrain final 4 · Outro 4
**Grille** : couplet `| Am | F | C | G |` · refrain `| F | C | G | Am |` · pont `| Dm | Am | E | Am |`

| Piste | Index | Rôle | Instrument | Réglage de maquette |
| :--- | :--- | :--- | :--- | :--- |
| `1-Piano` | 0 | Harmonie | Drift | Osc 1 triangle · Osc 2 saw oct +1 · décay 0,5 · Volume 0,65 |
| `2-Violoncelle` | 1 | Contre-chant | Drift | Osc 1 saw · Osc 2 triangle · attaque 0,06 · LP 0,65 · Volume 0,75 |
| `3-Contrebasse` | 2 | Fondation | Drift | Osc 1 triangle · Osc 2 sine oct −1 · LP 0,40 · Volume 0,75 |
| `4-Souffle` | 3 | Air | Drift | Osc 1 triangle · Osc 2 sine oct +1 · attaque 0,40 · Volume 0,30 |
| `5-Guide` | 4 | Mélodie guide | Drift | Osc 1 triangle · Osc 2 off · Volume 0,70 |
| `6-Voix` | 5 | Chant final | Audio | vide pour l'instant |

**Niveaux** : volumes de piste 0,78 (violoncelle, contrebasse, guide), 0,75 (piano), 0,35 (souffle),
0,85 (voix). Pas de Utility, pas de saturation, pas d'EQ ; **pas de batterie** : c'est de la musique de chambre.
**Validation par extraits** : `data/analyses/cazeneuve_intro_02.wav` (RMS 0,123), `cazeneuve_couplet_03.wav`
(0,194), `cazeneuve_refrain_02.wav` (0,189), `cazeneuve_pont_02.wav` (0,182), `cazeneuve_refrain_final_02.wav`
(0,194). Peak maximal 0,829, aucun échantillon écrêté. Le violoncelle seul sort à 0,245 de peak
(`cazeneuve_cello_only_03.wav`), le guide seul à 0,309 (`cazeneuve_guide_only.wav`) : le violoncelle
répond, il ne masque pas.

### Steps

1. **Ouvrir la session** et la sauvegarder sous son nom dans le dossier du morceau.
2. **Vérifier le tempo** (70 BPM), la signature 4/4 et la tonalité de travail (Am).
3. **Garder 6 pistes** : piano, violoncelle, contrebasse, souffle, guide, voix. Pas de piste supplémentaire.
4. **Un clip de 192 temps par piste** dans la scène 1. Forme courte : 48 mesures, pont et refrain final de 4 mesures.
5. **Pas de batterie** : le tempo est tenu par le piano et la contrebasse. C'est un choix de chambre.
6. **Piano** : main gauche large, accords plaqués sur 1 et 3, très discret.
7. **Violoncelle** : longues tenues au couplet, contre-chant au refrain, phrase au pont.
8. **Contrebasse** : pizzicato, fondamentale en appui, quinte au contretemps.
9. **Souffle** : note haute tenue, très basse, pour l'air. Elle ne doit pas s'entendre comme un son.
10. **Guide** : motif de 4 notes par mesure, très conjoint, dans E3–B3 (64–71). Récitatif notarial.
11. **Écouter des extraits**, pas la forme entière : intro, couplet, refrain, pont. Valider ou corriger,
    puis remplir les valeurs réelles ci-dessus.

### Garde-fous

- **6 pistes suffisent** pour cette maquette. Ne pas ajouter de piste pour un détail.
- **Pas de rack à chaînes**, pas de Surge XT : le coût CPU et le temps de réglage ne sont pas justifiés ici.
- **Une seule capture à la fois**, et vérifier le WAV (peak < 1,0) plutôt que le RMS du tool.
- **Pas de capture intégrale à ce stade** : des extraits de 8–10 s par section suffisent à valider.
- **Le violoncelle doit être audible mais derrière la voix** : monter le filtre et le volume du Drift,
  puis redescendre le fader. C'est ce qui a été fait ici.
- **Ne citer aucun attentat précis** : le parcours à l'Intérieur suffit.
- Une maquette validée se fige : on note l'idée pour la suivante, on ne la réouvre pas.

## Paroles

Voir `PAROLES.md` : version multi-sections (différence, discours, partisans, refrain), avec
structure, base factuelle et garde-fous — notamment l'interdiction de citer un attentat précis.
