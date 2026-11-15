# Mon IA Lisa — plan de notes & réglages

Document d'exécution pour `prep_mona_ia.py`. Complète `PAROLES.md` (textes, accords, topline).
Positions en **temps** (beats) : `0` = temps 1, `0.5` = et du 1 … `3.75` = double-croche
avant le temps fort suivant. Vélocités **0–100**.

---

## 1. Le groove est dans les notes, pas dans le réglage

`set_groove_amount` de l'API Ableton pilote la **quantité globale de groove** (0–1), pas le
pourcentage de swing. Le « swing 58% » du doc IA **n'est pas scriptable** : il se choisit
dans le groove pool de l'UI, et il s'applique à toute la session.

**Solution retenue : le swing est cuit dans les positions de notes.**

| Élément | Retard | Équivalent |
|---|---|---|
| Charley/offset en croche (position x.5) | **+0.04 temps** | 58% de swing |
| Double-croches (x.25, x.75) | +0.015 temps | 58% |
| Basse sur les « et » | +0.03 temps | ~62% |
| Kick temps fort, caisse claire 2 et 4 | **0** (jamais de retard) | le backbeat reste droit |
| Jitter humain | ±0.008 temps | |

C'est plus fiable que le groove pool : le décalage est **par note**, donc on peut faire
respirer la caisse claire (droite) pendant que les charleys dansent (retardés).

**Position 0.5 → 0.54, position 1.5 → 1.54, 2.5 → 2.54, 3.5 → 3.54.**
La figure « A à Z » (3.0 / 3.5 / 3.75) devient 3.0 / 3.54 / 3.765 — le Z reste
juste avant le temps fort suivant, l'anticipation tient.

---

## 2. Les 8 pistes

| # | Nom | Type | Device | URI |
|---|---|---|---|---|
| 0 | `1-Batterie` | MIDI | Kit **Boom Bap** | `query:Drums#FileId_5291` |
| 1 | `2-Basse` | MIDI | **Drift** | `query:Synths#Drift` |
| 2 | `3-Voix` | **Audio** | chaîne voix (§11, vide au départ) | — |
| 3 | `4-Clav EP` | MIDI | **Drift** | `query:Synths#Drift` |
| 4 | `5-Arp+Hook` | MIDI | **Drift** | `query:Synths#Drift` |
| 5 | `6-Nappe` | MIDI | **Drift** (2e inst.) | `query:Synths#Drift` |
| 6 | `7-Percs` | MIDI | Kit **Perc Kitchen** | `query:Drums#FileId_5421` |
| 7 | `8-FX` | MIDI | **Drift** (3e inst.) | `query:Synths#Drift` |

### ⚠️ Live 12 Lite n'a que 6 instruments natifs

`get_browser_items(path="instruments")` sur cette installation renvoie **exactement** :
Drift · Drum Rack · Drum Sampler · Impulse · Instrument Rack · Simpler.

Il n'y a **ni Analog, ni Electric, ni Wavetable, ni Operator, ni Collision, ni Tension** —
ce sont des instruments Suite/Advanced. Les URIs `query:Synths#Analog` etc. **existent
dans le navigateur mais échouent au chargement** (`Browser item with URI ... not found`).

Les 5 synthés sont donc des **Drift**, le multis de l'install (12 familles de presets :
Bass, Pad, Strings, Mallets, Synth Lead, Piano & Keys, Brass, Winds, Percussive,
Guitar & Plucked, Synth Keys, Synth Rhythmic, Effects). Chaque rôle a besoin d'un
**preset différent** + du réglage des paramètres exposés — c'est le travail de l'étape 2.

**Pourquoi la piste Voix est en 3e position et pas en dernière :** le Remote Script n'expose
ni `create_audio_track` ni `move_track`. On ne peut donc **ni créer une piste audio, ni
déplacer une piste**. Le set contient 2 pistes audio vides (`3-Audio`, `4-Audio`) : on
supprime `4-Audio` et on garde `3-Audio` → elle reste en index 2. Si tu veux la voix en bas
de la grille, **glisse la piste dans Live** (2 secondes, une seule fois).

Le « vocal chop » du doc IA remplace le Drift de `8-FX` **après** l'enregistrement
de la voix : on ne peut pas charger un sample que je n'ai pas.

### Retours (returns)

| Retour | Device | Servi par |
|---|---|---|
| A (0) | **Reverb** | Voix 0.28 · Nappe 0.35 · EP 0.12 |
| B (1) | **Delay** (ping-pong 1/8 pointé) | Arp 0.20 · Voix 0.18 · Clav 0.10 |

⚠️ Les deux returns portaient **déjà** Reverb et Delay avant le build (ils sont nommés
`A-Reverb` / `B-Delay` : c'est le set de travail précédent). Le build en a chargé un
second exemplaire → **à supprimer à la main dans Live**, un sur chaque return.
`delete_device` du RS ne traite que `song.tracks`, pas `song.return_tracks`.

---

## 3. Accords — notes réelles et basses

Répertoire **D dorien** (D E F G A B C). `A7♭9` sort deliberately : Bb = la 9e mineure
du dominant, la couleur phrygienne du turnaround.

| Accord | Notes réelles | Voix EP (sans fundamental) | Basse (racine) |
|---|---|---|---|
| Dm9 | D F A C E | 53 57 60 64 | 38 (D2) / 26 (D1) pédale |
| Cmaj9 | C E G B D | 52 55 59 62 | 36 (C2) / 24 (C1) pédale |
| G13 | G B D F A E | 59 62 65 69 | 43 (G2) / 31 (G1) |
| A7♭9 | A C♯ E G B♭ | 61 64 67 (+58 = Bb, vél. 60) | 45 (A2) / 33 (A1) |
| Bbmaj7 | B♭ D F A | 62 65 69 | 46 (B♭2) / 34 (B♭1) |
| C7 | C E G B♭ | 64 67 70 | 36 (C2) / 48 (C3) |
| Dm7 | D F A C | 65 69 72 | 38 (D2) |
| Gm7 | G B♭ D F | 58 62 65 | 43 (G2) / 31 (G1) |
| Ebmaj7 | E♭ G B♭ D | 55 58 62 | 39 (E♭2) / 27 (E♭1) |

### Le refrain est une seule ligne de voix qui monte

```
Bbmaj7  D4(62) F4(65) A4(69)     →
C7      E4(64) G4(67) Bb4(70)      ↗ monte d'un degré
Dm7     F4(65) A4(69) C5(72)      ↗
Gm7     Bb3(58) D4(62) F4(65)    ↘ retour de quinte (la « chute » du refrain)
```

Trois accords montent, le quatrième décroche d'une quinte. C'est la forme du refrain
choral classique, et c'est exactement la forme du hook (`Mo-na Li-sa` = ascendant,
`Mon I-A` = descendant). **La ligne de voix du refrain et le hook chanté sont le même geste.**

---

## 4. Batterie (piste 0) — Boom Bap Kit

⚠️ **Le kit n'est PAS un kit GM.** Vérifié avec `get_drum_pad_info(0, 0)` : 16 pads,
**36 à 51, rien au-dessus**. Le mapping réel :

| Note | Pad | Note | Pad |
|---|---|---|---|
| 36 | Kick Shadow | 44 | Hihat Closed SciFi |
| 37 | Rim Something | 45 | Tom High Rough |
| 38 | Snare Hat Chop | 46 | Hihat Open Bonzo |
| 39 | Clap Ina | 47 | Tom High Rough |
| 40 | Snare Dubplate | 48 | **Stab Brass Blast** |
| 41 | Kick Flabby | 49 | Crash Stacked |
| 42 | Hihat Closed Memphis | 50 | Bass Chop Happy B |
| 43 | Tom Low Rough | 51 | Ride Gated |

Tous les pads utilisés par le groove (`36 38 39 42 46 49 51`) existent bien.
`64` / `70` / `75` **n'existent pas** dans ce kit.

**Motif de base (16 doubles-croches, une mesure) :**

| Instrument | Positions | Vélocités |
|---|---|---|
| Kick 36 | **0** · 2.54 · 3.54 | 112 · 96 · 88 |
| Caisse claire 38 | **1** · 3 (+ fantôme 3.25) | 104 · 98 · 38 |
| Charley 42 | 0 · 0.54 · 1 · 1.54 · 2 · 2.54 · 3 · 3.54 | 74 (temps) / 54 (et) |
| Charley ouvert 46 | 3.54 | 60 |

Le kick **2.54** et le kick **3.54** (les deux « et » de la fin de mesure) sont la signature
funk : c'est ce qui fait danser la mesure à 105 BPM. Le fantôme à 3.25 est l'accent
discret qui empêche la caisse claire de sonner militaire.

**Variantes par section :**

| Section | Batterie |
|---|---|
| Intro (mes. 1–4) | charley seules, croches, vél. 40→70 crescendo ; crash à 3.5 de la mes. 4. **Pas de kick.** |
| Couplets (5–12, 21–28) | motif de base + **fill** sur la dernière demi-mesure de chaque mesure 4/8/12 : caisse claire doubles-croches 2.5→3.75, vél. 60→110 |
| Refrains (13–20, 29–36, 65–72) | motif + **clap 39** en 1 et 3 (vél. 72, +3 dB de Sustain) + charley ouvert plus long + crash sur le temps 1 de chaque phrase de 4 mesures |
| Pre-Hook (37–40) | **kick sur 0 seulement**, charley croches puis doubles-croches (16) à partir de la mes. 39 ; **roulement caisse claire** mes. 40 (2.0→3.75, vél. 62→112) |
| Mini-Hook (41–44) | **half-time** : kick 0 et 2, caisse claire 2, charley croches. À partir de 1.54 de la mes. 42 : **plus rien** (2,5 temps, la basse seule). Sur le « eh » de la mes. 44 (temps 3) : **coupure**, la cymbale inverse (piste FX) déborde sur la mes. 45 — **pas de crash**, il mangerait « Elle te voit » |
| Post-Hook (45–48) | **aucune batterie.** Un seul sub-kick (36) à 0 de la mes. 48, vél. 70 |
| Pont (49–56) | **ni kick ni caisse claire.** Charley 42 croches vél. 50 (+4 sur les temps) crescendo +3 par mesure. Le **crescendo de maracas 70 en doubles-croches est sur la piste `7-Percs`**, pas ici : le kit Perc Kitchen est un kit GM, le pad 70 y est garanti, pas dans le Boom Bap |
| Double-Hook (57–64) | motif complet + **ride 51** (0, 1, 2, 3, vél. 46) + crash au temps 1. Mes. 64 (« eh » crié) : **un seul kick, puis un temps de silence absolu** — la basse, l'arp, l'EP et la nappe coupent aussi. Impact au temps 1 de la mes. 65 |
| Outro (73–76) | mes. 73–74 : motif, mais kick seulement sur 0 et 2 ; mes. 75 : charley + 1 kick ; mes. 76 : **rien**, cymbale inverse + queue de réverb, fin sur 3.5 |

---

### La piste `7-Percs` (Perc Kitchen)

⚠️ **Ce kit n'est PAS un kit GM non plus** — et c'est un piège qui a coûté une passe
complete. `get_drum_pad_info(6, 0)` renvoie **16 pads, 36 à 51**, tous nommés « Perc… »
ou « FX… » : `36` Perc Pan · `37` Perc Pot 1 · `38` Perc Pot 2 · `39` Perc Strike ·
`40-41` FX Drip · `42` Perc Knifes · `43` FX Drip 3 · `44` FX Ice Cubes · `45` FX Drip 4 ·
`46` Perc Spoons · `47` FX Water · `48` Perc Glass Low · `49` Perc Kettle ·
`50` Perc Kling · `51` Perc Klang.

**Il n'y a ni 64 (tambourin), ni 70 (maracas), ni 75 (clave).** Écrire 64/70/75 ne
produit **aucun son** : la piste était entièrement muette, sans aucune erreur affichée.

Rôles remappés sur des pads qui existent :

| Rôle prévu | Pad GM | Pad réel | Nom du pad |
|---|---|---|---|
| Shaker (croches) | 70 | **37** | Perc Pot 1 |
| Shaker (temps 2 et 4) | 64 | **38** | Perc Pot 2 |
| Clave | 75 | **39** | Perc Strike |
| Tambourin | 64 | **46** | Perc Spoons |
| Maracas du pont (crescendo) | 70 | **50** | Perc Kling |

C'est la seule source de percussions du morceau (le Boom Bap n'a que de la batterie).

| Section | Percussions |
|---|---|
| Intro | **rien** — les charley de la batterie suffisent |
| Couplets | shaker 37 croches (vél. 50 temps / 38 croches) + Perc Pot 2 38 sur les temps 2 et 4 (vél. 66 / 64). Perc Strike 39 en croches 2.765 / 3.265 / 3.765 sur la dernière mesure de chaque groupe de 4 |
| Refrains | idem couplets + Perc Strike 39 sur le « et » du 3 (2.54, vél. 52) |
| Pre-Hook | shaker croches, vél. 44 → 58 sur les 4 mesures (la montée) |
| Mini-Hook | shaker croches + Perc Strike 39 sur le « et » du 3 |
| Post-Hook | shaker croches **vél. 22** — presque inaudible, juste assez pour que le silence ne soit pas mort. C'est le fond sur lequel tombe le « ding » |
| Pont (49–56) | **Perc Kling 50 en doubles-croches (16 par mesure), vél. 38 → 108, +8 sur les temps** : c'est le crescendo du pont. Perc Spoons 46 sur le temps 3 des mes. 52 et 56 |
| Double-Hook | shaker croches + tambourin + clave sur le « et » du 3 |
| Outro | shaker croches jusqu'à la mes. 75, puis plus rien (mes. 76 = silence + queue de réverb) |

---

## 5. Basse (piste 1) — Drift

**Cellule fondamentale** (Dm9, Cmaj9, Bbmaj7, Dm7, Gm7, Ebmaj7, Cm7) — 6 notes/mesure :

| Pos. | Note | Vél. |
|---|---|---|
| 0 | fondamentale | 96 |
| 1.54 | fondamentale **+12** | 84 |
| 2 | fondamentale | 90 |
| 2.765 | fondamentale | 60 |
| 3.54 | **approche chromatique** (racine suivante ± 1) | 68 |

> Les positions `x.765` et `x.54` sont le **swing cuit** (§1) : 2.75 + 0.015, 1.5 + 0.04.
> Le script les calcule, il ne les recopie.

**Cellule G13** : `G2(43) · G2+12(55) · D2(38) · G2(43) · G2+12(55) · A2(45, la 9e)`
positions 0, 1.54, 2, 2.54, 3, 3.54.

**Cellule A7♭9** — la plus importante, elle fait le pont vers le bII :

| Pos. | Note | Vél. |
|---|---|---|
| 0 | A2 (45) | 94 |
| 0.765 | A♭2 (44) | 78 |
| 1 | G2 (43) | 86 |
| 1.54 | A2 (45) | 80 |
| 2 | A2 (45) | 90 |
| 2.54 | A♭2 (44) | 74 |
| 3 | G2 (43) | 84 |
| 3.54 | F2 (41) | 70 |

C'est une **descente chromatique sur une tierce** : la seule chose qui « amenait » le
`Ebmaj7` du pont par la porte, au lieu de le faire sauter aux oreilles.

**Refrain — 8 notes/mesure, la basse marche sous le refrain :**

| Accord | Ligne |
|---|---|
| Bbmaj7 | B♭1(34) · B♭2(46) · F2(41) · B♭1 · B♭2 · D2(38) · B♭1 |
| C7 | C2(36) · C3(48) · C2 · B♭1(34) · C2 · G2(43) · B♭2(46) · G2 |
| Dm7 | D2(38) · D3(50) · F2(41) · D2 · D3 · A2(43) · F2 |
| Gm7 | G2(43) · G1(31) · B♭1(34) · G1 · G2 · B♭1 · G1 |

**Pont (mes. 49–56)** : notes rondes, une par mesure, **sans mouvement** :
`E♭2(39) · D2(38) · C2(36) · B♭1(34) · E♭2(39) · D2(38) · C2(36) · A1(33) tenu 2 mesures`.
C'est la seule section où la basse ne funk pas : elle tient le sol.

**Mini-Hook (mes. 41–44)** : la basse **remplit le trou de la mesure 42** — c'est la
seule chose qui joue pendant les 2,5 temps de silence de la voix. Un seul accord tenu :
`B♭1(34)` à 1.54, tenu 2 temps, vél. 88. Rien d'autre dans la mesure. Un accord tenu dans
le vide, c'est le « moi je lis de A à Z ».

**Pre-Hook (mes. 37–40)** : pédale de basse, une ronde par mesure, vél. 70 — la tension
est dans la batterie et le riser, la basse ne funk pas.

**Double-Hook (mes. 57–64)** : cellule de couplet, sauf :
- mes. 58 : même trou que la mes. 42 (`B♭1(34)` à 1.54, tenu 2 temps, vél. 88) — l'identité
  du hook se reconnaît là ;
- mes. 64 : **rien**. Le « eh » crié laisse un temps de silence absolu.

**Post-Hook** : aucune basse sauf la mes. 48 (`A1(33)`, ronde, vél. 60). Le vide est total.

---

## 6. Clav EP (piste 3) — Drift

**Motif de stabs, 2 accords par mesure**, excepté le refrain qui en a 4 :

| Position | Accent | Vél. |
|---|---|---|
| 0 | 1er temps | 92 |
| 2.54 | et du 3 | 84 |
| 3.5 (mesures de refrain) | et du 4 | 70 |

Alternate les inversions à 4 notes : la 2e fois sur la même mesure, on inverse l'accord
première et dernière note. Notes tirées du tableau §3 **+12** sur les couplets (EP aigu,
percutant), **+0** sur le pont (EP grave,Pad ).

**Refrain :** stabs **sur le temps 1 de chaque mesure + sur le « et » du 3** (positions 0,
2.54), vél. 96. Le stab du temps 1 tombe **avec** le kick, celui du 2.54 tombe avec le
kick fantôme. Puis : au temps qui suit chaque « A à Z », un **stab_extra** de 2 notes
(vél. 100) sur la fondamentale.

---

## 7. Arpège / Hook (piste 4) — Drift

**Couplets : arpège en doubles-croches, 8 notes par mesure, montée 4 / descente 4.**

| Accord | Arpège (positions 0, 0.54, 1, 1.54, 2, 2.54, 3, 3.54) |
|---|---|
| Dm9 | 62 · 65 · 69 · 72 · 69 · 65 · 62 · 60 |
| Cmaj9 | 60 · 64 · 67 · 72 · 67 · 64 · 60 · 59 |
| G13 | 59 · 62 · 65 · 69 · 65 · 62 · 59 · 57 |
| A7♭9 | 61 · 64 · 67 · **70** · 67 · 64 · 61 · 57 |

Le **70 (B♭4) sur la mesure A7♭9** est la seule note hors dorien de tout le morceau côté
instruments. Vélocité 62 (doux), une seule fois par mesure. C'est le « grincement ».

**Refrain :** l'arpège **s'arrête** (l'EP prend le refrain), la piste joue le **contre-chant**
— la version inférieure de la topline, à l'octave sous la voix :

| Mes. | R1 / R2 contre-chant | Vél. |
|---|---|---|
| 1 | Bb2(46) A2(45) Bb2(46) C3(48) | 76 |
| 2 | Bb2(46) tenue 4 temps | 72 |
| 7 | Bb2(46) Bb2 · C3(48) · A2(45) | 74 |
| 8 | Bb2(46) Bb2 · A2(45) · G2(43) · F2(41) | 70 |

**Hook (mini-hook + double-hook)** : l'arpège joue le **motif A/B du hook**, une octave
sous la voix, à l'unisson du chœur :

- Motif A (`Mo-na Li-sa`) : Bb3(58) C4(60) D4(62) **D4 tenu 2 temps**
- Motif B (`Mon I-A`) : Bb3(58) A3(57) G3(55) — **puis le silence du gimmick**

**Pont :** notes rondes, une par mesure, registré bas, avec le filtre qui descend :
`Bb2(46) · A2(45) · G2(43) · A2(45) · Bb2(46) · A2(45) · G2(43) · F2(41) tenu`

**Post-Hook :** rien. Le silence est le contenu.

---

## 8. Nappe (piste 5) — Drift (2e instance)

Accord tenu **2 temps par note** (respiration, 2 segments par mesure), en croches :

| Accord | Nappe (3e octave) | Vél. |
|---|---|---|
| Dm9 | 50 · 53 · 57 · 60 | 54 |
| Cmaj9 | 48 · 52 · 55 · 59 | 54 |
| G13 | 43 · 59 · 62 · 64 | 52 |
| A7♭9 | 45 · 61 · 64 · 67 | 50 |
| Bbmaj7 | 46 · 62 · 65 | 56 |
| C7 | 48 · 64 · 67 | 56 |
| Dm7 | 50 · 65 · 69 | 56 |
| Gm7 | 43 · 58 · 62 | 56 |
| Ebmaj7 | 39 · 55 · 58 | 50 |
| Cm7 | 36 · 51 · 55 | 50 |

**Pont :** la nappe **descend d'une octave sur la dernière note** du pont (mes. 56,
`A2(45) → A1(33)` à 2.54 puis tenue). C'est le mouvement le plus grave de la nappe, et le
hook qui suit repart d'un coup en haut (Bb3). La coupe de filtre sur la piste 4
(`5-Arp+Hook`, automate §10) fait le reste : c'est ce mouvement + la fermeture du filtre
qui fait basculer l'auditeur du noir du Louvre dans le hook.

**Refrain :** la nappe passe à **4 notes** sur `Bbmaj7` (62 · 65 · 69) pour s'ouvrir, et
revient à 3 notes sur `Dm7` / `Gm7`. L'ouverture du refrain est donc aussi une ouverture
de voicing.

---

## 9. FX (piste 7) — Drift « cloche / bruit »

| Moment | Position | Rôle |
|---|---|---|
| Intro fin | mes. 4, 3.0 → 3.75 | cymbale inverse, crescendo |
| R1 | mes. 13, 0 | impact (verbe + crash) |
| R2 | mes. 29, 0 | impact |
| Pre-Hook | mes. 40, 0 | riser (2 temps) |
| Mini-Hook | mes. 44, 3 | « eh » → réverb inverse seule (le reste est coupé) |
| Post-Hook | mes. 45, 2.54 | **le « ding » de notification** sur « Elle te voit » |
| Pont | mes. 49, 0 | impact (le noir du Louvre) |
| Pont fin | mes. 56, 2.0 | cymbale inverse (monte vers le hook) |
| Double-Hook | mes. 64, 3 | « eh » → réverb inverse |
| R3 | mes. 65, 0 | impact |
| Outro | mes. 76, 0 | cymbale inverse longue, coupe sur 3.5 |

Le « ding » est le seul moment comique literal du morceau : **il tombe exactement sur le
mot « voit »**, au milieu du post-hook silencieux. Ne le place pas ailleurs.

### ⚠️ État du son FX (sculpté, pas fini) — à retravailler

Sculpté le 26/09 : oscillateurs coupés, noise 0.6, LP 0.4, release 0.7 → c'est un burst de
bruit, **pas encore un impact qui « claque »**. David : « c'est pas terrible ». **Ne pas y
toucher tant que les 4 autres Drift ne sont pas sculptés** ; ensuite on revient dessus.
Idées de prochaine passe : filtre piloté par enveloppe (ouvrir au lieu de fixer), un peu
d'oscillo grave pour le poids, et un vrai tail de réverb.

---

## 10. Automations — **étape 2, après validation des scènes**

⚠️ **Ces cibles n'existent pas encore.** `device_1_…` / `device_2_…` supposent les chaînes
FX des §9 et §11 déjà chargées, et le build initial ne pose **que l'instrument** sur chaque
piste. Ne pas écrire ces lanes avant l'étape 2 : un `set_automation_lanes` sur une cible
inexistante est silencieusement perdu.

Toutes écrites en un seul appel `set_automation_lanes` par clip (les lanes s'écrasent).

| Piste · cible | Intro | Couplet | Refrain | Hook | Pont | Outro |
|---|---|---|---|---|---|---|
| `2-Basse` · `device_1_Global Glide` | 0.005 | 0.005 | 0.02 | 0.05 | 0.08 | 0.02 |
| `4-Clav EP` · `device_3_Dry/Wet` (Reverb) | 0.15 | 0.12 | 0.18 | 0.10 | 0.45 | 0.30 |
| `5-Arp+Hook` · `device_2_Filter Freq` | 500 | 800 | 3000 | 4000 | 400 | 300 |
| `5-Arp+Hook` · `device_2_Dry/Wet` (Reverb) | 0.30 | 0.20 | 0.25 | 0.15 | 0.60 | 0.50 |
| `6-Nappe` · volume du clip | 0.30 | 0.70 | 0.85 | 0.55 | 0.90 | 0.60 |
| `8-FX` · `device_1_Dry/Wet` | 0.30 | 0.10 | 0.20 | 0.45 | 0.55 | 0.70 |

Sur `5-Arp+Hook`, le **filtre 500 → 3000 Hz** entre couplet et refrain est le mouvement
majeur du morceau : le refrain s'ouvre. `Dry/Wet` à 0.60 sur le pont = le « vide » sonore
de la phrase « et y'a rien, voilà ».

---

## 11. Chaîne voix (piste 2, audio)

Une seule piste audio = voix lead + adlibs. La chaîne est **transparente d'abord** :
on ne pose aucun preset sans capture.

| # | Device | Réglages de départ (normalisés 0–1) |
|---|---|---|
| 1 | **Utility** | HPF `On` · Freq 0.02 (≈ 40 Hz) · Output 0.85 |
| 2 | **Saturator** | Mode Soft Clip · Drive 0.20 · Output 0.80 · **On = 1** |
| 3 | **Glue Compressor** | Threshold 0.55 · Ratio 2:1 · Attack 0.02 · Release 0.25 · Makeup 0.55 |
| 4 | **Reverb** (retour A) | Room Size 0.42 · Decay 1.6 · **Dry/Wet 0.18** (insert léger, pas plus) |
| 5 | **Delay** (retour B) | Ping-Pong · Sync 1/8 pointé · Feedback 0.28 · **Dry/Wet 0.12** |

⚠️ **Ne jamais coller cette chaîne telle quelle.** Le Saturator efface le signal si on
pousse Drive avant d'avoir vérifié le RMS (ça arrive). Étape par étape : Utility →
capture → Saturator → capture.

---

## 12. Ordre d'exécution dans Live

1. `set_tempo(105)`, `set_signature(4, 4)`, `set_groove_amount(0)` (le groove est dans les notes).
2. Supprimer la piste audio `4-Audio` (vide) → 2 MIDI + 1 audio, créer 5 pistes MIDI → 7 MIDI + 1 audio.
3. Renommer les 8 pistes (§2). La Voix reste en index 2 : le RS ne sait pas déplacer une piste.
4. Charger les devices : `query:Drums#FileId_5291` (Boom Bap), **`query:Synths#Drift` ×5**,
   `query:Drums#FileId_5421` (Perc Kitchen). Un `delete_device` par device avant chargement,
   sinon un re-run empile les instruments.
5. Returns : **ne rien charger** — ils portent déjà Reverb (A) et Delay (B) du set précédent.
6. Vider la grille (16 slots × 8 pistes), puis écrire **84 clips** (12 scènes × 7 pistes MIDI).
   Les clips vides (EP dans l'intro, le pont, l'outro…) sont **volontaires** : ils servent de
   bouton stop.
7. Vérifier `get_clip_notes` sur les 84 clips avant de toucher à l'arrangement.
8. **Étape 2, seulement après ta validation à l'oreille** : choisir et sculper les 5 presets
   Drift (§2), chaînes FX (§9, §11) en état transparent, puis automations (§10). Jamais avant.
9. **Ne pas sauvegarder sans validation de David.**

---

## 13. Ce que le build a révélé (à savoir avant de relancer)

`prep_mona_ia.py` a tourné, et la vérification a corrigé 4 erreurs du plan :

| Découvert | Effet | Correctif dans le script |
|---|---|---|
| **`Analog` / `Electric` / `Wavetable` n'existent pas en Live 12 Lite** | le build s'est arrêté à la 2e piste | 5 × `Drift` |
| **Perc Kitchen n'est pas un kit GM** (16 pads, 36-51) | les 2 100 notes de la piste percs étaient **toutes muettes** — aucune erreur affichée | pads remappés 37/38/39/46/50 |
| **L'humanisation poussait le premier temps sous 0** | Live **jette silencieusement** toute note de `start_time` négatif : le kick et la basse du début de chaque clip disparaissaient (1 à 2 notes par clip) | le temps 0 n'est plus bougé |
| **`set_scene_name` est cassé dans le RS** | les 12 lignes de la grille sont sans nom | renommer à la main dans Live |

Autres limites du RS rencontrées :

- `load_instrument_or_effect_on_return_track` **n'existe pas** côté RS. Le nom réel est
  **`load_browser_item_on_return_track`**.
- **`delete_device` ne traite que `song.tracks`**, pas les returns → impossible de retirer le
  doublon Reverb/Delay à la main depuis le script.
- **`create_scene` existe mais `delete_scene` non**, et la grille contenait déjà 4 lignes :
  le build en a ajouté 12 → **16 lignes, dont 4 vides en bas**. À supprimer à la main.
- `create_clip` échoue sur une piste **audio** : pour sonder la grille, viser une piste MIDI.
- Live stocke les positions **au tick** (960 PPQ) : un écart de 0.001 temps dans `get_clip_notes`
  est un arrondi, pas une note perdue.
- Une note dont la **durée dépasse la fin du clip est acceptée** (le crash de l'intro déborde) :
  ne pas rogner les durées.

---

## 14. État figé du morceau (à la sauvegarde de David)

Version instrumentale terminée et sauvegardée. À rejouer :

### Instruments (piste : device)

| Piste | Device(s) | Sculpture |
|---|---|---|
| `1-Batterie` | **Toy LoFi Kit** `query:Drums#FileId_15029` (pas Boom Bap) | pads réglés : kick vol −10, snare −12, clap −14 (decay 0.42), charley −28 (pitch env −8, decay 0.35), charley ouverte −22 (pitch env −8, decay 0.45), ride −16 |
| `2-Basse` | Drift + Saturator (Analog Clip 0.25) + Compressor (sidechain) | basse chaude/rond ; Saturator pour la présence ; **sidechain kick→basse** (input ← batterie Post FX, S/C On, ratio 0.9, thresh 0.5, release 0.35) |
| `3-Voix` | (audio, vide) | à enregistrer |
| `4-Clav EP` | Drift | caractère Rhodes (2e osc détuné, hammer noise, thickness) + EQ Three GainLo 0.7 |
| `5-Arp+Hook` | Drift | pluck chaud (triangle), filtre fermé |
| `6-Nappe` | Drift + EQ Three | grandiose/planant : triangles détunés, spread 0.7, swell lent, GainMid 0.7 |
| `7-Percs` | Perc Kitchen Kit | pads 37/38/39/46/50 (remap non-GM) + **Crash Lofi** sur pad 52 (E2) : vol −22, decay 0.9, release 0.9, sustain 1.0, pitch env |
| `8-FX` | Drift | risers / cymbales inverses (les crashs sont sur la percu) |

### Mix

- **Staging** : pans (EP −0.3, arp +0.3, percs +0.2) ; volumes calés.
- **Carving** : batterie GainLo 0.6, EP GainLo 0.7, nappe GainMid 0.7.
- **Dynamique** : sidechain kick→basse.
- **Profondeur** : sends — nappe→réverb 0.35, EP→réverb 0.12 + delay 0.10, arp→delay 0.20, percu→réverb 0.18.
- **Master** : Compressor glue (ratio 0.7, thresh 0.4, release 0.3) + Limiter (lookahead 3 ms, plafond 0.95, True Peak). Fader master = **1.0**.

### Automations (par clip, session)

- **Arp** : filtre couplet 0.35 → refrain 0.6 (l'ouverture).
- **Nappe** : volume Drift par section (intro 0.3 / couplet 0.5 / refrain 0.6 / hook 0.4 / pont 0.55 / outro 0.4).
- **EP** : send réverb couplet 0.12 / refrain 0.18 / hook 0.10.
- **Basse** : glide couplet 0.005 / refrain 0.02 / hook 0.05 / pont 0.08.

### Arrangement

12 scènes posées séquentiellement dans la timeline → **76 mesures** (304 temps), + la queue de
réverb/cymbales de l'outro (336 temps). L'arrangement a repris les automations des clips.

### Conventions / pièges à retenir

- **Note E2 = 52** (Ableton C3 = 60), pas 40.
- L'échelle d'automation = **plage native du paramètre** (0-1 pour LP Freq), pas un brut 0-127
  (voir `pieges-automation`).
- Bug RS corrigé : `delete_events_in_range` sur clips de session (end_time invalide → « Inverted
  ranges »). Fix dans `_clip_bounds`.
