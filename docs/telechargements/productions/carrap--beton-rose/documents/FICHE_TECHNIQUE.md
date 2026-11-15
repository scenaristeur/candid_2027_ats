# Béton Rose — Fiche Technique

**Chanson :** Béton Rose · **Style :** Drill mélodique / Afro-drill
**Projet Ableton :** Live Lite · **Tempo :** 144 BPM · **Mesure :** 4/4 · **Tonalité :** Do mineur (Cm)
**Durée arr. :** ~1:20 (48 mesures, 192 beats)
**État :** Maquette à créer (clés et grilles = propositions à valider à l'oreille)

## Structure / Arrangement (beats 0-based)

| Section | Mesures | Beats | Contenu |
|---|---|---|---|
| Intro | 1-2 | 0-7 | Oud/flûte mélancolique + hats drill, 808 slide |
| Refrain | 3-10 | 8-39 | Hook ×2 (Cm→Ab→Eb→Bb), plein |
| Couplet 1 | 11-18 | 40-71 | Flow sec entre les 808 |
| Pont | 19-22 | 72-87 | Breakdown (Ab→Bb→Cm→Bb), voix qui s'élève |
| Refrain | 23-30 | 88-119 | Hook ×1 |
| Couplet 2 | 31-38 | 120-151 | Flow + mélodies |
| Refrain | 39-46 | 152-183 | Hook final, tutti |
| Outro | 47-48 | 184-191 | Mélodie intro + fade |

## Grille d'accords (Cm mineur)

| Section | Grille |
|---|---|
| Intro / Outro | Cm (tenu, mélodie oud) |
| Couplet | `Cm \| Eb \| Bb \| F` (i–III–VII–IV) |
| Refrain | `Cm \| Ab \| Eb \| Bb` (i–VI–III–VII, plus sombre/large) |
| Pont | `Ab \| Bb \| Cm \| Bb` |

- Basse : 808 avec **slide** sur les temps faibles (signature drill), racines exactes.
- Mélodie oud/flûte : motif 1 mesure sur Cm (C–Eb–G), reprise en intro et outro.

## Pistes / Instruments (5 cœur + 2 returns + 1 voix)

| Piste | Device | Rôle | Note son |
|---|---|---|---|
| 0 | Gen Purpose Kit (ou kit trap) | Drums drill | clap/rimbox, hats rapides, kick sparse |
| 1 | Analog/Wavetable (sub 808) | **Basse 808 slide** | sin 40-60 Hz, Saturator (sub virtuel) |
| 2 | Oud / Flûte → **Surge XT** (flûte douce) | Mélodie intro + phrasé | patch léger, pas d'unison |
| 3 | Warm Analog Pad (rack) | Nappes refrains | **couper bas (HPF ~150-200 Hz)** |
| 4 | Dark Piano (rack) | Stabs / tenues | couplets aérés |
| 5 | *(voix — audio)* | Lead vocal David | à enregistrer |
| Ret A | Reverb (Hall) | Retour espace | send 0.2-0.35 |
| Ret B | Delay (1/8) | Retour écho | send 0.15-0.3 |

Master : Compressor (glue) → Limiter True Peak (ceiling ~-1 dB, lookahead 3 ms).

## Chaînes FX natives

- **Drums :** Drum Buss → Compressor → Saturator
- **Basse 808 :** Saturator → Compressor (sidechain kick)
- **Oud/Flûte :** Reverb (send) → Delay (send), un léger Saturator si besoin
- **Pad :** HPF (coupe bas) → Reverb (send) → Auto Filter
- **Piano :** Reverb (send) → Compressor
- **Voix (à enregistrer) :** EQ Eight → Compressor → Reverb → Delay

## Pattern Drums (drill, 1 mesure = 4 temps)

```
Kick:   X··· ···· X··· ····   (temps 1 et 3, slide sur celui du 3)
Clap:   ···X X··· ···X X···   (contretemps serrés, accent 2&4)
HiHat:  ··X· ··XX ·X·X ··X·   (triplets/doubles-croches flam)
Rim:    ···· ···· ···· ····   (soulève les chutes de mesures)
```

## Ad-libs

« gang », « ouais », « béton », « jusqu'au sommet », « droit ».

## Cibles mix (mix-translation)

- Centroid global **~700-900 Hz** ; la flûte/oud monte le centre, pas trop d'aigus.
- Basse **40-60 Hz présente** + Saturator pour le sub virtuel (téléphone).
- HPF tout sauf kick/basse à ~150-200 Hz.
- Limiter master ~-1 dB, voix devant, delay sur les fins de ligne.

## Workflow de production

1. Session : clips par section (Intro / Refrain / Couplet / Pont) sur chaque piste.
2. Valider la scène oud intro (motif mémorable = identité du morceau).
3. `duplicate_to_arrangement(track, clip, destination_time)` **en beats exacts** (tableau ci-dessus).
4. Fills / rim rolls 1 mesure avant chaque changement de section.
5. Enregistrer la voix, capturer/analyser, ajuster le mix, valider à l'oreille.

## Références

- Source : `sources/CarRap/3 chansons rap claquantes.md`
- Guide vocal : `PAROLES.md` (même dossier) · méthode `voice-guide` (E3–C4, note par phrase)
- Patchs flûte/oud : `doc_surge/presets/PRESETS.md`