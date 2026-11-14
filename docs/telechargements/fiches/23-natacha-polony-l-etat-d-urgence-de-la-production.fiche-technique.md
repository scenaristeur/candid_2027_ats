# 23 — Natacha Polony — L'État d'urgence de la Production

**Statut** : préparation documentaire — aucune session Ableton ouverte pour ce morceau.
**Tempo** : 76 BPM *(proposition, à valider)*
**Tonalité** : La mineur (Am) *(proposition, à valider à l'oreille)*
**Signature** : 4/4
**Durée cible** : ≈ 2 min 35
**Atmosphère** : Tribune, gravité de femme de lettres
**Style** : Chanson réaliste, piano, voix grave, récitatif
**Voix** : baryton parlé-chanté de David, E3–B3 (MIDI 64–71, convention Ableton C3 = 60).

---

## 1. Le candidat — brief du 14/11/2026

| | |
| :--- | :--- |
| **Profil** | Journaliste et essayiste, ancienne directrice de *Marianne*, candidate annoncée en octobre 2026. |
| **Couleur politique** | Sans étiquette, souverainisme de production, critique des « offres qui fracturent ». |
| **Actions déjà menées** | Aucune action politique élective ; tribunes, direction de *Marianne*, campagne pour « rassembler les orphelins de la politique ». |
| **Programme 2027** | Augmentation des salaires de 20 à 30 % ; « état d'urgence de la production » ; priorité à la production française dans la commande publique ; suppression des aides aux entreprises non conditionnées à une production locale. |
| **Pour** | Voix hors partis ; parle de production et de souveraineté industrielle sans la radicalité du RN ou de LFI. |
| **Contre** | Absence d'expérience politique ; programme encore très général ; risque de ne pas réunir les 500 signatures, règle qu'elle juge elle-même « aberrante ». |
| **Actualité** | Candidature annoncée en octobre 2026. |
| **Transition Marseillaise** | « Marchons, marchons… vers la production française ! » |

> **Fiabilité** : contenu issu de `Candidats 2027.md` (compilation interne du 14/11/2026). Chaque chiffre, score et procédure doit être revérifié et **daté** avant l'enregistrement. L'album doit pouvoir dire sa date de vérité.

## 2. Ce que la chanson doit faire

- Traduire « production » en vies concrètes : usines, salaires, commande publique.
- Confronter le « hors partis » à l'épreuve des 500 signatures.
- Ne pas la ranger à droite ni à gauche : c'est justement son ambiguïté.

## 3. Structure (en barres)

Intro récitée (8) → Couplet 1 (16) → Refrain (8) → Couplet 2 (16) → Refrain (8) → Pont (8) → Refrain final (8) → Outro (4) = 76 barres

## 4. Grille d'accords (proposition)

| Section | Grille (4 mesures) | Couleur / intention |
| :--- | :--- | :--- |
| **Couplet** | `| Am | Dm | G | C |` | Chanson réaliste, presque un pamphlet chanté. |
| **Refrain** | `| F | C | G | Am |` | Le refrain est un mot d'ordre, pas une mélodie. |

## 5. Palette Live 12 Lite (proposition)

| Piste | Rôle | Instrument / Kit | Index |
| :--- | :--- | :--- | :--- |
| `1-Piano` | Harmonie | Drift (piano) | 0 |
| `2-Contrebasse` | Fondation | Drift (basse acoustique) | 1 |
| `3-Accordéon` | Couleur | Drift (accordéon) | 2 |
| `4-Percussions` | Rythme | Impulse | 3 |
| `5-Voix` | Chant | Audio | 4 |

> 8 pistes maximum (Live 12 Lite). Index **0-based** ; le nom porte l'index 1-based : `1-Batterie` = index 0.

## 6. Intention de mix

Voix nue, très proche ; piano discret. Aucune saturation : la colère passe par les mots, pas par le son.

## 7. À vérifier avant d'enregistrer

- Les 20 à 30 % d'augmentation des salaires : base de calcul, coût, calendrier.
- Le coût des aides publiques conditionnées.
- Son statut exact de candidature et l'état de ses parrainages.

## 8. Notes de production

Récitatif assumé : les couplets peuvent être parlés, le refrain chanté. Attention à ne pas tomber dans la chronique télévisée.

## 9. Session et steps de production

> La structure complète (§3) reste la cible lointaine. **À ce stade, on ne construit que trois scènes : Intro / Refrain / Outro.** Le tableau §5 décrit la couleur idéale ; l'implémentation réelle en 8 pistes mutualisées est ci-dessous. En cas de conflit, **c'est §9 qui fait foi**.

**Session** : D — Chanson / variété
**Scènes réservées** : S07–S09 (Intro / Refrain / Outro) — scène S16 libre
**Tempo de scène** : 76 BPM · **Tonalité de travail** : La mineur (Am) · **Signature** : 4/4
**Chaînes à armer** : Harmonie = piano · Mélodie = piano · Texture = contrebasse
**Kit de batterie de la session** : Kit acoustique léger / balais

| Piste | Index | Rôle | Instrument / chaîne |
| :--- | :--- | :--- | :--- |
| `1-Batterie` | 0 | Rythme | Kit acoustique léger / balais |
| `2-Basse` | 1 | Fondation | Drift — contrebasse + basse électrique |
| `3-Harmonie` | 2 | Accords | Instrument Rack — 5 chaînes piano/accordéon/cordes |
| `4-Mélodie` | 3 | Hook | Instrument Rack — 5 chaînes leads |
| `5-Texture` | 4 | Nappe | Instrument Rack — 2 chaînes : cordes, nappe |
| `6-Percs/FX` | 5 | Transitions | Percussions — balais, tambourin |
| `7-Guide` | 6 | Voix guide | Drift — voix douce |
| `8-Voix` | 7 | Chant final | Audio |

### Steps

1. **Créer les scènes.** Dans la session D, trois scènes consécutives : `S07 <Candidat> Intro`, `S08 <Candidat> Refrain`, `S09 <Candidat> Outro`. La scène S16 reste vide (réserve).
2. **Tempo et tonalité.** Régler le tempo de scène à 76 BPM (propriété de scène ; si l'outil ne l'expose pas, le faire à la main) et vérifier 4/4. La tonalité La mineur (Am) est un repère d'écriture, pas un réglage à automatiser.
3. **Armer les chaînes.** Harmonie = piano, Mélodie = piano, Texture = contrebasse. Vérifier le **chain selector** de chaque rack sur la valeur du candidat : c'est ce qui permet 5 sons différents sur la même piste.
4. **Écrire l'harmonie du refrain.** 8 mesures, grille `| F | C | G | Am |`. Accords réels (vérifier les notes contre le nom), pas de renversement inutile. Vélocités 70–85, légères variations pour éviter le MIDI plat.
5. **Écrire basse et batterie.** Motif du style (Chanson réaliste, piano, voix grave, récitatif), 8 mesures. Vélocités : kick 90–100, snare 85–95, hats 55–75. La basse suit la fondamentale, sans doubler la voix.
6. **Écrire le hook puis le guide vocal.** Mélodie du refrain sur `4-Mélodie`, 1 note par syllabe, tessiture **E3–B3 (64–71)**. Paroles : `PAROLES.md`. Guide chanté sur `7-Guide`, vélocités qui phrasent (75–110), pas une note plate.
7. **Intro (4–8 mesures).** Un ou deux éléments seulement : texture + basse, ou batterie + nappe. Ne pas jouer le refrain avant la scène Refrain.
8. **Outro / transition (4 mesures).** Accord tenu + transition Marseillaise : « Marchons, marchons… vers la production française ! ». Si l'outro est coupée, garder au moins 2 mesures de queue pour l'enchaînement.
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
