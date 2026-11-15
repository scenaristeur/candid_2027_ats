# À fond dans l'casque — Fiche Technique

**Chanson :** À fond dans l'casque · **Style :** Pop-rap / Jersey club / Hyperpop
**Projet Ableton :** Live Lite · **Tempo :** 155 BPM (ressenti half-time) · **Mesure :** 4/4 · **Tonalité :** Sol mineur (Gm)
**Durée arr. :** ~1:17 (50 mesures, 200 beats)
**État :** Maquette à créer (clés et grilles = propositions à valider à l'oreille)

## Structure / Arrangement (beats 0-based)

| Section | Mesures | Beats | Contenu |
|---|---|---|---|
| Intro | 1-2 | 0-7 | Synthés brillants, hats 2-step, voix pitchée « à fond », riser |
| Refrain | 3-10 | 8-39 | Hook ×2 (Bb→F→Gm→Eb), plein |
| Couplet 1 | 11-18 | 40-71 | Débit rapide ludique, drums half-time feel |
| Refrain | 19-26 | 72-103 | Hook ×1 |
| Pont | 27-30 | 104-119 | Build-up (Eb→F→Gm→Gm), levée de bras |
| Couplet 2 | 31-38 | 120-151 | Flow + mélodies |
| Refrain | 39-46 | 152-183 | Hook final, tutti, voix pitchées |
| Outro | 47-50 | 184-199 | Synthés s'effeuillent, chantéon pitché |

## Grille d'accords (Gm mineur)

| Section | Grille |
|---|---|
| Intro / Outro | Gm (tenu, arpège brillant) |
| Couplet | `Gm \| Bb \| F \| Eb` (i–III–VII–VI) |
| Refrain | `Bb \| F \| Gm \| Eb` (III–VII–i–VI, qui monte/coule) |
| Pont | `Eb \| F \| Gm \| Gm` |

- Basse : four-on-floor / bounce, racines exactes, sidechain sur le kick.
- Synthés : arpèges brillants (plucks) qui « piquent » — signature pop-rap.

## Pistes / Instruments (5 cœur + 2 returns + 1 voix)

| Piste | Device | Rôle | Note son |
|---|---|---|---|
| 0 | Gen Purpose Kit (ou kit trap) | Drums bounce | kick rebondissant, claps 2&4, hats 2-step/16e |
| 1 | Analog/Wavetable (sub 808) | **Basse saturée** | bounce sur les temps, Saturator (sub virtuel) |
| 2 | Bright Pluck (rack / Surge léger) | Arpèges hooks/refrains | attack rapide, brillant |
| 3 | Warm Analog Pad (rack) | Nappes de soutien | **couper bas (HPF ~150-200 Hz)** |
| 4 | Auto-Tune / voix pitchée (sample) | Chœur jersey « oh / eh / à fond » | pitch + forme courte |
| 5 | *(voix — audio)* | Lead vocal David | à enregistrer |
| Ret A | Reverb (Hall) | Retour espace | send 0.2-0.35 |
| Ret B | Delay (1/8 ou dotted) | Retour écho | send 0.15-0.3 |

Master : Compressor (glue) → Limiter True Peak (ceiling ~-1 dB, lookahead 3 ms).

## Chaînes FX natives

- **Drums :** Drum Buss → Compressor → Saturator (sidechain kick sur la basse)
- **Basse :** Saturator → Compressor (sidechain kick)
- **Pluck :** Delay (send) → Reverb (send) → Auto Filter (petit mouvement)
- **Pad :** HPF (coupe bas) → Reverb (send)
- **Voix pitchée :** Pitch + forme courte, léger Saturator, pan large
- **Voix (à enregistrer) :** EQ Eight → Compressor → Reverb → Delay

## Pattern Drums (bounce, 1 mesure = 4 temps)

```
Kick:   X··· X··· X··· X···   (four-on-floor, léger relâchement sur 2&4)
Clap:   ···· X··· ···· X···   (2&4)
HiHat:  ··X· X·X· ·X·· ·X·X   (16e rebondissantes, flam)
Open:   ···· ···· ·X·· ····   (fin de mesure)
Bruitage : stutter sur la voix (« à-fond-à-fond-à-fond ») dans l'instro
```

## Ad-libs & voix pitchées

« oh », « eh », « yeah », « let's go », « à fond » — voix chipmunk jersey en réponse.

## Cibles mix (mix-translation)

- Centroid global **~700-900 Hz** ; le pluck bright est à tenir en retrait pour ne pas exploser le centre.
- Basse **40-60 Hz présente** + Saturator pour le sub virtuel (téléphone).
- HPF tout sauf kick/basse à ~150-200 Hz.
- Limiter master ~-1 dB, **voix devant**, voix de chœur en large (pan ±40).

## Workflow de production

1. Session : clips par section (Intro / Refrain / Couplet / Pont) + boucle de stutter voix pitchée.
2. Valider la boucle de chœur jersey (signature du morceau).
3. `duplicate_to_arrangement(track, clip, destination_time)` **en beats exacts** (tableau ci-dessus).
4. Riser + silence 1 temps **juste avant chaque drop** (voir conseils « pour que ça claque »).
5. Enregistrer la voix, capturer/analyser, ajuster le mix, valider à l'oreille.

## Références

- Source : `sources/CarRap/3 chansons rap claquantes.md`
- Guide vocal : `PAROLES.md` (même dossier) · méthode `voice-guide` (F3–D4, note par phrase)