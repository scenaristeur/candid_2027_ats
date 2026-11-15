# MadMax 2308 — TODO technique

Points mis de côté pendant la construction, à traiter **après l'arrangement**.

## À faire après l'arrangement

- [ ] **Pad secondaire — filtre qui s'ouvre en section B.** Le document demande une ouverture
      progressive du filtre pendant toute la section B. Les enveloppes de clip créées par script
      ne s'appliquent pas dans ce build (vérifié 3 fois : une enveloppe à 0 ne coupe pas le son,
      le fader reste à 0,85 pendant la lecture). → à faire en **automation d'arrangement**.

- [ ] **Sidechain kick → pad.** Le Compressor est en place sur `2-Pad Principal` (`S/C On` actif,
      Threshold/Ratio/Release réglés) mais **la source du sidechain n'est pas exposée par l'API** :
      `S/C Listen` renvoie le pad au lieu du kick, donc la clé n'arrive pas. Le Remote Script ne
      sait régler que l'entrée de piste, pas le sélecteur S/C du device.
      → soit David choisit `6-Percussion | Post FX` à la main dans le panneau S/C (un clic),
      soit on remplace par un Auto Pan synchronisé.

- [ ] **Coupe EQ sur la piste percussion.** Le kick feutré du `Recording Hybrid Kit` garde un clic
      d'attaque (6,7 % d'énergie entre 2,5 et 5 kHz) que le filtre du pad n'enlève pas.
      → MEqualizer, coupe dans le haut du kick, au moment du mix.

- [ ] **Master complet.** Un limiteur de sécurité est posé (plafond 0,95, lookahead actif) pour
      éviter l'écrêtage pendant la construction. Il manque la chaîne définitive :
      compresseur de colle puis limiteur final. Fader master à 0,85.

- [ ] **Lookahead du limiteur.** Ce build n'expose le paramètre qu'en **tout ou rien** (0 ou 1),
      pas en millisecondes : impossible de régler les 3 ms demandés par la fiche master.

- [ ] **Fiche technique du morceau** (`FICHE_TECHNIQUE.md`) : patchs retenus, réglages sculptés,
      grilles, tempi, décisions — à écrire une fois les sections figées.

## Patchs encore à choisir

- [ ] **Contre-chant (piste 5, Rhen)** — entre en section C en contrepoint, décalé d'un temps.
      Le document veut un wavetable métallique + filtre bandpass. **Audition mesurée à faire.**
      ⚠️ État actuel : cette piste porte une **copie du patch de mélodie** (elle sert à la ligne
      en Ré# de la section D). Elle n'a donc pas encore sa propre identité de timbre, et en
      section C le contre-chant n'est pas écrit.
- [ ] **8-Fork (piste 7)** — le second monde de la section D, en Ré# (triton). À auditionner.

## Incohérence du document

- [ ] Le pitch parle de **Naya Kerr**, les sections d'**Elia** et **Rhen**. Non tranché.
