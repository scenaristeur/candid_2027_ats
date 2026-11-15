# 04 — Jean Lassalle — La Chasse aux Parrainages

**Statut** : préparation documentaire — aucune session Ableton ouverte pour ce morceau.
**Tempo** : 68 BPM *(proposition, à valider)*
**Tonalité** : Sol mineur (Gm) *(proposition, à valider à l'oreille)*
**Signature** : 4/4
**Durée cible** : ≈ 2 min 30
**Atmosphère** : Montagne, berger, patience
**Style** : Chant béarnais traditionnel, voix seule, paysages
**Voix** : baryton parlé-chanté de David, E3–B3 (MIDI 64–71, convention Ableton C3 = 60).

---

## 1. Le candidat — brief du 14/11/2026

| | |
| :--- | :--- |
| **Profil** | Ancien député des Pyrénées-Atlantiques, maire de Lourdios-Ichère pendant 40 ans, figure de Résistons ! |
| **Couleur politique** | Ruralisme, antisystème, sincérité revendiquée. |
| **Actions déjà menées** | Candidat en 2017 et 2022 (3,13 %) ; grève de la faim pour sauver des emplois ; chants à l'Assemblée ; cagnotte pour financer sa campagne. |
| **Programme 2027** | Pas de programme 2027 publié ; le site de Résistons ! présente encore celui de 2022 : réduction forte de l'immigration légale, quotas annuels, restriction du droit du sol. |
| **Pour** | Électeurs des territoires ruraux qui se sentent oubliés ; voix « contre le système ». |
| **Contre** | Programme flou sur l'économie ; candidature pressentie, conditionnée à une cagnotte de 100 000 € ; environ 250 parrainages revendiqués. |
| **Actualité** | Il parle de « chasse aux parrainages » plus que de campagne. |
| **Transition Marseillaise** | « Entendez-vous… dans nos montagnes ? » |

> **Fiabilité** : contenu issu de `Candidats 2027.md` (compilation interne du 14/11/2026). Chaque chiffre, score et procédure doit être revérifié et **daté** avant l'enregistrement. L'album doit pouvoir dire sa date de vérité.

## 2. Ce que la chanson doit faire

- Prendre la sincérité au sérieux, y compris quand elle tient lieu de programme.
- Dire ce que l'absence de programme signifie pour un vote.
- Parler des territoires sans les idéaliser.

## 3. Structure (en barres)

Intro voix seule (8) → Couplet 1 (16) → Refrain (8) → Couplet 2 (16) → Refrain (8) → Pont (8) → Refrain final (8) → Outro (8) = 80 barres

## 4. Grille d'accords (proposition)

| Section | Grille (4 mesures) | Couleur / intention |
| :--- | :--- | :--- |
| **Couplet** | `| Gm | Eb | Bb | F |` | Chant de montagne, ample. |
| **Refrain** | `| Eb | Bb | F | Gm |` | Le refrain s'élargit comme une vallée. |

## 5. Palette Live 12 Lite (proposition)

| Piste | Rôle | Instrument / Kit | Index |
| :--- | :--- | :--- | :--- |
| `1-Voix` | Chant | Audio | 0 |
| `2-Guitare` | Harmonie | Simpler (acoustique) | 1 |
| `3-Accordéon` | Couleur | Drift (accordéon) | 2 |
| `4-Basse` | Fondation | Drift (basse acoustique) | 3 |

> 8 pistes maximum (Live 12 Lite). Index **0-based** ; le nom porte l'index 1-based : `1-Batterie` = index 0.

## 6. Intention de mix

Voix très nue, presque sans compression. Un souffle de montagne (bruit filtré) peut tenir le fond.

## 7. À vérifier avant d'enregistrer

- Son statut de candidature au 14/11/2026.
- Le programme de 2022 et ce qui reste en ligne.
- Le nombre de parrainages et la cagnotte.

## 8. Notes de production

Ne pas imiter l'accent : chanter avec le sien. Le morceau doit sentir le froid.

## 9. Session et steps de production

> La structure complète (§3) reste la cible lointaine. **À ce stade, on ne construit que trois scènes : Intro / Refrain / Outro.** Le tableau §5 décrit la couleur idéale ; l'implémentation réelle en 8 pistes mutualisées est ci-dessous. En cas de conflit, **c'est §9 qui fait foi**.

**Session** : C — Traditionnel / militaire / populaire
**Scènes réservées** : S01–S03 (Intro / Refrain / Outro) — scène S16 libre
**Tempo de scène** : 68 BPM · **Tonalité de travail** : Sol mineur (Gm) · **Signature** : 4/4
**Chaînes à armer** : Harmonie = guitare acoustique · Mélodie = accordéon · Texture = vent de montagne
**Kit de batterie de la session** : Tambour + grosse caisse (Impulse ou kit .adg)

| Piste | Index | Rôle | Instrument / chaîne |
| :--- | :--- | :--- | :--- |
| `1-Batterie` | 0 | Rythme | Impulse / Drum Rack — tambour, grosse caisse |
| `2-Basse` | 1 | Fondation | Drift — basse acoustique |
| `3-Harmonie` | 2 | Accords | Instrument Rack — 5 chaînes accordéon/guitare/piano |
| `4-Mélodie` | 3 | Hook | Instrument Rack — 5 chaînes fifre/cuivres |
| `5-Texture` | 4 | Chœur / ambiance | Instrument Rack — 2 chaînes : chœur, salle |
| `6-Percs/FX` | 5 | Transitions | Percussions — tambourin, caisse |
| `7-Guide` | 6 | Voix guide | Drift — voix douce |
| `8-Voix` | 7 | Chant final | Audio |

### Steps

1. **Créer les scènes.** Dans la session C, trois scènes consécutives : `S01 <Candidat> Intro`, `S02 <Candidat> Refrain`, `S03 <Candidat> Outro`. La scène S16 reste vide (réserve).
2. **Tempo et tonalité.** Régler le tempo de scène à 68 BPM (propriété de scène ; si l'outil ne l'expose pas, le faire à la main) et vérifier 4/4. La tonalité Sol mineur (Gm) est un repère d'écriture, pas un réglage à automatiser.
3. **Armer les chaînes.** Harmonie = guitare acoustique, Mélodie = accordéon, Texture = vent de montagne. Vérifier le **chain selector** de chaque rack sur la valeur du candidat : c'est ce qui permet 5 sons différents sur la même piste.
4. **Écrire l'harmonie du refrain.** 8 mesures, grille `| Eb | Bb | F | Gm |`. Accords réels (vérifier les notes contre le nom), pas de renversement inutile. Vélocités 70–85, légères variations pour éviter le MIDI plat.
5. **Écrire basse et batterie.** Motif du style (Chant béarnais traditionnel, voix seule, paysages), 8 mesures. Vélocités : kick 90–100, snare 85–95, hats 55–75. La basse suit la fondamentale, sans doubler la voix.
6. **Écrire le hook puis le guide vocal.** Mélodie du refrain sur `4-Mélodie`, 1 note par syllabe, tessiture **E3–B3 (64–71)**. Paroles : `PAROLES.md`. Guide chanté sur `7-Guide`, vélocités qui phrasent (75–110), pas une note plate.
7. **Intro (4–8 mesures).** Un ou deux éléments seulement : texture + basse, ou batterie + nappe. Ne pas jouer le refrain avant la scène Refrain.
8. **Outro / transition (4 mesures).** Accord tenu + transition Marseillaise : « Entendez-vous… dans nos montagnes ? ». Si l'outro est coupée, garder au moins 2 mesures de queue pour l'enchaînement.
9. **Valider, puis figer.** Solo chaque piste, capture **une à la fois**, noter le RMS et ce qui a changé. Ensuite : nommer les clips, noter tempo/tonalité dans la fiche, et ne plus toucher la scène validée.

### Garde-fous

- **8 pistes maximum.** Si un instrument manque, ajouter une **chaîne** dans un rack — jamais une piste.
- **5 chaînes par rack au maximum.** Préférer Drift/Simpler à Surge XT : le coût CPU de Surge est par voix.
- **16 scènes maximum** : 15 utilisées (5 candidats × 3) + 1 libre.
- **Ne pas changer le kit de batterie** de la session sans revalider les quatre autres candidats.
- **Une seule capture à la fois.** Le set Ableton ne doit pas jouer pendant une capture.
- Une scène validée ne se réouvre pas pour « améliorer » : on note l'idée pour la suivante.

## Paroles

Voir `PAROLES.md` dans ce dossier (squelette à écrire).
