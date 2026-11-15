# 06 — Nicolas Dupont-Aignan — Debout la France

**Statut** : préparation documentaire — aucune session Ableton ouverte pour ce morceau.
**Tempo** : 108 BPM *(proposition, à valider)*
**Tonalité** : Do mineur (Cm) *(proposition, à valider à l'oreille)*
**Signature** : 4/4
**Durée cible** : ≈ 2 min 05
**Atmosphère** : Garde républicaine, solennité un peu fanée
**Style** : Chant militaire, tambours et fifres, ton solennel
**Voix** : baryton parlé-chanté de David, E3–B3 (MIDI 64–71, convention Ableton C3 = 60).

---

## 1. Le candidat — brief du 14/11/2026

| | |
| :--- | :--- |
| **Profil** | Maire d'Yerres, président de Debout la France. |
| **Couleur politique** | Droite souverainiste, attachée à l'État-nation. |
| **Actions déjà menées** | Quatre campagnes présidentielles (2012, 2017, 2022, 2027), sans jamais dépasser 5 % ; candidature officialisée en septembre 2026. |
| **Programme 2027** | Sortie de l'UE ; arrêt du financement de l'Ukraine ; préférence nationale ; baisse des impôts. Le site ajoute un fonds souverain « à la norvégienne », la défiscalisation des heures supplémentaires, la retraite à 62 ans et 9 mois, et un minimum retraite par capitalisation. |
| **Pour** | Droite souverainiste « classique », sans la radicalité du RN ou de Reconquête. |
| **Contre** | 2,2 % (moyenne 2027etmoi.fr, 14/11/2026) ; plafond de verre électoral ; positions sur l'Ukraine qui le marginalisent dans le débat actuel. |
| **Actualité** | Sa position sur l'Ukraine le coupe d'une partie de l'électorat de droite. |
| **Transition Marseillaise** | « Marchons, marchons… hors de l'UE ! » |

> **Fiabilité** : contenu issu de `Candidats 2027.md` (compilation interne du 14/11/2026). Chaque chiffre, score et procédure doit être revérifié et **daté** avant l'enregistrement. L'album doit pouvoir dire sa date de vérité.

## 2. Ce que la chanson doit faire

- Rendre l'ancienneté de la candidature sans la réduire à un running gag.
- Mettre en face un programme clair (Frexit, Ukraine, impôts) et son plafond électoral.
- Dire ce que « debout » veut dire quand on est déjà debout depuis 2012.

## 3. Structure (en barres)

Intro tambours (8) → Couplet 1 (16) → Refrain (8) → Couplet 2 (16) → Refrain (8) → Pont (8) → Refrain final (8) → Outro (8) = 80 barres

## 4. Grille d'accords (proposition)

| Section | Grille (4 mesures) | Couleur / intention |
| :--- | :--- | :--- |
| **Couplet** | `| Cm | Ab | Eb | Bb |` | Marche harmonique simple, sans surprise. |
| **Refrain** | `| Ab | Eb | Bb | Cm |` | Le refrain est un défilé : on peut le reprendre en marchant. |

## 5. Palette Live 12 Lite (proposition)

| Piste | Rôle | Instrument / Kit | Index |
| :--- | :--- | :--- | :--- |
| `1-Tambours` | Rythme | Impulse (caisse claire + grosse caisse) | 0 |
| `2-Fifre` | Mélodie | Drift (flûte) | 1 |
| `3-Cuivres` | Renfort | Drift (brass) | 2 |
| `4-Voix` | Chant | Audio | 3 |
| `5-Chœur` | Réponse | Audio / Drift | 4 |

> 8 pistes maximum (Live 12 Lite). Index **0-based** ; le nom porte l'index 1-based : `1-Batterie` = index 0.

## 6. Intention de mix

Tambours très secs, fifre devant, voix au-dessus. Le refrain doit sonner comme une salle des fêtes, pas comme un stade.

## 7. À vérifier avant d'enregistrer

- L'appellation exacte du parti et sa position sur l'Ukraine au 14/11/2026.
- Le chiffre de 5 % : quel scrutin, quelle année.
- Le financement de l'Ukraine : ce qu'il propose exactement.

## 8. Notes de production

Chant militaire : ne pas pasticher la Marseillaise, seulement en garder la cadence. Une seule citation de la transition, en intro.

## 9. Session et steps de production

> La structure complète (§3) reste la cible lointaine. **À ce stade, on ne construit que trois scènes : Intro / Refrain / Outro.** Le tableau §5 décrit la couleur idéale ; l'implémentation réelle en 8 pistes mutualisées est ci-dessous. En cas de conflit, **c'est §9 qui fait foi**.

**Session** : C — Traditionnel / militaire / populaire
**Scènes réservées** : S04–S06 (Intro / Refrain / Outro) — scène S16 libre
**Tempo de scène** : 108 BPM · **Tonalité de travail** : Do mineur (Cm) · **Signature** : 4/4
**Chaînes à armer** : Harmonie = cuivres · Mélodie = fifre · Texture = tambour
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

1. **Créer les scènes.** Dans la session C, trois scènes consécutives : `S04 <Candidat> Intro`, `S05 <Candidat> Refrain`, `S06 <Candidat> Outro`. La scène S16 reste vide (réserve).
2. **Tempo et tonalité.** Régler le tempo de scène à 108 BPM (propriété de scène ; si l'outil ne l'expose pas, le faire à la main) et vérifier 4/4. La tonalité Do mineur (Cm) est un repère d'écriture, pas un réglage à automatiser.
3. **Armer les chaînes.** Harmonie = cuivres, Mélodie = fifre, Texture = tambour. Vérifier le **chain selector** de chaque rack sur la valeur du candidat : c'est ce qui permet 5 sons différents sur la même piste.
4. **Écrire l'harmonie du refrain.** 8 mesures, grille `| Ab | Eb | Bb | Cm |`. Accords réels (vérifier les notes contre le nom), pas de renversement inutile. Vélocités 70–85, légères variations pour éviter le MIDI plat.
5. **Écrire basse et batterie.** Motif du style (Chant militaire, tambours et fifres, ton solennel), 8 mesures. Vélocités : kick 90–100, snare 85–95, hats 55–75. La basse suit la fondamentale, sans doubler la voix.
6. **Écrire le hook puis le guide vocal.** Mélodie du refrain sur `4-Mélodie`, 1 note par syllabe, tessiture **E3–B3 (64–71)**. Paroles : `PAROLES.md`. Guide chanté sur `7-Guide`, vélocités qui phrasent (75–110), pas une note plate.
7. **Intro (4–8 mesures).** Un ou deux éléments seulement : texture + basse, ou batterie + nappe. Ne pas jouer le refrain avant la scène Refrain.
8. **Outro / transition (4 mesures).** Accord tenu + transition Marseillaise : « Marchons, marchons… hors de l'UE ! ». Si l'outro est coupée, garder au moins 2 mesures de queue pour l'enchaînement.
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
