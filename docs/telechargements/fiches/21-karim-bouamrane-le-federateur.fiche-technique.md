# 21 — Karim Bouamrane — Le Fédérateur

**Statut** : préparation documentaire — aucune session Ableton ouverte pour ce morceau.
**Tempo** : 104 BPM *(proposition, à valider)*
**Tonalité** : Do dièse mineur (C#m) *(proposition, à valider à l'oreille)*
**Signature** : 4/4
**Durée cible** : ≈ 2 min 20
**Atmosphère** : Quartier, travail, énergie collective
**Style** : Pop urbaine, touche de raï, refrain fédérateur
**Voix** : baryton parlé-chanté de David, E3–B3 (MIDI 64–71, convention Ableton C3 = 60).

---

## 1. Le candidat — brief du 14/11/2026

| | |
| :--- | :--- |
| **Profil** | Maire PS de Saint-Ouen-sur-Seine, candidat à la présidentielle depuis juin 2026. |
| **Couleur politique** | Gauche sociale-démocrate, « ancrée dans le réel ». |
| **Actions déjà menées** | Gestion de sa ville ; offensive contre les « barons socialistes » qui le « méprisent ». |
| **Programme 2027** | Pas encore de programme complet : sécurité, école, travail, « reconnaissance des territoires populaires ». |
| **Pour** | Gauche capable de parler aux classes populaires sans la radicalité de LFI. |
| **Contre** | Notoriété nationale faible ; candidature qui fragmente encore la gauche sociale-démocrate. |
| **Actualité** | Sa candidature divise le PS et la gauche modérée. |
| **Transition Marseillaise** | « Formez vos bataillons… dans les quartiers ! » |

> **Fiabilité** : contenu issu de `Candidats 2027.md` (compilation interne du 14/11/2026). Chaque chiffre, score et procédure doit être revérifié et **daté** avant l'enregistrement. L'album doit pouvoir dire sa date de vérité.

## 2. Ce que la chanson doit faire

- Parler de la banlieue sans misérabilisme ni folklore.
- Demander un programme, pas seulement une posture de rassemblement.
- Situer sa candidature dans la guerre interne du PS.

## 3. Structure (en barres)

Intro (4) → Couplet 1 (12) → Refrain (8) → Couplet 2 (12) → Refrain (8) → Pont (8) → Refrain final (8) → Outro (4) = 64 barres

## 4. Grille d'accords (proposition)

| Section | Grille (4 mesures) | Couleur / intention |
| :--- | :--- | :--- |
| **Couplet** | `| C#m | A | E | B |` | Pop urbaine, basse ronde. |
| **Refrain** | `| A | E | B | C#m |` | Le refrain rassemble, presque un chant de quartier. |

## 5. Palette Live 12 Lite (proposition)

| Piste | Rôle | Instrument / Kit | Index |
| :--- | :--- | :--- | :--- |
| `1-Batterie` | Rythme | Drum Rack (urbain) | 0 |
| `2-Basse` | Fondation | Drift (basse) | 1 |
| `3-Claviers` | Harmonie | Drift (piano électrique) | 2 |
| `4-Oud` | Couleur | Simpler (oud) | 3 |
| `5-Voix` | Chant | Audio | 4 |

> 8 pistes maximum (Live 12 Lite). Index **0-based** ; le nom porte l'index 1-based : `1-Batterie` = index 0.

## 6. Intention de mix

Basse ronde et voix devant ; oud discret en réponse. Reverb courte, comme une cage d'escalier.

## 7. À vérifier avant d'enregistrer

- Son programme au 14/11/2026 (probablement incomplet).
- Les accusations contre les « barons » : citer des faits, pas des rumeurs.
- Son score dans les sondages nationaux.

## 8. Notes de production

Le oud doit être joué ou échantillonné légalement. Le refrain peut être repris par un chœur de voix d'enfants, une seule fois.

## 9. Session et steps de production

> La structure complète (§3) reste la cible lointaine. **À ce stade, on ne construit que trois scènes : Intro / Refrain / Outro.** Le tableau §5 décrit la couleur idéale ; l'implémentation réelle en 8 pistes mutualisées est ci-dessous. En cas de conflit, **c'est §9 qui fait foi**.

**Session** : B — Pop / électro / urbain
**Scènes réservées** : S10–S12 (Intro / Refrain / Outro) — scène S16 libre
**Tempo de scène** : 104 BPM · **Tonalité de travail** : Do dièse mineur (C#m) · **Signature** : 4/4
**Chaînes à armer** : Harmonie = piano électrique + oud · Mélodie = pluck · Texture = nappe urbaine
**Kit de batterie de la session** : Kit pop-électro (.adg)

| Piste | Index | Rôle | Instrument / chaîne |
| :--- | :--- | :--- | :--- |
| `1-Batterie` | 0 | Rythme | Drum Rack — kit pop/électro |
| `2-Basse` | 1 | Fondation | Drift — sub + drive (2 chaînes) |
| `3-Harmonie` | 2 | Accords | Instrument Rack — 5 chaînes pads/plucks/piano/oud |
| `4-Mélodie` | 3 | Hook | Instrument Rack — 5 chaînes leads |
| `5-Texture` | 4 | Nappe / riser | Instrument Rack — 2 chaînes : nappe, riser |
| `6-Percs/FX` | 5 | Transitions | Drum Rack — claps, shaker, tambour |
| `7-Guide` | 6 | Voix guide | Drift — voix douce |
| `8-Voix` | 7 | Chant final | Audio |

### Steps

1. **Créer les scènes.** Dans la session B, trois scènes consécutives : `S10 <Candidat> Intro`, `S11 <Candidat> Refrain`, `S12 <Candidat> Outro`. La scène S16 reste vide (réserve).
2. **Tempo et tonalité.** Régler le tempo de scène à 104 BPM (propriété de scène ; si l'outil ne l'expose pas, le faire à la main) et vérifier 4/4. La tonalité Do dièse mineur (C#m) est un repère d'écriture, pas un réglage à automatiser.
3. **Armer les chaînes.** Harmonie = piano électrique + oud, Mélodie = pluck, Texture = nappe urbaine. Vérifier le **chain selector** de chaque rack sur la valeur du candidat : c'est ce qui permet 5 sons différents sur la même piste.
4. **Écrire l'harmonie du refrain.** 8 mesures, grille `| A | E | B | C#m |`. Accords réels (vérifier les notes contre le nom), pas de renversement inutile. Vélocités 70–85, légères variations pour éviter le MIDI plat.
5. **Écrire basse et batterie.** Motif du style (Pop urbaine, touche de raï, refrain fédérateur), 8 mesures. Vélocités : kick 90–100, snare 85–95, hats 55–75. La basse suit la fondamentale, sans doubler la voix.
6. **Écrire le hook puis le guide vocal.** Mélodie du refrain sur `4-Mélodie`, 1 note par syllabe, tessiture **E3–B3 (64–71)**. Paroles : `PAROLES.md`. Guide chanté sur `7-Guide`, vélocités qui phrasent (75–110), pas une note plate.
7. **Intro (4–8 mesures).** Un ou deux éléments seulement : texture + basse, ou batterie + nappe. Ne pas jouer le refrain avant la scène Refrain.
8. **Outro / transition (4 mesures).** Accord tenu + transition Marseillaise : « Formez vos bataillons… dans les quartiers ! ». Si l'outro est coupée, garder au moins 2 mesures de queue pour l'enchaînement.
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
