# 31 — Marine Le Pen — La Patrie en héritage

**Statut** : préparation documentaire — aucune session Ableton ouverte pour ce morceau.
**Tempo** : 96 BPM *(proposition, à valider)*
**Tonalité** : Do dièse mineur (C#m) *(proposition, à valider à l'oreille)*
**Signature** : 4/4
**Durée cible** : ≈ 2 min 30
**Atmosphère** : Solennité de meeting, tendresse et raideur mêlées
**Style** : Variété française populaire, cordes sobres, accordéon discret
**Voix** : baryton parlé-chanté de David, E3–B3 (MIDI 64–71, convention Ableton C3 = 60).

---

## 1. Le candidat — brief du 14/11/2026

| | |
| :--- | :--- |
| **Profil** | Candidate du Rassemblement national, en tête des intentions de vote (34–37 % au premier tour selon plusieurs sondages de novembre 2026). |
| **Couleur politique** | Droite nationale, protectionniste et identitaire. |
| **Actions déjà menées** | Députée, présidente du RN, candidate en 2012, 2017 et 2022. A porté la « priorité nationale » ; la sortie de l'euro, défendue en 2017, a été abandonnée depuis. |
| **Programme 2027** | 140 milliards d'euros d'économies nettes d'ici 2032 ; réduction de l'immigration ; préférence nationale ; mesures sur le logement. |
| **Pour** | Rupture nette avec la politique migratoire et économique actuelle ; figure très expérimentée en campagne. |
| **Contre** | Risque d'inéligibilité lié au pourvoi examiné le 16 décembre 2026 ; faisabilité des 140 milliards sans dire quels services publics sont touchés ; compatibilité de certaines mesures avec la Constitution et le droit européen. |
| **Actualité** | La percée de David Lisnard fragmente l'alternative à droite et au centre. |
| **Transition Marseillaise** | « Allons enfants… mais de quelle patrie parle-t-on ? » |

> **Fiabilité** : contenu issu de `Candidats 2027.md` (compilation interne du 14/11/2026). Chaque chiffre, score et procédure doit être revérifié et **daté** avant l'enregistrement. L'album doit pouvoir dire sa date de vérité.

## 2. Ce que la chanson doit faire

- Raconter une dynastie politique et un mot — la patrie — qui rassure autant qu'il exclut.
- Donner les deux faces : l'expérience de campagne, et le risque judiciaire qui peut retirer la candidate de la course.
- Éviter le procès d'intention : les faits datés, pas les caricatures.

## 3. Structure (en barres)

Intro parlée (4) → Couplet 1 (16) → Refrain (8) → Couplet 2 (16) → Refrain (8) → Pont (8) → Refrain final (8) → Outro (4) = 72 barres

## 4. Grille d'accords (proposition)

| Section | Grille (4 mesures) | Couleur / intention |
| :--- | :--- | :--- |
| **Couplet** | `| C#m | A | E | B |` | Boucle mineure qui avance malgré elle. |
| **Refrain** | `| E | B | C#m | A |` | Le refrain s'ouvre : la patrie comme héritage, pas comme drapeau. |

## 5. Palette Live 12 Lite (proposition)

| Piste | Rôle | Instrument / Kit | Index |
| :--- | :--- | :--- | :--- |
| `1-Batterie` | Rythme | Kit acoustique .adg (browser) | 0 |
| `2-Basse` | Fondation | Drift (basse) | 1 |
| `3-Cordes` | Harmonie | Drift (nappe) + Reverb | 2 |
| `4-Accordéon` | Couleur | Simpler (sample) + Auto Filter | 3 |
| `5-Voix` | Chant | Audio | 4 |

> 8 pistes maximum (Live 12 Lite). Index **0-based** ; le nom porte l'index 1-based : `1-Batterie` = index 0.

## 6. Intention de mix

Voix au centre, très intelligible ; cordes à −0.4 et accordéon à +0.4 pour aérer. Pas de reverb longue : la solennité vient du texte, pas de l'espace.

## 7. À vérifier avant d'enregistrer

- Le calendrier exact du pourvoi (audience annoncée au 16 décembre 2026) : à confirmer la veille de l'enregistrement.
- Les 140 milliards d'économies : vérifier le périmètre (net, sur combien d'années, quels postes).
- Les scores de sondage : citer l'institut et la date, jamais un chiffre nu.

## 8. Notes de production

Le titre doit pouvoir se chanter en meeting adverse sans être une insulte : c'est le test d'objectivité. L'outro reparle la transition Marseillaise pour boucler sans classer.

## 9. Session et steps de production

> La structure complète (§3) reste la cible lointaine. **À ce stade, on ne construit que trois scènes : Intro / Refrain / Outro.** Le tableau §5 décrit la couleur idéale ; l'implémentation réelle en 8 pistes mutualisées est ci-dessous. En cas de conflit, **c'est §9 qui fait foi**.

**Session** : G — Variété — session d'accueil (31e et suivants)
**Scènes réservées** : S01–S03 (Intro / Refrain / Outro) — scène S16 libre
**Tempo de scène** : 96 BPM · **Tonalité de travail** : Do dièse mineur (C#m) · **Signature** : 4/4
**Chaînes à armer** : Harmonie = cordes · Mélodie = cordes + accordéon · Texture = accordéon
**Kit de batterie de la session** : Kit acoustique léger

| Piste | Index | Rôle | Instrument / chaîne |
| :--- | :--- | :--- | :--- |
| `1-Batterie` | 0 | Rythme | Kit acoustique léger |
| `2-Basse` | 1 | Fondation | Drift — basse |
| `3-Harmonie` | 2 | Accords | Instrument Rack — 5 chaînes (1 utilisée) |
| `4-Mélodie` | 3 | Hook | Instrument Rack — 5 chaînes (1 utilisée) |
| `5-Texture` | 4 | Nappe | Instrument Rack — 2 chaînes : cordes, accordéon |
| `6-Percs/FX` | 5 | Transitions | Percussions |
| `7-Guide` | 6 | Voix guide | Drift — voix douce |
| `8-Voix` | 7 | Chant final | Audio |

### Steps

1. **Créer les scènes.** Dans la session G, trois scènes consécutives : `S01 <Candidat> Intro`, `S02 <Candidat> Refrain`, `S03 <Candidat> Outro`. La scène S16 reste vide (réserve).
2. **Tempo et tonalité.** Régler le tempo de scène à 96 BPM (propriété de scène ; si l'outil ne l'expose pas, le faire à la main) et vérifier 4/4. La tonalité Do dièse mineur (C#m) est un repère d'écriture, pas un réglage à automatiser.
3. **Armer les chaînes.** Harmonie = cordes, Mélodie = cordes + accordéon, Texture = accordéon. Vérifier le **chain selector** de chaque rack sur la valeur du candidat : c'est ce qui permet 5 sons différents sur la même piste.
4. **Écrire l'harmonie du refrain.** 8 mesures, grille `| E | B | C#m | A |`. Accords réels (vérifier les notes contre le nom), pas de renversement inutile. Vélocités 70–85, légères variations pour éviter le MIDI plat.
5. **Écrire basse et batterie.** Motif du style (Variété française populaire, cordes sobres, accordéon discret), 8 mesures. Vélocités : kick 90–100, snare 85–95, hats 55–75. La basse suit la fondamentale, sans doubler la voix.
6. **Écrire le hook puis le guide vocal.** Mélodie du refrain sur `4-Mélodie`, 1 note par syllabe, tessiture **E3–B3 (64–71)**. Paroles : `PAROLES.md`. Guide chanté sur `7-Guide`, vélocités qui phrasent (75–110), pas une note plate.
7. **Intro (4–8 mesures).** Un ou deux éléments seulement : texture + basse, ou batterie + nappe. Ne pas jouer le refrain avant la scène Refrain.
8. **Outro / transition (4 mesures).** Accord tenu + transition Marseillaise : « Allons enfants… mais de quelle patrie parle-t-on ? ». Si l'outro est coupée, garder au moins 2 mesures de queue pour l'enchaînement.
9. **Valider, puis figer.** Solo chaque piste, capture **une à la fois**, noter le RMS et ce qui a changé. Ensuite : nommer les clips, noter tempo/tonalité dans la fiche, et ne plus toucher la scène validée.

### Garde-fous

- **8 pistes maximum.** Si un instrument manque, ajouter une **chaîne** dans un rack — jamais une piste.
- **5 chaînes par rack au maximum.** Préférer Drift/Simpler à Surge XT : le coût CPU de Surge est par voix.
- **16 scènes maximum** : 15 utilisées (5 candidats × 3) + 1 libre.
- **Ne pas changer le kit de batterie** de la session sans revalider les quatre autres candidats.
- **Une seule capture à la fois.** Le set Ableton ne doit pas jouer pendant une capture.
- Une scène validée ne se réouvre pas pour « améliorer » : on note l'idée pour la suivante.

## Paroles

Paroles écrites (titre pilote) — voir `PAROLES.md`. À valider à l'oreille avant la maquette.
