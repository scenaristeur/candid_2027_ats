# Catalogue des productions

Ce dossier est généré par `scripts/build_catalog.py`.

## Page publique

`docs/catalogue.html` est générée par `scripts/build_catalogue.py`. Elle charge
`productions.json`, affiche les statistiques, une recherche, un filtre par album
et par statut, et renvoie vers les pages Candidats 2027 lorsqu’elles existent.

## Fichiers

- `PRODUCTIONS.md` : vue lisible, groupée par album.
- `productions.csv` : une ligne par production.
- `productions.json` : données structurées pour un futur site.
- `als_versions.csv` : inventaire des sessions `.als` principales.
- `exports.csv` : inventaire des exports audio/MIDI.

## Régénérer

```powershell
python scripts/build_catalog.py
```

Les sources sont lues en lecture seule. Seul `catalog/` est écrit.
