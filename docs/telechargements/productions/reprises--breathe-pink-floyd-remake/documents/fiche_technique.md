# Fiche technique — Breathe (Pink Floyd) [remake]

Source : `Breathe/Pink Floyd — Breathe in the Air [MIDIfind.com].mid`
Tempo : 140 BPM | Signature : 4/4 | Durée : ~2.5 min | 89 bars
Fusion : 7 pistes MIDI (0-4,6) + piste 7 audio (voix). Tempo 140.

## Pistes (indices 0-based)

| Ableton | Instrument chargé | URI | Source |
|---|---|---|---|
| 0 | 1-Batterie — **Selector Kit Warm** | `query:Drums#FileId_5282` | track 6 |
| 1 | 2-Guit — **Guitar Electric Clean** | `query:Sounds#Guitar%20&%20Plucked:FileId_5053` | track 0 |
| 2 | 3-SlideGuit — **Guit Layter** | `query:Sounds#Guitar%20&%20Plucked:FileId_5051` | tracks 2,3 |
| 3 | 4-Basse — **Electric Bass Soft** | `query:Sounds#Bass:FileId_5202` | track 5 |
| 4 | 5-Clavier — **Warm Analog Pad** | `query:Sounds#Pad:FileId_4979` | track 1 |
| 5 | 6-Libre | — | — |
| 6 | 7-GuideVocal — **Sweet Lead** | `query:Sounds#Synth%20Lead:FileId_4636` | track 4 |
| 7 | 8-Voix (audio) | — | ta voix |

## Scènes (session view) — tempo 140

| Scène | Bars | Beats | Notes |
|---|---|---|---|
| 0 | 1–26 | 104 | intro/motif |
| 1 | 27–60 | 136 | dev |
| 2 | 61–89 | 116 | fin |

## Factorisation (top xN ≥ 3 → FACTORISER en groove court + fills)

| Piste | sc0 | sc1 | sc2 |
|---|---|---|---|
| Batt | x7 | x6 | x9 |
| Guit | var | x4 | var |
| Slide | x12 | x7 | x6 |
| Basse | x4 | x4 | var |
| Clavier | x11 | x17 | x13 |
| Guide | — | x18 | x5 |

Fort factorisable : Clavier (x17), Guide (x18), Slide (x12). Batt + basse aussi → clips groove courts.

## Options / forks à tester (TODOs)

- [ ] **Kit batterie** : tester Foundation Dance Kit (`FileId_15025`) pour + d'énergie, ou Drum Machine
      Selector Kit (`FileId_5280`) rétro-moderne, si Selector Warm manque de "pêche" ou CPU.
- [ ] **Slide Guit** : alternatives à Guit Layter : Atmo Pluck `4773`, Ionosphere Guitar `5058`,
      Oscillation Guitar `5061` (plus éthéré) — si Guit Layter trop simple.
- [ ] **Clavier** : alternatives pad/nappe : Cathedral Keys (spatial), Analog natif `query:Synths#Analog`
      (chaud) — si Warm Analog Pad trop "usine".
- [ ] **Guide vocal** : alternatives Sweet Lead : Radio Lead `10039` (voix), CatSynth — pour guider le
      chant plus naturellement.
- [ ] **Basse** : Electric Bass (moteur), Pale (dit applicable) si besoin de plus de grain : Saturator
      Bass Shaper + comp parallèle (workflow Keep Talking).
- [ ] **CPU** : si Saturations/effect à 8 pistes trop lourd, fusionner/desactiver devices, ou loader
      moins de Surge. Tester `get_cpu_load` en jeu.
- [ ] **Si manque quelque chose** : doubler la nappe clavier + delay (profondeur), ou ajouter un
      sous-basse pour le "sport".

## Thème / intention
Hymne au souffle, au sport, à la méditation, à la reconnexion. Objectif : "donner la pêche" tout en
gardant l'air/la respiration de l'original. Paroles originales (Breathe, Dark Side of the Moon) :
respiration, vivre l'instant, ne pas avoir peur de ressentir, choisir son chemin.

## Réglages appliqués (mix instrumental)

| Piste | FX / réglage |
|---|---|
| 1-Batterie | Selector Kit Warm : DrBuss **Drive 45**, **Boom 60**, **Comp 35** |
| 2-Guit | Chorus-Ensemble (Mode Ensemble, Width 0.8, Dry/Wet 0.35) |
| 3-SlideGuit | Reverb (Room 0.6, Dry/Wet 0.25, Decay 0.4) |
| 4-Basse | Saturator **Bass Shaper** (Drive 0.3, Dry/Wet 0.7) |
| 5-Clavier | Saturator Medium Curve (Drive 0.35, Wet 0.7) + **EQ Three GainLo 0.5** (HPF, libère la basse) |

Volume final : basse **0.95** (fondement), clavier **0.70**, reste 0.85. Pan slide remis à 0.
Status basse : validée (centroid solo 584, bande 150-400 nettoyée du pad).

## Master chain (Live Lite) — BREATHE
- Compressor **glue** : Threshold 0.8, Ratio 0.25, Release 0.3
- Limiter **True Peak** : Ceiling 0.95 (~-1 dB), Lookahead 3 ms
- Fader master : 1.0

## Captures finale (avec master)
| Section | Beat | RMS | Centroid | Rolloff | DR |
|---|---|---|---|---|---|
| sc0 | 0 | 0.145 | 1072 | 2111 | 16.8 |
| sc1 | 104 | 0.156 | 1052 | 2106 | 16.1 |
| sc2 | 240 | 0.239 | 1086 | 2294 | 12.4 |

Bel arc d'énergie (0.145→0.239), centroid stable ~1070, C# mineur.

## Vélocités
Les vélocités sont **préservées de la source** (prépare_midi garde les vélos dans `_scenes_notes.json`, injectées telles quelles) — donc les variations existent déjà. ⚠️ Si on FACTORISE (groove court bouclé), répéter les motifs avec variations, sinon vélos aplaties.

## À faire (workflow)
- [x] Tweak instrus + FX (AVANT capture)
- [x] Dupliquer vers l'arrangement (`duplicate_to_arrangement` destination_time beats : 0/104/240)
- [x] Capture/analyse RMS-centroid-rolloff-DR (3 sections)
- [x] Mix 6 étapes + master glue+limiter
- [x] Charger les notes (clips 0-2 injectées)
- [ ] Écoute finale complète (export smartphone)
- [ ] (option) factorisation batterie si besoin CPU

## Outils
- notes : `_scenes_notes.json` (3 scènes)
- prep : `prep_midi.py` / `prep_anycolour_group.py`
- factorisation : `prep_midi.py` output `/Factorisation par piste`
- skill `midi-remake`
