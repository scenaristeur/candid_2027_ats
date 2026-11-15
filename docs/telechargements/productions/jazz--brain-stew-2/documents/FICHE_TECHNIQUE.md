# Brain Stew 2 — Fiche Technique

**Chanson** : Brain Stew (Green Day) · **Version** : Jazz / Torch-song façon **Postmodern Jukebox** (réf. "Creep" feat. Haley Reinhart)
**Projet Ableton** : Live Lite · **Tempo** : 80 BPM · **Mesure** : 4/4 · **Durée arr.** : ~3:36 (72 mesures)

## Structure / Arrangement

| Section | Mesures | Contenu |
|---|---|---|
| Intro | 1-8 | Riff Brain Stew (Rhodes) + **Riff Punch cuivres** (octave au-dessus) + stabs basse + balais |
| Verse 1 | 9-16 | Riff + walking bass + balais |
| **Hook "here we go"** | 17-18 | A→E→A, lift batterie + **Hook Punch cuivres** |
| Verse 2 | 19-26 | + vibraphone réponse |
| **Hook** | 27-28 | + Hook Punch |
| Verse 3 | 29-36 | + cuivres (Surge) + vibra |
| **Hook** | 37-38 | + Hook Punch |
| **Solo** | 39-54 | Lead Surge (16 mes.) sur la grille du riff |
| Verse final | 55-62 | Reprise douce + vibra (redescente) |
| **Hook** | 63-64 | + Hook Punch |
| Outro | 65-72 | Tag riff + stabs + balais |

**Positions Hook Punch** (arrangement, en temps) : 64, 104, 144, 248.
**Riff Punch** : intro uniquement — cuivres = riff Brain Stew doublé à l'octave (vél 86/78).

Grille (2 mes.) : **A – G – F# – F – E** (la mineur avec chromas F#/F). Riff = power chords à trous, doubles attaques 16e (fidèle au `.mid` original).

## Pistes / Instruments (6 MIDI, 2 returns)

| Piste | Device | Rôle | Notes son |
|---|---|---|---|
| 0 | Vintage Keys — E-Piano Rhodish | Riff + comping | Cutoff 62, Space 55 ; **Volume 1.0** |
| 1 | Upright Bass (Simpler) | Stabs intro/outro, walking verses | Filter Drive 1.5 |
| 2 | Tenor Sax → **Surge (brass)** | **Cuivres** (V3) + **Riff Punch / Hook Punch** | `Bread & Butter Synth Brass` : 3 oscs (osc3 vol 0.5) + noise + 1x2/2x3 (0.05-0.1) + unison + drift + vibrato LFO (depth 0.025) |
| 3 | Brushed Drums — Gen Purpose Kit | Balais swing | kick 1&3, balai 2&4, ride swing |
| 4 | Vibraphone | Réponses dans les trous (Am/F#m/Em) | vélos ~46-59, **Volume 0.7** |
| 5 | Lead Funky → **Surge (lead)** | **Solo** | `Classic Lead 2` : filtre Legacy Ladder, 3 oscs + 1x2/2x3 (0.08/0.06) + unison + FEG + drift |

## Sound Design — état actuel

- **Brass (inst 0)** : 3 oscs actifs, filtre OB-Xd, noise+1x2+2x3 discrets, vibrato LFO léger (0.025)
- **Lead (inst 1)** : `Classic Lead 2`, filtre Legacy Ladder, 3 oscs + ring mods + unison + FEG + drift → **validé à l'oreille**
- **Riff Punch** : octave haute, vél 86 (tps) / 78 (échos) — l'énergie du riff est portée par les cuivres, pas seulement le Rhodes
- Analyse capture solo : spectral centroid ~480 Hz → **mix sombre**, présence haute à gagner au mix

## Points d'attention client

- **Trop loin de l'original** Brain Stew → recadré : riff mis devant (Riff Punch intro + Hook Punch hooks), 80 BPM conservé
- **Vintage PMJ perdu** → repasser en torch-song plus chaud/dépouillé
- Direction proposée : instruments **Surge uniquement** (sauf drums native + effets), re-capture vintage — à finaliser
- **Reste à faire** : No Mix → mix complet (présence, EQ, saturation, réverb) puis validation capture + oreille ; enregistrer la voix (David, anglais) ; tracks restants 1 MIDI + 1 audio
- Sauvegarde : `save_project` indisponible via API → **Ctrl+S manuel** dans Ableton

## Références externes

- Riff original : `C:/Users/Public\Music\midi\Brain-Stew.mid`
- MIDI parsers : `_parse_midi.py`, `_timeline.py`, `_gen_riff.py`, `_gen_verse1.py`, `_gen_solo.py`, `_gen_hook.py`, `_gen_riff_punch.py`
- Presets Surge : `doc_surge/presets/PRESETS.md` · OSC référence : `doc_surge/surge_OSC.md`
