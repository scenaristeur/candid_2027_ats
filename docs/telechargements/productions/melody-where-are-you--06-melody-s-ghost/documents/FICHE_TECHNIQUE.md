# 06 — Melody's Ghost

**Tempo**: 120 BPM
**Tonalité**: Fa# mineur (F#m) — notes réelles F#m9 / C#m7(b5) / Bm9 / E13(sus4)
**Signature**: 4/4
**Durée**: ≈ 7 min (arrangement 0-424 beats → ~90 mesures, loop 0-368)
**Atmosphère**: Ballade sombre, mélancolie assumée, recueillement
**Style**: Pink Floyd (« Wish You Were Here ») + Portishead + trip-hop
**Voix**: Baryton, douce narrative flottant sur la 9ème/11ème, plus lyrique au refrain

> **NOTE** : version reconstruite (2026-08-17) — abandon de Analog Lab, tout en **Surge XT (moteur pur) + effets MeldaProduction (natif/Melda)**. CPU optimisé (~46% en jeu, ~12% au repos). Adaptité pour smartphone + grosses enceintes.

## Hommage
- Pink Floyd : lead spectral sur le pont, nappes, résolutions retardées
- Melody Nelson : l'écharpe écarlate, l'absence
- Portishead / trip-hop : atmosphère nocturne, groove vif

## Structure (vue arrangement, beats)
Intro (0-16) | Couplet 1 (16-80) | Refrain (80-112) | Couplet 2 (112-176) | Refrain 2 (176-256) | Pont/lead guitar (192-256) | Couplet (256-304) | Refrain final (304-368+)

- Leads guitar ne jouent que sur **mesures 49-64 (beats 192-256)**, le pont spectral
- Voix sur toute la longueur (clip audio 0-302)

## Grille d'accords (réelle, notes playback)

| Section | Grille | Couleur / Sonorité |
| :--- | :--- | :--- |
| **Couplet** | `\| F#m9 \| C#m7(b5) \| Bm9 \| E13(sus4) \|` | C#m7(b5) = naufrage, mélancolie intime |
| **Refrain** | `\| A9 \| E/G# \| F#m11 \| D9/F# \|` | A9 lumineux, D9/F# suspense douce-amère |
| **Pont (lead)** | lead spectral sur F#m/A colours | le lead perce le tissu sombre |

## Pistes (ordre session) — reconstruction

| Piste | Moteur | Patch | Pan | Vol | Chaîne FX |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Pads** | Surge XT | **`Organ 1`** (poly **8**) | 0 | 0.70 | MSaturator (léger) → MCharmVerb (reverb) |
| **Bass** | Surge XT | `Sub Square` | 0 | 0.78 | MEqualizer (HPF ~45Hz) ; sends reverb 0.57 + delay 0.41 |
| **Vocal** | audio | — | 0 | 0.85 | MEqualizer (HPF 85 + présence + air) → MCompressor ; send reverb 0.25 |
| **Guitar** | Surge XT | lead (pont) | **+0.3** | 0.52 | MEqualizer (présence) → MDelay ; send reverb 0.25 + delay 0.15 |
| **Texture** | Surge XT | `melody's ghost` | **-0.3** | 0.58 | MEqualizer (carve ~500Hz) ; sends reverb 0.68 + delay 1.0 |
| **Drums** | Tamuz Kit (+ MidiPitcher -12) | — | 0 | 0.88 | MCharmVerb (ambiance 0.15) |
| **Vocal Dbl** | audio (doublure voix) | — | **+0.105 R** | 0.73 | *(aucun device)* — contrebalance le lead |

**Retours** : A-Reverb (0.85), B-Delay (0.85). **Master** : MCompressor (glue) → Limiter (True Peak, Ceiling ~-1dB, Lookahead 3ms).

## Batterie — humanisation (workflow session → arrangement)

- Les clips drums vivent **en arrangement** (session vidées puis workflow par scènes).
- Clips session clés sur Drums :
  - scène 3 = `ancien refrain` (mécanique, référence)
  - **scène 6 = `refrain vivant`** (humanisé : vélocités variables kick + micro-décalages)
  - **scène 7 = `refrain vivant2`** (calme→fourni, **retenu** : refrain + pont)
- **Refrain (80-112) et pont (192-256) ×2 = `refrain vivant2`** — le pattern qui colle à la voix.
- ⚠️ **contre-temps** : tout espacement/cre-scendo improvisé (kick spirse, `pont narrac cresc`) crée un faux contre-temps. **Réutiliser les patterns vivants existants**, ne pas en inventer.

## Optimisations CPU (leçon clé)

- **Surge XT = lourd** ; les patches orgue riches (`House Organ`) saturaient à ~100% en jeu. **`Organ 1` (plus léger) + poly 8/6** → ~40-46% en jeu, plus de « tonnerre »/dropouts.
- Le CPU global ne permet pas d'isoler une piste au repos (bruité ±5pts) ; mesurer **en jeu en solo** pour cibler le couplable.
- Réduire les **FX internes Surge** : passer `fx/chain_bypass` à **3 (All FX Off)** puis **vider les slots** (type=0) — sinon EQ/DLY/PH reviennent au reload du patch.
- **Abandon de Analog Lab / Surge FX Effects** au profit de Surge (moteur) + **Melda** pour les effets.

## Paroles
Voir `PAROLES.md` dans ce dossier.
