# 04 — Une guitare, trois personnages

## Décision

`Synergy Pluck Brass` (l'ancienne piste 5, `query:Sounds#Brass:FileId_10027`) est **retenue comme
source unique**. Les trois autres guitares ont été **supprimées**.

**Pourquoi Synergy** : c'est la seule des trois à avoir une **attaque de médiator**. Une attaque
permet d'aller *vers* le plus brillant (cuivres) comme *vers* plus sourd et plus tenu (orgue, pluck
dub). Un orgue, lui, n'a pas d'attaque — il monte vers les cuivres beaucoup moins naturellement.

Les deux autres pistes libérées ne sont pas perdues : leurs **caractères sont obtenus par
automation** sur la piste Synergy. Voir la table plus bas.

**Contrainte résolue** : les enveloppes d'automation sont **portées par le clip**. Déclencher le
clip « Refrain » donne automatiquement le caractère cuivres ; le clip « Couplet » donne l'orgue.
Pas d'automation à retoucher à chaque section.

---

## ⚠️ État des connaissances — à lire avant d'utiliser ces recettes

**Aucune de ces guitares n'a été mesurée.** Elles ont été proposées, chargées, écrites dans un clip
skank identique, puis écoutées et jugées à l'oreille par David — **sans aucun effet, sans aucune
capture, sans aucune analyse**.

La seule donnée dure obtenue sur ce lot est **négative** : `Chord Key Stabs` **saturait le CPU**
(c'était un `InstrumentGroupDevice`, donc un rack à voix multiples).

**Conséquence** : les descriptions ci-dessous sont des **intentions musicales**, pas des mesures.
Elles disent « vers quoi on vise », pas « ce que la piste faisait exactement ». Si tu veux les
vraies valeurs d'origine, il faut recharger le preset et le mesurer — les `.adg` sont toujours dans
le browser.

---

## Les recettes : comment `Synergy` se rapproche de chaque personnage

Toutes se font sur la chaîne **`Compressor` → `MEqualizer` → sends**, posée sur la piste Synergy.

### → vers l'orgue *(ex-Organ Klick)* — couleur des couplets

| Coupure | Effet |
|---|---|
| MEqualizer bande 6 (~4 kHz) | **Bas** — c'est ce qui tue l'attaque du médiator. Un orgue n'a pas d'attaque, il a une attaque de tuyau |
| MEqualizer bande 2 (~145 Hz) | Bas — débourrer le bas |
| MEqualizer bande 4 (~1 kHz) | **Haut** — le corps de l'orgue est entre 800 Hz et 2 kHz. C'est LA bande à remonter |
| Send Reverb (return A) | **Fort** — la tenue vient surtout de là |
| Compressor | Ratio bas, attaque plus lente — lisse au lieu de percussif |
| *(option)* | un `Chorus` en insert pour le scintillement d'orgue |

### → vers le pluck dub *(ex-Chord Dub Pluck)* — couleur du pont

| Coupure | Effet |
|---|---|
| MEqualizer bande 5 (~2,8 kHz) | Bas |
| MEqualizer bande 6 (~4 kHz) | **Bas franchement** — c'est ce qui fait le dub sombre |
| MEqualizer bande 3 (~390 Hz) | **Haut** — chaleur |
| **Send return B (delay)** | **Monté** — c'est l'écho dub. Voilà à quoi le return B était réservé depuis le début |
| Send Reverb (return A) | Bas — plus sec |

> La piste d'origine embarquait son propre ping-pong ; il aurait faut le couper avant tout
> jugement. Ici on n'a pas ce problème : le retour d'écho vient du return B, sous contrôle.

### → vers la guitare propre *(ex-Guitar Electric Clean)* — couleur claire

| Coupure | Effet |
|---|---|
| MEqualizer bande 6 | **Haut** — rendre l'attaque et le claquement |
| MEqualizer bande 1 (~120 Hz) | Neutre ou légèrement haut — le corps de la guitare électrique |
| Compressor | Attaque **rapide**, ratio plus haut — le « clac » |
| Send Reverb | Modéré, plutôt court |

### → vers le skank brûlé *(ex-Surge XT Overdriven Guitar)* — couleur agressive

David avait jugé ce son « vraiment trop fou », donc il ne sert pas de cible. **Mais la recette
sert quand même**, pour un pont plus saturé si besoin :

| Coupure | Effet |
|---|---|
| Compressor | Seuil **très bas**, ratio **très haut** — écraser jusqu'à plus aucune dynamique |
| *(insert)* | ajouter un `Saturator` ou un `Overdrive` — Synergy n'en a aucun aujourd'hui |
| Send Reverb | Bas |

---

## Le plan de sections

| Section | Personnage | Couleurs du texte |
|---|---|---|
| Couplet 1 | orgue | « Sous le soleil qui brûle les cailloux » |
| Refrain | cuivres | « De tes déchets, on fait des beautés » |
| Couplet 2 | orgue | « À Aix, dans un atelier qui bourdonne » |
| Pont | pluck dub | « Et si tu ramasses avec nous » |
| Couplet 3 | cuivres (plus ouverts) | « Six cent trente mille tonnes » |
| Refrain final | cuivres, plein | « Le plastique devient monnaie » |
| Outro | fondu vers l'orgue | « Ramasser, c'est déjà aimer » |

## ⚠️ Séquence retenue : le guide vocal AVANT l'automation

David a validé cet ordre le 2026-10-04, contre-intuitif mais juste : **ce qui doit décider quand la
guitare change d'humeur, c'est ce que fait la voix.** Écrire l'automation d'abord obligerait à
recaler les transitions dès que le chant serait posé, parce que le refrain n'entre pas forcément où
on l'avait prévu.

Le guide vocal se fait sur **`Surge XT` (instance 0)**, choisi pour ça : un chant guide doit être
brut et sans prétention, « trop fou » est exactement la bonne qualité ici.

## Fautes à éviter

- **Ne pas confondre l'index Live et l'index MCP.** Live affiche 1-based (« 3-Synergy »), les
  outils MCP sont 0-based. Après les suppressions : Live « 4-Surge XT » = MCP index 3.
- **Toujours vérifier `get_cpu_report` avant de viser un index**, les suppressions décalent tout.
- Un rack du browser peut être bien plus gourmand qu'un preset une voix. Mesurer avant d'empiler.
