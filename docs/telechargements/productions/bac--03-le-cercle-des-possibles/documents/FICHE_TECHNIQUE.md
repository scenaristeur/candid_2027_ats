# 03 — Le Cercle des Possibles

**Tempo**: 55 → 122 → 88 → 120 BPM (map tempo, voir BPM Map)
**Tonalité**: Bbmaj (intro) / Gmaj (refrain) — modulations jazz (accords clusters, #11, alt)
**Durée**: ≈ 3 min (estimation à calibrer — 44 barres)
**Atmosphère**: Math rock / jazz fusion, mécanique intellectuelle, bancal puis lumineux
**Style**: Math Rock / Jazz Fusion (batterie tordue, basse slap, accords clusters)
**Voix**: Baryton parlé-chanté, tessiture **E3–B3 (pitch 64–71)**

## Concept

Liberté (déterminisme vs libre arbitre), Raison (Descartes, Kant), Probabilités (loi binomiale, écart-type), Limites (suites convergentes, asymptotes). Le cercle : la boucle du hasard et de la raison qui se referme.

## Structure (en barres)

| Section | Signature | Barres | Contenu |
| :--- | :---: | :---: | :--- |
| **Intro** | 5/4 | 4 | Compteur Geiger + roue de casino, grille intro (Bbmaj9 → Eb9sus4 → Amaj7#11 → Dm13) |
| **Couplet 1** | 5/4 | 8 | « Bancal » : voix parlé-chantée, basse slap, batterie polyrythmique |
| **Refrain 1** | 4/4 | 8 | Lumineux : grille refrain × 2 (Gmaj9 → Cmaj13#11 → F#7alt → Bm9) |
| **Couplet 2** | 4/4 | 8 | Calme, piano solo : Rhodes, voix posée |
| **Pont** | 4/4 | 4 | Explosion bruitiste (lead glitch, samples horloge/casino) |
| **Refrain 2** | 4/4 | 8 | Dernier refrain, 120 BPM |
| **Outro** | 3/4 | 4 | Batterie qui se décompose en 3/4 ; **55 BPM** (retour au tempo de l'intro, la boucle se referme) |
| **Total** | — | **44** | |

## BPM Map

> Temps du doc en **beats** (noires). Signature 5/4 : 1 mesure = 5 beats ; 4/4 : 1 mesure = 4 beats. À aligner sur la structure en barres à l'implémentation.

| Repère | Temps (beats) | BPM | Signature |
| :---: | :---: | :---: | :---: |
| Départ | 0.0 | **55** | 5/4 |
| Accélération | 8.0 | **122** | 4/4 |
| Pont | 24.0 | **88** | 4/4 |
| Dernier refrain | 32.0 | **120** | 4/4 |

## Grille d'accords

| Section | Grille | Couleur / Sonorité |
| :--- | :--- | :--- |
| **Intro (5/4)** | `| Bbmaj9 | Eb9sus4 | Amaj7#11 | Dm13 |` | Quartale/altérée, clusters bancaux. Le triton Amaj7#11 → Dm13 (sous-dominante mineure) ouvre le cercle. |
| **Refrain (4/4)** | `| Gmaj9 | Cmaj13#11 | F#7alt | Bm9 |` | Cycle de quintes modifié. Le F#7alt (dominante altérée) tire vers Bm9 — lumineux et suspendu. |

## Instruments (Ableton) — Mix

> Pistes = template réel `bac.als`, indices **0-based**. Toute piste Fx est MIDI (Surge XT). Un effet Meldaproduction cité par le doc mais absent du template est marqué **« à charger »**.

| Piste | Index | Instrument (Surge XT) | Chaîne FX (template) | Réglages doc / à charger |
| :--- | :---: | :--- | :--- | :--- |
| **Drums** | 0 | Gen Purpose Kit (rack polyrythmique : Kick C1, Snare D1, Hi-Hat F#1, Ride A#1) | MCompressor | MCompressor **Attack 2 ms, Release 60 ms** |
| **Basse fretless** | 1 | Surge XT « Smooth Bass » (Osc1 Sine, **Portamento 80 ms**) | MDelay + MEqualizer | `MChorus` (Rate 1.2 Hz) — **à charger** (absent du template) |
| **Pads / Claviers** | 2 | Surge XT « Electric Piano » (FM ratio **1.5**) — rôle Rhodes | Reverb (Ableton) + MFlanger | `MPhaser` (Stages 6, Rate 0.4 Hz) — **à charger** |
| **Lead / Mélodie** | 3 | Surge XT « FM Digi » (Ratio **4.0**, Feedback **30 %**) — son « glitch » | Drum Noise Glitcher (rack) + Massive Sidechain Distort (rack) | `MRhythmizer` (Preset « Glitch 1/8 ») — **à charger** |
| **Arp / Contrepoint** | 4 | Surge XT Wavetable « Sawtooth » + **LFO sur Cutoff 0.6 Hz** (modulation interne Surge) — nappe modulée | MPhaser + MDelay | `MReverb` (Hall) — **à charger** |
| **Fx** | 5 | Surge XT (sound design : roulette de casino, compteur Geiger reproduits en bruit/bruitage) | Reverb + Auto Filter | Doc : samples audio (mais piste 5 = **MIDI**) ; `MFilter` (LFO en dent de scie) — remplacé par **Auto Filter** du template |
| **Aux / Synthé 2** | 6 | Surge XT « Organ » — tenues (guitare saturée tenue / organ) | Chorus-Ensemble + Chorus + MCompressor | Chorus du template = tenue saturée/lumineuse |
| **Voix** | 7 | Audio (micro) — baryton parlé-chanté E3–B3 | MCompressor + De-esser | `MDelay` (Slap **80 ms**) — **à charger** |

## Clips JSON (blocs valides)

> `time` en **beats**, pitch = note MIDI (C3 = 60), velocity **0–100**. Signature 5/4 : 2 mesures = 10 temps.

### Motif principal — Basse (piste 1) en 5/4 sur `Bbmaj9 - Eb9sus4`

```json
{
  "clip_name": "C3_Bass_54",
  "notes": [
    { "time": 0.0, "pitch": 46, "duration": 1.0, "velocity": 90 },
    { "time": 1.0, "pitch": 53, "duration": 1.0, "velocity": 80 },
    { "time": 2.0, "pitch": 50, "duration": 1.0, "velocity": 85 },
    { "time": 3.0, "pitch": 55, "duration": 0.5, "velocity": 80 },
    { "time": 3.5, "pitch": 58, "duration": 0.5, "velocity": 75 },
    { "time": 4.0, "pitch": 46, "duration": 1.0, "velocity": 90 },
    { "time": 5.0, "pitch": 53, "duration": 1.0, "velocity": 80 },
    { "time": 6.0, "pitch": 51, "duration": 1.0, "velocity": 85 },
    { "time": 7.0, "pitch": 56, "duration": 1.0, "velocity": 80 },
    { "time": 8.0, "pitch": 58, "duration": 1.0, "velocity": 85 },
    { "time": 9.0, "pitch": 63, "duration": 1.0, "velocity": 75 }
  ]
}
```

### Accords intro (piste 6 Organ / piste 2 Rhodes) en 5/4, 4 mesures (20 temps)

```json
{
  "clip_name": "C3_Intro_Chords_54",
  "notes": [
    { "time": 0.0, "pitch": 70, "duration": 5.0, "velocity": 70 },
    { "time": 0.0, "pitch": 74, "duration": 5.0, "velocity": 65 },
    { "time": 0.0, "pitch": 77, "duration": 5.0, "velocity": 60 },
    { "time": 0.0, "pitch": 81, "duration": 5.0, "velocity": 55 },
    { "time": 0.0, "pitch": 84, "duration": 5.0, "velocity": 50 },
    { "time": 5.0, "pitch": 63, "duration": 5.0, "velocity": 70 },
    { "time": 5.0, "pitch": 70, "duration": 5.0, "velocity": 65 },
    { "time": 5.0, "pitch": 73, "duration": 5.0, "velocity": 60 },
    { "time": 5.0, "pitch": 80, "duration": 5.0, "velocity": 55 },
    { "time": 10.0, "pitch": 69, "duration": 5.0, "velocity": 70 },
    { "time": 10.0, "pitch": 73, "duration": 5.0, "velocity": 65 },
    { "time": 10.0, "pitch": 76, "duration": 5.0, "velocity": 60 },
    { "time": 10.0, "pitch": 80, "duration": 5.0, "velocity": 55 },
    { "time": 10.0, "pitch": 86, "duration": 5.0, "velocity": 50 },
    { "time": 15.0, "pitch": 62, "duration": 5.0, "velocity": 70 },
    { "time": 15.0, "pitch": 65, "duration": 5.0, "velocity": 65 },
    { "time": 15.0, "pitch": 69, "duration": 5.0, "velocity": 60 },
    { "time": 15.0, "pitch": 72, "duration": 5.0, "velocity": 55 },
    { "time": 15.0, "pitch": 76, "duration": 5.0, "velocity": 50 },
    { "time": 15.0, "pitch": 83, "duration": 5.0, "velocity": 45 }
  ]
}
```

### Accords refrain (piste 6 Organ) en 4/4, 4 mesures (16 temps)

```json
{
  "clip_name": "C3_Refrain_Chords",
  "notes": [
    { "time": 0.0, "pitch": 67, "duration": 4.0, "velocity": 75 },
    { "time": 0.0, "pitch": 71, "duration": 4.0, "velocity": 70 },
    { "time": 0.0, "pitch": 74, "duration": 4.0, "velocity": 65 },
    { "time": 0.0, "pitch": 78, "duration": 4.0, "velocity": 60 },
    { "time": 0.0, "pitch": 81, "duration": 4.0, "velocity": 55 },
    { "time": 4.0, "pitch": 72, "duration": 4.0, "velocity": 75 },
    { "time": 4.0, "pitch": 76, "duration": 4.0, "velocity": 70 },
    { "time": 4.0, "pitch": 79, "duration": 4.0, "velocity": 65 },
    { "time": 4.0, "pitch": 83, "duration": 4.0, "velocity": 60 },
    { "time": 4.0, "pitch": 86, "duration": 4.0, "velocity": 55 },
    { "time": 4.0, "pitch": 90, "duration": 4.0, "velocity": 50 },
    { "time": 8.0, "pitch": 66, "duration": 4.0, "velocity": 75 },
    { "time": 8.0, "pitch": 70, "duration": 4.0, "velocity": 70 },
    { "time": 8.0, "pitch": 72, "duration": 4.0, "velocity": 65 },
    { "time": 8.0, "pitch": 76, "duration": 4.0, "velocity": 60 },
    { "time": 8.0, "pitch": 79, "duration": 4.0, "velocity": 55 },
    { "time": 12.0, "pitch": 71, "duration": 4.0, "velocity": 75 },
    { "time": 12.0, "pitch": 74, "duration": 4.0, "velocity": 70 },
    { "time": 12.0, "pitch": 78, "duration": 4.0, "velocity": 65 },
    { "time": 12.0, "pitch": 81, "duration": 4.0, "velocity": 60 },
    { "time": 12.0, "pitch": 85, "duration": 4.0, "velocity": 55 }
  ]
}
```

### Corrections & vérifications d'accords (C3 = 60)

| Accord | Composition | Voicing retenu | Pitch | Statut |
| :--- | :--- | :--- | :--- | :--- |
| **Bbmaj9** | Bb D F A C | Bb3–D4–F4–A4–C5 | 70–74–77–81–84 | ✓ |
| **Eb9sus4** | Eb Bb Db Ab (+9 F optionnel) | Eb3–Bb3–Db4–Ab4 | 63–70–73–80 | ✓ |
| **Amaj7#11** | A C# E G# D | A3–C#4–E4–G#4–D5 | 69–73–76–80–86 | ✓ |
| **Dm13** | D F A C E B | D3–F3–A3–C4–E4–B4 | 62–65–69–72–76–83 | ✓ |
| **Gmaj9** | G B D F# A | G3–B3–D4–F#4–A4 | 67–71–74–78–81 | ✓ |
| **Cmaj13#11** | C E G B D F# | C4–E4–G4–B4–D5–F#5 | 72–76–79–83–86–90 | ✓ |
| **F#7alt** | F# A# C# E + b9 (G) / b5 | F#3–A#3–C4–E4–G4 | 66–70–72–76–79 | ✓ |
| **Bm9** | B D F# A C# | B3–D4–F#4–A4–C#5 | 71–74–78–81–85 | ✓ |

**Correction de commentaires du doc (basse)** : sous la convention C3 = 60, pitch 46 = **Bb1** (le doc commentait « Bb2 »), pitch 51 = **Eb2**. Hauteurs et vélocités inchangées — le motif est valide tel quel.

## Automations

| Moment | Paramètre | Points breakpoints (beats) | Effet produit |
| :--- | :--- | :--- | :--- |
| **Intro → Couplet 1** | Tempo (courbe exponentielle) | 55 → 122 BPM sur 4 mesures (à aligner avec la BPM map) | Accélération : la mécanique s'emballe |
| **Chanson** | P4 (Lead) Filter Cutoff | `(0.0, 0.1)` → `(8.0, 0.9)` → `(24.0, 0.3)` → `(32.0, 0.95)` | Le lead glitch s'ouvre/se referme |
| **Nappe** | Piste 4 — Cutoff Surge XT (LFO interne) | LFO **0.6 Hz** sur Cutoff | Nappe modulée (pulsation du cercle) |
| **Fx** | Piste 5 — Auto Filter | LFO en dent de scie (1/8) | Compteur Geiger / roulette qui tourne |
| **Pont** | Lead glitch + samples | Explosion bruitiste (MRhythmizer Glitch 1/8 si chargé) | Chaos déterministe |

## Réglages Mix

| Piste | Vol | Pan | Notes |
| :--- | :---: | :---: | :--- |
| Drums | 0.80 | 0 | Polyrythmique, MCompressor Attack 2 ms / Release 60 ms |
| Basse fretless | **0.60** | 0 | **Baisse pour saturation master** (patch Fretless amp -6 dB, notes sub graves Bb1 + portamento) ; Slap, Portamento 80 ms, sub couvert par MEqualizer |
| Pads / Claviers (Rhodes) | 0.80 | −0.20 | Piano électrique FM, lumineux mais en retrait |
| Lead / Mélodie | 0.75 | +0.20 | FM Digi, glitch rythmé |
| Arp / Contrepoint (nappe) | 0.70 | 0 | Wavetable + LFO Cutoff 0.6 Hz, fond |
| Fx | 0.60 | 0 | Horloge/casino, Auto Filter, discret |
| Aux / Synthé 2 (Organ) | 0.75 | 0 | Tenues accord, Chorus — porteur du refrain |
| Voix | 0.90 (mix manuel) | 0 | MCompressor + De-esser, parlé-chanté baryton |

## Production Notes

- **Intro** : compteur Geiger et roue de casino (bruitages) sur la grille Bbmaj9 → Eb9sus4 → Amaj7#11 → Dm13, tempo lent 55 BPM.
- **Couplet 1 (5/4 bancal)** : la signature 5/4 + basse slap + batterie polyrythmique donnent l'effet « instable » du libre arbitre.
- **Refrain (4/4 lumineux)** : cycle de quintes modifié (Gmaj9 → Cmaj13#11 → F#7alt → Bm9). Le F#7alt est la tension « P = NP » résolue sur Bm9.
- **Couplet 2 (calme, piano solo)** : seuls le Rhodes et la voix — l'équation intime avant l'explosion.
- **Pont (explosion bruitiste)** : lead glitch + samples, chaos déterministe ; le « nombre d'or » et « l'entropie » en cri.
- **Outro (3/4)** : la batterie se décompose, le cercle se referme — revenir à la signature impaire pour la boucle avec l'intro.
- **Voix baryton** : parlé-chanté E3–B3, tension croissante des couplets au pont.
- ⏳ **À valider** : adaptation de la tonalité si la mélodie sort de la tessiture baryton (E3–B3).

## Intégration MCP

- Tempo : `set_tempo(bpm)` (points de la BPM map : 55 → 122 → 88 → 120).
- Clips session : `create_clip(track_index, clip_index, length)` puis `add_notes_to_clip(track_index, clip_index, notes)` avec `notes` = blocs JSON ci-dessus (time en beats).
- Indices 0-based : Drums 0, Basse 1, Pads/Claviers 2, Lead 3, Arp/Contrepoint 4, Fx 5, Aux/Synthé2 6, Voix 7.
- Surge XT : chargement des patches et réglages (Portamento, FM ratio, Feedback, LFO Cutoff) via les paramètres OSC de l'instance concernée.
- Effets « à charger » (MChorus, MPhaser Rhodes, MRhythmizer, MReverb Hall, MDelay voix) : ajoutés manuellement puis réglés par `set_device_parameter`.

## Paroles

Voir `PAROLES.md` dans ce dossier.

## État d'avancement (2026-08-10)

**Fait — maquette instrumentale complète (session + arrangement 184 temps = 44 mesures) :**
- Scènes session : Intro (slot 0, 20 t, 5/4) · Couplet 1 (slot 1, 40 t, 5/4) · Refrain 1 (slot 2, 32 t, 4/4) · Couplet 2 (slot 3, 32 t, 4/4 — Rhodes+basse seuls) · Pont (slot 4, 16 t, 4/4 — drums+lead+Fx) · Refrain 2 (= Refrain 1 réutilisé) · Outro (slot 6, 12 t, 3/4 — drums+Rhodes).
- Notes générées (JSON) : `data/analyses/_gen_c3.py` + `data/analyses/_c3_*.json`. Insertion fiabilisée via `data/analyses/_send_notes.py` (même protocole TCP 9877 que le serveur).
- Arrangement (beats) : Intro 0 · Couplet1 20 · Refrain 60 · Couplet2 92 · Pont 124 · Refrain2 140 · Outro 172 → fin 184.
- Remarque : la piste Fx (5) étant MIDI (template), les bruitages Geiger/casino sont des clicks genérés par Surge XT (patch par défaut), pas des samples audio du doc.

**Restant :**
- ⚠️ **Signature non automatisable** : contrario du tempo (enveloppe automatisable), la signature (5/4, 4/4, 3/4) **ne peut PAS être automatisée** dans Live. Conséquence pour la 03 qui change de mètre. Clips posés en **beats** (indépendants de la signature) donc le timing reste correct ; mais le repère de barres et le feel impair (5/4 bancal, 3/4 outro) exigent : (1) en Vue Session → **signature par scène** (chaque scène a sa propre signature, commutée au launch) — fait ; (2) en arrangement → placer les **changements de signature manuellement sur la timeline** (Live les stocke par position, mais pas via `set_automation_curve`).
- ⚠️ **Signature : GLOBALE uniquement dans l'arrangement** (confirmé) : Live n'autorise qu'**une seule signature d'ensemble** dans la vue Arrangement — il est **impossible d'en placer de différentes sur la timeline** (les signatures par scène n'existent qu'en Vue Session). Les sections 5/4, 4/4, 3/4 partagent donc la grille de l'arrangement (choisir une signature globale de compromis, ex. 4/4). Le timing reste correct car les clips sont posés en beats ; le feel impair (5/4 bancal, 3/4 outro) est porté par le contenu des clips et par la Vue Session pour le travail/composition.
- ⚠️ **Re-record Session→Arrangement via MCP testé, NON concluant** : `session_record=True` + `start_playback` + `fire_scene` lance bien les scènes (signature/tempo de session commutent, le playhead avance) mais **n'écrit PAS les clips dans l'arrangement** car le transport Record (`song.record_mode`) n'est pas exposé par le Remote Script. Les clips d'arrangement restent ceux posés par `duplicate_to_arrangement` (vérifiés intacts). Approche retenue : clips via `duplicate_to_arrangement` (fait) + **tempo automatisé à la main** dans l'enveloppe d'arrangement (fait par David) + signature globale unique.
- ⏳ **Automations tempo par section** : 55→122→88→120 (à poser manuellement dans Live, comme pour la chanson 02 ; la table tempo compressée du doc est à recaler sur les frontières de barres ci-dessus).
- ⏳ **PATCHES Surge XT à façonner via OSC** (instances) : Basse « Smooth Bass » (Osc1 Sine, Portamento 80 ms) ; Rhodes « Electric Piano » (FM ratio 1.5) sur piste 2 ; Lead « FM Digi » (Ratio 4.0, Feedback 30 %) sur piste 3 ; Nappe Wavetable + LFO Cutoff 0.6 Hz sur piste 4. Actuellement en patches par défaut (la maquette sonne avec les patches chargés du template).
- ⏳ **Charger les plugins Meldaproduction** (absents) : Basse→MChorus (1.2 Hz) ; Rhodes→MPhaser (6 étages, 0.4 Hz) ; Lead→MRhythmizer (Glitch 1/8) ; Arp→MReverb (Hall) ; Voix→MDelay (Slap 80 ms). MCompressor Drums Attack 2 ms / Release 60 ms.
- ⏳ **Automations enveloppes** : P4 Lead Filter Cutoff `(0,0.1)→(8,0.9)→(24,0.3)→(32,0.95)` ; Nappe LFO 0.6 Hz (interne Surge) ; Fx Auto Filter LFO dent de scie 1/8.
- ⏳ **Voix (piste 7)** : enregistrement parlé-chanté baryton E3–B3 (par David), tension croissante vers le pont.
- ⏳ **Mix complet** : staging, EQ, dynamique, profondeur, master glue+limiteur, validation captures + à l'oreille (skills full-mix-workflow / mix-translation).
- ⏳ **Validation tessiture** : adapter si la mélodie sort de E3–B3.
