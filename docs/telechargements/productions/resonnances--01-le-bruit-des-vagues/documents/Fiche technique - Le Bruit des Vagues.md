# Fiche Technique — 01 — Le Bruit des Vagues

**Album** : RÉSONANCES
**Tempo** : ~112 BPM (capturé, léger swing)
**Tonalité** : Ré mineur (Dm) — confirmé via analyse MCP (toutes sections)
**Durée** : ~240 temps (~2'08 à 112 BPM, sans le fade final)

## Structure (en temps, 0-based)

| Section | Début (temps) | Fin (temps) | RMS final | DR (dB) | Centroid |
|---|---|---|---|---|---|
| Intro | 0 | 32 | 0.217 | 13.3 | 1358 |
| Pré-couplet | 32 | 48 | 0.417 | 7.6 | 1193 |
| Couplet | 48 | 112 | 0.374 | 8.5 | 1521 |
| Montée | 112 | 144 | 0.367 | 8.7 | 1690 |
| Explosion | 144 | 208 | 0.467 | 6.6 | 506 |
| Outro | 208 | 240 | 0.348 | 9.2 | 891 |

## Pistes et Traitements

### 0. Pad
- Instrument : Ableton Wavetable "Glass Pad" (Sea Pad Space macro 95)
- FX : Reverb Chorus Amount 0.15, Chorus Rate 0.25, Decay 0.75
- Volume : 0.56

### 1. Orgue
- Instrument : Leslied Organ (effet Leslie 60's)
- Volume : 0.39

### 2. Voix (baryton — spoken + harmonie quinte)
- Audio clip : fichier monté "bruit des vagues c1" (48-112), "montee2" (112-143), "outro" (208-226.5)
- Focusrite Red 2 EQ : HPF ~100 Hz, HiMid +0.95, HiShelf +0.85
- Focusrite Red 3 Compressor : Threshold 0.5, Ratio ~0.3
- **Auto Shift** : Pitch +7 (quinte supérieure), Scale Aware=ON, Formant Follow=ON, Glide=0.01, Dry/Wet=0.35
  - Root=D, Scale=Minor (réglés manuellement — API ne peut pas modifier)
- Volume : 0.85

### 3. Guitare
- FX : Saturator (Soft Sine, Drive 0.15), Delay feedback 0.6, Reverb send 0.22
- Volume : 0.85

### 4. Basse
- FX : Over Tone 90, Attack 15, Distort 20, Reverb send 0.18
- Volume : 0.50

### 5. Drums Bongo
- FX : Compressor Threshold 0.3, Ratio 0.5, Reverb send 0.22
- Volume : 0.52

### 6. Vagues (Surge XT)
- Surge XT instance 1, port OSC IN=53282 OUT=53283
- Patches testés : ❌ "Pebble Beach Breaking Ocean Waves" (FX sans son propre) → ✅ **Ocean Shimmer 1**
- Clip arrangement : 256 temps, 75 notes (C4-G4, vélos 55-120, durées 3-8)
- **État : gelée (freeze)** — CPU saturait avec Surge + 75 notes
- Volume : 0.35

## Automations appliquées

### Explosion boost (+3 dB sur les 5 pistes instrumentales)
Clips `set_automation_curve` — target=volume, is_arrangement=True, courbe plate value=90 (0→64 temps)

| Piste | Clip | Notes préservées |
|---|---|---|
| Pad | Explosion Pad (index 4) | 67 notes ✅ |
| Orgue | Explosion Orgue (index 4) | intact ✅ |
| Guitare | Explosion Guitare (index 3) | intact ✅ |
| Basse | Explosion Basse (index 3) | intact ✅ |
| Drums Bongo | Explosion Drums (index 4) | 123 notes ✅ |

### Drums reduction (global, pour faire respirer le pré-couplet)
- Drums Bongo : 0.68 → 0.52 (-2.3 dB)
- Effet : pré-couplet RMS 0.461 → 0.417, DR 6.7 → 7.6

## Arc dynamique final

```
Intro 0.217 ──→ Pré-couplet 0.417 ──→ Couplet 0.374 ──→ Montée 0.367
──→ **Explosion 0.467** (PIC) ──→ Outro 0.348
```

## À faire (suggestions)

### Pré-couplet (32-48) — toujours ~0.5 dB au-dessus du couplet
Solutions pour faire respirer le pré-couplet (le passer sous le couplet en RMS) :
1. **Baisser les Drums** (0.52 → 0.42) — mais tasse aussi le couplet et l'explosion
2. **Baisser Guitare** (0.85 → 0.72) + **Orgue** (0.39 → 0.33) — le couplet tient grâce à la voix
3. **Ableton manuel** : sélectionner les clips MIDI du pré-couplet (32-48) et baisser leur gain directement dans l'arrangement — solution la plus propre
4. **Accepter** : la voix porte le couplet en perception, l'écart est minime

### Autres pistes
- Master Limiter : régler ceiling et threshold
- Vagues : si le freeze est retiré, réduire le nombre de notes (75 → ~40) pour soulager le CPU Surge
- Export prémix : bounce des 6 sections pour écoute externe

## Limitations connues
- **Pré-couplet (32-48)** : légèrement au-dessus du couplet en RMS (0.417 vs 0.374). Les clips sont trimmés (arrangement 32-48 pour un contenu de 64 temps) — l'automation via `set_automation_curve` est impossible sans perdre le trim (re-dup à pleine longueur).
- **Auto Shift** : Root/Scale en lecture seule depuis l'API Live — réglage manuel dans Ableton.
- **Arrangement envelopes** : write-once, lecture impossible. L'automation de volume via clips fonctionne à l'écriture mais ne peut pas être vérifiée par l'API.
- **CPU** : Piste Vagues (Surge XT + 75 notes) gelée.

## Captures d'analyse disponibles
`data/analyses/cap_0b.wav` `cap_32b_v2.wav` `cap_48b_v2.wav` `cap_112b.wav` `cap_144b_v3.wav` `cap_208b.wav`
