# 29 — Bruno Retailleau — L'Hiver démographique

**Statut** : préparation documentaire — aucune session Ableton ouverte pour ce morceau.
**Tempo** : 88 BPM *(proposition, à valider)*
**Tonalité** : Sol mineur (Gm) *(proposition, à valider à l'oreille)*
**Signature** : 4/4
**Durée cible** : ≈ 2 min 30
**Atmosphère** : Veillée, hiver, discipline de clan
**Style** : Chant traditionnel vendéen, tambour et fifre, ton grave
**Voix** : baryton parlé-chanté de David, E3–B3 (MIDI 64–71, convention Ableton C3 = 60).

---

## 1. Le candidat — brief du 14/11/2026

| | |
| :--- | :--- |
| **Profil** | Candidat des Républicains, ancien ministre de l'Intérieur, sénateur. |
| **Couleur politique** | Droite conservatrice, souverainiste et nataliste. |
| **Actions déjà menées** | A porté la loi « immigration » de 2024, des mesures de fermeté sur la sécurité, une politique nataliste. |
| **Programme 2027** | 197 milliards d'euros d'économies jusqu'en 2032 pour ramener le déficit sous 3 % du PIB en 2031 sans hausse d'impôts ; référendum sur l'immigration ; réforme constitutionnelle ; revenu familial et congé de naissance prolongé. |
| **Pour** | Politique migratoire restrictive ; baisse des dépenses publiques ; soutien affiché à la natalité. |
| **Contre** | Les 197 milliards interrogent sur les services publics touchés ; 5–8 % dans les sondages, derrière Philippe et Lisnard dans son propre camp ; conformité constitutionnelle du référendum sur l'immigration. |
| **Actualité** | Plan d'économies présenté le 12 octobre 2026, référendum sur l'immigration le 3 novembre 2026. |
| **Transition Marseillaise** | « Entendez-vous… dans nos campagnes ? » |

> **Fiabilité** : contenu issu de `Candidats 2027.md` (compilation interne du 14/11/2026). Chaque chiffre, score et procédure doit être revérifié et **daté** avant l'enregistrement. L'album doit pouvoir dire sa date de vérité.

## 2. Ce que la chanson doit faire

- Tenir ensemble deux choses : une inquiétude démographique réelle et un programme migratoire qui n'y répond pas forcément.
- Poser la question des 197 milliards : quels hôpitaux, quelles écoles, quelles routes ?
- Ne pas moquer le folklore ; s'en servir pour dire la rigueur.

## 3. Structure (en barres)

Intro tambour (8) → Couplet 1 (16) → Refrain (8) → Couplet 2 (16) → Refrain (8) → Pont (8) → Refrain final (8) → Outro (8) = 80 barres

## 4. Grille d'accords (proposition)

| Section | Grille (4 mesures) | Couleur / intention |
| :--- | :--- | :--- |
| **Couplet** | `| Gm | Eb | Bb | F |` | Cadence de marche, un pied après l'autre. |
| **Refrain** | `| Eb | Bb | F | Gm |` | Le refrain s'ouvre comme un chant de veillée. |

## 5. Palette Live 12 Lite (proposition)

| Piste | Rôle | Instrument / Kit | Index |
| :--- | :--- | :--- | :--- |
| `1-Tambour` | Rythme | Impulse (tambour) | 0 |
| `2-Fifre` | Mélodie | Drift (flûte) | 1 |
| `3-Basse` | Fondation | Drift (basse acoustique) | 2 |
| `4-Voix` | Chant | Audio | 3 |
| `5-Chœur` | Réponse | Audio / Drift (chœur) | 4 |

> 8 pistes maximum (Live 12 Lite). Index **0-based** ; le nom porte l'index 1-based : `1-Batterie` = index 0.

## 6. Intention de mix

Tambour sec et centré, fifre légèrement à gauche, voix devant. Pas de reverb moderne : une salle de grange suffit.

## 7. À vérifier avant d'enregistrer

- Le chiffre de 197 milliards et l'horizon 2031/2032.
- La recevabilité du référendum sur l'immigration au regard de la Constitution.
- La loi immigration 2024 : ce qui a été censuré par le Conseil constitutionnel.

## 8. Notes de production

Chant de veillée : privilégier une voix seule, puis un chœur masculin très simple sur le refrain. Le fifre ne doit pas couvrir la voix.

## 9. Session et steps de production

> La structure complète (§3) reste la cible lointaine. **À ce stade, on ne construit que trois scènes : Intro / Refrain / Outro.** Le tableau §5 décrit la couleur idéale ; l'implémentation réelle en 8 pistes mutualisées est ci-dessous. En cas de conflit, **c'est §9 qui fait foi**.

**Session** : C — Traditionnel / militaire / populaire
**Scènes réservées** : S13–S15 (Intro / Refrain / Outro) — scène S16 libre
**Tempo de scène** : 88 BPM · **Tonalité de travail** : Sol mineur (Gm) · **Signature** : 4/4
**Chaînes à armer** : Harmonie = accordéon / cordes · Mélodie = fifre · Texture = tambour
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

1. **Créer les scènes.** Dans la session C, trois scènes consécutives : `S13 <Candidat> Intro`, `S14 <Candidat> Refrain`, `S15 <Candidat> Outro`. La scène S16 reste vide (réserve).
2. **Tempo et tonalité.** Régler le tempo de scène à 88 BPM (propriété de scène ; si l'outil ne l'expose pas, le faire à la main) et vérifier 4/4. La tonalité Sol mineur (Gm) est un repère d'écriture, pas un réglage à automatiser.
3. **Armer les chaînes.** Harmonie = accordéon / cordes, Mélodie = fifre, Texture = tambour. Vérifier le **chain selector** de chaque rack sur la valeur du candidat : c'est ce qui permet 5 sons différents sur la même piste.
4. **Écrire l'harmonie du refrain.** 8 mesures, grille `| Eb | Bb | F | Gm |`. Accords réels (vérifier les notes contre le nom), pas de renversement inutile. Vélocités 70–85, légères variations pour éviter le MIDI plat.
5. **Écrire basse et batterie.** Motif du style (Chant traditionnel vendéen, tambour et fifre, ton grave), 8 mesures. Vélocités : kick 90–100, snare 85–95, hats 55–75. La basse suit la fondamentale, sans doubler la voix.
6. **Écrire le hook puis le guide vocal.** Mélodie du refrain sur `4-Mélodie`, 1 note par syllabe, tessiture **E3–B3 (64–71)**. Paroles : `PAROLES.md`. Guide chanté sur `7-Guide`, vélocités qui phrasent (75–110), pas une note plate.
7. **Intro (4–8 mesures).** Un ou deux éléments seulement : texture + basse, ou batterie + nappe. Ne pas jouer le refrain avant la scène Refrain.
8. **Outro / transition (4 mesures).** Accord tenu + transition Marseillaise : « Entendez-vous… dans nos campagnes ? ». Si l'outro est coupée, garder au moins 2 mesures de queue pour l'enchaînement.
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
