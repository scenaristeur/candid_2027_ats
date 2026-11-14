# 20 — Fabien Roussel — Vivre (Le Temps des Cerises électrique)

**Statut** : préparation documentaire — aucune session Ableton ouverte pour ce morceau.
**Tempo** : 116 BPM *(proposition, à valider)*
**Tonalité** : Do majeur (C) *(proposition, à valider à l'oreille)*
**Signature** : 4/4
**Durée cible** : ≈ 2 min 20
**Atmosphère** : Fête du parti, terroir et colère
**Style** : Chanson française populaire, accordéon et guitare électrique
**Voix** : baryton parlé-chanté de David, E3–B3 (MIDI 64–71, convention Ableton C3 = 60).

---

## 1. Le candidat — brief du 14/11/2026

| | |
| :--- | :--- |
| **Profil** | Secrétaire national du PCF, député du Nord, maire de Saint-Amand-les-Eaux. |
| **Couleur politique** | Gauche communiste, laïque, attachée aux services publics et au monde du travail. |
| **Actions déjà menées** | Candidature en 2022 (2,28 %) ; bataille pour les services publics ; proposition de 60 000 policiers et gendarmes de proximité. |
| **Programme 2027** | 60 000 postes de policiers, gendarmes et douaniers de proximité ; défense des services publics ; hausse du SMIC ; retraite à 60 ans. |
| **Pour** | Gauche de rupture mais institutionnelle, attachée au service public et à la sécurité républicaine. |
| **Contre** | Position minoritaire dans une gauche dominée par Mélenchon et Glucksmann ; risque d'être vu comme un candidat témoin. |
| **Actualité** | Sa candidature existe surtout pour porter les services publics dans le débat. |
| **Transition Marseillaise** | « Le jour de gloire est arrivé… pour les services publics ? » |

> **Fiabilité** : contenu issu de `Candidats 2027.md` (compilation interne du 14/11/2026). Chaque chiffre, score et procédure doit être revérifié et **daté** avant l'enregistrement. L'album doit pouvoir dire sa date de vérité.

## 2. Ce que la chanson doit faire

- Défendre les services publics avec des exemples concrets, pas avec le mot « vivre ».
- Prendre au sérieux la proposition sécuritaire de 60 000 postes, y compris ses contradictions.
- Montrer le risque du candidat témoin.

## 3. Structure (en barres)

Intro accordéon (8) → Couplet 1 (16) → Refrain (8) → Couplet 2 (16) → Refrain (8) → Pont (8) → Refrain final (8) → Outro (8) = 80 barres

## 4. Grille d'accords (proposition)

| Section | Grille (4 mesures) | Couleur / intention |
| :--- | :--- | :--- |
| **Couplet** | `| C | G | Am | F |` | Chanson populaire, refrain qui se retient. |
| **Refrain** | `| F | C | G | Am |` | Le refrain est une fête, presque un slogan de manif. |

## 5. Palette Live 12 Lite (proposition)

| Piste | Rôle | Instrument / Kit | Index |
| :--- | :--- | :--- | :--- |
| `1-Accordéon` | Mélodie | Drift (accordéon) | 0 |
| `2-Guitare` | Riff | Simpler (guitare électrique) | 1 |
| `3-Basse` | Fondation | Drift (basse) | 2 |
| `4-Batterie` | Rythme | Kit acoustique .adg | 3 |
| `5-Voix` | Chant | Audio | 4 |

> 8 pistes maximum (Live 12 Lite). Index **0-based** ; le nom porte l'index 1-based : `1-Batterie` = index 0.

## 6. Intention de mix

Accordéon et guitare se répondent ; voix franche, un peu ronde. Pas de reverb : une salle des fêtes sonne sec.

## 7. À vérifier avant d'enregistrer

- Les 60 000 postes : coût, calendrier, répartition police/gendarmerie/douanes.
- Le SMIC et la retraite à 60 ans : montants et financement.
- Le score de 2022 et le nombre de parrainages actuels.

## 8. Notes de production

Le titre cite *Le Temps des Cerises* : la mélodie doit être originale, seule la référence au titre est permise.

## 9. Session et steps de production

> La structure complète (§3) reste la cible lointaine. **À ce stade, on ne construit que trois scènes : Intro / Refrain / Outro.** Le tableau §5 décrit la couleur idéale ; l'implémentation réelle en 8 pistes mutualisées est ci-dessous. En cas de conflit, **c'est §9 qui fait foi**.

**Session** : C — Traditionnel / militaire / populaire
**Scènes réservées** : S10–S12 (Intro / Refrain / Outro) — scène S16 libre
**Tempo de scène** : 116 BPM · **Tonalité de travail** : Do majeur (C) · **Signature** : 4/4
**Chaînes à armer** : Harmonie = accordéon + guitare électrique · Mélodie = accordéon · Texture = chœur
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

1. **Créer les scènes.** Dans la session C, trois scènes consécutives : `S10 <Candidat> Intro`, `S11 <Candidat> Refrain`, `S12 <Candidat> Outro`. La scène S16 reste vide (réserve).
2. **Tempo et tonalité.** Régler le tempo de scène à 116 BPM (propriété de scène ; si l'outil ne l'expose pas, le faire à la main) et vérifier 4/4. La tonalité Do majeur (C) est un repère d'écriture, pas un réglage à automatiser.
3. **Armer les chaînes.** Harmonie = accordéon + guitare électrique, Mélodie = accordéon, Texture = chœur. Vérifier le **chain selector** de chaque rack sur la valeur du candidat : c'est ce qui permet 5 sons différents sur la même piste.
4. **Écrire l'harmonie du refrain.** 8 mesures, grille `| F | C | G | Am |`. Accords réels (vérifier les notes contre le nom), pas de renversement inutile. Vélocités 70–85, légères variations pour éviter le MIDI plat.
5. **Écrire basse et batterie.** Motif du style (Chanson française populaire, accordéon et guitare électrique), 8 mesures. Vélocités : kick 90–100, snare 85–95, hats 55–75. La basse suit la fondamentale, sans doubler la voix.
6. **Écrire le hook puis le guide vocal.** Mélodie du refrain sur `4-Mélodie`, 1 note par syllabe, tessiture **E3–B3 (64–71)**. Paroles : `PAROLES.md`. Guide chanté sur `7-Guide`, vélocités qui phrasent (75–110), pas une note plate.
7. **Intro (4–8 mesures).** Un ou deux éléments seulement : texture + basse, ou batterie + nappe. Ne pas jouer le refrain avant la scène Refrain.
8. **Outro / transition (4 mesures).** Accord tenu + transition Marseillaise : « Le jour de gloire est arrivé… pour les services publics ? ». Si l'outro est coupée, garder au moins 2 mesures de queue pour l'enchaînement.
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
