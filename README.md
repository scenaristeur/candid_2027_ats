# Candidats 2027 — le site de l’album

Site de présentation, d’écoute et de contribution pour l’album **Candidats 2027** :
31 chansons, une par candidat à la présidentielle, avec les paroles, les fiches
techniques et les sessions Ableton à télécharger.

- Site publié : <https://scenaristeur.github.io/candid_2027_ats/>
- Dépôt : <https://github.com/scenaristeur/candid_2027_ats>

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
│   └── markdown.py         # rendu Markdown minimal, sans dépendance
├── site/
│   ├── assets/style.css    # feuille de style source
│   ├── assets/app.js       # recherche, filtres, thème
│   ├── assets/favicon.svg
│   └── audio/              # optionnel : 01.mp3, 02.mp3… pour un lecteur
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

## Ajouter un lecteur audio (optionnel)

Déposer un fichier `site/audio/09.mp3` (ou `.ogg`, `.m4a`, `.wav`) puis
régénérer : un lecteur apparaît sur la page du titre 09. Aucun autre réglage
n’est nécessaire.

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
