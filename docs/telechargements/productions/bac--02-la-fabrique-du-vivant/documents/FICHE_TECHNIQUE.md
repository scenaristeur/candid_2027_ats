# 02 — La Fabrique du Vivant

**Tempo**: 68 → 84 → 88 → 72 → 88 → 68 BPM (map par section)
**Tonalité**: Mi mineur modal (Em)
**Durée**: ≈ 3 min 30 (68 barres — arrangement complet)
**Atmosphère**: Nappe ambient, laboratoire vivant, émergence du code génétique
**Style**: Ambient / Psytrance lente (ADN, polymérase, équilibres chimiques, photosynthèse)
**Voix**: Baryton parlé-chanté (E3 → B3, pitch 64-71), spoken word en intro

## Concept
- ADN (A-T / G-C), polymérase, mutations
- Équilibres chimiques (loi de Le Chatelier), photosynthèse / respiration
- Flux d'énergie, matière qui s'échange

## Structure (en barres)

Intro (12) | Couplet 1 (8) | Refrain (8) | Couplet 2 7/8 (8) | Refrain (8) | Pont 4/4 (8) | Outro (16) = **68 barres**

| # | Section | Barres | Éléments clés |
| :---: | :--- | :--- | :--- |
| 1 | Intro | 1-12 | Spoken word, nappe ambient, arpège ADN (DNA Arp) |
| 2 | Couplet 1 | 13-20 | Entrée sub bass, arpège, nappe continue |
| 3 | Refrain | 21-28 | Kick sidechain psytrance, lead hélicoïdal, basse puissante |
| 4 | Couplet 2 (7/8) | 29-36 | Break bancal en 7/8, nappe dissonante |
| 5 | Refrain | 37-44 | Retour de l'énergie, MRhythmizer actif |
| 6 | Pont (4/4) | 45-52 | Ralenti, basse secondaire « Subduction », dissonant |
| 7 | Outro | 53-68 | Fondu, arpège ADN en boucle, retour au calme |

## BPM Map

| Repère | Barres | BPM | Événement |
| :--- | :--- | :--- | :--- |
| Intro | 1-12 | **68** | Nappes, spoken word |
| Couplet 1 | 13-20 | **84** (linéaire sur 2 m) | Entrée du groove |
| Refrain | 21-28 | **88** | Kick sidechain, lead |
| Couplet 2 (7/8) | 29-36 | **72** | Break bancal |
| Refrain | 37-44 | **88** | Retour de l'énergie |
| Pont (4/4) | 45-52 | **72** | Ralenti, dissonant |
| Outro | 53-68 | **68** (fondu) | Retour au calme, dégradé |

> ⚠️ Le doc source fournit une table tempo compressée (0/6/14/22/30/36 m → 68/84/88/72/88/68) qui ne contient que 6 repères et **omet le Couplet 2 en 7/8**. **À arbitrer : recaler les points de tempo sur la structure 68 barres ci-dessus avant l'arrangement** (le 7/8 change la durée réelle d'une « mesure » = 3,5 temps).

## Grille d'accords

| Section | Grille | Couleur / Sonorité |
| :--- | :--- | :--- |
| **Intro** | `Em9 - Am11 - D7b9 - Gmaj7#5` | Nappe modale ; la `Gmaj7#5` (#5) donne le côté « hélice brisée ». |
| **Couplet** | `Em9 - F#m7b5 - B7alt - Em9` | Mineur modal, tension chromatique. |
| **Refrain** | `Am11 - D13 - Gmaj9 - C#m7b5` | Modulation ascendante, plus lumineux. |
| **Pont** | `F#maj7 - Bbm11 - Ebmaj13#11` | Quartale, dissonant, descente vers l'outro. |

> Rappel harmonique (vérification des accords) : Em9 = E-G-B-D-F# · Am11 = A-C-E-G-B(-D) · D7b9 = D-F#-A-C-Eb · Gmaj7#5 = G-B-D#-F#.

## Instruments (Ableton) — Mix

Template réel `bac.als` (indices **0-based**), pistes 0-6 MIDI, piste 7 Audio (Voix).

| Piste | Index | Instrument | Pan | Vol | Chaîne FX |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Drums** | 0 | Gen Purpose Kit (rack) | 0 | 0.85 | MCompressor (colle) ; `MRhythmizer` (preset "16T Psy", Mix 30 %) à charger |
| **Basse** | 1 | Surge XT — Sub Bass | 0 | 0.80 | MDelay (dub) + MEqualizer (coupe du sub) |
| **Pads/Claviers** | 2 | Surge XT — Ambient Pad | 0 | 0.75 | Reverb (Ableton) + MFlanger ; `MReverb` (Decay 5 s) à charger |
| **Lead/Mélodie** | 3 | Surge XT — Lead Hélicoïdal | 0 | 0.80 | Drum Noise Glitcher (rack) + Massive Sidechain Distort (rack) ; `MDelay` (Ping-Pong 1/4) à charger |
| **Arp/Contrepoint** | 4 | Surge XT — DNA Arp | +0.20 | 0.70 | MPhaser + MDelay ; `MFlanger` (Rate 0.8 Hz, Depth 70 %) à charger |
| **Fx** | 5 | Surge XT (MIDI — PAS audio) | −0.20 | 0.60 | Reverb (Ableton) + Auto Filter ; `MFilter` (LFO Sin 0.3 Hz sur Cutoff) à charger |
| **Aux/synthé2** | 6 | Surge XT — Basse Secondaire « Subduction » | 0 | 0.75 | Chorus-Ensemble + Chorus + MCompressor ; `MEqualizer` (boost 60 Hz, coupe 200 Hz) à charger |
| **Voix** | 7 | Audio (spoken word + chant réel) | 0 | 0.90 (mix manuel) | MCompressor (Ratio 4:1, Att 3 ms) + De-esser ; `MDeEsser` 6 kHz à charger |

> Convention : effet Meldaproduction cité par le doc mais absent du template → mentionné « à charger ». Le doc prévoyait la piste Fx en Audio (samples de labo) → **mappée sur la piste Fx MIDI du template** (Surge XT) comme toutes les pistes du template ; les samples ADN/pipettes passeront par le sampler Surge ou la piste Voix.

### Réglages Surge XT (du doc)
- **Drums (rack)** — Kick : Sine + Noise, Env A:1 ms D:60 ms. Snare : Noise, HPF 700 Hz. Hats : Wavefolded Sine.
- **Basse (Sub)** — Osc1 Triangle −12 dB, Osc2 Sine sub. LPF 24 dB, Cutoff 55 %. Env A:2 ms D:180 ms S:60 %.
- **DNA Arp (P4)** — Wavetable « Glass », Index 45 %. Unison 8, Detune 0.22. Filter BPF 55 %. L'Unison 8 = l'hélice qui tourne.
- **Ambient Pad (P2)** — Osc1 Saw + Osc2 Square ringmod. LPF 12 dB, Cutoff 40 %. Env A:4 s D:2 s S:90 % R:4 s.
- **Lead Hélicoïdal (P3)** — FM Ratio 2.00, Feedback 45 %. Env A:5 ms D:300 ms.
- **Basse Secondaire (P6)** — « Subduction » (Osc1 Square + Sine).

## Clips JSON (motifs principaux — temps en beats)

> Légende hauteurs (convention **C3 = 60**) : 57 A2 · 60 C3 · 62 D3 · 64 E3 · 66 F#3 · 67 G3 · 69 A3 · 71 B3 · 73 C4 · 74 D4 · 75 D#4/Eb4 · 78 F#4 · 82 A#4.
> Convention vélocité : 0-100. `time` en beats (4/4 : 1 mesure = 4 temps ; le Couplet 2 en 7/8 = 3,5 temps par mesure).

### A. Intro — Accords (Piste Pads/Claviers, index 2) — `Em9 - Am11 - D7b9 - Gmaj7#5`
Boucle de 4 mesures (16 beats), 1 accord par mesure. **Corrections appliquées :**
- `Gmaj7#5` (time 12.0) : le doc donnait 67, 71, 74, 79, 82 (G3-B3-D4-G4-A#4) — **remplacé par 67, 71, 75, 78** = G3-B3-D#4-F#4. **Correction obligatoire.**
- `D7b9` (time 8.0) : pitch 76 = E (9e naturelle) au lieu de la b9 → **corrigé en 75 = Eb4**. D7b9 = D-F#-A-C-Eb.
- `Em9` (64, 67, 71, 74, 78) vérifié ✓ = E3-G3-B3-D4-F#4.
- `Am11` (57, 60, 64, 67, 71) vérifié ✓ = A2-C3-E3-G3-B3 (optionnel : ajouter D4=74 pour l'11e complète).

```json
{
  "clip_name": "C2_Pad_Chords",
  "bpm": 68,
  "notes": [
    { "time": 0.0, "pitch": 64, "duration": 4.0, "velocity": 80 },
    { "time": 0.0, "pitch": 67, "duration": 4.0, "velocity": 75 },
    { "time": 0.0, "pitch": 71, "duration": 4.0, "velocity": 80 },
    { "time": 0.0, "pitch": 74, "duration": 4.0, "velocity": 70 },
    { "time": 0.0, "pitch": 78, "duration": 4.0, "velocity": 65 },
    { "time": 4.0, "pitch": 57, "duration": 4.0, "velocity": 80 },
    { "time": 4.0, "pitch": 60, "duration": 4.0, "velocity": 75 },
    { "time": 4.0, "pitch": 64, "duration": 4.0, "velocity": 80 },
    { "time": 4.0, "pitch": 67, "duration": 4.0, "velocity": 75 },
    { "time": 4.0, "pitch": 71, "duration": 4.0, "velocity": 70 },
    { "time": 8.0, "pitch": 62, "duration": 4.0, "velocity": 85 },
    { "time": 8.0, "pitch": 66, "duration": 4.0, "velocity": 80 },
    { "time": 8.0, "pitch": 69, "duration": 4.0, "velocity": 85 },
    { "time": 8.0, "pitch": 73, "duration": 4.0, "velocity": 75 },
    { "time": 8.0, "pitch": 75, "duration": 4.0, "velocity": 70 },
    { "time": 12.0, "pitch": 67, "duration": 4.0, "velocity": 80 },
    { "time": 12.0, "pitch": 71, "duration": 4.0, "velocity": 75 },
    { "time": 12.0, "pitch": 75, "duration": 4.0, "velocity": 80 },
    { "time": 12.0, "pitch": 78, "duration": 4.0, "velocity": 70 }
  ]
}
```

## Automations (temps en beats)

> Les points du doc sont donnés en mesures sur la table compressée (0/6/14/22/30/36) → **convertis en beats (×4) ci-dessous, à re-calquer sur les frontières de sections de la structure 68 barres**.

| Moment | Paramètre | Points (breakpoints) | Effet |
| :--- | :--- | :--- | :--- |
| **Toute la chanson** | Arp — Cutoff (Surge XT, DNA Arp, index 4) | `0→0.2`, `24→0.8`, `56→0.9`, `88→0.3`, `120→0.9`, `144→0.1` | L'arpège ADN s'ouvre (refrains), se referme sur le break et l'outro. |
| **Toute la chanson** | Drums — MRhythmizer Wet/Dry (à charger) | `0→0%`, `56→35%`, `88→10%`, `120→40%` | Stutter psytrance sur les refrains, allégé au break. |
| **Tempo** | Automations par section | Voir BPM Map (68/84/88/72/88/68) | Nappes lentes → groove → break → fondu. |

## Réglages Mix

| Piste | Vol | Pan | Notes |
| :--- | :--- | :--- | :--- |
| Drums | 0.85 | — | MCompressor colle ; MRhythmizer gate sur refrains |
| Basse | 0.80 | — | Sub ; MDelay (dub) + MEqualizer coupe le sub |
| Pads/Claviers | 0.75 | — | Nappe ringmod ; MReverb (à charger) selon automations |
| Lead/Mélodie | 0.80 | — | Hélicoïdal ; sidechain sur le kick |
| Arp/Contrepoint | 0.70 | +0.20 | DNA Arp Unison 8 ; MPhaser + MDelay ping-pong |
| Fx | 0.60 | −0.20 | MIDI (Surge XT) ; Auto Filter LFO |
| Aux/synthé2 | 0.75 | — | Basse secondaire « Subduction » ; boost 60 Hz |
| Voix | 0.90 (mix manuel) | — | MCompressor + De-esser ; spoken word en intro |

## Notes de production

- **Correction obligatoire Gmaj7#5** : `time 12.0` → voicing 67, 71, 75, 78 (G3, B3, D#4, F#4). Vérifié : G-B-D#-F# = Gmaj7#5.
- **Correction D7b9** : pitch 76 (E, 9e) → 75 (Eb4, b9). Le commentaire du doc « F (b9) » était faux : la b9 de D est Eb.
- **Couplet 2 en 7/8** : 1 mesure = 3,5 temps. Les `time` des notes et automations de cette section doivent utiliser cette unité (p. ex. slot 0, 3.5, 7.0, 10.5...).
- **Fx en MIDI** (Surge XT) : les samples ADN / bruits de pipettes prévus en Audio passent par la piste Fx MIDI du template — via le sampler Surge XT (ou sur la piste Voix pour les voix traitées).
- **Kick sidechain** : le rack Massive Sidechain Distort du lead + MCompressor de la batterie créent la respiration « psytrance » sur les refrains (coups de kick = pompage).
- **Meldaproduction absents du template** → à charger : MRhythmizer, MReverb, MDelay (Lead), MFlanger (Arp), MFilter, MEqualizer (Aux), MDeEsser.
- **Outro** : arpège ADN en boucle, fondu global 68 BPM, la voix s'entrelace avec l'hélice.
- ⏳ **À valider** : adaptation de la tonalité si la mélodie (voix baryton E3-B3) sort de la tessiture.

## Intégration MCP

Indices **0-based** (0 = Drums, 1 = Basse, 2 = Pads/Claviers, 3 = Lead/Mélodie, 4 = Arp/Contrepoint, 5 = Fx, 6 = Aux/synthé2, 7 = Voix). Temps des notes en **beats**.

1. **Tempo** : `set_tempo(bpm)` — 68 (intro) → 84 (couplet 1) → 88 (refrains) → 72 (couplet 2 7/8 + pont) → 88 (dernier refrain) → 68 (outro).
2. **Intro** : `create_clip(2, 0, 48)` (nappe pad, 12 barres = 48 beats) puis `add_notes_to_clip(2, 0, notes)` avec le JSON A (corrigé). Boucle de 4 mesures à répéter (offsets +16 / +32 / +48...). Spoken word enregistré sur piste 7.
3. **Couplet 1** : `create_clip(1, 0, 32)` (sub bass) et `create_clip(4, 0, 32)` (DNA Arp) puis `add_notes_to_clip` sur chacun ; nappe sur index 2.
4. **Refrains** : `create_clip(0, 0, 32)` + groove kick sidechain (Gen Purpose Kit) ; lead sur `create_clip(3, 0, 32)` + `add_notes_to_clip`.
5. **Couplet 2 (7/8)** : clips sur 28 temps (8 mesures × 3,5) — nappe + arpège, batterie allégée.
6. **Pont** : `create_clip(6, 0, 32)` basse secondaire « Subduction » ; MDelay dub sur la basse (`set_device_parameter`).
7. **Outro** : arpège en boucle sur `create_clip(4, 1, 64)` ; fondu.
8. **Arrangement** : `duplicate_to_arrangement(track_index, clip_index, destination_time)` pour chaque clip aux positions en beats (1 barre 4/4 = 4 beats, 1 barre 7/8 = 3,5 beats).
9. **Automations** : `set_automation_curve(track_index, clip_index, target, points, is_arrangement=True)` avec les breakpoints ci-dessus (Cutoff Surge XT et MRhythmizer Mix en beats).

## Paroles
Voir `PAROLES.md` dans ce dossier.

## État d'avancement (2026-08-10)

**Fait — maquette instrumentale complète (session + arrangement 268 temps) :**
- Scènes session : Intro (slot 0, validée) · Couplet 1 (slot 1) · Refrain 1 (slot 2) · Couplet 2 7/8 (slot 3, 28 temps/clip) · Refrain 2 (= Refrain 1 réutilisé) · Pont (slot 5, Subduction sur piste 6) · Outro (slot 6, 64 temps).
- Groupes de notes générés (JSON) : `_gen_refrain.py`, `_gen_rest.py` + `data/analyses/_refrain_*.json`, `_c2p_*.json`, `_pont_*.json`, `_outro_*.json`.
- Arrangement : clips posés via `duplicate_to_arrangement` aux temps suivants (beats) : Intro 0, Couplet1 48, Refrain 80, Couplet2 112, Refrain 140, Pont 172, Outro 204 → fin 268.
- Patch Pads (Surge XT inst 1) sculpté via OSC : Init Saw, 3 osc detune (±7¢) + osc3 +1 oct, poly 32, AEG A0.85/R0.85, LP12 cutoff 277 Hz résonance 0.15, SLFO lent sur cutoff, width 1.3.

**Restant :**
- ⏳ **Automations tempo par section** : FAIT — réglé manuellement par David (68→84→88→72→88→68).
- ⏳ **Voix (piste 7)** : enregistrement réel du chant/spoken word (par David). Appuyer poitrine baryton E3-B3 ; C4 ponctuel en mixte.
- ⏳ **Charger les plugins Meldaproduction** (absents) : Drums→MRhythmizer (preset "16T Psy", Mix 30 %) ; Basse→MDelay+MEQ ; Pads→MReverb (Decay 5 s) ; Lead→MDelay (Ping-Pong 1/4) ; Arp→MFlanger (0.8 Hz, 70 %) ; Fx→MFilter (LFO Sin 0.3 Hz) ; Aux→MEQ (boost 60 Hz, coupe 200 Hz) ; Voix→MDeEsser 6 kHz, MCompressor (4:1, 3 ms).
- ⏳ **Automations enveloppes** : Arp Cutoff (`0→0.2, 24→0.8, 56→0.9, 88→0.3, 120→0.9, 144→0.1`) et Drums MRhythmizer Wet/Dry (`0→0%, 56→35%, 88→10%, 120→40%`) — points à re-calquer sur les frontières de sections.
- ⏳ **Mix complet** : staging/volumes, carving EQ, dynamique, profondeur (sends), master glue+limiteur, validation captures + à l'oreille (cf. skill full-mix-workflow / mix-translation). Ne pas appliquer les chaînes FX doc en aveugle.
- ⏳ **Validation tessiture** : adapter la mélodie si la voix sort de E3-B3.
