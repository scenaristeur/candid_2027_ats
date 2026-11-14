# Candidats 2027 — le site de l’album

Site de présentation, d’écoute et de contribution pour l’album **Candidats 2027** :
31 chansons, une par candidat à la présidentielle, avec les paroles, les fiches
techniques et les sessions Ableton à télécharger.

- Site publié : <https://scenaristeur.github.io/candid_2027_ats/>
- Dépôt : <https://github.com/scenaristeur/candid_2027_ats>

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

## Ce qui est publié

Pour chaque titre :

- une page de présentation (candidat, titre, style, tempo, tonalité, durée) ;
- les **paroles** en lecture et en téléchargement (`PAROLES.md`) ;
- la **fiche technique** en lecture et en téléchargement (`FICHE_TECHNIQUE.md`) ;
- la **session Ableton** (`.als`) lorsqu’elle existe ;
- le cas échéant, la **version longue** d’écriture ;
- un lien de contribution pré-rempli (correction factuelle, paroles, session).

Le site contient aussi une page **Le projet** (note d’intention et règles
éditoriales) et une page **Participer** (méthode, modèles d’issues GitHub).

## MP3 et MIDI : hébergement sur Internet Archive

Les exports audio et MIDI ne sont **pas versionnés dans Git** : ils sont hébergés
sur Internet Archive, et le site pointe vers leurs URLs. Le dossier local de
départ est :

```text
C:\Users\admin\Music\exports ableton\Candid_2027_ats
├── mp3\    NN - Candidat - Titre.mp3
└── midi\   NN - Candidat - Titre.mid
```

Le fichier `site/media.json` fait le lien entre les titres et les fichiers
hébergés. Par sécurité, `requireVerified` vaut `true` : **le site ne publie que
les fichiers dont l’URL a été vérifiée en HTTP 200**, pour éviter les lecteurs
cassés.

### 1. Générer la correspondance locale

```powershell
python scripts/prepare_media.py --item candidats-2027-exports
```

Le script lit le dossier d’exports en lecture seule, associe chaque fichier à son
numéro de titre et écrit `site/media.json` avec les URLs
`https://archive.org/download/candidats-2027-exports/…`.

### 2. Déposer les fichiers sur Internet Archive

Créer un compte sur <https://archive.org>, puis :

```powershell
pip install internetarchive
ia configure
```

Uploader l’ensemble des fichiers (le script affiche la commande complète) :

```powershell
$files = Get-ChildItem "C:\Users\admin\Music\exports ableton\Candid_2027_ats\mp3","C:\Users\admin\Music\exports ableton\Candid_2027_ats\midi" -File -Recurse | ForEach-Object FullName
ia upload candidats-2027-exports $files `
  --metadata="title:Candidats 2027 — exports audio et MIDI" `
  --metadata="creator:Candidats 2027" `
  --metadata="date:2026-11-14" `
  --metadata="language:fre" `
  --metadata="collection:opensource_audio"
```

L’identifiant `candidats-2027-exports` est un exemple : il doit être unique sur
Internet Archive. On peut le changer avec `--item`.

### 3. Vérifier puis régénérer le site

```powershell
python scripts/prepare_media.py --item candidats-2027-exports --verify
python scripts/build_site.py
python scripts/check_site.py
```

Les fichiers vérifiés apparaissent alors sur la page du titre : lecteur audio,
téléchargement MP3, téléchargement MIDI, badge sur l’accueil et filtre « MP3 ».

Pour remplacer un export, on réuploade le fichier sous le même nom, puis on
relance `prepare_media.py --verify` et le build.

### Alternative : lecteur local

Pour tester sans Internet Archive, déposer `site/audio/09.mp3` puis régénérer :
un lecteur local apparaît sur le titre 09. Ces fichiers-là seraient versionnés
dans Git, donc à réserver aux tests ou aux petits extraits.

## Pourquoi pas de lien symbolique vers les sources ?

Un lien symbolique ne fonctionne pas pour GitHub Pages :

1. Git enregistre un lien comme un simple fichier texte contenant un chemin
   (`.gitconfig` a même `symlinks = false` ici, donc Windows peut le stocker
   comme un fichier ordinaire) ;
2. au déploiement, GitHub checkout le dépôt sans accès à
   `C:\Users\admin\dev\ableton-holland-mcp\...` ni au dossier Ableton Live ;
3. le lien serait donc cassé, et les fichiers ne seraient pas publiés.

La solution retenue est un **script de synchronisation en lecture seule** :
`scripts/build_site.py` lit les sources, copie les fichiers utiles dans `docs/`
et génère les pages. Le site publié est autonome, reproductible et ne dépend
d’aucun chemin local au moment du déploiement.

**Règle importante** : les sources sont ouvertes en lecture seule. Le script
n’écrit jamais dans `ableton-holland-mcp/sources` ni dans le dossier Ableton
Live. Toutes les écritures vont dans `docs/`.

## Régénérer le site

Prérequis : Python 3.10+ (aucune dépendance externe).

```powershell
python scripts/build_site.py
```

Chemins par défaut :

- sources : `C:\Users\admin\dev\ableton-holland-mcp\sources\Candid_2027_ats`
- sessions Ableton : `C:\Users\admin\Music\Ableton Live\Candid_2027_ats`

On peut les surcharger :

```powershell
python scripts/build_site.py `
  --sources "D:\chemin\vers\Candid_2027_ats" `
  --als "D:\chemin\vers\les\projets\Ableton"
```

ou avec les variables `CANDIDAT_SOURCES` et `CANDIDAT_ALS_DIR`.

Le script :

1. lit `Album.MD`, les 31 dossiers `NN - Candidat - Titre`, chaque
   `PAROLES.md` et `FICHE_TECHNIQUE.md` ;
2. détecte les sessions `.als` par leur préfixe numérique (sans toucher au
   dossier `Backup`) ;
3. copie les fichiers dans `docs/telechargements/` ;
4. génère l’accueil, les 31 pages de titres, les pages projet/participer/404,
   le plan du site et l’archive ZIP ;
5. copie `site/assets/` (CSS, JS, favicon) dans `docs/assets/`.

Vérifier le résultat :

```powershell
python scripts/check_site.py
```

Le contrôle vérifie les liens locaux, la structure HTML, les 31 pages de titres
et la présence de l’archive et du manifeste.

## Publier sur GitHub Pages

Le site publié vit dans `docs/`. Deux options :

### Option A — GitHub Actions (recommandée)

1. Settings → Pages → Build and deployment → Source : **GitHub Actions**.
2. Pousser sur `main` : le workflow `.github/workflows/pages.yml` publie `docs/`.

### Option B — branche `main` / dossier `/docs`

1. Settings → Pages → Source : **Deploy from a branch**.
2. Branche `main`, dossier `/docs`.

Le fichier `docs/.nojekyll` évite le traitement Jekyll.

## Structure

```text
.
├── scripts/
│   ├── build_site.py       # génère docs/ depuis les sources (lecture seule)
│   ├── prepare_media.py    # associe les exports MP3/MIDI à Internet Archive
│   ├── check_site.py       # vérifie liens, structure et fichiers attendus
│   └── markdown.py         # rendu Markdown minimal, sans dépendance
├── site/
│   ├── assets/style.css    # feuille de style source
│   ├── assets/app.js       # recherche, filtres, thème
│   ├── assets/favicon.svg
│   ├── media.json          # URLs des exports hébergés sur Internet Archive
│   └── audio/              # optionnel : 01.mp3, 02.mp3… pour un lecteur local
├── docs/                   # site généré, publié par GitHub Pages
│   ├── index.html
│   ├── titres/NN-….html
│   ├── projet.html
│   ├── participer.html
│   ├── 404.html
│   ├── assets/
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
    └── ISSUE_TEMPLATE/     # corrections et contributions
```

## Contribuer

Les corrections et contributions passent par les issues GitHub :

- **Correction factuelle** : source datée obligatoire.
- **Contribution** : paroles, session Ableton, mix, voix, visuel ou site.

Les règles éditoriales du projet sont publiées sur `/projet.html` et rappelées
sur `/participer.html` : on critique le programme, pas la personne ; un chiffre
= une source + une date ; aucun fait judiciaire dans un refrain.

## Crédits

Textes, musiques et sessions : © leurs auteurs. Le site propose les fichiers
pour l’écoute, l’étude et la reprise ; contacter le projet pour tout autre usage.
