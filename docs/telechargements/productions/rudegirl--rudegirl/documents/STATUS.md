# RudeGirl — STATUS.md

**Date :** 2026-08-01
**Version :** v1.0 (mix rééquilibré, Fill transposé d'une octave)

---

## Vue d'ensemble

| Métrique | Valeur |
|---|---|
| Style | Black & Roll / Punk Rock |
| Tempo | 150 BPM |
| Mesure | 4/4 |
| Tonalité | C#m |
| Durée arrangement | ~2:33 (384 beats / 96 bars) |
| Pistes utilisées | 8/8 (Live Lite max) |

---

## Structure Arrangement

| Section | Bars | Beats | Description |
|---|---|---|---|
| Intro | 0-16 | 4 | Toutes pistes, riff C#5 power chord |
| Couplet 1 | 16-48 | 8 | Voix + instr complètes |
| Refrain 1 | 48-80 | 8 | F#m → C#m → A → B |
| Couplet 2 | 80-112 | 8 | Voix + instr |
| Refrain 2 | 112-144 | 8 | Refrain identique |
| Pont | 144-160 | 4 | A→A→E→E, respiration |
| Solo | 160-192 | 8 | Lead Surge XT + Stabs |
| Refrain 3 | 192-224 | 8 | |
| Section extended | 224-288 | 16 | SoloDéch + Damage |
| Refrain 4 | 288-320 | 8 | |
| Outro | 320-336 | 4 | Fade out riff + cymbales |
| Extra | 336-384 | 12 | Matériel supplémentaire |

---

## Pistes & Dispositifs

| # | Nom | Type | Instr/Device | FX |
|---|---|---|---|---|
| 0 | 1-Drums | MIDI | Gen Purpose Kit | Compressor |
| 1 | 2-Bass | MIDI | Surge XT | Saturator |
| 2 | 3-Audio | Audio | — | Compressor → Channel EQ → Limiter |
| 3 | 4-FX | MIDI | Surge XT (choeur/pad) | MEqualizer (HPF 200 Hz) |
| 4 | 5-GuitarRythm | MIDI | Surge XT | Saturator |
| 5 | 6-GuitarLead | MIDI | Surge XT (solo) | Reverb |
| 6 | 7-Fill | MIDI | Surge XT (stabs) | MEqualizer (HPF 200 Hz) |
| 7 | 8-Extra | MIDI | Surge XT (damage FX) | MEqualizer (HPF 200 Hz) |

**Master :** Maximizer (Limiter) — Input Gain 0.25, Output 0.85, Threshold 0.97, Mode True Peak

---

## Analyse Notes MIDI

### 1-Drums (Couplet, d-beat)
- Kick (36) : 1, 1.5, 3.5, 4, 4.5, 7.5 — vélocités 95-110 ✅
- Snare (38) : 2, 6 — vel 105 ✅
- HH (42) : croches continues — vel 75-80 ✅

### 2-Bass (Couplet, 32b)
- 8 mesures : C#2 (37) → E2 (40) → A2 (45) → B2 (47), croches 8e
- Vélocités 85-100, pattern 16th + finale longue ✅

### 5-GuitarRythm (Couplet, 32b)
- Power chords par accords : C#3/G#3 → E2/A2 → E3/B2 → F#3/B2
- Motif : noire + 2 croches, vélocités 85-100 ✅

### 6-GuitarLead (Solo, 32b)
- Bluesy C#m : E3(52), F#3(54), G#3(56), A3(57), B3(59), C#4(61)
- Phrasé varié, bends/tenues, vélocités 85-100 ✅

### 4-FX (Choeur Intro)
- 2 notes longues : C#2(37) + F#3(44), 16 beats ✅

### 7-Fill (Stabs Intro, transposé +12)
- C#3(49)→**C#4(61)** sur contre-temps (1.5, 3.0, 4.5...), vel 75-100 ✅
- Couplet/Refrain : E2→E3(52), A2→A3(57), C#3→C#4(61), B2→B3(59) ✅

### 8-Extra (Damage Intro)
- Crescendo C#2(37) : vel 40 → 100 sur 8 notes ✅

**Verdict :** Construction MIDI solide — d-beat punk, power chords, stabs, crescendos. Vélocités bien variées.

---

## Analyse Audio — Full Mix v1 → v2 (intro, 20s)

| Métrique | v1 | v2 | Cible | Verdict |
|---|---|---|---|---|
| **Energy RMS** | 0.40 | 0.28 | 0.15-0.25 | ⚠️ Amélioré, encore un peu chaud |
| **Dynamic Range** | 7.9 dB | **11.1 dB** | 10-15 dB | ✅ Corrigé |
| **Spectral Centroid** | 923 Hz | 1230 Hz | 700-900 Hz | ⚠️ Plus brillant (HPF + moins de distorsion limiter) |
| **Spectral Rolloff** | 1660 Hz | 2621 Hz | 1200-2500 Hz | ⚠️ Léger |
| **Key détectée** | F min | **C# min** | C#m | ✅ Confirme la tonalité |

## Analyse Voix (3-Audio, solo)

**Tessiture chantée :** profil spectral = voix masculine grave, centroid ~540 Hz, rolloff ~925 Hz, ZCR 0.024.
Chroma dominant : G 13% / G# 12% / F# 10% / A 10% → notes de la gamme C#m, centrée ~F#3-G#3.
Cohérent avec la tessiture E3-B3 de David.

| Métrique | Avant | Après | Verdict |
|---|---|---|---|
| **Energy RMS** | 0.524 | 0.486 | ✅ Moins chaud |
| **Dynamic Range** | 5.6 dB | 6.3 dB | ⚠️ Encore compressée |
| **Spectral Centroid** | 538 Hz | 536 Hz | ✅ Inchangé |
| **Respiration audible** | Oui (Makeup ON + Limiter 0.75) | Masquée (HPF 120 Hz + Makeup OFF + Limiter 0.50) | ✅ Traitée |

**Chaîne voix finale :** Compressor (Threshold 0.40, Makeup OFF, Model Expand) → Channel EQ → Limiter (Input Gain 0.50) → **MEqualizer (HPF ~120 Hz)**

---

## Corrections Appliquées (session actuelle)

### Mix
1. ✅ Master Limiter : Input Gain 0.55→**0.25**, Output 1.0→**0.85** (DR 7.9→11.1 dB)
2. ✅ Master volume : 0.85→**0.78**
3. ✅ MEqualizer chargé + **HPF 200 Hz** sur 4-FX, 7-Fill, 8-Extra (MeldaProduction, pas d'EQ Eight en Live Lite)
4. ✅ Refrain allégé : 6-GuitarLead 0.75→**0.60**, 8-Extra 0.78→**0.60**, 4-FX 0.85→**0.65**
5. ✅ Voix 3-Audio : MEqualizer bande 2 = **notch Bell 50 Hz** (Q 0.85) — non retenu (voix à réenregistrer), bande 1 = HPF 120 Hz confirmé

### Volumes finaux (analyse solo par instrument)
| Piste | Avant | Après | Verdict solo |
|---|---|---|---|
| 1-Drums | 0.91 | 0.91 | RMS 0.22 / DR 13.2 ✅ |
| 2-Bass | 0.70 | **0.42** | RMS 0.49→équilibré (écrasait le mix, DR 6.2) |
| 5-GuitarRythm | 0.55 | **0.30** | RMS 0.51→équilibré (Saturator très chaude) |
| 4-FX | 0.75 | **0.65** | RMS 0.21 / DR 13.7 ✅ |
| 6-GuitarLead | 0.60 | 0.60 | RMS 0.21 / DR 13.5 ✅ |
| 7-Fill | 0.60 | 0.60 | RMS 0.046→**0.063** après transposition |
| 8-Extra | 0.60 | 0.60 | RMS 0.12 / DR 18.6 (damage = normal) |

### 7-Fill transposé d'une octave (+12)
- **Problème :** stabs E2–C#3 (40–49) doublaient la basse → inaudibles, redondants
- **Fix :** tous les clips session + arrangement montés d'une octave (52/57/59/61/64...)
- **Découverte technique :** `set_arrangement_clip_notes` (via `clip.set_notes()`) **AJOUTE** les notes au lieu de les remplacer → les clips arrangement avaient doublé (ancienne + nouvelle octave). Corrigé en **supprimant les 11 clips arrangement et en les recréant** via `duplicate_to_arrangement` depuis les clips session (source correcte).

### Voix / Tessiture
4. ✅ Couplet 1 & 2 : C#3(49)→**E3(52)** — "T'arrives en", "T'as grandi dans"
5. ✅ Refrain : C#4(61)→**B3(59)** — "rien à perdre", "Le monde brûle"
6. ✅ Tessiture effective : **E3–B3** (52–59)
7. ✅ MEqualizer **HPF 120 Hz** sur la voix (coupe le souffle bas, garde le E3=165 Hz)
8. ✅ Compressor voix : Makeup ON→**OFF**, Threshold 0.25→**0.40** (les respirations tombent sous le seuil)
9. ✅ Limiter voix : Input Gain 0.75→**0.50** (moins d'amplification des silences)

---

## Problèmes Restants

### 1. Refrain encore dense (priorité moyenne)
- RMS 0.41→**0.367**, DR ~7.8→**8.7 dB** après équilibrage (cible 10-15)
- Mur du son à la source — acceptable pour du Black & Roll, mais surveiller
- **État :** volumes équilibrés (Bass 0.42, GuitarRythm 0.30, Lead 0.60, FX 0.65), Fill transposé ✅

### 2. Section par section (captures v3)
| Section | RMS | DR | Centroid | Verdict |
|---|---|---|---|---|
| Intro (0) | 0.251 | 12.0 | 1250 Hz | ✅ Dans la cible |
| Refrain (48) | 0.367 | 8.7 | 1193 Hz | ⚠️ Mur du son (genre) |
| Solo (160) | 0.310 | 10.2 | 1296 Hz | ✅ Quasi-cible |

### 3. Voix à ré-enregistrer ou supprimer (décision utilisateur)
- **Décision prise :** oublier le traitement du souffle, David réenregistrera (ou supprimera) la voix
- La chaîne voix corrigée (HPF 120 Hz + Compressor + Limiter) reste en place

### 4. Tuning offset étrange (-3637/-4521 cents)
- Artéfact librosa, pas un vrai problème

---

## A/B Multi-Support — Verdict & Idées en attente (non appliquées)

**Check effectué le 2026-08-01 — rien n'a été modifié, idées à décider plus tard.**

### Ce qui passe bien ✅
- **Bass Saturator** : Drive 0.65, Type Medium Curve (3), Dry/Wet 1.0 → harmoniques audibles sur téléphone (skill : 0.60-0.80, Medium Curve)
- **Drums Compressor** : Threshold 0.30, Attack 0.15, Model Peak, Makeup On → glue (skill : ~4:1, Peak)
- **HPF 200 Hz** sur 4-FX / 7-Fill / 8-Extra (MEqualizer)
- **DR 12 dB** (intro) → survit à la normalisation Spotify/YouTube
- **Master Maximizer** : Ceiling 0.94 (-0.5 dB), Mode True Peak

### Risques petit haut-parleur ⚠️
1. **Sends trop mouillés** :
   - 1-Drums B-Delay **0.59** → proposé 0.20
   - 5-GuitarRythm A-Reverb **0.46** → proposé 0.20
   - 7-Fill A-Reverb **1.00** → proposé 0.35
   - (Cible glue skill : 0.10-0.25)
   - Effet : queues reverb/delay lavent le médium sur téléphone/autoradio et ramollissent l'attaque punk
2. **Centroid 1193-1296 Hz** (cible 700-900) : brillant, peut être strident sur téléphone — à écouter, OK pour le genre

### Volumes — écart faders vs cibles enregistrées
- Faders réels : Drums 0.85, Bass **0.61**, Voix 0.85, FX 0.85, GuitarRythm **0.67**, Lead 0.84, Fill 0.85, Extra 0.68
- Mes cibles notées plus tôt : Bass 0.42, GuitarRythm 0.30, Lead 0.60, Fill 0.60, Extra 0.60 — **ne correspondent pas**
- Décision utilisateur : **garder l'état actuel**, mixer avec le rendu réel (les sections mesurent bien : intro RMS 0.251/DR 12.0)
- Si rééquilibrage voulu plus tard : refaire les captures solo aux volumes actuels avant

---

## Prochaines étapes suggérées

1. ~~Équilibrer le refrain~~ ✅ (Bass 0.42, GuitarRythm 0.30, Lead 0.60, FX 0.65, Fill 0.60) — vérifier à l'écoute
2. ~~Finaliser le volume master~~ ✅ (0.78, Input Gain 0.25, Output 0.85)
3. ~~Monter les stabs du Fill d'une octave~~ ✅ (session + arrangement recréés proprement)
4. **Ré-enregistrer la voix en E3-B3** (ou supprimer) — décision utilisateur
5. Automation (volume rides, sends FX)
6. **A/B multi-support** — verdict fait, ajustements sends en attente de décision (voir section A/B)
7. Export WAV 48kHz 24-bit → MP3 320k
