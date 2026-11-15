# « Faut des Parts » — Strates@Gemmes (2001) — Reimagining contemporain

## Objectif
Réinventer l'album de 2001 avec un son 2026. On **garde les voix originales** (impossibles à refaire)
et on reconstruit une moquette instrumentale moderne par-dessus, dans Ableton Live Lite.

## Sources
- Archive.org : https://archive.org/details/StratesGemmes/ (MP3 128k, uploadé 2007)
- Fichiers WAV 22050 Hz mono générés dans `00_source/wav/` (décodage librosa)

## Analyse technique (clé · tempo estimé · durée)

| # | Titre | Clé | Tempo (bpm) | Durée (s) | Durée (mm:ss) |
|---|-------|-----|-------------|-----------|----------------|
| 1 | Totale Emprise      | A mineur  | ~144 | 195.8 | 3:16 |
| 2 | Wake Up             | C# mineur | ~136 | 241.2 | 4:01 |
| 3 | Sauce y était       | E mineur  | ~129 | 282.8 | 4:43 |
| 4 | Eve (cherrito)      | E mineur  | ~136 | 246.7 | 4:07 |
| 5 | 6 T'aime            | E mineur  | ~108 | 275.5 | 4:36 |
| 6 | Raide Iz Dead       | A mineur  | ~144 | 246.5 | 4:06 |
| 7 | vErs zIOn 1         | B mineur  | ~144 | 191.9 | 3:12 |
| 8 | Marylene            | A mineur  | ~136 | 356.6 | 5:57 |

**Total album : ~33:40**

Notes :
- Tempo estimé par onset/autocorrélation — risque de moitié/double. À confirmer à l'oreille dans Ableton (warp).
- Quasi tout l'album est en **mineur** — cohérent avec une ambiance sombre/nostalgique 2001.
- Tonalités voisines (A, C#, E, B) : très cohérentes, transitions faciles entre pistes.

## Méthode de travail
1. Charger chaque piste originale dans une session Ableton (piste "VOCAL/FRAME" audio).
2. Identifier la structure (intro/couplet/refrain/pont) + tempo réel à l'oreille.
3. Reconstruire beats, basse, harmonies, textures 2026 autour de la voix/matériau original.
4. Mixer + masteriser chaque morceau (workflow mix complet + mix-translation).

---

## Template « Totale Emprise » (piste 1) — en cours

**Session :** 144 bpm, 4 pistes.

| Piste | Type | Device | Volume | Rôle |
|-------|------|--------|--------|------|
| BASS  | MIDI | 808 Drifter | 0.75 | Basse 808, ligne Am racine + octave (à affiner contre l'harmonie réelle — non convainquant pour l'instant) |
| SRC   | Audio | Utility + EQ Three (GainHi 0.65, GainMid 0.92) | 0.7 | Piste originale 2001 warped — matière première/voix. Carving : dompte la brillance MP3 128k |
| BEAT  | MIDI | Big Break Kit | 0.8 | Beat trap 2026 : kick 1&3 half-time, clap, hats swingées — VALIDÉ par David |
| PAD   | MIDI | Chord Eno Pad | 0.6 | Nappe Am–F–C–G (i–VI–III–VII) — à ajuster selon l'harmonie réelle |

**Structure (validée par David) :** Intro (bars 1-4) → Verse 1 (4-25) → Pré/Refrain (25-51) → Transition (51-57) → Verse 2 (57-69) → Bridge (69-81) → Refrain final (81-105) → Outro (105-117).
Beat posé sur les sections actives (gaps aux intro/bridge/outro).

**Mastering :** Master 1.0. Chaîne master = Compressor glue (Threshold 0.7 / Ratio 0.4 / Release 0.3) → Limiter (True Peak, Lookahead 3 ms, Ceiling 0.95). Résultat sur Head (refrain final ~beat 330) : RMS 0.184 / DR 14.7 / centroid 2516. VALIDE (en attente de validation oreille finale).

## ⭐ Philosophie de travail RÉVISÉE — « Doubler » (décision 2026-08-26)

Trouvé avec David : **pas de reconstruction en boucles**, mais :
1. **Garder le SRC entier** (mix 2001, voix comprise dès le départ) — matière première.
2. **Doubler l'existant en ÉCARTS RYTHMIQUES** : les couches 2026 RÉPONDENT au SRC (guitare en contre-temps, batterie call-and-response) plutôt que doubler à l'unisson.
3. **Suivre les MONTÉES** : ajouter **risers (swoosh/white-noise) + accumulation aux pics** d'énergie.
4. Petites « couches par-dessus » le mix original.

**Pics de montée détectés (par barre, mix original) :** 16, 24, 34, 72-75, 108-115. Dernier fade barre 117 (~ -65 dB).

**Caractère du SRC :** guitare TRÈS saturée partout → centroid haut (2700→5419 Hz), brillance écrasante (4-8k ≈ 30%, 8-20k ≈ 18%). C'est LE trait à manager dans le mix (et à doubler intelligemment).

**Le SRC est à ~143.55 bpm reels** (source WAV), session à 144. Warp du clip SRC : non persistant via API (Live désactive le warp faute d'analyse exploitable sur MP3 128k) — à résoudre dans Ableton à la main si besoin.

### Découverte technique (capture)
- La **capture_and_analyze est muette quand une piste est en SOLO en arrangement** (RENVOIE un WAV de silence RMS 0). Toujours désolo avant toute capture.
- Le `output_name` doit être unique — l'analyse peut renvoyer des résultats en cache si le nom est réutilisé à une position similaire.
