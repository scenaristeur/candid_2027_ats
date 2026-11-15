# 03 — Skank : 6 candidats en audition

## Pourquoi 6 guitares d'un coup

David a demandé une guitare donnant un **effet de « révolte douce »**, cohérent avec les paroles
(déchets sauvages, Monnaie Sauvage). Une piste ne suffisait pas à trancher : on a donc mont�� un
dispositif d'audition.

**Contrainte de budget : 8 pistes max.** Le calcul tombe juste :

```
2 pistes (batterie + basse) + 6 guitares = 8
```

Pour faire la place, les deux basses perdantes ont été supprimées (`Dub Techno`, `Analog`).
`Deep Chill` est conservée — elle porte la « vague » validée.

## La partie écrite

**Identique sur les 6 pistes.** Seul le son change. C'est la condition pour que l'audition soit
honnête : on compare des timbres, pas des presets bruts.

### Rythme — skank sur les contretemps, avec des trous

6 frappes en croches sur 8 temps, durée **0,3 temps** (accord très court, étouffé) :

| Contretemps | 0,5 | 1,5 | 2,5 | 3,5 | 4,5 | 5,5 | 6,5 | 7,5 |
|---|---|---|---|---|---|---|---|---|
| Frappe | ✓ | ✓ | **silence** | ✓ | ✓ | ✓ | **silence** | ✓ |

**Les trous aux contretemps 2,5 et 6,5 sont délibérés.** Ce sont les deux « and » qui suivent les
coups de grosse caisse + caisse claire (temps 2 et 6). Laisser ces deux endroits vides donne au
one-drop de l'air pour respirer — sans quoi la guitare recouvre le drop et on retombe dans le
« tic-tac » que David avait déjà fait relever sur la basse.

### Accords

| Temps | Accord | Notes (Ableton, C3 = 60) |
|---|---|---|
| 0,5 / 1,5 / 3,5 | **Do#m + si bémol 2** | 61, **62**, 64, 68 |
| 4,5 / 5,5 / 7,5 | **Labmaj (bVII)** | 68, 72, 75 |

- **Le 62 (Ré naturel) est la décision musicale centrale.** C'est le b2 contre le Do#. Il fait
  deux choses à la fois : il donne la **couleur phrygienne** — méditerranéenne, occitane — et c'est
  un intervalle **dissonant et tendu** qui pousse contre l'accord sans jamais crier. C'est ça, la
  « révolte contenue ».
- Il n'est posé **que** sur l'accord de Do#. L'accord de Lab reste pur et flottant : le contraste
  entre les deux est voulu.
- Le 68 (Sol#/Lab) est commun aux deux accords — les voix glissent au lieu de sauter.

### Vélocités — la phrase qui monte

| Frappe | 0,5 | 1,5 | 3,5 | 4,5 | 5,5 | 7,5 |
|---|---|---|---|---|---|---|
| Vélocité | 96 | 88 | 100 | 92 | 86 | **110** |

Le 110 sur le dernier contretemps est la « phrase tirée vers le haut » qui lance le retour du
groove.

> ⚠️ **Limite assumée** : ce « tirée vers le haut » est fait en **vélocité**, pas en bend de hauteur.
> Live n'a pas d'export de pitch bend par note dans les outils MCP. Si tu veux un bend réel, il
> faudra le poser à la main dans l'UI sur le dernier accord.

## Les 6 candidats

| # | Piste | Son | URI | Intention |
|---|---|---|---|---|
| 3 | `Guitar Electric Clean` | guitare électrique propre | `query:Sounds#Guitar%20&%20Plucked:FileId_5053` | *révolte douce* — la piste de référence, la plus proche du brief |
| 4 | `Chord Key Stabs` | accords stabs | `query:Sounds#Guitar%20&%20Plucked:FileId_4780` | plus de mordant |
| 5 | `Chord Dub Pluck` | pluck avec ping-pong **intégré** | `query:Sounds#Guitar%20&%20Plucked:FileId_4779` | couleur dub ⚠️ voir ci-dessous |
| 6 | `Synergy Pluck Brass` | cuivres | `query:Sounds#Brass:FileId_10027` | les cuivres en contestation |
| 7 | `Organ Klick` | orgue percussif | `query:Sounds#Piano%20&%20Keys:FileId_4868` | **A** — le skank sans guitare (roots) |
| 8 | `Surge XT` | `Overdriven Guitar` | `query:Plugins#VST3:Surge%20Synth%20Team:Surge%20XT` | **B** — le skank brûlé, l'opposé de « douce » |

**Les deux pistes « très différentes »** demandées en complément du brief « révolte douce » :

- **A — l'organe.** Le skank sans guitare : pas d'attaque de médiator, un accord tenu qui *pousse*
  sous le chant au lieu de le ponctuer. Voix canonique du roots reggay, antérieure à l arrivals de
  la guitare. Change la grammaire, pas seulement la couleur.
- **B — le skank brûlé.** Même source, saturée jusqu'au mur, decay court, aucune retenue. Plus de
  nuance du tout. Teste l'autre bout de l'axe.

**Écarté : `Guitar Electric Muted`.** Le skank mute est déjà étouffé dans le son lui-même : il n'y a
plus rien à retenir, donc plus rien à contenir. Il jouerait la prudent-par-défaut — exactement
l'opposé de la « révolte douce » demandée.

## ⚠️ Piège connu sur la piste 5

`Chord Dub Pluck` **embarque un delay ping-pong** dans le preset. Il se battra avec le `MDelay`
posé sur la batterie. **Si cette piste est retenue, couper son delay interne** avant tout jugement
définitif.

## Surge XT

- Instance **0** — c'est la seule. L'OSC répond.
- Patch : `Overdriven Guitar` (LinnStrument MPE).
- Chemin : `patches_3rdparty\LinnStrument MPE\Guitars\Overdriven Guitar`
- Chargé avec `load_instrument_or_effect`. **`load_external_plugin` ne fonctionne pas** : il ne
  cherche que dans `plugins/VST3/<nom>` sans Fabricant, et Surge est sous
  `VST3/Surge Synth Team/Surge XT`. Voir `doc_surge/surge_OSC.md`.
- ⚠️ **Charger un patch Surge reclasse son architecture** (oscillateurs, filtre, FX). Il faut
  re-approuver les mutes après chaque rechargement. Voir skill `remake-midi`.

## Chaînes FX des guitares — NON POSÉES

Rien n'est encore traité sur les 6 pistes guitares. Principe acté : **chaîne de même forme,
calibrage individuel** — `Compressor` (serré, pour l'attaque) → `MEqualizer` (creux sous ~250 Hz
pour dégager la grosse caisse, présence 2–3 kHz) → petit send Reverb.

Non fait volontairement : on ne bride pas le skank avant d'avoir trouvé le bon son. Brider six
sons qu'on n'a pas encore choisis serait du travail perdu.

## Ce qu'il faut écouter

1. **Le b2 pique ou il gêne ?** C'est le point le plus risqué de la partie. S'il fait « faux »
   plutôt que « tendu », on le retire et on revient à une quinte.
2. **Les trous aux contretemps 2,5 et 6,5 sont-ils suffisants ?** Si la grosse caisse reste
   couverte, on allonge les trous.
3. **La guitare reste-t-elle sous la caisse claire ?** Elle ne doit jamais la dépasser.
4. **La couleur phrygienne est-elle occitane, ou simplement dissonante ?** Si c'est la seconde,
   le b2 sort.