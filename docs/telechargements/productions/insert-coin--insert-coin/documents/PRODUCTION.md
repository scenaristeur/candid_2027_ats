# Production — Insert Coin

## Session Info

| Paramètre | Valeur |
|---|---|
| Tempo | 128 BPM |
| Signature | 4/4 |
| Tonalité | Do mineur (C minor) |
| Structure | Intro(4) → Verse(8) → Chorus(8) → Verse(8) → Chorus(8) → Break(4) → Chorus(8) → Outro(4) |
| Durée | 52 mesures (208 temps) |
| Loop | 0 — 208 |

## Pistes

### Track 0 — Drums
**Instrument :** 808 Core Kit (Drum Rack)
**FX :** Compressor (Ratio 4:1, Attack ~10ms, Makeup on)
**Session Clips :**
- clip 0 « Drums Main » (16b) : kick 2/4, snare/clap 2&4, CHH 8th, rim 16th offbeats, OHH offbeat
- clip 1 « Drums Intro » (32b) : kick every 2 beats + CHH 8th notes seulement
- clip 2 « Drums Verse » (32b) : kick every 4 beats (1&3), snare/clap 2&4, CHH 8th, moins dense
- clip 3 « Drums Outro » (16b) : kick every 4 beats, CHH quarters, rim offbeat 8ths, half-time feel
- clip 4 « Drums Max » (32b) : kick every 2 beats + extra offbeats, snare+clap 2&4, rim 16th offbeats, CHH 8th, OHH fréquent

### Track 1 — Bass
**Instrument :** Basic Saturated Bass
**FX :** Saturator (Analog Clip, Drive 0.6)
**Session Clips :**
- clip 0 « Bass Main » (32b) : groove C2-G1-Ab1-Bb1-C3 en C minor
- clip 1 « Bass Verse » (32b) : pattern simplifié C2→G1→Ab1, répété tous les 4 temps
- clip 2 « Bass Max » (32b) : plus intense, C3 accents, plus de notes

### Track 2 — Lead
**Instrument :** Game Console (Drift)
**FX :** Reverb (Dry/Wet 25%, Decay ~2s)
**Session Clips :**
- clip 0 « Lead Main » (32b) : mélodie arcade 8th notes en C minor
- clip 1 « Lead Max » (32b) : octave doublings, plus aigu, climax final

### Track 3 — Arp
**Instrument :** Light Electro
**Session Clips :**
- clip 0 « Arp Main » (32b) : arpège Cm en 8th/16th notes
- clip 1 « Arp Max » (32b) : arpège 16th notes en Cm, registre plus haut (G5→G6)

### Track 4 — FX
**Instrument :** Riser Arcade
**Clip :** Riser FX (16b) : C3 held aux beats 12→16, 4 beats de riser

### Track 5 — Chord Rave Pad
**Instrument :** Chord Rave Pad
**Clip :** Pad Main (32b) : C3-Eb3-G3 sustained sustain

## Volumes

| Track | Volume |
|---|---|
| Drums | 0.85 |
| Bass | 0.75 |
| Lead | 0.70 |
| Arp | 0.60 |
| FX | 0.85 |
| Pad | 0.85 |
| Master | 0.85 |

## Arrangement

```
Beats:  0    16          48    64    80         112   128   144   160         192   208
       |Intro| Verse 1   | Chorus 1  | Verse 2   | Chorus 2  |Break| Chorus 3   |Outro|
Drums  |Intro| Verse     |Main|Main  | Verse     |Main|Main  |Intro| Max        |Outro|
Bass   |     | Verse     | Main      | Verse     | Main      |     | Max        |Main→|
Lead   |     |           | Main      |           | Main      |     | Max        |Main→|
Arp    |     |           | Main      |           | Main      |     | Max        |     |
FX     |     | Riser     |           | Riser     |           |Riser|            |     |
Pad    |     | Pad Main  | Pad Main  | Pad Main  | Pad Main  |     | Pad Main   |Pad→ |
```

## Notes

- Tout est dans l'arrangement (pas de session clips firing)
- Sauvegarder manuellement (Ctrl+S) — API Live non disponible
- FX riser (Riser Arcade) : C3 sustained aux beats 12→16 du clip 16b, placé 4 beats avant chaque chorus
- Le pad n'est pas présent sur Intro (0-16) ni Break (144-160) pour contraste
- Bass et Lead continuent sur Outro ; Arp s'arrête après Chorus 3
