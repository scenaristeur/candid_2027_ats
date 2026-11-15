# 05 — Rue de la Loi

**Tempo**: 140 BPM (couplet reggae) → 150 BPM (refrain punk)
**Tonalité**: Do mineur (Cm) → Mib majeur (Eb) sur le refrain
**Durée**: ≈ 2:50 (100 barres, forme classique complète)
**Atmosphère**: Ska → punk, rébellion, tension de rue
**Style**: Hommage The Clash + Téléphone
**Voix**: Baryton parlé grave et menaçant en couplet (type Sting baryton) → hurlé en refrain

## Hommage
- The Clash : ska → punk, rythmes reggae, rage politique
- Téléphone : énergie française, refrains fédérateurs
- Contemporain (2026) : piano Wurly staccato, auto-filter en « gate », basse dub qui groovy

## Structure (en barres)
Riff (4) | Couplet ska (16) | Pré-refrain (8) | Refrain punk (12) | Bridge

## Grille d'accords

| Section | Grille (4 mesures) | Couleur / Sonorité |
| :--- | :--- | :--- |
| **Couplet** | `| Cm | Bb | G | Cm |` (avec silences) | Ska : les silences font le groove, la basse répond. |
| **Refrain** | `| Ab | Bb | Cm | G |` (attaque franche) | Montée Ab → G : l'explosion punk du refrain. |

## Instruments (Ableton)

| Piste | Son | Effets | Rôle |
| :--- | :--- | :--- | :--- |
| **Guitare** | Électrique (croches ska) | Auto-Filter en « gate » | Le « skank » : attaque sèche coupée net. |
| **Piano Wurly** | Piano électrique | Staccato | Accents rythmiques du ska, côté Clash. |
| **Basse** | Basse reggae | Distorsion qui double au refrain | Répond aux silences, groove dub. |
| **Batterie** | Kit ska → punk | Grosse caisse hors du 1er temps | Le décalage reggae, puis la machine punk. |
| **Voix** | Baryton | Delay 1/4 pointé (couplet) | Parlé grave, menaçant, puis hurlé. |

### Maquette MIDI — chaînes réelles (août 2026)

| Piste | Index | Instrument | Chaîne FX |
| :--- | :--- | :--- | :--- |
| **Guitare** | 0 | `Guitar Electric Muted` | Auto Filter (band-pass, reso 0.4, drive 0.2, env gate) |
| **Batterie** | 1 | `Dry Session Kit` | Warmth 35, Drive 18, Master Comp 30 |
| **Basse** | 4 | `Electric Bass Raw` | Saturator (Bass Shaper, drive 0.35) → Compressor (RMS, ratio 0.6) |
| **Guide Voix** | 5 | `Surge XT` (patch Vocal Lead, play_mode 4) | Compressor → Delay 1/4 pointé (6 sixteenths, feedback 0.4) |
| **Piano Wurly** | 6 | `E-Piano Wurli` | Chorus-Ensemble (ensemble, dry/wet 0.35) → Compressor |

> **Piste Guide Voix** : monitoring Off + input « No Input ». **Piège Surge XT** : `play_mode 5` (Mono single trigger & legato) laisse une note fantôme → bourdon continu. Toujours `play_mode 4` (Mono single trigger & fingered portamento) = silencieux au repos.

## La Voix Baryton — Ligne de chant

- **Couplet** : parlé grave et menaçant, type Sting baryton — les mots comptent, posés sur le groove reggae.
- **Pré-refrain** : l'énergie monte, la voix se tend (« Le bruit des sirènes est ma seule prière »).
- **Refrain** : hurlé — le contraste extrême parlé/hurlé est le cœur du morceau.
- **Bridge** : « La loi, c'est nous maintenant ! » — puissance totale, fédératrice.

## La Chaîne Vocale Ableton

- **Micro** : SM7B.
- **Chaîne** : EQ8 (coupe 80 Hz, boost 2 kHz pour la diction) → Compresseur Glue 3:1 (attack 10 ms) → **Delay 1/4 pointé** synchronisé au tempo reggae (140 BPM) sur le couplet.

## Automations de Scène (à dessiner au mixage)

| Moment | Automation | Effet produit |
| :--- | :--- | :--- |
| **Couplet** | Delay voix en 1/4 pointé synchronisé au tempo reggae | L'écho ska/reggae, l'espace de la rue. |
| **Refrain** | Distorsion de la basse qui double | La basse prend le feu en même temps que la voix. |

## 6 bis. État de la maquette MIDI + Automations à faire au mixage

> **Statut (août 2026) :** maquette MIDI **finalisée** — 5 scènes en Vue Session, arrangement + mix terminés (104 barres, 140 BPM, 7 pistes). Les automations ci-dessous seront appliquées à l'étape de mixage final, une fois l'audio réel enregistré.

### Scènes créées (slot 0-4)

| Slot | Section | Longueur (beats) | Notes |
| :--- | :--- | :--- | :--- |
| 0 | **Riff** | 16 | Skank + one-drop, pose le thème |
| 1 | **Couplet ska** | 64 | Ska, silences, basse dub qui répond |
| 2 | **Pré-refrain** | 32 | Montée, la voix se tend |
| 3 | **Refrain punk** | 48 | Power chords, 4/4 punk, basse distordue |
| 4 | **Bridge** | 32 | Demi-temps, « La loi c'est nous » |

### Arrangement (barres, 0-based)

**Forme classique complète** (validée) : Riff 0-4 | Couplet 4-20 | Pré-ref 20-28 | Refrain 28-40 | Couplet 40-56 | Pré-ref 56-64 | Refrain 64-76 | Bridge 76-84 | Refrain final 84-96 | Outro apothéose 96-104.

| Barre | Section | Notes |
| :--- | :--- | :--- |
| 0 | Riff | 4 pistes instrus |
| 4 | Couplet 1 | 5 pistes, voix entre |
| 20 | Pré-refrain 1 | |
| 28 | Refrain punk 1 | |
| 40 | Couplet 2 | |
| 56 | Pré-refrain 2 | |
| 64 | Refrain punk 2 | |
| 76 | Bridge | demi-temps |
| 84 | Refrain final | |
| 96 | Outro apothéose | 2× riff (32 beats), tous les instrus, apothéose |
| 96 | Outro skank | rejoue le Riff, s'éteint sur le skank |

> **Piège API** : `duplicate_clip_to_arrangement(destination_bar=N)` est décalé d'une mesure (`(N-1)*4` beats). Utiliser `duplicate_to_arrangement(destination_time=beats)` — documenté dans AGENTS.md.

### To-do automations (au mixage)

| # | Moment | Action | Paramètre | Cible |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Couplet | Delay voix 1/4 pointé synchro reggae | B-Delay → Tempo/Feedback | Retour B / Voix |
| 2 | Refrain | Distorsion basse qui double | Distorsion → Drive | Piste Basse |

## Production Notes

- Le changement de tempo 140 → 150 BPM se fait au refrain : la bascule ska → punk.
- Grosse caisse hors du 1er temps : la marque du reggae, le contraste avec le punk.
- Les silences du couplet font le groove — la basse et le piano répondent aux vides.

## Notes live (set)

- Pic d'énergie de la partie punk, enchaîne sur « Décharges ».
- Le contraste parlé/hurlé est le moment fort : le public attend l'explosion du refrain.
- Visuel murs de briques, graffitis, néons.

## Paroles
Voir `PAROLES.md` dans ce dossier.
