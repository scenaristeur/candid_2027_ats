# Le Train des Possibles — Structure

## Arrangement Blueprint (Non-Binary Structure)

Pas de formule intro–couplet–refrain–pont classique. Sections non-déterministes.

| Section | Durée | Contenu |
|---------|-------|---------|
| **A** | 8 bars | Quantum Pad + Snoop Bass + vocal spoken (pitch-less) |
| **B** | 16 bars | Ajout Mozartium lead (contre-mélodie à la voix), drums entrent à bar 5 |
| **C** | 12 bars | **Refrain** → harmonie complète, toutes voix, claps, explosion reverb |
| **D** | 8 bars | Break → seulement delay feedbacks + samples vocaux inversés |
| **E** | 16 bars | Climax → tous les instruments + nouvelle mélodie (train whistle en whole-tone) |
| **F** | 12 bars | Outro → fade progressif, ne restent que pad + filtered snare |
| **Coda** | ∞ | Boucle infinie du delay sur la dernière note, spectral freeze à 3.7 kHz |

## Correspondance Paroles → Sections

| Section | Paroles | Bars |
|---------|---------|------|
| A | Intro spoken ("Yeah... Un, deux, quantique...") | 1–8 |
| B | Couplet 1 ("C'était un jeune garçon...") + Pré-refrain ("Les injonctions pleuvaient...") | 9–24 |
| C | Refrain ("Ce train-là, il va vers l'inconnu...") | 25–36 |
| B' | Couplet 2 ("Il a croisé des regards...") + Pont ("Il a fermé les yeux...") | 37–60 |
| D | Break (instrumental) | 61–68 |
| E | Climax ("JE SUIS UN UNIVERS À PART ENTIÈRE !") + Break parlé ("Check it out...") | 69–84 |
| C' | Refrain final ("Ce train-là, il va vers l'inconnu...") | 85–96 |
| F | Outro ("Iel est devenu son propre chef d'orchestre...") + spoken | 97–108 |
| Coda | Dernière note + delay infini | ∞ |

## Tonalité Fondamentale — La Gamme Schrödinger

**Gamme hexatonique non-octaviante** (inspirée Wendy Carlos Alpha + octatonique symétrique, détourée d'un quart de ton sur la 3e note).

```
! schrodinger.scl
Schrödinger Hexatonic
6
203.91
386.31
498.04
702.00
884.36
1017.60
```

Degrés : 1, ♭2 (quarter-flat), 3 (neutral), 4, ♭5 (quarter-sharp), 6, ♭7 (harmonic), 8

## Progressions Harmoniques (Non-Fonctionnelles)

### Versets — Polychords en superposition

```
| AΔ♯5 (no3) / B♭maj7♭5 | D♭^♯11 / E♭maj9♯5 | F♯ø7 / GΔ♯5 | Cmaj7♯9♭13 / Dm6/9 |
```

### Refrain — Le "Train" lift

```
| E♭maj13♯11 / Amaj7♭5 | BΔ♯9 / C♯m6/9 | Fmaj9♯11 / G♯Δ♯5 | Dm7♭5 / Abmaj7♯11 |
```

## Track Mapping Actuel (0-indexé)

| Index | Nom Ableton | Rôle | Devices / FX Chain |
|-------|-------------|------|--------------------|
| 0 | 1 Voice | Groupe vocal (à remplir) | Channel EQ → Reverb |
| 1 | 2 Quantum Pad | Quantum Pad (Surge) | Surge XT → Erosion → Delay → Auto Filter |
| 2 | 2-Snoop Bass | Snoop Bass (Surge) | Surge XT → Saturator → Compressor → Auto Pan-Tremolo |
| 3 | 3-Mozartium | Mozartium (Surge) | **Arpeggiator** (UpDown, 1/16, Gate 50%, Retrig Note) → Surge XT |
| 4 | 4-Drums | Drums | Drum Rack → Compressor → Erosion |
| 5 | 5-Percussion FX | Percussion FX (Simpler) | Simpler → Auto Shift → Beat Repeat → Reverb |
| 6 | 6-Texture | Texture (Simpler) | Simpler → Delay → Reverb |

**Remarques Live Lite** : Pas d'Operator, Multiband, EQ8, Shifter, Filter Delay, Hybrid Reverb, Grain Delay, Spectral Resonator, Corpus. Adapté avec les équivalents Lite.

## Surge XT Patches — État Actuel

### Patch A — Quantum Pad (instance 0, track 0)

**Patch de base** : `Ghost Pad` (factory) — nappe atmosphérique spectrale, reverb + delay déjà intégrés

**Ajustements OSC appliqués :**

| OSC Address | Valeur | Effet |
|---|---|---|
| `/param/a/aeg/attack` | 0.9 | Attaque très lente (~4s) — fondu d'entrée |
| `/param/a/aeg/sustain` | 1.0 | Sustain infini |
| `/param/a/octave` | 1 | Monte d'une octave pour la nappe |
| `/param/a/send/1/level` | 0.6 | Reverb renforcée |
| `/param/a/send/2/level` | 0.4 | Delay présent |

**FX intégrés au patch** : Reverb (fx/a/1, type 1) + Delay (fx/a/2, type 6)

### Patch B — Snoop Bass (instance 1, track 1)

**Patch de base** : `Waveshaper Bass` (Luna) — déjà du growl via waveshaper

**Ajustements OSC appliqués :**

| OSC Address | Valeur | Effet |
|---|---|---|
| `/param/a/play_mode` | 1 (Mono) | Mode monophonique (basse) |
| `/param/a/portamento` | 0.15 | Glide ~80ms |
| `/param/a/osc/2/type` | 0 (Sine) | Sub sine ajouté |
| `/param/a/osc/2/octave` | -1 | Sub une octave en dessous |
| `/param/a/mixer/osc2/mute` | 0 (unmuted) | Sub activé |
| `/param/a/mixer/osc2/volume` | 0.6 | Volume sub modéré |

**Modulation active** : LFO1 (random S&H par défaut) → Osc1 Param1 (depth 0.3)

### Patch C — Mozartium (instance 2, track 2)

**Patch de base** : `Classic Lead 1` (factory) — lead classique, bonne base pour un lead mozartien

**Ajustements OSC appliqués :**

| OSC Address | Valeur | Effet |
|---|---|---|
| `/param/a/osc/1/param7` | 7 | Unison 7 voix |
| `/param/a/osc/1/param6` | 0.04 | Détune ±2 cents |
| `/param/a/filter/1/type` | 2 (BP) | Filtre band-pass (sonorité "classique") |
| `/param/a/filter/1/cutoff` | 0.5 | Fréquence centrale |
| `/param/a/mixer/noise/volume` | 0.15 | Bruit léger ajouté |
| `/param/a/mixer/noise/mute` | 0 (unmuted) | Noise activé |

**Modulation active** : LFO3 (sine) → Filter Cutoff (depth 0.4)

## Règles "Non-Déjà-Vu"
- Pas de 808s → sine wave avec phase distortion
- Pas de piano (sauf ghost en reverb) → celesta + glass + metal
- Pas de 16th hi-hats droites → bursts (1/32, rest, 1/16 triplets)
- Pas d'accords majeurs/mineurs → add♭13 ou sus♯11 par défaut
- Pas de répétition finale du refrain → nouveau matériel harmonique aux 16 dernières bars
- Pas de fade-out → cut abrupt sur une note delayed qui décroît naturellement
