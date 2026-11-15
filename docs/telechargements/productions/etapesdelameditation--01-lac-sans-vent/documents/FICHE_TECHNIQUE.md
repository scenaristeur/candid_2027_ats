# Lac sans vent — Fiche technique

> Morceau issu de « Les étapes de la méditation » (Kamalashila). Version de travail, à mettre à jour au fil des décisions.

## En-tête

- **Tempo :** 104 BPM, 4/4.
- **Tonalité :** Do# mineur (validée, voir Notes de production). Grille transposée depuis Ré mineur.
- **Durée estimée :** 76 mesures ≈ 176 s à 104 BPM (structure ci-dessous).
- **Style :** gospel-funk incantatoire, « gospel tibétain », musique actuelle.
- **Voix :** baryton, lead parlé-chanté, chœur en appel-réponse dans l'aigu.
- **Tessiture chantée (mesurée) :** D#2 à C#3 (convention Ableton), soit environ 154 à 272 Hz. Médiane vers 210 Hz (G#2).

## Structure (en mesures)

| Section | Mesures | Énergie | Contenu |
|---|---|---|---|
| Intro | 8 | basse | orgue, tambourin/shaker, « Calme… Vision… Union… » |
| Couplet 1 | 8 | moyenne | voix seule et groove |
| Pré-refrain | 4 | montée | chœur en écho |
| Refrain | 8 | haute | « Calme — Vision — Union ! » |
| Couplet 2 | 8 | moyenne | shamatha / vipashyanā |
| Pré-refrain | 4 | montée | idem |
| Refrain | 8 | haute | idem |
| Pont | 8 | basse → montée | half-time, claps à la 2e passe |
| Vamp | 16 | haute | call & response, ad libs |
| Outro | 4 | baisse | chuchoté, filtre qui se referme |

## Grille d'accords (Do# mineur)

Boucle de 4 mesures : **C#m9 | A∆9 | E6 | B** (transposition de Dm9 | B♭∆9 | F6 | C).

## Pistes (index 0-based)

| Index | Nom | Moteur / source | Contenu |
|---|---|---|---|
| 0 | 1-Selector Kit Warm | Drum Rack (kit `Selector Kit Warm.adg`) | clip « S1 Groove » |
| 1 | 2-calme vision union | audio, guide vocal | clip « calme vision union » (texte de la première version, à remplacer) |
| 2 | 3 Basse | Surge XT, patch **Acid Funk Bass** (Kinsey Dulcet) | clip « S1 Basse » |
| 3 | 4 Rhodes | Surge XT, patch **Treated Rhodes** (Bluelight) | vide |
| 4 | 5 Nappe | Surge XT, patch **Analog Pad** (Stefan Singer). Trois oscillateurs à 1 voix chacun, sans effet. Remplace Iso Pad, trop lourd (unisson de 8 voix et chaîne d'effets). | vide |
| 5 | 6 Pluck | Surge XT, patch **Bandpass Pluck** (Kyurumi) | vide |
| 6 | 7-Guide vocal | Drum-less guide : instrument **Celeste** (Live, Sounds > Mallets). MIDI, arrangement, mesure 21. Brouillon du refrain tiré de la voix de David, à valider. | Clips de session « Guide - Refrain 1 » (scène 4) et « Guide - Refrain 2 » (scène 7), 8 mesures chacun, dupliqués en arrangement aux mesures 21 et 41 (mêmes notes : même texte). Brouillon à valider. Guides des autres sections (Couplet 1, Pré-refrain 1 et 2, Couplet 2, Pont, Vamp, Outro) : **composés à partir du texte, pas chantés**, pour inspirer David. Placés en session (scènes 2, 3, 5, 6, 8, 9, 10) et dupliqués en arrangement. À réécrire d'après la voix de David. |

### Détail des pistes

- **Batterie (0) :** caisse sur 1 et « et » de 3, caisse claire sur 2 et 4, charley fermé en 16es sauf la dernière 8e de mesure, open hat sur cette dernière 8e, shaker sur les contretemps (le kit n'a pas de tambourin). Vélocités 80/65/50 en 16es, accents sur les temps.
- **Voix guide (1) :** warp **Complex Pro**, tempo d'origine **90,69 BPM** (warp réglé dans Live par David).
- **Basse (2) :** fondamentale seule sur chaque accord, rythme 1 / « et » de 2 / 3 / « et » de 4. Vélocités 100/85/90/80. Notes en MIDI 37 (C#2), 33 (A1), 40 (E2), 35 (B1). Fréquences réelles : 55 à 82 Hz. Chaîne : Surge XT (Acid Funk Bass), puis **Auto Filter** en passe-bas, fréquence 130 Hz (paramètre à 0,271), pente 24 dB, résonance 0.
- **Batterie (0) — chaîne :** Channel EQ, bande médium à 150 Hz, -3 dB (paramètre Mid Gain à 0,4). Provisoire : la coupe est large et touche aussi la grosse caisse et la caisse claire.

## Clips

| Piste | Clip | Longueur | Contenu |
|---|---|---|---|
| 0 | S1 Groove | 32 temps (8 mesures) | batterie, 192 notes, groove assigné |
| 1 | calme vision union | 274 s | guide vocal audio, **paroles à remplacer** |
| 2 | S1 Basse | 32 temps (8 mesures) | basse, 32 notes, groove assigné |
| 3 | S1 Rhodes | 32 temps (8 mesures) | stabs Rhodes sur le « et » de 2 et de 4, 64 notes, groove assigné. Validé à l'écoute par David. |
| 4 | S1 Nappe | 32 temps (8 mesures) | accords tenus d'une mesure, une octave sous le Rhodes, vélocité 55, sans groove. Lancé. Ouverture de filtre à l'intro et à l'outro : **pas encore écrite**. |
| 0 | S2 Groove - Couplet 1 | 32 temps (8 mesures) | Couplet 1, dépouillé : grosse caisse, caisse claire, charley fermé. Sans shaker ni open hat. 152 notes, groove assigné. Lancé. |
| 2 | S2 Basse | 32 temps (8 mesures) | Couplet 1 : même ligne que S1 Basse, 32 notes, groove assigné. Lancé. |
| 4 | S2 Nappe | 32 temps (8 mesures) | Couplet 1 : même nappe que S1. Lancé. |
| 3 | (pas de clip) | — | Rhodes coupé pour le couplet 1 (stop_clip sur la session 0). |
| 0 | S3 Groove4M - Pré-refrain | 16 temps (4 mesures) | Pré-refrain : batterie complète (avec shaker et open hat), vélocités des hats qui montent de mesure en mesure (×1,00 à ×1,24). 96 notes, groove assigné. Non lancé. |
| 2 | S3 Basse | 16 temps (4 mesures) | Pré-refrain : même ligne que S1. Non lancé. |
| 3 | S3 Rhodes | 16 temps (4 mesures) | Pré-refrain : stabs sur le « et » de 2 et de 4, vélocité en montée. Non lancé. |
| 4 | S3 Nappe | 16 temps (4 mesures) | Pré-refrain : nappe plus présente (vélocité 60 à 74). Non lancé. |
| 0 | S4 Groove - Refrain | 32 temps (8 mesures) | Refrain : batterie complète. 192 notes, groove assigné. Non lancé. |
| 2 | S4 Basse | 32 temps (8 mesures) | Refrain : ligne de basse de S1. Non lancé. |
| 3 | S4 Rhodes | 32 temps (8 mesures) | Refrain : stabs de S1. Non lancé. |
| 4 | S4 Nappe | 32 temps (8 mesures) | Refrain : nappe à vélocité 65. Non lancé. |
| 0 | S5 Groove - Couplet 2 | 32 temps (8 mesures) | Couplet 2 : dépouillé comme le couplet 1. Caisse claire fantôme sur le « et » de 3 aux mesures paires, grosse caisse fantôme sur le « et » de 4 à la mesure 8. 157 notes, groove assigné. |
| 2 | S5 Basse - Couplet 2 | 32 temps (8 mesures) | Même ligne que S2 Basse, sauf la mesure 8 : octave au-dessus sur le « et » de 4. |
| 4 | S5 Nappe - Couplet 2 | 32 temps (8 mesures) | Accords tenus, une octave sous le Rhodes, vélocité 55. |
| 0 | S6 Groove4M - Pré-refrain 2 | 16 temps (4 mesures) | Pré-refrain 2 : même montée que S3. Mesure 4 : roulement de caisse claire en 16es, vélocité de 60 à 102, qui remplace la caisse claire du « 4 ». |
| 2 | S6 Basse - Pré-refrain 2 | 16 temps (4 mesures) | Mesure 4 : croches sur la fondamentale. Les mesures 1 à 3 restent sur la ligne habituelle. |
| 3 | S6 Rhodes - Pré-refrain 2 | 16 temps (4 mesures) | Mesures 1 à 3 : stabs du pré-refrain 1. Mesure 4 : Rhodes en croches, vélocité de 70 à 91. |
| 4 | S6 Nappe - Pré-refrain 2 | 16 temps (4 mesures) | Accords tenus, vélocité de 60 à 74. |
| 0 | S7 Groove - Refrain 2 | 32 temps (8 mesures) | Refrain 2 : batterie de S4, plus charley ouvert sur les mesures impaires et claps superposés à la caisse claire aux mesures 5 à 8. |
| 2 | S7 Basse - Refrain 2 | 32 temps (8 mesures) | Refrain 2 : ligne de S4, la mesure 4 de chaque cycle a une octave au-dessus sur le « et » de 4. |
| 3 | S7 Rhodes - Refrain 2 | 32 temps (8 mesures) | Refrain 2 : stabs de S4, plus un stab léger sur le temps 4 aux mesures 5 à 8. |
| 4 | S7 Nappe - Refrain 2 | 32 temps (8 mesures) | Accords tenus, vélocité 70. |
| 0 | S8 Groove - Pont | 32 temps (8 mesures) | Pont en half-time : grosse caisse sur 1 et 3, caisse claire sur 3, charley en croches. Claps superposés à la caisse claire aux mesures 5 à 8 (deuxième passe). 92 notes, groove assigné. |
| 2 | S8 Basse - Pont | 32 temps (8 mesures) | Fondamentale tenue sur 3,5 temps par accord. 8 notes. |
| 4 | S8 Nappe - Pont | 32 temps (8 mesures) | Accords tenus, vélocité 60. |
| 5 | S8 Pluck - Pont | 32 temps (8 mesures) | Arpège de 16es sur les accords du Rhodes, une octave au-dessus. Seule piste à jouer sur le pont. 128 notes, groove assigné. |
| 0 | S9 Groove16M - Vamp | 64 temps (16 mesures) | Vamp : batterie complète avec fills de caisse claire en 16es sur la dernière mesure de chaque groupe de 4. 396 notes, groove assigné. |
| 2 | S9 Basse - Vamp | 64 temps (16 mesures) | Mesures 1 à 2 silencieuses (le call du chœur). Ligne de basse à partir de la mesure 3. 56 notes. |
| 3 | S9 Rhodes - Vamp | 64 temps (16 mesures) | Mesures 9 à 16 : stabs en crescendo (vélocité de 85 à 106), sur le temps 1 et les « et » de 2 et de 4. 96 notes. |
| 4 | S9 Nappe - Vamp | 64 temps (16 mesures) | Accords tenus, vélocité 75. |
| 0 | S10 Groove4M - Outro | 16 temps (4 mesures) | Outro : grosse caisse sur le 1 des mesures 1 et 2, tambourin (shaker) en décroissance, puis shaker seul puis silence. 13 notes. |
| 2 | S10 Basse - Outro | 16 temps (4 mesures) | Fondamentale tenue sur les mesures 1 et 2, puis silence. |
| 4 | S10 Nappe - Outro | 16 temps (4 mesures) | Accords tenus en décroissance de vélocité : 55, 50, 40, 30. |
| — | Filtre de l'outro | — | **Pas encore automatisé** : la fermeture du filtre (intro et outro, nappe et batterie) reste à faire. |

## Groove et mix

- **Groove :** « Swing MPC 3000 16ths 57 » (Groove Pool), assigné aux clips S1 Groove et S1 Basse.
- **Montant global :** 1,0 (`groove_amount`). Ce réglage est global : il touche tous les clips qui ont un groove.
- **Tempo du set :** 104 BPM (il était à 90 au départ, la voix était à 90,69 d'origine).

## Plages de fréquences (mesures sur captures, voix seule)

- **Voix parlée :** fondamentale entre **105 et 165 Hz**, médiane 120 à 135 Hz. 90 % de l'énergie entre 110 et 420 Hz.
- **Voix chantée (refrain) :** fondamentale entre **154 et 272 Hz**, médiane 210 Hz. 90 % de l'énergie entre 161 et 818 Hz, centre vers 334 Hz.
- **Basse :** visée entre **40 et 100 Hz** pour rester sous la voix. Mesure sur la capture de la basse seule : 66 % de l'énergie sous 100 Hz, 88 % sous 200 Hz.

## Notes de production

- **Tonalité :** Do# mineur, validée par David. Les analyses de tonalité automatiques sont faibles (confiance 20 à 33 %) et contradictoires (La mineur, Do mineur) : la décision repose sur la tessiture mesurée, pas sur ces analyses.
- **Tessiture :** la tessiture D#2 à C#3 (154 à 272 Hz) est mesurée sur le refrain chanté (capture de 8 mesures, batterie et basse coupées). L'ancienne valeur E3 à B3 (MIDI 64 à 71, soit 330 à 494 Hz) était fausse : elle était à environ une octave au-dessus de la voix réelle. Corrigée.
- **Tonalité et tessiture :** en Do# mineur, le haut de la mélodie tombe sur C#3, la tonique une octave au-dessus. En Ré mineur, il monterait vers D3 (environ 294 Hz), au-dessus de la plage mesurée.
- **Filtre de la basse :** le cutoff du filtre 2 de la Surge (0,35 → 190 Hz affiché) n'a pas modifié le spectre mesuré. Valeur restaurée à 0,4846 (état d'origine). Le passe-bas est donc posé en Auto Filter, après la Surge.
- **Mesures d'équilibrage (scène 1, 8 mesures) :**
  - Basse seule, avant le passe-bas : 17 % de l'énergie entre 100 et 200 Hz. Après : 3 %.
  - Scène complète : 38 % entre 100 et 200 Hz, avant comme après le passe-bas. La batterie porte l'essentiel de cette zone (48 % de son énergie).
  - Après la coupe batterie à 150 Hz : 36 % entre 100 et 200 Hz.
  - Le passe-bas fait baisser le niveau de la basse seule (RMS 0,050 à 0,032) sans changer le mix.
- **Choix provisoire :** on ajustera selon les sections et les autres instruments. Options laissées ouvertes : coupe plus profonde sur le bus batterie, ou coupe ciblée sur la caisse claire et les toms via le pad.
- **Mesures :** les chiffres renvoyés par `capture_and_analyze` ne correspondent pas toujours au WAV écrit (une capture « voix seule » était muette sur le disque). Les mesures sont refaites sur les WAV, dans `data/analyses/`.
- **Pistes restantes :** Rhodes (stabs sur le « et » de 2 et de 4), nappe (très discrète, ouverture de filtre à l'intro et à l'outro), pluck (arpège 16es filtré, dans le pont). Patches chargés, rien n'est encore écrit. Les patchs ont été choisis par la recherche de la bibliothèque Surge : le « Cathedral Pad » des notes n'existe pas dans cette installation.
- **Paroles :** la version 2 (ligne 238 du fichier de conversation `Chanson méditation Kamalashila.md`) est la version retenue. Le guide vocal actuel contient encore la version 1.
- **Nommage :** « 3 Basse », « 4 Rhodes » et suivants n'ont pas le tiret des deux premières pistes. À harmoniser.
