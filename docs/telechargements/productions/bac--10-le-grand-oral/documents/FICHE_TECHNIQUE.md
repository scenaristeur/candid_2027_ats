# 10 — Le Grand Oral

**Tempo**: 72 → 98 BPM (map par section)
**Tonalité**: Sol majeur (G)
**Durée**: ≈ 2 min 40 (56 barres — arrangement complet)
**Atmosphère**: Hymne fédérateur, montée en puissance, chaleureux, confiance
**Style**: Pop acoustique / Hymne
**Voix**: Baryton parlé-chanté (E3 → B3, pitch 64-71)

## Hommage / Inspirations
- Hymne pop acoustique : guitare strumming, montée en puissance, chœurs.
- « Chanson du bac » : la méthodologie (problématique, plan, dialectique) comme matière à chanter.
- Modulation `Am9 - D13 - Gmaj7 - E7b9` pour la montée orchestrale avant le dernier refrain.

## Structure (en barres)

Intro (4) | Couplet 1 (8) | Refrain 1 (8) | Couplet 2 (8) | Refrain 2 (8) | Pont (8) | Dernier refrain (8) | Outro (4) = **56 barres**

| # | Section | Barres | Éléments clés |
| :---: | :--- | :--- | :--- |
| 1 | Intro | 1-4 | Guitare folk fingerpicking, Gmaj9 arpégé |
| 2 | Couplet 1 | 5-12 | Entrée shaker/cajón + basse acoustique, accords strumming |
| 3 | Refrain 1 | 13-20 | Chœurs, modulation Am9-D13-Gmaj7-E7b9 |
| 4 | Couplet 2 | 21-28 | Retour du couplet, claps |
| 5 | Refrain 2 | 29-36 | Chœurs + claps, plus énergique |
| 6 | Pont | 37-44 | Montée orchestrale, cordes douces (swell) |
| 7 | Dernier refrain | 45-52 | Crescendo, 98 BPM, chœurs complets |
| 8 | Outro | 53-56 | A cappella final, retour au calme |

## BPM Map

| Repère | Barres | BPM | Événement |
| :--- | :--- | :--- | :--- |
| Intro | 1-4 | **72** | Fingerpicking guitare folk |
| Couplet 1 | 5-12 | **72** | Shaker/cajón, basse acoustique |
| Refrain 1 | 13-20 | **72** | Modulation, chœurs |
| Couplet 2 | 21-28 | **72** | Retour du couplet, claps |
| Refrain 2 | 29-36 | **72** | Chœurs, plus énergique |
| Pont | 37-44 | **72** | Montée orchestrale, cordes douces |
| Dernier refrain | 45-52 | **98** | Crescendo, modulation finale |
| Outro | 53-56 | **98 → 72** | A cappella, retour au calme |

> ⚠️ Le doc source ne fournit que 2 points de tempo (`0.0 → 72`, `16.0 → 98` « dernier refrain ») sans table complète. **À arbitrer : recaler le passage à 98 BPM sur la frontière du dernier refrain (barre 45) avant l'arrangement.**

## Grille d'accords

| Section | Grille | Couleur / Sonorité |
| :--- | :--- | :--- |
| **Intro** | `Gmaj9 - Cmaj7 - D7sus4 - Em11` (fingerpicking, arpégé) | Chaleureuse, ouverture lumineuse. |
| **Couplet** | `Gmaj9 - Cmaj7 - D7sus4 - Em11` (2 mesures par accord) | Strumming guitare folk, posé. |
| **Refrain** | `Am9 - D13 - Gmaj7 - E7b9` (2 mesures par accord) | Modulation pour la montée, fédérateur. |
| **Pont** | `Am9 - D13 - Gmaj7 - E7b9` (sur cordes) | Montée orchestrale, crescendo. |
| **Outro** | Voix seule a cappella (fond Gmaj9) | Retour au calme, braise émotionnelle. |

## Instruments (Ableton) — Mix

Template réel `bac.als` (indices **0-based**), pistes 0-6 MIDI, piste 7 Audio (Voix).

| Piste | Index | Instrument | Pan | Vol | Chaîne FX |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Drums** | 0 | Gen Purpose Kit (rack) — shaker + cajón ; claps (sample, pattern 4/4) | 0 | 0.80 | MCompressor (light, doc) ; `MReverb` (Short — claps) à charger |
| **Basse** | 1 | Surge XT — « Acoustic Bass » (Sine + Noise) | 0 | 0.80 | MDelay + MEqualizer (coupe du sub) |
| **Pads/Claviers** | 2 | Surge XT — « Nylon Guitar » (FM + Wavetable, guitare folk) + « Grand Piano » (FM ratio 1.0) | 0 | 0.75 | Reverb (Ableton) + MFlanger ; `MChorus` à charger (doc) |
| **Lead/Mélodie** | 3 | Surge XT — « Soft Strings » (Att 300 ms) — cordes douces | 0 | 0.75 | Drum Noise Glitcher (rack) + Massive Sidechain Distort (rack) ; `MFlanger` à charger (doc) |
| **Arp/Contrepoint** | 4 | Surge XT (contrepoint / nappes secondaires) | +0.20 | 0.70 | MPhaser + MDelay |
| **Fx** | 5 | Surge XT (MIDI — PAS audio) | −0.20 | 0.60 | Reverb (Ableton) + Auto Filter |
| **Aux/synthé2** | 6 | Chœurs (samples ooh/ahh) | 0 | 0.80 | Chorus-Ensemble + Chorus + MCompressor ; `MCharisma` à charger (doc) |
| **Voix** | 7 | Audio (David, baryton) | 0 | 0.90 (mix manuel) | MCompressor (Ratio 3:1, doc) + De-esser ; `MDeEsser` + `MDelay` (Slap 100 ms — refrain) à charger |

> Convention : effet Meldaproduction cité par le doc mais absent du template → mentionné « à charger ».

### Réglages Surge XT (du doc)
- **Basse acoustique** — Osc1 « Acoustic Bass » (Sine + Noise). Env posée ; MEqualizer coupe le sub.
- **Guitare folk** — Osc1 « Nylon Guitar » (FM + Wavetable).
- **Piano** — Osc1 « Grand Piano » (FM, Ratio 1.0).
- **Cordes douces** — Osc1 « Soft Strings », Env Attack 300 ms (swell progressif).

## Clips JSON (motifs principaux — temps en beats)

> Légende hauteurs (convention **C3 = 60**) : 43 G1 · 47 B1 · 48 C2 · 50 D2 · 52 E2 · 54 F#2 · 55 G2 · 57 A2 · 59 B2 · 60 C3 · 62 D3 · 64 E3 · 65 F3 · 66 F#3 · 69 A3.
> ⚠️ Les commentaires du doc source utilisaient un nommage d'octave différent (C3=48) ; les **pitches sont identiques**, seuls les noms de notes sont recalés sur la convention C3=60.

### A. Hymne — Accords couplet (Pistes Pads/Claviers, index 2 — guitare folk + piano) — `Gmaj9 - Cmaj7 - D7sus4 - Em11`
Motif de 2 mesures (8 beats), chaque accord sur 2 beats. **Corrections appliquées : Gmaj9 → ajout de la 9te A (time 0.0, 59→57) ; D7sus4 → 54→55 (G, sus4) et 65→60 (C, 7e).** Répéter ×4 (offsets +8 / +16 / +24 beats) pour un couplet complet de 8 mesures.

```json
{
  "clip_name": "C10_Hymne_Chords",
  "bpm": 72,
  "notes": [
    { "time": 0.0, "pitch": 43, "duration": 2.0, "velocity": 85 },
    { "time": 0.0, "pitch": 47, "duration": 2.0, "velocity": 85 },
    { "time": 0.0, "pitch": 50, "duration": 2.0, "velocity": 80 },
    { "time": 0.0, "pitch": 54, "duration": 2.0, "velocity": 80 },
    { "time": 0.0, "pitch": 57, "duration": 2.0, "velocity": 75 },
    { "time": 2.0, "pitch": 48, "duration": 2.0, "velocity": 85 },
    { "time": 2.0, "pitch": 52, "duration": 2.0, "velocity": 85 },
    { "time": 2.0, "pitch": 55, "duration": 2.0, "velocity": 80 },
    { "time": 2.0, "pitch": 59, "duration": 2.0, "velocity": 80 },
    { "time": 2.0, "pitch": 64, "duration": 2.0, "velocity": 75 },
    { "time": 4.0, "pitch": 50, "duration": 2.0, "velocity": 85 },
    { "time": 4.0, "pitch": 55, "duration": 2.0, "velocity": 85 },
    { "time": 4.0, "pitch": 57, "duration": 2.0, "velocity": 80 },
    { "time": 4.0, "pitch": 62, "duration": 2.0, "velocity": 80 },
    { "time": 4.0, "pitch": 60, "duration": 2.0, "velocity": 75 },
    { "time": 6.0, "pitch": 52, "duration": 2.0, "velocity": 85 },
    { "time": 6.0, "pitch": 55, "duration": 2.0, "velocity": 85 },
    { "time": 6.0, "pitch": 59, "duration": 2.0, "velocity": 80 },
    { "time": 6.0, "pitch": 62, "duration": 2.0, "velocity": 80 },
    { "time": 6.0, "pitch": 66, "duration": 2.0, "velocity": 75 },
    { "time": 6.0, "pitch": 69, "duration": 2.0, "velocity": 70 }
  ]
}
```

> ⚠️ Le doc précise « 2 mesures par accord pour le couplet » mais le JSON fourni place chaque accord sur **2 beats** (boucle de 2 mesures). **À arbitrer : étendre chaque accord sur 8 beats (2 mesures) pour le couplet, ou garder la boucle JSON.**

## Automations (temps en beats)

| Moment | Paramètre | Points (breakpoints) | Effet |
| :--- | :--- | :--- | :--- |
| **Toute la chanson** | Cordes — Volume (Piste Lead/Mélodie, index 3) | `0.0→-∞dB`, `8.0→-12dB`, `16.0→-6dB` (linéaire) | Swell des cordes douces, emphase finale. |
| **Refrain + dernier refrain** | Voix — MDelay Mix | `0.0→5%`, `16.0→30%` | Slap 100 ms, espace du refrain. |
| **Tempo** | Automations par section | Voir BPM Map (72 → 98) | Montée en puissance de l'hymne. |

## Réglages Mix

| Piste | Vol | Pan | Notes |
| :--- | :--- | :--- | :--- |
| Drums | 0.80 | — | MCompressor light ; MReverb (Short) sur les claps |
| Basse | 0.80 | — | Basse acoustique (Surge XT) ; MEqualizer coupe le sub |
| Pads/Claviers | 0.75 | — | Guitare folk + piano (accords) ; MChorus à charger |
| Lead/Mélodie | 0.75 | — | Cordes douces, swell automatisé (volume) |
| Arp/Contrepoint | 0.70 | +0.20 | MPhaser + MDelay |
| Fx | 0.60 | −0.20 | MIDI (Surge XT) ; reverb + auto filter |
| Aux/synthé2 | 0.80 | — | Chœurs samplés ; MCharisma à charger |
| Voix | 0.90 (mix manuel) | — | MCompressor 3:1 + De-esser ; MDelay slap au refrain |

## Notes de production

- **Correction Gmaj9** (time 0.0) : la note supérieure 59 (B2, 3ce dupliquée, commentée « F# ») → **57 (A2)** : la 9te A manquait pour `Gmaj9 = G-B-D-F#-A`. Voicing final : 43-47-50-54-57 = G-B-D-F#-A ✓.
- **Correction D7sus4** (time 4.0) : deux notes hors accord — 54 (F#2) → **55 (G2, la sus4)** et 65 (F3) → **60 (C3, la 7e)** : `D7sus4 = D-G-A-C`. Voicing final : 50-55-57-62-60 = D-G-A-D-C ✓.
- **Cmaj7 vérifié** (time 2.0) : 48-52-55-59-64 = C-E-G-B-E ✓ (E dupliqué, valide).
- **Em11 vérifié** (time 6.0) : 52-55-59-62-66-69 = E-G-B-D-F#-A ✓.
- **Refrain (grille)** : `Am9` = A-C-E-G-B · `D13` = D-F#-A-C-E · `Gmaj7` = G-B-D-F# · `E7b9` = E-G#-B-D-F — modulation pour la montée. Voicings à poser comme le motif couplet (2 beats par accord, boucle 2 mesures).
- **2 mesures par accord** : voir avertissement du JSON — à arbitrer avant l'arrangement.
- **Chœurs samplés** (ooh/ahh) sur Aux/synthé2 (index 6, piste MIDI) ; MCharisma à charger.
- **Fx en MIDI** (Surge XT) : textures/risers — la piste Fx reste MIDI.
- **Meldaproduction absents du template** → à charger : MChorus, MFlanger, MReverb, MCharisma, MDeEsser, MDelay (slap).
- **Voix baryton** (David, E3-B3, pitch 64-71) : parlé-chanté, mélodie dans la tessiture prévue.
- ⏳ **À valider : adaptation de la tonalité si la mélodie sort de la tessiture.**

## Intégration MCP

Indices **0-based** (0 = Drums, 1 = Basse, 2 = Pads/Claviers, 3 = Lead/Mélodie, 4 = Arp/Contrepoint, 5 = Fx, 6 = Aux/synthé2, 7 = Voix). Temps des notes en **beats**.

1. **Tempo** : `set_tempo(72)` (intro → pont) ; `set_tempo(98)` (dernier refrain).
2. **Intro** : `create_clip(2, 0, 8)` (fingerpicking guitare, motif Hymne arpégé) ; `add_notes_to_clip(2, 0, notes)` avec le JSON A.
3. **Couplets** : `create_clip(2, 0, 32)` puis `add_notes_to_clip(2, 0, notes)` (accords Hymne corrigés) ; `create_clip(1, 0, 32)` + `add_notes_to_clip(1, 0, notes)` (basse acoustique) ; `create_clip(0, 0, 32)` + `add_notes_to_clip(0, 0, notes)` (shaker/cajón).
4. **Refrains** : `create_clip(2, 1, 32)` + `add_notes_to_clip(2, 1, notes)` (accords Am9-D13-Gmaj7-E7b9) ; chœurs via `create_clip(6, 0, 32)` + `add_notes_to_clip(6, 0, notes)`.
5. **Pont** : `create_clip(3, 0, 32)` + `add_notes_to_clip(3, 0, notes)` (cordes douces, swell) ; `create_clip(4, 0, 32)` (contrepoint).
6. **Outro** : voix a cappella enregistrée sur la piste 7 (audio).
7. **Automations** : `set_automation_curve(track_index, clip_index, target, points, is_arrangement=True)` avec les breakpoints ci-dessus (volume cordes et MDelay Mix en beats).

## Paroles
Voir `PAROLES.md` dans ce dossier.
