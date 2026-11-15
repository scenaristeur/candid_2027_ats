# FICHE TECHNIQUE — Je lis (malgré le bruit)

**Tempo** : 94 BPM
**Tonalité** : Ré dorien (Dm), grille Dm9 / G13 / Cmaj9 / A7#9
**Signature** : 4/4 (« half-time trip-hop » : caisse claire sur le 3)
**Durée** : 72 mesures = 288 temps = **3 min 04**
**Atmosphère** : refuge actif, mélancolie groovy, résistance tranquille
**Style** : trip-hop / funk atmosphérique
**Voix** : baryton grave, parlé-chanté. Fondamentale mesurée **93-130 Hz** (médiane ~110 Hz)
**Projet** : `sources/Reprises/Je lis - Johnny Hallyday/`
**Paroles** : voir `PAROLES.md`

## Références (couleur, pas pastiche)

- **Pink Floyd** — textures, espace, guitare tenue, montée lente
- **Morcheeba** — beat downtempo, Rhodes, mélancolie groovy
- **Deep Purple** — orgue tenu, chaleur, ouverture au refrain
- **Prince** — basse syncopée, minimalisme funk, clavinet

---

## Structure

Indices de section en **mesures** (1-based), positions en **temps (beats)** dans l'arrangement.

| # | Section | Mesures | Début (temps) | Longueur | Énergie | Batterie | Clavinet | Guide |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Intro | 1-8 | 0 | 32 | 2/10 | entre à la mes. 8 (kick + snare sur le 3) | — | — |
| 2 | Couplet 1 | 9-16 | 32 | 32 | 3/10 | half-time | — | ✓ |
| 3 | Couplet 2 | 17-24 | 64 | 32 | 4/10 | half-time | — | ✓ |
| 4 | Pré-refrain | 25-28 | 96 | 16 | 6/10 | charley seul + roulement 16es | ✓ | ✓ |
| 5 | Refrain | 29-36 | 112 | 32 | 8/10 | plein + crash | ✓ | ✓ |
| 6 | Couplet 3 | 37-44 | 144 | 32 | 5/10 | half-time, plus présent | ✓ | ✓ |
| 7 | Pont | 45-52 | 176 | 32 | 3/10 | ride + kick sur le 1 | — | ✓ |
| 8 | **Solo** | 53-60 | 208 | 32 | 7/10 | plein + crash | ✓ (4 mes.) | — |
| 9 | Refrain final | 61-68 | 240 | 32 | 9/10 | plein + 2 crashes | ✓ | ✓ |
| 10 | Outro | 69-72 | 272 | 16 | 2/10 | **silencieuse** | — | ✓ |

**Durée vérifiée** : 288 temps à 94 BPM = 183,8 s.

---

## Grille d'accords

Notes réelles (convention **Ableton : C3 = 60**).

| Section | Grille mesure par mesure |
| :--- | :--- |
| Intro | Dm9 \| G13 \| Cmaj9 \| A7#9 \| Dm9/C \| Bbmaj7#11 \| Gm9 \| A7sus4 → A7#9 |
| Couplet 1 | Dm9 \| G13 \| Dm9 \| G13 \| Dm9 \| G13 \| Bbmaj7#11 \| A7sus4 → A7#9 |
| Couplet 2 | idem C1, mais fin : Bbmaj7#11 \| **Em7b5 → A7#9** |
| Pré-refrain | Em7b5 \| A7#9 \| Dm9 → Bb13 \| Gm9 → C13 |
| Refrain | Dm9 \| Bb13 \| Gm9 \| A7#9 \| Dm9 \| Bb13 \| Cmaj9 \| A7#9 |
| Couplet 3 | idem C1 |
| Pont | Bbmaj7#11 \| Gm9 \| Em7b5 → A7#9 \| Dm9 \| Bbmaj7#11 \| Gm9 \| C13 \| A7sus4 → A7#9 |
| Solo | Dm9 \| Bb13 \| Gm9 \| A7#9 \| Dm9 \| Bb13 \| Cmaj9 \| A7#9 |
| Refrain final | idem refrain |
| Outro | Dm9 \| G13 \| Cmaj9 \| Dm9 |

### Voicings employés (Rhodes / nappe, main droite)

| Accord | Notes | MIDI |
| :--- | :--- | :--- |
| Dm9 | F–A–C–E | 53-57-60-64 |
| G13 | G–B–E–F | 55-59-64-65 |
| Cmaj9 | C–G–B–E | 48-55-59-64 |
| A7#9 | A–C#–E–G | 57-61-64-67 |
| Bbmaj7#11 | Bb–D–E–F | 58-62-64-65 |
| Bb13 | Bb–D–F–Ab | 58-62-65-68 |
| Gm9 | G–Bb–D–F | 55-58-62-65 |
| Em7b5 | E–G–Bb–D | 52-55-58-62 |
| C13 | C–G–Bb–D | 48-55-58-62 |

### Orgue (registre aigu, zone de split ≥ 72)

| Accord | MIDI |
| :--- | :--- |
| Dm9 | 74-77-81-84 |
| Bb13 | 74-77-80-84 |
| Gm9 | 74-77-79-82 |
| A7#9 | 73-76-79-84 |
| Cmaj9 | 76-79-83-86 |

---

## Pistes (indices 0-based)

| # | Index | Nom | Moteur / patch | Vol | Pan | Chaîne FX |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 0 | **1-Batterie** | `Dry Session Kit.adg` (GM : kick 36, snare 38, hats 42/46, toms 41-47, ride 50, crash 48, conga 51) | 0.72 | 0 | Saturator (Soft Sine, Drive 0.14, Dry/Wet 0.22) |
| 2 | 1 | **2-Basse** | `Deep Chill Bass.adg` | 0.80 | 0 | Saturator (Soft Sine, Drive 0.30, DC filter, Dry/Wet 0.45) → Compressor (seuil 0.72, ratio 0.6) |
| 3 | 2 | **3-Rhodes** | `E-Piano Wurli.adg` — Tone 1/2 = 50/44, Tine 52, Phaser 12, Room 38, Warmth 55, Tone Decay 52 | 0.62 | 0 | Saturator (Soft Sine, Drive 0.20, 32 %) → Reverb (17 %, Room 0.42) |
| 4 | 3 | **4-Guitare** | `Palm Guitar.adg` — Filter Cutoff 70, Palm Mutes 18, Echo 0, Reverb 10, Amp Gain 45, Rotary 0 | 0.46 | +0.22 | Saturator (Soft Sine, Drive 0.2, 30 %) → Delay (ping-pong, croche pointée / noire, FB 0.45, Dry/Wet 0.25) → Reverb (10 %) → **Utility** (Output 0.62) → EQ Three (LowOff, Mid 1.0, High 0.85) |
| 5 | 4 | **5-Nappe/Orgue** | **Instrument Rack, 2 chaînes avec Key Zones** — voir ci-dessous | 0.60 | 0 | Chorus-Ensemble (Ensemble, 22 %, Warmth 0.30) → Reverb (22 %, Room 0.62) |
| 6 | 5 | **6-Voix** | `Basic Sine Keys.adg` — FM 0, Drive 0, Chorus 0, Reverb 0, Attack 15, Release 60 | 0.70 | 0 | — (guide MIDI, sec à dessein) |
| 7 | 6 | **7-Clavinet** | `Clav Rebel Musak.adg` — Filter Env 10, Note Length 80, Delay 0, Reverb 4, Send 18 | 0.42 | 0 | Auto Filter (low-pass 12 dB, freq 0.62, réso 0.15, LFO 0, Dry/Wet 0.45) → Compressor (seuil 0.78, ratio 0.65) → **Utility +15 dB** (Output 0.78) |
| 8 | 7 | **8-Audio** | Piste audio (voix réelle) | 0.85 | 0 | — |

### ⚠️ Split nappe / orgue (piste 5)

Deux rôles sur une seule piste, pour tenir dans le budget de 8 pistes de Live Lite.

| Chaîne | Contenu | Key Zone |
| :--- | :--- | :--- |
| 1 | `Wavetable + Reverb + Delay` = **Organ Plush** | **C4 → G8** (72 → 127) |
| 2 | **Surge XT** = `MKS-70 Warm Pad` | **C-2 → B3** (0 → 71) |

- Patch Surge sculpté : `osc/drift` 0.12, `filter/1/cutoff` 0.62, résonance 0.30, `amp/width` 0.85, `aeg/attack` 0.87, osc3 en **sine** (volume 0.55), ring 1×2 0.12, ring 2×3 0.08, noise 0.05 (color 0.35), `filter/2/cutoff` 0.55, detune osc2 0.10.
- **`/param/global/volume` = 0.9578** (une instance Surge neuve démarre vers 0.55 et sonne 5 à 15 dB plus bas).
- **OSC activé par David pour chaque instance** — instance 0 = ancienne piste (supprimée), instance 1 = celle du rack.

---

## Clips (session et arrangement)

Les clips de session portent le nom de leur section. L'arrangement reprend exactement les mêmes noms.

| Section | Début (temps) | Longueur (temps) | Clips |
| :--- | :--- | :--- | :--- |
| Intro | 0 | 32 | S1 Intro |
| Couplet 1 | 32 | 32 | S2 Couplet 1 |
| Couplet 2 | 64 | 32 | S3 Couplet 2 |
| Pré-refrain | 96 | 16 | S4 Pré-refrain |
| Refrain | 112 | 32 | S5 Refrain |
| Couplet 3 | 144 | 32 | S6 Couplet 3 |
| Pont | 176 | 32 | S7 Pont |
| Solo | 208 | 32 | S7b Solo |
| Refrain final | 240 | 32 | S8 Refrain final |
| Outro | 272 | 16 | S9 Outro |

---

## Guide vocal

### Tessiture mesurée (voix seule, casque)

| Source | p10 | médiane | p90 |
| :--- | :--- | :--- | :--- |
| Take 1 (retour enceintes) | 93.4 Hz | 103.0 Hz | 126.7 Hz |
| **Take 3 (casque)** | **97.0 Hz** | **110.7 Hz** | **130.2 Hz** |
| Guide couplet | 99.3 Hz | 111.6 Hz | 150.2 Hz |
| Guide refrain | 110.2 Hz | 117.1 Hz | 147.5 Hz |

Le guide est **composé dans la zone mesurée**, pas transposé depuis une lead sheet. Ambitus écrit : **G2 → E3 (43 → 52 MIDI)**.

### Carte d'énergie du guide

Vélocités indiquées sur **l'échelle 0-100** (les clips stockent 0-127 ; ×0.787).

| Section | Énergie | Hauteur | Vélocités | Longueur / densité |
| :--- | :--- | :--- | :--- | :--- |
| Couplet 1 | 3/10 | G2–D3 | 63-76 | croches syllabiques, fins tenues |
| Couplet 2 | 4/10 | G2–D3 | 63-76 | idem, fin descendante |
| Pré-refrain | 6/10 | G2–D3 | 66-79 | ça monte, sommet D3 |
| Refrain | 8/10 | A2–E3 | 72-82 | plus haut, plus tenu |
| Couplet 3 | 5/10 | G2–E3 | 66-76 | groove + clavinet ; **fin chuchotée (50-54)** |
| Pont | 3/10 | G2–D3 | 50-58 | notes longues, presque parlé |
| Refrain final | 9/10 | A2–E3 | 77-88 | même mélodie, poussée |
| Outro | 2/10 | G2–D3 | 43-49 | parlé, dernière note tenue |

### Règles d'écriture

- **Une note par syllabe**, le texte commande le rythme.
- Mouvement **par secondes**, un seul élan vers le haut par phrase.
- **Ancre** : chaque « je lis » retombe sur **A2 ou G2**, tenu.
- Contretemps légèrement en retard (+12 à +15 ms) = nonchalance.

---

## Voix — état de l'enregistrement

- Piste `8-Audio` (index 7).
- **Couplet 1** : take 3, enregistré au casque — **slot 1**, clip `8-Audio 4`, longueur 32 temps. Médiane 110.7 Hz, aligné sur le guide.
- **Anciens takes à supprimer** : slots 14 (`8-Audio 3`) et 15 (`8-Audio 2`).
- Sections restantes : **non enregistrées** (couplet 2, pré-refrain, refrain, couplet 3, pont, refrain final, outro).

## Automations

Aucune pour l'instant. À dessiner au mix (voir plus bas).

---

## Réglages mix — état actuel

| Piste | Vol | Pan | Notes |
| :--- | :--- | :--- | :--- |
| 1-Batterie | 0.72 | 0 | Compressor glue ajouté au prémix |
| 2-Basse | 0.80 | 0 | EQ Three : mid 0.72 |
| 3-Rhodes | 0.62 | −0.12 | EQ Three : LowOff |
| 4-Guitare | 0.46 | +0.22 | Palm Guitar + Utility 0.62 ; EQ Three LowOff / Mid 1.0 / High 0.85 |
| 5-Nappe/Orgue | 0.60 | 0 | EQ Three : LowOff |
| 6-Voix | 0.70 | 0 | guide MIDI — **coupé au prémix** |
| 7-Clavinet | 0.42 | −0.25 | baissée à l'oreille après +15 dB d'Utility ; EQ Three LowOff |
| 8-Audio | 0.85 | 0 | |
| Master | 0.85 | 0 | Compressor glue → Limiter 0.95 / 3 ms / True Peak |

### Mesures de référence (guide coupé, mêmes conditions)

| Section | RMS | Dynamique |
| :--- | :--- | :--- |
| Pont | 0.083 | 21.6 dB |
| Couplet 1 | 0.181 | 14.8 dB |
| Couplet 3 | 0.190 | 14.4 dB |
| Refrain | 0.180 | 14.9 dB |
| Refrain final | 0.206 | 13.7 dB |
| Outro | 0.073 | 22.8 dB |

---

## Prémix (novembre 2026) — instrumental, sans voix

Le guide MIDI est **coupé** : ce n'est pas un élément de mix. La voix n'est pas encore enregistrée.

### 1. Staging

| Piste | Vol | Pan |
| :--- | :--- | :--- |
| 1-Batterie | 0.72 | 0 |
| 2-Basse | 0.80 | 0 |
| 3-Rhodes | 0.62 | **−0.12** |
| 4-Guitare | 0.46 | **+0.22** |
| 5-Nappe/Orgue | 0.60 | 0 |
| 6-Voix (guide) | 0.70 | — **coupé** |
| 7-Clavinet | 0.42 | **−0.25** |
| 8-Audio | 0.85 | 0 |

### 2. Carving (EQ Three)

Référence : `LowOff` coupe sous ≈ 224 Hz ; Mid ≈ 224-960 Hz ; High > 960 Hz.

| Piste | Action |
| :--- | :--- |
| 2-Basse | GainMid **0.72** (dégage 224-960), GainLo 0.88 |
| 3-Rhodes | **LowOff** (plus rien sous 224), GainMid 0.85 |
| 4-Guitare | **LowOff**, GainMid 0.80 |
| 5-Nappe/Orgue | **LowOff**, GainMid 0.82 |
| 7-Clavinet | **LowOff**, GainMid 0.95 |

### 3. Dynamique

- Batterie : **Compressor** (seuil 0.82, ratio 0.55, attaque 0.45, release 0.25) → glue du kit.
- Basse : Saturator + Compressor (déjà en place).

### 4. Profondeur

Reverbs en insert sur Rhodes, Guitare, Nappe/Orgue. Returns A et B inutilisés.

### 5. Master

| Device | Réglage |
| :--- | :--- |
| **Compressor** (glue) | Threshold 0.55, Ratio 0.65, Attack 0.5, Release 0.3 |
| **Limiter** | Ceiling **0.95**, Lookahead **3 ms**, Mode **True Peak** |
| Fader master | **0.85** (unité de cette installation) |

### 6. Validation (arrangement, 10 s par section)

| Section | Position | Peak | RMS | Écrêtés |
| :--- | :--- | :--- | :--- | :--- |
| Couplet 1 | temps 32 | −13.1 dBFS | −26.5 | **0** |
| Refrain | temps 112 | −11.1 | −26.2 | **0** |
| Pont | temps 176 | −15.2 | −32.7 | **0** |
| Solo | temps 208 | −11.8 | −27.0 | **0** |
| Refrain final | temps 240 | −11.6 | −26.0 | **0** |

**Aucun écrêtage.** Le mix garde **≈ 11 dB de marge sous le plafond** : c'est volontaire, la voix n'est pas encore là et elle prendra cette place. Conséquence : le Compressor de master ne déclenche pas encore (seuil 0.55, crête à ~0.28) — il travaillera quand les niveaux monteront.

---

## Notes de production

1. **Le guide vocal a été refait sur la voix réelle.** La première version venait d'une lead sheet : elle était deux octaves trop haut et inchantable. Toujours mesurer avant d'écrire (voir `guide-vocal-sur-mesure`).
2. **Les presets de guitare de l'usine sont très faibles** (RMS isolé 0.03-0.08 contre 0.22 pour un Rhodes) — d'où l'Utility. Et ils sont **très brillants** : `Ionosphere Guitar` sortait à 90 % de son énergie entre 1 et 4 kHz, ce qui sonne « piquant » et ne prend pas sa place. `Palm Guitar` sculpté (Filter Cutoff 70, Palm Mutes 18) donne **92 % de son énergie entre 300 Hz et 1 kHz**, centroïde 586 Hz : du corps, pas d'agression.
3. **Le clavinet avait besoin d'un gain de rattrapage** : ni l'Auto Filter ni le Compressor n'en avaient, le preset sortait à −26 dBFS. Utility +15 dB.
4. **Un bruit de « frappe » persiste sur le clavinet.** Le LFO de l'Auto Filter a été coupé et le `Filter Env` du preset baissé de 40 à 10, sans l'éliminer. Si ça revient, changer de preset (`Clav Variations` testé, plus brillant).
5. **Couplets et refrain sont au même niveau RMS** (~0.18). Le refrain gagne en densité, pas en niveau. À trancher au mix : pousser le refrain plutôt que baisser les couplets.
6. **Le solo est placé après le pont**, pas avant : pont (creux) → solo (relance) → refrain final (sommet). C'est ce qui donne l'effet d'explosion.
7. **Le split nappe/orgue impose la hauteur** : toute note ≥ 72 MIDI part dans l'orgue, toute note ≤ 71 dans la nappe. Un clip peut contenir les deux, c'est le split qui route.

---

## À faire

| # | Action | Cible | Statut |
| :--- | :--- | :--- | :--- |
| 1 | Enregistrer la voix sur les 7 sections restantes | 8-Audio | À faire |
| 2 | Supprimer les anciens takes (slots 14 et 15) | 8-Audio | À faire |
| 3 | Rééquilibrer couplets / refrain comme courbe d'énergie | Mix | À faire (couplet 1.2 dB au-dessus du refrain) |
| 4 | Carving voix / basse autour de 95-205 Hz, une fois la voix enregistrée | Mix | À faire |
| 5 | Automatiser la courbe d'énergie par section (volume de clip) | Mix | À faire au mix final |
| 6 | Vérifier le mix sur téléphone et sur FOH | Mix | À faire au mix final |

## Paroles

Voir `PAROLES.md` dans ce dossier.
