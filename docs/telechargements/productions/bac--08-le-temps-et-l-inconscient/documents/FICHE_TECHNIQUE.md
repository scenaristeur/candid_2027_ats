# 08 — Le Temps et l'Inconscient

**Tempo**: 58 → 55 BPM (map par section)
**Tonalité**: La mineur (Am)
**Durée**: ≈ 1 min 50 (32 barres — arrangement complet)
**Atmosphère**: Rêve éveillé, flottement, courant de conscience (Proust), très lent
**Style**: Dream Pop / Ambient
**Voix**: Baryton parlé-chanté (E3 → B3, pitch 64-71), couplet 1 chuchoté

## Hommage / Inspirations
- Dream Pop / Ambient : nappes très lentes, guitares reverse, voix flottante.
- Courant de conscience (Proust), le temps comme durée (Bergson), l'inconscient (Freud).
- Pendules et eaux : le temps qui s'égrène en bruit de fond.

## Structure (en barres)

Intro (4) | Couplet 1 (4) | Refrain (4) | Couplet 2 (4) | Refrain 2 (4) | Pont (4) | Outro (8) = **32 barres**

Bloc 3/4 (barres 1-12) → Bloc 4/4 (barres 13-24) → Outro 3/4 (barres 25-32).

| # | Section | Barres | Signature | Éléments clés |
| :---: | :--- | :--- | :--- | :--- |
| 1 | Intro | 1-4 | 3/4 | Vagues, cristaux, pad (Surge XT), arpège de piano préparé |
| 2 | Couplet 1 | 5-8 | 3/4 | Voix chuchotée, kick feutré, nappe |
| 3 | Refrain | 9-12 | 3/4 | Envolée, voix mixte |
| 4 | Couplet 2 | 13-16 | 4/4 | Plus clair, basse en longues tenues |
| 5 | Refrain 2 | 17-20 | 4/4 | Retour de l'envolée |
| 6 | Pont | 21-24 | 4/4 | Nappe qui s'élève, guitare e-bow |
| 7 | Outro | 25-32 | 3/4 | Pendules, eaux, fondu, retour au calme |

> ⚠️ Le doc source fixe les repères tempo/signature aux mesures 0, 12 et 24 (3/4 → 4/4 → 3/4). Les barres ci-dessus en sont déduites (12 barres par bloc) ; à ajuster à l'oreille.

## BPM Map

| Repère | Barres | BPM | Événement |
| :--- | :--- | :--- | :--- |
| Bloc 1 (3/4) | 1-12 | **58** | Signature 3/4 — intro, couplet 1, refrain |
| Bloc 2 (4/4) | 13-24 | **58** | Signature 4/4 — couplet 2, refrain 2, pont |
| Outro (3/4) | 25-32 | **55** | Ralenti, pendules, fondu |

## Grille d'accords

| Section | Grille | Couleur / Sonorité |
| :--- | :--- | :--- |
| **Intro** | `Am9 - Dm11` (arpégé) | Ouverture onirique, couleurs pastel. |
| **Couplet** | `Am9 - Dm11 - Gmaj13 - Cmaj9#11` | Nappe modale en La mineur, pastel. |
| **Refrain** | `Am9 - Dm11 - Gmaj13 - Cmaj9#11` | Envolée, nappe qui s'ouvre. |
| **Pont** | `F#m7b5 - B7alt - Em9 - A7sus4` | Tension, résolution, nappe qui s'élève. |
| **Outro** | `Am9 - Dm11` | Retour au calme, en fondu. |

## Instruments (Ableton) — Mix

Template réel `bac.als` (indices **0-based**), pistes 0-6 MIDI, piste 7 Audio (Voix).

| Piste | Index | Instrument | Pan | Vol | Chaîne FX |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Drums** | 0 | Gen Purpose Kit (rack) — kick feutré, snare étouffée | 0 | 0.80 | MCompressor (lent) |
| **Basse** | 1 | Surge XT — Soft Sine (Legato 100 ms) | 0 | 0.85 | MDelay + MEqualizer (coupe des aigus) |
| **Pads/Claviers** | 2 | Surge XT — Wavetable « Reverse » (Index 70 %, Env A:5 s R:6 s) | 0 | 0.75 | Reverb (Ableton) + MFlanger ; `MReverb` (Decay 8 s) à charger |
| **Lead/Mélodie** | 3 | Surge XT — Sustain Guitar (LFO sur amplitude) | 0 | 0.70 | Drum Noise Glitcher (rack) + Massive Sidechain Distort (rack) ; `MFlanger` à charger |
| **Arp/Contrepoint** | 4 | Surge XT — Tines + cloche | +0.15 | 0.65 | MPhaser |
| **Fx** | 5 | Surge XT (MIDI — PAS audio) | −0.20 | 0.60 | Reverb (Ableton) + Auto Filter ; `MReverb` (Non-linéaire) à charger |
| **Aux/synthé2** | 6 | Surge XT — Wavetable « Glitter » (Unison 16) | 0 | 0.70 | Chorus-Ensemble + Chorus + MCompressor ; `MDelay` (1/2T) à charger |
| **Voix** | 7 | Audio (couplet 1 chuchoté + chant) | 0 | 0.85 (mix manuel) | MCompressor (vocal) + De-esser ; `MReverb` (Send 70 %) à charger |

> Convention : effet Meldaproduction cité par le doc mais absent du template → mentionné « à charger ».

### Réglages Surge XT (du doc)
- **Basse** — Osc1 « Soft Sine », Legato 100 ms. Filtre LPF, coupe des aigus à l'égalisation.
- **Dream Pad (P3)** — Osc1 Wavetable « Reverse », Index 70 %. Env A:5 s, R:6 s.
- **Guitare E-Bow (P4)** — « Sustain Guitar », LFO sur l'amplitude (mouvement de nappe).
- **Piano préparé (P5)** — « Tines » + cloche (partiel métallique).
- **Synthé Scintillant (P7)** — Wavetable « Glitter », Unison 16 (shimmer).

## Clips JSON (motifs principaux — temps en beats)

> Légende hauteurs (convention **C3 = 60**) : 50 D2 · 53 F2 · 57 A2 · 60 C3 · 64 E3 · 67 G3.

### A. Arpège Piano (Piste Arp/Contrepoint, index 4) — `Am9 - Dm11`
Motif de 2 mesures en 3/4 (6 beats, croches) : mesure 1 = Am9, mesure 2 = Dm11. **Correction appliquée : pitch 50 = D2 (le commentaire « D3 » du doc était erroné — D3 = 62).** Répéter ×2 (offset +6 beats) pour une section de 4 mesures (12 beats).

```json
{
  "clip_name": "C8_Piano_Arp",
  "bpm": 58,
  "notes": [
    { "time": 0.0, "pitch": 57, "duration": 0.5, "velocity": 70 },
    { "time": 0.5, "pitch": 60, "duration": 0.5, "velocity": 65 },
    { "time": 1.0, "pitch": 64, "duration": 0.5, "velocity": 70 },
    { "time": 1.5, "pitch": 67, "duration": 0.5, "velocity": 60 },
    { "time": 2.0, "pitch": 64, "duration": 0.5, "velocity": 65 },
    { "time": 2.5, "pitch": 60, "duration": 0.5, "velocity": 70 },
    { "time": 3.0, "pitch": 50, "duration": 0.5, "velocity": 70 },
    { "time": 3.5, "pitch": 53, "duration": 0.5, "velocity": 65 },
    { "time": 4.0, "pitch": 57, "duration": 0.5, "velocity": 70 },
    { "time": 4.5, "pitch": 60, "duration": 0.5, "velocity": 60 },
    { "time": 5.0, "pitch": 57, "duration": 0.5, "velocity": 65 },
    { "time": 5.5, "pitch": 53, "duration": 0.5, "velocity": 70 }
  ]
}
```
> Les arpèges égrènent Am7 (A-C-E-G, mesure 1) puis Dm7 (D-F-A-C, mesure 2) : extensions 9/11 non jouées — voir Notes de production.

## Automations (temps en beats)

| Moment | Paramètre | Points (breakpoints) | Effet |
| :--- | :--- | :--- | :--- |
| **Toute la chanson** | Pads — `MReverb` Decay (P3) | `0 → 4 s`, `36 → 8 s`, `84 → 10 s` (linéaire) | La nappe s'ouvre de l'intro à l'outro (repères doc 0/12/24 mes convertis en beats : 0, 36, 84) |
| **Début (8 mesures 3/4)** | Volume P7 (Scintillant) | `0 → 0` (silence) → `24 → −6 dB` (linéaire) | Fondu entrant du synthé « Glitter » |
| **Tempo** | Automations par section | Voir BPM Map | Changements de tempo/signature (58 → 58 → 55) |

## Réglages Mix

| Piste | Vol | Pan | Notes |
| :--- | :--- | :--- | :--- |
| Drums | 0.80 | — | MCompressor lent colle ; kick feutré |
| Basse | 0.85 | — | Soft Sine en tenues ; MEqualizer coupe les aigus |
| Pads/Claviers | 0.75 | — | MReverb Decay 4 → 10 s selon automations |
| Lead/Mélodie | 0.70 | — | Guitare E-Bow, LFO d'amplitude |
| Arp/Contrepoint | 0.65 | +0.15 | Piano préparé (Tines + cloche), MPhaser |
| Fx | 0.60 | −0.20 | MIDI (Surge XT) ; pendules/vagues, MReverb non-linéaire |
| Aux/synthé2 | 0.70 | — | Scintillant, fondu entrant sur 8 mesures |
| Voix | 0.85 (mix manuel) | — | MCompressor + De-esser ; MReverb Send 70 % |

## Notes de production

- **Correction de note (label)** : le pitch 50 du JSON (début du Dm11) est **D2**, pas « D3 » comme l'indiquait le commentaire du doc (D3 = 62). Valeur de pitch conservée (50), label corrigé.
- **Vérification des accords** : Am9 = A-C-E-G-B · Dm11 = D-F-A-C-G · Gmaj13 = G-B-D-F#-A · Cmaj9#11 = C-E-G-B-D-F# · F#m7b5 = F#-A-C-E · B7alt = B-D#-F#-A-C · Em9 = E-G-B-D-F# · A7sus4 = A-D-E-G. **Aucune note fausse** relevée dans le JSON fourni.
- **Arpèges Am7 / Dm7** : le motif du piano égrène A-C-E-G puis D-F-A-C — les extensions 9/11 ne sont pas jouées. Coloration plus ouverte possible (ajouter B2=59 et G3=67) à valider à l'oreille.
- **Fx en MIDI** (Surge XT) : les samples de pendules/eaux passeront par la piste **Fx** (index 5) en MIDI — la piste reste MIDI, PAS audio.
- **Meldaproduction absents du template** → à charger : MReverb, MFlanger, MPhaser, MDelay, MEqualizer.
- **Basse en longues tenues** : « Soft Sine » Legato 100 ms sur les racines de la grille (Am9→Dm11→Gmaj13→Cmaj9#11), entrée au couplet 2.
- **Signature/tempo** : bloc 3/4 58 BPM (barres 1-12), bloc 4/4 58 BPM (13-24), outro 3/4 55 BPM (25-32).
- ⏳ **À valider** : adaptation de la tonalité si la mélodie (voix baryton E3-B3) sort de la tessiture.

## Intégration MCP

Indices **0-based** (0 = Drums, 1 = Basse, 2 = Pads/Claviers, 3 = Lead/Mélodie, 4 = Arp/Contrepoint, 5 = Fx, 6 = Aux/synthé2, 7 = Voix). Temps des notes et longueurs de clips en **beats** (1 mesure 3/4 = 3 beats, 1 mesure 4/4 = 4 beats).

1. **Tempo** : `set_tempo(58)` (blocs 3/4 et 4/4) ; `set_tempo(55)` pour l'outro (barre 25).
2. **Intro (barres 1-4)** : `create_clip(2, 0, 12)` — nappe pad (Surge XT « Reverse ») ; `create_clip(4, 0, 12)` — arpège piano (JSON A, répété ×2, offset +6 beats).
3. **Couplet 1 (barres 5-8)** : `create_clip(0, 0, 12)` — kick feutré ; `create_clip(4, 1, 12)` + `add_notes_to_clip(4, 1, notes)` — arpège (JSON A, offset +6 beats).
4. **Refrain (barres 9-12)** : `create_clip(2, 1, 12)` — accords de nappe (grille Am9-Dm11-Gmaj13-Cmaj9#11) ; voix enregistrée sur piste 7.
5. **Couplet 2 (barres 13-16, 4/4)** : `create_clip(1, 0, 16)` — basse Soft Sine en tenues + `add_notes_to_clip(1, 0, notes)` (racines) ; `create_clip(4, 2, 16)`.
6. **Refrain 2 (barres 17-20)** : `create_clip(2, 2, 16)` — retour de la nappe.
7. **Pont (barres 21-24)** : `create_clip(6, 0, 16)` — scintillant (fondu entrant) ; `create_clip(3, 0, 16)` — guitare e-bow.
8. **Outro (barres 25-32)** : `set_tempo(55)` ; `create_clip(5, 0, 24)` — pendules/eaux (FX MIDI) ; `create_clip(2, 3, 24)` — nappe finale en fondu.

## Paroles
Voir `PAROLES.md` dans ce dossier.
