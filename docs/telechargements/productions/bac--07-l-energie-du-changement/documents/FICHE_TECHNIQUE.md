# 07 — L'Énergie du Changement

**Tempo**: 108 → 65 → 110 BPM (map BPM)
**Tonalité**: Mi mineur funky (Em) — grille `Em9 - A13 - Dmaj9 - G#m7b5` ; refrain `Am11 - D9sus4 - Gmaj13 - Cmaj9`
**Durée**: ≈ 1 min 45 (44 barres — structure proposée)
**Atmosphère**: Disco-funk psychoédélique, rythme en 16e, wah-wah, synthé bouncy
**Style**: Disco-Funk psychoédélique
**Voix**: Baryton parlé-chanté (E3 → B3, pitch 64-71), poitrine posée sur les couplets, groove léger au refrain, mixte flottante au pont

## Hommage / Inspirations

- Disco-funk : 4-on-floor + hats en 16e, slap bass FM (Ratio 1.5), wah-wah (BPF LFO 4 Hz), cuivres Unison.
- Stevie Wonder : progression `Em9 - A13 - Dmaj9 - G#m7b5`, la basse descendante E → A → D → G#.
- Psychoédélisme : nappe acide (LFO 6 Hz sur cutoff), clavinet Wavetable, break planant à 65 BPM.
- Contenu scolaire (SVT / Physique-Chimie) : effet de serre (CO₂, méthane, GES), conversion d'énergie, 1er/2e principe, homéostasie, entropie.

## Structure (en barres)

Intro (4) | Couplet 1 (8) | Refrain (8) | Couplet 2 (8) | Pont (8) | Outro funky (8) = **44 barres**

| # | Section | Barres | Éléments clés |
| :---: | :--- | :--- | :--- |
| 1 | Intro | 1-4 | Lignes de basse entraînante + groove 16e, sans voix, 108 BPM |
| 2 | Couplet 1 | 5-12 | Basse slap + wah, voix de poitrine — l'effet de serre |
| 3 | Refrain | 13-20 | Groove total, cuivres, « Énergie ! » — 1er/2e principe |
| 4 | Couplet 2 | 21-28 | Homéostasie, thermorégulation |
| 5 | Pont | 29-36 | Break planant 65 BPM, voix mixte flottante, l'acid ralentit |
| 6 | Outro funky | 37-44 | Retour du groove 110 BPM, instrumental |

> ⚠️ Structure **proposée** : le doc source ne donne pas de découpage en barres. À valider sur l'arrangement réel.

## BPM Map

| Repère | Position (beats) | Barres (4/4) | BPM | Événement |
| :--- | :--- | :--- | :--- | :--- |
| Début | 0.0 | 1 | **108** | Intro / Couplets / Refrains — groove disco |
| Pont planant | 16.0 | — | **65** | Pont — break planant, l'acid ralentit |
| Outro funky | 24.0 | — | **110** | Outro — retour du groove, plus rapide |

> ⚠️ Positions du doc (en **beats**, repères de section) ; à **re-calquer** sur la structure réelle (44 barres).

## Grille d'accords

| Section | Grille | Couleur / Sonorité |
| :--- | :--- | :--- |
| **Couplet** | `Em9 - A13 - Dmaj9 - G#m7b5` | Mi mineur funky — progression de Stevie Wonder ; basse descendante E→A→D→G#, le G#m7b5 tire vers la dominante. |
| **Refrain** | `Am11 - D9sus4 - Gmaj13 - Cmaj9` | Montée vers Do majeur lumineux ; D9sus4 = tension suspendue, Cmaj9 = résolution « Énergie ! ». |

> Vérification des accords (convention **C3 = 60**) :
> - **Em9** = E-G-B-D-F# ✓
> - **A13** = A-C#-E-G-F# ✓
> - **Dmaj9** = D-F#-A-C#-E ✓
> - **G#m7b5** = G#-B-D-F# ✓
> - **Am11** = A-C-E-G-B ✓
> - **D9sus4** = D-G-A-C-E ✓
> - **Gmaj13** = G-B-D-F#-E ✓
> - **Cmaj9** = C-E-G-B-D ✓

## Instruments (Ableton) — Mix

Template réel `bac.als` (indices **0-based**), pistes 0-6 MIDI, piste 7 Audio (Voix). Réaffectation des pistes du doc (P1-P8) sur le template : P1→0, P2→1, P3→3, P4→2, P5→4, P6→6, P7→5, P8→7.

| Piste | Index | Instrument | Pan | Vol | Chaîne FX |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Drums** | 0 | Gen Purpose Kit (rack) — Kick C1, Snare D1, Hats 16e F#1, Cymbales | 0 | 0.80 | MCompressor (colle) ✓ ; `MCharisma` (Drive 25 %) à charger |
| **Basse** | 1 | Surge XT — Slap Bass (Osc1 FM Ratio 1.5, Env A 1 ms / D 80 ms) | 0 | 0.85 | MDelay ✓ + MEqualizer (boost 800 Hz) ✓ |
| **Pads/Claviers** | 2 | Surge XT — « Electric Clav » (Wavetable) | −0.15 | 0.75 | Reverb (Ableton) + MFlanger ; `MChorus` à charger |
| **Lead/Mélodie** | 3 | Surge XT — « Wah Lead » (Filter BPF LFO 4 Hz sur Modulation) | +0.20 | 0.70 | `MPhaser` à charger ; Drum Noise Glitcher + Massive Sidechain Distort à bypasser (son wah propre) |
| **Arp/Contrepoint** | 4 | Surge XT — Acid (Osc1 Saw, LFO 6 Hz sur Cutoff) | −0.20 | 0.65 | MPhaser + MDelay (1/8) ✓ |
| **Fx** | 5 | Surge XT (MIDI — PAS audio) — Percussions latines samplées (congas, bongos) | +0.25 | 0.60 | Reverb (Ableton) + Auto Filter ✓ ; `MReverb` (Room) à charger |
| **Aux/synthé2** | 6 | Surge XT — « Brass Section » (Unison) | +0.15 | 0.70 | Chorus-Ensemble + Chorus + MCompressor ✓ |
| **Voix** | 7 | Audio | 0 | 0.90 (mix manuel) | MCompressor ✓ + De-esser ✓ ; `MDelay` (Ping-Pong 1/8T) à charger |

> Convention : effet Meldaproduction cité par le doc mais absent du template → mentionné « à charger ».

### Réglages Surge XT (du doc)

- **Basse** — Slap : Osc1 FM (Ratio 1.5), enveloppe courte (A 1 ms, D 80 ms) — attaque slap.
- **Wah Guitare** — « Wah Lead » : filtre BPF modulé par LFO à 4 Hz sur Modulation (wah-wah auto).
- **Clav** — « Electric Clav » : Wavetable, son clavinet funky.
- **Acid** — Osc1 Saw + LFO sur Cutoff à 6 Hz (nappe acide bouncy).
- **Brass** — « Brass Section » : Unison, cuivres synthétiques larges.
- **Percussions latines** : congas / bongos samplés (chaînes échantillons Surge XT ou rack Drums).
- **Fx** — pas de patch précis (percussions samplées).

## Clips JSON (motifs principaux — temps en beats)

> Légende hauteurs (convention **C3 = 60**) : 36 C1 · 38 D1 · 42 F#1 · 60 C3 · 62 D3 · 64 E3 · 66 F#3 · 67 G3 · 68 G#3 · 69 A3 · 71 B3 · 72 C4 · 73 C#4 · 74 D4 · 76 E4 · 78 F#4 · 79 G4 · 83 B4.
>
> Conversion métrique utilisée : **4/4 → 1 mesure = 4 beats**.
>
> ⚠️ **Convention de hauteurs** : le JSON du doc (wah) était écrit en **C3 = 48** (ancienne numérotation MIDI) — tous les pitch sont convertis **+12** (C3 = 60), les noms de notes restent identiques. Une correction d'accord est appliquée sur l'A13 (voir A).

### A. Wah Guitare (piste Lead/Mélodie, index 3) — motif du doc, corrigé — `Em9 - A13 - Dmaj9`

Rythme syncopé (2 accords/mesure), 2 notes par accord (fondamentale + quinte/tierce). **Corrections appliquées** :
1. **Convention C3 = 60** : tous les pitch du doc +12 (le doc était en C3 = 48).
2. **A13** : le doc donnait **75 = D#4** comme tierce → corrigé en **73 = C#4** (A13 = A-C#-E-G-F#, la 3e majeure est C#).

```json
{
  "clip_name": "C7_Wah_Rhythm",
  "bpm": 108,
  "notes": [
    { "time": 0.0, "pitch": 76, "duration": 0.25, "velocity": 90 },
    { "time": 0.0, "pitch": 83, "duration": 0.25, "velocity": 90 },
    { "time": 0.5, "pitch": 76, "duration": 0.25, "velocity": 80 },
    { "time": 0.5, "pitch": 83, "duration": 0.25, "velocity": 80 },
    { "time": 1.0, "pitch": 69, "duration": 0.25, "velocity": 90 },
    { "time": 1.0, "pitch": 73, "duration": 0.25, "velocity": 90 },
    { "time": 1.5, "pitch": 69, "duration": 0.25, "velocity": 80 },
    { "time": 1.5, "pitch": 73, "duration": 0.25, "velocity": 80 },
    { "time": 2.0, "pitch": 62, "duration": 0.25, "velocity": 85 },
    { "time": 2.0, "pitch": 66, "duration": 0.25, "velocity": 85 },
    { "time": 2.5, "pitch": 62, "duration": 0.25, "velocity": 75 },
    { "time": 2.5, "pitch": 66, "duration": 0.25, "velocity": 75 }
  ]
}
```

> Em9 : E4(76) + B4(83) = fondamentale + quinte ✓ ; A13 : A3(69) + C#4(73) = fondamentale + tierce majeure ✓ (**corrigé**) ; Dmaj9 : D3(62) + F#3(66) = fondamentale + tierce majeure ✓. Le motif du doc couvre 2 mesures sans le G#m7b5 (4e mesure) — grille complète dans le clip B.

### B. Couplet — Accords (Pads/Claviers index 2 + Aux/synthé2 index 6) — `Em9 - A13 - Dmaj9 - G#m7b5`

Grille complète construite (le doc ne fournit de JSON que pour la wah), 1 accord/mesure (4 beats), boucle 4 mesures (16 beats).

```json
{
  "clip_name": "C7_Couplet_Chords",
  "bpm": 108,
  "notes": [
    { "time": 0.0, "pitch": 64, "duration": 4.0, "velocity": 85 },
    { "time": 0.0, "pitch": 67, "duration": 4.0, "velocity": 85 },
    { "time": 0.0, "pitch": 71, "duration": 4.0, "velocity": 80 },
    { "time": 0.0, "pitch": 74, "duration": 4.0, "velocity": 75 },
    { "time": 0.0, "pitch": 78, "duration": 4.0, "velocity": 75 },
    { "time": 4.0, "pitch": 69, "duration": 4.0, "velocity": 85 },
    { "time": 4.0, "pitch": 73, "duration": 4.0, "velocity": 80 },
    { "time": 4.0, "pitch": 76, "duration": 4.0, "velocity": 80 },
    { "time": 4.0, "pitch": 78, "duration": 4.0, "velocity": 75 },
    { "time": 4.0, "pitch": 79, "duration": 4.0, "velocity": 75 },
    { "time": 8.0, "pitch": 62, "duration": 4.0, "velocity": 85 },
    { "time": 8.0, "pitch": 66, "duration": 4.0, "velocity": 80 },
    { "time": 8.0, "pitch": 69, "duration": 4.0, "velocity": 80 },
    { "time": 8.0, "pitch": 73, "duration": 4.0, "velocity": 75 },
    { "time": 8.0, "pitch": 76, "duration": 4.0, "velocity": 75 },
    { "time": 12.0, "pitch": 68, "duration": 4.0, "velocity": 85 },
    { "time": 12.0, "pitch": 71, "duration": 4.0, "velocity": 80 },
    { "time": 12.0, "pitch": 74, "duration": 4.0, "velocity": 75 },
    { "time": 12.0, "pitch": 78, "duration": 4.0, "velocity": 75 }
  ]
}
```

> Em9 = E3(64)+G3(67)+B3(71)+D4(74)+F#4(78) ✓ ; A13 = A3(69)+C#4(73)+E4(76)+F#4(78)+G4(79) ✓ ; Dmaj9 = D3(62)+F#3(66)+A3(69)+C#4(73)+E4(76) ✓ ; G#m7b5 = G#3(68)+B3(71)+D4(74)+F#4(78) ✓.

### C. Refrain — Accords (Pads/Claviers index 2 + Aux/synthé2 index 6) — `Am11 - D9sus4 - Gmaj13 - Cmaj9`

Construit (le doc fournit la grille du refrain mais pas de JSON), 1 accord/mesure, boucle 4 mesures (16 beats).

```json
{
  "clip_name": "C7_Refrain_Chords",
  "bpm": 108,
  "notes": [
    { "time": 0.0, "pitch": 69, "duration": 4.0, "velocity": 85 },
    { "time": 0.0, "pitch": 72, "duration": 4.0, "velocity": 80 },
    { "time": 0.0, "pitch": 76, "duration": 4.0, "velocity": 80 },
    { "time": 0.0, "pitch": 79, "duration": 4.0, "velocity": 75 },
    { "time": 0.0, "pitch": 83, "duration": 4.0, "velocity": 70 },
    { "time": 4.0, "pitch": 62, "duration": 4.0, "velocity": 85 },
    { "time": 4.0, "pitch": 67, "duration": 4.0, "velocity": 80 },
    { "time": 4.0, "pitch": 69, "duration": 4.0, "velocity": 80 },
    { "time": 4.0, "pitch": 72, "duration": 4.0, "velocity": 75 },
    { "time": 4.0, "pitch": 76, "duration": 4.0, "velocity": 75 },
    { "time": 8.0, "pitch": 67, "duration": 4.0, "velocity": 85 },
    { "time": 8.0, "pitch": 71, "duration": 4.0, "velocity": 80 },
    { "time": 8.0, "pitch": 74, "duration": 4.0, "velocity": 80 },
    { "time": 8.0, "pitch": 76, "duration": 4.0, "velocity": 75 },
    { "time": 8.0, "pitch": 78, "duration": 4.0, "velocity": 75 },
    { "time": 12.0, "pitch": 60, "duration": 4.0, "velocity": 85 },
    { "time": 12.0, "pitch": 64, "duration": 4.0, "velocity": 80 },
    { "time": 12.0, "pitch": 67, "duration": 4.0, "velocity": 80 },
    { "time": 12.0, "pitch": 71, "duration": 4.0, "velocity": 75 },
    { "time": 12.0, "pitch": 74, "duration": 4.0, "velocity": 75 }
  ]
}
```

> Am11 = A3(69)+C4(72)+E4(76)+G4(79)+B4(83) ✓ ; D9sus4 = D3(62)+G3(67)+A3(69)+C4(72)+E4(76) ✓ ; Gmaj13 = G3(67)+B3(71)+D4(74)+F#4(78)+E4(76) ✓ ; Cmaj9 = C3(60)+E3(64)+G3(67)+B3(71)+D4(74) ✓.

### D. Drums Disco (piste Drums, index 0) — pattern 16e

4-on-floor + backbeat + hats en 16e, construit à partir du map du doc (Kick **C1=36**, Snare **D1=38**, Hats **F#1=42**, cymbales).

```json
{
  "clip_name": "C7_Drums_Disco",
  "bpm": 108,
  "notes": [
    { "time": 0.0, "pitch": 36, "duration": 0.25, "velocity": 95 },
    { "time": 1.0, "pitch": 36, "duration": 0.25, "velocity": 90 },
    { "time": 2.0, "pitch": 36, "duration": 0.25, "velocity": 95 },
    { "time": 3.0, "pitch": 36, "duration": 0.25, "velocity": 90 },
    { "time": 1.0, "pitch": 38, "duration": 0.25, "velocity": 85 },
    { "time": 3.0, "pitch": 38, "duration": 0.25, "velocity": 85 },
    { "time": 0.0, "pitch": 42, "duration": 0.125, "velocity": 60 },
    { "time": 0.5, "pitch": 42, "duration": 0.125, "velocity": 70 },
    { "time": 1.0, "pitch": 42, "duration": 0.125, "velocity": 60 },
    { "time": 1.5, "pitch": 42, "duration": 0.125, "velocity": 70 },
    { "time": 2.0, "pitch": 42, "duration": 0.125, "velocity": 60 },
    { "time": 2.5, "pitch": 42, "duration": 0.125, "velocity": 70 },
    { "time": 3.0, "pitch": 42, "duration": 0.125, "velocity": 60 },
    { "time": 3.5, "pitch": 42, "duration": 0.125, "velocity": 80 }
  ]
}
```

## Automations (temps en beats)

| Moment | Paramètre | Points (breakpoints) | Effet |
| :--- | :--- | :--- | :--- |
| **Pont planant** | Cutoff LFO (P5 Acid, index 4) | `0.0→2 Hz`, `16.0→0.1 Hz`, `24.0→6 Hz` | L'acide ralentit au pont (0.1 Hz, nappe statique), repart à 6 Hz sur l'outro. |
| **Toute la chanson** | MCharisma Drive (P1 Drums, index 0) | `0.0→20 %`, `16.0→50 %`, `24.0→15 %` | La saturation des drums monte au pont (le désordre augmente — entropie), retombe sur l'outro. |

> ⚠️ Points du doc (positions en **beats**) ; à **re-calquer** sur la structure 44 barres. MCharisma à charger sur la piste 0 (`load_instrument_or_effect`). Les Hz/% sont des valeurs du doc — mapping à vérifier à l'oreille.

## Réglages Mix

| Piste | Vol | Pan | Notes |
| :--- | :--- | :--- | :--- |
| Drums | 0.80 | 0 | 4-on-floor, hats 16e (F#1), cymbales ; sidechain Master facultatif |
| Basse | 0.85 | 0 | Slap Osc1 FM Ratio 1.5, Env A 1 ms / D 80 ms ; MEqualizer boost 800 Hz |
| Pads/Claviers | 0.75 | −0.15 | Electric Clav Wavetable ; MChorus à charger |
| Lead/Mélodie | 0.70 | +0.20 | Wah Lead BPF LFO 4 Hz ; glitcher/distort bypassés ; MPhaser à charger |
| Arp/Contrepoint | 0.65 | −0.20 | Acid Saw + LFO 6 Hz cutoff ; MDelay 1/8 |
| Fx | 0.60 | +0.25 | Congas / bongos samplés ; MReverb Room à charger |
| Aux/synthé2 | 0.70 | +0.15 | Brass Section Unison ; Chorus-Ensemble + Chorus + MCompressor |
| Voix | 0.90 (mix manuel) | 0 | MCompressor + De-esser ; MDelay Ping-Pong 1/8T à charger |

## Notes de production

- **Correction convention C3 = 60** : le JSON du doc (wah) était écrit en **C3 = 48** → conversion **+12** (E4=76, A3=69, D3=62...), les noms de notes du doc sont conservés.
- **Correction A13** : le doc donnait **D#4 (75)** comme tierce de l'A13 → corrigé en **C#4 (73)**. A13 = A-C#-E-G-F#, la 3e majeure est le C#.
- **Grille** : couplet `Em9 - A13 - Dmaj9 - G#m7b5` (Stevie Wonder, basse descendante E→A→D→G#) ; refrain `Am11 - D9sus4 - Gmaj13 - Cmaj9`. Le JSON du doc ne couvre que la wah (Em9/A13/Dmaj9) → clips B (couplet complet) et C (refrain) construits.
- **Réaffectation doc → template** : P1 Drums→0, P2 Basse→1, P3 Wah→3, P4 Clav→2, P5 Acid→4, P6 Brass→6, P7 Percussions latines→5, P8 Voix→7.
- **Disco-funk psycho** : 4-on-floor + hats en 16e, wah-wah auto (BPF LFO 4 Hz), slap bass FM (Ratio 1.5), clav Wavetable, acid LFO 6 Hz, cuivres Unison.
- **BPM map** : 108 / 65 (pont planant) / 110 (outro funky) — positions du doc (0.0, 16.0, 24.0 beats) à re-calquer sur la structure réelle.
- **Meldaproduction absents du template** → à charger : MCharisma, MPhaser, MChorus, MReverb (Room), MDelay (Ping-Pong voix).
- **Entropie** (concept) : la saturation des drums monte au pont (20 → 50 %) — le désordre augmente, puis se réorganise sur l'outro (15 %).
- **Voix baryton** : E3-B3 (pitch 64-71), parlé-chanté, poitrine sur les couplets, groove léger au refrain, mixte flottante au pont.
- ⏳ **À valider** : adaptation de la tonalité si la mélodie (voix baryton E3-B3) sort de la tessiture.

## Intégration MCP

Indices **0-based** (0 = Drums, 1 = Basse, 2 = Pads/Claviers, 3 = Lead/Mélodie, 4 = Arp/Contrepoint, 5 = Fx, 6 = Aux/synthé2, 7 = Voix). Temps des notes en **beats**.

1. **Tempo** : `set_tempo(108)` → `set_tempo(65)` (pont) → `set_tempo(110)` (outro funky).
2. **Wah Guitare** : `create_clip(3, 0, 8)` puis `add_notes_to_clip(3, 0, notes)` avec le JSON A.
3. **Drums disco** : `create_clip(0, 0, 4)` puis `add_notes_to_clip(0, 0, notes)` avec le JSON D.
4. **Accords couplet** : `create_clip(2, 0, 16)` puis `add_notes_to_clip(2, 0, notes)` avec le JSON B ; doublé sur les cuivres `create_clip(6, 0, 16)` puis `add_notes_to_clip(6, 0, notes)`.
5. **Accords refrain** : `create_clip(2, 1, 16)` puis `add_notes_to_clip(2, 1, notes)` avec le JSON C ; doublé `create_clip(6, 1, 16)` puis `add_notes_to_clip(6, 1, notes)`.
6. **Arrangement** : `duplicate_to_arrangement(track_index, clip_index, destination_time)` — 1 barre 4/4 = 4 beats (destination_time en beats, 0-based).
7. **Automations** : `set_automation_curve(track_index, clip_index, target, points, is_arrangement=True)` avec les breakpoints ci-dessus — Cutoff LFO sur la piste 4, MCharisma Drive sur la piste 0 (en beats). Les effets Meldaproduction (MCharisma, MPhaser, MChorus, MReverb Room, MDelay) doivent d'abord être chargés (`load_instrument_or_effect` / `load_external_plugin`) — ils ne sont pas dans le template.

## Paroles
Voir `PAROLES.md` dans ce dossier.
