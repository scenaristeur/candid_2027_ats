# 06 — Le Trône de Papier

**Tempo**: 70 BPM (ballade) → 140 BPM (rock)
**Tonalité**: Sib majeur (Bb) → Fa majeur (F)
**Durée**: ≈ 4 min (estimé)
**Atmosphère**: Opéra rock, majesté puis explosion
**Style**: Hommage Queen
**Voix**: Baryton « le grand écart » — poitrine profonde (Do3) en ballade → mixte aigu (Fa4) à l'opéra

## Hommage
- Queen : grand écart ballade/opéra, chœurs lyriques, piano réverbéré, dramatique
- Français (2026) : production cinématique, le baryton comme instrument de majesté
- Le baryton apporte une majesté naturelle à ce style — les aigus du rock opéra sont tenus, jamais criés

## Structure (en barres)
Intro Piano (8) | Ballade (16) | Chœurs opéra (8) | Rock (16) | Fin piano (8)

## Grille d'accords

| Section | Grille (4 mesures) | Couleur / Sonorité |
| :--- | :--- | :--- |
| **Ballade** | `| Bb | Gm | Eb | F |` | Sib majeur : noblesse ; le Gm (vi) apporte l'ombre. |
| **Opéra / Rock** | `| F | Bb | C | F |` | Modulation en Fa majeur : l'éclat, l'explosion. |

## Instruments (Ableton)

| Piste | Son | Effets | Rôle |
| :--- | :--- | :--- | :--- |
| **Grand Piano** | Piano à queue | Réverb convolution (cathédrale) | Le pilier de la ballade et de la fin. |
| **Guitare** | Électrique | Phaser | Texture pendant le rock, arpèges sur la ballade. |
| **Chœurs** | Looper vocal (5 pistes d'harmonies) | Volume 0 → +6 dB à l'opéra | Les « Glory ! Glory ! » lyriques qui écrasent tout. |
| **Batterie** | Kit | Toms + crash en crescendo | Pas de kick frontal en ballade — l'explosion vient au rock. |
| **Voix** | Baryton | Poitrine → mixte | Do3 profond en ballade, Fa4 tenu à l'opéra. |

## La Voix Baryton — Ligne de chant

- **Ballade** : poitrine profonde (Do3) — la majesté calme du roi déchu.
- **Opéra** : mixte aigu (Fa4) — le drame, les « Glory ! Glory ! ».
- **Rock** : la voix explose avec les chœurs, mais le sommet reste tenu et maîtrisé.
- **Final** : murmuré, « ... juste un souffle sur du papier. Un souffle... et puis rien. »

## La Chaîne Vocale Ableton

- **Micro** : SM7B (ou U87 pour le côté « grand »).
- **Chaîne** : EQ8 (coupe 80 Hz, boost 160 Hz et 4 kHz) → Compresseur Glue 3:1 (attack 10 ms) → Réverb cathédrale (A-Reverb) plus présente que sur les autres titres.

## Automations de Scène (à dessiner au mixage)

| Moment | Automation | Effet produit |
| :--- | :--- | :--- |
| **Entrée des chœurs opéra** | Volume des chœurs 0 dB → +6 dB | Les chœurs écrasent tout — l'apothéose lyrique. |
| **Partie opéra** | Réverb du piano en mode « cathédrale » | Le piano devient immense, majestueux. |

## 6 bis. État de la maquette MIDI + Automations à faire au mixage

> **Statut (août 2026) :** MAQUETTE MIDI TERMINÉE — vérifiée via MCP. Arrangement construit (480 beats = **120 barres**, 70 BPM). **Structure réelle bien plus développée que la fiche :** 9 sections au lieu de 5. Voix pas encore enregistrée (piste audio vide). Automations ci-dessous à appliquer au mixage final (dessin manuel dans Live — API Python non fiable pour les enveloppes d'arrangement).

### Structure réelle (vérifiée, 120 barres)

| # | Section | Barres | Beats | Piano | Guitare | Batterie | Orgue |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Intro | 8 | 0-32 | Intro Piano | Pre-Intro Guitare | — | — |
| 2 | Ballade Fusion | 16 | 32-96 | Ballade Fusion Piano | Ballade Fusion Guitare | Pre-Opera (64-96) | — |
| 3 | Opéra | 8 | 96-128 | Opera Piano | Opera Guitare | Opera Drums | — |
| 4 | Rock | 16 | 128-192 | Rock Piano | Rock Guitare | Rock Drums | Pre-Funky Orgue |
| 5 | Funky | 16 | 192-256 | Funky Piano | Funky Guitare | Funky Drums | Funky Orgue |
| 6 | Climax | 16 | 256-320 | Climax Piano | Climax Guitare | Climax Drums | Climax Orgue |
| 7 | Final Dance | 16 | 320-384 | Final Dance Piano | Final Dance Guitare | Final Dance Drums | Final Dance Orgue |
| 8 | Redescente | 16 | 384-448 | Redescente Piano | Redescente Guitare | Redescente Drums | Redescente Orgue |
| 9 | Fin | 8 | 448-480 | Fin Piano | — | — | — |

### Vérification session (août 2026)

| Piste | Nom session | Volume | Arm | Devices | Clips session | Arrangement |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | Piano | 0.82 | non | Grand Piano + Compressor + ValhallaSupermassive | 12 clips (Intro, Ballade, Opera, Rock, Fin, Ballade B, Funky, Climax, Ballade Fusion, Final Dance, Redescente, Fin) | 9 clips 0→480 |
| 1 | Guitare | 0.75 | **oui** | Guitar Electric Clean + MPhaser + Compressor + MFlanger + MAutopan | 10 clips | 8 clips 0→448 |
| 2 | Voix | 0.85 | non | — | vide | — |
| 3 | Batterie | 0.82 | non | Gen Purpose Kit + Compressor | 8 clips | 7 clips 64→448 |
| 4 | Orgue | **0.60** | non | Organ Analog + Reverb | 5 clips | 5 clips 128→448 |
| Master | Master | 0.85 | — | Limiter + MEqualizer | — | — |

Notes de vérification :
- **Batterie n'entre qu'au beat 64** (Pre-Opera, fin de la Ballade) — pas de kick frontal en ballade, conforme à la fiche. L'Orgue n'entre qu'au beat 128 (Rock).
- **Guitare armée** (prête pour enregistrement audio) — l'arm est actif.
- Sends déjà routés : **Guitare A-Reverb 0.30 / B-Delay 0.15**, **Orgue A-Reverb 0.15**, **Piano A-Reverb 0.08 / B-Delay 0.08**. Batterie 0/0.
- Le Rock Drums est dense : kick en croches continues (vélocités 115-127), snare sur 2&4, crash → l'explosion est construite (double-pédale).
- Tempo : 70 BPM en session — vérifier le **changement 70 → 140 BPM** à la bascule ballade → opéra (fiche initiale) : à confirmer si automatisé dans la timeline.
- Clips supplémentaires vs fiche : « Ballade Fusion », « Funky », « Climax », « Final Dance », « Redescente » — la maquette a évolué vers une forme live plus longue.

### To-do automations (au mixage)

| # | Moment | Action | Paramètre | Cible |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Entrée chœurs opéra | Volume chœurs 0 → +6 dB | Volume piste | Piste Chœurs |
| 2 | Partie opéra | Réverb piano « cathédrale » | Send A-Reverb | Piste Piano |

## Production Notes

- Le changement de tempo 70 → 140 BPM se fait à la bascule ballade → opéra.
- Toms et crash en crescendo à l'entrée du rock : l'explosion se construit avant d'arriver.
- Les chœurs « Glory ! Glory ! » : 5 pistes d'harmonies (looper vocal) pour le chœur lyrique.
- Pas de kick frontal en ballade — la batterie n'entre vraiment qu'au rock.

## Notes live (set)

- L'apothéose théâtrale du set : confettis, moment opéra, lumière dorée.
- Le chanteur lâche le Fa4 tenu — le public retient son souffle.
- Le final piano murmuré fait retomber le silence avant « Poussières d'Étoiles ».

## Paroles
Voir `PAROLES.md` dans ce dossier.
