# Sauvage Méditerranée — Fiche technique

> ⚠️ **Morceau en cours de construction.** Cette fiche est tenue à jour au fur et à mesure.
> Seuls les éléments validés à l'oreille par David y figurent.

## En-tête

| | |
|---|---|
| **Tempo** | 100 BPM |
| **Tonalité** | Do#m (C#m) |
| **Signature** | 4/4 |
| **Style** | Reggae rub-a-dub / ragga occitan, façon Massilia Sound System |
| **Contexte** | Association Sauvage Méditerranée (Aix-en-Provence) — déchets sauvages → bijoux, Monnaie Sauvage |
| **Voix** | Non posée à ce jour |
| **Phase** | Maquette — riffs et choix de sonorités |

## Structure

Non encore construite. On travaille en Session View scène par scène.

## Grille d'accords

| Section | Accord | Notes réelles (MIDI, C3=60) |
|---|---|---|
| Groove de base | C#m | C#2 = 49, G#2 = 56 |

## Pistes

Budget : 8 pistes max. Returns A/B non comprises.

### Index 0 — `Selector Kit Warm`
- **Type** : Drum Rack (kit `.adg` — `query:Drums#FileId_5282`)
- **Rôle** : one-drop, colonne vertébrale rythmique
- **Volume** : 0.85 (0 dB)
- **FX** : `Compressor` → `MEqualizer` → `MDelay` (chaîne dub, voir « Chaînes FX — détail »)

Pads utilisés (vérifiés via `get_drum_pad_info`) :

| Note | Pad |
|---|---|
| 36 | Kick Selector Warm 1 |
| 38 | Snare Selector Warm 1 |
| 42 | Hihat Closed Selector Warm |
| 44 | Shaker Selector Warm (disponible, non utilisé) |
| 46 | Hihat Open Selector Warm (disponible, non utilisé) |

### Index 1 — `Dub Techno Bass` — **SUPPRIMÉE**
- **Moteur** : Drift (`query:Sounds#Bass:FileId_7166`)
- **FX** : Saturator → Compressor
- Supprimée pour libérer 2 places sur le budget de 8 pistes, afin de monter le dispositif
  d'audition du skank (6 guitares). Voir `03 - Skank 6 candidats.md`.

### Index 1 (actuel) — `Deep Chill Bass`
- **Moteur** : `Deep Chill Bass.adg` (`query:Sounds#Bass:FileId_11211`), InstrumentGroupDevice
- **FX** : Saturator → Compressor → **Delay** (insert, signature « vague »)
- **Statut** : basse retenue, non mutée

### Index 3 — `Analog Bass` — **SUPPRIMÉE**
- **Moteur** : `Analog Bass.adg` (`query:Sounds#Bass:FileId_5167`), InstrumentGroupDevice
- **FX** : Saturator → Compressor
- Supprimée pour la même raison que la Dub Techno.

> ⚠️ **Les deux autres basses ont été supprimées sans avoir été jugées.** Elles ont été retirées
> pourTenir le budget de 8 pistes pendant l'audition du skank. Si aucune des 6 guitares ne convient,
> il faudra les recharger — le choix de la basse n'est donc **pas** acté.

### Index 2 à 6 (actuels) — les 5 guitares du skank
Pistes d'audition, même partie écrite, seul le son change. Détail complet dans
**`03 - Skank 6 candidats.md`**.

| Index | Piste (nom Live) | Rôle | État |
|---|---|---|---|
| 2 | `3-Guitar Electric Clean` | *révolte douce* | mutée |
| 3 | `4-Chord Dub Pluck` | couleur dub ⚠️ delay interne | mutée |
| 4 | `5-Synergy Pluck Brass` | **préférence de David** | mutée |
| 5 | `6-Organ Klick` | A — skank sans guitare | mutée |
| 6 | `7-Surge XT` (`Overdriven Guitar`) | B — skank brûlé | mutée |

⚠️ **Les chaînes FX des guitares ne sont pas posées.** Principe acté : chaîne de même forme,
calibrage individuel. Non fait volontairement — on ne bride pas six sons avant d'avoir choisi.

### Pistes supprimées
- `3-Audio`, `4-Audio` (pistes audio par défaut, sans usage) — sur demande de David.
- `2-Dub Techno Bass`, `4-Analog Bass` — supprimées pour le dispositif d'audition du skank.
- **`4-Chord Key Stabs` — supprimée par David.** Deux motifs : il ne la trouvait pas bonne, et
  elle **saturait le CPU**. C'était un `InstrumentGroupDevice` (rack), donc un engin à voix
  multiples, pas un simple preset. **Lesson : les racks du browser peuvent être bien plus
  gourmands qu'un preset unVoix** — mesurer avant d'en empiler.

> ⚠️ **Après cette suppression, les index de piste ont glissé de 1 pour tout ce qui suivait.**
> `Synergy Pluck Brass` est passée de l'index 5 à l'index 4 (affichée « 5- » dans Live).
> Toujours vérifier `get_cpu_report` avant de viser un index.

## Clips

| Piste | Clip | Longueur | Contenu |
|---|---|---|---|
| 0 | `One-Drop Base` | 8 temps (2 mesures) | 20 notes — voir ci-dessous |
| 1 | `Bass Roots` | 8 temps (2 mesures) | 4 notes |
| 2 | `Bass Roots` | 8 temps (2 mesures) | 4 notes |
| 3 | `Bass Roots` | 8 temps (2 mesures) | 4 notes |

### Clip `One-Drop Base` (index 0) — groove validé

**One-drop** : grosse caisse + caisse claire ensemble sur le 3e temps. Pas de kick sur le 1er
temps — c'est ce qui donne le balancement « en arrière ».

| Temps | Note | Son | Vélocité |
|---|---|---|---|
| 2 | 36 | Kick | 100 |
| 2 | 38 | Snare | 90 |
| 6 | 36 | Kick | 100 |
| 6 | 38 | Snare | 90 |
| 0 → 7.5 | 42 | Hihat Closed, croches | 75 sur temps 2 et 6, 70 sur temps pairs, 60 sur croches faibles |

### Clip `Bass Roots` (index 1, 2, 3) — ligne identique sur les trois basses

| Temps | MIDI | Note | Vélocité |
|---|---|---|---|
| 0 | 49 | C#2 (racine) | 95 |
| 2 | 49 | C#2 | 85 |
| 4 | 56 | G#2 (quinte) | 90 |
| 6 | 49 | C#2 | 85 |

## Réglages mix

| Piste | Volume | Pan | Mute |
|---|---|---|---|
| 0 Selector Kit Warm | 0.85 (0 dB) | 0.0 | non |
| 1 Dub Techno Bass | 0.85 (0 dB) | 0.0 | **oui** |
| 2 Deep Chill Bass | 0.85 (0 dB) | 0.0 | non (audible) |
| 3 Analog Bass | 0.85 (0 dB) | 0.0 | **oui** |
| Master | 0.85 (0 dB) | 0.0 | — |

### Return A — `A-Reverb`
Device : Reverb. Réglages d'origine, non travaillés.

### Return B — `B-Delay`
Device : Delay. **Volontairement laissé neutre** — réservé au delay du mix général.

| Paramètre | Valeur |
|---|---|
| Ping Pong | 0 (off) |
| LFO > Delay | 0 |
| Feedback | 0.221 |
| L/R 16th | 2 |

> ⚠️ **Piège évité.** Une première version avait envoyé Deep Chill vers ce return avec ping-pong +
> wobble. Effet liked mais **intrusif**, et tout instrument futur envoyé vers B aurait hérité de la
> vague. Le delay a donc été déplacé en **insert sur la piste**, et le return remis à zéro.

## Chaînes FX — détail

### Basse — `Saturator → Compressor`

`Type = 3` (**Bass Shaper**) sur les trois : c'est la courbe faite pour le grave, elle ajoute les
harmoniques qui font tenir la basse sur téléphone (voir `mix-translation`).

| Basse | Saturator Drive | Comp. Threshold | Comp. Ratio |
|---|---|---|---|
| 1 Dub Techno | 0.45 | 0.78 | 0.70 |
| 2 Deep Chill | 0.35 | 0.80 | 0.65 |
| 3 Analog | 0.40 | 0.76 | 0.75 |

### Basse Deep Chill (index 2) — `Delay` en insert, signature « vague »

L'effet voulu, décrit par David : « une vague, flottante, berçante, whaouwhaouwha ».

**Démarche** : un delay en double-croche collait aux charleys → effet « tactactac ». Pour décrocher
du tic, on a allongé le retard, décalé son point d'arrivée, et surtout mis un **LFO sur le temps de
delay** (le wobble) — c'est lui qui transforme la répétition en ondulation.

| Paramètre | Valeur | Rôle |
|---|---|---|
| L/R 16th | 6 (pointé) | Retard long — l'écho arrive *après* la battue |
| **L/R Offset** | **0.33** | Décalage : l'écho tombe *entre* les temps, plus « afloat » |
| **Ping Pong** | **1** | Écho alterné G/D → mouvement latéral |
| **LFO Mode** | **1** (*Time*) | Le LFO module le **temps** de delay |
| **LFO Wave** | **5** (**S & H** — Sample & Hold) | Wobble **non périodique** : le retard change de valeur par paliers aléatoires, jamais deux fois pareil. C'est ce qui fait le côté « vivant » plutôt que « vibrato machine » |
| **LFO Freq** | **0.10** | Respiration lente |
| **LFO > Delay** | **0.45** | Amplitude du wobble — le paramètre de la « vague » |
| **Feedback** | **0.5** | L'écho s'étire, se dilue |
| **Dry/Wet** | **0.22** | **Intensité perçue.** À 0.5 l'écho domine ; à 0.22 c'est un nappage de fond |

> **Forme d'onde — choix à connaître.** Le wobble était d'abord une **sinusoïde** (Wave = 0), donc
> parfaitement périodique : c'est précisément ce qui sonnait « machine ». David a demandé des
> variations plus naturelles, et `LFO Wave = 5` (**S & H**) a été retenu. Alternatives disponibles
> sur ce device, pour arbitrage ultérieur : **Wander** (6, dérive continue, moins saccadée),
> **Triangle** (1, plus douce mais toujours périodique — donc « vibrato », pas « vivant »).
> Other waves disponibles : Ramp Up (2), Ramp Down (3), Square (4).

**Ordre de réglage** : l'effet a d'abord été trouvé trop présent (Dry/Wet 0.5, wobble 0.55).
Il a été abaissé en deux temps — wobble 0.55 → 0.45, puis Dry/Wet 0.5 → 0.30 → 0.22 — jusqu'à ce
que l'écho redevienne un fond berçant sans se faire entendre comme un effet.

**Levier principal si retouche** : **Dry/Wet**. C'est lui qui dose l'intensité globale perçue.

### Batterie (index 0) — `Compressor → MEqualizer → MDelay`, variante « dub »

Objectif : faire basculer le morceau du reggae vers le dub, en faisant porter le mouvement par la
**caisse claire**. Le one-drop y est favorable : le kick et la caisse claire ne tombent que sur le 3,
donc les temps 1 et 2 sont **vides** et leave la place à un écho.

URI Melda : `query:Plugins#VST3:MeldaProduction:<Nom>`. **Pas** `query:AudioFx#…` — cette catégorie ne
contient que le stock Live.

| # | Device | Type | Réglages posés |
|---|---|---|---|
| 1 | `Compressor` | natif | Threshold 0.62, Ratio 0.35, Attack 0.2, Release 0.4, Makeup **On**, Sidechain **Off** |
| 2 | `MEqualizer` | Melda VST3 | **Aucun réglage — EQ plate.** Le carving n'est pas fait, volontairement (une étape à la fois) |
| 3 | `MDelay` | Melda VST3 | 2 taps synchronisés, Feedback 0.35 / 0.35, Gain tap 0.5 / 0.5, filtre actif Min 0.2 / Max 0.35 |

**`Compressor`** : colle la caisse claire et le kick ensemble, sans pompage. **Pas de sidechain** —
en one-drop le kick ne tombe que sur le 3, donc un pompage continu_createdait du vide sur les temps
1 et 2.

**`MDelay`** : les deux taps sont synchronisés sur la même subdivision, avec un filtre dans le
feedback (Min 0.2 / Max 0.35) → **chaque répétition perd ses aigus** et l'écho s'assombrit en
s'éloignant. C'est ce qui donne la profondeur du dub au lieu d'un simple claquement sec.

#### ⚠️ Deux angles morts à l'oreille — division de delay non vérifiable

- **`Type (Synchronization 1/2)` n'est pas lisible.** Valeur `is_quantized: true`, plage 0→1, mais
  `value_items: null` — l'outil MCP ne renvoie aucun libellé. Le plugin refuse la valeur 2 et
  accepte 1. **Impossible de savoir par lecture quelle subdivision est active.**
- **`Length (Synchronization 1/2)` = 0.643** est une valeur *normalisée 0→1*, pas une durée. Même
  défaut que les paramètres natifs : aucun affichage en Hz ou en notes.
- **`Delay mode` et `Filter mode` ont aussi été posés à l'aveugle** (valeur 1), sans libellé lisible.

**Conséquence** : ce que je *visais* musicalement est un écho pointé de la caisse claire retomphant
sur le contretemps du 3 (l'« and »), puis sonnant plus sombre à chaque répétition. **Seule l'oreille
peut confirmer que c'est bien ce qui se passe.** Si l'écho tombe ailleurs, il faut afficher la
division dans l'UI d'Ableton et la régler à la main, puis noter la valeur en clair ici.

#### 🪤 Piège évité — `MDelay` et le paramètre `Dry`

`Dry` de `MDelay` est un **niveau continu 0→1**, pas un interrupteur de routage. Le mettre à 0 ne
coupe pas l'envoi vers les taps : **ça supprime le signal sec et ne laisse que les échos.** Erreur
commise puis immédiatement corrigée (remis à 1.0). Même famille de piège que
`C3 = 60` : ne jamais supposer qu'un paramètre nommé comme un interrupteur en est un.

### Basse Deep Chill — paramètres du moteur (`Deep Chill Bass.adg`)

Relevés pour référence : Filter Cutoff 106, Filter Reso 26, Chorus Amount 18, Tone 54,
Attack 34, Release 82, Drive 24, Volume 116.7 (échelle 0-127).

## Notes de production

- **Convention de pitch : Ableton C3 = 60.** Donc C#2 = 49, G#2 = 56, et non 37 / 44 comme le
  donnerait la convention scientifique C4=60. Ne pas appliquer cette dernière.
- **Le kit `.adg` ne reproduit pas le mappage GM du fichier.** Les pads rechargés après
  l'incident (voir ci-dessous) ont été relus via `get_drum_pad_info` avant écriture des notes.
- **`load_drum_kit` a chargé un Drum Rack vide** (0 pad, 0 chaîne) sur cette installation. Le kit ne
  se charge correctement que via `load_instrument_or_effect` avec l'URI `FileId`. Charger le kit
  crée aussi un clip vide de 4 temps en slot 0 — à supprimer avant d'écrire le groove.
- **Incident : suppression de piste par nom.** `delete_track(track_name="4-Audio")` a supprimé la
  piste **0** (la batterie) au lieu de la piste audio visée. Le nom a été ignoré et l'index par
  défaut (0) utilisé. **Utiliser `track_index` explicite, et revérifier la session après chaque
  suppression.** La batterie a été recréée à l'identique.
- **David a demandé des gammes très riches** (« pas de limites, même très très riches »). À ce jour
  on est sur la fondamentale et la quinte. Les gammes riches (mineure naturelle, pentatonique
  mineure, passages modaux pour la couleur dub) restent à explorer quand la basse et le skank
  seront posés — non abordées volontairement à ce stade.

### Plugins Melda — ce qui existe et ce qui manque

Inventaire réel de cette machine (41 plugins Melda, forme d'URI
`query:Plugins#VST3:MeldaProduction:<Nom>`). Pour le mix : `MEqualizer` (seul vrai EQ 8 bandes —
Live 12 Lite n'a pas d'EQ Eight), `MDelay`, `MCompressor`, `MDynamicEq`, `MSaturator`, `MCharmVerb`,
`MComb`.

**Absents, à ne plus proposer :**

| Plugin | Conséquence musicale |
|---|---|
| `RetroBoy` | **Le réverb à ressort analogique n'existe pas ici.** C'est la signature du son batterie reggae/ska. Le plus proche est `MCharmVerb` court et fortement amorti — une **approximation**, à dire comme telle |
| `MFreeverb` | Remplacé par `MCharmVerb` |
| `MTransient` | Pas de shaper de transitoire → l'attaque de la caisse claire se travaille au compresseur |
| `MTurboComp` | Remplacé par `MCompressor` |
| `MDynamics` | Remplacé par `MDynamicEq` |

- **`list_external_plugins` est cassé** sur cette installation (erreur Python
  `'dict' object has no attribute 'lower'`). Pour inventorier les plugins, passer par
  `get_browser_items` sur le path `audio_effects`, ou par le skill `fx-lite` lui-même (corrigé).

## Historique de validation

| Étape | Contenu | Statut |
|---|---|---|
| 1 | Groove one-drop + kit `Selector Kit Warm`, 100 BPM, Do#m | ✅ **Validé à l'oreille** |
| 2 | Trois basses candidates + chaînes FX | ⏳ En cours — vague calibrée sur Deep Chill |
| 2a | Vague « whaouwhaouwha » — delay insert, ping-pong, offset, wobble LFO | ⏳ **En cours de réglage** |
| 2b | Chaîne dub batterie — `Compressor → MEqualizer → MDelay` | ✅ **Validé** après correction (taps 0.3, filtre Max 0.725) |
| 3 | Choix de la basse définitive | ⏸ **Suspendu** — `Deep Chill` conservée par défaut, les 2 autres supprimées pour l'audition skank |
| 4 | Skank « révolte douce » — 6 guitares candidates | ⏳ **Synergy Pluck Brasspreferred** (cuivres) — `Chord Key Stabs` supprimée par David |

## ✅ Fracture résolue — les paroles restent en français, la musique reste rub-a-dub

**David a tranché le 2026-10-04 :** l'en-tête de `PAROLES.md` avait été écrit **avant** que la
direction musicale ne soit donnée. Il ne décrivait donc pas le morceau. **Il a été corrigé** — le
style est bien ragga / rub-a-dub sombre, 100 BPM, one-drop, Do#m avec b2 phrygien, guitare
électrique. Le texte reste **en français** : la piste occitane de la direction initiale n'est pas
retenue.

| | Direction retenue |
|---|---|
| Style | ragga / rub-a-dub, clin d'œil Massilia Sound System |
| Tempo | 100 BPM, one-drop |
| Tonalité | Do#m + b2 phrygien |
| Langue | **français** |
| Guitare | électrique, skank sur contretemps |

**Reste à nettoyer dans `PAROLES.md`** (artefacts de la conversation source, pas des paroles) :
les marqueurs `[reference:0]` (pont) et `[reference:1]` (couplet 3), et la dernière ligne qui
propose une version courte ou une traduction. Non touché — fichier de David.

## Fichiers du morceau

| Fichier | Rôle | Auteur |
|---|---|---|
| `PAROLES.md` | Texte des paroles + structure des sections | **David** |
| `Conversation.md` | Conversation d'origine, extraite en markdown | **David** |
| `Sauvage_Méditerranée_conversation.json` | Source originale | source |
| `FICHE_TECHNIQUE.md` | Ce document | moi |
| `01 - One-Drop Base.md` | Groove validé | moi |
| `02 - Basse + FX.md` | Basse et FX | moi |
| `03 - Skank 6 candidats.md` | Audition skank — **périmé** : 5 candidates, `Chord Key` supprimée | moi |

## Journal de réglage de la vague

Trace chronologique, pour pouvoir revenir en arrière.

| Ordre | Action | Valeur | Verdict à l'oreille |
|---|---|---|---|
| 1 | Delay posé sur le **return B**, send de Deep Chill à 35 % | Delay en double-croche (L/R 16th = 2) | « Ça suit trop le rythme tactactac » — l'écho tombait pile sur les charleys |
| 2 | Retard allongé en pointé + ping-pong + wobble | L/R 16th = 6, Ping Pong = 1, LFO Mode = 1, LFO Freq = 0.15, LFO > Delay = 0.35, Feedback = 0.45 | « Ça va, mais il faut plus de vague, plus marquée et présente » |
| 3 | Retourné en **insert sur la piste**, return B remis à zéro | Dry/Wet 0.5, wobble 0.55, Offset 0.33 | « Beaucoup trop présent » |
| 4 | Atténué | wobble 0.55 → **0.45** ; Dry/Wet 0.5 → **0.30** | Toujours trop présent |
| 5 | Atténué davantage | Dry/Wet 0.30 → **0.22** | Retenu — vague en arrière-plan |
| 6 | Wobble rendu non périodique | LFO Wave 0 (Sine) → **5 (S & H)** | En cours d'écoute |

**Leçons pour la suite :**
- Le delay en double-croche est **à éviter** dès qu'une piste rythmique est presente : l'écho
  double le tic et donne un effet « tactactac ».
- **L'insert vaut mieux que le send** pour un effet de caractère : un send vers un return comuns
  contamine tous les instruments futurs qui y sont envoyés.
- **Le Dry/Wet est le levier d'intensité**, pas le feedback. C'est le premier paramètre à baisser
  quand un delay «whelcom ».
- La **sinusoïde** est le pire choix pour un wobble : périodique donc mécanique. Utiliser S & H
  (ou Wander) systématiquement quand on cherche du naturel.