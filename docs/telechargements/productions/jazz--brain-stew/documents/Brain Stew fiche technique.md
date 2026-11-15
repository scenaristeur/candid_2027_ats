# Brain Stew — Fiche Technique (Version Jazz PMJ)
# Thème de la chanson 
A song where Billie Joe Armstrong sings about insomnia from methamphetamine usage. Armstrong admitted to using speed for writing most of the band’s early songs. The symptoms, especially the album’s titular ‘insomnia’ are typical of methamphetamine usage.

It’s also notable for segueing directly to the next track, “Jaded,” to the point the single had both together.

## Identité

| Champ | Valeur |
|---|---|
| Titre | Brain Stew |
| Artiste original | Green Day (album *Insomniac*, 1995) |
| Style cible | Postmodern Jukebox — torch song / swing rétro vintage (ambiance Mrs Maisel) |
| Tonalité | **E mineur** |
| Tempo | **77 BPM** — swing lent et sombre |
| Signature | 4/4 |
| Durée cible | ~1:40 (32 barres) |

## Concept

Reprise « vintage » façon Postmodern Jukebox : le riff punk descendant A-G#-F#-F-E est réharmonisé en grille de jazz sombre, au son d'un club des années 50. Haunting, langoureux, balais sur ride, walking bass contrebasse, Rhodes + vibraphone old-school, saxo ténor lead (patch Surge). Comme « Basket Case » de PMJ (style Mrs Maisel) et la « haunting reharmonization » de Brain Stew faite par PMJ.

## Grille harmonique (loop 2 barres = 8 temps)

```
| A7#11 (2t) | Gmaj7 (2t) | F#m7b5 (2t) | F7#9 (1t) | Em9 (1t) ||
```

Détail des temps (hérité du riff original : A à t0, G à t2, F# à t4, F à t6, E à t7) :

| Temps | Degré | Accord |
|---|---|---|
| 0 | VII7 | A7#11 |
| 2 | bVIImaj7 | Gmaj7 |
| 4 | vi m7b5 | F#m7b5 |
| 6 | bVI7#9 | F7#9 |
| 7 | i m9 | Em9 (résolution) |

Fonctions en Em : approche chromatique descendante de 2 barres résolvant sur la tonique — très « jeu de nuit ».

## Structure (scènes, Vue Session)

| Scène | Slot | Barres | Beats | Contenu |
|---|---|---|---|---|
| Intro | 1 | 4 | 16 | Rhodes vamp seule → basse walk @b8 → balais @b12 |
| Head A | 2 | 8 | 32 | Trio complet, sax joue le head (riff réharmonisé) |
| Head B | 3 | 8 | 32 | Intensité : sax variation + vibraphone/pad couleurs |
| Solo Sax | 4 | 8 | 32 | Impro sax sur la grille |
| Outro | 5 | 4 | 16 | Em9 tenu, ralenti, dernier accord |

**Total : 32 barres / 128 beats / ~1:40**

## Playback & Instruments

| Track | Index | Instrument | VST/natif | Notes |
|---|---|---|---|---|
| Jazz Rhodes | 0 | E-Piano Rhodish.adg | natif `query:Sounds#Piano%20&%20Keys:FileId_4848` | vamp/comping |
| Upright Bass | 1 | Upright Bass.adv | natif `query:Sounds#Bass:FileId_6515` | walking bass |
| Tenor Sax | 2 | Surge XT — patch `Tenor Sax` (Dan Maurer) | VST3 + OSC instance 0 | lead, head + solo |
| Pad Colors | 3 | Warm Analog Pad.adg | natif `query:Sounds#Pad:FileId_4979` | couleurs Head B |
| Vibraphone | 4 | Vibraphone.adg | natif `query:Sounds#Mallets:FileId_5039` | (option) contre-chant |
| Brushed Drums | 5 | Gen Purpose Kit.adg (FileId_5419) | natif rack | ride 50, HH 42/44, kick 36, snare 38 |

Mapping kit confirmé : kick 36, snare 38, HH closed 42, HH open 44, **ride 50**, crash 48.

### Patch Surge XT dispo (si besoin trompette en 2e voix cuivre)
- `Clean Trumpet` (Malfunction) / `Miles Trumpet` (LinnStrument MPE)
- `Orchestral Trombone` (Nick Moritz) / `Trumpet` (John Valentine)

## Règles de vélocité

| Instrument | Plage |
|---|---|
| Kick | 110-127 |
| Snare | 95-120 |
| HH / ride | 60-90 (croches), 70-90 (temps forts) |
| Basse fondamentale | 85-100 |
| Basse passages | 65-80 |
| Rhodes nappes | 65-80 |
| Rhodes accents | 85-100 |
| Vibraphone | 70-90 |
| Sax (phrasé) | 80-110 |

Varier les vélocités entre répétitions (jamais de groove plat).

## Premix (2026-08-06)

État validé piste par piste (solo → capture → plage + volume). Capture master : RMS 0.103, centroid 1616 Hz, rolloff 3533 Hz, dynamic range 19.8 dB. Master à 0.75.

| Track | Volume | EQ / Devices | Rôle fréquentiel | Captures solo (RMS, centroid) |
|---|---|---|---|---|
| Jazz Rhodes (0) | 0.85 | EQ Three : GainLo 0.7 (coupe bas) | comping médium, laisse le bas à la basse | 0.099 / 911 Hz |
| Upright Bass (1) | 0.85 | Saturator **Bass Shaper** (Drive 0.3, Color Low 0.4, Color Hi 0.6) + EQ Three **GainMid 1.0** (boost ~150-500 Hz via FreqHi 0.5) | fondation : sub 41-82 Hz + harmoniques audibles | 0.15 / 472 Hz |
| Tenor Sax (2) | 0.95 | Surge XT patch `Tenor Sax`, global vol 0.7, résonance 60 %, release 353 ms + EQ Three GainMid 0.85 (flat) + Saturator Analog Clip (Drive 0.46, mix 0.33, Color off, Post Soft) | lead, dénasalisé | 0.155 / 1091 Hz |
| Pad Colors (3) | 0.15 | EQ Three : GainHi 0.5 (assombrit), GainLo 0.7 | fond Head B uniquement (beats 48-80) | 0.34 → dompté ~0.05 |
| Vibraphone (4) | 0.85 | — | contre-chant brillant (Head B + Outro) | 0.065 / 2597 Hz |
| Brushed Drums (5) | 1.0 | Utility Output 0.5 (+~9.5 dB) | support : ride 2-4, brushes aigus | 0.09 / 2242 Hz |
| Guide Vocal (6) | 0.85 | muet | — | — |
| 8-Audio Voix (7) | 0.85 | Saturator off, Compressor, MEqualizer, Limiter ; clip `Audio 6` gain 0.569 = 6.75 dB | voix, take à refaire | 0.128 / 872 Hz |
| Master | 0.75 | — | — | — |

### Découvertes techniques (premix)
- **Gain clip arrangement normalisé 0-1 (pas dB)** : 0.4 = 0 dB, 0.506 = 4.25 dB, 0.569 = 6.75 dB, 0.6 = 8 dB, 0.65 = 10 dB.
- **Mapping gain EQ Three très compressé** : GainMid/GainLo/GainHi ~0.85 = flat, 0.95 = quasi rien, **1.0 = boost max (+15 dB)**. La plage utile du boost est [~0.98 … 1.0]. Les cuts (0 → 0.85) semblent plus linéaires.
- **Basse E1-C2 (41-82 Hz) = contrebasse authentique** mais 100 % sub → inaudible en mix. Rendu audible via boost EQ mid (GainMid 1.0), pas via transposition.
- **Le pic de capture reste à 1.0 quel que soit le master** → saturation de l'interface de capture (VB-Cable), PAS du mix. Se fier à RMS/centroid.
- **Capture 20 s réelles** (WAV ~40 s) : les lectures de Head B incluent pad/vibes. Capturer au beat 56 pour les instruments Head B-only.
- Le Sax n'utilisait PAS le bon patch Surge (`unknown`) → rechargé `Tenor Sax` (Dan Maurer) : patch correct + note sur le diagnostic.

## Mix final (2026-08-06) — « vrai mix de producteur »

Complété et **validé à l'oreille** : staging → carving → dynamique → profondeur → master. Master à l'unité (1.0) avec glue + limiter.

| Track | Volume | EQ / Devices | Rôle fréquentiel |
|---|---|---|---|
| Jazz Rhodes (0) | 0.85 | EQ Three : GainLo 0.7 (coupe bas) | comping médium |
| Upright Bass (1) | 0.85 | Saturator Bass Shaper (Drive **0.3**, Color Low 0.4, Color Hi 0.6) + EQ Three GainMid 1.0 + **Compressor** (Threshold 0.8, Ratio 0.5, Dry/Wet 0.4) | fondation sub + présence médium |
| Tenor Sax (2) | 0.71 | Surge XT Tenor Sax + EQ Three GainMid 0.85 (flat) + Saturator Analog Clip (Drive 0.46, mix 0.33) + **Compressor** (Threshold 0.8, Ratio 0.5, Dry/Wet 0.4) + **Reverb** (Dry/Wet **0.2**, Room Size **0.45**) | lead + profondeur |
| Pad Colors (3) | 0.15 | EQ Three : GainHi 0.5, GainLo 0.7 | fond Head B |
| Vibraphone (4) | 0.85 | — | contre-chant |
| Brushed Drums (5) | 1.0 | Utility Output 0.5 + **EQ Three GainLo 0.6** (coupe bas = moins de mud, plus de brillance balais) | support |
| Guide Vocal (6) | 0.85 | muet | — |
| 8-Audio Voix (7) | 0.85 | Saturator off, Compressor, MEqualizer, Limiter + **Reverb** (Dry/Wet **0.18**, Room Size **0.4**) ; clip `Audio 6` gain 0.569 | voix + profondeur |
| **Master** | **1.0** | **Compressor glue** (Threshold 0.7, Ratio 0.4, Release 0.3) → **Limiter** (Mode True Peak, Lookahead 3 ms, Ceiling ~0.95 ≈ **-1 dB**) | niveau final, anti-écrêtage |

### Captures master final
- **Head A (beat 16)** : RMS 0.206 (**-13.7 dBFS**), centroid 1597 Hz, rolloff 3515 Hz, **DR 13.7 dB**
- **Head B (beat 56)** : RMS 0.256 (**-11.8 dBFS**), centroid 1708 Hz, rolloff 3804 Hz, **DR 11.8 dB**

### Découvertes techniques (mix final)
- **Returns A-Reverb / B-Delay** : étaient vides au moment du mix (les sends n'avaient AUCUN effet — testé send 0.2 vs 0.7 → résultat identique) → Reverb en **insert** direct sur sax et voix. **Depuis, les returns sont peuplés** (Reverb sur A-Reverb, Delay sur B-Delay) et de **nouveaux outils MCP** permettent de les contrôler : `get_return_tracks`, `get_return_track_device_parameters`, `set_return_track_device_parameter`, `set_return_track_volume`, `load_instrument_or_effect_on_return_track` (`return_index` 0=A-Reverb, 1=B-Delay). Un contrôle par send est donc redevenu possible.
- **Modification du Remote Script → redémarrage d'Ableton obligatoire** (le `reload` via `deploy_rs.py` est non fiable : nouveaux handlers manquants ou hang). Ensuite redémarrer le serveur MCP pour exposer les nouveaux outils.
- **Glue Compressor indisponible en Live Lite** (`query:AudioFx#Glue Compressor` introuvable) → utiliser le **Compressor standard** en glue (ratio faible, seuil haut).
- **Le fader master est EN AVAL des devices insert** : pour un master plafonné à -1 dB, le volume master doit être à **1.0** (à l'unité). À 0.75 la sortie serait sous le ceiling.
- **Master à 1.0 sans limiter → écrêtage interne** (RMS 0.231, DR 12.7). Avec le limiter True Peak : propre (DR 13.7).
- **Captures solo basse peu fiables** : le « boost 472 Hz » documenté au premix venait du test `eqmax` (Saturator saturé, RMS 5x plus fort, 1000-4000 Hz = 29 %). À Drive 0.3 la basse est propre mais sub-dominée (0-100 Hz ≈ 65 %) — **validée à l'oreille dans le mix**.
- Le `Compressor` chargé en insert ne dégrade pas le spectre (testé réglages différents → résultats identiques) : compression quasi transparente en Dry/Wet parallèle.

## À faire

- [ ] **Refaire la prise vocale** — la prise `Audio 6 [2026-08-06 142842]` sature au début ; chaîne voix en place sur piste 8 (Saturator off, Compressor, MEqualizer, Limiter), gain clip 6.75 dB, warp off, pitch 0. Enveloppe posée. À ré-enregistrer puis rééquilibrer voix/thème (le master final est calibré sur la prise actuelle).
- [x] Exposer les return tracks dans le Remote Script (outils `get_return_tracks`, `get_return_track_device_parameters`, `set_return_track_device_parameter`, `set_return_track_volume`, `load_instrument_or_effect_on_return_track`). Returns désormais peuplés (Reverb/Delay) → contrôle par send possible.

## Notes & Limitations

- Index 0-based (track 0 = première piste, clip 0 = premier slot)
- Clips de référence d'origine conservés en slot 0 (ne pas supprimer)
- `save_project()` indisponible → sauvegarder avec Ctrl+S
- La batterie par défaut joue du rock binaire → réécrire en pattern swing (ride sur les 2-4 + offbeats)
- Automation arrangement = write-once ; travailler en session puis dupliquer
