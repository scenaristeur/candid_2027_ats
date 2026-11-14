# 08 — Selma Labib — Le Bus de la Révolution

**Statut** : préparation documentaire — aucune session Ableton ouverte pour ce morceau.
**Tempo** : 168 BPM *(proposition, à valider)*
**Tonalité** : Mi mineur (Em) *(proposition, à valider à l'oreille)*
**Signature** : 4/4
**Durée cible** : ≈ 2 min
**Atmosphère** : Dépôt de bus, colère jeune, énergie de manif
**Style** : Punk ouvrier, paroles scandées, bruit de moteur
**Voix** : baryton parlé-chanté de David, E3–B3 (MIDI 64–71, convention Ableton C3 = 60).

---

## 1. Le candidat — brief du 14/11/2026

| | |
| :--- | :--- |
| **Profil** | Conductrice de bus en région parisienne, 30 ans, porte-parole du NPA-Révolutionnaires. |
| **Couleur politique** | Anticapitalisme radical, féminisme ouvrier. |
| **Actions déjà menées** | Tête de liste aux européennes de 2024 (0,15 %) ; aux municipales de 2026 à Ivry-sur-Seine. |
| **Programme 2027** | Interdiction de tous les licenciements ; ouverture des frontières ; expropriation des grandes entreprises ; partage du temps de travail. |
| **Pour** | Voix ouvrière, jeune et radicale, qui parle des conditions de travail réelles. |
| **Contre** | Candidature très minoritaire, sans programme économique chiffré ; risque de ne pas obtenir les parrainages. |
| **Actualité** | Le NPA-Révolutionnaires cherche une voix dans une gauche dominée par LFI. |
| **Transition Marseillaise** | « Qu'un sang impur… abreuve nos bus ! » |

> **Fiabilité** : contenu issu de `Candidats 2027.md` (compilation interne du 14/11/2026). Chaque chiffre, score et procédure doit être revérifié et **daté** avant l'enregistrement. L'album doit pouvoir dire sa date de vérité.

## 2. Ce que la chanson doit faire

- Partir du travail réel : horaires, agressions, salaire, fatigue.
- Confronter le programme radical à l'épreuve des urnes et des parrainages.
- Ne pas faire de la jeunesse un argument, mais une expérience.

## 3. Structure (en barres)

Intro moteur (4) → Couplet 1 (12) → Refrain (8) → Couplet 2 (12) → Refrain (8) → Pont (8) → Refrain final (8) → Outro (4) = 64 barres

## 4. Grille d'accords (proposition)

| Section | Grille (4 mesures) | Couleur / intention |
| :--- | :--- | :--- |
| **Couplet** | `| Em | C | G | D |` | Punk rapide, trois accords. |
| **Refrain** | `| C | D | Em | Em |` | Le refrain scande, sans mélodie. |

## 5. Palette Live 12 Lite (proposition)

| Piste | Rôle | Instrument / Kit | Index |
| :--- | :--- | :--- | :--- |
| `1-Batterie` | Rythme | Kit punk .adg | 0 |
| `2-Guitare` | Riff | Simpler (guitare saturée) | 1 |
| `3-Basse` | Fondation | Drift (basse drive) | 2 |
| `4-Moteur` | Texture | Simpler (moteur de bus) | 3 |
| `5-Voix` | Chant | Audio + Saturator | 4 |

> 8 pistes maximum (Live 12 Lite). Index **0-based** ; le nom porte l'index 1-based : `1-Batterie` = index 0.

## 6. Intention de mix

Tout devant, voix saturée mais compréhensible. Le moteur de bus ouvre et ferme le morceau.

## 7. À vérifier avant d'enregistrer

- Les scores de 2024 et 2026 : chiffres exacts.
- Le programme du NPA-Révolutionnaires : ce qui est chiffré.
- L'état des parrainages au 14/11/2026.

## 8. Notes de production

Le bruit de moteur doit être enregistré ou synthétisé, pas emprunté à un film.

## 9. Session et steps de production

> La structure complète (§3) reste la cible lointaine. **À ce stade, on ne construit que trois scènes : Intro / Refrain / Outro.** Le tableau §5 décrit la couleur idéale ; l'implémentation réelle en 8 pistes mutualisées est ci-dessous. En cas de conflit, **c'est §9 qui fait foi**.

**Session** : A — Rock / punk
**Scènes réservées** : S04–S06 (Intro / Refrain / Outro) — scène S16 libre
**Tempo de scène** : 168 BPM · **Tonalité de travail** : Mi mineur (Em) · **Signature** : 4/4
**Chaînes à armer** : Harmonie = guitare punk · Mélodie = lead guitare · Texture = moteur de bus (Simpler)
**Kit de batterie de la session** : Kit rock-punk (.adg à choisir dans le browser)

| Piste | Index | Rôle | Instrument / chaîne |
| :--- | :--- | :--- | :--- |
| `1-Batterie` | 0 | Rythme | Drum Rack — kit rock/punk |
| `2-Basse` | 1 | Fondation | Drift — basse drive (2 chaînes : ronde / saturée) |
| `3-Harmonie` | 2 | Accords | Instrument Rack — 5 chaînes guitare/orgue |
| `4-Mélodie` | 3 | Hook | Instrument Rack — 5 chaînes leads |
| `5-Texture` | 4 | Nappe / bruit | Instrument Rack — 2 chaînes : orgue, bruit blanc |
| `6-Percs/FX` | 5 | Transitions | Drum Rack / Simpler — tambourin, crash, noise |
| `7-Guide` | 6 | Voix guide | Drift — voix douce |
| `8-Voix` | 7 | Chant final | Audio |

### Steps

1. **Créer les scènes.** Dans la session A, trois scènes consécutives : `S04 <Candidat> Intro`, `S05 <Candidat> Refrain`, `S06 <Candidat> Outro`. La scène S16 reste vide (réserve).
2. **Tempo et tonalité.** Régler le tempo de scène à 168 BPM (propriété de scène ; si l'outil ne l'expose pas, le faire à la main) et vérifier 4/4. La tonalité Mi mineur (Em) est un repère d'écriture, pas un réglage à automatiser.
3. **Armer les chaînes.** Harmonie = guitare punk, Mélodie = lead guitare, Texture = moteur de bus (Simpler). Vérifier le **chain selector** de chaque rack sur la valeur du candidat : c'est ce qui permet 5 sons différents sur la même piste.
4. **Écrire l'harmonie du refrain.** 8 mesures, grille `| C | D | Em | Em |`. Accords réels (vérifier les notes contre le nom), pas de renversement inutile. Vélocités 70–85, légères variations pour éviter le MIDI plat.
5. **Écrire basse et batterie.** Motif du style (Punk ouvrier, paroles scandées, bruit de moteur), 8 mesures. Vélocités : kick 90–100, snare 85–95, hats 55–75. La basse suit la fondamentale, sans doubler la voix.
6. **Écrire le hook puis le guide vocal.** Mélodie du refrain sur `4-Mélodie`, 1 note par syllabe, tessiture **E3–B3 (64–71)**. Paroles : `PAROLES.md`. Guide chanté sur `7-Guide`, vélocités qui phrasent (75–110), pas une note plate.
7. **Intro (4–8 mesures).** Un ou deux éléments seulement : texture + basse, ou batterie + nappe. Ne pas jouer le refrain avant la scène Refrain.
8. **Outro / transition (4 mesures).** Accord tenu + transition Marseillaise : « Qu'un sang impur… abreuve nos usines ! ». Si l'outro est coupée, garder au moins 2 mesures de queue pour l'enchaînement.
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
