# 09 — L'Art de la Guerre et de la Paix

**Tempo**: 75 → 130 → 80 BPM (map par section, accélération brutale au refrain)
**Tonalité**: Si mineur (Bm)
**Durée**: ≈ 1 min 36 (36 barres — arrangement complet)
**Atmosphère**: Guerres mondiales (tranchées, génocide, Hiroshima), théâtre tragique (Racine, Molière, Ionesco), tension, chaos puis résilience
**Style**: Cinématique / Orchestral (bruitiste)
**Voix**: Baryton parlé-chanté (E3 → B3, pitch 64-71), parole scandée sur le pont

## Hommage / Inspirations
- Cinématique orchestrale : musiques de films de guerre, montées en tension, samples de champ de bataille (obus, mitrailleuses, sirènes).
- Théâtre : Racine, Molière, Ionesco, Beckett — le héros tragique comme miroir des grandes fureurs humaines.
- Clausewitz : « La guerre est la continuation de la politique par d'autres moyens » — le pont se dit sur une parole scandée.

## Structure (en barres)

Intro (4) | Couplet 1 (8) | Refrain (8) | Couplet 2 (8) | Pont (8) = **36 barres**

| # | Section | Barres | Éléments clés |
| :---: | :--- | :--- | :--- |
| 1 | Intro | 1-4 | Bruit d'obus, sirènes, puis violon solo sur nappe Bm9 |
| 2 | Couplet 1 | 5-12 | Voix parlé-chanté, accords tragiques Bm9 → E7#9, toms graves |
| 3 | Refrain | 13-20 | Accélération brutale, cuivres (Brass Ensemble), voix mixte tendue |
| 4 | Couplet 2 | 21-28 | Retour au calme progressif, plus résilient |
| 5 | Pont | 29-36 | Parole scandée (Clausewitz), accord tenu Amaj7#11 |

## BPM Map

| Repère | Barres | BPM | Événement |
| :--- | :--- | :--- | :--- |
| Intro | 1-4 | **75** | Bruit d'obus, violon solo |
| Couplet 1 | 5-12 | **75** | Narration, accords tragiques |
| Refrain | 13-20 | **130** | Saut linéaire 75→130 sur 2 mes. (barres 13-15) |
| Couplet 2 | 21-28 | **130 → 80** | Retour calme (rampe 130→80, barres 25-27) |
| Pont | 29-36 | **80** | Parole scandée, théâtral |

> ⚠️ Le doc source cale les changements de tempo aux barres 12 et 24 (0-based) — ici recalculés sur la structure 36 barres (refrain à la barre 13, retour calme à la barre 25). Rampe 75→130 : beats 48→56.

## Grille d'accords

| Section | Grille | Couleur / Sonorité |
| :--- | :--- | :--- |
| **Intro** | `Bm9` (tenu) — `E7#9` sur la 4e mesure | Nappe sombre, cordes cinématiques. |
| **Couplet 1** | `Bm9 - E7#9` (1 mesure chacun) | Chords Tragiques (JSON source), tenus. |
| **Refrain** | `Bm9 - E7#9 - G13 - F#m7b5` | Dramatique, cuivres, accélération. |
| **Couplet 2** | `Em9 - A7sus4b9 - Bm9 - B7b13` | Résilient, plus calme ; B7b13 « pantin bancal ». |
| **Pont** | `Amaj7#11 - Bm9 - Em9 - Bm9` | Lumineux-tragique, parole scandée. |

## Instruments (Ableton) — Mix

Template réel `bac.als` (indices **0-based**), pistes 0-6 MIDI, piste 7 Audio (Voix).

| Piste | Index | Instrument | Pan | Vol | Chaîne FX |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Drums** | 0 | Gen Purpose Kit (rack) — toms graves + grosse caisse | 0 | 0.85 | MCompressor (template) ; `MDistortion` (Drive 40 %) à charger |
| **Basse** | 1 | Surge XT — Orchestral Sub (Sine + Noise) | 0 | 0.80 | MDelay + MEqualizer (template) ; `MCompressor` à charger |
| **Pads/Claviers** | 2 | Surge XT — Cinematic Strings (Att 1 s) | 0 | 0.75 | Reverb (Ableton, Hall) + MFlanger ; `MReverb` (Hall, Decay automatisé) à charger |
| **Lead/Mélodie** | 3 | Surge XT — violon solo (intro) | 0 | 0.75 | Drum Noise Glitcher (rack) + Massive Sidechain Distort (rack) |
| **Arp/Contrepoint** | 4 | Surge XT — Detuned Piano (pianos désaccordés) | +0.20 | 0.70 | MPhaser + MDelay |
| **Fx** | 5 | Surge XT — Alarm Lead (Square + LFO), synthé d'urgence (MIDI — PAS audio) | −0.20 | 0.60 | Reverb (Ableton) + Auto Filter ; `MFilter` (HPF automatisé) + `MDelay` à charger |
| **Aux/synthé2** | 6 | Surge XT — Brass Ensemble (cuivres synthétiques) | 0 | 0.75 | Chorus-Ensemble + Chorus + MCompressor ; `MCharisma` (Tube) à charger |
| **Voix** | 7 | Audio (voix baryton + samples de champ de bataille) | 0 | 0.90 (mix manuel) | MCompressor (Ratio 5:1) + De-esser ; `MDeEsser`, `MFilter` (EQ voix radio) à charger |

> Convention : effet Meldaproduction cité par le doc mais absent du template → mentionné « à charger ».

### Réglages Surge XT (du doc)
- **Drums (rack)** — Toms graves et grosses caisses ; MDistortion Drive 40 %.
- **Basse** — Osc « Orchestral Sub » (Sine + Noise). Env lente, sub présent.
- **Cordes** — « Cinematic Strings », Env A:1 s. MReverb Hall.
- **Cuivres** — « Brass Ensemble », MCharisma Tube.
- **Piano désaccordé** — « Detuned Piano », MPhaser.
- **Synthé d'urgence** — « Alarm Lead » (Square + LFO), MDelay.

## Clips JSON (motifs principaux — temps en beats)

> Légende hauteurs (convention **C3 = 60**) : 47 B1 · 50 D2 · 52 E2 · 54 F#2 · 56 G#2 · 57 A2 · 59 B2 · 61 C#3 · 62 D3 · 64 E3 · 67 G3 · 71 B3.

### A. Couplet — Chords Tragiques (Cordes index 2, doublés Cuivres index 6) — `Bm9 - E7#9`
Motif de 2 mesures (8 beats), accords tenus 1 mesure chacun. **Corrections appliquées : Bm9 complété (ajout de la 7e A2 = 57 et de la 9e C#3 = 61) ; E7#9 complété (ajout de la 7e bémol D3 = 62).** Répéter ×4 (offsets +8 / +16 / +24 beats) pour un couplet complet de 8 mesures.

```json
{
  "clip_name": "C9_Chords_Tragiques",
  "bpm": 75,
  "notes": [
    { "time": 0.0, "pitch": 47, "duration": 4.0, "velocity": 90 },
    { "time": 0.0, "pitch": 50, "duration": 4.0, "velocity": 85 },
    { "time": 0.0, "pitch": 54, "duration": 4.0, "velocity": 90 },
    { "time": 0.0, "pitch": 57, "duration": 4.0, "velocity": 80 },
    { "time": 0.0, "pitch": 59, "duration": 4.0, "velocity": 85 },
    { "time": 0.0, "pitch": 61, "duration": 4.0, "velocity": 80 },
    { "time": 0.0, "pitch": 62, "duration": 4.0, "velocity": 80 },
    { "time": 4.0, "pitch": 52, "duration": 4.0, "velocity": 95 },
    { "time": 4.0, "pitch": 56, "duration": 4.0, "velocity": 90 },
    { "time": 4.0, "pitch": 59, "duration": 4.0, "velocity": 95 },
    { "time": 4.0, "pitch": 62, "duration": 4.0, "velocity": 85 },
    { "time": 4.0, "pitch": 64, "duration": 4.0, "velocity": 85 },
    { "time": 4.0, "pitch": 67, "duration": 4.0, "velocity": 85 },
    { "time": 4.0, "pitch": 71, "duration": 4.0, "velocity": 80 }
  ]
}
```
> Notes ajoutées en correction : `57` (A2, 7e de Bm9), `61` (C#3, 9e de Bm9) au temps 0.0 ; `62` (D3, b7 de E7#9) au temps 4.0. Les autres notes sont conservées du doc source.

## Automations (temps en beats)

| Moment | Paramètre | Points (breakpoints) | Effet |
| :--- | :--- | :--- | :--- |
| **Intro → Refrain → Pont** | Cordes — `MReverb` Decay (à charger) | `0→1.5 s`, `48→4 s`, `80→8 s`, `96→2 s` | L'espace s'élargit sur le refrain, sommet au pont, retour au calme. |
| **Toute la chanson** | Fx — `MFilter` HPF | automatisé sur les sections de guerre | Balayage « sirène / mitrailleuse ». |
| **Barres 13-15** | Tempo | 75 → 130 (linéaire, beats 48→56) | Accélération brutale. |
| **Barres 25-27** | Tempo | 130 → 80 (beats 96→104) | Retour au calme. |

> ⚠️ Le doc source donne les points de Reverb Decay en barres (0.0/12.0/20.0/24.0) — ici convertis en beats (×4).

## Réglages Mix

| Piste | Vol | Pan | Notes |
| :--- | :--- | :--- | :--- |
| Drums | 0.85 | — | MDistortion Drive 40 % pour la grosse caisse |
| Basse | 0.80 | — | Orchestral Sub ; MCompressor |
| Pads/Claviers | 0.75 | — | Cinematic Strings, MReverb Decay automatisé |
| Lead/Mélodie | 0.75 | — | Violon solo en intro |
| Arp/Contrepoint | 0.70 | +0.20 | MPhaser sur le piano désaccordé |
| Fx | 0.60 | −0.20 | MIDI (Surge XT) ; MFilter HPF |
| Aux/synthé2 | 0.75 | — | Brass Ensemble + MCharisma Tube |
| Voix | 0.90 (mix manuel) | — | MCompressor Ratio 5:1, De-esser, EQ voix radio |

## Notes de production

- **Correction Bm9** : le bloc source donnait B-D-F#-B-D (fondamentale/3e/5e, doublées) sans 7e ni 9e → ajout de A2 = 57 (7e) et C#3 = 61 (9e) pour obtenir **B-D-F#-A-C# = Bm9 complet**.
- **Correction E7#9** : le bloc source donnait E-G#-B-E-G-B sans la 7e bémol → ajout de D3 = 62 pour **E-G#-B-D-G = E7#9 complet** (le #9 = F## = G3, pitch 67, était déjà présent).
- **Chords Tragiques** : motif de couplet (P3 Cordes = index 2, doublé P4 Cuivres = index 6), accords tenus 1 mesure chacun.
- **Piste Fx en MIDI** (Surge XT, PAS audio) : le synthé d'urgence (Alarm Lead) s'y trouve ; les samples de champ de bataille (mitrailleuses, sirènes, discours) seront placés sur la piste **Voix** (index 7, audio) — via `create_audio_clip` ou import manuel.
- **Tempo** : saut linéaire 75→130 sur 2 mesures (barres 13-15), retour 80 (barres 25-27). À recaler finement à l'oreille.
- **Meldaproduction absents du template** → à charger : MDistortion, MReverb, MCharisma, MFilter, MDelay, MDeEsser.
- **Cuivres** : Brass Ensemble + MCharisma (Tube) sur Aux/synthé2 (index 6), doublent les accords tragiques du refrain.
- ⏳ **À valider** : adaptation de la tonalité si la mélodie (voix baryton E3-B3) sort de la tessiture.

## Intégration MCP

Indices **0-based** (0 = Drums, 1 = Basse, 2 = Pads/Claviers, 3 = Lead/Mélodie, 4 = Arp/Contrepoint, 5 = Fx, 6 = Aux/synthé2, 7 = Voix). Temps des notes en **beats**.

1. **Tempo** : `set_tempo(75)` (intro, couplet 1) → `set_tempo(130)` (refrain) → `set_tempo(80)` (couplet 2, pont). Les rampes linéaires sont à recréer manuellement.
2. **Intro** : `create_clip(2, 0, 16)` (nappe cordes Bm9) et `create_clip(3, 0, 16)` (violon solo).
3. **Couplet 1** : `create_clip(2, 1, 8)` puis `add_notes_to_clip(2, 1, notes)` avec le JSON Chords Tragiques (Bm9 → E7#9, corrigé) ; drums sur `create_clip(0, 0, 32)`.
4. **Refrain** : `create_clip(6, 0, 32)` (cuivres) + `add_notes_to_clip(6, 0, notes)` (doublure des accords) ; pads sur `create_clip(2, 2, 32)`.
5. **Couplet 2** : basse orchestrale `create_clip(1, 0, 32)` + `add_notes_to_clip(1, 0, notes)` ; pads sur `create_clip(2, 3, 32)`.
6. **Pont** : `create_clip(2, 4, 32)` (accord tenu Amaj7#11) ; parole scandée enregistrée sur la piste 7.
7. **Samples de champ de bataille** : placés sur la piste Voix (index 7, audio) aux positions des sections de guerre.

## Paroles
Voir `PAROLES.md` dans ce dossier.
