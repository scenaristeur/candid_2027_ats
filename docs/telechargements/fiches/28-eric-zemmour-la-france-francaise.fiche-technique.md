# 28 — Éric Zemmour — La France Française

**Statut** : préparation documentaire — aucune session Ableton ouverte pour ce morceau.
**Tempo** : 72 BPM *(proposition, à valider)*
**Tonalité** : Ré mineur (Dm) *(proposition, à valider à l'oreille)*
**Signature** : 4/4
**Durée cible** : ≈ 2 min 40
**Atmosphère** : Déclinisme solennel, presque funèbre
**Style** : Classique sombre, cordes graves, piano, sample de Beethoven
**Voix** : baryton parlé-chanté de David, E3–B3 (MIDI 64–71, convention Ableton C3 = 60).

---

## 1. Le candidat — brief du 14/11/2026

| | |
| :--- | :--- |
| **Profil** | Président de Reconquête, polémiste devenu politique, condamné en 2024 pour provocation à la haine. |
| **Couleur politique** | Extrême droite identitaire, nationaliste. |
| **Actions déjà menées** | Candidature en 2022 (7,07 %), structuration de Reconquête, offensive contre l'immigration et l'islam politique. |
| **Programme 2027** | Expulsion de 2 millions d'immigrés, réduction drastique de l'immigration légale, baisse d'impôts estimée à 280 milliards d'euros. |
| **Pour** | Rupture identitaire radicale revendiquée ; électorat qui veut une immigration zéro. |
| **Contre** | Faisabilité juridique et humaine des expulsions massives ; condamnation judiciaire ; marginalisation face au RN, qui capte l'essentiel de l'électorat identitaire. |
| **Actualité** | Crédité d'environ 4 % ; la concurrence du RN limite sa portée. |
| **Transition Marseillaise** | « Allons enfants… la France, la vraie ? » |

> **Fiabilité** : contenu issu de `Candidats 2027.md` (compilation interne du 14/11/2026). Chaque chiffre, score et procédure doit être revérifié et **daté** avant l'enregistrement. L'album doit pouvoir dire sa date de vérité.

## 2. Ce que la chanson doit faire

- Dire la thèse décliniste et son programme, sans lui donner plus de place qu'il n'en a dans les urnes.
- Nommer la condamnation de 2024 factuellement, sans en faire le sujet de la chanson.
- Montrer que la concurrence RN est la vraie limite de cette candidature.

## 3. Structure (en barres)

Intro (8) → Couplet 1 (16) → Refrain (8) → Couplet 2 (16) → Refrain (8) → Pont (12) → Refrain final (8) → Outro (8) = 84 barres

## 4. Grille d'accords (proposition)

| Section | Grille (4 mesures) | Couleur / intention |
| :--- | :--- | :--- |
| **Couplet** | `| Dm | Bb | Gm | A |` | Marche harmonique grave, la basse descend. |
| **Refrain** | `| Bb | Gm | Dm | A |` | Le refrain s'élargit sans se réchauffer. |

## 5. Palette Live 12 Lite (proposition)

| Piste | Rôle | Instrument / Kit | Index |
| :--- | :--- | :--- | :--- |
| `1-Piano` | Harmonie | Drift (piano) + Reverb | 0 |
| `2-Cordes` | Nappe | Drift (strings) | 1 |
| `3-Basse` | Fondation | Drift (arco) | 2 |
| `4-Percussions` | Rythme | Impulse (tambour grave) | 3 |
| `5-Voix` | Chant | Audio + MEqualizer | 4 |

> 8 pistes maximum (Live 12 Lite). Index **0-based** ; le nom porte l'index 1-based : `1-Batterie` = index 0.

## 6. Intention de mix

Voix très présente, presque parlée sur les couplets. Cordes larges mais sombres ; aucune brillance dans les aigus.

## 7. À vérifier avant d'enregistrer

- La condamnation de 2024 : juridiction, motif, date, appel éventuel.
- Les 280 milliards : périmètre et année de référence.
- Les 2 millions d'expulsions : d'où vient le chiffre, sur quelle durée.

## 8. Notes de production

Le sample de Beethoven doit être rejoué ou libre de droits (la Symphonie n°7 est dans le domaine public pour la partition ; l'enregistrement ne l'est pas).

## 9. Session et steps de production

> La structure complète (§3) reste la cible lointaine. **À ce stade, on ne construit que trois scènes : Intro / Refrain / Outro.** Le tableau §5 décrit la couleur idéale ; l'implémentation réelle en 8 pistes mutualisées est ci-dessous. En cas de conflit, **c'est §9 qui fait foi**.

**Session** : E — Jazz / classique / chambre
**Scènes réservées** : S13–S15 (Intro / Refrain / Outro) — scène S16 libre
**Tempo de scène** : 72 BPM · **Tonalité de travail** : Ré mineur (Dm) · **Signature** : 4/4
**Chaînes à armer** : Harmonie = cordes graves · Mélodie = piano · Texture = cordes
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

1. **Créer les scènes.** Dans la session E, trois scènes consécutives : `S13 <Candidat> Intro`, `S14 <Candidat> Refrain`, `S15 <Candidat> Outro`. La scène S16 reste vide (réserve).
2. **Tempo et tonalité.** Régler le tempo de scène à 72 BPM (propriété de scène ; si l'outil ne l'expose pas, le faire à la main) et vérifier 4/4. La tonalité Ré mineur (Dm) est un repère d'écriture, pas un réglage à automatiser.
3. **Armer les chaînes.** Harmonie = cordes graves, Mélodie = piano, Texture = cordes. Vérifier le **chain selector** de chaque rack sur la valeur du candidat : c'est ce qui permet 5 sons différents sur la même piste.
4. **Écrire l'harmonie du refrain.** 8 mesures, grille `| Bb | Gm | Dm | A |`. Accords réels (vérifier les notes contre le nom), pas de renversement inutile. Vélocités 70–85, légères variations pour éviter le MIDI plat.
5. **Écrire basse et batterie.** Motif du style (Classique sombre, cordes graves, piano, sample de Beethoven), 8 mesures. Vélocités : kick 90–100, snare 85–95, hats 55–75. La basse suit la fondamentale, sans doubler la voix.
6. **Écrire le hook puis le guide vocal.** Mélodie du refrain sur `4-Mélodie`, 1 note par syllabe, tessiture **E3–B3 (64–71)**. Paroles : `PAROLES.md`. Guide chanté sur `7-Guide`, vélocités qui phrasent (75–110), pas une note plate.
7. **Intro (4–8 mesures).** Un ou deux éléments seulement : texture + basse, ou batterie + nappe. Ne pas jouer le refrain avant la scène Refrain.
8. **Outro / transition (4 mesures).** Accord tenu + transition Marseillaise : « Allons enfants… de quelle patrie parle-t-on ? ». Si l'outro est coupée, garder au moins 2 mesures de queue pour l'enchaînement.
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
