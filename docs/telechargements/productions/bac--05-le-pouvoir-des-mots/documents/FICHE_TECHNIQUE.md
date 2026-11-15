# 05 — Le Pouvoir des Mots

**Tempo**: 85 BPM (constant) — rubatos vocaux via `MTime` (Meldaproduction)
**Tonalité**: Fa mineur blues (F) — grille `Fm9 - Bb13 - Ebmaj9 - Abmaj7` ; pont `Dbm9 - Gb13 - Bmaj7 - E6` (modulation montante de quarte)
**Durée**: ≈ 2 min 50 (60 barres — arrangement proposé)
**Atmosphère**: Trip-hop sombre, nappe organique, scratches, voix parlée-chantée
**Style**: Trip-Hop / Slam
**Voix**: Baryton parlé-chanté (E3 → B3, pitch 64-71), rythmique parlée sur couplets, spoken word sur le pont

## Hommage / Inspirations

- Massive Attack / Portishead : breaks lo-fi, basse sub 808, atmosphère sombre.
- Slam / spoken word : la voix du slameur porte le texte, les mots claquent sur les temps.

## Structure (en barres)

Intro (4) | Couplet 1 (16) | Refrain 1 (8) | Couplet 2 (12) | Pont (8) | Refrain 2 (8) | Outro (4) = **60 barres**

| # | Section | Barres | Éléments clés |
| :---: | :--- | :--- | :--- |
| 1 | Intro | 1-4 | Sample « Le langage est la maison de l'être » (Heidegger), nappe organique Fm9, naissance des scratches |
| 2 | Couplet 1 | 5-20 | Rythmique parlée, breaks lo-fi, basse 808 sub, grille Fm9-Bb13-Ebmaj9-Abmaj7 |
| 3 | Refrain 1 | 21-28 | Chanté, plus mélodique — la voix se pose sur la nappe |
| 4 | Couplet 2 | 29-40 | Plus lent, grave — Bergson, l'outil qui asservit |
| 5 | Pont | 41-48 | Spoken word sur nappe dissonante `Dbm9 - Gb13 - Bmaj7 - E6`, citation de Buffon |
| 6 | Refrain 2 | 49-56 | Retour chanté, plus intense |
| 7 | Outro | 57-60 | Scratches + voix, fondu |

> ⚠️ Structure **proposée** : le doc source ne donne pas de découpage en barres. À valider sur l'arrangement réel.

## BPM Map

| Repère | Position (beats) | Barres (4/4) | BPM | Événement |
| :--- | :--- | :--- | :--- | :--- |
| Début | 0.0 | 1 | **85** | Toute la chanson — BPM constant |

> Les rubatos sur la voix ne changent pas le BPM global : ils sont gérés par `MTime` (Meldaproduction) sur la piste Voix.

## Grille d'accords

| Section | Grille | Couleur / Sonorité |
| :--- | :--- | :--- |
| **Couplet / Refrain** | `Fm9 - Bb13 - Ebmaj9 - Abmaj7` | Fa mineur blues, nappe organique trip-hop sombre. |
| **Pont** | `Dbm9 - Gb13 - Bmaj7 - E6` | Modulation montante de quarte, nappe dissonante. |

> Vérification des accords (convention **C3 = 60**) :
> - **Fm9** = F-Ab-C-Eb-G ✓
> - **Bb13** = Bb-D-F-Ab-G → **corrigé** (voir Clips JSON A)
> - **Ebmaj9** = Eb-G-Bb-D-F ✓
> - **Abmaj7** = Ab-C-Eb-G ✓
> - **Dbm9** = Db-Fb-Ab-Cb-Eb = Db-E-Ab-B-Eb ✓
> - **Gb13** = Gb-Bb-Db-Fb-Eb = Gb-Bb-Db-E-Eb ✓
> - **Bmaj7** = B-D#-F#-A# ✓
> - **E6** = E-G#-B-C# ✓

## Instruments (Ableton) — Mix

Template réel `bac.als` (indices **0-based**), pistes 0-6 MIDI, piste 7 Audio (Voix). Réaffectation des pistes du doc (P1-P8) sur le template : P1→0, P2→1, P3→2, P4→3, P5→4, P6→5, P7→6, P8→7.

| Piste | Index | Instrument | Pan | Vol | Chaîne FX |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Drums** | 0 | Gen Purpose Kit (rack) — breaks lo-fi | 0 | 0.80 | MCompressor (colle) ; `MCharisma` (Lo-fi 30 %) à charger |
| **Basse** | 1 | Surge XT — « 808 Sub » (Sine + saturation) | 0 | 0.85 | MDelay (dub) + MEqualizer |
| **Pads/Claviers** | 2 | Surge XT — « Hammond B3 » (Drawbars 888000000) | −0.20 | 0.75 | Reverb (Ableton) + MFlanger ; `MReverb` (Spring) à charger |
| **Lead/Mélodie** | 3 | Surge XT — « Sustain Guitar » (Pad e-bow) | +0.20 | 0.70 | Drum Noise Glitcher (rack) + Massive Sidechain Distort (rack) ; `MFlanger` à charger |
| **Arp/Contrepoint** | 4 | Surge XT — scratches | −0.30 | 0.60 | MPhaser + MDelay ; `MFilter` (Auto-Wah) à charger |
| **Fx** | 5 | Surge XT (MIDI — PAS audio) — « Subharmonics » (Osc1 Square −2 oct.) | 0 | 0.65 | Reverb (Ableton) + Auto Filter |
| **Aux/synthé2** | 6 | Surge XT — percussions (claps, rimshots) | +0.30 | 0.70 | Chorus-Ensemble + Chorus + MCompressor ✓ |
| **Voix** | 7 | Audio (slameur) | 0 | 0.90 (mix manuel) | MCompressor (vocal) + De-esser ; `MDelay` (Feedback 60 %) à charger |

> Convention : effet Meldaproduction cité par le doc mais absent du template → mentionné « à charger ».

### Réglages Surge XT (du doc)

- **Basse** — « 808 Sub » : Sine + saturation (drive intégré), sub profond.
- **Orgue** — « Hammond B3 » : Drawbars 888000000, son d'orgue trip-hop.
- **E-Bow** — « Sustain Guitar » : son de guitare à sustain (pad), notes tenues.
- **Synthé grave** — « Subharmonics » : Osc1 Square −2 octaves, couche de fréquences graves.
- **Scratches** — échantillons audio (à charger en sampler Surge XT sur la piste 4, ou en clips audio sur la piste Voix — voir Notes de production).

## Clips JSON (motifs principaux — temps en beats)

> Légende hauteurs (convention **C3 = 60**) : 40 E2 · 42 Gb1 · 44 Ab1 · 46 Bb1 · 47 B1 · 48 C2 · 49 Db2 · 50 D2 · 51 Eb2 · 52 E2 · 53 F2 · 54 Gb2 · 55 G2 · 56 Ab2 · 58 Bb2 · 59 B2 · 60 C3 · 61 Db3 · 62 D3 · 63 Eb3 · 64 E3 · 65 F3 · 66 F#3 · 67 G3 · 68 Ab3 · 69 A3 · 70 Bb3 · 71 B3 · 72 C4.
>
> Conversion métrique utilisée : **4/4 → 1 mesure = 4 beats**.

### A. Couplet — Accords (Piste Pads/Claviers, index 2) — `Fm9 - Bb13 - Ebmaj9 - Abmaj7`

Boucle de 2 mesures (8 beats), 2 beats par accord. **Corrections appliquées** :
1. Le Bb13 du doc était Bb-D-F-Bb-D-F (46-50-53-58-62-65), sans la 7e (Ab) ni la 13e (G) → corrigé en Bb-D-F-Ab-Bb-G (46-50-53-56-58-67).
2. La boucle « 2 mesures » du doc ne contenait que 2 accords → complétée avec Ebmaj9 et Abmaj7 pour couvrir les 2 mesures de la grille.

```json
{
  "clip_name": "C5_Chords_Slam",
  "bpm": 85,
  "notes": [
    { "time": 0.0, "pitch": 53, "duration": 2.0, "velocity": 75 },
    { "time": 0.0, "pitch": 56, "duration": 2.0, "velocity": 70 },
    { "time": 0.0, "pitch": 60, "duration": 2.0, "velocity": 75 },
    { "time": 0.0, "pitch": 63, "duration": 2.0, "velocity": 70 },
    { "time": 0.0, "pitch": 67, "duration": 2.0, "velocity": 65 },
    { "time": 2.0, "pitch": 46, "duration": 2.0, "velocity": 80 },
    { "time": 2.0, "pitch": 50, "duration": 2.0, "velocity": 75 },
    { "time": 2.0, "pitch": 53, "duration": 2.0, "velocity": 80 },
    { "time": 2.0, "pitch": 56, "duration": 2.0, "velocity": 75 },
    { "time": 2.0, "pitch": 58, "duration": 2.0, "velocity": 75 },
    { "time": 2.0, "pitch": 67, "duration": 2.0, "velocity": 70 },
    { "time": 4.0, "pitch": 51, "duration": 2.0, "velocity": 75 },
    { "time": 4.0, "pitch": 55, "duration": 2.0, "velocity": 70 },
    { "time": 4.0, "pitch": 58, "duration": 2.0, "velocity": 75 },
    { "time": 4.0, "pitch": 62, "duration": 2.0, "velocity": 70 },
    { "time": 4.0, "pitch": 65, "duration": 2.0, "velocity": 65 },
    { "time": 6.0, "pitch": 56, "duration": 2.0, "velocity": 75 },
    { "time": 6.0, "pitch": 60, "duration": 2.0, "velocity": 70 },
    { "time": 6.0, "pitch": 63, "duration": 2.0, "velocity": 75 },
    { "time": 6.0, "pitch": 67, "duration": 2.0, "velocity": 65 }
  ]
}
```

> Fm9 = F2(53)+Ab2(56)+C3(60)+Eb3(63)+G3(67) ✓ ; Bb13 = Bb1(46)+D2(50)+F2(53)+Ab2(56)+Bb2(58)+G3(67) ✓ ; Ebmaj9 = Eb2(51)+G2(55)+Bb2(58)+D3(62)+F3(65) ✓ ; Abmaj7 = Ab2(56)+C3(60)+Eb3(63)+G3(67) ✓.

### B. Pont — Accords (Piste Pads/Claviers, index 2) — `Dbm9 - Gb13 - Bmaj7 - E6`

Boucle de 2 mesures (8 beats), 2 beats par accord, nappe dissonante. **Ajout proposé** : le doc fournit la grille du pont mais pas de JSON — clip construit pour l'implémenter.

```json
{
  "clip_name": "C5_Pont_Chords",
  "bpm": 85,
  "notes": [
    { "time": 0.0, "pitch": 49, "duration": 2.0, "velocity": 70 },
    { "time": 0.0, "pitch": 52, "duration": 2.0, "velocity": 70 },
    { "time": 0.0, "pitch": 56, "duration": 2.0, "velocity": 65 },
    { "time": 0.0, "pitch": 59, "duration": 2.0, "velocity": 65 },
    { "time": 0.0, "pitch": 63, "duration": 2.0, "velocity": 60 },
    { "time": 2.0, "pitch": 42, "duration": 2.0, "velocity": 75 },
    { "time": 2.0, "pitch": 46, "duration": 2.0, "velocity": 70 },
    { "time": 2.0, "pitch": 49, "duration": 2.0, "velocity": 70 },
    { "time": 2.0, "pitch": 51, "duration": 2.0, "velocity": 65 },
    { "time": 2.0, "pitch": 52, "duration": 2.0, "velocity": 65 },
    { "time": 4.0, "pitch": 47, "duration": 2.0, "velocity": 70 },
    { "time": 4.0, "pitch": 51, "duration": 2.0, "velocity": 70 },
    { "time": 4.0, "pitch": 54, "duration": 2.0, "velocity": 65 },
    { "time": 4.0, "pitch": 58, "duration": 2.0, "velocity": 65 },
    { "time": 6.0, "pitch": 40, "duration": 2.0, "velocity": 75 },
    { "time": 6.0, "pitch": 44, "duration": 2.0, "velocity": 70 },
    { "time": 6.0, "pitch": 47, "duration": 2.0, "velocity": 70 },
    { "time": 6.0, "pitch": 56, "duration": 2.0, "velocity": 65 },
    { "time": 6.0, "pitch": 61, "duration": 2.0, "velocity": 60 }
  ]
}
```

> Dbm9 = Db2(49)+E2(52/Fb)+Ab2(56)+B2(59/Cb)+Eb3(63) ✓ ; Gb13 = Gb1(42)+Bb1(46)+Db2(49)+Eb2(51)+E2(52/Fb) ✓ ; Bmaj7 = B1(47)+Eb2(51/D#)+Gb2(54/F#)+Bb2(58/A#) ✓ ; E6 = E2(40)+Ab1(44/G#)+B1(47)+Ab2(56/G#)+Db3(61/C#) ✓.

## Automations (temps en beats)

| Moment | Paramètre | Points (breakpoints) | Effet |
| :--- | :--- | :--- | :--- |
| **Couplet 1 → Pont** | MDelay — Feedback (P8 Voix, index 7) | `0.0→30 %`, `16.0→60 %`, `24.0→10 %`, `32.0→70 %` | Le delay enfle sur les fins de phrases (60 %), retombe, remonte au pont. |
| **Toute la chanson** | MFilter — Cutoff (P5 Scratch, index 4) | LFO Sin, Rate 2 Hz, Depth 80 % | Auto-wah sur les scratches. |

> ⚠️ Points MDelay = valeurs du doc (schematic, positions en beats, barres 1-9) ; **à re-calquer sur la structure 60 barres**. Les pourcentages sont à convertir en valeur normalisée (0-1) — mapping à vérifier à l'oreille.

## Réglages Mix

| Piste | Vol | Pan | Notes |
| :--- | :--- | :--- | :--- |
| Drums | 0.80 | — | Breaks lo-fi, MCharisma Lo-fi 30 % (à charger) |
| Basse | 0.85 | — | 808 Sub (Sine + saturation) ; MDelay dub + MEqualizer |
| Pads/Claviers | 0.75 | −0.20 | Hammond B3 Drawbars 888000000 ; Reverb + MReverb Spring |
| Lead/Mélodie | 0.70 | +0.20 | E-Bow Sustain Guitar (pad) ; MFlanger |
| Arp/Contrepoint | 0.60 | −0.30 | Scratches ; MFilter Auto-Wah (LFO Sin 2 Hz, Depth 80 %) |
| Fx | 0.65 | — | Synthé grave Subharmonics (Osc1 Square −2 oct.) |
| Aux/synthé2 | 0.70 | +0.30 | Percussions (claps, rimshots) |
| Voix | 0.90 (mix manuel) | — | MCompressor + De-esser ; MDelay Feedback 60 % |

## Notes de production

- **Correction Bb13 (doc)** : l'accord fourni était Bb-D-F-Bb-D-F (46-50-53-58-62-65), sans la 7e (Ab) ni la 13e (G). Corrigé → Bb1(46)+D2(50)+F2(53)+Ab2(56)+Bb2(58)+G3(67) = Bb13 complet.
- **Complétion de la boucle accords** : le doc donnait un JSON à 2 accords (Fm9-Bb13) pour une « boucle de 2 mesures » → complété avec Ebmaj9 et Abmaj7 (2 beats par accord = 8 beats = 2 mesures).
- **Accords du pont vérifiés** : Dbm9 = Db-E-Ab-B-Eb (Fb→E, Cb→B) ; Gb13 = Gb-Bb-Db-E-Eb ; Bmaj7 = B-D#-F#-A# ; E6 = E-G#-B-C#. Clip JSON ajouté (le doc ne fournissait que la grille).
- **Réaffectation doc → template** : P1 Drums → 0, P2 Basse → 1, P3 Orgue → 2, P4 E-Bow → 3, P5 Scratch → 4, P6 Synthé grave → 5, P7 Percussions → 6, P8 Voix → 7.
- **Fx en MIDI (Surge XT)** : la piste Fx (5) est MIDI — le synthé grave (Subharmonics) est un patch Surge XT, PAS un clip audio.
- **Scratches (audio)** : la piste 4 est MIDI au template → les samples de scratches sont à charger en échantillon Surge XT sur la piste 4, ou en clips audio sur la piste Voix (7). À arbitrer.
- **Meldaproduction absents du template** → à charger : MCharisma, MReverb, MFlanger, MFilter, MDelay (voix).
- **MTime** : rubatos sur la voix (Meldaproduction) — ne touche pas au BPM global (85 constant).
- **Voix baryton** : parlé-chanté E3-B3 (pitch 64-71), rythmique parlée sur les couplets, chanté sur les refrains, spoken word sur le pont.
- ⏳ **À valider** : adaptation de la tonalité si la mélodie (voix baryton E3-B3) sort de la tessiture.

## Intégration MCP

Indices **0-based** (0 = Drums, 1 = Basse, 2 = Pads/Claviers, 3 = Lead/Mélodie, 4 = Arp/Contrepoint, 5 = Fx, 6 = Aux/synthé2, 7 = Voix). Temps des notes en **beats**.

1. **Tempo** : `set_tempo(85)` — constant sur toute la chanson.
2. **Accords couplet** : `create_clip(2, 0, 8)` puis `add_notes_to_clip(2, 0, notes)` avec le JSON A (boucle de 2 mesures).
3. **Accords pont** : `create_clip(2, 1, 8)` puis `add_notes_to_clip(2, 1, notes)` avec le JSON B.
4. **Intro** : sample « Le langage est la maison de l'être » via `create_audio_clip(7, 0, "chemin/vers/heidegger.wav")` (piste Voix, audio).
5. **Arrangement** : `duplicate_to_arrangement(track_index, clip_index, destination_time)` — 1 barre 4/4 = 4 beats (destination_time en beats, 0-based).
6. **Automations** : `set_automation_curve(track_index, clip_index, target, points, is_arrangement=True)` avec les breakpoints ci-dessus (MDelay Feedback sur la piste 7, MFilter Cutoff sur la piste 4 — en beats). Les effets Meldaproduction (MDelay, MFilter, MCharisma, MReverb, MFlanger) doivent d'abord être chargés (`load_instrument_or_effect` / `load_external_plugin`) — ils ne sont pas dans le template.

## Paroles
Voir `PAROLES.md` dans ce dossier.
