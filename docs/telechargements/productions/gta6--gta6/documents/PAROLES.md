# Vice City, Inc. — Fiche Technique & Paroles

**Tonalité :** Sol mineur (Gm) — progression Gm → Eb → F → D
**Tempo :** 138 BPM
**Signature :** 4/4
**Groove :** MPC 16 Swing (~60%) appliqué à batterie + basse
**Style :** Trip-hop / dub à la Gorillaz (« Feel Good Inc. ») — sale, bancal, cynique, en retard sur le beat
**Guide voix :** Piste 5 « 4-Lead Whistle » (Theremin Whistle) pour le hook
**Tessiture guide :** baryton/ténor confortable

**Structure (mesures) :** Intro (8) → Couplet 1 (8) → Pré-refrain (4) → Refrain (8) → Couplet 2 (8) → Pré-refrain (4) → Refrain (8) → Pont (4) → Refrain final (8) → Refrain final 2 (8) → Outro (4)

---

## Fiche Technique — Production

### Pistes (indices MCP, 0-based)

| Index | Nom piste | Type | Instrument / Contenu | Rôle |
|---|---|---|---|---|
| 0 | 1-Drums | MIDI | Big Break Kit (Drum Rack GM) | Batterie half-time « sale » |
| 1 | 2-Basse | MIDI | Drift | Basse mélodique ronde Gm-Eb-F-D |
| 2 | 6-Voix Rap | Audio | — | Couplets rap (en retard, parlé-chanté) |
| 3 | 7-Voix Chant | Audio | — | Refrains planants falsetto grave |
| 4 | 3-Wurli | MIDI | E-Piano Wurli | Nappes / pads harmoniques |
| 5 | 4-Lead Whistle | MIDI | Theremin Whistle | Hook mélodique (intro, refrains, pont) |
| 6 | 5-FX Audio | MIDI | Surge XT (instance 1) | Risers / quack / tension |
| 7 | 8-Surge XT | MIDI | Surge XT (instance 2) | Nappes de tension (couplet 2, refrains finaux) |

**Complexité globale :** 8 pistes de Session (Lite max) — le Couplet 2 et les refrains finaux viennent superposer les 2 Surge XT.

### Scènes Session (blocs en Vue Session)

| Slot | Scène | Drums | Basse | Wurli | Whistle | Surge | Mesures |
|---|---|---|---|---|---|---|---|
| 0 | Intro | — | — | Pad Gm/Eb | Hook | — | 8 |
| 1 | Couplet 1 | Groove | Gm-Eb-F-D | Pad | — | — | 8 |
| 2 | Refrain | Groove | Root bounce | Accords ouverts | Hook | — | 8 |
| 3 | Pré-refrain | Build | — | — | — | Riser montant | 4 |
| 4 | Couplet 2 | + densité | + 8èmes | Pad | — | Nappe tension | 8 |
| 5 | Pont | Call&Resp | — | — | Resp | Risers | 4 |
| 6 | Refrain final | Groove | Root | Accords | Hook | Nappe | 8 |
| 7 | Refrain final 2 | Groove | Root | Accords | Hook +2t | Nappe épaisse | 8 |
| 8 | Outro | — | — | Pad final | Vent+sirène | — | 4 |

### Surge XT — plan de montée de tension

- **Instance 1 (piste 6, `5-FX Audio`)** → effets de tension : risers (bruit blanc montant), sweeps, « quack ». Patches candidats : `FM Riser`, `Sweep Noise Up-Down`, `8 Measure Noise & Comb Sweep`.
- **Instance 2 (piste 7, `8-Surge XT`)** → nappe de tension musicale. Patch retenu : **`Brass Pad`** (Nick Moritz) — remplace `Sweeping Distorted Pad` (inaudible RMS 0.027 + CPU lourd : 11 voix unison, Ensemble + Reverb). Brass Pad = 3 osc Classic × 2 voix, tous FX off, polyphonie 6 → **audible (RMS 0.262 solo)** et léger.
- **Couplet 2** : la nappe Surge entre en fond dès la 2e mesure, filtre qui s'ouvre progressivement.
- **Refrain final / Refrain final 2** : nappe épaisse + riser avant chaque impact ; sur le RF2 la nappe grimpe d'un ton dans l'aigu pour accompagner le whistle +2.
- **Contrôle OSC** : 8 instances max (IN 53280 + stride), patchs chargés via `surge-osc`. Meilleur levier CPU = **voix unison** (`/param/a/osc/N/param7`) + FX internes (`/param/fx/a/N/deactivate=1`, `/param/fx/send/2/type=0`). Configs filtres 0-7 = toutes 2 filtres (pas de « Single »).

### Réglages de mix (translation gros-baffles / smartphone)
- HPF ~150–200 Hz sur tout sauf kick/basse.
- Basse sur **Drift** : triangle + carrée, low-pass ~400 Hz, distorsion légère pour l'harmonique « proche sub ».
- Wurli en stéréo large ; basse + kick en mono serré.
- Sidechain léger basse sur kick.
- Master : Compressor glue (Thres 0.7 / Ratio 0.4 / Release 0.3) → **Limiter True Peak** (Lookahead 3 ms / Ceiling 0.95) → **fader master 1.0** (il est en aval des FX).
- Centroid cible ~700–900 Hz.

### Premix appliqué (2026-09-01, Refrain final = référence)
- **Staging** : pistes à 0.62-0.68, master 1.0 (voir calibration plus bas).
- **EQ Three piste 1-Drums** (device 1) : GainLo 0.6 (dégraisse le sub), GainHi **flat 0.85** (le doux est géré au pad).
- **EQ Three piste 2-Basse** : GainMid 0.98 (boost léger = audibilité mid sans toucher au sub). Basse solo : 25% sub, 7% 4-8k → source propre.
- **EQ Three piste 3-Wurli** : GainLo 0.7, GainHi 0.5 (assombrit, évite le masquage bas).
- **EQ Three piste 8-Surge XT** (device 1) : GainLo 0.72 (coupe le corps 100-250 Hz du Brass Pad, laisse le bas à la basse).
- **Charley = note 42 dans le Drum Rack imbriqué** : Volume 0.325 → **0.22** (≈ -3 dB). Verdict des captures solo : **les drums étaient LA source du 4-8 kHz** (51% via charley/crash), pas le whistle (85% en 500-1000 Hz), basse (7%), riser FM (0%), Surge pad (3%).
- **Dynamique** : Compressor parallèle basse (Dry/Wet 0.4, Threshold 0.8, Ratio 0.5) — glue invisible au spectre, à juger à l'oreille.
- **Profondeur** : Reverb en insert whistle (Dry/Wet 0.2, Room 0.45, Decay 0.4) — returns inaccessibles via MCP (workaround fiable).
- **Master** : Compressor glue (0.7/0.4/0.3) + **Limiter True Peak** (Mode=2, Lookahead=1→3ms, Ceiling 0.95) + fader 1.0.
- **Calibration staging → master** (leçon) : avec toutes les pistes à 0.85 + master 1.0 → RMS 0.40 / DR 7.9 (limiter écrasé). Baisser en 2 paliers → **pistes 0.62/0.68 → RMS 0.194 / DR 14.3**. L'entrée limiter doit laisser le glue travailler, pas le forcer au mur.
- Résultat RF final : **RMS 0.194, DR 14.3, centroid 906 Hz** (départ: 0.238/12.5/1433).

---

## Légende des annotations

- `D2 ◷3` = note D2 tenue 3 temps — attaquer la syllabe suivante sur cette note
- `→` = enchaînement sans nouvelle attaque
- `...` = silence / respiration
- **(…)** = echo / réponse vocale en fond

---

## Les Paroles — Version Française

**(Intro – Voix déformée / Filtre radio façon 2D)**

*La haine s'écrase sur le tableau d'bord...*
*On attend la nuit, l'odeur du remord...*

---

**(Couplet 1 – Rap posé, grave et en retrait)**

Téléphone en main, j'scanne les leaks à 3h du mat'
Rockstar a lâché l'trailer, j'l'ai bouclé vingt fois d'affilée
Jason et Lucia, les rois du braquage en acier
La carte est deux fois plus grande, l'océan presque réel
Six étoiles sur le toit, j'suis pas là pour les perdre
J'traîne au coin d'la rue, la sub qui fait trembler les vitres
Des années qu'on attend, on a joué les apprentis
Maintenant l'sequel débarque, la hype est en sursis

---

**(Pré-refrain – Parlé sur un filtre passe-bas)**

*La ville fond... La manette tremble...*
*Voilà l'séisme... J'perds les repères...*

---

**(Refrain – Mélodie planante, falsetto grave)**

GTA... *(GTA...)*
L'vent d'la Vice... *(L'vent d'la Vice...)*
On flotte dans un brouillard d'néons... *(néons...)*
À compter les jours et les saisons... *(saisons...)*

GTA... *(GTA...)*
N'tue pas l'vibe... *(N'tue pas l'vibe...)*
On danse sous un ciel à six étoiles... *(étoiles...)*
Ce soir, on s'en fout, on est trop haut pour eux... *(pour eux...)*

---

**(Couplet 2 – Rap plus incisif, toujours cynique — tension qui monte)**

Les politiques veulent censurer, les corpos veulent porter plainte
Mais nous, on veut juste une caisse volée, une autoroute sans contrainte
La satire est acérée, ça cogne comme un poing dans la gueule
Ils nous vendent du rêve, on achète juste l'fun et la gueule d'bois qui s'ensuit
La préco est validée, l'disque tourne dans l'lecteur
Treize ans d'attente pour un monde virtuel, quel ascenseur
Alors pousse le son, fais péter les haut-parleurs
GTA 6 arrive, c'est notre seule lueur

---

**(Pont – Partie aérienne, "la la la" ou "oh oh")**

Oh, oh-oh, Vice City m'tend les bras...
Oh, oh-oh, on n'est qu'des pions dans l'grand chaos...

---

**(Refrain final – x2, en montant dans l'aigu)**

*(Même phrasé que le Refrain, chant plus déchiré sur la 2e)*

---

**(Outro – La basse s'arrête, ne reste que le vent et les sirènes lointaines)**

---

## Rappel notes MIDI (pitch → note)

| Pitch | Note | Usage |
|---|---|---|
| 38 | D2 | Basse (racine D) |
| 39 | Eb2 | Basse (racine Eb) |
| 41 | F2 | Basse (racine F) |
| 43 | G2 | Basse (racine G) |
| 60 | C3 | Référence Wurli pad |
| 64 | E3 | Hook / guide voix |
| 67 | G3 | Hook / guide voix |

## Notes d'adaptation

- **Couplet 1** : placer les mots **en retard** sur le beat (laisser traîner « mat' », « réel ») ; le Groove MPC 16 Swing donne le bounce.
- **GTA** : chanter sur 3 notes descendantes (Gé=T3, Té=R3, A=Mi) version chevrotante 2D.
- **néons / saisons** : tenir la dernière syllabe (allonger le « on ») pour le chœur.
- **Refrain final** : monter d'un demi-ton sur la reprise pour l'émotion (« étoiles »).
- **Voix rap** : une prise sans trop articuler, bitcrush léger (Redux) sur le couplet 1 façon talkie-walkie.
- **Voix chantée** : doubler la voix du refrain, pan ±40 %, Chorus-Ensemble.