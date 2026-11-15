# Fourvière — Statut du projet

> Dernière mise à jour : 2025-07-31

## Rappel de la chanson

- **BPM** : 72
- **Tonalité** : D major
- **Structure** : Intro(8b) → Couplet A(16b) → Refrain(8b) → Interlude(4b) → Couplet B(16b) → Refrain(8b) → Outro(12b) = 68 barres, 288 beats ≈ 3min40
- **Fichier source** : `FOURVIÈRE.md`

---

## Layout des pistes (Ableton)

| Track Index | Nom | Type | Instrument | Instance OSC |
|------------|-----|------|------------|--------------|
| 0 | 2-Nappes | MIDI | Surge XT — Ooh (choir pad) | 0 (53280/53281) |
| 1 | 1-Voix | Audio | Enregistrement externe | — |
| 2 | 3-Basse | MIDI | Surge XT — Smoothie | 1 (53282/53283) |
| 3 | 4-Mélodies | MIDI | Surge XT — Cathedral Bell Pad | 2 (53284/53285) |
| 4 | 5-Drums | MIDI | 606 Core Kit (Ableton) | — |
| 5 | 6-Textures | MIDI | Surge XT — Drone Melancholy | 3 (53286/53287) |
| Return A | — | Audio | (vide) | — |
| Return B | — | Audio | (vide) | — |

**Volume Ableton** : toutes les pistes à 0.85 (0 dB) sauf Textures (0.46). Ne pas changer tant qu'on n'a pas le mix final.

**Sends configurés :**
| Piste | → A-Reverb | → B-Delay |
|---|---|---|
| 2-Nappes | 0.30 | 0 |
| 6-Textures | 0.30 | 0 |

---

## État des patches Surge XT

### Instance 0 — Nappes : "Ooh" (pad chœur)
- **Fichier** : `patches_factory/Pads/Ooh`
- **FX** : Reverb 1 — Mix 30%, Decay 4s, Predelay 0.15
- **Filtre** : LP 24dB, Cutoff 0.45 → vérifié via OSC (surge_get_patch + surge_set_param)
- **Enveloppe** : Attack 500ms, Decay auto, Sustain 80%, Release 700ms
- **Octave** : default

### Instance 1 — Basse : "Smoothie"
- **Fichier** : `patches_factory/Basses/Smoothie`
- **FX** : Reverb 1 — Mix 12% (subtil), Decay 3.5s, Predelay 0.15
- **Filtre** : LP 24dB, Cutoff 0.3, Resonance 0.15
- **Enveloppe** : Attack 400ms, Decay 50%, Sustain 85%, Release 60%
- **Octave** : -1 (défaut patch)

### Instance 2 — Mélodies : "Cathedral Bell Pad"
- **Fichier** : `patches_3rdparty/LinnStrument MPE/Pads/Cathedral Bell Pad`
- **FX** : Reverb 1 — Mix 35%, Decay 5.5s, Predelay 0.2 + Chorus 20%
- **Filtre** : LP 24dB, Cutoff 0.65
- **Enveloppe** : Attack 150ms, Decay 40%, Sustain 50%, Release 60%
- **Octave** : +1 (réglé depuis -3 défaut)

### Instance 3 — Textures : "Drone Melancholy"
- **Fichier** : `patches_3rdparty/Inigo Kennedy/FX/Drone Melancholy`
- **FX** : Reverb 1 — Mix 45%, Decay 7s, Predelay 0.25 + Delay 30%
- **Filtre** : défaut
- **Enveloppe** : défaut

---

## Clips session et arrangement

**35 clips session** créés (7 sections × 5 pistes), tous nommés et placés dans l'arrangement via `duplicate_to_arrangement`.

| Section | Beats | Position début | Position fin |
|---------|-------|---------------|-------------|
| Intro | 32 | 0 | 32 |
| Couplet A | 64 | 32 | 96 |
| Refrain | 32 | 96 | 128 |
| Interlude | 16 | 128 | 144 |
| Couplet B | 64 | 144 | 208 |
| Refrain 2 | 32 | 208 | 240 |
| Outro | 48 | 240 | 288 |

**Loop** : activé, start=0, length=288 beats.

---

## Notes insérées (MIDI)

- **Track 0 (Nappes)** : 67 notes — Intro, CoupletA, Refrain, CoupletB, Refrain2, Outro
- **Track 2 (Basse)** : 25 notes — racines des accords
- **Track 3 (Mélodies)** : 147 notes — arpèges, mélodies, accords plaqués
- **Track 4 (Drums)** : 89 notes — pattern minimaliste (kick, snare, triangle)
- **Track 5 (Textures)** : 2 notes — drone Intro + Outro

---

## Dernière analyse audio (2025-07-31)

### Refrain (beat 100) — mix final
- **Fichier** : `data/analyses/cap_100b_234126.wav`
- **Energy RMS** : 0.211
- **Spectral centroid** : 481 Hz (chaud, ambient sacré)
- **Spectral rolloff** : 868 Hz
- **Dynamic range** : 13.5 dB
- **Commentaire** : Mix équilibré multi-support. Centroid bas mais approprié (ambient sacré).

### Analyse piste par piste
| Piste | Patch | RMS | Centroid | DR | Verdict |
|---|---|---|---|---|---|
| Nappes | Surge Ooh | 0.234 | 495 Hz | 12.6 dB | ✅ Chaud, « pierres dorées » |
| Basse | Surge Smoothie | 0.195 | 188 Hz | 14.2 dB | ✅ Harmoniques (Waveshaper drive 0.7, Medium Curve) |
| Mélodies | Surge Bell Tower | 0.089 | 1194 Hz | 21.0 dB | ✅ Cloche sans bourdon (AEG sustain 0, FEG sustain 0) |
| Drums | 606 Core Kit | 0.010 | 4562 Hz | 39.9 dB | ✅ Minimaliste (voulu) |
| Textures | Surge Drone Melancholy | 0.157 | 695 Hz | 16.1 dB | ✅ Drone chaud |

---

## Ce qui reste à faire

### Haute priorité

1. **Piste Voix (Track 1)** — Enregistrer la voix en dehors d'Ableton, puis :
   - Importer le fichier audio → `create_audio_clip(track=1, slot=X, path="...")`
   - Appliquer EQ Eight : coupe < 80Hz, boost léger 3kHz
   - Appliquer Compressor : Ratio 3:1, Threshold -18dB, Makeup +3dB
   - Envoyer 25% → Return A : `set_send(track=1, send=0, value=0.25)`
   - Envoyer 15% → Return B : `set_send(track=1, send=1, value=0.15)`
   - **Paroles** : voir `FOURVIÈRE.md`

2. **Automations** (selon `FOURVIÈRE.md`) :
   - Track 0 (Nappes) : Cutoff filtre 500Hz → 1.5kHz pendant le Refrain
   - Track 1 (Voix) : Volume +2dB sur Refrain
   - Return A : Wet reverb 20% → 60% sur Outro
   - Master : Fade out sur les 4 dernières mesures

3. **Return FX** (à faire manuellement — API MCP ne peut pas écrire sur les retours) :
   - Return A : Reverb Hall (envoi 25-40% des pistes 1, 2, 6)
   - Return B : Delay 1/4 (envoi 15% de la piste 1)

### Faits (2025-07-31)

- ✅ **Master** : MEqualizer (Low shelf 80Hz +2.5dB, Low-mid 250Hz +1.5dB, High shelf 6kHz +3dB) + Limiter (Input 0.55, Ceil -0.3dB, Lookahead 6ms)
- ✅ **Basse** : Waveshaper Medium Curve drive 0.7, LP cutoff 0.7, Volume 0.35
- ✅ **Mélodies** : Patch Bell Tower, Pitch -24, MEqualizer (Low shelf +3dB 100Hz + High shelf cut -3dB 4kHz), AEG sustain 0, FEG sustain 0. 3 oscillateurs (FM3 + 2 Classic désaccordés ±7¢)
- ✅ **Nappes** : Cutoff 0.55, Attack 0.6, Release 0.8
- ✅ **Sends** : Nappes→A-Reverb 0.30, Textures→A-Reverb 0.30

### Moyenne priorité

4. **Commande `set_clip_loop`** dans le Remote Script (`AbletonMCP_Remote_Script.py`) — permettre de boucler les clips session.

5. **Ajuster le mix** — Les volumes Surge XT sont tous à 1.0, les volumes Ableton à 0.85 (0 dB). Affiner selon l'écoute :
   - Voix : -6dB (doc)
   - Nappes : -12dB
   - Basse : -15dB
   - Mélodies : -18dB
   - Batterie : -20dB
   - Textures : -22dB

6. **Champs de samples** (Track 6 dans le doc, mais pas de track dédiée) :
   - Intro : cloches de Fourvière (fade in)
   - Interlude : vent dans les vitraux
   - Outro : cloches lointaines (fade out)
   - **Note** : ce serait une track Audio supplémentaire. Vérifier qu'on reste sous la limite de pistes Ableton Lite.

### Basse priorité

7. **Refinement sonore** — Écouter et ajuster :
   - Plus de corps sur la basse si besoin
   - Équilibrer mélodies / nappes
   - Vérifier que le delay sur les textures ne cause pas de conflit rythmique

8. **Dynamic automation** sur les nappes : swell pendant les couplets, plus intense au Refrain.

---

## Notes techniques importantes

- **Mapping OSC** : instance N → port 53280 + N×2 (IN) / 53281 + N×2 (OUT)
- **Clips** : `create_clip` utilise des **beats** (pas des barres). 4/4 : 1 barre = 4 beats.
- **Volume Ableton API** : 0.85 = 0 dB unity gain
- **Limite Ableton Lite** : 8 pistes max (6 MIDI/Audio + 2 Return)
- **Pas de Surge XT sur** : Track 1 (Voix/Audio) et Track 4 (Drums/606)
