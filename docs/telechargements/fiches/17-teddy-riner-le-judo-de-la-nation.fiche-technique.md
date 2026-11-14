# 17 — Teddy Riner — Le Judo de la Nation

**Statut** : préparation documentaire — aucune session Ableton ouverte pour ce morceau.
**Tempo** : 92 BPM *(proposition, à valider)*
**Tonalité** : Do dièse mineur (C#m) *(proposition, à valider à l'oreille)*
**Signature** : 4/4
**Durée cible** : ≈ 2 min 25
**Atmosphère** : Hymne sportif qui bascule dans la politique
**Style** : Hip-hop orchestral, cuivres solennels, beat de stade
**Voix** : baryton parlé-chanté de David, E3–B3 (MIDI 64–71, convention Ableton C3 = 60).

---

## 1. Le candidat — brief du 14/11/2026

| | |
| :--- | :--- |
| **Profil** | Quintuple champion olympique de judo, icône du sport français, candidat de la société civile. |
| **Couleur politique** | Société civile, rassemblement, discipline. |
| **Actions déjà menées** | Aucune action politique. Sa notoriété, sa discipline et son image de rassembleur sont son seul capital. |
| **Programme 2027** | Encore flou : sécurité et retraites évoquées, sans cadre programmatique détaillé. |
| **Pour** | Rupture avec les professionnels de la politique ; figure d'unité. |
| **Contre** | Absence totale d'expérience politique et de programme structuré ; risque de faire de l'élection un concours de popularité. |
| **Actualité** | Sa candidature déplace la question de la légitimité. |
| **Transition Marseillaise** | « Entendez-vous… dans les stades ? » |

> **Fiabilité** : contenu issu de `Candidats 2027.md` (compilation interne du 14/11/2026). Chaque chiffre, score et procédure doit être revérifié et **daté** avant l'enregistrement. L'album doit pouvoir dire sa date de vérité.

## 2. Ce que la chanson doit faire

- Reconnaître la puissance symbolique du sport, sans la confondre avec un programme.
- Demander des réponses concrètes sur sécurité et retraites.
- Poser la question de la légitimité sans mépriser le candidat.

## 3. Structure (en barres)

Intro cuivres (8) → Couplet 1 (16) → Refrain (8) → Couplet 2 (16) → Refrain (8) → Pont (8) → Refrain final (8) → Outro (4) = 76 barres

## 4. Grille d'accords (proposition)

| Section | Grille (4 mesures) | Couleur / intention |
| :--- | :--- | :--- |
| **Couplet** | `| C#m | A | E | B |` | Hip-hop orchestral, cuivres larges. |
| **Refrain** | `| A | E | B | C#m |` | Le refrain est un hymne de stade. |

## 5. Palette Live 12 Lite (proposition)

| Piste | Rôle | Instrument / Kit | Index |
| :--- | :--- | :--- | :--- |
| `1-Batterie` | Rythme | Drum Rack (stade) | 0 |
| `2-Basse` | Fondation | Drift (sub) | 1 |
| `3-Cuivres` | Mélodie | Drift (brass) | 2 |
| `4-Cordes` | Nappe | Drift (strings) | 3 |
| `5-Voix` | Chant | Audio | 4 |

> 8 pistes maximum (Live 12 Lite). Index **0-based** ; le nom porte l'index 1-based : `1-Batterie` = index 0.

## 6. Intention de mix

Cuivres très larges, beat de stade, voix devant. Le pont doit se vider (couper batterie et cuivres) pour laisser la question politique.

## 7. À vérifier avant d'enregistrer

- Le palmarès exact (titres olympiques, dates).
- Le contenu réel de son programme au 14/11/2026.
- Son statut de candidature.

## 8. Notes de production

Le morceau doit commencer comme un hymne et finir comme une question : c'est le renversement de tout l'album.

## 9. Session et steps de production

> La structure complète (§3) reste la cible lointaine. **À ce stade, on ne construit que trois scènes : Intro / Refrain / Outro.** Le tableau §5 décrit la couleur idéale ; l'implémentation réelle en 8 pistes mutualisées est ci-dessous. En cas de conflit, **c'est §9 qui fait foi**.

**Session** : F — Orchestral / folk / rap
**Scènes réservées** : S13–S15 (Intro / Refrain / Outro) — scène S16 libre
**Tempo de scène** : 92 BPM · **Tonalité de travail** : Do dièse mineur (C#m) · **Signature** : 4/4
**Chaînes à armer** : Harmonie = cuivres · Mélodie = cuivres · Texture = cordes
**Kit de batterie de la session** : Boom bap / folk / tambour

| Piste | Index | Rôle | Instrument / chaîne |
| :--- | :--- | :--- | :--- |
| `1-Batterie` | 0 | Rythme | Drum Rack — boom bap / folk / tambour |
| `2-Basse` | 1 | Fondation | Drift — sub / basse acoustique |
| `3-Harmonie` | 2 | Accords | Instrument Rack — 5 chaînes cordes/cuivres/guitare |
| `4-Mélodie` | 3 | Hook | Instrument Rack — 5 chaînes cuivres/cordes |
| `5-Texture` | 4 | Nature / nappe | Instrument Rack — 2 chaînes : nature, nappe |
| `6-Percs/FX` | 5 | Transitions | Percussions — tambour, shaker |
| `7-Guide` | 6 | Voix guide | Drift — voix douce |
| `8-Voix` | 7 | Chant final | Audio |

### Steps

1. **Créer les scènes.** Dans la session F, trois scènes consécutives : `S13 <Candidat> Intro`, `S14 <Candidat> Refrain`, `S15 <Candidat> Outro`. La scène S16 reste vide (réserve).
2. **Tempo et tonalité.** Régler le tempo de scène à 92 BPM (propriété de scène ; si l'outil ne l'expose pas, le faire à la main) et vérifier 4/4. La tonalité Do dièse mineur (C#m) est un repère d'écriture, pas un réglage à automatiser.
3. **Armer les chaînes.** Harmonie = cuivres, Mélodie = cuivres, Texture = cordes. Vérifier le **chain selector** de chaque rack sur la valeur du candidat : c'est ce qui permet 5 sons différents sur la même piste.
4. **Écrire l'harmonie du refrain.** 8 mesures, grille `| A | E | B | C#m |`. Accords réels (vérifier les notes contre le nom), pas de renversement inutile. Vélocités 70–85, légères variations pour éviter le MIDI plat.
5. **Écrire basse et batterie.** Motif du style (Hip-hop orchestral, cuivres solennels, beat de stade), 8 mesures. Vélocités : kick 90–100, snare 85–95, hats 55–75. La basse suit la fondamentale, sans doubler la voix.
6. **Écrire le hook puis le guide vocal.** Mélodie du refrain sur `4-Mélodie`, 1 note par syllabe, tessiture **E3–B3 (64–71)**. Paroles : `PAROLES.md`. Guide chanté sur `7-Guide`, vélocités qui phrasent (75–110), pas une note plate.
7. **Intro (4–8 mesures).** Un ou deux éléments seulement : texture + basse, ou batterie + nappe. Ne pas jouer le refrain avant la scène Refrain.
8. **Outro / transition (4 mesures).** Accord tenu + transition Marseillaise : « Entendez-vous… dans les stades ? ». Si l'outro est coupée, garder au moins 2 mesures de queue pour l'enchaînement.
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
