# 04 — Matière et Mouvement

**Tempo**: 110 → 75 → 115 BPM (breakdown 7/8 à 75, dernier drop à 115)
**Tonalité**: Fa mineur phrygien (F) — drop en `Fm9 - GbMaj7#11 - C7sus4(b9) - Bbm13`
**Durée**: ≈ 2 min 30 (56 barres — arrangement proposé)
**Atmosphère**: Metal progressif, locomotive, loi de Newton en déclamation scientifique
**Style**: Metal progressif (drop, blast beats, longs breaks atmosphériques)
**Voix**: Baryton parlé-chanté (E3 → B3, pitch 64-71), spoken word en intro sur sample de locomotive

## Hommage / Inspirations
- Gojira : riff lourd en drop, blast beats, breaks qui respirent.
- Tool / Meshuggah : passages en 7/8, atmosphérique ↔ brutal.
- Metal orchestré : nappe cinématique « Strings » sous le breakdown.

## Structure (en barres)

Intro (4) | Couplet 1 (8) | Refrain 1 (8, en 7/8) | Couplet 2 (8) | Refrain 2 (8, en 7/8) | Pont (8) | Dernier drop (8) | Outro (4) = **56 barres**

| # | Section | Barres | Éléments clés |
| :---: | :--- | :--- | :--- |
| 1 | Intro | 1-4 | Bruit de locomotive, sample « Référentiel galiléen... », nappe ciné (pad Strings) |
| 2 | Couplet 1 | 5-12 | Riff lourd (power chords Fm9/GbMaj7#11), blast beats, basse distordue |
| 3 | Refrain 1 | 13-20 (7/8) | Breakdown atmosphérique `Dbmaj9 - Em11 - A7alt - Dm(add9)`, larsens lead, batterie au ralenti |
| 4 | Couplet 2 | 21-28 | Mid-tempo, riff, déclamation des trois lois |
| 5 | Refrain 2 | 29-36 (7/8) | Retour du breakdown, plus intense |
| 6 | Pont | 37-44 | Larsens, batterie au ralenti, pad + voix seule, dérivée seconde |
| 7 | Dernier drop | 45-52 | Blast beats, tout le monde, brass hits, MDistortion Drive 90 % |
| 8 | Outro | 53-56 | Fondu, train qui s'éloigne |

> ⚠️ Structure **proposée** : le doc source ne donne pas de découpage en barres. À valider sur l'arrangement réel.

## BPM Map

| Repère | Position (beats) | Barres (4/4) | BPM | Événement |
| :--- | :--- | :--- | :--- | :--- |
| Début | 0.0 | 1 | **110** | Intro + Couplet 1 (riff lourd) |
| Break | 16.0 | 5 | **75** | Breakdown atmosphérique (Refrain 7/8) |
| Dernier drop | 24.0 | 7 | **115** | Dernier drop (blast) |

> ⚠️ Table du doc **compressée** (3 points en beats, position 0/16/24). **À arbitrer : recaler les points de tempo sur la structure 56 barres** (110 couplets → 75 refrains/pont → 115 dernier drop) avant l'arrangement.

## Grille d'accords

| Section | Grille | Couleur / Sonorité |
| :--- | :--- | :--- |
| **Drop / Couplet** | `Fm9 - GbMaj7#11 - C7sus4(b9) - Bbm13` | Mode phrygien en Fa, riff lourd en power chords. |
| **Refrain (7/8)** | `Dbmaj9 - Em11 - A7alt - Dm(add9)` | Breakdown atmosphérique, 1 accord par mesure de 7/8. |
| **Pont** | Nappe sur Fm9 (tenue) | Respiration, dérivée seconde, larsens. |

> Vérification des accords (convention **C3 = 60**) :
> - **Fm9** = F-Ab-C-Eb-G → power chord F5 = **F2 (53) + C3 (60)** ✓
> - **GbMaj7#11** = Gb-Bb-Db-F-C → power chord Gb5 = **Gb2 (54) + Db3 (61)** ✓
> - **C7sus4(b9)** = C-F-G-Bb-Db → power chord C5 = **C3 (60) + G3 (67)**
> - **Bbm13** = Bb-Db-F-Ab-G → power chord Bb5 = **Bb2 (58) + F3 (65)**

## Instruments (Ableton) — Mix

Template réel `bac.als` (indices **0-based**), pistes 0-6 MIDI, piste 7 Audio (Voix). Réaffectation des pistes du doc (P1-P8) sur le template.

| Piste | Index | Instrument | Pan | Vol | Chaîne FX |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Drums** | 0 | Gen Purpose Kit (rack) — Kick C1 (36), Snare D1 (38), Hats F#1 (42), Cymbales A#1 (46) | 0 | 0.85 | MCompressor (colle) ; `MDistortion` (Drive 15 %, → 90 % au dernier drop) à charger |
| **Basse** | 1 | Surge XT — Square + Sub | 0 | 0.80 | MEqualizer (boost 80 Hz, coupe 400 Hz) |
| **Pads/Claviers** | 2 | Surge XT — « Strings » (attaque 2 s) | −0.10 | 0.70 | Reverb (Ableton, Hall) + MFlanger ; `MReverb` à charger |
| **Lead/Mélodie** | 3 | Surge XT — « Heavy Riff » (Saw + Noise, Filter BPF) | 0 | 0.80 | Drum Noise Glitcher (rack) + Massive Sidechain Distort (rack) ; `MCharisma` (Drive 50 %) à charger |
| **Arp/Contrepoint** | 4 | Surge XT — « Scream Lead » (FM ratio 1.2, Feedback 70 %) | +0.10 | 0.75 | MPhaser + MDelay (1/4) ; MDelay déjà présent sur le template ✓ |
| **Fx** | 5 | Surge XT (MIDI — PAS audio) — moteurs, train | −0.25 | 0.60 | Reverb (Ableton) + Auto Filter ; `MFilter` (Low-pass automatisé) à charger |
| **Aux/synthé2** | 6 | Surge XT — « Synth Brass » (hits du dernier drop) | +0.30 | 0.75 | Chorus-Ensemble + Chorus + MCompressor ✓ |
| **Voix** | 7 | Audio (spoken word + parlé-chanté réel) | 0 | 0.90 (mix manuel) | MCompressor (Ratio 6:1) + De-esser ; `MDeEsser` à charger |

> Convention : effet Meldaproduction cité par le doc mais absent du template → mentionné « à charger ».

### Réglages Surge XT (du doc)
- **Drums (rack)** — Kick : C1 (36). Snare : D1 (38). Hats/cymbales : blast sur F#1 (42) / A#1 (46).
- **Basse** — Osc1 Square + Sub. Filter LPF, Cutoff 45 %. Drive intégré 60 %.
- **Guitare Rythmique** — « Heavy Riff » : Saw + Noise, Filter BPF. MCharisma Drive 50 %.
- **Lead** — « Scream Lead » : FM ratio 1.2, Feedback 70 %. MDelay 1/4.
- **Pad** — « Strings » : attaque 2 s.
- **Brass** — « Synth Brass » : pour les hits du dernier drop.

## Clips JSON (motifs principaux — temps en beats)

> Légende hauteurs (convention **C3 = 60**) : 36 C1 · 38 D1 · 42 F#1 · 46 A#1 · 53 F2 · 54 Gb2 · 58 Bb2 · 60 C3 · 61 Db3 · 62 D3 · 63 Eb3 · 64 E3 · 65 F3 · 66 Gb3 · 67 G3 · 68 Ab3 · 69 A3 · 70 Bb3 · 71 B3 · 72 C4 · 73 Db4 · 74 D4 · 75 Eb4 · 76 E4 · 77 F4.
>
> Conversion métrique utilisée : **4/4 → 1 mesure = 4 beats** ; **7/8 → 1 mesure = 7 croches = 3,5 beats** (1 croche = 0,5 beat). Les durées du refrain sont donc en multiples de 3,5.

### A. Drop — Power Chords (Piste Lead/Mélodie, index 3) — `Fm9 - GbMaj7#11`
Motif de 1 mesure 4/4 (4 beats), rythmique en noires. **Correction appliquée : les commentaires du doc indiquaient « F3 » et « C4 » pour les pitch 53 et 60 — sous la convention C3=60 ce sont F2 et C3 (F5) ; 54 et 61 sont Gb2 et Db3 (Gb5). Les pitch sont corrects (racine + quinte), seuls les libellés sont corrigés.** Répéter ×2 sur le drop (C7sus4(b9) → C3+G3, Bbm13 → Bb2+F3).

```json
{
  "clip_name": "C4_Drop_Riff",
  "bpm": 110,
  "notes": [
    { "time": 0.0, "pitch": 53, "duration": 1.0, "velocity": 95 },
    { "time": 0.0, "pitch": 60, "duration": 1.0, "velocity": 95 },
    { "time": 1.0, "pitch": 53, "duration": 1.0, "velocity": 90 },
    { "time": 1.0, "pitch": 60, "duration": 1.0, "velocity": 90 },
    { "time": 2.0, "pitch": 54, "duration": 1.0, "velocity": 95 },
    { "time": 2.0, "pitch": 61, "duration": 1.0, "velocity": 95 },
    { "time": 3.0, "pitch": 54, "duration": 1.0, "velocity": 90 },
    { "time": 3.0, "pitch": 61, "duration": 1.0, "velocity": 90 }
  ]
}
```
> F5 = F2 (53) + C3 (60) — racine + quinte du Fm9 ✓ ; Gb5 = Gb2 (54) + Db3 (61) — racine + quinte du GbMaj7#11 ✓.

### B. Drop — Basse (Piste Basse, index 1) — racines du riff
Motif de 1 mesure 4/4 (4 beats), suit le riff A (F puis Gb, 2 beats par accord).

```json
{
  "clip_name": "C4_Drop_Bass",
  "bpm": 110,
  "notes": [
    { "time": 0.0, "pitch": 53, "duration": 2.0, "velocity": 95 },
    { "time": 2.0, "pitch": 54, "duration": 2.0, "velocity": 90 }
  ]
}
```

### C. Couplet — Batterie blast (Piste Drums, index 0)
Kick = C1 (36), Snare = D1 (38), Hats = F#1 (42), Cymbale = A#1 (46). Motif de 1 mesure 4/4 : kick en croches, snare en contre-temps, hats en 16e, crash sur le 1. Répéter sur les 8 mesures du couplet.

```json
{
  "clip_name": "C4_Couplet_Blast",
  "bpm": 110,
  "notes": [
    { "time": 0.0, "pitch": 36, "duration": 0.5, "velocity": 95 },
    { "time": 0.5, "pitch": 36, "duration": 0.5, "velocity": 90 },
    { "time": 1.0, "pitch": 36, "duration": 0.5, "velocity": 95 },
    { "time": 1.5, "pitch": 36, "duration": 0.5, "velocity": 90 },
    { "time": 2.0, "pitch": 36, "duration": 0.5, "velocity": 95 },
    { "time": 2.5, "pitch": 36, "duration": 0.5, "velocity": 90 },
    { "time": 3.0, "pitch": 36, "duration": 0.5, "velocity": 95 },
    { "time": 3.5, "pitch": 36, "duration": 0.5, "velocity": 90 },
    { "time": 0.25, "pitch": 38, "duration": 0.5, "velocity": 85 },
    { "time": 0.75, "pitch": 38, "duration": 0.5, "velocity": 85 },
    { "time": 1.25, "pitch": 38, "duration": 0.5, "velocity": 85 },
    { "time": 1.75, "pitch": 38, "duration": 0.5, "velocity": 85 },
    { "time": 2.25, "pitch": 38, "duration": 0.5, "velocity": 85 },
    { "time": 2.75, "pitch": 38, "duration": 0.5, "velocity": 85 },
    { "time": 3.25, "pitch": 38, "duration": 0.5, "velocity": 85 },
    { "time": 3.75, "pitch": 38, "duration": 0.5, "velocity": 85 },
    { "time": 0.0, "pitch": 46, "duration": 0.5, "velocity": 80 },
    { "time": 0.0, "pitch": 42, "duration": 0.125, "velocity": 60 },
    { "time": 0.25, "pitch": 42, "duration": 0.125, "velocity": 55 },
    { "time": 0.5, "pitch": 42, "duration": 0.125, "velocity": 60 },
    { "time": 0.75, "pitch": 42, "duration": 0.125, "velocity": 55 },
    { "time": 1.0, "pitch": 42, "duration": 0.125, "velocity": 62 },
    { "time": 1.25, "pitch": 42, "duration": 0.125, "velocity": 55 },
    { "time": 1.5, "pitch": 42, "duration": 0.125, "velocity": 60 },
    { "time": 1.75, "pitch": 42, "duration": 0.125, "velocity": 55 },
    { "time": 2.0, "pitch": 42, "duration": 0.125, "velocity": 62 },
    { "time": 2.25, "pitch": 42, "duration": 0.125, "velocity": 55 },
    { "time": 2.5, "pitch": 42, "duration": 0.125, "velocity": 60 },
    { "time": 2.75, "pitch": 42, "duration": 0.125, "velocity": 55 },
    { "time": 3.0, "pitch": 42, "duration": 0.125, "velocity": 62 },
    { "time": 3.25, "pitch": 42, "duration": 0.125, "velocity": 55 },
    { "time": 3.5, "pitch": 42, "duration": 0.125, "velocity": 60 },
    { "time": 3.75, "pitch": 42, "duration": 0.125, "velocity": 55 }
  ]
}
```

### D. Refrain — Breakdown (Piste Pads/Claviers, index 2) — 7/8
1 accord par mesure de 7/8 (**3,5 beats**). 4 mesures = 14 beats, grille `Dbmaj9 - Em11 - A7alt - Dm(add9)`. Répéter ×2 sur un refrain de 8 mesures (28 beats).

```json
{
  "clip_name": "C4_Refrain_Breakdown",
  "bpm": 75,
  "notes": [
    { "time": 0.0, "pitch": 61, "duration": 3.5, "velocity": 80 },
    { "time": 0.0, "pitch": 65, "duration": 3.5, "velocity": 80 },
    { "time": 0.0, "pitch": 68, "duration": 3.5, "velocity": 80 },
    { "time": 0.0, "pitch": 72, "duration": 3.5, "velocity": 75 },
    { "time": 0.0, "pitch": 75, "duration": 3.5, "velocity": 75 },
    { "time": 3.5, "pitch": 64, "duration": 3.5, "velocity": 80 },
    { "time": 3.5, "pitch": 67, "duration": 3.5, "velocity": 80 },
    { "time": 3.5, "pitch": 71, "duration": 3.5, "velocity": 80 },
    { "time": 3.5, "pitch": 74, "duration": 3.5, "velocity": 75 },
    { "time": 3.5, "pitch": 77, "duration": 3.5, "velocity": 75 },
    { "time": 7.0, "pitch": 69, "duration": 3.5, "velocity": 80 },
    { "time": 7.0, "pitch": 73, "duration": 3.5, "velocity": 80 },
    { "time": 7.0, "pitch": 67, "duration": 3.5, "velocity": 75 },
    { "time": 7.0, "pitch": 70, "duration": 3.5, "velocity": 75 },
    { "time": 7.0, "pitch": 75, "duration": 3.5, "velocity": 75 },
    { "time": 10.5, "pitch": 62, "duration": 3.5, "velocity": 80 },
    { "time": 10.5, "pitch": 65, "duration": 3.5, "velocity": 80 },
    { "time": 10.5, "pitch": 69, "duration": 3.5, "velocity": 80 },
    { "time": 10.5, "pitch": 76, "duration": 3.5, "velocity": 75 }
  ]
}
```
> Vérification : Dbmaj9 = Db-F-Ab-C-Eb (61-65-68-72-75) ✓ ; Em11 = E-G-B-D-F-A (64-67-71-74-77) ✓ ; A7alt = A-C#-G-Bb-Eb (69-73-67-70-75) ✓ ; Dm(add9) = D-F-A-E (62-65-69-76) ✓.

### E. Refrain — Lead « Scream Lead » (Piste Arp/Contrepoint, index 4) — larsen
Motif de 2 mesures 7/8 (7 beats), notes tenues phrygiennes (Bb-Ab-Gb), à valider à l'oreille.

```json
{
  "clip_name": "C4_Refrain_Lead",
  "bpm": 75,
  "notes": [
    { "time": 0.0, "pitch": 70, "duration": 1.75, "velocity": 85 },
    { "time": 1.75, "pitch": 72, "duration": 1.75, "velocity": 85 },
    { "time": 3.5, "pitch": 73, "duration": 3.5, "velocity": 80 }
  ]
}
```

## Automations (temps en beats)

| Moment | Paramètre | Points (breakpoints) | Effet |
| :--- | :--- | :--- | :--- |
| **Couplet → Dernier drop** | MDistortion — Drive (P1 Drums, index 0) | `0.0→20 %`, `12.0→70 %`, `16.0→10 %`, `24.0→90 %` | Saturation qui monte au drop, redescend au breakdown, sommet au dernier drop. |
| **Breakdown → Dernier drop** | Volume Master | `16.0→−3 dB`, `18.0→−12 dB`, `24.0→0 dB` | Le breakdown s'éteint presque, le dernier drop repart à fond. |
| **Toute la chanson** | MFilter — Low-pass (P6 FX, index 5) | `0.0→10 %`, `16.0→40 %`, `24.0→80 %`, `56.0→5 %` | Le train approche (intro fermé), s'ouvre sur le drop, s'éloigne à l'outro. |
| **Tempo** | Automations par section | 110 → 75 → 115 | Voir BPM Map. |

> ⚠️ Points MDistortion/Volume Master = valeurs du doc (schematic, positions en beats) ; **à re-calquer sur la structure 56 barres**. Les dB du Volume Master sont à convertir en valeur normalisée (0-1) — mapping à vérifier à l'oreille.

## Réglages Mix

| Piste | Vol | Pan | Notes |
| :--- | :--- | :--- | :--- |
| Drums | 0.85 | — | Blast kicks/snare, MDistortion Drive 15 % → 90 % dernier drop |
| Basse | 0.80 | — | Square + Sub, Drive 60 % ; MEqualizer boost 80 Hz / coupe 400 Hz |
| Pads/Claviers | 0.70 | −0.10 | Nappe Strings (attaque 2 s) sur intro, breakdown et pont |
| Lead/Mélodie | 0.80 | — | Heavy Riff (power chords) ; MCharisma Drive 50 % |
| Arp/Contrepoint | 0.75 | +0.10 | Scream Lead (larsens breakdown), MDelay 1/4 |
| Fx | 0.60 | −0.25 | Moteurs/train (MIDI Surge) ; Auto Filter + MFilter Low-pass |
| Aux/synthé2 | 0.75 | +0.30 | Synth Brass : hits sur les temps du dernier drop |
| Voix | 0.90 (mix manuel) | — | MCompressor 6:1 + De-esser ; spoken word + parlé-chanté |

## Notes de production

- **Correction des libellés du clip power chords** : pitch 53 = F2 (et non « F3 »), 60 = C3 (et non « C4 »), 54 = Gb2, 61 = Db3. Les hauteurs étaient correctes (F5 = racine + quinte du Fm9 ; Gb5 = racine + quinte du GbMaj7#11), seuls les commentaires du doc étaient faux.
- **Extension du drop (grille complète)** : après le motif F-Gb, ajouter C7sus4(b9) → power C5 (C3+G3) et Bbm13 → power Bb5 (Bb2+F3), soit 2 beats par accord sur 4 mesures.
- **Réaffectation doc → template** : Guitare Rythmique → index 3 (Lead/Mélodie, Surge « Heavy Riff »), Lead Guitare → index 4 (Arp/Contrepoint, Surge « Scream Lead », MDelay 1/4 présent sur le template ✓), Pad Ciné → index 2 (Strings, Reverb Ableton + MReverb à charger), Brass → index 6 (Aux/synthé2, MCompressor présent ✓).
- **Fx en MIDI (Surge XT)** : les moteurs/train sont des notes/patches Surge sur la piste Fx (index 5), PAS des clips audio ; le sample de locomotive de l'intro ira sur la piste **Voix** (audio) via `create_audio_clip`.
- **Conversion métrique** : drop et couplets en 4/4 (1 mesure = 4 beats) ; refrain en **7/8 (1 mesure = 7 croches = 3,5 beats)** — toutes les durées du refrain sont en multiples de 3,5.
- **Meldaproduction absents du template** → à charger : MDistortion, MCharisma, MReverb, MFilter, MDeEsser.
- **Arbitrage MDistortion** : le doc le place sur P1 Drums (section 2) mais l'automation dit « P3 » — cible retenue : Drums (index 0), à confirmer.
- **Voix baryton** : parlé-chanté E3-B3, spoken word d'intro « Référentiel galiléen... » sur sample de locomotive.
- ⏳ **À valider** : adaptation de la tonalité si la mélodie (voix baryton E3-B3) sort de la tessiture.

## Intégration MCP

Indices **0-based** (0 = Drums, 1 = Basse, 2 = Pads/Claviers, 3 = Lead/Mélodie, 4 = Arp/Contrepoint, 5 = Fx, 6 = Aux/synthé2, 7 = Voix). Temps des notes en **beats**.

1. **Tempo** : `set_tempo(110)` (intro/couplet) → `set_tempo(75)` (refrain 7/8 et pont) → `set_tempo(115)` (dernier drop).
2. **Intro** : `create_clip(2, 0, 16)` (nappe Strings) et `create_clip(5, 0, 16)` (train FX) ; sample « Référentiel galiléen » via `create_audio_clip(7, 0, "chemin/vers/locomotive.wav")`.
3. **Couplet 1** : `create_clip(3, 0, 32)` puis `add_notes_to_clip(3, 0, notes)` avec le JSON A (power chords) ; `create_clip(1, 0, 32)` + JSON B (basse) ; `create_clip(0, 0, 32)` + JSON C (blast).
4. **Refrain 7/8** : `create_clip(2, 1, 28)` + JSON D (breakdown, 1 mesure = 3,5 beats) ; lead sur `create_clip(4, 1, 28)` + JSON E.
5. **Dernier drop** : brass hits via `create_clip(6, 0, 32)` + `add_notes_to_clip` ; MDistortion Drive 90 %.
6. **Arrangement** : `duplicate_to_arrangement(track_index, clip_index, destination_time)` — 1 barre 4/4 = 4 beats, 1 barre 7/8 = 3,5 beats (destination_time en beats, 0-based).
7. **Automations** : `set_automation_curve(track_index, clip_index, target, points, is_arrangement=True)` avec les breakpoints ci-dessus (MDistortion Drive, Volume Master, MFilter Low-pass — en beats).

## Paroles
Voir `PAROLES.md` dans ce dossier.
