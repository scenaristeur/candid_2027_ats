# 24 — François Hollande — Le Revenant Social-démocrate

**Statut** : préparation documentaire — aucune session Ableton ouverte pour ce morceau.
**Tempo** : 100 BPM *(proposition, à valider)*
**Tonalité** : Do dièse mineur (C#m) *(proposition, à valider à l'oreille)*
**Signature** : 4/4
**Durée cible** : ≈ 2 min 35
**Atmosphère** : Retour vers le futur, nostalgie et embarras
**Style** : Variété rétro années 80–90, piano désabusé
**Voix** : baryton parlé-chanté de David, E3–B3 (MIDI 64–71, convention Ableton C3 = 60).

---

## 1. Le candidat — brief du 14/11/2026

| | |
| :--- | :--- |
| **Profil** | Ancien président de la République (2012–2017), député de Corrèze. N'est pas officiellement candidat. |
| **Couleur politique** | Social-démocratie, recours de la gauche modérée. |
| **Actions déjà menées** | A gouverné cinq ans, renoncé à se représenter en 2017 ; loue des locaux, publie un livre de 80 propositions et se pose en « recours ». |
| **Programme 2027** | 80 propositions encore peu détaillées : éducation, santé, « modernisation des institutions ». |
| **Pour** | Figure expérimentée, capable de rassembler la gauche modérée face à Mélenchon et Glucksmann. |
| **Contre** | Bilan contesté au sein même de la gauche ; retour perçu comme une difficulté du personnel politique à se renouveler. |
| **Actualité** | Il n'est pas candidat déclaré, mais tout le monde parle de son retour. |
| **Transition Marseillaise** | « Allons enfants… de la patrie reconnaissante ? » |

> **Fiabilité** : contenu issu de `Candidats 2027.md` (compilation interne du 14/11/2026). Chaque chiffre, score et procédure doit être revérifié et **daté** avant l'enregistrement. L'album doit pouvoir dire sa date de vérité.

## 2. Ce que la chanson doit faire

- Faire le bilan sans le procès : ce qui a marché, ce qui a laissé des traces.
- Poser la question du retour : recours ou refus de passer la main ?
- Ne pas transformer la chanson en règlement de comptes.

## 3. Structure (en barres)

Intro (8) → Couplet 1 (16) → Refrain (8) → Couplet 2 (16) → Refrain (8) → Pont (8) → Refrain final (8) → Outro (8) = 80 barres

## 4. Grille d'accords (proposition)

| Section | Grille (4 mesures) | Couleur / intention |
| :--- | :--- | :--- |
| **Couplet** | `| C#m | A | E | B |` | Variété rétro, presque une cassette. |
| **Refrain** | `| A | E | B | C#m |` | Le refrain a un goût de déjà-vu. |

## 5. Palette Live 12 Lite (proposition)

| Piste | Rôle | Instrument / Kit | Index |
| :--- | :--- | :--- | :--- |
| `1-Claviers` | Harmonie | Drift (piano électrique) | 0 |
| `2-Basse` | Fondation | Drift (basse) | 1 |
| `3-Batterie` | Rythme | Kit 80s .adg | 2 |
| `4-Nappe` | Texture | Drift (pad) + Chorus | 3 |
| `5-Voix` | Chant | Audio + Reverb courte | 4 |

> 8 pistes maximum (Live 12 Lite). Index **0-based** ; le nom porte l'index 1-based : `1-Batterie` = index 0.

## 6. Intention de mix

Reverb de snare années 80 assumée ; voix un peu en avant pour l'intelligibilité. Le kitsch doit être un choix, pas un accident.

## 7. À vérifier avant d'enregistrer

- Son statut exact : candidat ou non.
- Les 80 propositions : combien sont chiffrées.
- Les éléments de bilan cités (mariage pour tous, loi travail, etc.) : exactitude et dates.

## 8. Notes de production

Le titre est un clin d'œil au film *Les Revenants* : garder le ton fantomatique, pas méchant.

## 9. Session et steps de production

> La structure complète (§3) reste la cible lointaine. **À ce stade, on ne construit que trois scènes : Intro / Refrain / Outro.** Le tableau §5 décrit la couleur idéale ; l'implémentation réelle en 8 pistes mutualisées est ci-dessous. En cas de conflit, **c'est §9 qui fait foi**.

**Session** : D — Chanson / variété
**Scènes réservées** : S10–S12 (Intro / Refrain / Outro) — scène S16 libre
**Tempo de scène** : 100 BPM · **Tonalité de travail** : Do dièse mineur (C#m) · **Signature** : 4/4
**Chaînes à armer** : Harmonie = piano électrique · Mélodie = pad 80s · Texture = nappe chorus
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

1. **Créer les scènes.** Dans la session D, trois scènes consécutives : `S10 <Candidat> Intro`, `S11 <Candidat> Refrain`, `S12 <Candidat> Outro`. La scène S16 reste vide (réserve).
2. **Tempo et tonalité.** Régler le tempo de scène à 100 BPM (propriété de scène ; si l'outil ne l'expose pas, le faire à la main) et vérifier 4/4. La tonalité Do dièse mineur (C#m) est un repère d'écriture, pas un réglage à automatiser.
3. **Armer les chaînes.** Harmonie = piano électrique, Mélodie = pad 80s, Texture = nappe chorus. Vérifier le **chain selector** de chaque rack sur la valeur du candidat : c'est ce qui permet 5 sons différents sur la même piste.
4. **Écrire l'harmonie du refrain.** 8 mesures, grille `| A | E | B | C#m |`. Accords réels (vérifier les notes contre le nom), pas de renversement inutile. Vélocités 70–85, légères variations pour éviter le MIDI plat.
5. **Écrire basse et batterie.** Motif du style (Variété rétro années 80–90, piano désabusé), 8 mesures. Vélocités : kick 90–100, snare 85–95, hats 55–75. La basse suit la fondamentale, sans doubler la voix.
6. **Écrire le hook puis le guide vocal.** Mélodie du refrain sur `4-Mélodie`, 1 note par syllabe, tessiture **E3–B3 (64–71)**. Paroles : `PAROLES.md`. Guide chanté sur `7-Guide`, vélocités qui phrasent (75–110), pas une note plate.
7. **Intro (4–8 mesures).** Un ou deux éléments seulement : texture + basse, ou batterie + nappe. Ne pas jouer le refrain avant la scène Refrain.
8. **Outro / transition (4 mesures).** Accord tenu + transition Marseillaise : « Allons enfants… de la patrie reconnaissante ? ». Si l'outro est coupée, garder au moins 2 mesures de queue pour l'enchaînement.
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
