# 27 — Clara Egger — La Démocratie Directe

**Statut** : préparation documentaire — aucune session Ableton ouverte pour ce morceau.
**Tempo** : 84 BPM *(proposition, à valider)*
**Tonalité** : La mineur (Am) — bourdon *(proposition, à valider à l'oreille)*
**Signature** : 4/4
**Durée cible** : ≈ 1 min 55
**Atmosphère** : Performance, boucle, insistance
**Style** : Spoken word minimaliste, boucle rythmique
**Voix** : baryton parlé-chanté de David, E3–B3 (MIDI 64–71, convention Ableton C3 = 60).

---

## 1. Le candidat — brief du 14/11/2026

| | |
| :--- | :--- |
| **Profil** | Professeure de sciences politiques, candidate de « Solution démocratique ». |
| **Couleur politique** | Démocratie directe, transpartisane. |
| **Actions déjà menées** | A créé son mouvement en 2024 ; campagne transpartisane pour « changer les règles du jeu politique ». |
| **Programme 2027** | Une seule mesure : réviser l'article 89 de la Constitution pour permettre à 700 000 citoyens de proposer une révision constitutionnelle, soumise ensuite au référendum. |
| **Pour** | Redonner le pouvoir aux citoyens ; fatigue de la classe politique. |
| **Contre** | Une seule mesure, sans programme économique ou social ; risque de paralysie institutionnelle. |
| **Actualité** | Sa campagne porte un seul mot : référendum. |
| **Transition Marseillaise** | « Aux armes, citoyens… votez directement ! » |

> **Fiabilité** : contenu issu de `Candidats 2027.md` (compilation interne du 14/11/2026). Chaque chiffre, score et procédure doit être revérifié et **daté** avant l'enregistrement. L'album doit pouvoir dire sa date de vérité.

## 2. Ce que la chanson doit faire

- Expliquer l'article 89 et les 700 000 citoyens sans jargon.
- Dire ce qu'une seule mesure ne règle pas.
- Faire de la répétition une forme politique, pas un défaut.

## 3. Structure (en barres)

Intro boucle (8) → Couplet 1 (16) → Refrain (8) → Couplet 2 (16) → Refrain (8) → Pont (8) → Refrain final (8) → Outro (4) = 76 barres

## 4. Grille d'accords (proposition)

| Section | Grille (4 mesures) | Couleur / intention |
| :--- | :--- | :--- |
| **Couplet** | `| Am | Am | Am | Am |` | Bourdon volontaire : une seule couleur. |
| **Refrain** | `| F | G | Am | Am |` | Le refrain est une boucle parlée, presque hypnotique. |

## 5. Palette Live 12 Lite (proposition)

| Piste | Rôle | Instrument / Kit | Index |
| :--- | :--- | :--- | :--- |
| `1-Boucle` | Rythme | Drum Rack (minimal) | 0 |
| `2-Bourdon` | Fondation | Drift (drone) | 1 |
| `3-Voix` | Chant | Audio | 2 |
| `4-Doublage` | Texture | Audio (voix doublée) | 3 |

> 8 pistes maximum (Live 12 Lite). Index **0-based** ; le nom porte l'index 1-based : `1-Batterie` = index 0.

## 6. Intention de mix

Voix sèche, boucle très discrète. Le silence entre les phrases fait partie du morceau.

## 7. À vérifier avant d'enregistrer

- Le seuil exact de 700 000 citoyens et le mécanisme proposé.
- La rédaction actuelle de l'article 89.
- Le statut juridique de sa candidature et ses parrainages.

## 8. Notes de production

Morceau le plus court de l'album, avec celui de Philippot. Presque pas de mélodie : la voix porte le rythme.

## 9. Session et steps de production

> La structure complète (§3) reste la cible lointaine. **À ce stade, on ne construit que trois scènes : Intro / Refrain / Outro.** Le tableau §5 décrit la couleur idéale ; l'implémentation réelle en 8 pistes mutualisées est ci-dessous. En cas de conflit, **c'est §9 qui fait foi**.

**Session** : E — Jazz / classique / chambre
**Scènes réservées** : S10–S12 (Intro / Refrain / Outro) — scène S16 libre
**Tempo de scène** : 84 BPM · **Tonalité de travail** : La mineur (Am) — bourdon · **Signature** : 4/4
**Chaînes à armer** : Harmonie = bourdon · Mélodie = voix parlée · Texture = boucle
**Kit de batterie de la session** : Kit jazz / balais

| Piste | Index | Rôle | Instrument / chaîne |
| :--- | :--- | :--- | :--- |
| `1-Batterie` | 0 | Rythme | Kit jazz / percussions |
| `2-Basse` | 1 | Fondation | Drift — contrebasse |
| `3-Harmonie` | 2 | Accords | Instrument Rack — 5 chaînes piano/cello/cordes |
| `4-Mélodie` | 3 | Hook | Instrument Rack — 5 chaînes piano/cello |
| `5-Texture` | 4 | Bourdon / souffle | Instrument Rack — 2 chaînes : bourdon, souffle |
| `6-Percs/FX` | 5 | Transitions | Percussions — balais |
| `7-Guide` | 6 | Voix guide | Drift — voix douce |
| `8-Voix` | 7 | Chant final | Audio |

### Steps

1. **Créer les scènes.** Dans la session E, trois scènes consécutives : `S10 <Candidat> Intro`, `S11 <Candidat> Refrain`, `S12 <Candidat> Outro`. La scène S16 reste vide (réserve).
2. **Tempo et tonalité.** Régler le tempo de scène à 84 BPM (propriété de scène ; si l'outil ne l'expose pas, le faire à la main) et vérifier 4/4. La tonalité La mineur (Am) — bourdon est un repère d'écriture, pas un réglage à automatiser.
3. **Armer les chaînes.** Harmonie = bourdon, Mélodie = voix parlée, Texture = boucle. Vérifier le **chain selector** de chaque rack sur la valeur du candidat : c'est ce qui permet 5 sons différents sur la même piste.
4. **Écrire l'harmonie du refrain.** 8 mesures, grille `| F | G | Am | Am |`. Accords réels (vérifier les notes contre le nom), pas de renversement inutile. Vélocités 70–85, légères variations pour éviter le MIDI plat.
5. **Écrire basse et batterie.** Motif du style (Spoken word minimaliste, boucle rythmique), 8 mesures. Vélocités : kick 90–100, snare 85–95, hats 55–75. La basse suit la fondamentale, sans doubler la voix.
6. **Écrire le hook puis le guide vocal.** Mélodie du refrain sur `4-Mélodie`, 1 note par syllabe, tessiture **E3–B3 (64–71)**. Paroles : `PAROLES.md`. Guide chanté sur `7-Guide`, vélocités qui phrasent (75–110), pas une note plate.
7. **Intro (4–8 mesures).** Un ou deux éléments seulement : texture + basse, ou batterie + nappe. Ne pas jouer le refrain avant la scène Refrain.
8. **Outro / transition (4 mesures).** Accord tenu + transition Marseillaise : « Aux armes, citoyens… votez directement ! ». Si l'outro est coupée, garder au moins 2 mesures de queue pour l'enchaînement.
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
