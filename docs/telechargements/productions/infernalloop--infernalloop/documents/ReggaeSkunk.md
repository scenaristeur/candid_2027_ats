# Fiche technique — « Un jour avec les oiseaux »

> Projet Ableton (Live 12 Lite). Titre de travail partagé avec le projet InfernalLoop.
> Fiche de production / mix. Mise à jour : 2026-08-08.

---

## Identité du morceau

| Champ | Valeur |
| :--- | :--- |
| **Titre** | Un jour avec les oiseaux |
| **Tempo** | 100 BPM (fixed) |
| **Signature** | 4/4 |
| **Tonalité** | Do majeur relatif (progression I–vi–IV–V) |
| **Progression** | **C — Am — F — G** (1 mesure par accord, boucle) |
| **Durée arrangement** | 224 temps = **56 mesures** |
| **Pistes MIDI** | 8 |
| **Returns** | 2 (A-Reverb, B-Delay) |

---

## Architecture (arrangement, 56 mesures)

| Temps (beats) | Section | Mesures | Caractère |
| :--- | :--- | :--- | :--- |
| 0–16 | **L'Aube** | 4 | Piano C→G tenu, Lead oiseau s'éveille seul, pas de batterie |
| 16–32 | **La Forêt** | 4 | Dialogue Lead/Alto/Tenor, bass+batterie légères, pad posé |
| 32–48 | **La Danse** | 4 | Groove skank reggae |
| 48–64 | **La Funk** | 4 | Funk, guitare wah |
| 64–80 | **La Danse (2)** | 4 | Rappel du groove (corps dansant) |
| 80–96 | **La Funk (2)** | 4 | Rappel funk |
| 96–160 | **Le Chœur** | 16 | **Cœur** : chorale complète 8 pistes + brass, 4 sous-sections |
| 160–176 | **Le Vol** | 4 | Climax, **kick 4-on-the-floor** |
| 176–192 | **Le Vol (2)** | 4 | Climax prolongé, 4-on-the-floor |
| 192–208 | **Le Couchant** | 4 | Décroissance, tenues longues |
| 208–224 | **La Nuit** | 4 | Résolution, un dernier chirp du Lead |

Le Chœur (96–160) se décompose lui-même en 4 sections de 4 mesures : calme → éveil → pic → retour au calme.

---

## Pistes & instruments

| Track (0-based) | Nom | Instrument | Rôle |
| :--- | :--- | :--- | :--- |
| 0 | 1-Grand Piano | Grand Piano (rack) + Chorus + Reverb + Delay | Basse + piano (fondation) |
| 1 | 2-Viral Kit | Viral Kit | Batterie |
| 2 | skank | Surge XT (inst 0) | Pad / skank orgue |
| 3 | 4-Funk Guitar | Surge XT (inst 1) | Guitare wah-wah funk |
| 4 | 5-Birds | Surge XT (inst 2) | Lead oiseau (chant) |
| 5 | 6-Birds Alto | Surge XT (inst 3) | Oiseau alto |
| 6 | 7-Birds Tenor | Surge XT (inst 4) | Oiseau ténor |
| 7 | 8-Brass Trumpet | Surge XT (inst 5) | **Trompette (dialogue avec la chorale)** |

**Mapping Surge XT (OSC) :**

| Instance | Ports OSC | Track | Patch |
| :--- | :--- | :--- | :--- |
| 0 | 53280/53281 | 2 (skank) | Pad |
| 1 | 53282/53283 | 3 (Funk Guitar) | Wah Guitar |
| 2 | 53284/53285 | 4 (Lead Bird) | Bird Chirp 2 |
| 3 | 53286/53287 | 5 (Alto) | Bird Chirp 1 |
| 4 | 53288/53289 | 6 (Tenor) | Bird Chirp 3 |
| 5 | 53290/53291 | 7 (Brass Trumpet) | Miles Trumpet |

---

## Chaînes de traitement (mix appliqué)

| Track | Devices (ordre) | Réglages clés |
| :--- | :--- | :--- |
| **0 Basse/Piano** | Grand Piano, Chorus, Reverb, Delay, **EQ Three**, **Saturator** | EQ: GainMid **1.0** (boost médium). Saturator: Type **Medium Curve**, Drive **0.65**, Dry/Wet **0.75** (harmoniques pour petits HP). Vol 0.727 |
| **1 Batterie** | Viral Kit, **EQ Three** | EQ: GainLo **0.7** (coupe bas). Vol **0.85** |
| **2 skank (Pad)** | Surge XT, **EQ Three** | EQ: GainLo **0.5** (éclaircit le grave), GainMid **0.95**. Vol **0.42** |
| **3 Funk Guitar** | Surge XT | Vol 0.75. Wah réduit (2.5 Hz @ 45 %), osc Twist, drive ~0.85 |
| **4 Lead Bird** | Surge XT, **Reverb**, **EQ Three** | Reverb: Dry/Wet **0.20**, Room Size **0.45**. EQ: GainHi **0.55** (coupe stridence). Vol **0.60** |
| **5 Alto** | Surge XT, **EQ Three** | EQ: GainHi **0.6**. Vol **0.68** |
| **6 Tenor** | Surge XT, **EQ Three** | EQ: GainHi **0.6**. Vol **0.60** |
| **7 Brass** | Surge XT (Miles Trumpet) | Filtre ouvert (cutoff 0.6 ≈ 1.2 kHz), amp 0 dB, global 0 dB. Vol **0.55**. Places du Chœur (beat 96) |
| **Master** | **Compressor**, **Limiter**, **Utility** | Compressor glue: Thresh **0.7** / Ratio **0.4** / Release **0.3**. Limiter: Mode **True Peak**, Lookahead **3 ms**, Ceiling **0.95**, Input Gain **0.5**. Utility: neutre (Output 0). Fader master **1.0** |

---

## Validation externe (captures VB-Cable)

### Volume balancing — captures solo (Chœur, beat 100)

| Piste | RMS solo | Centroid | Ajustement |
| :--- | :--- | :--- | :--- |
| 0 Basse/Piano | 0.183 | 347 Hz | — |
| 1 Batterie | 0.057 | 3206 Hz | ↑ (sous-estimé en solo, bon en contexte) |
| 2 Pad | 0.206 | 241 Hz | ↓ 0.55→0.42 |
| 3 Guitare | 0.021 | 3914 Hz | — |
| 4 Lead Bird | 0.105 | 3210 Hz | — |
| 5 Alto | 0.032 | 3925 Hz | ↑ 0.675→0.78 |
| 6 Tenor | 0.043 | 4104 Hz | ↑ 0.585→0.70 |
| 7 Brass (filtre fermé) | 0.079 | 2965 Hz | **problème : filtre 101 Hz** |
| 7 Brass (filtre ouvert) | 0.162 | 866 Hz | ✓ audible, redressé |

**Piège brass** : le patch Miles Trumpet charge **filtre passe-bas fermé à ~101 Hz** (cutoff 0.27) → quasi muet (-35 dB). Fix : ouvrir le cutoff à 0.6 (≈1.2 kHz). Vérifier toujours le cutoff des patchs Surge lors du chargement.

### Captures globales (mastered)

| Section | RMS | Centroid | DR | Notes |
| :--- | :--- | :--- | :--- | :--- |
| Chœur | 0.140 | 2380 Hz | 17.1 | ✓ rééquilibré |
| Le Vol | 0.160 | 1537 Hz | 15.9 | coup 4-temps appliqué |
| La Danse | 0.189 | 1179 Hz | 14.5 | ✓ riche |
| Vol 4-temps | 0.160 | 1537 Hz | 15.9 | beat house |
| Chœur + brass (final) | 0.139 | 1862 Hz | 17.2 | ✓ médium rééquilibré, oiseaux adoucis |

**Avant mix** : Chœur centroid global **2881 Hz** (aigu, creux au médium).
**Après mix** : Chœur **1862–2380 Hz**, sections groove **1179–1537 Hz**. Le médium est rééquilibré.

---

## Découvertes techniques (à réutiliser)

- **Oiseaux très aigus** (Lead 3210 / Alto 3925 / Tenor 4104 Hz) : pour rééquilibrer, couper le bas du pad + booster le médium de la basse plutôt que d'éteindre les oiseaux (le chant EST la mélodie).
- **Adoucir les piaillements** : baisser le volume des pistes oiseaux + **couper les aigus** (EQ Three GainHi ↓ 0.55-0.6) pour enlever la stridence sans perdre la présence (GainMid flat 0.85).
- **Batterie sous-estimée en solo** (RMS 0.057) : ne pas sur-corer sur un relevé solo, vérifier en contexte de mix global.
- **Kick 4-on-the-floor ClubHouse** : ajouter un kick sur les temps 2&4 (vel ~82 vs 100 sur 1&3) au-dessus d'un groove funk = effet disco instantané sans réécrire le pattern.
- **Patch Surge fermé à l'entrée** : certains patchs (Miles Trumpet) chargent avec un **filtre passe-bas très bas (~101 Hz)** → quasi inaudible. Toujours lire `/param/a/filter/1/cutoff` au chargement et l'ouvrir.
- **Écrêtage master** : l'indicateur + dB au master = niveau d'entrée (somme des pistes avant le limiter). Réduire le niveau des pistes chaudes (brass) plutôt que le limiter/fader ; remettre la chaîne pro après ajustement.
- **Chaîne master Live Lite** : Compressor glue (0.7/0.4/0.3) → Limiter True Peak (3 ms, 0.95, Input 0.5) → fader 1.0. Baisse le centroid sans perdre l'énergie.

---

## Reste à faire (TODO)

- [x] **Dialogue instru/chorale** : trompette (Miles Trumpet, instance 5 / piste 8) qui répond à la chorale d'oiseaux dans le **Chœur** (beats 96–160).
- [ ] (Option) Étendre le dialogue brass à **La Forêt** et **Le Vol** — clips session déjà créés (slot 2 & 6), restent à placer dans l'arrangement.
- [ ] Automations sur les effets (à faire à l'oreille par David).
- [ ] Écoute finale de validation sur grosses enceintes + téléphone.
- [ ] (Option) Export WAV 48 kHz / 24 bits → MP3 320 kbps.

---

## Communication oiseaux–brass (dialogue)

**Principe** : sur la progression C-Am-F-G, la trompette (registre médium C4–G5, MIDI 60-79) « répond » aux chirps des oiseaux (aigus 76-91). Les oiseaux chantent, le cuivre répond dans un registre plus grave et rond — une sorte de conversation / appel-réponse.

**Clip « Choir Brass » (64 temps)** — 4 sous-sections calées sur celles du Chœur :
- Mes 1-4 (calme) : le brass entre subtilement, une tenue par mesure (C4-C G4-...)
- Mes 5-8 (éveil) : phrases de 2-3 notes qui répondent aux gazouillis
- Mes 9-12 (pic) : brass + oiseaux en contrepoint animé, montées (jusqu'à G5-D6)
- Mes 13-16 (retour au calme) : tenues longues, le brass se retire

**Réglages brass utiles** :
- Filtre 1&2 cutoff **0.6** (~1.2 kHz) — sinon quasi muet
- Amp `a/amp/volume` **1.0**, global **1.0**
- Volume piste **0.55** (bien audible, ne sabote pas le master)
- Niveau solo : RMS 0.162, centroid 866 Hz (après ouverture du filtre)
