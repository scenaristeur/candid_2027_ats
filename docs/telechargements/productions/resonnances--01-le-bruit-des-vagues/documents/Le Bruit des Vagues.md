# 01 — Le Bruit des Vagues

**Tempo**: 110 BPM (swing 8e)
**Tonalité**: Ré mineur (Dm) avec emprunts phrygiens (Eb)
**Durée**: ≈ 2 min (56 barres — estimé)
**Atmosphère**: Incantatoire, psychédélique, spoken word
**Style**: Hommage Pink Floyd + The Doors
**Voix**: Baryton parlé / murmuré (Mi2 → Si2) — pas de chant, juste *poser* la voix comme un acteur

## Hommage
- Pink Floyd : nappes, filtres qui s'ouvrent, production atmosphérique
- The Doors : spoken word, orgue Farfisa, côté « incantation » psychédélique
- Contemporain (2026) : pad Wavetable « Glass », delay ping-pong, côté cinématique

## Structure (en barres)
Intro (8) | Couplet parlé (16) | Montée (8) | Explosion instrumentale (16) | Outro (8)

## Grille d'accords

| Section | Grille (4 mesures) | Couleur / Sonorité |
| :--- | :--- | :--- |
| **Couplet** | `| Dm | Bb | C | Dm |` | Mineur sombre ; le Bb (VI) apporte la lumière phrygienne. |
| **Montée** | `| F | Eb | Bb | Dm |` | Le Eb (II phrygien) crée l'étrangeté et prépare l'explosion. |

## Instruments (Ableton)

| Piste | Son | Devices | Rôle |
| :--- | :--- | :--- | :--- |
| **Pad Wavetable** | « Sea Pad » (Wavetable) | WavePos 45, FiltreEnv 55, Pulse 35, Space 85, Reverb Hall 55% | Nappe de fond permanente. |
| **Orgue Farfisa** | Surge XT → Drawbar Organ 2 | Filter cutoff 2 kHz, Saturator SoftSine sur Guitare + Utility | Collision avec le pad — couleur « Doors ». |
| **Batterie** | Bonzo Kit (toms graves) | Compressor RMS 4:1, Attack 5ms | Roulements de toms, groove dépouillé. |
| **Guitare** | Guitar Electric Clean | Delay ping-pong 1/4, Saturator AnalogClip Drive 0.35, Utility | Motifs éthérés qui rebondissent. |
| **Basse** | Basic Sub Sine | OverTone 75, Tone 85, Distort 40, Attack 5, Release 40, Utility Gain | Pédale de Dm, harmoniques + présence. |
| **Master** | — | Limiter TruePeak, Ceiling −0.5 dB, Input Gain 0.72 | Niveau commercial −0.3 dBFS.

## La Voix Baryton — Ligne de chant

- **Mode** : spoken word / murmuré. Pose la voix comme un acteur, pas besoin de chanter.
- **Tessiture** : Mi2 → Si2 — le grave de confort absolu. Le texte est *posé*, à mi-voix, très collé au micro.
- **Montée** : la voix reste grave mais l'énergie monte — le texte devient pressant (« tout va basculer »).
- **Outro** : parlé-soufflé, encore plus grave, presque un souffle.

## La Chaîne Vocale Ableton

- **Micro** : SM7B collé aux lèvres — le souffle fait partie du son.
- **Chaîne** : EQ8 (coupe 80 Hz, léger boost 160 Hz) → Compresseur Glue 3:1 (attack 10 ms) → léger Saturator (couleur « tube »). Aucune ambiance sur le couplet : la voix est sèche et intime.

## État de la maquette — août 2026

> **Statut :** MAQUETTE MIDI TERMINÉE + **MIX RÉÉQUILIBRÉ** (août 2026). Arrangement construit, voix enregistrée (3 clips audio sur la piste Voix). Mix final couplet : RMS 0.27 / DR 11.4 dB / centroid 713 Hz / Sub+Basse 54%. Limiter master True Peak −1 dB. Automations ci-dessous restent à dessiner à la main (API Python non fiable pour les enveloppes d'arrangement).

### Vérification session (août 2026 — état réel MCP)

| Piste | Nom session | Volume | Clips session (slots 0-4) | Arrangement (224 beats = 56 barres) | État |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | Pad | 0.74 | Intro Pad (32) · Couplet (64) · Montée (32) · Explosion (64) · Outro (32) | 5 clips continus 0→224 | **FROZEN** (CPU) |
| 1 | Orgue | 0.53 | Intro Orgue (32) · Couplet (64) · Montée (32) · Explosion (64) · Outro (32) | 5 clips continus 0→224 | — |
| 2 | Voix | 0.82 | **Audio enregistré** : c1 (64) · montee2 (32) · outro (32) | 3 clips audio | — |
| 3 | Guitare | 0.85 | Couplet (64) · Montée (32) · Explosion (64) · Outro (32) — **pas d'Intro** | 4 clips 32→224 | — |
| 4 | Basse | 0.72 | Couplet (64) · Montée (32) · Explosion (64) · Outro (32) — **pas d'Intro** | 4 clips 32→224 | — |
| 5 | Drums Bongo | 0.60 | Intro Toms (32) · Couplet (64) · Montée (32) · Explosion (64) · Outro (32) | 5 clips continus 0→224 | **FROZEN** (CPU) |
| 6 | Vagues | 0.35 | Vagues Océan (64) | 1 clip | **FROZEN** (CPU) |
| Master | Master | 0.75 | Limiter True Peak (Ceiling −1 dB, Threshold 0.9) | — | — |

Notes de vérification :
- **Guitare et Basse n'ont volontairement pas de clip d'Intro** (8 barres) : l'Intro ne joue que Pad + Orgue + Toms, comme prévu à la fiche. Elles entrent au Couplet (beat 32).
- **Sends (A-Reverb, B-Delay) = 0 sur toutes les pistes** — les retours existent mais ne sont pas routés sur la maquette MIDI (à faire au mixage, idem automations).
- L'Intro Toms (pitch 36 kick, 40 toms bas, 43/45 toms) utilise des vélocités 82-120 avec roulements croissants jusqu'au beat 31 → effet tribale.
- Les sends pourront être branchés au mixage pour la Reverb Hall « Pink Floyd » (to-do #4).

### Devices chargés par piste

| Piste | Devices ajoutés |
| :--- | :--- |
| Pad | Sea Pad + Reverb Hall (Decay 0.65s, Wet 55%, Room Size 0.85, Chorus on) + **Auto Filter HPF ~200 Hz** — FROZEN |
| Orgue | Surge XT Drawbar Organ 2 + Utility Gain + **Auto Filter HPF ~200 Hz** |
| Voix | **Focusrite Red 2 EQ** (HiMidGain 0.67 ≈ +1 dB @ ~2.4 kHz) + Red 3 Compressor + Auto Shift + Saturator + Reverb + Utility |
| Guitare | Guitar Electric Clean + Delay ping-pong 1/4 + Utility + Saturator AnalogClip + **Auto Filter HPF ~200 Hz** |
| Basse | Basic Sub Sine (D1–B1, 37–62 Hz) + Utility + Saturator **Medium Curve** (Drive 0.67, Dry/Wet 0.30, Output 0.30) |
| Drums | Bonzo Kit + Compressor (RMS, Ratio ~4:1, Attack ~5 ms) + **Auto Filter HPF ~60 Hz** — FROZEN |
| Vagues | Surge XT + **Auto Filter HPF ~200 Hz** — FROZEN |
| Master | Limiter TruePeak (Ceiling −1 dB, Threshold 0.9) |

### Mixage — rééquilibrage multi-support (août 2026)

Objectif : basse abyssale mais pas écrasante, voix audible, bonne écoute sur tout support (enceintes, smartphone, radio).

**Résultats mesurés (capture couplet beat 56, répartition par bandes STFT n_fft=4096) :**

| Bande | Départ | Final |
| :--- | :--- | :--- |
| Sub (20-60 Hz) | 38% | **21.6%** |
| Basse (60-150 Hz) | 32% | **32.5%** |
| Body (150-400 Hz) | 15% | **25.9%** |
| Bas-méd (400-800 Hz) | 11% | **15.0%** |
| Méd+Présence (0.8-5 kHz) | 3% | **4.0%** |
| Sub+Basse total | 70% | **54%** |
| RMS / DR | 0.32 / 9.9 dB | **0.27 / 11.4 dB** |
| Spectral centroid | ~560 Hz | **713 Hz** |

**Actions appliquées :**
- **HPF Auto Filter** (High-pass, LFO/Env off) : **Pad, Orgue, Guitare, Vagues ~200 Hz** (freq 0.33), **Drums ~60 Hz** (freq 0.16) — dégraisse le bas du spectre des nappes pour laisser la basse respirer.
- **Basse** : Saturator Medium Curve, Drive 0.67, Dry/Wet 0.30, **Output 0.45 → 0.30**, fader 0.85 → **0.72**. Le sub est D1–B1 (37-62 Hz) : vérifié en solo, il reste **98% sous 150 Hz** → sur smartphone il ne s'entend que comme un *sub-thump* (limite physique, acceptée — pas de couche octave).
- **Voix** : HiMid +1 dB @ ~2.4 kHz (Red 2 EQ), fader 0.85 → **0.82** — clarté sans montée de niveau.
- **Master** : Limiter True Peak, **Ceiling −0.5 dB → −1 dB**, Threshold 0.9, Input Gain à l'unité.
- **Freeze** Pad, Drums, Vagues (CPU Saturé pendant les captures Surge XT).

**Notes multi-support** : audibles sur smartphone — Voix (claire), Orgue, Pad, Guitare, Vagues. En partie seulement — Basse (thump), Drums/Toms (attaque, sub perdu). ~4% de l'énergie > 0.8 kHz : le morceau sonne plus faible/creux sur téléphone que sur enceintes, la voix reste la plus claire.

**Explosion** : section d'impact, sub-lourde (Sub 42-70% selon le moment du build-up — le sub vient du sine de basse, pas des Drums). Le HPF 60 Hz des Drums a nettoyé le sub des toms.

### To-do automations (mix terminé — à dessiner à la main)

| # | Moment | Action | Cible |
| :--- | :--- | :--- | :--- |
| 1 | Entrée de la Montée | HPF qui s'ouvre brutalement (100 Hz → 20 Hz) | Pad / Master |
| 2 | Dernier mot « basculer » | Reverb voix → 80% wet | Piste Voix |
| 3 | Tout le morceau | LFO lent sur filtre du Sea Pad (ouverture cyclique) | Piste Pad |
| 4 | Tout le morceau | Reverb hall sur drums (ambiance Pink Floyd) | Piste Drums |
| 5 | Tout le morceau | Delay ping-pong guitare (déjà en place) | Piste Guitare |

## Production Notes

- Pas de caisse claire — la batterie vit sur les toms graves et les roulements.
- Le swing 8e groove sur la nappe ; la voix *parle par-dessus* le groove, sans s'y coller.
- L'emprunt phrygien (Eb) est la marque de fabrique de l'incantation.

## Notes live (set)

- Titre d'ouverture : le groupe entre sur la nappe, lumière verte, laser.
- La voix parle dans le silence — le public écoute, c'est l'appel.
- Transition sans blanc vers « Marteau-Pilon » via le drone d'orgue.

## Paroles
Voir `PAROLES.md` dans ce dossier.
