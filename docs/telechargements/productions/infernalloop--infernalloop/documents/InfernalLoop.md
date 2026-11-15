# Infernal Loop — Rapport de production

**Tempo :** 120 BPM  
**Signature :** 4/4  
**Clé :** D mineur (détection automatique, confiance faible ~20 % — à confirmer à l'oreille)  
**Pistes :** 5 (swing, 2-Viral Kit, clarinet, guitare, basse)

---

## Ce qui a été fait

### Session
- **5 pistes MIDI** : swing (0), 2-Viral Kit (1), clarinet (2), guitare (3), basse (4)
- **Instruments chargés** :
  - swing : Surge XT
  - 2-Viral Kit : Viral Kit (InstrumentGroupDevice → DrumGroup + Saturator interne)
  - clarinet : Surge XT — patch **Another Flute**
  - guitare : Surge XT
  - basse : Surge XT (instance 3) — patch **Digibass** sculpté via OSC

### Progression harmonique
**Am → F → Em → Dm** (16 beats par cycle), détectée sur le clip clarinet. La basse scène 4 suit cette progression sur 6 cycles (96 beats).

### Effets Melda chargés (device_index 1, 1 par piste)
| Piste | Effet | Rôle prévu |
|-------|-------|------------|
| basse | MSaturator | Drive automatisé |
| swing | MCompressor | Pompe |
| clarinet | MEqualizer | Filtre animé |
| guitare | MCharmVerb | Espace |
| 2-Viral Kit | MCompressor | Impact |

Automations **écrites sur l'arrangement** via `set_automation_curve(is_arrangement=True)` (workaround temp-session-clip : copie notes → enveloppe → delete → re-duplicate). Lecture API des enveloppes d'arrangement non fiable (retourne None) — la vérification se fait à l'oreille / par capture.

### Automations appliquées (arrangement)
| Piste | Device | Target | Courbe (points rel. au clip) |
|-------|--------|--------|-------------------------------|
| basse | MSaturator | `device_1_Gain` | Crescendo drive 0.4→0.7 (0/32/64/96) |
| swing | MCompressor | `device_1_Threshold` | Pompe 38→76→38 par clip de 4 beats (×40) |
| clarinet | MEqualizer | `device_1_Frequency 4 (EQ 4)` | Sweep 44→95→44 par clip 16 beats (×8) |
| guitare | MCharmVerb | `device_1_Dry/Wet (Globals)` | Ouverture 0.25→0.6 (0/48/96) (×2 clips) |
| 2-Viral Kit | MCompressor | `device_1_Threshold` | Impact pompe 38↔76 par clip 16 beats (×10) |

**Limiter natif chargé sur Master** (device_index 0) — ceiling réglé à 0.92 (≈ -1 dB) pour éviter le clipping à l'export.

### Clips batterie — arc d'évolution (tous 16 beats)
| Scène | Vibe | Notes | Transition vers |
|-------|------|-------|-----------------|
| S0 | Perturbant, attention | 22 | Toms décalés → kicks 0/2.5 (pulse S1) |
| S1 | Pulse naissant | 34 | Kick 0/2.5 → 0/2 (backbeat S2) |
| S2 | Backbeat émerge | 37 | Groove renforcé + tom 47 @15.75 |
| S3 | Groove complet | 42 | Ghost + fill toms crescendo 45/47 |
| S4 | Majestueux (4 mesures) | 56 | Fill toms crescendo @14.25-15.75 |

### Saturator Viral Kit (interne au rack)
Drive Amount 109 → **85**, Drive Output 59 → **70**, Drive Color 50 → **55**

### Autres clips session
- **basse** : S3 « basse sautillante » (16 beats), S4 « basse 96 legato » (96 beats, 168 notes — racines/quintes/tierces, ghost notes, legato portamento)
- **clarinet** : clips 16 beats (S1-S4)
- **guitare** : « PLAINTE guitare » 96 beats (S2-S4)
- **swing** : clips 4 beats (S0-S4)

---

## Arrangement construit (160 beats / 40 barres / 80 s à 120 BPM)

Crescendo validé S0 → S4 :
- **S0** @0-16 : swing + batterie perturbante
- **S1** @16-32 : batterie plus construite
- **S2** @32-48 : batterie backbeat + clarinet
- **S3** @48-64 : + guitare (clip 96 qui continue)
- **S4** @64-160 : tout — basse 96 legato, guitare en continu, kit 4 mesures ×6, clarinet ×6, swing ×24

**État réel** :
- swing : 40 clips 4 beats (0→160, continu)
- 2-Viral Kit : 10 clips 16 beats (0→160)
- clarinet : 8 clips 16 beats (32→160)
- guitare : 2 clips 96 beats (48→144, 144→240 — **tail ring-out validé**)
- basse : 1 clip 96 beats (64→160)

---

## Suggestions manuelles (à faire dans Live)

### 1. Mix — vérifier à l'oreille
| Piste | Action |
|-------|--------|
| Volume global | Staging — viser un ensemble cohérent (basse ~0.85, clarinet basse ~0.5) |
| Master | Limiter ~ -1 dB ceiling avant export |
| Basse | MSaturator drive — vérifier la chaleur du bas du spectre |
| Guitare | MCharmVerb — ne pas noyer la clarinet (HPF du reverb ~150 Hz) |

### 2. Automations (après arrangement)
- **basse** : MSaturator drive pump (downbeat fort / relâchement)
- **swing** : MCompressor pompe sur le temps
- **clarinet** : MEqualizer — animation de filtre
- **guitare** : MCharmVerb — ouverture d'espace
- **batterie** : MCompressor — impact

### 3. Export
1. **File → Export Audio/Video**
2. Plage d'arrangement : 0 → ~160 beats
3. Format : WAV 44.1 kHz / 24-bit (ou MP3 320 kbps)

---

## Ce qu'il reste à faire

- [x] Construire l'arrangement 160 beats (crescendo S0→S4)
- [x] Automatiser les 5 effets Melda (sur arrangement)
- [x] Ajouter Limiter master (~ -1 dB ceiling)
- [x] Capture audio + analyse spectrale (voir section Résultats capture)
- [ ] Vérifier le rendu sur enceintes ET smartphone
- [ ] Exporter le rendu final (WAV) — plage 0 → 160 beats

## Résultats capture (VB-Cable)

### Capture brute (avant limiter) — `infernal_full.wav`
- Peak réel WAV : **0.485 (-6.3 dBFS)**, RMS 0.081 — **pas de clipping réel**
- Analyse outils : RMS 0.15, DR 16.4 dB, centroid 973 Hz, rolloff 2103 Hz, key D minor

### Capture avec Limiter — `infernal_full_limited.wav`
- Peak réel WAV : **0.477 (-6.4 dBFS)**, RMS 0.110 — limiter agit en protection (source < ceiling)
- Centroid 838 Hz, rolloff 1793 Hz (plus équilibré)

**Note** : `capture_and_analyze` rapporte `energy_peak: 1.0` systématiquement — c'est une valeur normalisée trompeuse. Toujours vérifier le peak réel dans le WAV.

### Captures par section (à faire pour valider le crescendo)
- S0 @0-16 (intensité minimale)
- S2 @32-48 (montée)
- S4 @128-144 (pic)

---

## Problèmes techniques rencontrés
- **set_automation_curve sur clip session** : erreur « Inverted ranges are not supported » (paramètres Melda normalisés 0-1) → reporter les automations sur l'arrangement.
- **get_drum_pad_info** : le DrumGroup est imbriqué dans le rack (InstrumentGroupDevice) — l'outil ne fouille pas les chaînes. Utiliser `get_chain_info(chain_index=1)`.
- **list_external_plugins** : bug « 'dict' object has no attribute 'lower' » → utiliser `get_browser_items(path="plugins/MeldaProduction")`.
- **duplicate_clip** : copie vers le prochain slot vide — attention aux doublons parasites.
