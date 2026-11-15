# Fiche technique — Time (Pink Floyd) [remake]

Source : `Time/Pink Floyd — Time [MIDIfind.com].mid`
Tempo : 124 BPM | Signature : 4/4 | Durée : ~5 min | 156 bars
Fusion : 10 pistes source → ≤7 instruments + 1 voix.

## Pistes (indices 0-based, mapping proposé)

| Ableton | Instrument proposé | Source |
|---|---|---|
| 0 | 1-Batterie+Perc | Woodblock + Drumkit ×2 (le woodblock = intro cloche) |
| 1 | 2-Guit Rythm | Rythm Guitar |
| 2 | 3-Guit Lead | Lead Guitar |
| 3 | 4-Basse | Bass |
| 4 | 5-EP/Keys | Electric Piano + Keyboard |
| 5 | 6-Libre | — |
| 6 | 7-GuideVocal | Vocals Gilmour + Wright (guide) |
| 7 | 8-Voix (audio) | ta voix |

## Scènes (à valider — ambient→rock)

| Scène | Bars | Beats | Note |
|---|---|---|---|
| 0 | 1–4 | 16 | intro sparse (ambiant) |
| 1 | 5–15 | 44 | montée |
| 2 | 16–43 | 112 | groove |
| 3 | 44–75 | 128 | break (chute densité bar ~43) |
| 4 | 76–105 | 120 | retour |
| 5 | 106–156 | 204 | final |

## Active Drumkit = très rempli (543 notes sc2). FACTORISER (woodblock intro à part + groove + fills).

## Options / forks (TODOs)
- [ ] **Intro woodblock** : le "marteau" des horloges au début = à garder distinct (piste séparée ou
      intro). Heavy rock ensuite.
- [ ] **Cloche/clock** : vérifier si les horloges sont dans une piste ; sinon les poser sur sc0.
- [ ] **Guit** : Time = guitares rocks (rythm + lead overdrive). Guit Electric Clean → ajouter un
      saturator/distortion, ou Axe Of Velvet, ou Surge disto. Tester clean vs saturé.
- [ ] **Basse** : fondamentale rock → Electric Bass Soft + Saturator Bass Shaper (comme Keep Talking).
- [ ] **Keys** : EP + orgue → Electric (Wurlitzer) + Warm Analog, ou Surge.
- [ ] **Guide vocal** : Sweet Lead / Radio Lead.
- [ ] **Structure** : le break (sc3) = moment clé "le temps file" — espace/drop rythmique à
      magnifier. Paroles : le temps qui passe, "the time is gone, the song is over".
- [ ] **CPU** : sc2 très dense (543 batt) → factoriser + possiblement geler.

## À faire
- [ ] Charger instrus + FX | tweak + capture | dupliquer arr. | mix 6 étapes + master

## Outils
notes : `_scenes_notes.json` | prep : `prep_midi.py` / `prep_anycolour_group.py`
