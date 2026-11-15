# FICHE TECHNIQUE — DoubleDubbyDub

## En-tête

| Champ | Valeur |
|---|---|
| Tempo | 88 BPM |
| Tonalité | Fa majeur / ré mineur (double lecture), avec Bb et Gm |
| Signature | 4/4 |
| Durée | 89 mesures = 356 temps = **4 min 03 s** |
| Style | Reggae dub roots politique — révolte lycéenne |
| Voix | Baryton, E3–B3 (MIDI 64–71, C3 = 60) |
| Dossier | `sources/ReggaeDubLive/04-DoubleDubbyDub/` |

---

## Structure

| # | Section | Mesures | Temps | Énergie |
|---|---|---|---|---|
| 1 | Intro | 8 | 32 | Basse + batterie, puis orgue, puis skank |
| 2 | Couplet 1 | 13 | 52 | Riddim complet sans cuivres |
| 3 | Refrain 1 | 8 | 32 | Cuivres + caisse claire |
| 4 | Couplet 2 | 13 | 52 | Riddim, texte « double peine » |
| 5 | Refrain 2 | 8 | 32 | Full |
| 6 | Pont | 5 | 20 | Dub, trou, **silence d'or** à la mesure 5 |
| 7 | Refrain final | 21 | 84 | **Climax — point d'or** |
| 8 | Outro | 13 | 52 | Fade, delay |

**Total : 89 mesures** (Fibonacci).

### Nombre d'or

- Le refrain final commence à la **mesure 56** : 55 / 89 = **0,618**.
- Le refrain final est le plus grand bloc : **21 mesures** (Fibonacci).
- Suite des sections : 8-13-8-13-8-5-21-13.
- Réverb : **Decay Time = 0,618**. Delay : **Filter Freq = 0,618**.

---

## Grille d'accords

| Accord | Notes réelles (C3 = 60) |
|---|---|
| F | F–A–C (65–69–72) |
| Dm | D–F–A (62–65–69) |
| Bb | Bb–D–F (58–62–65) à l'orgue ; F–Bb–D (65–70–74) au skank |
| C | C–E–G (60–64–67) |
| Gm | G–Bb–D (67–70–74) |

**Couplet (13 mes.) :** F | Dm | Bb | C | F | Dm | Bb | C | Gm | Bb | F | C | C

**Refrain (8 mes.) :** F | C | Dm | Bb | F | C | Bb | C

**Pont (5 mes.) :** Dm | Bb | F | C | C (la mesure 5 est un silence)

**Refrain final (21 mes.) :** refrain 8 mes. ×2 (16 mes.) + tag F | C | Dm | Bb | C

**Outro (13 mes.) :** F | Dm | Bb | C ×3 + F

---

## Pistes

| Index | Nom | Moteur | Patch | Pan | Volume | Chaîne FX | Sends A / B |
|---|---|---|---|---|---|---|---|
| 0 | `1-Basse` | Surge XT | **Attacky** (osc octave -1) | 0 | 0.85 | Saturator → Compressor | 0 / 0 |
| 1 | `2-Batterie` | Drum Rack | **505 Core Kit** | 0 | 0.85 | Compressor → Utility | 0.10 / 0.04 |
| 2 | `3-Orgue` | Surge XT | **Hammond's Hall** | 0 | **0.78** | Auto Filter ×2 → EQ Three | 0.15 / 0.32 |
| 3 | `4-Cuivres` | Instrument Rack | **Alpha Brass Affair** | 0 | **0.70** | Auto Filter | 0.22 / 0.22 |
| 4 | `5-Skank` | Instrument Rack | **Guitar Electric Muted** | 0 | **0.70** | Auto Filter → Utility | 0.10 / 0.28 |
| 5 | `6-Guide voix` | Instrument Rack | **E-Piano Light** | 0 | 0.60 | aucun | 0.10 / 0.05 (sortie **Ext. Out**) |
| 6 | `7-Voix` | Audio | — (micro) | 0 | 0.85 | EQ Three → Compressor → Reverb | 0.15 / 0.12 |
| 7 | `8-Percs/FX` | Drum Rack | **Percussion Core Kit** | 0 | **0.60** | **Utility (Output 0.45)** | 0 / 0 |

### Réglages des devices

**Basse — Saturator** : Type `Bass Shaper`, Drive 0.38, Dry/Wet 0.38, Output 1.00.
**Basse — Compressor** : Threshold 0.72, Ratio 0.62, Attack 0.28, Release 0.22, Output 0.08.
**Batterie — Compressor** : Threshold 0.70, Ratio 0.62, Attack 0.18, Release 0.16, Output 0.10.
**Batterie — Utility** : Output 0.55 (compense le niveau bas du kit 505).
**Orgue — Auto Filter** : Low-pass, Frequency 0.88, Resonance 0.05, Drive 0.08.
**Cuivres — Auto Filter** : High-pass, Frequency 0.24, Resonance 0.05, Drive 0.05.
**Skank — Auto Filter** : High-pass, Frequency 0.30, Resonance 0.06, Drive 0.10.
**Skank — Utility** : Output 0.40, Stereo Width 0.85, Bass Mono On, Bass Freq 0.25.

### Batterie — mapping des pads utilisés

| Note | Pad | Réglage |
|---|---|---|
| 36 | Bassdrum | Tune 56, Decay 55, Level 116 |
| 37 | Rimshot | Tune 64 |
| 38 | Snaredrum | Tune 60, Decay 45, Level 110 |
| 40 | Conga Lo | Level 108 |
| 43 | Conga Hi | Tune 66, Level 98 |
| 46 | Open Hi Hat | Level 100 |
| 49 | Crash | Level 108 |
| 50 | Hi Cowbell | Level 96 |
| 51 | Ride | Level 96 |

---

## Clips

Tous les clips portent le nom de leur scène. Longueurs en **temps (beats)**.

| Scène | Nom | Longueur | Contenu |
|---|---|---|---|
| 1 | `S1 Intro` | 32 temps (8 mes.) | Batterie sparse 4 mes., full 4 mes. ; orgue à partir de la mes. 5 ; skank à partir de la mes. 7 |
| 2 | `S2 Couplet 1` | 52 temps (13 mes.) | Basse, batterie, orgue, skank. Pas de cuivres |
| 3 | `S3 Refrain 1` | 32 temps (8 mes.) | + cuivres, caisse claire sur le 3, crash |
| 4 | `S4 Couplet 2` | 52 temps (13 mes.) | Identique au couplet 1 |
| 5 | `S5 Refrain 2` | 32 temps (8 mes.) | Identique au refrain 1 |
| 6 | `S6 Pont` | 20 temps (5 mes.) | Batterie sparse 2 mes., full 2 mes., silence mes. 5 |
| 7 | `S7 Refrain final` | 84 temps (21 mes.) | Refrain ×2 + tag, fills de toms toutes les 8 mes., crash tous les 4 mes., **ride 51 sur les contretemps et cowbell 50 tous les 4 mes.** |
| 8 | `S8 Outro` | 52 temps (13 mes.) | Full 8 mes., sparse 5 mes., cuivres 6 mes. |

### Guide voix

La piste `6-Guide voix` (index 5) porte la mélodie de référence, jouée par **E-Piano Light**.
Elle est routée en **Ext. Out 1/2**, donc elle contourne le master (Compressor + Limiter) : c'est
une piste de travail, pas une piste de mix. Elle n'apparaît pas dans le rendu final.

| Scène | Clip | Longueur | Contenu |
|---|---|---|---|
| 2 | `Guide - Couplet 1` | 52 temps | 6 phrases, une note par syllabe |
| 3 | `Guide - Refrain 1` | 32 temps | 4 phrases |
| 4 | `Guide - Couplet 2` | 52 temps | 6 phrases |
| 5 | `Guide - Refrain 2` | 32 temps | 4 phrases |
| 6 | `Guide - Pont` | 20 temps | 4 phrases parlées, 1 mesure de silence |
| 7 | `Guide - Refrain final` | 84 temps | 8 phrases + tag « debout » |
| 8 | `Guide - Outro` | 52 temps | 2 phrases puis silence |

Tessiture du guide : **E3–A3 (64–69)**, la zone confortable de David. Le guide est volontairement
au même octave que la voix : on peut le baisser ou le couper, il ne sert qu'à la répétition.

### Percussions — `8-Percs/FX`

Kit **Percussion Core Kit** (Drum Rack), volume **1.00 + Utility Output 0.45**.
⚠️ Le kit est **très discret** à l'unité : sans le Utility, la piste est inaudible dans le mix.
Pads utilisés :

| Note | Pad | Rôle |
|---|---|---|
| 37 | Wood Claves | intro, mesures 1–4 |
| 42 | Shake Cabasa Short | **shaker, contretemps (0.5 / 1.5 / 2.5 / 3.5), vélocité 127** |
| 48 | Tamb | backbeat, temps 2 et 4 |
| 39 | Cowbell Simple | « and » de 4, toutes les 4 mesures du final |

⚠️ **Le Shaker Egg (pad 41) a été retiré.** Mesuré seul : **RMS 0.037 à vélocité 127**, contre
0.059 pour les claves et 0.063 pour la cabasa — il est trop fin et disparaît derrière le bas-médium.
La **cabasa (42)** le remplace : même famille de shaker, plus de corps et de présence. Si David veut
le timbre exact de l'œuf, il faudra remonter le volume du pad 41 dans l'interface ou charger un
autre échantillon sur ce pad.

**Mesures après le reset Voicemeeter (13/11/2026) :** couplet RMS 0.194 / centroïde 1 718 Hz ;
final 0.209 / **2 427 Hz** ; perc seule 0.056 / 4 677 Hz. La cabasa est présente à ~−11 dB sous le
mix. Si c'est trop brillant, baisser le Utility de 0.45 à 0.30.

Shaker et tamb s'arrêtent à la mesure 5 du pont (silence d'or) et à la mesure 9 de l'outro.
Le shaker est plus fort au final (vélocité 72) qu'au couplet (50).

### Contre-chant de cuivres

Le clip `S7 Refrain final` de la piste `4-Cuivres` reçoit un riff de 2 mesures répété aux mesures
1, 5, 9, 13 et 17 du final :

- F : A–C–A–F (69–72–69–65) ;
- C : G–C–G–E (67–72–67–64).

Il répond à la voix sans ajouter de piste. 40 notes ajoutées.

**Scènes 14 à 16** : les trois scènes de départ de David, conservées comme référence. Elles
traversent maintenant la nouvelle chaîne de mix (sends et timbres), mais leur contenu MIDI est
inchangé.

---

## Réglages mix

| Élément | Valeur |
|---|---|
| Master | Volume 0.85, Compressor glue → Limiter |
| Master Compressor | Threshold 0.78, Ratio 0.55, Attack 0.30, Release 0.20, Output +1 dB |
| Master Limiter | Ceiling 0.95, Lookahead 3 ms, Mode True Peak, Release 0.50 |
| A-Reverb | Predelay 0.22, Decay Time 0.618, Room Size 0.55, Dry/Wet 1.00 |
| B-Delay | L/R 3/16, Ping Pong On, Feedback 0.52, Filter On, Filter Freq 0.618, Dry/Wet 1.00 |
| Orgue — high-pass | Auto Filter High-pass, Frequency 0.28 (~150 Hz), Resonance 0.05 |
| Basse — mono | Utility : Bass Mono On, Bass Freq 0.25 (~120 Hz), Output 0 |
| Skank — largeur | Utility : Stereo Width **1.0** |
| Groove | **Swing 16ths 66** assigné aux clips de skank, timing 100 |
| Percs — niveau | Track volume 0.71, Utility Output 0.45 (kit très faible à l'unité) |

⚠️ Le Groove Pool n'a pas de retrait scriptable (`clear_clip_groove` time out). Pour l'enlever :
clic droit sur le clip → **Remove Groove**, à la main.

Les sends sont **post-fader**. Le delay est donc plus fort quand l'orgue ou le skank jouent fort.

---

## Notes de production

- **La basse est écrite une octave plus bas que le riff d'origine.** Surge `Attacky` a `osc/1/octave = -1` :
  les notes écrites 43–65 sonnent 31–53. C'est ce qui donne le grave roots.
- **Le riff de basse est volontairement simple** : fondamentale sur le contretemps de 1, quinte sur
  le 3, retour à la fondamentale. Il laisse la place au kick et au delay.
- **La batterie est un one-drop** : kick sur le 3, rimshot sur le 3, caisse claire sur le 3 au
  refrain. Les congas 40/43 remplacent le charley régulier.
- **Le skank est une guitare électrique étouffée**, high-passée à 0.30, doublée sur les contretemps
  au refrain. C'est le « double » rythmique.
- **Les cuivres n'entrent qu'aux refrains** ; au couplet, ils laissent la place au texte.
- **Le pont est le seul endroit où la basse ne joue qu'une note** (mes. 1) puis se tait à la mes. 5 :
  c'est le silence d'or avant le refrain final.
- **Les scènes 14–16 sont la version d'origine** ; si un choix de timbre ne plaît pas, on peut y
  revenir pour comparer.

---

## Arrangement timeline

Les 8 scènes sont posées sur la timeline, dans l'ordre, sur **356 temps (89 mesures)**.

| Section | Début (0-based) | Début en temps | Longueur |
|---|---|---|---|
| S1 Intro | mesure 0 | 0 | 32 |
| S2 Couplet 1 | mesure 8 | 32 | 52 |
| S3 Refrain 1 | mesure 21 | 84 | 32 |
| S4 Couplet 2 | mesure 29 | 116 | 52 |
| S5 Refrain 2 | mesure 42 | 168 | 32 |
| S6 Pont | mesure 50 | 200 | 20 |
| S7 Refrain final | mesure 55 | 220 | 84 |
| S8 Outro | mesure 76 | 304 | 52 |

**Automation écrite :**

| Clip | Cible | Points |
|---|---|---|
| S1 Intro (orgue) | Auto Filter Frequency | 0.55 → 0.88 sur 32 temps |
| S1 Intro (orgue) | Send B | 0.10 → 0.15 |
| S6 Pont (orgue) | Auto Filter Frequency | 0.88 → 0.60 → 0.55 |
| S6 Pont (orgue) | Send B | 0.32 → 0.45 → 0.65 |
| S7 Final (orgue) | Auto Filter Frequency | 0.62 → 0.90 |
| S7 Final (orgue) | Send B | 0.65 → 0.40 → 0.35 |

⚠️ Les **cue points** ne sont pas créables via l'API (`Song.create_cue` absent). À poser à la main
aux mesures 0, 8, 21, 29, 42, 50, 55, 76.

**Vérification au playhead (13/11/2026) :** à la mesure 107 — et sur 104–109 battement par
battement — les valeurs sont **constantes** : filtre LP 0.88, filtre HP 0.28, send B 0.32,
volume 0.85. Il n'y a **aucun changement audible** à la mesure 107. Les seules variations sont
au pont et au final : send B **0.45 → 0.65** aux mesures 54–56, filtre **0.62** au début du final.
Le point visuel à 107 est un reste du clip de test (mesures 100–107), supprimé depuis ; il est
inaudible. Le lecteur d'enveloppes de l'API ne le voit pas — vérifier en lisant la valeur du
paramètre au playhead, pas avec `get_track_automation`.

## Voix — piste créée et configurée

La piste audio **`7-Voix`** (index 6) a été créée via `create_audio_track` (Remote Script patché
le 13/11/2026), puis configurée :

| Élément | Valeur |
|---|---|
| Type | Audio |
| Entrée | **Ext. In**, canal **1** (micro mono) |
| Monitoring | **Auto** (0 = In, 1 = Auto, 2 = Off) |
| Volume / Pan | **0.75** / 0 |
| Chaîne | **EQ Three → Compressor → Reverb (insert)** |
| Sends | A-Reverb 0.15 / B-Delay 0.12 |

Réglages des devices :

| Device | Paramètre | Valeur |
|---|---|---|
| EQ Three | GainLo | **0.45** |
| EQ Three | GainMid | **1.00** |
| EQ Three | GainHi | **1.00** |
| EQ Three | FreqHi | **0.45** (présence plus basse) |
| EQ Three | Slope | 24 dB/oct |
| Compressor | Threshold | **0.60** |
| Compressor | Ratio | **0.50** |
| Compressor | Attack | **0.10** |
| Compressor | Release | **0.18** |
| Compressor | Output | 0.05 |
| Reverb | Dry/Wet | **0.06** |
| Reverb | Room Size | 0.40 |
| Reverb | Decay Time | 0.40 |
| Reverb | Predelay | 0.22 |
| Reverb | Stereo Image | 0.65 |

### Prise maquette

Un seul clip audio : **`7-Voix 3`**, de 0 à **339,58 temps** (~85 mesures), **gain 0.70**,
warp off. C'est une maquette, pas une prise définitive.

| Section | Voix |
|---|---|
| Intro | souffle/ambiance (RMS 0.054) |
| Couplet 1 | chanté |
| Refrain 1 | chanté **sauf les premières mesures** (début manqué) |
| Couplet 2 | chanté |
| Refrain 2 | chanté |
| Pont | chanté |
| Final | chanté |
| Outro | chanté |

Mesures après calage : couplet RMS **0.258** / centroïde 1 362 Hz ; final 0.258 / 1 818 Hz.
Voix seule : **0.166** / 1 266 Hz. La voix est maintenant à ~−4 dB sous le mix, clairement devant,
et presque aussi claire que les instruments (1 266 Hz contre 1 362 Hz).

Pour la dégager, les instruments ont été creusés : **skank 0.70**, **cuivres 0.70**,
**orgue 0.78 + EQ Three mid 0.60**, **percs 0.60**. Le niveau de la maquette reste
**irrégulier** (couplet/final) : à lisser par automation de clip ou compression au mix final.

**Ce qui reste manuel :** armer la piste (bouton Arm) et refaire le début du refrain 1 si on veut
la version définitive. Pour la maquette, le trou peut rester un moment dub.

**Double du refrain final :** une deuxième prise avec 20 ms de décalage, pan légèrement à gauche.
**Harmonie :** à la tierce au-dessus sur « debout » (F→A, G→B, A→C).

## TODO — améliorations

- [x] **1. Arrangement 89 mesures + automation** — les 8 scènes sont posées sur la timeline
  (0–356 temps), avec automation du filtre orgue et du send B sur l'intro, le pont et le final.
  ⚠️ **Cue points abandonnés** : l'API ne peut pas les créer et David ne peut pas les poser.
- [x] **2. Voix réelle** — `6-Guide voix` prêt. Piste `7-Voix` configurée et **maquette
  enregistrée** (`7-Voix 3`, gain 0.70). Reste : refaire le début du refrain 1 et lisser le niveau.
- [ ] **2b. Double et harmonie du final** — deuxième prise de voix décalée de ~20 ms, pan légère,
  plus harmonie à la tierce sur « debout » (F→A, G→B, A→C).
- [x] **3. Percussions / FX** — piste `8-Percs/FX`, Percussion Core Kit : claves, shaker, tamb,
  cowbell. Volume 0.60 + Utility Output 0.45 ; shaker = **cabasa 42** (l'egg 41 est trop fin et
  a été retiré).
- [x] **4. Contre-chant de cuivres** — riff A–C–A–F / G–C–G–E, 5 occurrences dans le final.
- [x] **5. Traduction téléphone / FOH** — high-pass orgue ~150 Hz, basse mono sous ~120 Hz,
  skank largeur 1.0, sub déjà généré par le Saturator.
- [x] **6. Groove** — **Swing 16ths 66** sur le skank, **groove amount 0.60**. Retrait manuel si
  besoin.
- [x] **7. Fills de transition** — caisse/toms/kick à la dernière mesure des couplets 1 et 2, des
  refrains 1 et 2 et du final.
- [x] **8. Outro** — crash et kick final, accord final basse/orgue/cuivres, queue de delay.
- [x] **9. Mix final** — couplet 0.259/1 353 Hz, refrain 0.264/1 793 Hz, pont 0.234/1 262 Hz,
  final 0.257/1 801 Hz. Outro en fade (0.150 → 0.125).

## Pour rejouer

1. Ouvrir le set, vérifier 88 BPM.
2. Lancer `S1 Intro` (scène 1), puis `S2 Couplet 1` (scène 2), `S3 Refrain 1` (scène 3),
   `S4 Couplet 2` (scène 4), `S5 Refrain 2` (scène 5), `S6 Pont` (scène 6),
   `S7 Refrain final` (scène 7), `S8 Outro` (scène 8).
3. Le texte et le guide mélodique sont dans `PAROLES.md`.
4. Le refrain final doit être le point le plus fort : c'est le point d'or du morceau.
5. Pour répéter, lancer la scène et jouer avec `6-Guide voix` (sortie Ext. Out). Pour le rendu,
   couper ou baisser cette piste : elle ne doit pas passer dans le master.
