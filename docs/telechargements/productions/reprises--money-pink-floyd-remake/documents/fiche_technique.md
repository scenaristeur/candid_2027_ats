# Fiche technique — Money (Pink Floyd) [remake]

Source : `Money/Pink Floyd — Money [MIDIfind.com].mid`
Tempo : 120 BPM | Signature : 4/4 (le .mid est en 4/4 ici) | Durée : ~7.3 min | 124 bars
Fusion : 14 pistes source → ≤7 pistes instruments + 1 voix.

## Pistes (indices 0-based, mapping proposé)

| Ableton | Instrument proposé | Source |
|---|---|---|
| 0 | 1-Batterie+Percs | Vibraslap, Guiro, Triangle, Shaker, Jingle Bell, Drumkit ×2 |
| 1 | 2-Guit Rythm | Rythm Guitar + Rythm/Lead Guitar |
| 2 | 3-Guit Lead | Lead Guitar |
| 3 | 4-Basse | Bass |
| 4 | 5-EP/Sax | Electric Piano + Sax |
| 5 | 6-Libre | — |
| 6 | 7-GuideVocal | Vocals |
| 7 | 8-Voix (audio) | ta voix |

## Scènes (à valider à l'écoute — temporaire)

| Scène | Bars | Beats |
|---|---|---|
| 0 | 1–6 | 24 |
| 1 | 7–14 | 32 |
| 2 | 15–24 | 40 |
| 3 | 25–40 | 64 |
| 4 | 41–56 | 64 |
| 5 | 57–75 | 76 |
| 6 | 76–96 | 84 |
| 7 | 97–124 | 112 |

## Factorisation batterie (top xN)
Drums sc3 x3, sc6 x3, sc7 x19 (très répétitif) → FACTORISER en groove court + fills.
Vérifier aussi guit/keys (lapercussions déjà isolées dans le .mid = atout).

## Options / forks (TODOs)
- [ ] **Batterie** : percs isolées (guiro, triangle, shaker, jingle) = chaque perc sur un pad du rack.
      Kit : Selector Warm / Foundation Dance / Drum Machine Selector à tester selon l'énergie voulue.
- [ ] **Guit** : les 2 guitares rythm (overdrive) : Guitar Elect Crit / Axe Of Velvet → tester distortion
      vs clean pour l'énergie "money".
- [ ] **Sax** (Parry) : chercher un preset sax/wind natif, sinon Surge (Les cuivres/) — sinon doubler
      avec un lead lead synth chaud.
- [ ] **EP** : Wurlitzer/EP natif (Electric) ou Surge EP — pour le groove funky.
- [ ] **Thème** : l'argent, le groove répétitif hypnotique (7/4 à l'origine) → riche pour un remake
      dance/funky. Paroles : critique, cynique, le "file tax" de Waters.
- [ ] **CPU** : 8 pistes + percussions multiples → surveiller get_cpu_load, fusionner si lourdeur.

## À faire
- [ ] Charger instrus + FX
- [ ] Tweak + capture + validation
- [ ] Dupliquer arr. (destination_time beats)
- [ ] Mix 6 étapes + master glue+limiter

## Outils
notes : `_scenes_notes.json` | prep : `prep_midi.py` / `prep_anycolour_group.py`
