# Catalogue des productions

**Date de première passe** : 2026-11-15  
**Branche** : `plateforme-productions`  
**Portée** : toutes les productions repérées dans les sources éditoriales, les projets Ableton Live et les exports audio/MIDI.

## Page publique

`docs/catalogue.html` est générée par `scripts/build_catalogue.py`. Elle charge
`productions.json`, affiche les statistiques, une recherche, un filtre par album
et par statut, et renvoie vers les pages Candidats 2027 ou vers les pages de
production.

Chaque production documentée ou session ALS a une page
`docs/productions/<id>.html` générée par `scripts/build_productions.py`, avec :

- les documents sources copiés dans `docs/telechargements/productions/<id>/documents/` ;
- les sessions ALS copiées et nettoyées dans `.../als/` ;
- les exports MP3/MIDI publiés sur Archive.org, via `site/media_productions.json`.

## Arborescences lues

Les chemins du catalogue sont **logiques**, pas absolus :

| Préfixe | Emplacement réel |
| :--- | :--- |
| `sources/` | `C:\Users\admin\dev\ableton-holland-mcp\sources` |
| `Ableton Live/` | `C:\Users\admin\Music\Ableton Live` |
| `exports ableton/` | `C:\Users\admin\Music\exports ableton` |

Les trois dossiers sont lus en **lecture seule**. Les scripts n’écrivent que dans
`catalog/` et `docs/`.

## Fichiers

- `PRODUCTIONS.md` : vue lisible, groupée par album. Les productions documentées sont détaillées ; les sessions sans fiche sont résumées par album.
- `productions.csv` : une ligne par production, avec tous les champs (Excel compatible, UTF-8 BOM).
- `productions.json` : version structurée, prévue pour alimenter la plateforme.
- `als_versions.csv` : chaque session `.als` principale (hors `Backup`), tempo, pistes, clips, date.
- `exports.csv` : chaque export MP3/WAV/MIDI, taille, date, chemin logique.
- `README.md` : ce document (méthode et limites). Il n’est pas écrasé par le build.

## Méthode

### 1. Sources éditoriales

Le script repère les dossiers de production qui contiennent :

- une fiche technique, des paroles, un statut, une structure ou un clip ;
- ou un document dont le nom correspond au dossier ;
- ou un dossier terminal contenant des documents.

Il extrait ensuite :

- le titre et, pour Candidats 2027, le candidat ;
- les documents présents (fiche, paroles, notes) ;
- le tempo, la tonalité, la signature, la durée cible, le style, l’atmosphère ;
- le statut indiqué dans la fiche ;
- les objectifs de la section « Ce que la chanson doit faire » ;
- le mode des paroles : complètes, refrain seul ou absentes.

Les doublons de casing/accents sont fusionnés (ex. `Lumiere` / `Lumière`).

### 2. Sessions Ableton

Chaque `.als` **hors dossier `Backup`** est inventorié. Le contenu est
décompressé (gzip + XML) pour extraire :

- le tempo manuel ;
- le nombre de pistes MIDI et audio ;
- le nombre de clips ;
- les noms de pistes ;
- la date de modification et la taille.

Un cache dans `catalog/.cache/als.json` accélère les relances. Il est ignoré par
Git.

### 3. Exports

Les fichiers `.mp3`, `.wav`, `.mid`, `.midi` et `.flac` sont inventoriés. Les
fichiers `.asd` sont ignorés.

### 4. Rapprochement

Le rapprochement est heuristique et **global** :

- chaque session et chaque export est affecté à la production source la plus
  proche, afin qu’une session ne soit pas comptée deux fois ;
- normalisation des titres (accents, `Copie`, `opencode`, `review`, `refactor`,
  `voix`, etc.) ;
- suppression des suffixes de version et des nombres de piste en tête ;
- comparaison par mots, sous-chaîne encadrée et similarité floue ;
- correspondance d’album avec quelques alias (`Mascu` → `Masculinisme`,
  `Melody_Where_are_you` → `Melody, Where are you`,
  `Candid_2027_ats` → `Candidats 2027`, etc.) ;
- pour un album à une seule production, rattachement des sessions restées
  orphelines de cet album.

## Confiance du rattachement

- **élevée** : titre très proche, album cohérent, souvent numéro identique.
- **moyenne** : recouvrement partiel ou album cohérent sans titre exact.
- **faible** : rattachement par album, par défaut, ou à vérifier manuellement.
- **sans objet** : aucune session/export à rattacher (documentation seule,
  session seule, etc.).

Les lignes `faible` sont listées dans la section « Rapprochements à vérifier »
de `PRODUCTIONS.md`.

## Statuts

- **maquette exportée** : documents + session Ableton + export audio.
- **maquette Ableton** : documents + session Ableton, sans export audio.
- **export + session** : session et audio, sans fiche source.
- **documentation seule** : fiche/paroles, pas encore de session.
- **session seule** : `.als` sans fiche source.
- **export seul** : MP3/WAV/MIDI sans fiche ni session identifiée.
- **à identifier** : aucun élément exploitable.

## Limites connues

1. Le catalogue ALS-only regroupe les versions par **nom de fichier exact**.
   Plusieurs versions d’un même morceau peuvent donc apparaître sur des lignes
   différentes ; `als_versions.csv` permet de les retrouver.
2. Certains projets Ableton n’ont pas de dossier source : ils restent en
   « session seule ».
3. Les MIDI ne sont comptés que s’ils sont dans `exports ableton` ; les `.mid`
   posés à la racine d’Ableton Live ne sont pas encore scannés.
4. La tonalité vient des fiches ; l’information de gamme des `.als` est souvent
   laissée à sa valeur par défaut et n’est pas fiable.
5. Les rapprochements `faible` doivent être relus ; les alias d’albums peuvent
   être complétés dans `scripts/build_catalog.py`.
6. Les exports peuvent exister en plusieurs versions (voix, instru, mix) ; la
   ligne production indique une version principale, `exports.csv` garde toutes
   les versions.

## Prochaines étapes

1. Relire les quelques lignes `faible` et corriger les alias/rapprochements.
2. Regrouper les versions d’un même morceau en une production + N versions.
3. Ajouter les MIDI présents dans les dossiers Ableton.
4. Ajouter un champ « album éditorial » et un statut de validation musicale.
5. Générer une page par production à partir de `productions.json`.
6. Faire de Candidats 2027 le premier **événement** d’une plateforme multi-albums.

## Régénérer

```powershell
python scripts/build_catalog.py
python scripts/build_site.py
python scripts/build_catalogue.py
python scripts/check_site.py
```

Options :

```powershell
python scripts/build_catalog.py `
  --sources "D:\chemin\sources" `
  --als "D:\chemin\Ableton Live" `
  --exports "D:\chemin\exports ableton"
```
