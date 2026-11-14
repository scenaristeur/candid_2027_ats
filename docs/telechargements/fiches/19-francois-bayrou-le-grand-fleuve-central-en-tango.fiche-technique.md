# 19 — François Bayrou — Le Grand Fleuve Central (en tango)

**Statut** : préparation documentaire — aucune session Ableton ouverte pour ce morceau.
**Tempo** : 96 BPM *(proposition, à valider)*
**Tonalité** : Ré mineur (Dm) *(proposition, à valider à l'oreille)*
**Signature** : 4/4
**Durée cible** : ≈ 2 min 30
**Atmosphère** : Lenteur hypnotique, salle de bal provinciale
**Style** : Tango et musique classique, bandonéon, piano
**Voix** : baryton parlé-chanté de David, E3–B3 (MIDI 64–71, convention Ableton C3 = 60).

---

## 1. Le candidat — brief du 14/11/2026

| | |
| :--- | :--- |
| **Profil** | Maire de Pau, ancien Premier ministre, président du MoDem. |
| **Couleur politique** | Centrisme pro-européen, obsédé par la dette. |
| **Actions déjà menées** | Plan « Stop à la dette » ; proposition d'une primaire « du grand fleuve central », de la gauche modérée à la droite gaulliste. |
| **Programme 2027** | Réduction du déficit à 2,8 % en 2029 ; non-remplacement d'un fonctionnaire sur trois ; augmentation du temps de travail. |
| **Pour** | Alternative au duel Le Pen–Mélenchon ; gestion sérieuse de la dette. |
| **Contre** | Primaire qui ne suscite pas d'enthousiasme ; il exclut lui-même une candidature personnelle, ce qui affaiblit la chanson. |
| **Actualité** | La primaire du « grand fleuve central » ne décolle pas. |
| **Transition Marseillaise** | « Marchons, marchons… vers le centre ! » |

> **Fiabilité** : contenu issu de `Candidats 2027.md` (compilation interne du 14/11/2026). Chaque chiffre, score et procédure doit être revérifié et **daté** avant l'enregistrement. L'album doit pouvoir dire sa date de vérité.

## 2. Ce que la chanson doit faire

- Dire la dette sans jargon : combien, pour qui, à quelle échéance.
- Montrer que la « primaire du grand fleuve » est une idée de rassemblement qui ne rassemble pas.
- Ne pas moquer le centrisme : le tango est lent parce que la décision l'est.

## 3. Structure (en barres)

Intro bandonéon (8) → Couplet 1 (16) → Refrain (8) → Couplet 2 (16) → Refrain (8) → Pont (8) → Refrain final (8) → Outro (8) = 80 barres

## 4. Grille d'accords (proposition)

| Section | Grille (4 mesures) | Couleur / intention |
| :--- | :--- | :--- |
| **Couplet** | `| Dm | Gm | A | Dm |` | Tango mineur, la cadence tourne en rond. |
| **Refrain** | `| Gm | A | Dm | Bb |` | Le refrain s'élargit, puis retombe. |

## 5. Palette Live 12 Lite (proposition)

| Piste | Rôle | Instrument / Kit | Index |
| :--- | :--- | :--- | :--- |
| `1-Bandonéon` | Mélodie | Drift (accordéon) | 0 |
| `2-Piano` | Harmonie | Drift (piano) | 1 |
| `3-Contrebasse` | Fondation | Drift (basse acoustique) | 2 |
| `4-Batterie` | Rythme | Impulse (percussions) | 3 |
| `5-Voix` | Chant | Audio | 4 |

> 8 pistes maximum (Live 12 Lite). Index **0-based** ; le nom porte l'index 1-based : `1-Batterie` = index 0.

## 6. Intention de mix

Bandonéon devant, presque trop ; voix légèrement en retrait au couplet, devant au refrain. Une petite reverb de salle, pas de hall.

## 7. À vérifier avant d'enregistrer

- Le 2,8 % de déficit en 2029 : hypothèses de croissance associées.
- Son statut de candidat : il exclut une candidature personnelle, donc la chanson parle d'une hypothèse.
- Le périmètre de la primaire proposée.

## 8. Notes de production

Si Bayrou n'est pas candidat, la chanson devient une chanson sur une primaire : c'est un cas intéressant, à assumer dans le texte.

## 9. Session et steps de production

> La structure complète (§3) reste la cible lointaine. **À ce stade, on ne construit que trois scènes : Intro / Refrain / Outro.** Le tableau §5 décrit la couleur idéale ; l'implémentation réelle en 8 pistes mutualisées est ci-dessous. En cas de conflit, **c'est §9 qui fait foi**.

**Session** : E — Jazz / classique / chambre
**Scènes réservées** : S04–S06 (Intro / Refrain / Outro) — scène S16 libre
**Tempo de scène** : 96 BPM · **Tonalité de travail** : Ré mineur (Dm) · **Signature** : 4/4
**Chaînes à armer** : Harmonie = bandonéon · Mélodie = bandonéon · Texture = piano
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

1. **Créer les scènes.** Dans la session E, trois scènes consécutives : `S04 <Candidat> Intro`, `S05 <Candidat> Refrain`, `S06 <Candidat> Outro`. La scène S16 reste vide (réserve).
2. **Tempo et tonalité.** Régler le tempo de scène à 96 BPM (propriété de scène ; si l'outil ne l'expose pas, le faire à la main) et vérifier 4/4. La tonalité Ré mineur (Dm) est un repère d'écriture, pas un réglage à automatiser.
3. **Armer les chaînes.** Harmonie = bandonéon, Mélodie = bandonéon, Texture = piano. Vérifier le **chain selector** de chaque rack sur la valeur du candidat : c'est ce qui permet 5 sons différents sur la même piste.
4. **Écrire l'harmonie du refrain.** 8 mesures, grille `| Gm | A | Dm | Bb |`. Accords réels (vérifier les notes contre le nom), pas de renversement inutile. Vélocités 70–85, légères variations pour éviter le MIDI plat.
5. **Écrire basse et batterie.** Motif du style (Tango et musique classique, bandonéon, piano), 8 mesures. Vélocités : kick 90–100, snare 85–95, hats 55–75. La basse suit la fondamentale, sans doubler la voix.
6. **Écrire le hook puis le guide vocal.** Mélodie du refrain sur `4-Mélodie`, 1 note par syllabe, tessiture **E3–B3 (64–71)**. Paroles : `PAROLES.md`. Guide chanté sur `7-Guide`, vélocités qui phrasent (75–110), pas une note plate.
7. **Intro (4–8 mesures).** Un ou deux éléments seulement : texture + basse, ou batterie + nappe. Ne pas jouer le refrain avant la scène Refrain.
8. **Outro / transition (4 mesures).** Accord tenu + transition Marseillaise : « Marchons, marchons… vers le centre ! ». Si l'outro est coupée, garder au moins 2 mesures de queue pour l'enchaînement.
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
