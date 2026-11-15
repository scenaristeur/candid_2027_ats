# Fiche technique — In the Flesh (Pink Floyd) [remake]

Source : `In the Flesh/Pink Floyd — In the Flesh [MIDIfind.com].mid`
Tempo : 76 BPM | **Signature : 12/8 puis 6/8 (mètre complexe !)** | Durée : ~3.9 min | 74 bars
Fusion : 3 pistes guitares uniquement (pas de drums/basse dans le .mid).

## Pistes (indices 0-based)

| Ableton | Instrument proposé | Source |
|---|---|---|
| 0 | 1-Basse (ajoutée) | (à créer — pas de basse source) |
| 1 | 2-Guit1 (overdrive) | Guitar 1 (prog 29) |
| 2 | 3-Guit2 (overdrive) | Guitar 2 (prog 29) |
| 3 | 4-Guit3 (clean) | Guitar 3 (prog 27) |
| 4 | 5-Libre | — |
| 5 | 6-Libre | — |
| 6 | 7-GuideVocal | (à créer — pas de voie source) |
| 7 | 8-Voix (audio) | ta voix |

## Scènes (temporaire)

| Scène | Bars | Beats |
|---|---|---|
| 0 | 1–20 | 80 |
| 1 | 21–44 | 96 |
| 2 | 45–74 | 120 |

## Options / forks (TODOs)
- [ ] **Mètre 12/8-6/8** : TRÈS IMPORTANT — régler le mètre de la session Ableton sur 12/8 (et gérer le
  6/8) sinon l'alignement sera faux. Vérifier `set_signature`. C'est un morceau à mètre complexe.
- [ ] **Pas de drums/basse/vocals dans le .mid** : ce sont de purs pads de guitares. Pour un "remake
      complet" il faudra AJOUTER basse + batterie (maison) + éventuellement la voix. C'est plus un
      matériau à "re-composer" qu'à "réarranger".
- [ ] **Guitares** : 2x overdrive (disto) + 1 clean. Charger overdrive (use disto/Amp), clean
      (Electric Clean). Alternates : Axe Of Velvet, Tube Lead Pluck.
- [ ] **Ambiance** : In the Flesh (The Wall) = marche militaire/lourde, mètre 6/8 = 12/8. Donner une
      "pêche" martiale + orchestrale serait cohérent (surge brass/pads).
- [ ] **Ajouter basse + batterie** : à écrire (build de groove) — c'est un chantier de composition,
      pas juste de réarrangement.
- [ ] **CPU** : léger (3 puis ~7 pistes) — ok.

## Note générale
Ce morceau est le **plus "matériau brut"** des 4 : pas de rythme ni de voix. C'est un vrai projet
de (re)composition sur des guitares. À traiter seulement si tu veux un gros chantier créatif.
Autres morceaux (Breathe, Money, Time) sont plus "clé en main" pour un remake immédiat.

## À faire
- [ ] Écouter/valider mètre + scènes
- [ ] Décider : réarranger tel quel vs re-composer (ajouter rythmique)

## Outils
notes : `_scenes_notes.json` | prep : `prep_midi.py` / `prep_anycolour_group.py`
