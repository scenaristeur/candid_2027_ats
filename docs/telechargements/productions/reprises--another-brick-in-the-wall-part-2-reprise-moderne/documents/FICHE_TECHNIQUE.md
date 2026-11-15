# FICHE_TECHNIQUE — Another Brick in the Wall (Part 2) — Reprise moderne

Session Ableton Live (Live Lite) · Tempo 120 BPM · Signature 4/4 · Tonalité Ré mineur (Dm)
Session View : 15 scènes (slots 0-14), clips MIDI de 32 beats (8 mesures) sauf Solo (120 beats = 30 mesures).

## Structure de la chanson (slots / scènes)

| Slot | Scène | Mesures | Accord | Contenu |
|------|-------|---------|--------|---------|
| 0 | Intro | 8 | Dm | Basse seule, groove aéré + touches G8 |
| 1 | Couplet 1 | 32 | Dm | Couplet aire — basse « Waters » + groove, arp de fin |
| 2 | Pre-Chorus 1 | 32 | G (pédale) | « Hey teacher » — basse pédale G + stabs + tremolo fills |
| 3 | Chorus 1 | 32 | **F→Dm→F→Dm** | « All in all » — alternance 2 mesures/2 mesures |
| 4 | Verse 2 | 32 | Dm | Couplet 2 (variante, basse allégée, arp fin) |
| 5 | Pre-Chorus 2 | 32 | G (pédale) | Montée (barrés G→Gmaj→A→B...) |
| 6 | Chorus 2 | 32 | **F→Dm→F→Dm** | Chorus 2 pleine puissance |
| 7 | **SOLO** | **30 mesures** | Dm | Solo Gilmour — piste 6 (Moogy Saw + Delay) |
| 8 | Outro | 32 | Dm | « Wrong, do it again » — épuré, G8 « SeaGull » en notes tenues |
| 9-14 | à définir | 32 | — | variations / ponts / outro longue |

## Principes directeurs (décisions validées)

1. **Piste 8 guitare (G8 / 8 guitare 8 = Overdriven Guitar) = touches ponctuelles** dès l'intro,
   jamais continue. Petites touches bien placées (stabs d'accords aux changements de section,
   pickups, fins de phrases). Au Chorus, transposée F/Dm. À l'Outro : **notes tenues « SeaGull »**
   (s'installe, s'efface parfois, revient = grande tenue 3-4 beats ol-Breathe, puis phrases).
2. **Changement d'accords au Chorus = outil de mouvement** : l'original alterne F (2 mes) /
   Dm (2 mes). On réutilise ce système à chaque fin de section ou pour créer des variantes
   (ex. montée Pre-Chorus : G → A → B, transitions C→G, F→C→G dans les arpèges).
3. **Basse = toujours en mouvement**, elle « s'installe » : depuis une racine tenue,
   elle ajoute progresyl pulse (octaves, pickups C→D, accès A), puis groove complet.
   Elle doit nous faire groover. Basses : Sub Square (Surge inst 0).
4. **Solo sur la piste dédiée « 7 guitare 3 Solo »** (Surge Moogy Saw inst 4 + Delay),
   30 mesures, pentatonique D avec montées vers A5 (F5→G5→A5), phrases 4-mesures,
   respirations, tenue finale sur E-D. Pas sur la G8.

## Tracking (0-based) — pistes session

| Index | Piste | Source | Rôle |
|-------|-------|--------|------|
| 0 | 1-Bass | Surge « Sub Square » (inst 0) | Basse groove |
| 1 | 2-Pads | Surge « MKS-70 Warm Pad » (inst 1) | Nappes / accords riches |
| 2 | 3-Guitar | Surge (inst 2) | Guitare rythmique / powerchords |
| 3 | 4-Drums | Drum Rack Core Kit | Batterie (dup au besoin) |
| 4 | 5-Tambourine | Percussion Core Kit | Tamb (note 48) / Tamb Shake (49), 8ths |
| 5 | 6 Guitare 2 | Surge (inst 3) | Fills : tremolo + arpèges |
| 6 | 7 guitare 3 Solo | Surge « Moogy Saw » (inst 4) + Delay | **LE SOLO (30 mesures)** |
| 7 | 8 guitare 8 | Surge « Overdriven Guitar » (inst 5) | Touches ponctuelles / tenues Outro |

## Accords (pitch mapping MIDI)

- Dm9 : 38/45/50/57/62/65
- F add9 : 41/48/53/57/60/65
- G : 43/55/62/67 (ou G5 43/55/62 / power 55/62)
- C : 48/55/60
- Bass : 26=D1, 29=F1, 31=G1, 33=A1, 36=C2, 38=D2, 41=F2, 43=G2
- Lead solo : 60=C4, 62=D4, 65=F4, 67=G4, 69=A4, 72=C5, 74=D5, 77=F5, 79=G5, 81=A5

## Batterie (Drum Rack)

- Kick 36, Snare 38, Closed Hat 42. Open Hats 46 disco sur 8ths aux couplets.
- Duplication des slots (Couplet→Verse2, PreChorus→PreChorus2, Chorus→Chorus2, Couplet→Solo/Outro).

## Paramètres clés

- Volume retour delay solo : Dry/Wet 0.25, Feedback 0.40, Delay synced (L16 dotted 8 sur 120 BPM).
- À viser (fétiche Gilmour) : Delay ~440 ms, feedback 2-3 répétitions distinctes, mix ~20-25%.
- Solo poly réglé 16 voix (limité polyphony_limit), jeu saw lead.
- Master : à finaliser (limiter ~ -1 dB, centroid cible 700-900 Hz fin).