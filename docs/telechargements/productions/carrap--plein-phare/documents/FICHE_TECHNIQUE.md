# Plein Phare — Fiche Technique

**Chanson :** Plein Phare · **Style :** Rap mélodique / Trap chantée (half-time)
**Projet Ableton :** Live Lite · **Tempo :** 140 BPM · **Mesure :** 4/4 · **Tonalité :** Mi mineur (Em)
**Durée arr. :** ~1:29 (52 mesures, 208 beats)
**État :** Maquette à créer (clés et grilles = propositions à valider à l'oreille)

## Structure / Arrangement (beats 0-based)

| Section | Mesures | Beats | Contenu |
|---|---|---|---|
| Intro | 1-4 | 0-15 | Piano sombre + hats qui montent, **chuchoté**, riser |
| Refrain | 5-12 | 16-47 | Hook ×2 (Em→C→G→D), 808 + clap de plein |
| Couplet 1 | 13-20 | 48-79 | Flow parlé sec, 808 + pianos |
| Pont | 21-24 | 80-95 | Breakdown (Am→Em→C→D), tension |
| Refrain | 25-32 | 96-127 | Hook ×1 |
| Couplet 2 | 33-40 | 128-159 | Flow + mélodies désinvoltes |
| Refrain | 41-48 | 160-191 | Hook final, tutti |
| Outro | 49-52 | 192-207 | Drums qui se vident, échos |

## Grille d'accords (Em mineur)

| Section | Grille |
|---|---|
| Intro | Em (tenu) |
| Refrain / Couplet | `Em \| C \| G \| D` (i–VI–III–VII) |
| Pont | `Am \| Em \| C \| D` |

- Basse : racine sur les temps 1 et 3 (half-time), slide vers les temps d'après.
- Piano : stabs sombres sur chaque accord au refrain ; couplets plus aérés (une attaque par accord).

## Pistes / Instruments (5 cœur + 2 returns + 1 voix)

| Piste | Device | Rôle | Note son |
|---|---|---|---|
| 0 | Gen Purpose Kit (ou kit trap) | Drums 808 | kick + clap, hats 16e, open hat |
| 1 | Analog/Wavetable (sub 808) | **Basse 808** | sin 40-60 Hz, Saturator (sub virtuel) |
| 2 | Piano sombre (rack) | Stabs + couplets | faible attack, réverb envoi |
| 3 | Warm Analog Pad (rack) | Nappes refrains | **couper bas (HPF ~150-200 Hz)** |
| 4 | Surge XT (arp/lead léger) | Arpégiateur spiendru du hook | doux, pas d'unison lourd |
| 5 | *(voix — audio)* | Lead vocal David | à enregistrer |
| Ret A | Reverb (Hall) | Retour espace | send 0.2-0.35 |
| Ret B | Delay (1/8) | Retour écho | send 0.15-0.3 |

Master : Compressor (glue) → Limiter True Peak (ceiling ~-1 dB, lookahead 3 ms).

## Chaînes FX natives (profil pop/rap)

- **Drums :** Drum Buss → Compressor → Saturator
- **Basse 808 :** Saturator → Compressor (sidechain kick)
- **Piano :** Reverb (send) → Compressor
- **Pad :** HPF (coupe bas) → Reverb (send) → Auto Filter
- **Lead/Arp :** Delay → Reverb → Auto Filter
- **Voix (à enregistrer) :** EQ Eight → Compressor → Reverb → Delay

## Pattern Drums (half-time, 1 mesure = 4 temps)

```
Kick:   X··· ···X ···· ····   (temps 1 et 3)
Clap:   ···· X··· ···· X···   (temps 2 et 4)
HiHat:  ··X· ·X·X ·X·· ·X·X   (16e, léger flam)
Open:   ···· ···· ·X·· ····   (fin de mesure)
808 slide sur le kick du temps 3
```

## Ad-libs

« Plein phare », « yeah », « let's go », « brr », « mets le son ».

## Cibles mix (mix-translation)

- Centroid global **~700-900 Hz** (EQ carving, pas trop d'aigus piano)
- Basse **40-60 Hz présente** + Saturator pour le sub virtuel (téléphone)
- HPF tout sauf kick/basse à ~150-200 Hz (dont le Pad)
- Limiter master ~-1 dB, voix devant au mix

## Workflow de production

1. Session : créer les clips par section (Intro / Refrain ×2 / Couplet / Pont) sur chaque piste.
2. Enchaîner scène par scène pour valider le flow.
3. `duplicate_to_arrangement(track, clip, destination_time)` **en beats exacts** (positions du tableau ci-dessus).
4. Fills de batterie 1 mesure avant chaque changement de section.
5. Enregistrer la voix, capturer/analyser, ajuster le mix, valider à l'oreille.

## Références

- Source : `sources/CarRap/3 chansons rap claquantes.md`
- Guide vocal : `PAROLES.md` (même dossier) · méthode `voice-guide` (E3–B3, note par phrase)