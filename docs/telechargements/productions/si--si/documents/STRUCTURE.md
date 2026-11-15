# Si — Structure & Arrangement

**Adaptation de "IF" (Pink Floyd, 1970)**
**Tonalité :** C#m | **Tempo :** 85 BPM | **Signature :** 4/4
**Durée :** ~4min00 (88 mesures)

---

## Architecture symétrique (palindrome)

Chaque instrument entre à un palier et sort au même palier en miroir.

```
Temps  →  ▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸▸
Guitare ────────────────────────────────────────────────────────────
Basse         ────────────────────────────────────────────
Batterie           ────────────────────────────
Piano/Nappes             ────────────
Lead/Tutti                       ────
Piano/Nappes             ────────────
Batterie           ────────────
Basse         ────────────
Guitare ────────────────────────────────────────────────────────────
```

---

## Grille d'accords détaillée

### Couplets (1, 2, 3, 4) — identiques
```
| C#m7    | Bmaj7   | A6      | G#7     |
| C#m7    | Bmaj7   | F#m7    | G#7     |
```

### Pont instrumental
```
| E/G#    | F#m7    | D#m7b5  | G#7     |
| Amaj7   | G#7     | C#m7    | G#7     |
```

### Peak — Partie A (lead mélodique)
```
| E/G#    | F#m7    | D#m7b5  | G#7     |
| Amaj7   | G#7     | C#m7    | Bmaj7   |
```

### Peak — Partie B (climax texturé)
```
| C#m7    | Bmaj7   | A6      | G#7     |
| C#m7    | Bmaj7   | F#m7    | G#7     |
```

### Transition
```
| C#m7    | —       | —       | —       |
| —       | —       | —       | —       |
```
(répéter 2 fois, C#m7 tenu avec variations rythmiques)

### Intro / Outro
```
| C#m7    | Bmaj7   | C#m7    | —       |
```
(répété 2 fois pour 8 mesures, fingerpicking seul)

---

## Plan d'arrangement mesure par mesure

| # | Mesures | Section | Instruments | Description |
|---|---|---|---|---|
| 1 | 1–8 | **Intro** | Guitare seule | Fingerpicking arpégé, C#m7 → Bmaj7 → C#m7. Rythme libre, atmosphérique. |
| 2 | 9–16 | **Couplet 1** | + Basse | Entrée basse (notes tenues, root/fifth). Voix parlée-chantée, tessiture E3–G#3. |
| 3 | 17–24 | **Couplet 2** | + Batterie | Batterie brush (balais), caisse claire légère, charlston. Pas de grosse caisse. |
| 4 | 25–32 | **Pont inst.** | + Piano/Nappes | Piano Fender Rhodes ou Wurlitzer (nappes tenues). Section instrumentale — la mélodie vocale est jouée au piano. |
| 5 | 33–48 | **Peak (16m)** | Tous + Lead | **A** (33-40): Lead mélodique (guitare électrique claire ou piano). **B** (41-48): Tutti, nappes, batterie pleine (grosse caisse + cymbales). Point culminant. |
| 6 | 49–56 | **Couplet 3** | − Piano/Nappes | La voix revient seule avec basse + batterie (retour au même niveau qu'avant le pont). Paroles sur IA / paraître. |
| 7 | 57–64 | **Couplet 4** | − Batterie | Plus que voix + basse. Paroles sur les guerres, les dirigeants. Batterie arrêtée. |
| 8 | 65–72 | **FS - Fade** | − Basse | Guitare seule, arpège ralenti C#m7 qui fond au silence. |
| 9 | 73–76 | **Silence** | — | Silence complet (16 temps). Tension. |
| 10 | 77–80 | **FS - Hit** | + Batterie + Lead | **Fausse sortie :** Batterie (crash + kick + snare), Lead (descente G#→C#, tenue), Guitare (reprise de la descente du Lead + montée du peak à l'octave). Volume Lead réduit en enveloppe. Crash supplémentaire batterie. Dernier accord C#m qui résonne seul jusqu'à 84. |

---

## Instrumentation détaillée

### Piste 1 — Guitare acoustique (fingerpicking)
- **Instrument :** Guitare acoustique (Ableton Acoustic Guitar ou session strings)
- **Pattern :** Arpèges en picking pattern 8 notes par mesure (croches)
  - Doigté : pouce (root), index (tierce), majeur (quinte), annulaire (septième)
  - Varier les renversements entre les passages
- **FS :** Reprend la descente du Lead (G#→F#→E→D#→C#) + montée du peak à l'octave
- **FX :** Light reverb (Room), Compressor gentle. Reverb + Delay ajoutés progressivement à partir de la mesure 65 (fin Couplet 4), automation Dry/Wet croissante sur le fade, qui continue de résonner après le silence dans l'accord final.
- **Rôle :** Colonne vertébrale, présent de la 1ʳᵉ à la dernière mesure

### Piste 2 — Basse électrique
- **Instrument :** Ableton Electric Bass ou session bass
- **Style :** Notes tenues (semi-staccato), root note sur temps 1, fifth sur temps 3
- **FX :** Amp, Compressor, très peu de saturation
- **Entrée :** Mesure 9 | **Sortie :** Mesure 72

### Piste 3 — Batterie
- **Kit :** Dry Session Kit.adg ou Recording Hybrid Kit - Damped Snare
- **Style :** Brushed snare, kick discret, hi-hat léger (pas de crash sauf peak)
- **Pattern :** Groove simple (2&4 sur caisse claire), kick sur 1 (&3 optionnel)
- **Peak :** Cymbales (crash ride), kick plus présent
- **FX send :** Drum Buss → Compressor → Reverb
- **Entrée :** Mesure 17 | **Sortie :** Mesure 64

### Piste 4 — Piano / Nappes
- **Instrument :** Ableton Collision (piano électrique type Rhodes) ou Wavetable (nappes douces)
- **Style :**
  - Nappes tenues longues (pad) pendant le pont et peak
  - Accords voicings ouverts (omit root, joué par la basse)
- **FX :** Reverb Hall, Chorus, Auto Filter (lent, ouvert → fermé)
- **Entrée :** Mesure 25 | **Sortie :** Mesure 48

### Piste 5 — Lead mélodique (peak + fausse sortie)
- **Instrument :** Sweet Lead
- **Style :** Single note melody, reprend la ligne vocale du couplet 1 (peak). Descente G#→F#→E→D#→C# tenue (fausse sortie).
- **FX :** Delay, Reverb, Auto Filter. Enveloppe volume baissée sur la section FS.
- **Entrée :** Mesure 33 | **Sortie :** Mesure 48, puis Mesure 77–80 (FS Hit)

### Piste 6 — Voix
- **Style :** Parlé-chanté, tessiture E3–B3, nonchalant et cynique
- **FX :** EQ Eight (HP ~80Hz, présence ~3-5kHz), Compressor, Reverb send, Delay slapback
- **Couplet 4 :** plus sec, plus proche (moins de reverb)

---

## Notes de production

### Dynamique / Automations
- **Intro → Peak :** Volume +0dB → +3dB progressif sur chaque section
- **Peak → Outro :** Symétrique, −3dB → 0dB
- **Reverb send :** Croissant de l'intro vers le peak, décroissant en sortie
- **Auto Filter :** sur les nappes, cutoff ouvert progressivement du pont au peak, refermé ensuite

### Palette harmonique (intervalles et couleurs)
- **C#m7** — C# E G# B (tonique, mineur, doux)
- **Bmaj7** — B D# F# A# (maj7 lumineux, tension)
- **A6** — A C# E F# (6ème, couleur jazzy)
- **G#7** — G# B# D# F# (dominante, tension → résolution)
- **F#m7** — F# A C# E (iv7, sous-dominante mineure)
- **E/G#** — E G# B (III, relatif lumineux)
- **D#m7b5** — D# F# A C# (ii∅7, demi-diminué, tension max)
- **Amaj7** — A C# E G# (bVI maj7, emprunt modal)

### Rendu final
- Master : Light Compressor → Limiter
- Pas de maximisation agressive — garder de la dynamique (indie rock organique)
- Silence laissé après la dernière note (réverbe naturelle qui s'éteint)
