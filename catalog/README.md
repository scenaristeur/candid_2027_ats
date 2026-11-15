# Catalogue des productions

Ce dossier est généré par `scripts/build_catalog.py`.

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
