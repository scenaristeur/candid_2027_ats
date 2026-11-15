# Danse tes illusions

**Tempo** : 92 BPM
**Tonalité** : La mineur (Am), alternance Am / G toutes les deux mesures
**Signature** : 4/4
**Durée** : ≈ 7 min 15 s (168 mesures, 672 temps)
**Atmosphère** : Dub nocturne, chaud et spacieux ; une couleur « faubourg de Kingston »
**Style** : Dub qui garde son empreinte (delays, reverb, espace) mais tend vers la largeur mélancolique de Pink Floyd (« Shine On You Crazy Diamond » comme référence spectrale)
**Voix** : aucune pour l'instant — instrumental

## Références sonores

- **Kingston / dub** : rim sidestick sur le skank, tambourin sur les contretemps, shaker sur les temps, delays et reverb partout, basse en colonne vertébrale.
- **Pink Floyd** : la guitare lead porte le sustain de Gilmour (phaser + saturateur), le bugle tient des notes longues sur le pont, le Glacial est un chant d'oiseau au loin.

## Structure (en mesures)

| Section | Mesures | Énergie | Contenu |
| :--- | :--- | :--- | :--- |
| Intro | 1-16 | faible | basse + batterie seuls ; le Glacial y fait 3 appels d'oiseau ; fill piano en 14-16 |
| Couplet 1 | 17-32 | moyenne | entrée du skank piano ; Glacial discret |
| Refrain 1 | 33-48 | haute | cuivres en stabs, shaker plein, tambourin |
| Break (dub) | 49-64 | basse | presque vide : nappes de bugle, espace |
| Couplet 2 | 65-80 | moyenne | |
| Refrain 2 | 81-96 | haute | |
| Pont | 97-112 | sommet | **solo de bugle** (la phrase longue) ; tout est le plus dense |
| Refrain 3 | 113-128 | haute | |
| Couplet 3 | 129-144 | moyenne | |
| Pré-outro | 145-160 | descendante | |
| Outro | 161-168 | éteinte | nappe finale de bugle, le reste se retire |

> Structure calée sur des blocs de 16 mesures (sauf l'outro, 8). Pas de cue points dans le projet — les bornes sont celles utilisées pour toute l'écriture.

## Grille d'accords

| Section | Grille | Couleur |
| :--- | :--- | :--- |
| Partout | `| Am | Am | G | G |` (alternance toutes les 2 mesures) | Mineur qui respire ; le G majeur ouvre sans résoudre. |

Notes réelles : **Am** = A C E (pitch 57-60-64), **G** = G B D (pitch 55-59-62). Vérifié contre le piano et la basse.

## Instruments (Ableton) — Mix

| Piste | Index | Instrument | Pan | Vol | Chaîne FX |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Batterie** | 0 | 505 Core Kit (Drum Rack) | 0 | 0.85 | Utility (Output 0.2) → Compressor → MEqualizer |
| **Piano skank** | 1 | Grand Piano Single Sample (Simpler) | 0 | 0.90 | Auto Filter (passe-bas Freq 0.22) → MEqualizer → Chorus-Ensemble (Rate 0.25, Amount 0.35, Dry/Wet 0.22) |
| **Basse** | 2 | Basic Jupo Bass | 0 | 0.45 | MEqualizer → Saturator (Drive 0.8, Dry/Wet 0.75, Output 0.72) → Compressor (bypassé, sidechain à armer à la main) |
| **Glacial** (oiseau) | 3 | Drift « Glacial Tolerance » | 0 | 0.67 | Auto Filter (passe-haut Freq 0.28, Drive 0.21) |
| **Guitare halo** | 5 | Surge XT (une octave au-dessus) | −0.22 | 0.38 | MTremolo (Depth 0.22) → Auto Filter |
| **Guitare lead** | 6 | **Guitar Electric Clean** (vraie guitare, rack d'échantillons) | +0.08 | 0.72 | MTremolo → MSaturator (Dry/Wet 0.35) → MEqualizer → MPhaser (Dry/Wet 0.18, Feedback 0.4) → Auto Filter (HPF 0.30) |
| **Bugle** | 7 | Ac Flugelhorn | 0 | 0.85 | Delay (insert dub : L 2×16, R 3×16, Feedback 0.5, Dry/Wet 0.32, échos assombris) → Auto Filter (passe-haut 0.28) |

> Les pistes 5 et 6 sont **dans le groupe** (index 4, illisible par l'API). Patchs Surge **sauvegardés en patch utilisateur par David** (base « Synth Guitar 2 » modifiée — l'OSC remonte encore le nom d'usine, mais la sauvegarde est faite).

### Sends / Returns

- **A-Reverb** : Predelay 0.26, Decay 0.44, Room Size 0.79. Sends — batterie 0.24, piano 0.33, basse 0.25, Glacial 0.45, guitares 0.38 / 0.28, bugle 0.30.
- **B-Delay** : Time 0.34, Feedback 0.22. Sends — piano 0.62, Glacial 0.74, guitares 0.38 / 0.45, bugle 0.22.

### Groove

Tous les clips d'instruments partagent le **même groove (index 0)** — cohésion rythmique.

## Patterns par piste

### Batterie (index 0)
- **Grosse caisse (36)** : « Kick 808 Boom Short », temps 1 et 3, vélocité ~73. **Doubles caisses** ajoutées : contretemps du 3 (offset 2.5) une mesure sur 2 dans les refrains, toutes les mesures + contretemps du 2 dans le pont, une sur 4 dans les couplets. Vélocité 60-63. Jamais dans l'intro, le break, l'outro.
- **Rim sidestick (37)** : temps 2 et 4 — le skank. Sample remplacé par « Rim Sidestick Soft Dry Session ».
- **Tambourin (42)** : « Bell Tambo FX.wav » sur les contretemps (0.5, 1.5, 2.5, 3.5). Disparaît de l'intro et du break, se double dans les refrains et le pont.
- **Shaker (52, E2)** : « Shaker 70s MPC.wav » sur les temps (0,1,2,3) — avec le tambourin, ils tissent des doubles croches. Refrains, pont, couplet 3 seulement.
- **Toms (44/45/47)** : accordés **48 / 54 / 60** (étaient tous à 63.5). Fill annonce des cuivres mesure 32 (descente Hi→Mid→Lo + crash mesure 33).

### Piano skank (index 1)
- Accord (C3+E3) sur les temps 1 et 3, basse (A2) sur les temps 2 et 4. Absent de l'intro et du break.
- **Fill d'annonce mesures 14-16** : esquisse le skank en crescendo, puis montée La→Do→Mi (45→48→52) sur la fin de la mesure 16, qui atterrit mesure 17.

### Basse (index 2)
- Riff Am/G, fondamentales 49-82 Hz. Ghost notes et arcs de vélocité travaillés.

### Glacial (index 3) — le chant d'oiseau
Pas un pad : des **appels** brefs et hauts (1,05-2,96 kHz). Deux logiques :
- **Réponses** : posées après les fins de phrase de guitare ou dans les fenêtres de silence mélodique, réparties dans le temps, jamais deux fois au même endroit.
- **Anticipations** : une note de l'accord *suivant* sur le contretemps de 4, avant chaque changement d'harmonie (sauf intro, break, outro).
- 195 notes au total. Le contenu harmonique vient toujours des notes réelles du piano (ou de la basse) — **aucune note inventée**.

### Guitares (index 5 et 6)
- **Le lead (6) est une vraie guitare** depuis la refonte : « Guitar Electric Clean » (rack d'échantillons), choisi par audition mesurée contre 4 autres candidates. **La mélodie a été transposée une octave vers le bas** (67 % des notes étaient au-dessus du Mi6, hors du registre d'une guitare réelle) — le lead chante maintenant dans le registre médium, ce qui est aussi plus proche de Gilmour. Le Surge d'origine est remplacé (patch sauvegardé par David).
- La **halo (5)** reste un Surge aigu, une octave au-dessus — elle fait le scintillement au-dessus de la vraie guitare.
- La chaîne Gilmour (saturateur + phaser) a survécu au changement d'instrument.

### Bugle (index 7)
Découpé en **9 clips nommés par section** (Refrain 1 m.33, Break m.49, Couplet 2 m.65, Refrain 2 m.81, Pont m.97, Refrain 3 m.113, Couplet 3 m.129, Pré-outro m.145, Outro m.161).
- **Stabs Kingston** (refrains) : accords sur les temps 2 et 4, avec le rim.
- **Nappes Floyd** (break, pré-outro, outro) : accords longs.
- **Le pont (97-112) = le solo** : ligne de 15 notes longues qui monte vers un Mi5 (m.105), un **Si tenu 6 temps** (m.107-108, le geste Gilmour), puis descente qui se pose dans le grave (Si3, m.112).
- **Réponses dans les couplets** (ajoutées) : une courte réponse tierce+quinte de l'accord sur le contretemps de 3, toutes les 4 mesures, dans les trois couplets (clips Couplet 1, 2 et 3).

## Réglages Mix

| Piste | Vol | Pan | Notes |
| :--- | :--- | :--- | :--- |
| Batterie | 0.85 | 0 | Utility Output 0.2 + Compressor tiennent le socle |
| Piano skank | 0.90 | 0 | désaccord −11 cents corrigé, release 0.40 |
| Basse | 0.45 | 0 | Saturator Drive 0.8 — les harmoniques 300-600 Hz la font exister sur téléphone |
| Glacial | 0.67 | 0 | Drift : LP 0.85, Res 0.45, attaque 0, spread 0.35 |
| Guitare halo | 0.38 | −0.22 | send réverb ramené de 1.0 à 0.38 (c'était le « hors sol ») |
| Guitare lead | 0.61 | +0.08 | chaîne Gilmour réactivée (saturateur + phaser étaient bypassés) |
| Bugle | 0.85 | 0 | réglé par David |

**Master** : 0.85 (unité dans cette installation). Chaîne de mastering posée : **Compressor glue** (Threshold 0.4, Ratio 0.7, Attack 0.55, Release 0.3) → **Limiter** (Ceiling 0.95 ≈ −1 dB, Lookahead ~3 ms). Vérifié sans écrêtage (0 échantillon collé, true peak −1,84 dBFS).

**Passe-haut multi-support** : piano (Auto Filter 0.28 ≈ 140 Hz), guitare lead (0.30 ≈ 160 Hz), bugle (Auto Filter ajouté, 0.28). La guitare halo (0.38) et le Glacial étaient déjà filtrés. Résultat mesuré : 160-250 Hz à −29 %, le sub dégagé pour la basse et le kick.

**Sidechain kick→basse** : actif. Compressor sur la basse, source « 1-505 Core Kit, Post FX » (choisie à la main par David — l'API ne l'expose pas), S/C On, Ratio 0.88, Threshold 0.46, Release 0.35. La basse s'efface à chaque grosse caisse (pompage discret).

**Grosse caisse** : le 505 a été remplacé par **« Kick 808 Boom Short.aif »** (posé sur le pad 36, sélectionné à la main). Le sub 20-50 Hz passe de 7 % à 33 % — c'est le kick dub profond. Si la traîne de sub se bat avec la basse, la raccourcir via le Fade Out du Simpler, ou essayer « Kick 808 Boom Filtered » (attaque plus douce).

## Notes de production

- **Le rim d'origine a été remplacé** par un sidestick doux (sample externe posé sur le pad) plutôt que compensé à l'EQ — la bande 2-3,2 kHz agressive est passée de 0,96 % à 0,64 %.
- **La guitare « hors sol »** n'était ni un timbre ni un niveau : la piste halo envoyait 100 % dans la réverb. Resserrée (send 0.38, trémolo 0.22, pans resserrés).
- **Le chargement d'un sample sur un pad remplace le pad sélectionné dans Live** (geste manuel de David) ; les outils de pad continuent d'afficher l'ancien nom — vérifier à l'oreille.
- **Budget 8 pistes** : 7 pistes audibles + le groupe Surge. La piste 9 (copie de sauvegarde du bugle) a été supprimée après validation de la découpe.

## Pistes d'amélioration — état

### Fait
1. ✅ **Chaîne master** : Compressor glue + Limiter (true peak −1 dB). Posée et vérifiée sans écrêtage.
2. ✅ **Passe-haut multi-support** sur piano, guitare lead et bugle (le Glacial et la halo étaient déjà filtrés).
6. ✅ **Réponses de bugle dans les trois couplets** (tierce + quinte de l'accord, contretemps de 3, toutes les 4 mesures).

### Reste — geste manuel ou décision de David
3. ✅ **Sidechain grosse caisse → basse** : fait (source armée par David, pompage discret vérifié).
5. ✅ **Grosse caisse** : 505 → **Kick 808 Boom Short**. Sub profond. Réserve : si la traîne se bat avec la basse, raccourcir le Fade Out du Simpler ou essayer « Kick 808 Boom Filtered ».
4. ℹ️ **Send delay sur le Glacial** : déjà à 0.74 — l'oiseau est déjà loin. Ne pas en rajouter.

### Structure / contenu — à trancher
7. **Durée 7 min 15** — long. Assumer la longueur dub, ou resserrer un couplet.
8. **Tempo mesuré 92,21 BPM** — arrondir à 92 pile si ce n'est pas voulu.
9. **Pas de voix** — instrumental. David est baryton (tessiture E3-B3, parlé-chanté) ; le morceau est en Am, compatible. Un guide vocal est possible.
