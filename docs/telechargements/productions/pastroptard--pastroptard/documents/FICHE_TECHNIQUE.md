# Pas trop tard, Mary — Fiche technique

**Statut** : maquette complète et **posée en arrangement** (12 scènes, 84 mesures). Les scènes Intro, Couplet 1, Pré-refrain sont **validées à l'oreille** par David ; les autres sont construites et mesurées, oreille en attente. Premix en cours (basse en croches, sidechain, outro).

**Tempo** : 94 BPM
**Tonalité** : Ré majeur (D)
**Signature** : 4/4 — groove en 16ᵉ légèrement swinguée
**Durée** : 352 temps à 94 BPM = **88 mesures ≈ 3:45**
**Ambiance** : EP électrique, sub basse, pads chauds, plucks, batterie R&B, chœurs aériens
**Style** : pop/R&B, pop-soul
**Voix** : baryton — ambitus annoncé par le brief : **A2–F#4**, refrain autour de A3–F#4 → ⚠️ voir *Notes de production*, deux points non résolus.

Convention des notes : **Ableton C3 = 60**.

---

## Structure (12 scènes, ordre réel de la session)

| # | Scène | Slot | Section | Clips | État | Mesures |
| :-- | :-- | :-- | :--- | :--- | :--- | :-- |
| 1 | S1 | 0 | Intro | Basse, Clav, Pad, Pluck, Lead | **validée à l'oreille** | 8 (32 temps) |
| 2 | S1b | 1 | Couplet instrumental | Drums, Basse, Clav, Pad (entre m3) | **construit, oreille en attente** | 4 (16 temps) |
| 3 | S2 | 2 | Couplet 1 (chant enregistré) | Drums, Basse, Clav + 8-Audio | **validée à l'oreille** | 8 (32 temps) |
| 4 | S3 | 3 | Pré-refrain | Drums, Basse, Clav, Pad, Guide | **validée à l'oreille** | 8 (32 temps) |
| 5 | S4 | 4 | Refrain 1 | tous + Pluck + Lead + Guide | construit | 8 (32 temps) |
| 6 | S5 | 5 | Pont 1 | Basse, Clav, Pad (dépouillé) | construit | 4 (16 temps) |
| 7 | S6 | 6 | Couplet 2 | Drums, Basse, Clav, Pad, Guide | construit | 8 (32 temps) |
| 8 | S7 | 7 | Pré-refrain 2 | Drums, Basse, Clav, Pad, Guide | construit | 8 (32 temps) |
| 9 | S8 | 8 | Refrain 2 | tous + Pluck + Lead + Guide | construit | 8 (32 temps) |
| 10 | S9 | 9 | Pont 2 | Basse, Clav, Pad | construit | 8 (32 temps) |
| 11 | S10 | 10 | Refrain 3 (final) | tous + Pluck + Lead + Guide | construit | 8 (32 temps) |
| 12 | S11 | 11 | Outro (fondu) | Drums (2 mesures), Basse, Clav, Pad | construit | 8 (32 temps) |

**Durée totale : 352 temps à 94 BPM ≈ 3:45.**

---

## Grille d'accords

| Section | Accords |
| :--- | :--- |
| **Intro** | Dmaj7 – A/C# – Bm7 – G6/9 |
| **Couplet** | Dmaj7 – A/C# – Bm7 – G6/9 ǀ Dmaj7 – A/C# – Em7 – A7sus4 |
| **Pré-refrain** | Em7 – A7 – F#m7 – Bm7 ǀ Em7 – A7 – Dmaj7 – A/C# |
| **Refrain (appliqué)** | Dmaj7 – A/C# – Bm7 – G6/9 ǀ Em7 – A7 – (F#m7 / Bm7) – (G6/9 / A7) |
| **Refrain (brief)** | Dmaj7 – A/C# – Bm7 – G6/9 ǀ Dmaj7 – A/C# – Bm7 – G6/9 — variante 2ᵉ moitié : Em7 – A7 – F#m7 – Bm7 ǀ G6/9 – A7 – Dmaj7 |

Le brief place **7 accords sur 4 mesures** dans sa variante : ils ont été **condensés** pour tenir
dans les mesures 5–8 du refrain à 8 mesures (deux accords par mesure sur les mesures 7 et 8). La
finale `Dmaj7` du brief n'est pas posée : le refrain se termine sur **A7**, qui se résout en tête
de la section suivante (et surtout en `Outro Dmaj7`). **À valider à l'oreille.**
| **Pont** | Em7 – A7 – F#m7 – Bm7 ǀ G6/9 – A7 – Dmaj7 – Dmaj7 |
| **Outro** | Dmaj7 – A/C# – Bm7 – G6/9 – Dmaj7 |

**Voicings** :
- Dmaj7 = D–F#–A–C#
- A/C# = C#–E–A
- Bm7 = B–D–F#–A
- G6/9 = G–B–E–A
- Em7 = E–G–B–D
- A7sus4 = A–D–E–G
- F#m7 = F#–A–C#–E

---

## Pistes (index **0-based**, état vérifié)

| Idx | Nom | Moteur | Vol | Pan | Chaîne FX (dans l'ordre) |
| :-- | :--- | :--- | :--- | :--- | :--- |
| 0 | `1-Batterie` | Selector Kit Warm (DrumGroupDevice) | 0.62 | 0 | — *(charley fermé pad 42 : `Sample` = **96**, charley ouvert pad 46 : `Sample` = **112**)* |
| 1 | `2-Basse` | Analog Bass | 0.65 | 0 | Saturator (Type **Bass Shaper**, Drive 0.35, D/W 1.00) → Utility (Output 0.00) → **Compressor** (sidechain : entrée routée sur `1-Batterie` / **Post FX**, `S/C On`, `S/C EQ Type` Low Shelf, `Ratio` 0.9, `Threshold` 0.68, `Release` 0.35) |
| 2 | `3-Claviers` | E-Piano Rhodish | 0.65 | −0.10 | Utility (0.00) → Saturator (Type **Soft Sine**, Drive 0.28, D/W 0.60) → Auto Filter **high-pass** Freq 0.32 |
| 3 | `4-Pad` | Warm Analog Pad | 0.42 | 0 | Utility (0.00) → Auto Filter **high-pass** Freq 0.32 → EQ Three (GainMid 0.70) |
| 4 | `5-Pluck` | Soft Attention | 0.53 | +0.20 | Utility (0.00) → Auto Filter **high-pass** Freq 0.22 |
| 5 | `6-Lead` | Homebound Lead | 0.657 | 0 | Utility (0.00) → Auto Filter **high-pass** Freq 0.28 → Saturator (Type **Soft Sine**, Drive 0.40, D/W 0.70) |
| 6 | `7-Guide` | Blushed (Synth Lead) | 0.42 | 0 | — |
| 7 | `8-Audio` | Piste audio | 0.85 | 0 | — (contient l'enregistrement vocal de David, Couplet 1, slot 2) |

Notes :
- **Auto Filter : `Filter Type = 1 = High-pass`** (vérifié sur la liste de valeurs du device).
- Saturator `Type` : 0 Analog Clip, 1 Soft Sine, 2 Bass Shaper, 3 Medium Curve, 4 Hard Curve, 5 Sinoid Fold, 6 Digital Clip, 7 Waveshaper.
- `0,85` = unité (0 dB). Le fader vaut **≈ 40 dB par unité** : mesuré, 0.85 → 0.60 = −10,0 dB et 0.60 → 0.45 = −6,1 dB.
- Les deux pistes audio `7-Voix` et `8-Choeurs` ont été **supprimées** le 16 oct. 2026, remplacées par `7-Guide` (MIDI) et `8-Tampon` (MIDI, vide) — demande expresse de David, pour un guide vocal et une piste d'essais.

---

## Clips (session view)

| Clip | Piste | Slot | Longueur | Contenu |
| :--- | :--- | :-- | :-- | :--- |
| `S1 Basse` | 2-Basse | 0 | 16 beats (4 mesures) | basse intro |
| `S1 Clav` | 3-Claviers | 0 | 16 beats | EP intro |
| `S1 Pad` | 4-Pad | 0 | 16 beats | nappe intro |
| `S1 Pluck` | 5-Pluck | 0 | 16 beats | pluck intro |
| `S1 Lead` | 6-Lead | 0 | 16 beats | motif **69, 71, 66, 74** = A3, B3, F#3, D4 |
| `S2 Drums` | 1-Batterie | 1 | 32 beats (8 mesures) | 160 notes : kick `36` ×16, caisse claire `38` ×16, charley fermé `42` ×127, charley ouvert `46` ×1 |
| `S2 Basse` | 2-Basse | 1 | 32 beats | 26 notes, plage **43–52** (G1 → E2) |
| `S2 Clav` | 3-Claviers | 1 | 32 beats | 89 notes, plage **59–76** (B2 → E4) |
| `Guide - Couplet 1` | 7-Guide | 1 | 32 beats | 64 notes, plage **57–67** (A2 → G3), mélodie du couplet du brief |

---

## Groove (vérifié)

- Groove pool (un seul) : index **0** = **`Swing MPC 3000 16ths 57`**, base 3, Quantization 100, Timing 100, Velocity 0, Random 0.
- **`groove_amount` global = 0.70** (valeur unique, s'applique à tous les clips qui utilisent ce groove).
- **Tous les 9 clips** ont `groove_index` 0.

---

## Automations

Une seule, sur l'outro :

- **`4-Pad`, volume, clip d'arrangement à 320** : 0,42 jusqu'au temps 8, puis fondu linéaire à
  **0,0 au temps 31,5**. Mesuré en solo pad : rms **0,0112 → 0,0092 → 0,0033** (320 / 336 / 347) —
  soit −11 dB jusqu'au silence, après un départ calé sur le niveau du refrain (0,0125).
- Rappel : **le volume de clip d'arrangement écrase le fader de piste pendant le clip**. Pour
  qu'une enveloppe « continue » le mix, il faut l'écrire à la valeur du fader (0,42 pour le pad),
  pas à 1.0/0.85 : une enveloppe à 0,85 sur un fader à 0,42 donne **+16 dB mesurés**.

---

## Réglages mix

| Piste | Vol | Pan | Remarque |
| :--- | :-- | :-- | :--- |
| 1-Batterie | 0.56 | 0 | 0.85 = unité initiale → le kit est revenu de −14 dB sur l'intro |
| 2-Basse | 0.65 | 0 | |
| 3-Claviers | 0.65 | −0.10 | le EP est l'élément le plus haut du mix (scène 1) |
| 4-Pad | 0.44 | 0 | le plus en retrait |
| 5-Pluck | 0.53 | +0.20 | |
| 6-Lead | 0.657 | 0 | |
| 7-Guide | 0.60 | 0 | ≈ −5,5 dB sous le reste du mix |

**Mesures (fichiers WAV, `scripts/spect.py`)** — comparaison avec l'intro validée :

| Capture | Centroid | HF > 4 kHz | Corps 640–1280 | RMS | Peak |
| :--- | :-- | :-- | :-- | :-- | :-- |
| Intro validée (`S1_intro_v2`) | 2579 Hz | 20,9 % | 17,0 % | 0.0319 | 0.199 |
| Couplet 1 — **avant** correction charley (`S2_couplet1_final`) | 2923 Hz | 26,9 % | **7,6 %** | 0.0491 | 0.326 |
| Couplet 1 — **après** (`S2_couplet1_guide60`) | **2355 Hz** | **21,7 %** | **19,7 %** | 0.0541 | 0.342 |

Le couplet est calé sur l'intro. Il reste **+4,5 dB sur l'intro** (0.0541 vs 0.0319) — à vérifier à l'oreille : la batterie justifie une montée, mais peut-être pas autant.

---

## Notes de production

### ⚠️ 1. Tessiture du couplet — problème noté, décision reportée

La mélodie du couplet (brief §3) descend jusqu'à **A2 (57)**. Les notes **A2, B2, C#3, D3 (57 → 62)** sont **sous la zone confortable E3–B3 (64 → 71)** documentée dans le skill `guide-vocal-paroles`. La ligne écrite va de 57 à 67 (A2 → G3) : elle n'entre dans la zone qu'à partir de E3 (64).

Deuxième point : le brief annonce un ambitus global **A2–F#4**, et un refrain « autour de A3–F#4 ». Or **F#4 = 78**, soit 7 demi-tons **au-dessus** de B3 (71), sommet de la zone confortable. Le F#4 du refrain serait donc en **voix de tête**, à valider.

**Décision de David (16 oct. 2026)** : « base-toi pour l'instant sur ce qui est écrit, en notant ce problème pour éventuellement y revenir plus tard. »

→ **La mélodie est écrite telle quelle. Ne pas transposer, ne pas réécrire une ligne, sans accord explicite de David.**

### ⚠️ 2. Le charley ne passait pas sur grosse enceinte

Diagnostic du 16 oct. 2026, sur capture isolée du charley (pads kick/caisse claire/charley ouvert coupés, piste batterie solée) :

- **Charley fermé `Selector Kit Warm` en l'état : 88,9 % de son énergie au-dessus de 5 kHz, dont 49,5 % au-dessus de 10 kHz** — une grosse enceinte ne le reproduit pas ; le casque, si. C'est exactement le symptôme remonté par David.
- Zone de présence (1,3–5 kHz) : seulement **8,4 %**.
- Correctif appliqué : **`Sample = 96`** sur le pad 42 → zone de présence **31,4 %**, énergie au-dessus de 10 kHz **11,6 %**, **87,7 % de l'énergie sous 10 kHz**. Ratio présence/top : 0,17 → 2,71.
- **Alternatives mesurées, à garder sous la main** : `Sample` 8 (ratio 0,79), 64 (0,81), 112 (1,66).
- À valider à l'oreille sur grosse enceinte. Si insuffisant : changer de kit (les charleys fermés ont été mesurés — **Gen Purpose Kit** ratio 0,59, **Recording Hybrid Kit** 0,47, **Dry Session Kit** 0,25).
- Le paramètre `Sample` a été découvert en le mesurant ; **sa nature exacte (sélecteur d'échantillon ou non) n'est pas confirmée**.

### 3. Saturator de basse : pas encore aligné sur la recette de translation

Le skill `mix-translation` recommande pour la basse : **Type Medium Curve (3), Drive 0.60–0.80, Dry/Wet 1.0** — c'est ce qui génère les harmoniques qui font exister la basse sur téléphone.
État réel de `2-Basse` : **Type Bass Shaper (2), Drive 0.35**, D/W 1.00.
→ **À tester** si le grave ne traduit pas sur les petits haut-parleurs. Non fait : le couplet attend d'abord l'oreille.

### 4. Le guide `Blushed` occupe la zone vocale

Choix par mesure sur 5 candidats (famille Synth Lead) : `Blushed` met **56,1 %** de son énergie dans 640 Hz – 4 kHz, **0,1 %** au-dessus de 5 kHz, et n'empiète pas sur le grave de la basse (10,1 % sous 320 Hz).
Écartés : `Basic Sine Drive Lead` et `Basic OG Lead` (49,9 % et 63,0 % sous 320 Hz — sous la basse), `Basic Retro Lead` et `Anthem` (29,7 % et 25,9 % au-dessus de 5 kHz — déjà saturé par le charley).

---

## Repères de travail

- **Méthode de mesure** : toujours les WAV (`scripts/spect.py`, `--bands` dans une invocation séparée). L'outil d'analyse MCP **normalise** RMS/peak — ses chiffres ne servent pas de référence.
- **Comparabilité** : ne comparer que des captures capturées **de la même façon** (même fader, mêmes pads actifs, même position). Une capture « isolée » sans `set_track_solo` ne contient pas que l'objet isolé.
- Les lignes d'index de presets sont dans `preset_index/preset_index.csv` (famille Plucked = plucks de la scène 1, `clip-morceau-v0`, fader 0.68 ; famille Synth Lead = guide, `melodie-couplet1`, fader 0.85).

## Paroles

À écrire : `PAROLES.md` dans ce dossier (pas encore créé).

## Arrangement (vue Arrangement)

Les 12 scènes sont posées bout à bout, **336 temps = 84 mesures ≈ 3:34 à 94 BPM**. Positions exactes (en temps, 1 mesure = 4 temps) :

| Temps | Scène | Section |
| :-- | :-- | :--- |
| 0–32 | S1 | Intro (sans batterie) |
| 32–48 | S1b | Couplet instrumental |
| 48–80 | S2 | Couplet 1 — **chant enregistré** (`8-Audio`) |
| 80–112 | S3 | Pré-refrain |
| 112–144 | S4 | Refrain 1 |
| 144–160 | S5 | Pont 1 |
| 160–192 | S6 | Couplet 2 |
| 192–224 | S7 | Pré-refrain 2 |
| 224–256 | S8 | Refrain 2 |
| 256–288 | S9 | Pont 2 |
| 288–320 | S10 | Refrain 3 (final) |
| 320–352 | S11 | Outro (fondu) |

**Durée totale : 352 temps = 88 mesures ≈ 3:45 à 94 BPM.**

- Méthode : `duplicate_to_arrangement(track_index, clip_index, destination_time)` (en temps, exact — **pas** `duplicate_clip_to_arrangement`, qui est *off by one*).
- Pistes (nombre de clips) : Batterie 9 (pas d'intro, pas de pont, outro sur 2 mesures), Basse/Claviers 12, Pad 11 (pas de couplet 1), Pluck/Lead 4 (intro + 3 refrains), Guide 8, `8-Audio` 1.
- **Le guide du Couplet 1 a été retiré de l'arrangement** : il doublonnait le chant enregistré. Le guide reste présent en session.
- Vérifié : lecture de l'arrangement au refrain (t=112) = mesure de la scène S4 (centroid 3530 vs 3535, RMS 0.0617 vs 0.0609).

### Guides posés (7-Guide, 8 clips en arrangement)

| Section | Contenu |
| :--- | :--- |
| Pré-refrain 1 et 2, Refrain 1, 2, 3 | mélodies du brief |
| **Couplet 1 et Couplet 2** | identiques : 64 notes en croches (mélodie A2–G3 du brief) |
| **Pont 1** (144–160) | 32 notes — moitié 1 de la mélodie du pont (`76,74,71,69,67,69,71,74` / `76,74,71,69,66,64,62,64`) |
| **Pont 2** (256–288) | 64 notes — mélodie du pont complète |

⚠️ **La mélodie du pont monte à E4 (76)**, soit 5 demi-tons **au-dessus** de B3 (71), sommet de la
zone confortable du baryton. C'est le brief qui écrit cette ligne — **à valider à l'oreille** avant
l'enregistrement (voir *Notes de production* §1).

## Premix (état actuel)

- **Basse du refrain en croches** (S4, S8, S10) : 8 notes/mesure, accents sur 1 et 3. Mesuré : le bas du spectre est **préservé** (5,4 % sous 80 Hz, inchangé) — c'est un gain de mouvement, pas de tonalité.
- **Sidechain kick → basse** : Compressor sur `2-Basse`, entrée routée sur `1-Batterie` en **Post FX**, `S/C On`. A/B mesuré (basse seule, refrain) : S/C **on** vs **off** → **−1,7 dB RMS** mais **−3 dB sur les crêtes** ; sur le mix complet, RMS inchangé (0.0609) et **crête 0.4068 → 0.4329, crest 6.7 → 7.1** → le kick traverse, le pump reste discret. `Threshold` adouci de 0.5 à **0.68** (la valeur 0.5 creusait −3,1 dB, trop).
- **Intro allongée** à 8 mesures (32 temps) ; le pad monte progressivement (vélocités 40 → 64), pluck et lead montent aussi → l'intro amène le couplet.
- **Scène S1b « Couplet instrumental »** (slot 1, 4 mesures) insérée par David entre l'intro et le couplet chanté : batterie du couplet, basse, claviers, pad qui entre aux mesures 3-4. Pas de guide, pas de voix — laisse l'entrée du chant.
- **Refrain S4 — batterie retravaillée** : l'ancien clip n'était que le pattern du pré-refrain (avec roulement de caisse claire au bout). Reconstruit en batterie complète : kick 1/« et de 2 », caisse claire 2/4, charley 16ᵉ, **shaker (pad 44)** sur les croches — le « tambourin » du brief —, **charley ouverte** sur le « et de 4 » une mesure sur deux, **crash (pad 49)** à l'entrée (m1) et à la seconde moitié (m5).
- Gain staging : Batterie 0.62, Pad 0.42, Guide 0.42. HPF Claviers/Pad 0.32.
- Captures : S1b rms 0.0579 · S2 (chant) rms 0.0669 · S4 rms 0.0614 (les niveaux du couplet instrumental et du couplet chanté sont continus).

**Mesures comparées (refrain) :** avant retouche batterie centroid 3228 Hz / HF>4k 32,5 % / rms 0.0605 → après **3512 Hz / 35,3 % / 0.0614**. Le refrain est plus brillant et plus porté ; il reste au-dessus du couplet en énergie quand il aura le vrai chant.

### Notes de parcours
- Idée notée par David : un passage de couplet instrumental avant son chant → **fait** (S1b, 4 mesures, +10 s → durées totale ≈ 3:34).
- Le refrain n'est pas encore « plus gros » que le couplet en RMS parce qu'il ne porte que le guide MIDI ; le vrai chant n'est enregistré que sur le couplet (piste `8-Audio`).

