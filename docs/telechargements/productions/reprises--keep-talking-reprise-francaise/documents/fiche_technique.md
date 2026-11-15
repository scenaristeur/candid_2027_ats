# Fiche technique — Keep Talking (reprise française)

Source : `Pink Floyd — Keep Talking [MIDIfind.com].mid` (14 pistes, tempo 102 BPM, 4/4)
Fusion : 14 pistes MIDI → 7 pistes MIDI + 1 audio (voix). Drum Kit Selector Warm.
sample hawking : https://www.youtube.com/watch?v=du_iG7Veupc

## Pistes (indices 0-based = 1-based - 1)

| Ableton | Track lbl | Instrument actif | Pistes source fusionnées | Nb notes |
|---|---|---|---|---|
| 0 | 1-Batterie+Percs | **Selector Kit Warm** (pads réglés, DrBuss) | 13 + 9 + 11 + 12 | — |
| 1 | **2-Voix (talkbox)** | **Surge XT** inst 0 (**RoboTalker** tweaké) + Reverb | talkbox (track 6) | C2=115 / G=72 |
| 2 | 3-Guit Rythm | Guitar Electric Clean + Chorus + Reverb + Delay | 3, 4 | — |
| 3 | 4-Guit Lead | **Surge XT** inst 1 (**Synth Guitarish** tweaké) | 5 (lead) + 6 (talkbox) | — |
| 4 | 5-Basse | Electric Bass Soft + Saturator Bass Shaper + comp parallèle | 10 | — |
| 5 | 6-Nappes | Warm Analog Pad + Reverb + Auto Filter + EQ | 7, 8 | — |
| 6 | 7-Claviers | **Surge XT** inst 2 (**EP 2** tweaké) + EQ + Saturator + Auto Filter + Utility | 0, 1 | — |
| 7 | 8-Voix | MP3 Hawking + **chant enregistré** + MEqualizer + Comp + EQ | discours + couplets 1/2 | — |

## Options claviers (7-Claviers)

Choix actuel : **Evolve Organ** (`FileId_4692`).
Altérnatifs testables (mêmes pistes source pour le solo Rick Wright + nappe) :

| Niveau | Son | URI | Vibe |
|---|---|---|---|
| Actif | Evolve Organ | `FileId_4692` | Orgue FM évolutif, très Floyd |
| Alt 1 | Analog Emulation Keys | `FileId_4653` | Lead/nappe vintage chaud, très Rick Wright |
| Alt 2 | Cathedral Keys | `FileId_4675` | Nappe spacieuse ambiance |
| Alt 3 | Warm Saw Keys | `FileId_4737` | Lead doux luisant |
| Alt 4 | Moving Square | `FileId_4616` | Lead carré net (défaut initial) |

## Options batterie (1-Batterie+Percs)

Choix actuel : **Selector Kit Warm** (`FileId_5282`).

### Mappage notes source → pads (Selector Kit Warm)

| Note source (GM) | Rôle | Pad kit |
|---|---|---|
| 35 | Kick | 36 Kick |
| 38 | Snare | 38 Snare |
| 39 | Clap | 39 Clap |
| 42 | Hat fermé | 42 Hihat Closed |
| 46 | Hat ouvert | 46 Hihat Open |
| 51 | Ride | 51 Ride |
| 49 | Crash | 49 Crash |
| 53 / 55 / 57 | Toms | 43 / 45 / 47 |
| 82 | Shaker | 44 Shaker |

Remap effectué dans `prep_keep_talking.py` → `DRUM_PITCH_MAP`.

### Autres kits dispo (David)
- Selector Kit Clean — `FileId_5281`
- Selector Kit Warm — `FileId_5282` (actif)
- Dry Session Kit — `FileId_5418`
- Recording Hybrid — `FileId_14174`
- Toy LoFi — `FileId_15029`
- Gen Purpose Kit — `FileId_5419` (mappage non-GM, éviter pour cette fusion)

## Scènes (session view)

Découpage en 9 scènes (1 scène = 1 section), extrait par `prep_keep_talking.py` → `_scenes_notes.json`.
Section 13-40 splittée en A1/A2 (basse n'entre qu'à la mesure 29).

| Scène | Slot | Mesures | Beats | Contenu |
|---|---|---|---|---|
| 0 Intro | 0 | 1–12 | 48 | Batterie + Claviers |
| 1 A1 | 1 | 13–28 | 64 | Nappes + Guit Rythm (+ clave, hats/shaker) |
| 2 A2 | 2 | 29–40 | 48 | + Basse, groove complet (kick/ride dès le début) |
| 3 Refrain C1 | 3 | 41–68 | 112 | tutti (lead entre) |
| 4 C2 | 4 | 69–84 | 64 | tutti |
| 5 Keys | 5 | 85–104 | 80 | + Claviers |
| 6 Drop | 6 | 105–112 | 32 | sans nappes |
| 7 G | 7 | 113–136 | 96 | tutti |
| 8 Solo | 8 | 137–151 | 60 | clave+lead, sans nappes |

## Chaîne batterie (tweak natural) — 1-Batterie+Percs

| Device | Idx | Réglage |
|---|---|---|
| Selector Kit Warm | 0 | DrumGroupDevice |
| Compressor (glue) | 1 | Ratio 0.30 (~2:1), Threshold 0.45, Attack 0.15, Release 0.30, Makeup On, Model Peak |
| Reverb (room) | 2 | Dry/Wet 0.16, Room Size 0.40, Decay 0.20, Density Low |

Nota : vélocités préservées de la source (variées, non "usine"). Tweak par l'oreille — ex. plus de glue → Ratio ↑, plus d'espace → Dry/Wet ↑.

## Factorisation batterie (scènes 5-8) — groove + fills

Les scènes 5-8 utilisent la batterie **factorisée** : un **groove court bouclé**
(1-4 mesures) + des **fills de transition**, au lieu d'un clip pleine section à
500-800 notes. Réduction de notes ~5x et CPU.

| Slot batt | Clip | Rôle | Position arr. |
|---|---|---|---|
| 5 | S5 Groove | Groove Keys (1 m) | 340 → boucle 408 |
| 6 | S6 Groove | Groove Drop (1 m) | 416 → boucle 444 |
| 7 | S7 Groove4M | Groove G (4 m) | 448 → boucle 540 |
| 8 | S8 Groove | Groove Solo (1 m) | 544 → boucle 604 |
| 9 | S5 FillEntrée | transition entrée Keys | 336 |
| 10 | S5 FillSortie | fin Keys → Drop | 408 |
| 11 | S6 Fill | fill de toms Drop | 444 |
| 12 | S7 Fill | fin G → Solo | 540 |

Les clips 0-4 restent en pleine section (validées, usine humaine). Les grooves sont
placés dans l'arrangement et **étendus en boucle dans l'UI** (Loop + drag du bord).

## Arrangement complet (beats, tempo 102 ≈ 5min54)

| Section | Beats |
|---|---|
| Intro | 0–48 |
| A1 | 48–112 |
| A2 | 112–160 |
| C1 | 160–272 |
| C2 | 272–336 |
| Keys (S5) | 336–416 |
| Drop (S6) | 416–448 |
| G (S7) | 448–544 |
| Solo (S8) | 544–604 |

## Piste 8-Voix (MP3 Hawking)

- **Importé** : discours Stephen Hawking (source sample `du_iG7Veupc`).
- **À découper** : seul les segments utilisés dans l'original sont à garder —
  Intro (mes. 1-12) + interlude + outro. Positions exactes à repérer à l'écoute
  et à aligner sur l'arrangement (voir structure Hawking/paroles dans la traduction).
- Le discours n'est pas dans le MIDI → utilisé en audio (clip 8-Voix).

## Surge XT — tweaks des 2 racks (2026-08-22)

Mapping : inst 0 = **RoboTalker** → 2-Voix (talkbox) ; inst 1 = « Synth Guitarish » → 4-Guit Lead ;
inst 2 = « EP 2 » → 7-Claviers.

⚠️ Chat de patch Surge = réinitialisation de l'architecture → réappliquer les tweaks (mute/vol/LFO).

### 4-Guit Lead (inst 1 — Synth Guitarish)
| Param | Valeur |
|---|---|
| osc/1/unison (param6 detune / param7 voices) | 0.3 / 0.5 |
| waveshaper drive | 0.75 (grit rock) |
| filter/1 resonance | 0.15 (bite) |
| vibrato S-LFO sine → pitch | depth 0.02 |
| mixer osc3 vol | 0.5 (démute) |
| mixer rm1x2 / rm2x3 vol | 0.08 / 0.08 (démute) |
| FX chain (patch) | Distortion(5) → Chorus(9) → Airwindows(14) |
| amp volume | ~0.89 (-3 dB) |

### 7-Claviers (inst 2 — EP 2)
| Param | Valeur |
|---|---|
| filter/1 cutoff | 0.25 (doux, anti-caissette) |
| aeg attack | 0.3 (attaque douce) |
| waveshaper drive | 0.5 (neutre) |
| osc/1/param7 voices | 0.25 (2 voix) |
| mixer osc3 vol | 0.4 (démute) |
| mixer rm1x2 / rm2x3 vol | 0.04 / 0.04 (discret, anti-cloche) |
| amp volume | 0.88 (-3 dB, aligné) |

⚠️ Reload d'un patch Surge = réinstancie l'architecture (mute/vol réinitialisés). Refaire si changement de patch.

### 2-Voix (inst 0 — RoboTalker, talkbox)
| Param | Valeur |
|---|---|
| patch | **RoboTalker** (Damon Armani, Leads) |
| waveshaper drive | 0.75 (robot + chaleur) |
| osc/1 octave | -2 (coffre) |
| osc/3 octave / volume | -2 / 0.5 (couche grave) |
| osc/1 unison (param6 detune / param7 voices) | 0.3 / 0.5 (~3 voix) |
| S-LFO1 (sine 2 Hz) → pitch / amp / cutoff | 0.05 / 0.25 / 0.1 |
| S-LFO2 (saw lent) → cutoff | 0.3 (formatant robot) |
| Contenu | talkbox MIDI (track 6) : C2=115 n (slot 4), G=72 n (slot 7). Lead/C1 retirés. |

## Piste 8-Voix (chant + Hawking) — chaîne vocale

Contenu : sample Hawking (discours) + chant enregistré de l'utilisateur (couplets 1/2, clips `couplet1` @152-249, `couplet2` @408-481).
L'utilisateur débute en chant : besoin de présence sans avoir le coffre naturel.

| Device | Idx | Réglage |
|---|---|---|
| MEqualizer | 0 | band-pass ~1000-3000 Hz (isole la voix Hawking des samples), bandes cut graves/aigus |
| Compressor | 1 | **RMS**, Threshold 0.65, Ratio 0.5, Attack 0.3, Makeup On (égalise la dynamique de chanteur débutant) |
| EQ Three | 2 | **GainMid 0.98** (boost présence/articulation, clarté) |

Volume piste : ~0.53-0.61. Chant SEUL : centroid ~1310, rolloff 2560, RMS ~0.099 (propre).
⚠️ Les 3 devices s'appliquent AUSSI aux samples Hawking (même piste) → si ça les dégrade, poser une automation sur les intervalles de samples.

## B léger (2026-08-22) — libérer la bande du chant

Diagnostic : sub 0-60 Hz = 22% (section pleine) couvre la bande 1000-3000 Hz (11%) = la voix.
Fix (léger, l'utilisateur aime la basse) : **DrBuss Boom 70→60** (sub du kit) — basse ligne conservée.
Résultat couplet : sub 22%→20%, centroid 606→616. Chant validé par l'utilisateur.

## Intro claviers — adoucissement (Auto Filter, 2026-08-22)

Piste 7-Claviers, device 3 = **Auto Filter** (insert). Low-pass qui s'ouvre via enveloppe
pour arrondir l'attaque de l'intro (donne du coffre, enlève le nasillard « orgue de barbarie ») :

| Param | Valeur |
|---|---|
| Filter Type | Low-pass |
| Frequency | 0.65 (départ assombri) |
| Env Amount | 0.55 (s'ouvre à chaque note) |
| Env Attack | 0.25 (ouverture progressive) |
| LFO Amount | 0 (pas de pulsation) |
| Dry/Wet | 1.0 |

Résultat : rolloff des claviers intro 2219→**1807 Hz** (moins de brillance nasillarde), centroid stable (~1380).
Le pont garde son caractère (les notes s'ouvrent pareil, pas de changement de timbre permanent).
Nota : EQ Three claviers GainMid 1.0→0.78, GainHi 0.85→0.72 (moins de présence nasillarde globalement).
Surge EP2 : notes baissées d'une octave par utilisateur ; couches (osc3/rm1x2/rm2x3) restaurées en actives (pont validé).

## Piste 2-Voix (guide de chant / remplacement vocal)

- Instrument : **Radio Lead** (`query:Sounds#Synth%20Lead:FileId_10039`) — voix radio/chœur.
- Rôle : guide mélodique des lignes de chant de Gilmour + doublure du lead guit.
- **Scène 3 (couplet 2, refrains)** : 86 notes découpées en 3 registres —
  **aigu = chœurs en premier**, **médium/grave = Gilmour répond** (les 3 registres
  sont extraits de la ligne lead source, voir `prep_keep_talking` / split par position d'accord).
- Scènes 0-2 : le MIDI n'a pas de ligne de chant réelle. La **voix off de Hawking**
  (parlée) n'est PAS dans le MIDI → à échantillonner depuis l'original (pistes 8-Voix).
- Doublure avec 4-Guit Lead voulue style Pink Floyd (lead + chant).

## Chaînes instruments (FX, posées APRES les notes, AVANT validation)

Chaînes appliquées le 2026-08-22 (avant capture scène 2). Nota : visa Live a crash
à ce stade — les devices étaient persistés dans le projet, seul le Chorus guit a été
ré-ajouté après redémarrage.

### 5-Basse
| Device | Idx | Réglage |
|---|---|---|
| Electric Bass Soft | 0 | InstrumentGroupDevice |
| Saturator | 1 | Type **Bass Shaper** (2), Drive 0.30, Dry/Wet 0.70 — harmoniques graves, ancre le fondamental sans collision kick |

### 6-Nappes
| Device | Idx | Réglage |
|---|---|---|
| Warm Analog Pad | 0 | InstrumentGroupDevice |
| Reverb | 1 | Room Size 0.80, Decay 0.40, Stereo 0.90, Dry/Wet 0.30 — espace ambience |
| Auto Filter | 2 | Type Low-pass, LFO Amount 0.20, LFO Freq 0.15, Reso 0.10 — le pad "respire" |

### 4-Guit Lead
| Device | Idx | Réglage |
|---|---|---|
| Sweet Lead | 0 | InstrumentGroupDevice |
| Delay | 1 | L 16th 1/8 (3) / R 1/8. (4), Feedback 0.35, **Ping Pong On**, Dry/Wet 0.28 — couleur solo |

### 3-Guit Rythm
| Device | Idx | Réglage |
|---|---|---|
| Guitar Electric Clean | 0 | InstrumentGroupDevice |
| Chorus-Ensemble | 1 | Mode **Ensemble** (1), Amount 0.25, Rate 0.30, Width 0.70, Dry/Wet 0.40 — épaisseur (URI `query:AudioFx#Chorus-Ensemble`, PAS `#Chorus`) |

## Chaîne claviers (7-Basse → 7-Claviers)

| Device | Idx | Réglage |
|---|---|---|
| Evolve Organ | 0 | InstrumentGroupDevice |
| EQ Three | 1 | GainMid 1.0 (boost 200-350 Hz, corps) |
| Saturator | 2 | Type Medium Curve, Drive 0.25, Dry/Wet 0.60 (harmoniques pour smartphone) |

## Scène 1 (A1, mesures 13-28, 64 beats) — réglages

| Piste | Volume | Note |
|---|---|---|
| 1-Batterie+Percs | 0.75 | hats/shaker début, kick+snare à beat 44 |
| 3-Guit Rythm | 0.85 | accords warm (RMS solo 0.030) |
| 6-Nappes | **0.70** | abaissées : étaient 0.095 solo (plus fort que tout), masquaient le high-end |
| 7-Claviers | 0.85 | quasi absent (5 notes) |

Résultat recapture : RMS 0.096, centroid 1892 Hz, DR 20.3 dB (vs 0.136 / 1604 / 17.3 avant abaissement nappes).

## Scène 2 (A2, mesures 29-40, 48 beats) — réglages

| Piste | Volume | Contenu |
|---|---|---|
| 1-Batterie+Percs | 0.75 | groove complet dès beat 0 : kick(36) + snare(38) + hats(42) + ride(51) + fill toms(47) |
| 3-Guit Rythm | 0.85 | riff octave grave (40=E2 + 50/52), Chorus Ensemble |
| 4-Guit Lead | 0.85 | 3 notes lead, Delay ping-pong |
| 5-Basse | 0.85 | rentre ici (28=E1, fondamental), Saturator Bass Shaper |
| 6-Nappes | 0.70 | accord tenu, Reverb + Auto Filter |

Capture (mix sculpté) : RMS 0.135, centroid 1478 Hz, rolloff 3394 Hz, DR 17.4 dB, C# mineur.
Avant FX : RMS 0.125 / centroid 1468 / rolloff 3362. → Plus d'air (rolloff ↑), grave ancré (centroid bas), harmoniques (saturator).

## Niveau / marge

- Master : **1.0** (en aval des insert glue+limiter ; sortie plafonnée à -1 dB par le limiter)
- 1-Batterie+Percs : 0.75 (frozen)
- 5-Basse : 0.90 → gain réduit par utilisateur
- Concerné : capture peak = 1.0 est lié au normalisateur d'analyse, pas à un clip audible.

## Premix dance/groovy (2026-08-22)

Objectif : moins "usine/numérique", plus chaud + plus dance/club.

**Batterie (Selector Kit Warm, device 0 — macros du rack)**
| Macro | Valeur | Effet |
|---|---|---|
| DrBuss Drive | 75 | saturation analogique du bus, chaleur (anti-numérique) |
| DrBuss Boom | **60** (était 70, réduit B) | subs/body du kick, socle club (mais libre la bande du chant) |
| Comp | 50 | glue/groove du kit |
| Reverb (ext.) | Dry/Wet 0.14 | espace doux (retour harmonieux) |

**Couple base / kick**
- Basse : **E2 (82 Hz)** partout (jamais E0/41 Hz = inaudible en club). Volume **0.90**.
- Kick Selector Warm + Boom 70 → fondamental punchy.

**Nappes (device 2 Auto Filter)**
- LFO Amount **0.45** — "breathing"/pump dance.

**Global**
- Groove amount : **0.2** (retour "moins Dance, plus harmonieux" — était 0.45 en mode dance).
- Claviers : volume ~0.78-0.85 + Utility Output 0.5 (compense), Auto Filter intro, EQ adjusted.

**Résultat capture C1 (Refrain)** : RMS 0.153, centroid **1606 Hz** (chaud), rolloff **3684 Hz** (air), DR **16.3 dB** (groove). 
Évolution : centroid 1161→1398→1606 ; rolloff 2695→3297→3684 ; DR 14.5→13.8→16.3.

## Mix final (6 étapes, 2026-08-22)

Application du workflow full-mix (validé Brain Stew), adapté Keep Talking.

**Master chain (Live Lite) — TITRE : « Keep Talking & Listening » :**
- Compressor **glue** : Threshold 0.8, Ratio 0.25, Release 0.3 (desserré vs défaut pour éviter le sur-écrasement)
- Limiter **True Peak** : Input Gain ~0.35, Ceiling 0.95 (~-1 dB), Lookahead 3 ms
- **EQ Three master** : GainHi **0.945** (lift des hauts dosé — air pro, centroid ~883 Hz au Refrain)
- Fader master : 1.0
- (MDynamicEq testé puis écarté : n'exposait pas ses bandes à l'API ; EQ Three fixe retenu)
- Captures finales Refrain : RMS ~0.197, DR ~14.1, centroid ~883, rolloff ~1867

**Carving (EQ préventif) :**
- Claviers : EQ Three **GainLo 0.65** (laisse le bas à la basse)
- Nappes : EQ Three GainLo 0.7 + **GainHi 0.5** (assombrir, désencombrer)

**Dynamique :**
- Basse : Utility Output → 1.0 (remis à l'unité) + Compressor **glue parallèle** (Th 0.8 / Ratio 0.5 / Dry/Wet 0.4)

**Profondeur :**
- 2-Voix : Reverb insert (Dry/Wet **0.18** / Room **0.4** — intelligibilité)
- Guit Lead : Delay ping-pong déjà présent

**Captures finales (master 1.0 + limiter) :**
- C1 Refrain : RMS **0.259**, DR **11.7 dB**, centroid 1119, rolloff 2434 ✓ (cible)
- Drop S6 : RMS 0.340, DR 9.4, centroid 827 (moment le plus grave → boom)

**Piste batterie : frozen** (alliège CPU). Nota : freeze empêche d'éditer les clips batterie → dégeler pour retoucher.

**Non résolus / à trancher :**
- Drop (S6) est plus chaud que le Refrain (RMS 0.34 vs 0.26) → staffer l'équilibre ou assumer le crescendo.
- gain perte luminairement réduit par utilisateur (détail à confirmer à l'écoute).

## Réglage des pads batterie (Selector Kit Warm, 2026-08-22)

Nouveaux tools MCP : `get_drum_pad_parameters` / `set_drum_pad_parameter`
(track, device, note, chain_index, device_index_in_chain) — accès `drum_pads[i].chains[0].devices`.
Déployé via RS (deploy_rs.py) + redémarrage Ableton requis.

Réglages par pad (cohérence ambiance harmonieuse, desserre percussion) :

| Pad | Param | Valeur |
|---|---|---|
| 36 Kick | Boom / Volume | 55 / 100 |
| 38 Snare | Sizzle / Volume | 45 / 100 |
| 39 Clap | Sizzle / Volume | 70 / 95 |
| 42 Hat fermé | EQ Tilt / Volume | 60 / 90 |
| 44 Shaker | EQ Tilt / Volume | 70 / 95 |
| 51 Ride | EQ Tilt / Volume | 55 / 96 |
| 47 Tom 2 | Boom / Volume | 50 / 100 |
| 45 Tom 1 | Boom / Volume | 45 / 100 |
| 49 Crash | EQ Tilt / Volume | 45 / 98 |
| 48 Perc | EQ Tilt / Volume | 60 / 98 |

Principe : kick rond (Boom), brillance dosée (Sizzle/EQ Tilt), high-end (hats/shaker/ride) 
en volume réduit pour ne pas dominer. Tous en raccord avec le retour "moins Dance, plus harmonieux".

## Charge CPU (diagnostic 2026-08-22)

- Problème: **104% avg / 125% peak** en jeu → saturation (coupables : batterie + guit lead).
- **Mute ne réduit PAS la charge** (l'instrument reste chargé) — il faut **désactiver le device**
  (`disable_device` / Device On) ou **freezer** la piste.
- Mesure : en jeu, `get_cpu_load` (moyenne~±5 pts, mesurer quelques sec après purge).
- Diagnostic : batterie seule ~84% avg ; guit lead ~40 pts. Fix : freezer les deux.
- Après factorisation batterie + freeze : **~61% avg / 81% peak** en jeu.
- **Guit Lead : frozen** (le gros levier) — le rack Sweet Lead est le plus coûteux.
- Nota: geler une piste empêche de créer/éditer des clips dessus → dégeler pour éditer.

## Méthode de travail (1 scène = 1 section)

1. **Découper** en sections (SCENES dans `prep_keep_talking.py`). Splitter si un
   instrument entre en cours (ex: 13-40 → A1 sans basse / A2 avec basse).
2. **Régénérer** : `.venv/Scripts/python prep_keep_talking.py` → `_scenes_notes.json`
   (déduplique les doublons des pistes fusionnées à l'unisson, remappe drum pads, vélocités source préservées).
3. **Créer les clips** : `create_clip(track, slot, length_en_beats)` sur les pistes actives de la scène.
4. **Injecter les notes** : `add_notes_to_clip(track, slot, [{pitch, velocity, start_time, duration}])`.
   ⚠️ champ = **`start_time`** (erreur courante : `start` dans le mauvais champ → notes empilées au début).
   Vérifier : `get_clip_notes` (écarter sets début / répartition sur le clip).
   Pour gros volumes (500+ notes), utiliser **`inject_scene.py SCENE ATRACK`** (protocole socket
   port 9877, chunks de 200) — fiable et rapide. Audit des comptes aussi par socket.
5. **Nommer** les clips (`set_clip_name`) — A1 Batt, A2 Basse, ...
6. **Tweak des instrus** (avant validation, AVANT capture) :
   - Charger les FX natifs + régler timbres/volumes pour une harmonie (voir chaînes ci-dessus).
   - Analyse track-by-track en solo (`set_track_solo`), aux moments cruciaux
     (ex: début sans groove vs arrivée kick/snare) → identifier la piste dominante.
7. **Dupliquer dans l'arrangement** : `duplicate_to_arrangement(track, slot, destination_time_beats)`.
   ⚠️ bar param est off-by-one → toujours utiliser `destination_time` en beats (0-based exact).
8. **Capture + analyse** : lire depuis `position_beats`, `capture_and_analyze`, comparer
   RMS/centroid/DR/rolloff à la scène précédente, ajuster volumes si besoin.
9. **Validation utilisateur** avant la scène suivante.

## Outils de réglage

- Drum rack pads : `get_drum_pad_info(track, device=0)`
- Paramètres device : `get_device_parameters(track, device)` / `set_device_parameter(...)`
- Charger instrument : `load_instrument_or_effect(track, uri)`
- Solo piste : `set_track_solo(track)` / capture : `capture_and_analyze(position_beats, duration_sec)`
