# Album — Candidats 2027

**Dossier** : `sources/Candid_2027_ats/`
**Date de vérité** : 14 novembre 2026
**État** : production des maquettes — une session Ableton par candidat, Arthaud (09) en cours.

## Principe de production — maquette d'abord

**Objectif : quelque chose d'écoutable rapidement.** On ne règle pas finement les instruments
avant d'avoir une maquette. Première passe volontairement **spartiate** : peu de sons, peu de
réglages, une mélodie et un rythme qui tiennent. On affine ensuite, seulement ce qui résiste à
l'écoute.

- **Un instrument = un rôle.** Pas de rack à chaînes, pas de sound design long.
- **Niveaux grossiers**, on équilibre à l'oreille ; on ne mesure pas chaque piste avant d'écouter.
- **Une forme écoutable** : couplet / refrain / pont, même jouée avec 5 pistes.
- **La fiche technique se remplit après**, avec les valeurs réelles de la maquette.

## Le projet

Un album d'information civique : **une chanson par candidat à la présidentielle de 2027**. Chaque titre doit faire comprendre, en peu de mots, la personnalité, le parcours, les réalisations, le programme, les objectifs et la stratégie du candidat — avec un argument pour et un argument contre.

Décisions prises :

- **31 titres** (et non 34) : la liste du brief comptait quatre doublons (Zemmour, Roussel, Arthaud, Tondelier). La version retenue est celle des 31 candidats uniques.
- **Format chanson** : plusieurs sections par candidat — **ce qui le différencie**, **son discours**, **le point de vue de ses partisans**, et le **refrain**. Le refrain reste le cœur identitaire ; les autres sections nourrissent le sens.
- **Forme de maquette** : Couplet 1 (différence) → Refrain → Couplet 2 (discours) → Pont (partisans) → Refrain final. On peut commencer par deux sections et compléter.
- **Un style musical identifiable par candidat**, tiré de ses goûts connus, de son image ou de ses idées.
- **Des transitions façon Marseillaise**, humoristiques mais respectueuses, sans imposer d'ordre d'écoute.
- **Aucune diffamation** : la critique porte sur le programme, son coût, sa faisabilité, sa stratégie ou ses contradictions — jamais sur la personne, sa vie privée, son origine ou sa santé.

## Où on en est

| Élément | État |
| :--- | :--- |
| `Candidats 2027.md` (brief d'origine) | intact, non modifié |
| 31 dossiers `NN - Candidat - Titre` | créés |
| 31 `FICHE_TECHNIQUE.md` | créés (brief, angle, structure, grille, palette, mix, points à vérifier) + **§9 steps de production** |
| 31 `PAROLES.md` | refrain + sections à adapter (différence, discours, partisans) |
| `PLAN_SESSIONS.md` | **obsolète** : le modèle 6 sessions × 5 est abandonné, on passe à **une session par chanson** |
| 4 versions longues de pilotes | archivées dans `_versions_longues/` |
| Session Ableton | **Arthaud (09) ouverte** — maquette spartiate en cours |
| Mix / master | non commencés — maquette brute seulement |

## Ordre de l'album

Tirage au sort effectué avec la seed **580851** (`random.Random(580851).shuffle`). Le même tirage peut être rejoué à l'identique.

| N° | Candidat | Titre | Style |
| :--- | :--- | :--- | :--- |
| 01 | Gabriel Attal | Le Choc des savoirs (et des affaires) | pop électro |
| 02 | Jordan Bardella | Le Delfín | pop-électro identitaire |
| 03 | Philippe Poutou | Le Fordiste Anticapitaliste | punk rock |
| 04 | Jean Lassalle | La Chasse aux Parrainages | chant béarnais |
| 05 | Delphine Batho | La Politique de la Beauté | folk acoustique |
| 06 | Nicolas Dupont-Aignan | Debout la France | chant militaire |
| 07 | Raphaël Glucksmann | La Révolution écologique (en 100 jours) | folk-rock européen |
| 08 | Selma Labib | Le Bus de la Révolution | punk ouvrier |
| 09 | Nathalie Arthaud | La Révolution en 2 200 euros | chant de lutte |
| 10 | Florian Philippot | Le Frexit Rock | rock indépendant |
| 11 | Jean-Luc Mélenchon | L'Avenir en commun | rap engagé |
| 12 | Dominique de Villepin | Le Rap de la France Humaniste | rap conscient |
| 13 | Édouard Philippe | Le Havre, la dette et les familles | jazz / classique |
| 14 | Olivier Faure | La Loi du Plus Juste (en 1700) | variété social-démocrate |
| 15 | François Asselineau | Le Frexit intégral | marche militaire |
| 16 | David Lisnard | Le Rock du Gouvernement Commando | rock garage |
| 17 | Teddy Riner | Le Judo de la Nation | hip-hop orchestral |
| 18 | Laurent Wauquiez | I Will Survive (la droite) | disco-rock |
| 19 | François Bayrou | Le Grand Fleuve Central (en tango) | tango |
| 20 | Fabien Roussel | Vivre (Le Temps des Cerises électrique) | chanson populaire |
| 21 | Karim Bouamrane | Le Fédérateur | pop urbaine |
| 22 | Marine Tondelier | La Danse de la Première République Écologique | pop dansante |
| 23 | Natacha Polony | L'État d'urgence de la Production | chanson réaliste |
| 24 | François Hollande | Le Revenant Social-démocrate | variété rétro |
| 25 | Bernard Cazeneuve | Le Contrat | musique de chambre |
| 26 | Ségolène Royal | La Primaire de la Rose | chanson réaliste |
| 27 | Clara Egger | La Démocratie Directe | spoken word |
| 28 | Éric Zemmour | La France Française | classique sombre |
| 29 | Bruno Retailleau | L'Hiver démographique | chant traditionnel |
| 30 | Anasse Kazib | La Révolution Permanente | punk hardcore |
| 31 | Marine Le Pen | La Patrie en héritage | variété populaire |

## Règle de prudence (à appliquer à chaque refrain)

Avant d'écrire ou de valider une ligne :

1. **Hiérarchie des sources** : programme officiel du candidat → fait institutionnel daté → presse datée → brief interne. En cas de doute, on va au programme, pas à l'impression.
2. **Aucun fait judiciaire dans un refrain.** Si une procédure est indispensable au sens, elle est nommée exactement (juridiction, date, statut — pourvoi, appel, décision non définitive), jamais résumée par un mot qui accuse.
3. **Pas d'insinuation.** Un titre comme « et des affaires » (Attal) n'est pas repris dans le refrain : aucune affaire n'est documentée dans le brief.
4. **Critiquer le programme, pas la personne** : coût, financement, faisabilité, majorité nécessaire, compatibilité constitutionnelle ou européenne, stratégie électorale, contradiction interne.
5. **Nom officiel cité** dans chaque refrain.
6. **Chiffre = source + date.** Un chiffre sans date est un chiffre qui vieillit mal. La chanson doit pouvoir dire « au 14 novembre 2026 ».
7. **Ne pas présenter comme candidat quelqu'un qui ne l'est pas** : Bayrou, Hollande, Lassalle, Villepin (non officialisés) ; Poutou (le NPA ne présente plus de candidat) ; Bardella (substitution conditionnelle).

## Ce qui reste à faire

### 1. Validation artistique (David)

- Écouter la maquette d'Arthaud et valider la direction (chant de lutte, tambour, fanfare).
- Lire les sections (différence, discours, partisans) et dire ce qui sonne juste.
- Arbitrer les **titres de travail** : en priorité « Le Choc des savoirs (et des affaires) » (insinuation non sourcée).
- Décider, titre par titre, du degré de détail des sections.

### 2. Vérification factuelle

Chaque fiche a sa section **§7 — À vérifier avant d'enregistrer**. Les points chauds :

- **Le Pen** : calendrier du pourvoi (audience annoncée au 16/12/2026) ; périmètre des 140 milliards.
- **Philippe** : ne pas lui attribuer la réforme des retraites de 2023 (gouvernement Borne).
- **Mélenchon** : 1 069 mesures et 238 nouvelles, coût du programme, majorité parlementaire.
- **Attal** : le mot « affaires » ; 200 € net/500 € en milieu de carrière ; seuil de 20 élèves.
- **Retailleau** : 197 milliards, déficit 2031, conformité du référendum.
- **Lisnard** : 200–300 milliards « dans les dépenses de l'État ».
- **Glucksmann** : financement des 200 milliards.
- **Zemmour** : statut judiciaire exact, expulsion de 2 millions, 280 milliards.
- **Riner** : palmarès exact ; contenu réel du programme.
- **Les non-candidats** : Bayrou, Hollande, Lassalle, Villepin, Poutou, Bardella.

### 3. Mise en musique

- **Une session Ableton par chanson/candidat**, avec son tempo, ses instruments et son traitement.
  Pas de template partagé, pas de rack à chaînes.
- **Maquette spartiate d'abord** : 5–6 pistes maximum, un rôle par piste, réglages grossiers.
  On écoute, on corrige, on affine ensuite.
- **Sections** : Couplet 1 (différence) → Refrain → Couplet 2 (discours) → Pont (partisans) →
  Refrain final. Construire d'abord une forme courte, puis compléter.
- **Guide vocal** : une ligne simple pour tenir la mélodie ; on ne le peaufine pas.
- **Validation à l'oreille par extraits** de 8–10 s par section (intro, couplet, refrain, pont).
  La forme complète ne s'écoute qu'une fois la maquette stabilisée ; pas de capture intégrale à chaque passe.
- **La fiche technique se remplit après** la maquette, avec les valeurs réelles.

### 4. Production

- Enregistrer les voix, capturer, mesurer, mixer (six étapes), master (compresseur + limiteur).
- Remplir les `FICHE_TECHNIQUE.md` avec les valeurs réelles de session (pistes, volumes, FX, automations) — pas avec les propositions actuelles.

## Fichiers

```
sources/Candid_2027_ats/
├── Album.MD                     ← ce document
├── PLAN_SESSIONS.md             ← obsolète : une session par chanson
├── Candidats 2027.md            ← brief d'origine, intact
├── _versions_longues/           ← 4 versions longues de pilotes (référence)
│   ├── 09 - Nathalie Arthaud...
│   ├── 11 - Jean-Luc Mélenchon...
│   ├── 13 - Édouard Philippe...
│   └── 31 - Marine Le Pen...
└── NN - Candidat - Titre/
    ├── FICHE_TECHNIQUE.md       ← brief, angle, structure, palette, mix, §9 steps
    └── PAROLES.md               ← refrain seul + idées portées + prudence
```

## Prochaine étape proposée

1. **Arthaud (09)** : écouter la maquette, valider la direction (chant de lutte, tambour, fanfare).
2. Ajuster les paroles des sections (différence, discours, partisans) à l'oreille.
3. Quand la maquette tient, remplir la fiche technique avec les valeurs réelles.
4. Passer au candidat suivant, **une session neuve par chanson** — David ouvre et sauvegarde,
   je configure la maquette.
5. **Affiner les programmes et les personnalités** à partir de sources publiques comme
   https://2027etmoi.fr/ — vérifier et dater chaque information avant de l'intégrer aux fiches.
