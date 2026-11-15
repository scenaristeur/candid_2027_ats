# 01 — L'Essor du Monde Moderne

**Tempo**: 72 → 90 → 95 → 80 → 100 → 72 BPM (map par section)
**Tonalité**: Do majeur (C)
**Durée**: ≈ 2 min 30 (56 barres — arrangement complet)
**Atmosphère**: Récit épique, Guerre froide → Décolonisation → Mondialisation, montée en puissance
**Style**: Rock progressif / Folk épique
**Voix**: Baryton parlé-chanté (E3 → B3, pitch 64-71), spoken word en intro

## Hommage / Inspirations
- Rock progressif / folk épique : récit construit, ponts instrumentaux, crescendo.
- Pink Floyd (divagation musicale, nappes, fondu sur sample de discours).
- Narration « histoire-géo » : chaque section raconte une étape (1945, blocs, indépendances, mondialisation).

## Structure (en barres)

Intro (4) | Couplet 1 (8) | Refrain 1 (8) | Couplet 2 (8) | Refrain 2 (8) | Pont (8) | Dernier refrain (8) | Outro (4) = **56 barres**

| # | Section | Barres | Éléments clés |
| :---: | :--- | :--- | :--- |
| 1 | Intro | 1-4 | Spoken word, pad (Surge XT), arpège, nappe |
| 2 | Couplet 1 | 5-12 | Entrée batterie (rythme rock), basse, pads |
| 3 | Refrain 1 | 13-20 | Tous instruments, lead synthé (Surge XT) |
| 4 | Couplet 2 | 21-28 | Légère accélération, guitare plus saturée |
| 5 | Refrain 2 | 29-36 | Retour du chœur, plus énergique |
| 6 | Pont | 37-44 | Pause, pad, voix seule ou doublée |
| 7 | Dernier refrain | 45-52 | Crescendo, cuivres (Meldaproduction), tout le monde |
| 8 | Outro | 53-56 | Fondu, sample de discours historique, retour au calme |

## BPM Map

| Repère | Barres | BPM | Événement |
| :--- | :--- | :--- | :--- |
| Intro | 1-4 | **72** | Spoken word |
| Couplet 1 | 5-12 | **90** | Accélération linéaire sur 2 mes. |
| Refrain 1 | 13-20 | **90** | Retour du chœur |
| Couplet 2 | 21-28 | **95** | Légère accélération |
| Refrain 2 | 29-36 | **95** | Plus énergique |
| Pont | 37-44 | **80** | Ralenti |
| Dernier refrain | 45-52 | **100** | Crescendo |
| Outro | 53-56 | **100 → 72** | Retour au calme, fondu |

> ⚠️ Le doc source fournit aussi une table tempo compressée (0/8/16/24/32/36 mes → 72/90/95/80/100/72) qui omet Couplet 2 et Refrain 2. **À arbitrer : recaler les points de tempo sur la structure 56 barres ci-dessus avant l'arrangement.**

## Grille d'accords

| Section | Grille | Couleur / Sonorité |
| :--- | :--- | :--- |
| **Intro** | `C - G - Am - F` (arpégé, lent) | Ouverture lumineuse du récit. |
| **Couplet** | `C - G - Am - F` (2 temps par accord) | Rock, rythmique binaire. |
| **Refrain** | `F - G - C - Am` | Plus lumineux, énergique ; le C au climax = **Cmaj9**. |
| **Pont** | `Am - Dm - G - C` | Plus sombre, en mineur. |
| **Outro** | `C - G - Am - F` | Retour à l'intro, en fondu. |

> Transposition possible : pour une version plus grave, jouer en La majeur (`A - E - F#m - D`).

## Instruments (Ableton) — Mix

Template réel `bac.als` (indices **0-based**), pistes 0-6 MIDI, piste 7 Audio (Voix).

| Piste | Index | Instrument | Pan | Vol | Chaîne FX |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Drums** | 0 | Gen Purpose Kit (rack) | 0 | 0.85 | MCompressor (Ratio 4:1, Thresh −15 dB, Attack 5 ms, Release 80 ms) ; `MSaturator` (MCharisma — Drive/Timbre) |
| **Basse** | 1 | Surge XT — Classic Bass (Sub) | 0 | 0.80 | MDelay (Time 1/8 sync, Feedback 35 %, Mix 15 % — pont) + MEqualizer (coupe du sub) |
| **Pads/Claviers** | 2 | Surge XT — Wavetable (Saw, Unison 6, Detune 0.18) | 0 | 0.75 | Reverb (Ableton, Hall) + MFlanger + Auto Filter (autom. « pad qui s'ouvre ») ; `MCharmVerb` (MReverb) transparent |
| **Lead/Mélodie** | 3 | Surge XT — FM Pluck (Ratio 2.00, Feedback 40 %) | 0 | 0.80 | Drum Noise Glitcher (rack) + Massive Sidechain Distort (rack) ; `MWaveShaper` (MDistortion) ; Glitcher intensifié au dernier refrain (MRhythmizer) |
| **Arp/Contrepoint** | 4 | Surge XT — FM/Digital | +0.20 | 0.70 | MPhaser + MDelay (ping-pong) |
| **Fx** | 5 | Surge XT (MIDI — PAS audio) | −0.20 | 0.60 | Reverb (Ableton) + Auto Filter + `MBandPass` (MFilter) |
| **Aux/synthé2** | 6 | Surge XT — Orgues/Brass (cuivres du dernier refrain) | 0 | 0.75 | Chorus-Ensemble + Chorus + MCompressor (couvre MChorus) |
| **Voix** | 7 | Audio (spoken word + chant réel) | 0 | 0.90 (mix manuel) | MCompressor (vocal) + De-esser (couvre MDeEsser) |

> Convention : effet Meldaproduction cité par le doc mais **absent du template et non installé** → remplacé par l'équivalent gratuit de la collection installée (MSaturator, MCharmVerb, MWaveShaper, MBandPass) ou par le dispositif natif (MChorus → Chorus natif, MDeEsser → De-esser natif).

### Réglages Surge XT (du doc)
- **Drums (rack)** — Kick : Osc1 Sine, Env A:0 ms D:40 ms S:0 % R:60 ms, Pitch env −36 st. Snare : Osc1 Noise + Sine, Env A:2 ms D:80 ms. Hats : Noise, Filter HPF 800 Hz, Env D:60 ms.
- **Basse** — Osc1 « Classic Bass » (Square −12 dB, Sub osc). Filter LPF 24 dB, Cutoff 65 %, Reso 10 %. Env A:5 ms D:150 ms S:70 % R:80 ms.
- **Pads** — Osc1 Wavetable « Sawtooth », Unison 6, Detune 0.18. Filter LPF 12 dB, Cutoff 70 %, Reso 5 %. Env A:2 s D:1 s S:80 % R:3 s.
- **Lead** — Osc1 « FM Pluck », Ratio 2.00, Feedback 40 %. Filter BPF, Cutoff 50 %, Reso 20 %.

## Clips JSON (motifs principaux — temps en beats)

> Légende hauteurs (convention **C3 = 60**) : 45 A1 · 48 C2 · 49 G1 · 52 E2 · 53 F2 · 55 G2 · 57 A2 · 59 B2 · 60 C3 · 62 D3 · 77 F4 · 79 G4 · 81 A4 · 83 B4 · 84 C5 · 86 D5 · 88 E5 · 90 F#5 · 91 G5 · 95 B5.

### A. Refrain — Accords (Piste Pads/Claviers, index 2) — `F - G - Cmaj9 - Am`
Motif de 2 mesures (8 beats). **Correction appliquée : C → Cmaj9, ajout de D5 = 86 (time 4.0).** Répéter ×4 (offsets +8 / +16 / +24 beats) pour un refrain complet de 8 mesures.

```json
{
  "clip_name": "C1_Refrain_Chords",
  "bpm": 95,
  "notes": [
    { "time": 0.0, "pitch": 77, "duration": 2.0, "velocity": 85 },
    { "time": 0.0, "pitch": 81, "duration": 2.0, "velocity": 85 },
    { "time": 0.0, "pitch": 84, "duration": 2.0, "velocity": 85 },
    { "time": 0.0, "pitch": 88, "duration": 2.0, "velocity": 80 },
    { "time": 2.0, "pitch": 79, "duration": 2.0, "velocity": 80 },
    { "time": 2.0, "pitch": 83, "duration": 2.0, "velocity": 80 },
    { "time": 2.0, "pitch": 86, "duration": 2.0, "velocity": 80 },
    { "time": 2.0, "pitch": 90, "duration": 2.0, "velocity": 75 },
    { "time": 4.0, "pitch": 84, "duration": 2.0, "velocity": 85 },
    { "time": 4.0, "pitch": 86, "duration": 2.0, "velocity": 85 },
    { "time": 4.0, "pitch": 88, "duration": 2.0, "velocity": 85 },
    { "time": 4.0, "pitch": 91, "duration": 2.0, "velocity": 85 },
    { "time": 4.0, "pitch": 95, "duration": 2.0, "velocity": 80 },
    { "time": 6.0, "pitch": 81, "duration": 2.0, "velocity": 80 },
    { "time": 6.0, "pitch": 84, "duration": 2.0, "velocity": 80 },
    { "time": 6.0, "pitch": 88, "duration": 2.0, "velocity": 80 },
    { "time": 6.0, "pitch": 91, "duration": 2.0, "velocity": 75 }
  ]
}
```

### B. Couplet — Basse arpégée (Piste Basse, index 1) — `C - G - Am - F`
Motif de 2 mesures (8 beats). **Correction appliquée : l'arpège de la section G jouait D-F#-A (Ré majeur) au lieu de G — remplacé par G2-D3-B2-D3 (pitch 55-62-59-62).** Répéter ×4 (offsets +8 / +16 / +24 beats) pour un couplet complet de 8 mesures.

```json
{
  "clip_name": "C1_Couplet_Bass_Arp",
  "bpm": 90,
  "notes": [
    { "time": 0.0, "pitch": 48, "duration": 0.5, "velocity": 90 },
    { "time": 0.5, "pitch": 55, "duration": 0.5, "velocity": 80 },
    { "time": 1.0, "pitch": 52, "duration": 0.5, "velocity": 85 },
    { "time": 1.5, "pitch": 55, "duration": 0.5, "velocity": 80 },
    { "time": 2.0, "pitch": 55, "duration": 0.5, "velocity": 90 },
    { "time": 2.5, "pitch": 62, "duration": 0.5, "velocity": 80 },
    { "time": 3.0, "pitch": 59, "duration": 0.5, "velocity": 85 },
    { "time": 3.5, "pitch": 62, "duration": 0.5, "velocity": 80 },
    { "time": 4.0, "pitch": 45, "duration": 0.5, "velocity": 90 },
    { "time": 4.5, "pitch": 52, "duration": 0.5, "velocity": 80 },
    { "time": 5.0, "pitch": 49, "duration": 0.5, "velocity": 85 },
    { "time": 5.5, "pitch": 52, "duration": 0.5, "velocity": 80 },
    { "time": 6.0, "pitch": 53, "duration": 0.5, "velocity": 90 },
    { "time": 6.5, "pitch": 60, "duration": 0.5, "velocity": 80 },
    { "time": 7.0, "pitch": 57, "duration": 0.5, "velocity": 85 },
    { "time": 7.5, "pitch": 60, "duration": 0.5, "velocity": 80 }
  ]
}
```
> L'arpège Am (A-E-G-E, pitch 45-52-49-52) est conservé tel quel : coloration Am7 (A, quinte E, septième G), valide en basse. À valider à l'oreille si un Am pur (A-C-E) est préféré.

### C. Refrain — Batterie (Piste Drums, index 0) — groove rock
Kick = C1 (36), Snare = D1 (38), Hat = F#1 (42), Cymbal = A#1 (46). Motif de 2 mesures ; la snare marque le temps 3. Répéter sur les 8 mesures du refrain (hats 16e sur toutes les mesures, accents sur chaque temps).

```json
{
  "clip_name": "C1_Refrain_Drums",
  "bpm": 90,
  "notes": [
    { "time": 0.0, "pitch": 36, "duration": 0.25, "velocity": 90 },
    { "time": 0.5, "pitch": 36, "duration": 0.25, "velocity": 85 },
    { "time": 1.0, "pitch": 36, "duration": 0.25, "velocity": 95 },
    { "time": 1.5, "pitch": 36, "duration": 0.25, "velocity": 80 },
    { "time": 2.0, "pitch": 38, "duration": 0.25, "velocity": 100 },
    { "time": 2.5, "pitch": 36, "duration": 0.25, "velocity": 90 },
    { "time": 3.0, "pitch": 36, "duration": 0.25, "velocity": 85 },
    { "time": 3.5, "pitch": 36, "duration": 0.25, "velocity": 90 },
    { "time": 4.0, "pitch": 36, "duration": 0.25, "velocity": 95 },
    { "time": 4.5, "pitch": 36, "duration": 0.25, "velocity": 80 },
    { "time": 5.0, "pitch": 36, "duration": 0.25, "velocity": 90 },
    { "time": 5.5, "pitch": 36, "duration": 0.25, "velocity": 85 },
    { "time": 6.0, "pitch": 38, "duration": 0.25, "velocity": 100 },
    { "time": 6.5, "pitch": 36, "duration": 0.25, "velocity": 90 },
    { "time": 7.0, "pitch": 36, "duration": 0.25, "velocity": 85 },
    { "time": 7.5, "pitch": 36, "duration": 0.25, "velocity": 95 },
    { "time": 0.0, "pitch": 42, "duration": 0.125, "velocity": 60 },
    { "time": 0.25, "pitch": 42, "duration": 0.125, "velocity": 55 },
    { "time": 0.5, "pitch": 42, "duration": 0.125, "velocity": 60 },
    { "time": 0.75, "pitch": 42, "duration": 0.125, "velocity": 55 },
    { "time": 1.0, "pitch": 42, "duration": 0.125, "velocity": 62 },
    { "time": 1.25, "pitch": 42, "duration": 0.125, "velocity": 55 },
    { "time": 1.5, "pitch": 42, "duration": 0.125, "velocity": 60 },
    { "time": 1.75, "pitch": 42, "duration": 0.125, "velocity": 55 },
    { "time": 2.0, "pitch": 42, "duration": 0.125, "velocity": 65 },
    { "time": 2.25, "pitch": 42, "duration": 0.125, "velocity": 55 },
    { "time": 2.5, "pitch": 42, "duration": 0.125, "velocity": 60 },
    { "time": 2.75, "pitch": 42, "duration": 0.125, "velocity": 55 },
    { "time": 3.0, "pitch": 42, "duration": 0.125, "velocity": 60 },
    { "time": 3.25, "pitch": 42, "duration": 0.125, "velocity": 55 },
    { "time": 3.5, "pitch": 42, "duration": 0.125, "velocity": 60 },
    { "time": 3.75, "pitch": 42, "duration": 0.125, "velocity": 55 }
  ]
}
```

## Automations (temps en beats)

| Moment | Paramètre | Points (breakpoints) | Effet |
| :--- | :--- | :--- | :--- |
| **Toute la chanson** | Pads — Auto Filter `Frequency` (device 4, substitut du Cutoff Surge non automatable) | `0→0.30`, `32→0.50`, `64→0.80`, `96→0.40`, `128→0.90`, `144→0.20` | Le pad s'ouvre au fil du récit, respire au pont, sommet au dernier refrain. **Appliqué par clip arrangement (8 clips) : valeurs constantes par section.** |
| **Toute la chanson** | Pads — Reverb natif `Dry/Wet` (device 1) | Intro 0.50 → couplets 0.35-0.50 → refrains 0.25-0.40 → pont 0.80 → dernier refrain 0.40 → outro 0.80 | Intro immersive, pont très spacieux, retour au calme. **Appliqué par clip arrangement.** |
| **Dernier refrain** | Lead — Drum Noise Glitcher `Rack Dry/Wet` (device 1, substitut du MRhythmizer) | clip 176-208 → 0.79 (au lieu de 0.50) | Effet glitch/gate renforcé sur le climax. |
| **Pont** | Basse — MDelay | Time 1/8 sync, Feedback 35 %, Mix 15 % (uniquement pont) | Effet « dub » sur les notes de basse. **⚠️ Aucun clip basse en 144-176 → inaudible ; config appliquée à valider à l'oreille.** |
| **Tempo** | Automations par section | Voir BPM Map (72/90/95/80/100/72) | Montée en puissance du récit. |

> ⚠️ Les points de Cutoff/Reverb du doc source sont calés sur la structure compressée 36 mes ; **à re-calquer sur la structure 56 barres** (mêmes valeurs, positions décalées aux frontières de sections).

## Réglages Mix (appliqués 2026-08-10)

| Piste | Vol | Pan | Notes |
| :--- | :--- | :--- | :--- |
| Drums | 0.85 | — | MCompressor colle ; **EQ Three GainLo 0.7** (coupe le mud, garde le kick) |
| Basse | 0.78 | — | **Saturator Medium Curve (Drive 0.5, Dry/Wet 0.6)** = harmoniques « virtual sub » ; MDelay pont ; MEqualizer ; Compressor parallèle (Thresh 0.8, Ratio 0.5, Dry/Wet 0.4) |
| Pads/Claviers | 0.70 | — | Reverb Hall 30 % (Dry/Wet 0.30, Room 0.79) |
| Lead/Mélodie | 0.72 | — | **Compressor parallèle (Thresh 0.8, Ratio 0.5, Dry/Wet 0.4)** ; **Reverb insert (Dry/Wet 0.2, Room 0.45)** ; Gate 1/16 au dernier refrain |
| Arp/Contrepoint | 0.65 | +0.20 | MPhaser + MDelay ping-pong |
| Fx | 0.60 | −0.20 | MIDI (Surge XT, FM Riser) ; **pas de clip — non utilisé pour cette chanson** |
| Aux/synthé2 | 0.75 | — | Cuivres/orgues au dernier refrain (Toto Brass) |
| Voix | 0.90 (mix manuel) | — | MCompressor + De-esser ; spoken word en intro |
| **Master** | **1.0** | — | **Compressor glue (Thresh 0.7, Ratio 0.4, Release 0.3) → Limiter True Peak (Lookahead 3 ms, Ceiling 0.95)** |

### Captures de validation (position 178 beats, 12 s, dernier refrain)
| Capture | RMS | DR | Centroid | Rolloff | Sub 0-100 | Low-mid 100-250 | 1-4k | 4-10k |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Baseline | 0.157 | 16.1 | 1757 | 3384 | 7 % | 4 % | 42 % | 24 % |
| Finale | **0.25** (−12 dBFS) | **12.0** | **1684** | 3255 | **9 %** | **5 %** | 40 % | 23 % |
| Finale v5 (après Melda+automations) | **0.247** (−12 dB) | **12.1** | 1784 | 3474 | — | — | — | — |

### Sons Surge XT (chargés + tweakés via OSC)
| Instance | Piste | Patch | Tweaks |
| :--- | :--- | :--- | :--- |
| 0 | Basse | Square Bass | drift 0.07, unison (detune 0.3, 0.5 voix), osc2 Classic octave −1 sub vol 0.55 |
| 1 | Pads | MKS-70 Warm Pad | drift 0.07, unison 4 voix (detune 0.25), couche osc3 vol 0.4, width 80 %, drive 0.56, cutoff ~2 kHz, vel 0.8 |
| 2 | Lead | Classic Lead 2 | drift 21 %, unison 4 voix, couche osc3 vol 0.35, cutoff 0.5, **vibrato S-LFO sine → pitch (depth 0.03)** |
| 3 | Arp | Nice Pluck 2 | drift 0.05, unison 2 voix (detune 0.15), cutoff relevé 0.2 |
| 4 | Fx | FM Riser | (non utilisé — pas de clip) |
| 5 | Aux/Brass | Toto Brass | drift 0.06, unison 2 voix, couche osc3 vol 0.3, cutoff 0.5, width 60 % |

## Notes de production

- **Correction accord C → Cmaj9** : le C du refrain (time 4.0) reçoit D5 = 86. Vérifié : F = Fmaj7 (77-81-84-88), G = Gmaj7 (79-83-86-90), C = Cmaj9 (84-86-88-91-95), Am = Am7 (81-84-88-91) — toutes cohérentes avec leurs noms.
- **Correction basse section G** : l'arpège source (50-57-54-57 = D-F#-A, Ré majeur) ne correspondait pas au G → remplacé par G-B-D (55-62-59-62).
- **Fx en MIDI** (Surge XT) : le sample de discours historique de l'outro ira sur la piste **Voix** (audio) — via `create_audio_clip` — la piste Fx reste MIDI.
- **Spoken word** : enregistré sur la piste Voix, calé sur l'intro (barres 1-4).
- **Meldaproduction absents du template et non installés** → remplacés par les équivalents de la collection installée (MSaturator = MCharisma, MCharmVerb = MReverb, MWaveShaper = MDistortion, MBandPass = MFilter) ; MChorus couvert par Chorus natif, MDeEsser par De-esser natif, MRhythmizer par l'intensification du Drum Noise Glitcher au dernier refrain.
- **Dernier refrain** : cuivres via Aux/synthé2 (index 6, Surge Brass) + MRhythmizer gate sur le lead ; tout le monde joue.
- **Transposition optionnelle** en La majeur (A - E - F#m - D) pour une version plus grave.
- ⏳ **À valider** : adaptation de la tonalité si la mélodie (voix baryton E3-B3) sort de la tessiture.

## Problèmes de son (analyse par piste, à revoir — 2026-08-10)

Analyse solo par piste (captures position 178 beats, 10 s, dernier refrain) — évaluation sur RMS/centroid/rolloff (l'analyseur normalise le peak à 1.0).

| Piste | RMS | DR | Centroid | Rolloff | Bands clés | Diagnostic | État |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Drums | 0.060 | 24 | 1691 | 3450 | 0-100: 24 %, 1-4k: 33 %, 4-10k: 19 % | OK | ✅ |
| Basse | 0.160 | 16 | **172** | 114 | 0-100: 52 %, 1-4k: **4 %** | Trop sub, peu d'harmoniques → inaudible sur smartphone | 🟡 cutoff relevé 43→277 Hz (filter1 0.4) ; à re-valider |
| Pads | 0.19-0.22 | 13-17 | **360-412** | ~500 | 250-1000: ~82 %, 1-4k: 16 % | Fort mais **sombre** → masqué dans le mix (« on n'entend plus les pads ») | 🔴 patch intrinsèquement sombre ; à refaire |
| Lead | 0.184 | 15 | 2122 | 3925 | 1-4k: 51 %, 4-10k: 30 % | OK | ✅ |
| Arp | 0.027 | 31 | 4024 | 7299 | 1-4k: 53 %, 4-10k: 9 % | **Beaucoup trop bas** (Surge global −2 dB × amp −3.65 dB + fader 0.65) | 🟡 amp→0 dB, global→0.99, fader→0.78 ; à re-valider |
| Fx / Voix | — | — | — | — | — | Pas de clips (Fx = MIDI seul ; Voix vide) | ⏸ |

### Pads — synthèse du problème (le point bloquant)
- **Patch « MKS-70 Warm Pad » intrinsèquement sombre** : aucun contenu au-dessus de ~1 kHz, même filtres Surge complètement ouverts.
- Vérifications faites : filtre 1 → 8 kHz (0.85) puis filtre 2 → 8 kHz (0.85) : centroid quasi inchangé (395→412). Auto Filter bypässé : inchangé (393). → **le filtre n'est PAS la cause ; c'est le timbre/patch**.
- MSaturator (device 5, chargé pour générer des harmoniques) : « Harmonics » à 0.7 → centroid **a baissé** (412→360) ; mapping non vérifié (AGENTS.md). **Remis à 0 (transparent), device conservé inactif.**
- Tentative couche osc3 octave-up : pitch 0.55 = seulement +0.7 st (mapping non linéaire, pas +12) → **annulée** (pitch re-0.5, vol re-0.4).
- **À refaire (au retour)** : soit patch pad plus brillant dans Surge, soit couche octave +12 validée (OSC read-back pour caler le pitch), soit saturation à mapping vérifié. Ensuite refaire la capture solo (cible : centroid ~800-1500, présence 1-4k).

### État des modifications Surge (conservées)
- **Arp (instance 3)** : amp volume 1.0 (0 dB), global 0.99, fader piste 0.78 → bien plus audible. ✅ conservé.
- **Basse (instance 0)** : filter1 cutoff 0.15→0.4 (277 Hz) → expose les harmoniques. 🟡 conservé, à valider.
- **Pads (instance 1)** : filter1 + filter2 à 0.85 (8 kHz) — conservés (brightness, sans effet notable seul). osc3 reverted (vol 0.4, pitch 0.5).
- ⚠️ **Session non sauvegardée** — penser à **Ctrl+S** (save_project MCP ne fonctionne pas).

## Intégration MCP

Indices **0-based** (0 = Drums, 1 = Basse, 2 = Pads/Claviers, 3 = Lead/Mélodie, 4 = Arp/Contrepoint, 5 = Fx, 6 = Aux/synthé2, 7 = Voix). Temps des notes en **beats**.

1. **Tempo** : `set_tempo(bpm)` — 72 (intro) → 90 (couplet 1) → 95 (refrains) → 80 (pont) → 100 (dernier refrain) → 72 (outro).
2. **Intro** : `create_clip(2, 0, 16)` (nappe pad Surge XT) et `create_clip(4, 0, 16)` (arpège) ; spoken word enregistré sur piste 7.
3. **Couplet 1** : `create_clip(1, 0, 32)` puis `add_notes_to_clip(1, 0, notes)` avec le JSON B (basse) ; `create_clip(0, 0, 32)` + JSON C (drums) ; pads d'accords sur index 2.
4. **Refrains** : `create_clip(2, 1, 32)` + JSON A (accords, Cmaj9 corrigé) ; lead sur `create_clip(3, 0, 32)` + `add_notes_to_clip`.
5. **Pont** : `create_clip(2, 2, 32)` pads ; activer MDelay sur la basse (`set_device_parameter`).
6. **Dernier refrain** : cuivres via `create_clip(6, 0, 32)` ; activer MRhythmizer (gate) sur le lead.
7. **Outro** : fondu ; sample de discours via `create_audio_clip(7, 0, "chemin/vers/sample.wav")`.
8. **Arrangement** : `duplicate_to_arrangement(track_index, clip_index, destination_time)` pour chaque clip aux positions en beats (1 barre = 4 beats).
9. **Automations** : `set_automation_curve(track_index, clip_index, target, points, is_arrangement=True)` avec les breakpoints ci-dessus (Filter Cutoff et Reverb Mix en beats).

## Paroles
Voir `PAROLES.md` dans ce dossier.
