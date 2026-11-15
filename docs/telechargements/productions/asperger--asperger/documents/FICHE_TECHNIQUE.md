# FICHE TECHNIQUE — *Ici*

**Ableton Live 12 (Lite) + Surge XT (OSC) · 72 BPM · 4/4 · F# mineur · ambiance cinématique / néo-soul / ambient**
**Durée cible ≈ 4 min 52 s.** 1 mesure = 3,33 s. Tempo session actuel : **75 BPM** (à confirmer avec David).

> Morceau : « Ici ». Un vaisseau qui dérive dans la Noosphère. Spacieux, chaud, presque silencieux par moments. Rien ne doit briller.

---

## 1. SETUP SESSION

| Élément | Valeur |
|---|---|
| BPM | **72** (session actuelle : 75 — à reposer) |
| Signature | 4/4 |
| Groove | Aucun swing. Placement droit, humanisé manuellement (±15 ms) |
| Tonalité | F# mineur (F# G# A B C# D E) |
| Grille | 1/16, snap désactivé pour la plupart des instruments |

**Routing (concept kit; en attente de setup Live Lite)**
```
Drums ─────┐
Basse ─────┼─→ BUS RYTHMIQUE ──→ Glue Compressor ──→ Master
Percus ────┘
Rhodes ────┐
Pad ───────┼─→ BUS HARMONIQUE ──→ Glue Compressor lent ──→ Master
Pluck ─────┘
Textures ──┐
Lead ──────┼─→ BUS LEAD ──→ Echo + Hybrid Reverb ──→ Master
Vox ───────┘
```
Sidechain : Kick → Basse (threshold -18, ratio 3, attack 8 ms) et Kick → Pad (ratio 2).

---

## 2. STRUCTURE (Arrangement)

| Section | Mesures | Durée approx. | Contenu |
|---|---|---|---|
| Intro | 1–8 | 26 s | Pad + Basse (vamp F#m11–Bm11) + Textures, filtre qui s'ouvre |
| Couplet 1 | 9–24 | 53 s | + Rhodes, Drums minimal (kick t.1) |
| Refrain 1 | 25–32 | 26 s | Grille refrain, + rim t.3 |
| Couplet 2 | 33–48 | 53 s | idem C1 + rim + Pluck (gouttes) |
| Refrain 2 | 49–56 | 26 s | idem R1 + Lead + shaker 8èmes |
| Pont | 57–64 | 26 s | Pad seul dominant, Rhodes coupé, batterie réduite |
| Refrain final x2 | 65–80 | 53 s | Full, breakdown au 2e |
| Outro | 81–88 | 26 s | Vamp F#m11–Bm11, Low Pass 24 dB qui descend |

---

## 3. GRILLES D'ACCORDS (voicings ouverts)

### COUPLET — boucle 4 mesures (x4)
| Mes. | Accord | LH | RH |
|---|---|---|---|
| 1 | **F#m11** | F#1 | G#3 – C#4 – E4 – A4 |
| 2 | **Bm11** | B1 | F#3 – A3 – D4 – E4 |
| 3 | **Dmaj9** | D2 | C#4 – E4 – F#4 – A4 |
| 4 | **C#7#9** | C#2 | B3 – E4 – F4 – G#4 |

### REFRAIN — boucle 4 mesures (x2)
| Mes. | Accord | LH | RH |
|---|---|---|---|
| 1 | **Dmaj9** | D2 | C#4 – E4 – F#4 – A4 |
| 2 | **E13sus4** | E2 | D4 – F#4 – A4 – B4 |
| 3 | **F#m11** | F#1 | G#3 – C#4 – E4 – A4 |
| 4 | **A/B** | B1 | G#3 – A3 – C#4 – E4 |

### PONT — 4 mesures (encore plus ouvert)
| Mes. | Accord | LH | RH |
|---|---|---|---|
| 1 | **Bm9** | B1 | A3 – C#4 – D4 – F#4 |
| 2 | **G#m7b5** | G#2 | F#3 – A3 – B3 – D4 |
| 3 | **C#7alt** | C#2 | B3 – E4 – F4 – A4 |
| 4 | **F#m11** | F#1 | G#3 – C#4 – E4 – A4 |

### Couleurs bonus
| Substitut | Notes | Effet |
|---|---|---|
| F#m13 | F# A C# E G# D# | ouvre, presque majeur |
| Bm13 | B D F# A C# G# | dense, gospel |
| Dmaj9#11 | D F# A C# E G# | lydien, planant |
| E7#11 | E G# B D A# | tension fine |

---

## 4. PROGRAMMATION PAR INSTRUMENT

### 🥁 DRUMS — *minimal, respirant*
Pas de kick four-on-the-floor. Pas de backbeat marqué.

- **Kick** (pad 36) : temps 1, parfois ghost sur le « a » de 4. 808 sub rond, pitch -3 st, decay long.
- **Rim** (pad 37) : sec sur temps 3 — **dès le couplet 2 et refrain**.
- **Hats** : quasiment absents. **Shaker** (pad 48) discret en 8èmes, à partir du refrain 2.
- **Percussion libre** : crotale/triangle sur temps 1 des mesures impaires, réverb longue.
- **FX** : reverse cymbal avant chaque refrain, sub drop avant le pont.
- Realisé : kick + rim + ghost (session view, scènes).

Chaîne Ableton drums : `Drum Rack → EQ8 (HP 30 Hz) → Glue Compressor (attack 30, ratio 2) → Utility (mono < 120 Hz) → Reverb court (12%)`

### 🔊 BASSE — *ronde, lente, contrebasse*
Patch Surge **Sub_Grave** (loaded : Sub 1) : osc1 sine, osc2 triangle, osc3 saw, filtre LP24 ~280 Hz.

Ligne couplet : `F#1 ─── / B1 ─── / D2 ─── / C#2─B1─A1`
Ligne refrain : `D2 ─── / E2 ─── / F#1 ─── / B1─C#2─D2`

Chaîne Ableton basse : `Saturator → EQ8 (HP 30 Hz, LP 3 kHz) → Glue Compressor (sidechain kick) → Utility (mono < 100 Hz)`

### 🎹 RHODES — *le cœur harmonique*
Patch Surge **Rhodes_Voilé** (loaded : Treated Rhodes) : FM2, LP24 2,8 kHz, vibrato LFO lent.

Chaîne Ableton : `EQ8 (HP 140 Hz, coupe 400 Hz -2 dB) → Chorus léger → Echo 1/8p (fb 15%, mix 10%) → Hybrid Reverb (22%)`

**Placement :** couplets et refrains. **Pas au pont.**

### 🌆 PAD — *la Noosphère*
Patch Surge **Noosphère** (loaded : MKS-70 Warm Pad) + **Auto Filter LP 24 dB** (ouverture par enveloppe).

Chaîne Ableton : `Auto Filter → Hybrid Reverb (decay 8 s, 55%) → Utility (largeur 140%) → EQ8 (HP 100 Hz, LP 6 kHz)`

**Placement :** partout — très bas au C1, plus présent au refrain, **dominant au pont**.

### ✨ PLUCK — *les gouttes de verre*
Patch Surge **Pluck_Verre** (loaded : Icy Pluck) : BP12 ~2,8 kHz, res 40%, delay 3/16.

**Placement : 1 à 3 notes par mesure, jamais régulières. Uniquement à partir du couplet 2.**

MIDI exemple (couplet 2, mes. 1) : t.1.75 A4 · t.2.5 C#5 · t.3.5 F#4

Chaîne Ableton : `Delay ping-pong → Reverb 30% → Utility (pan L 30%)`

### 🎤 LEAD — *la voix intérieure du capitaine*
Patch Surge **Lead_Pensée** : saw unison 3, LP 1,8 kHz, monovoix glide 90 ms, vibrato.

Ligne (refrain, F#m) : `C#5─A4─F#4 / G#4─B4─C#5 / A4─G#4─F#4─E4 / F#4 (tenue)`

**Placement : uniquement refrain 2 et refrain final. Jamais au couplet.**

Chaîne Ableton : `Echo 1/4 → Reverb 35% → Utility`

### 🌫️ TEXTURES — *la coque du vaisseau*
Patch Surge **Coque** (loaded : Distant Thunder Rumble — élevé par David au volume global pour être audible).

**Placement : intro, outro, et très bas sous tout. Jamais identifiable. Juste présent.**

Chaîne Ableton : `Auto Pan 0,06 Hz → Hybrid Reverb 75% → Utility`

---

## 5. TRAITEMENT GLOBAL (à mettre en place à l'arrangement)

| Piste | Chaîne Ableton |
|---|---|
| Drums | EQ8 → Glue Comp → Utility (mono <120 Hz) → Reverb 12% |
| Basse | Saturator → EQ8 → Glue Comp (sidechain kick) → Utility |
| Rhodes | EQ8 → Chorus → Echo (1/8p) → Hybrid Reverb 22% |
| Pad | Auto Filter (LFO) → Hybrid Reverb 55% → Utility (140%) |
| Pluck | Delay ping-pong → Reverb 30% → Utility (pan L 30%) |
| Lead | Echo 1/4 → Reverb 35% → Utility |
| Textures | Auto Pan → Hybrid Reverb 75% → Utility |
| Master | Glue Compressor (2:1, lent) → EQ8 → Limiter (-1 dB) |

---

## 6. ÉTAT RÉEL DE LA SESSION (Live, session view)

| Piste | Slots faits | Patch Surge | Notes |
|---|---|---|---|
| 1-Drums | 0 Intro, 1 C1, 2 R1, 3 C2 | Drum Rack 808 Core Kit | kick t.1, rim dès C2 |
| 2-Basse | 0 Intro, 1 C1, 2 R1, 3 C2 | inst 0 · Sub 1 | octave scène corrigé → 0 |
| 3-Rhodes | 0 Intro (vide → refait ?), 1 C1, 2 R1, 3 C2 | inst 1 · Treated Rhodes | + riff scène 8 (à traiter) |
| 4-Pad | 0 Intro, 1 C1, 2 R1, 3 C2 | inst 2 · MKS-70 Warm Pad | + Auto Filter (device 1) |
| 5-Pluck | 3 C2 | inst 3 · Icy Pluck | gouttes ≥ C2 |
| 6-Lead | — | inst 4 · Subtle Lead | pas encore en scène |
| 7-Textures | 0 Intro, 1 R1, 2 C2 | inst 5 · Distant Thunder Rumble | volume global ajusté par David |

**Mapping Surge instances :** 0=Basse, 1=Rhodes, 2=Pad, 3=Pluck, 4=Lead, 5=Textures.

### Prochaines étapes
1. **Refrain 2 (mes. 49-56)** : Lead + shaker.
2. **Pont (mes. 57-64)** : Pad seul, sub drop.
3. **Refrain final x2 (mes. 65-80)** + **Outro (mes. 81-88)** à 8 (Low Pass descendant).
4. Réglages : reposer le tempo à 72 (accord avec David → le riff scène 8 est en E min / G maj, à transposer ou a adapter).
5. Arrangement (session → timeline) puis chaînes FX bus/master.

---

## 7. NOTES DE MIXAGE

- **Le silence est un instrument.** Laisser des mesures presque vides.
- **La voix au centre**, tout le reste autour. Baryton dominant sans forcer (comp 3:1, GR 3-4 dB).
- **Réverb longue sur pad et textures uniquement.** Rhodes, basse, drums restent secs — c'est ce contraste qui crée la profondeur.
- **Filtre les aigus.** LP 6 kHz sur le master, coupe douce. Rien ne doit briller.
- **Le morceau doit sonner comme un souvenir**, pas comme une performance.