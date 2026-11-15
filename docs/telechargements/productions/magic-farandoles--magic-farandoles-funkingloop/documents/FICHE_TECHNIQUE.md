# Fiche Technique — Magic Farandoles / FunkingLoop

> Session Ableton Live — MCP (Ableton Holland MCP)
> Tempo : **70 BPM** — Signature : **4/4** — Tonalité : **E minor** (Em7)
> Durée totale programmée : montée (scènes 1-6) → Scène 7 (64 mesures = 256 beats) → Scène 8 (64 mesures = 256 beats) → redescente (scènes 6 → 1) → intro/outro.

---

## 1. Concept artistique

Une **farandole magique** : chacun des 7 instruments devient un animal qui participe à une euphorie théâtrale grandissante. Le morceau est une **odyssée** qui s'élève par paliers (scènes), atteint ses deux apogées (scènes 7 et 8), puis **redescend** par les scènes 6 → 1 pour se refermer sur l'intro (boucle).

Structure narrative :
- **Intro / départ** : scènes 1-6 = montée musicale progressive (duo + instruments qui s'ajoutent).
- **Première envolée** : Scène 7 = 64 mesures d'enchevêtrement phantasmagorique des deux voix, suivies par les instruments → **climax 1**.
- **Deuxième envolée** : Scène 8 = 64 nouvelles mesures, chaque instrument affirme son identité animale → **climax 2** (plus haut).
- **Coda / redescente** : arrangement redescendant des scènes 6 → 1, retour à l'intro/outro.

---

## 2. Pistes et rôles (7 instruments = 7 animaux)

| Piste (0-based) | Instrument | Animal | Rôle dans l'odyssée |
|---|---|---|---|
| 0 | Watcher Kit | Le pas de la farandole | Percussions/drums ; kick 4-on-floor qui pousse, snare temps 2&4, hats syncopés, crash au climax |
| 1 | Grand Piano | L'écureuil | Moteur harmonique et figure syncopée/sautillante (arpèges brisés) ; soutient le duo |
| 2 | Pad 1 (Analog Lab V) | L'ours | Nappes graves tenues, respirations profondes ; fondation harmonique |
| 3 | Pad 2 (Analog Lab V, renommé) | Le dauphin | Nappes aiguës qui jaillissent puis retombent ; contre-chant des nappes |
| 4 | strange (Surge XT) | La baleine | Texture aérienne lointaine, sons suspendus rares et longs dans les aigus |
| 5 | vox (Surge XT, vocal17) | L'alouette | Voix lead soprano — mélismes, notes tenues qui s'élèvent |
| 6 | 7-Voicelike Pad | L'hirondelle | Voix harmonie — contrepoint en doubles-croches, croise la lead, imitation |

Résumé des rôles par famille :
- **Voix (foyer)** : track 5 (lead) + track 6 (harmonie) — contrepoint à 2 lignes indépendantes.
- **Harmonie** : Grand Piano (écureuil) + Pad 1 (ours) + Pad 2 (dauphin).
- **Espace** : strange (baleine).
- **Rythme / énergie** : Watcher Kit (moteur de la farandole).

---

## 3. Voix — contrepoint à 2 voix (tracks 5 & 6)

- **Lead (Alouette)** : ligne mélodique avec **notes tenues langoureuses** (durées 1.5-2.5 beats) et **mélismes** ; monte progressivement de registre jusqu'au sommet (pitch 86-90, zone C#6) à la fin.
- **Harmonie (Hirondelle)** : **sillons en doubles-croches** (durée 0.25) ; **imitation** de la lead en décalage ; **croisements de registre** (quand la lead est haute, l'harmonie passe en aigu et inversement).
- Principe : **contrepoint authentique** — deux lignes indépendantes qui dialoguent, PAS d'harmonie parallèle synchrone. Quand une voix tient, l'autre anime.
- Vélocités expressives (90 → 127 au climax), jamais uniformes.

### Surge XT — réglages vox (instance 1) validés
- Oscillateur : **Wavetable** (type 2) — wavetable vocale « vocal17 » (3rd party / layzer).
- 3 oscillateurs superposés (3 wavetables vocales, accordés, faibles désaccords).
- **Ring modulators : mutés** (étaient la cause du timbre métallique).
- Filtre : **Lowpass** (était « FX Comb + », responsable de la nasillardité) + voyelles ouvertes (morph).
- Play mode : **Mono legato**. **Polyphonie limit : 2 voix** (gestion CPU).
- Vibrato vocal sinusoidal, morph piloté par keytrack (la voyelle suit la hauteur), random par note pour la variation organique.

### Voicelike Pad (track 6)
- Rack Instrument Wavetable + Chorus-Ensemble + Reverb — voix d'origine analysée.

---

## 4. Scènes et structure

Les clips 64 mesures font **256 beats** à 70 BPM (≈ 3 min 40 s chacun).

### Scène 7 (clip_index 6) — première envolée, climax 1
- **Duo vocal** : 256 beats complets, lead soprano montant jusqu'au sommet C#6 (pitch 88), harmonie en contre-chant.
- **Grand Piano** : accompagnement Em → C → G → D (mesures 1-16).
- **Pads (ours + dauphin)** : nappes qui épaississent (mesures 17-64).
- **strange (baleine)** : notes aériennes suspendues vers le climax.
- **Watcher Kit** : percussion qui entre aux mesures 33, 4-on-floor + crash au climax (mesures 49-64).

### Scène 8 (clip_index 7) — deuxième envolée, climax 2 (plus haut)
- **Duo vocal en contrepoint** renforcé (sillons, croisements, imitation).
- **Tous les instruments affirment leur animal** et participent dès les mesures 17-32, densité croissante, **euphorie finale** mesures 49-64 (vélocités maximum, lead au sommet).

---

## 5. Harmonie (E minor)

Progression cyclique : **Em → C → G → D**, chaque accord sur 4-8 beats selon la section.
- Em : E-G-B ; C : C-E-G ; G : G-B-D ; D : D-F#-A.
- Le piano et les pads posent les fondations ; la voix orne au-dessus (notes de passage, appoggiatures) en retombant sur les notes des accords.

---

## 6. Arrangement (TERMINÉ)

L'arrangement est **déployé** : longueur totale **764 beats** (~191 mesures), boucle désactivée.

**Structure effective sur la timeline (exemple piste vox / Voicelike) :**
| Beats | Contenu |
|---|---|
| 0-80 | Montée (scènes 1-6) |
| 80-96 | Clip 8 beats |
| 96-352 | **Scène 7** — 256 beats (climax 1) |
| 352-608 | **Scène 8** — 256 beats (climax 2) |
| 608-624 | Clip 8 beats |
| 624-764 | Redescente (scènes 6 → 1) + outro (~140 beats) |

**CPU en lecture : ~33% moy / 40% pic — stable.**

> Règles MCP rappel : indices 0-based en interne, 1-based côté utilisateur. Scène 7 = clip index 6, Scène 8 = clip index 7.

---

## 7. Gestion CPU & effets

### CPU
- Symptôme : saturation au climax (66→111% moyen, pics 136%).
- **Cause** : polyphonie des Surge XT trop élevée (16+ voix) avec FX.
- **Fix** : polyphony limit **2** sur les instances Surge (vox + strange) → CPU stable à **~29-32 %**.
- Le contenu MIDI (et non la polyphonie) porte l'intensité théâtrale.

### FX (en place — validé)
- **Sends partagés communs** : A-Reverb + B-Delay (logent la couleur spatiale sans surcoût CPU).
- **Device natif de couleur retenu** : Chorus-Ensemble sur Pad 2 (dauphin) — mode Ensemble large, dry/wet 0.4, width 0.6.
- **Surge XT** : FX internes superflus coupés (flanger + delay). Seul l'EQ interne léger est conservé.
- **Enseignement CPU** : les **reverb natives par piste** (device Reverb de Live sur chaque piste) sont TRÈS lourds → ils faisaient monter le CPU à 73-85%. Solution : une seule couleur via sends communs, PAS un device Reverb par piste.

Sends posés :
  - Alouette (lead) : reverb send A (0.28).
  - Hirondelle (harm) : reverb send A (0.2) + delay send B (0.25).
  - Dauphin (Pad 2) : reverb send A (0.3) + delay send B (0.18).
  - Baleine (strange) : reverb send A (0.45) + delay send B (0.35).
  - Ours (Pad 1) : nappe pure (pas de send — la reverb native est supprimée).
  - Écureuil (piano) : net (reverb native supprimée).
  - Watcher Kit : sec (pas de send).

---

## 8. Notes de production
- Conservation du patch Surge « vocal17 » (wavette analysée) = LA technique qui a rendu la voix convaincante.
- Ne pas réactiver les ring mods ni le filtre « FX Comb » (métallique/nasillard).
- Valider l'arrangement en descendant les scènes 6 → 1 après le climax (objectif : retour à l'intro/outro).
