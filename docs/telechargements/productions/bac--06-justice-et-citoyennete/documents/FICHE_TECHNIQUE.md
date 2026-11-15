# 06 — Justice et Citoyenneté

**Tempo**: 62 → 92 → 65 → 95 BPM (map BPM)
**Tonalité**: Do majeur lumineux (C) — grille `Cmaj9 - Dm11 - Em9 - Fmaj7#11` ; refrain `G13sus4 - Cmaj9 - Am11 - D7b9(b13)`
**Durée**: ≈ 2 min 10 (42 barres — structure proposée)
**Atmosphère**: Gospel symphonique, orgue d'église solennel, chœurs puissants
**Style**: Gospel symphonique
**Voix**: Baryton parlé-chanté (E3 → B3, pitch 64-71), poitrine posée sur les couplets, chœur puissant sur le refrain, a cappella au pont

## Hommage / Inspirations

- Gospel et orgue d'église : Hammond B3 (Surge XT, overdrive léger), chœurs (Vocal Pad Unison 4).
- Ambiance cathédrale : `MReverb` (Cathedral) sur les cordes — la réverb s'ouvre et se referme avec la structure.
- Discours politiques samplés : Mandela, Churchill (FX / samples) — l'Histoire dans le mix.

## Structure (en barres)

Intro (2) | Couplet 1 (8) | Refrain (8) | Couplet 2 (8) | Pont (8) | Final (8) = **42 barres**

| # | Section | Barres | Éléments clés |
| :---: | :--- | :--- | :--- |
| 1 | Intro | 1-2 | Orgue solennel, sans batterie — la cathédrale s'ouvre |
| 2 | Couplet 1 | 3-10 | Orgue + basse, voix de poitrine posée, 62 BPM — Hobbes, Rousseau |
| 3 | Refrain | 11-18 | Chœur puissant, 92 BPM, sidechain du kick — « Justice ! » |
| 4 | Couplet 2 | 19-26 | Suite narrative (CECA, Maastricht), 92 BPM |
| 5 | Pont | 27-34 | A cappella puis montée, 65 BPM, réverb qui s'élargit |
| 6 | Final | 35-42 | Refrain final, 95 BPM, réverb qui se resserre |

> ⚠️ Structure **proposée** : le doc source ne donne pas de découpage en barres. À valider sur l'arrangement réel.

## BPM Map

| Repère | Position (beats) | Barres (4/4) | BPM | Événement |
| :--- | :--- | :--- | :--- | :--- |
| Début | 0.0 | 1 | **62** | Intro / Couplet 1 — orgue solennel |
| Refrain gospel | 8.0 | — | **92** | Refrain, chœur puissant |
| Pont | 24.0 | — | **65** | Pont a cappella puis montée |
| Final | 32.0 | — | **95** | Final — refrain gospel |

> ⚠️ Positions du doc (en **beats**, repères de section) ; à **re-calquer** sur la structure réelle (42 barres).

## Grille d'accords

| Section | Grille | Couleur / Sonorité |
| :--- | :--- | :--- |
| **Couplet** | `Cmaj9 - Dm11 - Em9 - Fmaj7#11` | Do majeur lumineux ; basse ascendante C-D-E-F (marche gospel). |
| **Refrain / Final** | `G13sus4 - Cmaj9 - Am11 - D7b9(b13)` | Tension dominante (D7b9b13 = V altéré de G), chœur puissant. |

> Vérification des accords (convention **C3 = 60**) :
> - **Cmaj9** = C-E-G-B-D ✓
> - **Dm11** = D-F-A-C-G ✓ (**corrigé** — voir Clips JSON A)
> - **Em9** = E-G-B-D-F# ✓
> - **Fmaj7#11** = F-A-C-E-B ✓ (**corrigé** — voir Clips JSON A)
> - **G13sus4** = G-C-D-F-A ✓
> - **Am11** = A-C-E-G-B ✓
> - **D7b9(b13)** = D-F#-A-C-Eb-Bb ✓

## Instruments (Ableton) — Mix

Template réel `bac.als` (indices **0-based**), pistes 0-6 MIDI, piste 7 Audio (Voix). Réaffectation des pistes du doc (P1-P8) sur le template : P1→0, P2→1, P3→2, P4→3, P5→4, P6→5, P7→6, P8→7.

| Piste | Index | Instrument | Pan | Vol | Chaîne FX |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Drums** | 0 | Gen Purpose Kit (rack) — Kick/Snare/Hats, sidechain sur Master | 0 | 0.80 | MCompressor (colle) ✓ ; `MCharisma` à charger |
| **Basse** | 1 | Surge XT — « Synth Bass » (Osc1 Saw, LPF 60 %) | 0 | 0.85 | MDelay + MEqualizer |
| **Pads/Claviers** | 2 | Surge XT — « Hammond B3 » (overdrive léger) | −0.20 | 0.75 | Reverb (Ableton) + MFlanger ; `MChorus` à charger |
| **Lead/Mélodie** | 3 | Surge XT — « String Ensemble » (attaque 500 ms) | +0.20 | 0.70 | Drum Noise Glitcher + Massive Sidechain Distort (à bypasser pour un pad cordes) ; `MReverb` (Cathedral) à charger |
| **Arp/Contrepoint** | 4 | Surge XT — « Vocal Pad » (Unison 4) | −0.30 | 0.65 | MPhaser + MDelay ; `MFlanger` à charger |
| **Fx** | 5 | Surge XT (MIDI — PAS audio) — discours Mandela/Churchill (samples) | 0 | 0.60 | Reverb (Ableton) + Auto Filter ; `MFilter` (HPF) à charger |
| **Aux/synthé2** | 6 | Surge XT — « Grand Piano » (FM) | +0.30 | 0.75 | Chorus-Ensemble + Chorus + MCompressor ✓ |
| **Voix** | 7 | Audio | 0 | 0.90 (mix manuel) | MCompressor (Ratio 3:1) + De-esser ✓ |

> Convention : effet Meldaproduction cité par le doc mais absent du template → mentionné « à charger ».

### Réglages Surge XT (du doc)

- **Basse** — « Synth Bass » : Osc1 Saw, LPF 60 %, basse ronde gospel.
- **Orgue** — « B3 » : drawbars, overdrive léger, son d'orgue d'église.
- **Cordes** — « String Ensemble » : attaque 500 ms (montée lente, nappe).
- **Chœur** — « Vocal Pad » : Unison 4, chœur large.
- **Piano** — « Grand Piano » : FM, piano acoustique lumineux.
- **Fx** — pas de patch : discours Mandela / Churchill (samples audio).

## Clips JSON (motifs principaux — temps en beats)

> Légende hauteurs (convention **C3 = 60**) : 60 C3 · 62 D3 · 64 E3 · 65 F3 · 66 F#3 · 67 G3 · 69 A3 · 70 Bb3 · 71 B3 · 72 C4 · 74 D4 · 76 E4 · 77 F4 · 78 F#4 · 79 G4 · 81 A4 · 82 Bb4 · 83 B4 · 84 C5 · 86 D5 · 87 Eb5.
>
> Conversion métrique utilisée : **4/4 → 1 mesure = 4 beats**. Chaque accord = 2 beats.

### A. Couplet — Accords (Piste Pads/Claviers, index 2 + Aux/synthé2, index 6) — `Cmaj9 - Dm11 - Em9 - Fmaj7#11`

Boucle de 2 mesures (8 beats), 2 beats par accord. **Corrections appliquées** :
1. **Dm11** : le doc donnait D3-F3-A3-C4-E4 (62-65-69-72-76) = un Dm9 (la 9e E à la place de la 11e G) → corrigé en **D-F-A-C-G** (62-65-69-72-**79**, G4 = 11e).
2. **Fmaj7#11** : le doc donnait 65-69-72-76-**80**-83 ; **80 = G#4** n'appartient pas à Fmaj7#11 (le #11 = B est déjà en 83) → retiré : **F3-A3-C4-E4-B4** (65-69-72-76-83).

```json
{
  "clip_name": "C6_Gospel_Chords",
  "bpm": 62,
  "notes": [
    { "time": 0.0, "pitch": 60, "duration": 2.0, "velocity": 85 },
    { "time": 0.0, "pitch": 64, "duration": 2.0, "velocity": 85 },
    { "time": 0.0, "pitch": 67, "duration": 2.0, "velocity": 80 },
    { "time": 0.0, "pitch": 71, "duration": 2.0, "velocity": 80 },
    { "time": 0.0, "pitch": 74, "duration": 2.0, "velocity": 75 },
    { "time": 2.0, "pitch": 62, "duration": 2.0, "velocity": 85 },
    { "time": 2.0, "pitch": 65, "duration": 2.0, "velocity": 85 },
    { "time": 2.0, "pitch": 69, "duration": 2.0, "velocity": 80 },
    { "time": 2.0, "pitch": 72, "duration": 2.0, "velocity": 80 },
    { "time": 2.0, "pitch": 79, "duration": 2.0, "velocity": 75 },
    { "time": 4.0, "pitch": 64, "duration": 2.0, "velocity": 85 },
    { "time": 4.0, "pitch": 67, "duration": 2.0, "velocity": 85 },
    { "time": 4.0, "pitch": 71, "duration": 2.0, "velocity": 80 },
    { "time": 4.0, "pitch": 74, "duration": 2.0, "velocity": 80 },
    { "time": 4.0, "pitch": 78, "duration": 2.0, "velocity": 75 },
    { "time": 6.0, "pitch": 65, "duration": 2.0, "velocity": 85 },
    { "time": 6.0, "pitch": 69, "duration": 2.0, "velocity": 85 },
    { "time": 6.0, "pitch": 72, "duration": 2.0, "velocity": 80 },
    { "time": 6.0, "pitch": 76, "duration": 2.0, "velocity": 80 },
    { "time": 6.0, "pitch": 83, "duration": 2.0, "velocity": 70 }
  ]
}
```

> Cmaj9 = C3(60)+E3(64)+G3(67)+B3(71)+D4(74) ✓ ; Dm11 = D3(62)+F3(65)+A3(69)+C4(72)+G4(79) ✓ ; Em9 = E3(64)+G3(67)+B3(71)+D4(74)+F#4(78) ✓ ; Fmaj7#11 = F3(65)+A3(69)+C4(72)+E4(76)+B4(83) ✓.

### B. Refrain — Accords (Piste Pads/Claviers, index 2 + Aux/synthé2, index 6) — `G13sus4 - Cmaj9 - Am11 - D7b9(b13)`

Boucle de 2 mesures (8 beats), 2 beats par accord. **Ajout proposé** : le doc fournit la grille du refrain mais pas de JSON — clip construit pour l'implémenter.

```json
{
  "clip_name": "C6_Refrain_Chords",
  "bpm": 92,
  "notes": [
    { "time": 0.0, "pitch": 67, "duration": 2.0, "velocity": 85 },
    { "time": 0.0, "pitch": 72, "duration": 2.0, "velocity": 80 },
    { "time": 0.0, "pitch": 74, "duration": 2.0, "velocity": 80 },
    { "time": 0.0, "pitch": 77, "duration": 2.0, "velocity": 75 },
    { "time": 0.0, "pitch": 81, "duration": 2.0, "velocity": 70 },
    { "time": 2.0, "pitch": 72, "duration": 2.0, "velocity": 85 },
    { "time": 2.0, "pitch": 76, "duration": 2.0, "velocity": 80 },
    { "time": 2.0, "pitch": 79, "duration": 2.0, "velocity": 80 },
    { "time": 2.0, "pitch": 83, "duration": 2.0, "velocity": 75 },
    { "time": 2.0, "pitch": 86, "duration": 2.0, "velocity": 70 },
    { "time": 4.0, "pitch": 69, "duration": 2.0, "velocity": 85 },
    { "time": 4.0, "pitch": 72, "duration": 2.0, "velocity": 80 },
    { "time": 4.0, "pitch": 76, "duration": 2.0, "velocity": 80 },
    { "time": 4.0, "pitch": 79, "duration": 2.0, "velocity": 75 },
    { "time": 4.0, "pitch": 83, "duration": 2.0, "velocity": 70 },
    { "time": 6.0, "pitch": 74, "duration": 2.0, "velocity": 85 },
    { "time": 6.0, "pitch": 78, "duration": 2.0, "velocity": 75 },
    { "time": 6.0, "pitch": 81, "duration": 2.0, "velocity": 75 },
    { "time": 6.0, "pitch": 82, "duration": 2.0, "velocity": 70 },
    { "time": 6.0, "pitch": 84, "duration": 2.0, "velocity": 70 },
    { "time": 6.0, "pitch": 87, "duration": 2.0, "velocity": 65 }
  ]
}
```

> G13sus4 = G3(67)+C4(72)+D4(74)+F4(77)+A4(81) ✓ ; Cmaj9 = C4(72)+E4(76)+G4(79)+B4(83)+D5(86) ✓ ; Am11 = A3(69)+C4(72)+E4(76)+G4(79)+B4(83) ✓ ; D7b9(b13) = D4(74)+F#4(78)+A4(81)+Bb4(82)+C5(84)+Eb5(87) ✓.

## Automations (temps en beats)

| Moment | Paramètre | Points (breakpoints) | Effet |
| :--- | :--- | :--- | :--- |
| **Refrain gospel** | Master — MCompressor (sidechain sur le Kick) | Ratio 4:1, Threshold −18 dB, Release 200 ms | Basse/pads « pompent » sur le kick — énergie gospel. |
| **Toute la chanson** | MReverb — Decay (P4 Cordes, index 3) | `0.0→2 s`, `8.0→4.5 s`, `24.0→6 s`, `32.0→3 s` | La cathédrale s'ouvre au refrain (4.5 s), s'élargit au pont (6 s), se resserre au final (3 s). |

> ⚠️ Points du doc (positions en **beats**) ; à **re-calquer** sur la structure 42 barres. MReverb Cathedral à charger sur la piste 3 (`load_instrument_or_effect`). Les pourcentages/DB sont des valeurs du doc — mapping à vérifier à l'oreille.

## Réglages Mix

| Piste | Vol | Pan | Notes |
| :--- | :--- | :--- | :--- |
| Drums | 0.80 | 0 | Kick/Snare/Hats ; sidechain Master (MCompressor 4:1, −18 dB, 200 ms) |
| Basse | 0.85 | 0 | Synth Bass Osc1 Saw, LPF 60 % |
| Pads/Claviers | 0.75 | −0.20 | Hammond B3 overdrive léger ; MChorus à charger |
| Lead/Mélodie | 0.70 | +0.20 | String Ensemble attaque 500 ms ; glitcher/distort bypassés ; MReverb Cathedral à charger |
| Arp/Contrepoint | 0.65 | −0.30 | Vocal Pad Unison 4 ; MFlanger à charger |
| Fx | 0.60 | 0 | Discours Mandela/Churchill ; MFilter HPF à charger |
| Aux/synthé2 | 0.75 | +0.30 | Grand Piano FM ; Chorus-Ensemble + Chorus + MCompressor |
| Voix | 0.90 (mix manuel) | 0 | MCompressor Ratio 3:1 + De-esser |

## Notes de production

- **Correction Dm11 (doc)** : l'accord fourni était D3-F3-A3-C4-E4 (62-65-69-72-76) = un Dm9 (la 9e E à la place de la 11e G). Corrigé → D3(62)+F3(65)+A3(69)+C4(72)+G4(79) = **Dm11** complet (D-F-A-C-G).
- **Correction Fmaj7#11 (doc)** : l'accord fourni incluait 80 = G#4, hors de Fmaj7#11 (le #11 est le B, déjà en 83). Corrigé → F3(65)+A3(69)+C4(72)+E4(76)+B4(83) = **F-A-C-E-B**.
- **Refrain** : le doc fournit la grille mais pas de JSON → clip B construit (boucle 2 mesures, 2 beats/accord), sommet du piano en D5/Eb5 pour le « lift » gospel.
- **Réaffectation doc → template** : P1 Drums → 0, P2 Basse → 1, P3 Orgue → 2, P4 Cordes → 3, P5 Chœur → 4, P6 FX → 5, P7 Piano → 6, P8 Voix → 7.
- **Fx en MIDI (Surge XT)** : la piste Fx (5) est MIDI — les discours Mandela/Churchill sont des samples audio à charger en échantillon Surge XT sur la piste 5, ou en clips audio sur la piste Voix (7). À arbitrer.
- **Meldaproduction absents du template** → à charger : MCharisma, MChorus, MReverb (Cathedral), MFlanger, MFilter.
- **BPM map** : 62 / 92 / 65 / 95 — positions du doc (0.0, 8.0, 24.0, 32.0 beats) à re-calquer sur la structure réelle.
- **Sidechain Master** : MCompressor Ratio 4:1, Threshold −18 dB, Release 200 ms, activé sur le Kick.
- **Voix baryton** : E3-B3 (pitch 64-71), poitrine posée sur les couplets, chœur puissant sur les refrains, a cappella au pont.
- ⏳ **À valider** : adaptation de la tonalité si la mélodie (voix baryton E3-B3) sort de la tessiture.

## Intégration MCP

Indices **0-based** (0 = Drums, 1 = Basse, 2 = Pads/Claviers, 3 = Lead/Mélodie, 4 = Arp/Contrepoint, 5 = Fx, 6 = Aux/synthé2, 7 = Voix). Temps des notes en **beats**.

1. **Tempo** : `set_tempo(62)` (intro/couplet 1) → `set_tempo(92)` (refrain) → `set_tempo(65)` (pont) → `set_tempo(95)` (final).
2. **Accords couplet** : `create_clip(2, 0, 8)` puis `add_notes_to_clip(2, 0, notes)` avec le JSON A (Orgue, Pads/Claviers). Même clip sur le Piano : `create_clip(6, 0, 8)` puis `add_notes_to_clip(6, 0, notes)` (Aux/synthé2).
3. **Accords refrain** : `create_clip(2, 1, 8)` puis `add_notes_to_clip(2, 1, notes)` avec le JSON B ; doublé `create_clip(6, 1, 8)` puis `add_notes_to_clip(6, 1, notes)`.
4. **Discours** : samples Mandela/Churchill via `create_audio_clip(7, 0, "chemin/vers/mandela.wav")` (piste Voix, audio), ou en échantillon Surge XT sur la piste Fx (5).
5. **Arrangement** : `duplicate_to_arrangement(track_index, clip_index, destination_time)` — 1 barre 4/4 = 4 beats (destination_time en beats, 0-based).
6. **Automations** : `set_automation_curve(track_index, clip_index, target, points, is_arrangement=True)` avec les breakpoints ci-dessus (MReverb Decay sur la piste 3, sidechain MCompressor sur le Master — en beats). Les effets Meldaproduction (MReverb, MChorus, MFlanger, MFilter, MCharisma) doivent d'abord être chargés (`load_instrument_or_effect` / `load_external_plugin`) — ils ne sont pas dans le template.

## Paroles
Voir `PAROLES.md` dans ce dossier.
