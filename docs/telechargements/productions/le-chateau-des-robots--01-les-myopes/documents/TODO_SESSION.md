# TODO Session — « Les Myopes » (Ableton Live + Surge XT + MCP)

## Objectif
Construire la chanson « Les Myopes » dans Ableton Live selon `Les Myopes chanson.md` : folk-rock marin, **96 BPM, 4/4, ré mineur (Dm)**, 136 mesures, 6 pistes MIDI, en Vue Session scène par scène puis arrangement final.

## État global — FAIT (validé par David le 2026-09-11)
- **Composition : COMPLÈTE.** Toutes les sections (slots 0-8) ont leurs clips remplis sur toutes les pistes concernées.
- **Arrangement : COMPLET** — 43 `duplicate_to_arrangement` posés (PERC 8 clips / BASSE 9 / NAPPES 9 / LEAD 4 / CHŒURS 5 / TEXTURES 7), vérifié `get_arrangement_clips` : aligné sans recouvrement, fin à 544 beats.
- **Mix : FINALISÉ et validé à l'oreille.** Basse divisée par ~2 (elle donnait du RMS −14.6 solo ≈ 50% du mix), chœur baissé (0.80→0.55, c'était l'énergie soutenue la plus forte et la plus sombre), pads HPFée, master Compressor glue + Limiter True Peak.
- Track 6 = « **7-Audio** » (l'ancienne VOIX GUIDE est devenue une piste audio — pas de guide vocal, David chante de mémoire).
- Patch lead inst 2 = **Piano Remains 1** (choisi par David), plus FM Pluck.

## Pistes
| Index | Nom | Instrument | Surge inst | Patch |
|---|---|---|---|---|
| 0 | PERCUSSIONS | Gen Purpose Kit (Core Library) | — | — |
| 1 | BASSE | Surge XT | 0 | Sub 2 |
| 2 | NAPPES | Surge XT | 1 | Organ 1 |
| 3 | LEAD | Surge XT | 2 | Piano Remains 1 |
| 4 | CHŒURS | Surge XT | 3 | Deep Choir |
| 5 | TEXTURES | Surge XT | 4 | FM Riser |
| 6 | 7-Audio | (piste audio) | — | (ex-VOIX GUIDE) |

- Return 0 → REVERB/DELAY (existe déjà).
- Drum rack (Gen Purpose Kit) : note 36=Kick/stomp, 38=Clap, 42=HatClosed/Shaker, 44=Crash, + tom 43, reverse cymbal 47, woodblock 48, anvil 49. (Vérifier emails réels via get_drum_pad_info si besoin.)

## Conventions critiques
- Indices **0-based** (track/clip/scene).
- `create_clip(track, clip, length)` — length en **BEATS**. 96 BPM, 4/4 → 1 barre = 4 beats.
- `velocity` OBLIGATOIRE et VARIÉE sur chaque note (humanisation naturelle).
- `add_notes_to_clip`: utiliser `start_time` (PAS `start`).
- `duplicate_to_arrangement(track, clip, destination_time)` — destination_time en beats 0-based (PAS `destination_bar`, off-by-one).
- `set_arrangement_clip_notes` AJOUTE des notes (doublons) au lieu de remplacer → toujours passer par session puis `duplicate_to_arrangement`.
- « Device On » param, pas `is_enabled`. Normalized 0-1. `arrangement clip gain` = 0-1 normalisé (PAS dB).
- Ne PAS utiliser `create_event()` ni `control_coefficients`.

## Structure sections (positions arrangement en beats)
```
0   → Intro parlée (8 mes)
32  → Couplet 1 (16 mes)
96  → Refrain 1 (16 mes)
160 → Couplet 2 (16 mes)
224 → Refrain 2 (16 mes)
288 → Pont (16 mes)
352 → Couplet 3 (16 mes)
416 → Refrain final (20 mes)
496 → Outro (12 mes)
Total 544 beats.
```
- Slots session : slot 0=Intro, 1=Couplet 1, 2=Refrain 1, 3=Couplet 2, 4=Refrain 2, 5=Pont, 6=Couplet 3, 7=Refrain final (80 beats), 8=Outro (48 beats).

## RÉCAP CE QUI EST FAIT

### Intro (slot 0) — COMPLET (32 beats)
- Percussion : kick (36) temps 1&3, clap (38) temps 2&4 ; **shaker (42) humanisé 48 croches de beat 8 à 31.5** (vel 39-62, micro-décalages ±0.03-0.06 sur contretemps) + crashes.
- Basse : swell D2 vel 32→60 beats 0/4/8/12 + fade-in D2-D2-D2-A2 beat 16+.
- Nappes : Dm pads (62/65/69) swell vel 30→46 beats 4/8/12 + pad Dm beat 16.
- Lead : ABSENT (intro tranquille sans lead).

### Couplet 1 (slot 1) — QUASI FAIT (16 mes = 64 beats)
- Percussion : kick temps 1&3, clap 2&4, shaker discrètes croches (64 beats).
- Basse (inst 0 Sub 2) : 64 notes noires/croches marine D2-F2 pattern de la grille Dm-Bb-F-C | Dm-Bb-Gm-A, doublé par mesure (16 barres).
- Nappes (inst 1) : 24 notes pads; grille Dm-Bb-F-C | Dm-Bb-Gm-A selon voicings du .md (barre par barre, inversion type D3-F3-A3 pour Dm etc.).
- TEXTURES (slot 1) : riser FM Riser — 8 notes montées barre 16 (transition vers refrain). **VÉRIFIER si notes présentes.**
- Lead : vide.
- Choix : David chante A CAPPELLA/GUIDÉ PAR MÉMOIRE — pas de lead suraigu dans les couplets (LEAD réservé aux refrains).

### Refrain 1 (slot 2) — COMPLET (16 mes = 64 beats)
- Percussion (210 notes) : kick double frappe « hisse-hisse » (36) temps 1 & juste après, clap 2&4, tambourin 8ths (42), crashes (48) beats 0 et 32.
- Basse (80 notes) : noire-croche-croche-noire racine/quinte 16 barres (Dm Dm Bb C | Dm Bb Gm A | Dm Bb F C | Gm A Dm Dm).
- Nappes (48 notes) : pads tenus 1 barre/chord.
- Lead (62 notes) : « Hisse hisse » A3-A3 croches, phrase montante/descendante, fin sur D3 tenu (melodie refrain, octave haute 62-77).
- Chœurs (32 notes) : Deep Choir, octaves racine/quinte, 2 barres/chord (en soutien, discret).

## REGLAGES SURGE APPLIQUÉS (ne PAS refaire, sauf ajustement)
- **Inst 0 BASSE (Sub 2)** : osc2+osc3 démutés (Classic), osc2 vol 0.55, osc3 vol 0.35 octave +1, drift 0.06, unison osc1 param6=0.3/param7=0.5, FX slot1=Conditioner (8).
- **Inst 1 NAPPES (Organ 1)** : osc3 démuté vol 0.6, drift 0.05, cutoff 118→0.45, FX slot1=Chorus (9), slot2=Reverb 1 (2).
- **Inst 2 LEAD (Piano Remains 1)** : osc1 FM base, **osc2 démuté (Classic, même octave) vol 0.6**, **osc3 démuté (Classic, octave +1) vol 0.45** (volumes ajustés ensuite finement par David à l'oreille). Release allongé pour la tenue des refrains. Patch depuis `patches_factory/Plucks/Piano Remains 1`.
- **Inst 3 CHŒURS (Deep Choir)** : drift 1.0→0.1 (100%→10% — était instable), amp width 0.75, prefilter_gain 0.7, FX slot1=Chorus (9), slot2=Reverb 2 (11).
- **Inst 4 TEXTURES** : patch **FM Riser** chargé (Slowboat/FX). Réglages par défaut du patch (non tweakés).

### Carte FX Surge confirmée
1=Delay, 2=Reverb 1, 3=Phaser, 4=INVALID(null), 5=Distortion, 6=EQ, 7=Freq Shift, 8=Conditioner, 9=Chorus, 10=Vocoder, 11=Reverb 2, 12=Flanger.

## VARIATIONS À APPLIQUER — toutes APPLIQUÉES (spec .md lignes ~531-537)
Les variations suivantes sont posées dans les sessions clips puis dans l'arrangement :
- **Couplet 2** : PLUS RYTHMIQUE, SYNCOPES ; accordéon retiré puis revenu (varier les pads/nappes — alterner silence/présence).
- **Refrain 2** : + harmonium, banjo plus présent, chœurs plus larges (étoffer vs Refrain 1).
- **Pont** : percussion retirée (sauf stomp lent + woodblock), parlé-rythmé, crescendo, chœurs en nappe. Stomp lent = kick espacé (X. . . . . . .), woodblock accent bar 2.
- **Couplet 3** : plus large, lyrique, banjo « solo » ; accordéon/nappes continu.
- **Refrain final** : ff, RALENTI sur les 2 derniers vers (dans les 20 mes), chœurs massifs, fin sur **Dm tenu**. Kick double + clap + tambourin denses, crash entrée, sub drop fin de section. **NB : 80 beats (20 mes) — les 2 derniers vers en tempo ralenti, notes longues.**
- **Outro** : percussion limitée (stomp très lent = kick espacé, anvil C#2 isolé), nappes/basse termine en suspension (Dm tenu), chœurs en écho chuchoté « plus profond ». 12 mes.

## GUIDE VOCAL (ABANDONNÉ par David — track 6 devenue piste audio « 7-Audio »)
- Historique : Suisse Lead et guides posés sur track 6 (Couplet 1 : 56 notes, Refrain 1 : 44 notes). David chante de mémoire — la piste 6 est devenue une piste AUDIO (réservée à l'enregistrement vocal futur).

## VOIX — TOUTES PARTIES ENREGISTRÉES + CHAÎNE « PRO » (2026-09-12)
- **David a enregistré toutes les parties voix** sur track 6 (clips audio en arrangement) : Intro parlée (0), Couplet 1 (32), Refrain 1 (96), Couplet 2 (160), Refrain 2 (224), Pont (304), Couplet 3 (352), Refrain final (416), Outro (497).
- **Chaîne vocale track 6 (ordres devices 0→6)** :
  - 0 **Auto Filter** HPF : Filter Type=1 (High-pass), Freq 0.09, Env Amount 0
  - 1 **MAutoPitch** (VST3 Melda) : gamme **ré mineur naturelle** (C,D,E,F,G,A,Bb=1 ; C#,D#,F#,G#,B=0), Depth 0.4, Speed 0.7, Threshold 0.2, Keep formants 1.0. URI : `query:Plugins#VST3:MeldaProduction:MAutoPitch`
  - 2 **Compressor** : Threshold 0.62, Ratio 0.6, Attack 0.25, Release 0.5, Model RMS, Makeup 1
  - 3 **Channel EQ** (live Lite n'a PAS EQ Eight) : Mid Gain 0.62 (présence), Mid Freq 0.8, High Gain 0.58 (air), Low Gain 0.48, Output 0.5
  - 4 **Saturator** : Type 3 (Medium Curve), Drive 0.55, Dry/Wet 0.35, **Color ON→OFF** (anti-pattern Hot Tubes), Output 0.9
  - 5 **Limiter** (protection, ré-ajouté — David l'avait enlevée) : Mode 2 (True Peak), Ceiling 0.85, Lookahead 1 (3ms)
  - 6 **Delay slapback** : L/R 16th=8 (1/8), Feedback 0.2, Filter Freq 0.4, **Dry/Wet 0.08** (écho réduit — David trouvait trop d'echo)
- **Sends track 6** : A-Reverb 0.2 (10.2%→ réduit), B-Delay 0.0. Enveloppe par clip impossible (clips d'arrangement uniquement — pas de clip session → `set_arrangement_clip_envelope` échoue).
- **Piste voix vol 0.58** (réglé par David en 2026-09-12).
- **LEAD trop aigu → adouci** : vol 0.9→**0.82** + **Auto Filter** low-pass (device 1 track 3 : Filter Type=0, Freq 0.9 léger, Reso 0, Env 0, Slope 12dB) — enlève le tranchant haut sans tuer le corps.
- **Décompression master** : master fader 0.85→**0.72**, Compressor Threshold 0.7→**0.8** (moins de glue) → headroom restauré (peak sections −9.5 à −13.4, plus d'écrasement constant au Limiter 0.95).
- **Balance finale validée (captures `rec*_*.wav`, master 0.72)** : Intro −30.4 / C1 −27.4 / R1 −26.9 / C2 −28.3 / R2 −27.1 / Pont −29.2 / C3 −26.0 / RefFin −26.4 / Outro −27.2 dB RMS ; centroïdes ~730-770 Hz (coherents, mix medium-bright, OK phone + speakers).
- ⚠️ **Piège capture** : si les captures redeviennent polluées (duration_s ~40 au lieu de ~20, seek dérive +12 temps, zcr ~0.23) → **redémarrer le serveur MCP** (re-détecte CABLE Output). Ne PAS lancer de capture pendant que la lecture joue.

## RESTE À FAIRE — FAIT (arrangement + mix + voix validés)
1. ✅ Arrangement complet posé (43 `duplicate_to_arrangement`, fin à 544 beats).
2. ✅ Nommage clips — fait pour toutes les sections.
3. ✅ **Mix instrumental final validé par David** (« Stop ici, tout est bon ») :
   - Diagnostic piste par piste (solo @96) : PERC centroid 2245 / BASSE 122 (Sub2 sine) / NAPPES 458 / LEAD 1078 / CHŒURS 343 — le grave était écrasé par la basse (RMS solo −14.6) puis par le chœur (−23.7, le plus fort ET le plus sombre).
   - Actions : BASSE vol 0.85→**0.45** + **Saturator** (Medium Curve drive 0.55 wet 0.6, Color OFF) → RMS réel −28.7, crest +7.7, harmonics pour le phone ; NAPPES **Auto Filter HPF** (Filter Type=1 High-pass, Freq 0.18, Reso 0.2, Env Amt 0) + vol 0.6→0.7 ; CHŒURS 0.8→**0.55** ; LEAD 0.715→**0.9** ; PERC 0.85→0.8 ; NAPPES 0.715→0.7.
   - Master : **Compressor** (Threshold 0.7 / Ratio 0.4 / Attack 0.3 / Release 0.3 / Model RMS) + **Limiter** (Mode True Peak, Ceiling 0.95, Lookahead 3ms). Master fader 0.85.
   - Captures de validation (`data/analyses/*_v5_*.wav`) : Refrain final centroid 334→**567** Hz (rolloff 944), Couplet 1 280→**382**, Pont 143→**213**. DR 18.2, plus de pompage. Cible 700-900 non atteinte mais esthétiquement à sa place (pistes brillantes présentes).
4. ✅ **Voix pro + décompression + LEAD adouci** (2026-09-12, voir section VOIX) — validation finale à l'oreille par David.
5. [Si utile] Ensuite : rendu/session live — rien d'autre prévu.

## Diagnostics / Pièges connus
- CPU : Surge = gros. Mesurer en solo en jeu (au repos bruité ±5). Réduire polyphony si dropouts (actuellement 8 partout).
- `surge_query_all` (inst 2) renvoie énormément de bruit MIDI — output écrémé ; utiliser `surge_get_param` adresse précise plutôt.
- Inst 4 était injoignable — solution découverte : réessayer (l'instance répond maintenant). Si à nouveau muet, vérifier ports OSC 53286/7 (inst 3) et 53288/9 (inst 4) dans surge_osc_mcp.py.
- Validation utilisateur : David donne le feu vert par section. NE PAS faire l'arrangement avant validation.

## Fichiers
- Spec : `sources/Le Château Des Robots/01 - Les Myopes/Les Myopes chanson.md`
- Paroles : `sources/Le Château Des Robots/01 - Les Myopes/PAROLES.md`
- Patches Surge : `<SurgeXTData>/patches_factory/Basses/Sub 2`, `Keys/Organ 1`, `Plucks/FM Pluck` ; `patches_3rdparty/Giana Brotherz/Pads/Deep Choir`, `patches_3rdparty/Slowboat/FX/FM Riser`.
- OSC reference : `~/.agents/skills/surge-osc/OSC_REFERENCE.md`
- Skills à charger : `scene-workflow`, `ableton-mcp`, `full-mix-workflow`, `mix-translation`, `anti-patterns`.