# Candidats 2027 — le site de l’album

Site de présentation, d’écoute et de contribution pour l’album **Candidats 2027** :
31 chansons, une par candidat à la présidentielle, avec les paroles, les fiches
techniques, les sessions Ableton et les exports MP3/MIDI.

- Site publié : <https://scenaristeur.github.io/candid_2027_ats/>
- Dépôt : <https://github.com/scenaristeur/candid_2027_ats>
- Médias : <https://archive.org/details/candidats-2027-exports>

> **Branche `plateforme-productions`** — inventaire de toutes les productions
> (sources, sessions Ableton, exports) dans [`catalog/`](catalog/README.md).
> Cette branche prépare une plateforme multi-albums ; le site Candidats 2027
> devient un événement parmi d’autres.

> **Avertissement** — Les titres, paroles et musiques de cet album ont été
> générés par IA. Ce sont des **brouillons de vulgarisation** : ils peuvent
> contenir des erreurs factuelles, juridiques ou artistiques. Ils ne constituent
> ni une source de référence ni une validation des programmes présentés.
> Les corrections documentées sont bienvenues via les issues du dépôt.
>
> Cet album est un **exercice de collaboration musicale et culturelle partagé**,
> pas un outil politique visant à favoriser ou défavoriser un candidat. La
> démarche souhaite respecter la **neutralité** et l’**égalité** de traitement
> entre les candidats.
>
> **Ce sont pour l’instant des maquettes.** Les voix, les arrangements et le mix
> restent à faire. Les contributions de **musicien·nes** et surtout de
> **chanteur·ses** sont sollicitées : une voix, un instrument, un beat ou un mix
> peuvent suffire à faire exister un titre. Voir
> <https://scenaristeur.github.io/candid_2027_ats/participer.html#voix>.

## Sommaire

1. [Ce qui est publié](#1-ce-qui-est-publié)
2. [Démarrage rapide](#2-démarrage-rapide)
3. [Sources et lecture seule](#3-sources-et-lecture-seule)
4. [Générer le site](#4-générer-le-site)
5. [Exports MP3 et MIDI (Internet Archive)](#5-exports-mp3-et-midi-internet-archive)
6. [SEO et Open Graph](#6-seo-et-open-graph)
7. [Procédures de mise à jour](#7-procédures-de-mise-à-jour)
8. [Publier sur GitHub Pages](#8-publier-sur-github-pages)
9. [Structure du dépôt](#9-structure-du-dépôt)
10. [Dépannage](#10-dépannage)
11. [Contribuer](#11-contribuer)

## 1. Ce qui est publié

Pour chaque titre :

- une page de présentation (candidat, titre, style, tempo, tonalité, durée) ;
- les **paroles** en lecture et en téléchargement (`PAROLES.md`) ;
- la **fiche technique** en lecture et en téléchargement (`FICHE_TECHNIQUE.md`) ;
- la **session Ableton** (`.als`) lorsqu’elle existe ;
- le cas échéant, la **version longue** d’écriture ;
- les **exports MP3 et MIDI** lorsqu’ils sont publiés sur Internet Archive ;
- un lien de contribution pré-rempli (correction factuelle, paroles, session).

Le site contient aussi une page **Le projet** (note d’intention et règles
éditoriales), une page **Participer** (méthode, modèles d’issues GitHub) et une
page **Catalogue** qui inventorie toutes les productions du projet.

## Catalogue des productions

La branche `plateforme-productions` prépare une plateforme multi-albums :
Candidats 2027 devient un album parmi d’autres. La page
`docs/catalogue.html` est générée depuis `catalog/productions.json` et permet
de rechercher/filtrer les productions par album, statut, session ALS ou export.

```powershell
python scripts/build_catalog.py     # scanne les sources, ALS et exports
python scripts/build_catalogue.py   # génère docs/catalogue.html
python scripts/build_site.py        # régénère le reste du site
python scripts/check_site.py
```

Le catalogue détaillé et sa méthode sont dans [`catalog/README.md`](catalog/README.md).
Les rapprochements sont automatiques : la colonne « confiance » et la section
« Rapprochements à vérifier » signalent les points à consolider.

L’ordre recommandé est : `build_catalog.py`, puis `build_site.py`, puis
`build_catalogue.py`, puis `check_site.py`.

L’accueil affiche des statistiques calculées à chaque build :

- nombre de titres ;
- nombre d’**exports MP3** (total détecté) et, si certains ne sont pas encore
  en ligne, le nombre réellement disponible en écoute ;
- nombre d’exports MIDI, le cas échéant ;
- nombre de sessions Ableton publiées ;
- nombre de paroles complètes ;
- nombre de fiches techniques.

### Appel aux musicien·nes et chanteur·ses

Les 31 titres sont des **maquettes**. Les paroles, les fiches, les sessions
Ableton et quelques exports existent, mais les voix ne sont pas encore
enregistrées. Les contributions sont ouvertes :

- **voix lead, chœurs, interprétation** — priorité du projet ;
- guitare, piano, basse, cuivres, batterie, beat, arrangements ;
- mix et mastering ;
- corrections de paroles, de faits ou de fiches.

Les liens « Proposer une voix » sont pré-remplis sur chaque page de titre et sur
`/participer.html#voix`. Le modèle d’issue `contribution.yml` permet de décrire
la proposition, les fichiers et les crédits.

## 2. Démarrage rapide

Prérequis : **Python 3.10+**. Le build du site n’a besoin d’aucune dépendance
externe.

```powershell
python scripts/build_catalog.py
python scripts/build_site.py
python scripts/build_catalogue.py
python scripts/check_site.py
```

Prévisualiser localement :

```powershell
python -m http.server 8000 --directory docs
```

Puis ouvrir <http://localhost:8000/>.

Les outils optionnels (upload Internet Archive et images Open Graph) :

```powershell
pip install -r requirements-media.txt
```

## 3. Sources et lecture seule

Les contenus sont lus depuis :

- sources éditoriales : `C:\Users\admin\dev\ableton-holland-mcp\sources\Candid_2027_ats`
- sessions Ableton : `C:\Users\admin\Music\Ableton Live\Candid_2027_ats`
- exports MP3/MIDI : `C:\Users\admin\Music\exports ableton\Candid_2027_ats`

**Règle importante** : ces dossiers sont ouverts en **lecture seule**. Les
scripts n’y écrivent jamais. Toutes les écritures vont dans `docs/`,
`site/media.json` ou `site/assets/og/`.

### Pourquoi pas de lien symbolique vers les sources ?

Un lien symbolique ne fonctionne pas pour GitHub Pages :

1. Git enregistre un lien comme un chemin, pas comme le contenu ;
2. au déploiement, GitHub checkout le dépôt sans accès aux chemins locaux
   Windows ;
3. le lien serait cassé et les fichiers ne seraient pas publiés.

La solution retenue est un **script de synchronisation en lecture seule** :
`scripts/build_site.py` lit les sources, copie les fichiers utiles dans `docs/`
et génère les pages. Le site publié est autonome et ne dépend d’aucun chemin
local au moment du déploiement.

## 4. Générer le site

```powershell
python scripts/build_site.py
```

Chemins surchargables :

```powershell
python scripts/build_site.py `
  --sources "D:\chemin\vers\Candid_2027_ats" `
  --als "D:\chemin\vers\les\projets\Ableton"
```

Variables d’environnement équivalentes : `CANDIDAT_SOURCES`, `CANDIDAT_ALS_DIR`.
L’URL canonique du site peut être changée avec `CANDIDAT_SITE_URL`.

Le build :

1. lit `Album.MD`, les 31 dossiers `NN - Candidat - Titre`, chaque
   `PAROLES.md` et `FICHE_TECHNIQUE.md` ;
2. détecte les sessions `.als` par leur préfixe numérique (dossier `Backup`
   ignoré) ;
3. lit `site/media.json` pour les exports MP3/MIDI et calcule les statistiques ;
4. copie paroles, fiches, sessions et versions longues dans
   `docs/telechargements/` ;
5. génère l’accueil, les 31 pages de titres, les pages projet/participer/404,
   le `sitemap.xml`, `robots.txt`, le manifeste et l’archive ZIP ;
6. copie `site/assets/` (CSS, JS, favicon, images Open Graph) dans
   `docs/assets/` ;
7. injecte les métadonnées SEO et les données structurées JSON-LD.

### Vérifier le résultat

```powershell
python scripts/check_site.py
```

Le contrôle vérifie :

- les liens locaux et les fichiers de téléchargement ;
- l’équilibre de la structure HTML ;
- la présence des métadonnées SEO obligatoires (description, robots, Open
  Graph, Twitter, canonique) ;
- la validité des blocs JSON-LD ;
- la présence des images Open Graph ;
- les 31 pages de titres, le manifeste, l’archive ZIP et `.nojekyll`.

## 5. Exports MP3 et MIDI (Internet Archive)

### Pourquoi Internet Archive ?

Les MP3 ne sont **pas versionnés dans Git** : GitHub Pages a un plafond de 1 Go,
les gros fichiers alourdissent l’historique et **Git LFS n’est pas résolu par
GitHub Pages**. Les exports sont donc hébergés sur Internet Archive, et le site
pointe vers leurs URLs.

### Convention de nommage

```text
C:\Users\admin\Music\exports ableton\Candid_2027_ats
├── mp3\    NN - Candidat - Titre.mp3
└── midi\   NN - Candidat - Titre.mid
```

Le préfixe `NN -` est obligatoire : il associe le fichier au bon titre. Les
extensions reconnues sont `.mp3`, `.mid` et `.midi`. Les doublons pour un même
numéro sont signalés, le plus récent est retenu.

### Fichiers de travail

- `site/media.json` : correspondance entre les titres et les URLs hébergées.
- `scripts/prepare_media.py` : scanne les exports, construit les URLs et vérifie
  leur disponibilité.
- `scripts/upload_media.py` : envoie uniquement les nouveaux fichiers ou ceux
  dont le MD5 a changé, puis vérifie.

Par sécurité, `requireVerified` vaut `true` : **le site ne publie que les
fichiers dont l’URL a été vérifiée en HTTP 200**, pour éviter les lecteurs
cassés. Un fichier présent localement mais pas encore catalogué sur Internet
Archive est quand même compté dans les statistiques comme « export », avec la
mention « en ligne » pour ceux qui sont réellement disponibles.

### 5.1 Renseigner les clés IA-S3

Créer un compte sur <https://archive.org>, puis générer les clés sur
<https://archive.org/account/s3.php>. Les placer dans `.env` (ignoré par Git) :

```dotenv
INTERNET_ARCHIVE_S3_ACCESS_key=…
INTERNET_ARCHIVE_S3_SECRET_KEY=…
```

`.env.example` sert de modèle. Les scripts acceptent aussi les variables
standard `IA_ACCESS_KEY_ID` et `IA_SECRET_ACCESS_KEY`.

Ne jamais committer `.env` : il contient les clés secrètes.

### 5.2 Envoyer les exports

```powershell
pip install -r requirements-media.txt
python scripts/upload_media.py --item candidats-2027-exports
```

Ce que fait `upload_media.py` :

- charge les clés depuis `.env` ;
- scanne les dossiers `mp3/` et `midi/` ;
- compare les empreintes MD5 avec les fichiers déjà présents sur l’item ;
- n’envoie que les nouveaux fichiers ou ceux qui ont changé ;
- utilise un User-Agent explicite conforme aux recommandations d’Internet
  Archive ;
- envoie les métadonnées de l’item (`mediatype:audio`,
  `collection:opensource_audio`, titre, créateur, date, langue, description) ;
- réessaie en cas d’erreur réseau ;
- relance automatiquement `prepare_media.py --verify`.

### 5.2 bis Nettoyer les métadonnées avant l’envoi

Les MP3 peuvent contenir des tags ID3 personnels (nom, e-mail, logiciel,
commentaires, pochettes). `sanitize_media.py` crée une copie propre **sans
modifier les originaux** :

```powershell
python scripts/sanitize_media.py `
  --input  "C:\Users\admin\Music\exports ableton\Candid_2027_ats" `
  --output "C:\Users\admin\Music\archive_clean\Candid_2027_ats"

python scripts/upload_media.py `
  --exports "C:\Users\admin\Music\archive_clean\Candid_2027_ats" `
  --item candidats-2027-exports
```

Le script :

- supprime tous les tags ID3 existants ;
- écrit uniquement des tags publics : titre, artiste, album, année, genre,
  commentaire ;
- copie les WAV/MIDI sans les modifier ;
- produit `sanitization-report.json` pour garder la trace.

Les `.als` publiés par le site sont également nettoyés : les chemins
`C:/Users/<nom>` sont remplacés par `C:/Users/Public` au moment du build, sans
toucher aux sources.

Voir ce qui serait envoyé sans rien téléverser :

```powershell
python scripts/upload_media.py --item candidats-2027-exports --dry-run
```

L’identifiant `candidats-2027-exports` doit être unique sur Internet Archive.
On peut le changer avec `--item`.

### 5.3 Vérifier et publier

```powershell
python scripts/prepare_media.py --item candidats-2027-exports --verify
python scripts/build_site.py
python scripts/check_site.py
```

Les fichiers vérifiés apparaissent alors sur la page du titre : lecteur audio,
téléchargement MP3, téléchargement MIDI, badge sur l’accueil et filtre « MP3 ».

### 5.4 Ajouter un nouvel export

1. Déposer le fichier dans `mp3/` ou `midi/` avec le préfixe `NN -`.
2. Lancer `python scripts/upload_media.py --item candidats-2027-exports`.
3. Attendre la fin du catalogage Internet Archive.
4. Lancer `python scripts/prepare_media.py --item candidats-2027-exports --verify`.
5. Régénérer et vérifier le site.

### 5.5 Remplacer un export

Réexporter le fichier sous le **même nom**, puis relancer
`upload_media.py` : la comparaison MD5 détecte le changement et réenvoie le
fichier. Internet Archive conserve une version de sauvegarde dans l’item.

### 5.6 Comprendre les URLs Internet Archive

Deux URLs peuvent exister pour un même fichier :

- **URL canonique** :
  `https://archive.org/download/candidats-2027-exports/fichier.mp3`
- **URL du nœud de stockage** :
  `https://ia601009.us.archive.org/11/items/candidats-2027-exports/fichier.mp3`

Pendant la dérivation d’un item, l’URL canonique peut renvoyer une erreur
temporaire alors que le nœud sert déjà le fichier. `prepare_media.py` teste les
deux : il utilise le nœud si nécessaire, conserve `canonicalUrl` dans
`site/media.json`, et repasse automatiquement à l’URL canonique dès qu’elle
répond.

### 5.7 Alternative : lecteur local

Pour tester sans Internet Archive, déposer `site/audio/09.mp3` puis régénérer :
un lecteur local apparaît sur le titre 09. Ces fichiers seraient versionnés
dans Git : à réserver aux tests ou aux petits extraits.

## 6. SEO et Open Graph

Chaque page générée contient :

- un `<title>` unique et une `meta description` ;
- une URL canonique et une alternative `hreflang="fr"` ;
- des directives `robots` (`index, follow`, previews larges) ;
- des mots-clés ;
- la balise de vérification **Google Search Console**
  (`GOOGLE_SITE_VERIFICATION` dans `scripts/build_site.py`) ;
- les balises **Open Graph** (`og:type`, `og:title`, `og:description`,
  `og:url`, `og:image`, dimensions et texte alternatif) ;
- les balises **Twitter/X** (`summary_large_image`) ;
- un bloc **JSON-LD** :
  - accueil : `MusicAlbum` avec les 31 `MusicRecording`, `WebSite` et
    `Organization` ;
  - page de titre : `MusicRecording`, `BreadcrumbList` et `WebPage`, avec
    durée ISO 8601 et `AudioObject` si un MP3 est publié ;
  - pages projet/participer : `AboutPage` / `WebPage` ;
- un `sitemap.xml` avec `lastmod`, priorités et images ;
- un `robots.txt` pointant vers le sitemap.

La page 404 est en `noindex, nofollow`.

Les titres de pages privilégient la requête « Paroles de … » ; le `<h1>` contient
le candidat **et** le titre de la chanson ; la navigation principale reste
visible sur mobile (elle passe sur une deuxième ligne au lieu d’être masquée).

> **Ne pas modifier `docs/index.html` à la main** : il est régénéré par
> `build_site.py`. La balise de vérification Google est portée par la constante
> `GOOGLE_SITE_VERIFICATION` dans le script.

### Images Open Graph

Les images sont dans `site/assets/og/` :

- `album.png` pour l’accueil et les pages projet/participer ;
- `NN.png` pour chaque titre.

Pour les régénérer après un changement de titre, de candidat ou de style :

```powershell
python scripts/make_og.py
```

Le build copie ensuite ces images dans `docs/assets/og/`. Format : 1200 × 630,
fond papier, accent propre à chaque titre.

### Vérifier le SEO

```powershell
python scripts/check_site.py
```

Pour aller plus loin :

- <https://search.google.com/test/rich-results>
- <https://validator.schema.org/>
- les débogueurs d’aperçu social de Facebook, LinkedIn et X.

## 7. Procédures de mise à jour

### 7.1 Après une modification des sources éditoriales

```powershell
python scripts/build_catalog.py
python scripts/build_site.py
python scripts/build_catalogue.py
python scripts/check_site.py
git add -A
git commit -m "Met à jour le site et le catalogue"
git push
```

### 7.2 Après l’ajout d’exports MP3/MIDI

```powershell
python scripts/upload_media.py --item candidats-2027-exports --dry-run
python scripts/upload_media.py --item candidats-2027-exports
python scripts/prepare_media.py --item candidats-2027-exports --verify
python scripts/build_catalog.py
python scripts/build_site.py
python scripts/build_catalogue.py
python scripts/check_site.py
git add -A
git commit -m "Publie les exports audio et MIDI"
git push
```

Si Internet Archive est encore en train de dériver les fichiers, le site
fonctionne avec l’URL du nœud de stockage. Relancer simplement
`prepare_media.py --verify` plus tard pour repasser aux URLs canoniques.

### 7.3 Après un changement de titre ou de style

```powershell
python scripts/make_og.py
python scripts/build_site.py
python scripts/build_catalogue.py
python scripts/check_site.py
git add -A
git commit -m "Met à jour les visuels et le SEO"
git push
```

### 7.4 Contrôle avant publication

```powershell
python scripts/build_catalog.py
python scripts/build_site.py
python scripts/build_catalogue.py
python scripts/check_site.py
```

Le contrôle doit afficher :

```text
✓ 32 pages de titres, liens, structure HTML et SEO valides
```

## 8. Publier sur GitHub Pages

Le site publié vit dans `docs/`. Deux options :

### Option A — GitHub Actions (recommandée)

1. Settings → Pages → Build and deployment → Source : **GitHub Actions**.
2. Pousser sur `main` : le workflow `.github/workflows/pages.yml` publie `docs/`.

### Option B — branche `main` / dossier `/docs`

1. Settings → Pages → Source : **Deploy from a branch**.
2. Branche `main`, dossier `/docs`.

Le fichier `docs/.nojekyll` évite le traitement Jekyll.

## 9. Structure du dépôt

```text
.
├── .env.example              # modèle de clés IA-S3 (le vrai .env est ignoré)
├── requirements-media.txt    # internetarchive + Pillow (outils optionnels)
├── scripts/
│   ├── build_site.py         # génère docs/ depuis les sources (lecture seule)
│   ├── build_catalog.py      # inventorie productions, ALS et exports
│   ├── build_catalogue.py    # génère docs/catalogue.html
│   ├── markdown.py           # rendu Markdown minimal, sans dépendance
│   ├── make_og.py            # génère les images Open Graph 1200 × 630
│   ├── prepare_media.py      # URLs et vérification des exports MP3/MIDI
│   ├── sanitize_media.py     # copie propre des MP3 avant Archive.org
│   ├── upload_media.py       # upload MD5 vers Internet Archive
│   └── check_site.py         # liens, HTML, SEO, JSON-LD, images OG
├── catalog/
│   ├── PRODUCTIONS.md        # catalogue lisible, groupé par album
│   ├── productions.csv       # une ligne par production
│   ├── productions.json      # données pour la plateforme
│   ├── als_versions.csv      # inventaire des sessions .als
│   ├── exports.csv           # inventaire des exports audio/MIDI
│   └── README.md             # méthode et limites
├── site/
│   ├── assets/style.css      # feuille de style source
│   ├── assets/app.js         # recherche, filtres, thème
│   ├── assets/favicon.svg
│   ├── assets/og/            # images Open Graph générées
│   ├── media.json            # URLs des exports hébergés
│   └── audio/                # optionnel : 01.mp3… pour un lecteur local
├── docs/                     # site généré, publié par GitHub Pages
│   ├── index.html
│   ├── catalogue.html
│   ├── titres/NN-….html
│   ├── projet.html
│   ├── participer.html
│   ├── 404.html
│   ├── sitemap.xml
│   ├── robots.txt
│   ├── assets/               # CSS, JS, favicon, og/
│   └── telechargements/
│       ├── als/
│       ├── paroles/
│       ├── fiches/
│       ├── versions-longues/
│       ├── album/Album.MD
│       ├── manifest.json
│       ├── candidats-2027-pack.zip
│       └── LISEZ-MOI.txt
└── .github/
    ├── workflows/pages.yml
    └── ISSUE_TEMPLATE/       # corrections et contributions
```

## 10. Dépannage

### Un MP3 n’apparaît pas sur le site

1. Vérifier qu’il est dans `site/media.json` :
   `python scripts/prepare_media.py --item candidats-2027-exports --verify`
2. Vérifier que `verified` vaut `true`.
3. Régénérer : `python scripts/build_site.py`.

### « The item you have requested has a problem… »

L’item est encore dans la file de dérivation d’Internet Archive. Le fichier
peut déjà être servi par le nœud de stockage. `prepare_media.py` bascule
automatiquement dessus. Pour suivre la tâche :

```powershell
pip install internetarchive
ia tasks candidats-2027-exports
ia tasks --get-task-log <task_id>
```

La dérivation peut prendre plusieurs minutes. Ne pas recréer l’item : attendre
la fin, puis relancer `prepare_media.py --verify`.

### L’URL canonique renvoie 404 mais le nœud fonctionne

C’est normal pendant la dérivation. Le site utilise l’URL du nœud. Relancer
`prepare_media.py --verify` plus tard pour repasser au canonique.

### L’upload échoue

- Vérifier `.env` et régénérer les clés sur
  <https://archive.org/account/s3.php>.
- Vérifier que les deux clés sont présentes.
- L’identifiant d’item doit être unique : changer `--item` si nécessaire.
- Respecter les limites : `upload_media.py` ne renvoie que les fichiers dont le
  MD5 a changé.

### Les images Open Graph manquent

```powershell
python scripts/make_og.py
python scripts/build_site.py
```

### Le contrôle SEO échoue

Lire le message : il indique la page, la métadonnée absente, le JSON-LD invalide
ou l’image manquante. Corriger puis relancer `build_site.py` et
`check_site.py`.

## 11. Contribuer

Les corrections et contributions passent par les issues GitHub :

- **Voix / interprétation** : priorité du projet — une voix lead, des chœurs,
  une intention.
- **Musique** : instrument, arrangement, beat, mix.
- **Correction factuelle** : source datée obligatoire.
- **Contribution** : paroles, session Ableton, visuel ou site.

Les règles éditoriales sont publiées sur `/projet.html` et rappelées sur
`/participer.html` : on critique le programme, pas la personne ; un chiffre =
une source + une date ; aucun fait judiciaire dans un refrain ; les partisans
parlent en leur nom ; neutralité et égalité de traitement.

## Crédits

Textes, musiques et sessions : © leurs auteurs. Le site propose les fichiers
pour l’écoute, l’étude et la reprise ; contacter le projet pour tout autre usage.
