# La VM — FICHE TECHNIQUE

Reprise-parodie de « La Bohème » (Aznavour) sur le thème de la virtualisation.
Cette fiche décrit le set **tel qu'il est réellement dans Ableton**, pas tel qu'il a été rêvé au
départ. Les valeurs viennent de mesures sur les clips et sur les captures audio.

## En-tête

| | |
|---|---|
| **Tempo** | 112 BPM |
| **Tonalité** | La mineur |
| **Signature** | 4/4 |
| **Scènes** | 9 (S0 → S8), **120 mesures**, ≈ **4 min 17** |
| **Atmosphère** | Intro médiévale (générique de Kaamelott) → club/funk → retour médiéval |
| **Style** | Parodie rap/électro. Flow parlé à la Eminem, nappe fragile à la Agnes Obel, refrain fédérateur à la Imagine Dragons |
| **Voix** | Baryton, tessiture utile **E4–B4** (notes 64–71). Refrain « La VM la VM » sur A4–B4–A4–B4 |

### Convention de hauteur (Ableton)

**C3 = 60** (et non C4 = 60). Donc 60 = C3, 64 = E3, 69 = A3, 71 = B3, 81 = A4, 93 = A5.
La convention scientifique décale tout d'une octave — ne pas l'utiliser.

### Convention de vélocité

Les clips stockent les vélocités sur **l'échelle MIDI 0–127** (l'API ne connaît qu'elle).
Cette fiche les donne sur **0–100** (convention projet) : `fiche = MIDI × 100 / 127`.

---

## Structure

| Scène | Section | Mesures | Temps | Énergie |
|---|---|---|---|---|
| **S0** | Intro médiévale | 16 | 64 | Livre ouvert. Percussions médiévales, luth, chalumeau, bourdon |
| **S1** | Couplet 1 | 16 | 64 | Nu, intimiste. Flow parlé, kick discret, pad aérien |
| **S2** | Pré-refrain | 8 | 32 | Build-up. Filtre qui s'ouvre, riser |
| **S3** | Refrain | 16 | 64 | DROP funky. Tout le monde est là |
| **S4** | Couplet 2 | 16 | 64 | Groove installé, flow plus incisif |
| **S5** | Refrain 2 | 16 | 64 | idem S3 |
| **S6** | Pont | 8 | 32 | Break planant, retour au calme |
| **S7** | Refrain final | 16 | 64 | Double énergie |
| **S8** | Outro médiévale | 8 | 32 | Livre fermé. Écho de l'intro, cadence qui se pose sur un La |

⚠️ **Un écrasement a eu lieu** : des clips parasites avaient été écrits dans le slot S0, écrasant
l'intro. David les a supprimés, puis `1-Batterie`, `3-Pad` et `5-Médiéval` ont été réécrits.
Les 16 mesures sont là, et les percussions médiévales commencent **mesure 5** — c'est volontaire,
pas un trou.

---

## Grille d'accords

| Section | Accords (1 mesure chacun) | Notes réelles |
|---|---|---|
| Intro / Couplet | Am — F — C — G | A-C-E / F-A-C / C-E-G / G-B-D |
| Pré-refrain | Dm — Am — F — E7 | D-F-A / A-C-E / F-A-C / E-G#-B-D |
| Refrain | F — C — G — Am | F-A-C / C-E-G / G-B-D / A-C-E |
| Pont | Dm — Am — Bb — F | D-F-A / A-C-E / Bb-D-F / F-A-C |
| Outro | Am — F — C — G | A-C-E / F-A-C / C-E-G / G-B-D |

Vérifié contre les notes réelles des clips de pad : l'ensemble des hauteurs du pad du refrain
(43–65) couvre exactement F, C, G et Am. Aucun accord mal nommé.

---

## Pistes

| # | Nom | Moteur | Volume | Chaîne |
|---|---|---|---|---|
| 0 | `1-Batterie` | Gotta Feel Kit (Drum Rack, kit `.adg`) | 0.792 | — |
| 1 | `2-Basse` | Analog Bass (natif) | 0.792 | — |
| 2 | `3-Pad` | Classic Ensemble Pad (natif) | 0.792 | — |
| 3 | `4-Lead` | House Stab (natif) | 0.560 | — |
| 4 | `5-Médiéval` | **Surge XT** (patch Dual, voir plus bas) | 0.792 | — |
| 5 | `6-FX` | Riser Basic (`.adg`, catégorie Sounds › Effects) | 0.465 | — |
| 6 | `7-Voix` | **audio** | 0.850 | MAutoPitch → Focusrite Red 2 EQ → Focusrite Red 3 Compressor |
| 7 | `8-Résample` | — | 0.850 | vide (soupape de sécurité) |

Volumes sur l'échelle normalisée d'Ableton : **0.85 = unité (0 dB)**, 1.0 = +6 dB.

### 5-Médiéval — patch Surge XT

Mode **Dual** (`/param/global/scene_mode` = 2, adresse **globale**). Séparation des deux timbres
**par la vélocité** :

- **Scène A — Chalumeau** (vélocité haute) : Bagpipes. osc1 Twist 0 dB, osc3 −31 dB, rm1x2 0.046,
  noise 0.25. Filtres `FX Comb+` @682.5 Hz et 125 Hz, résonance 70 %, feedback 50 %.
  EG A 19.8 ms / D 83.6 ms / S 70 % / R 423 ms. amp 0.216.
- **Scène B — Luth / Hammered Dulcimer** (vélocité basse) : osc1 muet, osc2 et osc3 à 1.0
  (unison 50 %), rm1x2 0.05, noise 0.45. Filtre1 HP OB-Xd @80 Hz, filtre2 LP OB-Xd @15 kHz,
  waveshaper « Asymmetric » drive 0.55, amp 1.0.

Modulations : `vel` → `/param/a/amp/volume` (+0.110) et `/param/b/amp/volume` (−0.30) — c'est ce
qui crée le split. `a/vlfo_1/0` → `/param/a/osc/1/pitch` 0.02. `macro_1` → `/param/a/filter/1/cutoff` 0.25.

⚠️ `surge_load_patch` n'écrit **que dans la scène A** et remet `scene_mode` à 0 : reposer 2 après
chaque chargement de patch.

### 7-Voix — chaîne vocale

| # | Device | Réglages |
|---|---|---|
| 0 | **MAutoPitch** (Melda) | Gamme **La mineur** (A B C D E F G actives, les 5 dièses OFF) · Depth 1.0 · Speed 0.85 · Keep formants 1.0 · Dry/Wet 1.0 · Detune 0.5 |
| 1 | **Focusrite Red 2 EQ** | HiPass 0.50 · LowShelf (0.55 / 0.42) · LowMid (0.30 / 0.40 / Q 0.50) · HiMid (0.60 / 0.62 / Q 0.50) · HiShelf (0.70 / 0.58) · LowPass 1.00 · Gain 0.50 |
| 2 | **Focusrite Red 3 Compressor** | Threshold 0.95 · Ratio 0.30 · Attack 0.50 · Release 0.23 (AutoRelease ON) · MakeUpGain 0.33 · Blend 1.0 |

**Effet mesuré de l'EQ** sur la voix (avant → après) :

| Bande | Delta |
|---|---|
| 20–80 Hz | −11.8 dB |
| 80–150 Hz | −6.2 dB |
| 150–300 Hz | −3.0 dB |
| 800–1500 Hz | +2.0 dB |
| 1500–3000 Hz | +4.6 dB |
| 3000–6000 Hz | +6.2 dB |
| 6000–14000 Hz | +4.7 dB |

**Effet mesuré du compresseur** : dynamique (écart-type du niveau / tranches de 0.2 s)
**6.9 dB → 5.1 dB**, niveau global restauré par le make-up.

⚠️ Le **seuil du Red 3 est piégeux** : à 0.50 il écrase la voix de **17 dB**. Il faut monter à
**0.95** pour n'obtenir plus que ≈ 4 dB de réduction. Le make-up est tout aussi raide :
0.50 = **+9.5 dB**.

La prise voix brute était **très sombre** : toute l'énergie sous 500 Hz, rapport formante/grave
à −10 dB. D'où le dégraissage du grave et la poussée de présence.

---

## Clips

Nommage : le clip du slot `S n` porte le nom `S(n+1) …` (convention projet, 1-based dans le nom).

| Piste | S0 | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 |
|---|---|---|---|---|---|---|---|---|---|
| Batterie | `S1 PercMed16M` | `S2 Groove16M` | `S3 PreRefrain` | `S4 Refrain` | `S5 Couplet2` | `S6 Refrain2` | `S7 Pont` | `S8 RefrainFinal` | `S9 PercOutro` |
| Basse | — | `S2 Groove16M` | `S3 PreRefrain` | `S4 Refrain` | `S5 Couplet2` | `S6 Refrain2` | `S7 Pont` | `S8 RefrainFinal` | — |
| Pad | `S1 Bourdon16M` | `S2 Groove16M` | `S3 PreRefrain` | `S4 Refrain` | `S5 Couplet2` | `S6 Refrain2` | `S7 Pont` | `S8 RefrainFinal` | `S9 BourdonOutro` |
| Lead | — | `S2 Groove16M` | `S3 PreRefrain` | `S4 Refrain` | `S5 Couplet2` | `S6 Refrain2` | `S7 Pont` | `S8 RefrainFinal` | — |
| Médiéval | `S1 Medieval16M` | — | — | — | — | — | — | — | `S9 MedievalOutro` |
| FX | `FX Intro Riser` | — | `FX Riser PreRefrain` | — | `FX Riser Refrain2` | — | `FX Riser Pont` | — | — |
| Voix | — | `la vm` | — | — | — | — | — | — | — |

### Contenu par clip

| Clip | Long. | Notes | Hauteurs | Vélocités | Contenu |
|---|---|---|---|---|---|
| `S1 PercMed16M` | 64 t | 154 | 37, 39, 41 | 51–87 | Percussion médiévale : rim 37 sur contretemps, tambourin 39 en croches, bodhrán 41 sur temps 1 et 3 (mesures 5–15) |
| `S2 Groove16M` (batterie) | 64 t | 476 | 36, 37, 39, 42 | 31–88 | Kick 36, rim 37, clap 39, hat 42. Couplet dépouillé : **pas** de congas |
| `S2 Groove16M` (basse) | 64 t | 144 | 41–55 | 46–87 | Basse funky |
| `S2 Groove16M` (pad) | 64 t | 64 | 65–84 | 60–63 | Voicings Am F C G à l'octave haute |
| `S2 Groove16M` (lead) | 64 t | 72 | 77–88 | 43 | **Lead volontairement effacé** dans le couplet (vélocité 43) |
| `S3 PreRefrain` (batterie) | 32 t | 238 | 36, 39, 42, 46, 70 | 43–87 | Charley qui s'accélère |
| `S3 PreRefrain` (basse) | 32 t | 80 | 53–71 | 75 | Dm Am F E7 |
| `S3 PreRefrain` (pad) | 32 t | 32 | 45–65 | 71 | idem |
| `S3 PreRefrain` (lead) | 32 t | 48 | 57–72 | 64–78 | Le lead **rentre** ici |
| `S4 Refrain` (batterie) | 64 t | 705 | 36,39,40,42,46,62,63,70 | 51–98 | **Congas 62/63** : c'est le refrain qui est « club », pas le couplet. Boom 808 (pad 40) au temps 1 |
| `S4 Refrain` (basse) | 64 t | 256 | 43–60 | 83 | F C G Am |
| `S4 Refrain` (pad) | 64 t | 64 | 43–65 | 79 | idem à l'octave basse |
| `S4 Refrain` (lead) | 64 t | 114 | 65–76 | 68–74 | Hook « La VM » |
| `S5 Couplet2` (batterie) | 64 t | 532 | 36,39,41,42,46,62,63,70 | 30–85 | |
| `S5 Couplet2` (basse) | 64 t | 256 | 43–64 | 79 | |
| `S5 Couplet2` (pad) | 64 t | 64 | 43–65 | 75 | |
| `S5 Couplet2` (lead) | 64 t | 101 | 57–76 | 45–56 | Très effacé (couplet) |
| `S6 Refrain2` | 64 t | 709 (bat.) | — | 55–98 | |
| `S7 Pont` (batterie) | 32 t | 100 | 36, 39, 42, 70 | 43–79 | Break |
| `S7 Pont` (basse) | 32 t | 32 | 45–60 | 67 | Dm Am Bb F |
| `S7 Pont` (pad) | 32 t | 56 | 45–65 | 75 | |
| `S7 Pont` (lead) | 32 t | 26 | 72–82 | 75 | |
| `S8 RefrainFinal` | 64 t | 725 (bat.) | 36,39,40,41,42,46,**49**,62,63,70 | 59–98 | |
| `S1 Medieval16M` | 64 t | 178 | 64–93 | 33 / 93 | **Luth v33** (arpèges 16èmes, mesures 1–4 et 9–12) + **chalumeau v93** (thème, mesures 5–8 et tenues 13–16). Groove « Swing 16ths 66 » |
| `S9 MedievalOutro` | 32 t | 69 | 64–88 | 20–82 | Luth en fondu (v42→20) + cadence chalumeau **A4-G4-F4-E4-A4**. Groove « Swing 16ths 66 » |
| `S9 PercOutro` | 32 t | 38 | 37, 39, 41 | 19–46 | Percussion médiévale qui s'éteint |
| `S9 BourdonOutro` | 32 t | 16 | 45, 52 | 22–54 | Bourdon La + Mi qui décroît |
| FX risers | 64/32 t | 1 note | 60 | 100 | **Une seule note tenue** : le `.adg` fait le balayage lui-même. Monter de 4 mesures |
| Voix `la vm` | 96 t | audio | — | — | Prise voix de David |

Le clip de batterie du refrain final contient en plus la note **49**, absente des autres refrains.

---

## Réglages de mix

Mesuré sur les WAV de capture (recalculés à la main, **pas** lus dans la réponse de l'outil).

| Section | RMS | Pic | Crête | Écrêtés |
|---|---|---|---|---|
| Intro | 0.069 | 0.729 | 20.5 dB | 0 |
| Couplet | 0.133 | 0.816 | 15.8 dB | 0 |
| Pré-refrain | 0.109 | 0.851 | 17.9 dB | 0 |
| Refrain final | 0.158 | **0.936** | 15.5 dB | 0 |
| Outro | 0.063 | 0.337 | 14.5 dB | 0 |

Arc dynamique : l'intro et l'outro sont **≈ 10 dB sous** le refrain final.

### Master

| # | Device | Réglages |
|---|---|---|
| 0 | Compressor (glue) | Threshold 0.40 · Ratio 0.70 · Attack 0.40 · Release 0.30 |
| 1 | **Limiter** (true peak) | Mode **True Peak** · Lookahead **3 ms** · Ceiling **0.95** |

Fader master : **0.85**. C'est l'unité (0 dB) dans cette installation ; **1.0 = +6 dB** et, comme
le fader est *après* les inserts, monter à 1.0 casse le plafond et écrête (mesuré : 196 échantillons
écrêtés contre 0). Pour gagner du niveau, on remonte **les pistes**, pas le master.

---

## Notes de production

### Ce qui a été mesuré, pas supposé

- **Les couplets n'ont ni congas ni shaker** — seulement kick, rim, clap, hat. Le côté « club » vient
  des refrains (congas 62/63, boom 808). Un allègement des couplets a donc été tenté et s'est révélé
  **sans effet** : le groove que David aime était déjà intact.
- **Le « riser » de la piste FX est muet pendant un moment** : le Simpler de `6-FX` était vide, les
  66 notes écrites ne produisaient rien. Réparé en chargeant `Riser Basic` et en remplaçant les
  16èmes par **une note tenue**.
- **L'outil `capture_and_analyze` peut renvoyer des chiffres périmés.** Sur un WAV totalement muet
  il a annoncé `rms=0.3397` — deux fois la valeur identique à la 15e décimale. **Le WAV fait foi** :
  recalculer soi-même.

### Problème ouvert : le nasillard du chalumeau

Le chalumeau (scène A de Surge) nasille. Cause identifiée : **deux filtres `FX Comb+` à ≈ 99 % de
résonance**. Correction appliquée : résonance 75 %, feedback 50 %, pitch master remis à 0.00 st
(il était à +0.86 st). Mesuré : le rapport formante/grave passe de **+35.4 dB à −0.37 dB**.

**Décision de David : laisser ainsi pour l'instant**, y revenir après le premix. Options restantes :
résonance à 75 %, jouer sur `filter/balance`, le `feedback`, ou un cut correctif 700–1100 Hz.

### Décisions prises

- **Surge XT est réservé au timbre médiéval** (`5-Médiéval`). Partout ailleurs, natif.
- **Le refrain n'est pas touché par l'allègement** — c'est lui qui porte le contraste avec les couplets.
- **Le lead est volontairement effacé dans les couplets** (vélocité 43) pour laisser le flow respirer.
- **La voix à +3.5 dB devant les instruments.** Le gain s'est logé surtout dans le 150–500 Hz
  (+2.3 / +2.6 dB) plutôt que dans la présence (+1.4 dB) — c'est ce qui la rend présente, mais c'est
  aussi la zone qui peut rendre le mix pâteux. Si un jour ça sonne épais : recouper le 150–400 Hz
  de la voix et monter la présence à la place.

### Ce qui reste à faire

- **Voix** : enregistrée sur le **couplet 1 seulement**. Pré-refrain, refrains et pont sont nus.
- **Le nasillard du chalumeau** (voir plus haut).
- **Vérifier la traduction** — cible : grosse sono avec caisson **et** téléphone.
