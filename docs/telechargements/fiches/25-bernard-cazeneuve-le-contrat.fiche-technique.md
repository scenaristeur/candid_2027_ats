# 25 — Bernard Cazeneuve — Le Contrat

**Statut** : préparation documentaire — aucune session Ableton ouverte pour ce morceau.
**Tempo** : 70 BPM *(proposition, à valider)*
**Tonalité** : La mineur (Am) *(proposition, à valider à l'oreille)*
**Signature** : 4/4
**Durée cible** : ≈ 2 min 45
**Atmosphère** : Notarial, grave, un peu austère
**Style** : Musique de chambre, piano et violoncelle
**Voix** : baryton parlé-chanté de David, E3–B3 (MIDI 64–71, convention Ableton C3 = 60).

---

## 1. Le candidat — brief du 14/11/2026

| | |
| :--- | :--- |
| **Profil** | Ancien Premier ministre socialiste (2016–2017), ancien ministre de l'Intérieur. |
| **Couleur politique** | Gauche de gouvernement, fermeté républicaine. |
| **Actions déjà menées** | Ministre de l'Intérieur pendant les attentats de 2015–2016, Premier ministre ; a refusé de participer à la primaire socialiste et publie un « contrat » avec les Français. |
| **Programme 2027** | Trois chantiers : éducation et santé ; modernisation des institutions ; sécurité. Pas de détail chiffré pour l'instant. |
| **Pour** | Gauche de gouvernement, sérieuse et républicaine, sans compromis avec LFI. |
| **Contre** | Positionnement perçu comme une difficulté à se renouveler ; divise la gauche modérée avec Glucksmann et Faure. |
| **Actualité** | Son « contrat » est une lettre aux Français, pas encore un programme chiffré. |
| **Transition Marseillaise** | « Tremblez, tyrans… et électeurs ! » |

> **Fiabilité** : contenu issu de `Candidats 2027.md` (compilation interne du 14/11/2026). Chaque chiffre, score et procédure doit être revérifié et **daté** avant l'enregistrement. L'album doit pouvoir dire sa date de vérité.

## 2. Ce que la chanson doit faire

- Lire le « contrat » comme un acte politique : que signe-t-on exactement ?
- Rappeler l'expérience de l'Intérieur sans en faire un argument d'autorité.
- Montrer la fragmentation de la gauche modérée.

## 3. Structure (en barres)

Intro piano (8) → Couplet 1 (16) → Refrain (8) → Couplet 2 (16) → Refrain (8) → Pont (8) → Refrain final (8) → Outro (8) = 80 barres

## 4. Grille d'accords (proposition)

| Section | Grille (4 mesures) | Couleur / intention |
| :--- | :--- | :--- |
| **Couplet** | `| Am | F | C | G |` | Chambre, respiration lente. |
| **Refrain** | `| F | C | G | Am |` | Le refrain reste grave, sans éclat. |

## 5. Palette Live 12 Lite (proposition)

| Piste | Rôle | Instrument / Kit | Index |
| :--- | :--- | :--- | :--- |
| `1-Piano` | Harmonie | Drift (piano) | 0 |
| `2-Violoncelle` | Mélodie | Drift (cello) | 1 |
| `3-Contrebasse` | Fondation | Drift (basse acoustique) | 2 |
| `4-Voix` | Chant | Audio | 3 |
| `5-Souffle` | Texture | Simpler (souffle) | 4 |

> 8 pistes maximum (Live 12 Lite). Index **0-based** ; le nom porte l'index 1-based : `1-Batterie` = index 0.

## 6. Intention de mix

Très peu de compression, beaucoup de dynamique. Voix nue au couplet ; violoncelle qui répond, jamais qui double.

## 7. À vérifier avant d'enregistrer

- Le contenu exact des trois chantiers.
- Sa position sur la primaire socialiste et le nombre de parrainages.
- Les attentats de 2015–2016 : ne citer que des faits établis.

## 8. Notes de production

Le morceau doit finir sur une question, pas sur une conclusion : c'est un contrat non signé.

## 9. Session et steps de production

> La structure complète (§3) reste la cible lointaine. **À ce stade, on ne construit que trois scènes : Intro / Refrain / Outro.** Le tableau §5 décrit la couleur idéale ; l'implémentation réelle en 8 pistes mutualisées est ci-dessous. En cas de conflit, **c'est §9 qui fait foi**.

**Session** : E — Jazz / classique / chambre
**Scènes réservées** : S07–S09 (Intro / Refrain / Outro) — scène S16 libre
**Tempo de scène** : 70 BPM · **Tonalité de travail** : La mineur (Am) · **Signature** : 4/4
**Chaînes à armer** : Harmonie = piano · Mélodie = violoncelle · Texture = souffle
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

1. **Créer les scènes.** Dans la session E, trois scènes consécutives : `S07 <Candidat> Intro`, `S08 <Candidat> Refrain`, `S09 <Candidat> Outro`. La scène S16 reste vide (réserve).
2. **Tempo et tonalité.** Régler le tempo de scène à 70 BPM (propriété de scène ; si l'outil ne l'expose pas, le faire à la main) et vérifier 4/4. La tonalité La mineur (Am) est un repère d'écriture, pas un réglage à automatiser.
3. **Armer les chaînes.** Harmonie = piano, Mélodie = violoncelle, Texture = souffle. Vérifier le **chain selector** de chaque rack sur la valeur du candidat : c'est ce qui permet 5 sons différents sur la même piste.
4. **Écrire l'harmonie du refrain.** 8 mesures, grille `| F | C | G | Am |`. Accords réels (vérifier les notes contre le nom), pas de renversement inutile. Vélocités 70–85, légères variations pour éviter le MIDI plat.
5. **Écrire basse et batterie.** Motif du style (Musique de chambre, piano et violoncelle), 8 mesures. Vélocités : kick 90–100, snare 85–95, hats 55–75. La basse suit la fondamentale, sans doubler la voix.
6. **Écrire le hook puis le guide vocal.** Mélodie du refrain sur `4-Mélodie`, 1 note par syllabe, tessiture **E3–B3 (64–71)**. Paroles : `PAROLES.md`. Guide chanté sur `7-Guide`, vélocités qui phrasent (75–110), pas une note plate.
7. **Intro (4–8 mesures).** Un ou deux éléments seulement : texture + basse, ou batterie + nappe. Ne pas jouer le refrain avant la scène Refrain.
8. **Outro / transition (4 mesures).** Accord tenu + transition Marseillaise : « Tremblez, tyrans… et électeurs ! ». Si l'outro est coupée, garder au moins 2 mesures de queue pour l'enchaînement.
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
