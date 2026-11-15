# STATUS — Comptine des Traboules

## État : Mix finalisé — Master Limiter + Saturator Harpe. RMS 0.124, centroid 980 Hz, DR 18.1 dB ✅

## Session Ableton
- **BPM** : 88
- **Signature** : 4/4
- **Loop** : 0 → 352 beats (88 barres)
- **CPU** : ~20% (polyphony limitée)

## Piste Layout

| Track | Nom | Type | Instrument | OSC Instance | Poly |
|-------|-----|------|------------|--------------|------|
| 0 | Voix | Audio | External (muted) | — | — |
| 1 | Harpe | MIDI | Surge XT — Harpie | 0 (53280/53281) | 4 |
| 2 | Basse | MIDI | Surge XT — Fingered | 1 (53282/53283) | 3 |
| 3 | Flûte | MIDI | Surge XT — Moon Flute | 2 (53284/53285) | 4 |
| 4 | Percussions | MIDI | 606 Core Kit | — | — |
| 5 | Cordes | MIDI | Surge XT — Chamber Strings | 3 (53286/53287) | 6 |
| Return A | FX | Audio | | — | — |
| Return B | FX | Audio | | — | — |

## Clips Session (7 sections × 5 tracks = 35 clips)

| Section | Beats | Harpe | Basse | Flûte | Percussions | Cordes |
|---------|-------|-------|-------|-------|-------------|--------|
| Intro | 0-31 (32b) | 64 notes | 2 notes | 6 notes | 40 notes | 7 notes |
| Couplet A | 32-95 (64b) | 128 notes | 8 notes | 15 notes | 84 notes | 26 notes |
| Refrain | 96-143 (48b) | 96 notes | 4 notes | 10 notes | 60 notes | 13 notes |
| Pont | 144-175 (32b) | 64 notes | 4 notes | 4 notes | 32 notes | 12 notes |
| Couplet B | 176-239 (64b) | 128 notes | 8 notes | 15 notes | 84 notes | 26 notes |
| Refrain 2 | 240-287 (48b) | 96 notes | 4 notes | 10 notes | 60 notes | 13 notes |
| Outro | 288-351 (64b) | 72 notes | 3 notes | 5 notes | 56 notes | 10 notes |

## Arrangement
- **35 clips dupliqués** dans l'arrangement (5 tracks × 7 sections)
- **Positions** : Intro@0, CoupletA@32, Refrain@96, Pont@144, CoupletB@176, Refrain2@240, Outro@288

## Surge XT OSC Params

### Instance 0 — Harpie
- Filter cutoff: **0.50**, Attack: **0.05s**, Release: **0.75s**, FX: off, Volume: **0.75**, Poly: 4

### Instance 1 — Fingered
- Filter cutoff: **0.25**, Resonance: 0.25, Attack: **0.15s**, Release: **0.5s**, Volume: **0.9**, Poly: 3

### Instance 2 — Moon Flute
- Filter cutoff: **0.40**, Attack: **0.25s**, Release: **0.75s**, FX: off, Volume: **0.65**, Poly: 4

### Instance 3 — Chamber Strings
- Attack: **0.8s**, Release: **0.9s**, Filter cutoff: **0.30**, FX: off, Volume: **0.70**, Poly: 6

## Sends (Return A — Reverb)

| Track | Send A (Reverb) |
|-------|-----------------|
| Harpe | 0.35 |
| Basse | 0.0 |
| Flûte | 0.15 |
| Percussions | 0.0 |
| Cordes | 0.45 |

## Analyses Audio

### AVANT ajustements (patches initiaux)
| Section | RMS | Centroid (Hz) | Key | Dynamic Range |
|---------|-----|---------------|-----|---------------|
| Intro | 0.065 | 828 | A minor* | 23.7 dB |
| Couplet A | 0.071 | 714 | D minor ✓ | 22.9 dB |
| Refrain | 0.075 | 767 | D minor ✓ | 22.5 dB |

### APRÈS ajustements (paramètres envoutants + Reverb)
| Section | RMS | Centroid (Hz) | Key | Dynamic Range |
|---------|-----|---------------|-----|---------------|
| Intro | 0.077 | 931 | D minor ✓ | 22.2 dB |
| Couplet A | 0.088 | 805 | G minor* | 21.1 dB |

*Détecté G minor car le Couplet A commence par Gm.

*Détecté A minor car l'intro ne contient que Dm et A7.

## Problèmes résolus
1. **Basse inaudible** → cutoff 42 Hz → 600 Hz (0.45)
2. **Drum Rack vide** → chargé 606 Core Kit
3. **Sons trop digitaux** → patches Galactic Harp→Harpie, Mellow→Fingered, Dreamy Flute→Moon Flute, Symphonic Strings→Chamber Strings
4. **CPU 162%** → polyphonie 16→3-6 voix par instance
5. **Pas d'ambiance** → Reverb via Return A + envoi Harpe (35%), Cordes (45%), Flûte (15%)
6. **Sons trop digitaux (v2)** → ajustement cutoff, attack, release pour ambiance envoutante

## TODO
- [ ] Écouter et ajuster les volumes/mix
- [x] Ajouter reverb via returns Ableton (pas Surge XT) pour l'ambiance envoutante
- [x] Créer STATUS.md avec détails complets
- [ ] Ajuster les mélodies Flûte si besoin
- [ ] Vérifier que les Percussions 606 sonnent bien avec les notes existantes
- [x] Ajuster paramètres Surge XT pour ambiance envoutante (cutoff, attack, release)
