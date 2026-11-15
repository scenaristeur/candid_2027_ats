# TODO_Guitare.md — Les Myopes (guitare fil conducteur)

## Etat actuel
- Patch : **Strummed Strings** (instance 5 / track 7 "8 Guitare")
- Device chain : Surge XT (device 0) + Channel EQ (device 1)
- Volume : 0.45, Panning : -0.2
- CPU global : ~62% au repos (5 instances Surge)

## Architecture
- Thème = cellule D–F–G–A pentatonique ré mineur qui évolue
- 9 clips session (slots 0–8) = 9 scènes = 9 sections du morceau
- Vue session = vue arrangement

## 9 clips session — données de notes

### Slot 0 : INTRO (32 beats) — V1L (0–16) + V2L (16–32)

**V1L** (29 notes) :
```
{50,0,0.5,100},{53,0,0.5,96},{57,0,0.5,98}
{50,1.5,0.5,90},{53,1.5,0.5,86},{57,1.5,0.5,88}
{62,2.25,0.25,92},{65,2.5,0.25,94},{67,2.75,0.25,96},{69,3,1.25,98}
{57,4.5,0.25,80},{55,4.75,0.25,78},{53,5,0.5,76},{50,5.5,1.5,74}
{65,6.5,0.25,70},{64,6.75,0.25,72},{62,7,0.5,74}
{50,8,0.5,100},{53,8,0.5,96},{57,8,0.5,98}
{62,9,0.25,92},{65,9.25,0.25,94},{67,9.5,0.25,96},{69,9.75,0.25,98}
{69,10,2,100}
{55,12.5,0.5,74},{57,13,0.5,78},{50,13.5,2,76},{62,13.5,2,72}
```

**V2L** (décalé +16) :
```
{62,16,1,84},{60,17,1,80},{57,18,2,78}
{53,20,0.5,74},{55,20.5,0.5,76},{57,21,1.5,80},{60,23,1,72}
{69,24,1,82},{67,25,1,78},{65,26,2,76}
{62,28,1,80},{50,30,2,84},{62,30,2,72}
```

### Slot 1 : C1 / C2 / C3 ACCENT (8 beats)
```
{50,0,0.35,88},{53,0,0.35,84},{57,0,0.35,86}
{62,1.5,1,76}
{62,4,0.25,72},{65,4.25,0.25,74},{67,4.5,1,78}
```

### Slot 2 : REFRAIN 1 (16 beats) — V3L (24 notes)
```
{50,0,0.5,100},{53,0,0.5,96},{57,0,0.5,98}
{50,1,0.5,92},{53,1,0.5,88},{57,1,0.5,90}
{62,1.75,0.25,92},{65,2,0.25,94},{67,2.25,0.25,96},{69,2.5,1.5,98}
{57,3.75,0.25,72},{55,4,0.25,70}
{50,8,0.5,98},{53,8,0.5,94},{57,8,0.5,96}
{62,9,0.25,90},{65,9.25,0.25,92},{67,9.5,0.25,94},{69,9.75,0.5,96}
{67,10.25,0.25,86},{65,10.5,0.25,84},{62,10.75,0.25,82}
{57,11.5,0.25,76},{55,11.75,0.25,74}
```

### Slot 4 : REFRAIN 2 (16 beats) — V5 (18 notes)
```
{50,0,0.5,100},{53,0,0.5,96},{57,0,0.5,98}
{50,1.5,0.5,92},{53,1.5,0.5,88},{57,1.5,0.5,90}
{62,2.25,0.25,92},{65,2.5,0.25,94},{67,2.75,0.25,96},{69,3,1,96}
{62,8,0.5,92},{65,8.5,0.5,94},{67,9,0.5,96},{69,9.5,0.5,98},{69,10,1.25,96}
{57,11.5,0.25,74},{55,11.75,0.25,72},{53,12,0.5,70}
```

### Slot 5 : PONT (16 beats) — V4L (11 notes)
```
{50,0,8,88},{57,0,8,84},{62,0,8,72}
{65,3.5,4.5,66}
{62,12,0.5,88},{65,12.5,0.5,90},{67,13,0.5,92},{69,13.5,1.5,96}
{57,15.25,0.25,74},{55,15.5,0.25,72},{53,15.75,0.5,70}
```

### Slot 7 : REFRAIN FINAL (16 beats) — V6 (17 notes)
```
{62,0,0.4,96},{74,0,0.4,92},{65,0.5,0.4,94},{77,0.5,0.4,90}
{67,1,0.4,92},{79,1,0.4,88},{69,1.5,2.5,96}
{50,8,0.5,100},{53,8,0.5,96},{57,8,0.5,98}
{62,9,0.25,92},{65,9.25,0.25,94},{67,9.5,0.25,96},{69,9.75,1.5,98}
{57,12,0.25,74},{55,12.25,0.25,72},{53,12.5,0.5,70}
```

### Slot 8 : OUTRO (16 beats) — V7 (10 notes)
```
{62,0,3,72},{65,0,3,68}
{69,4,2,76},{50,4,2,80}
{60,8,1,66},{57,9,1,62},{55,10,1,58}
{50,12,4,72},{57,12,4,68},{62,12,4,60}
```

## Layout arrangement (à dupliquer)
| Temps | Clip | Durée | Section |
|-------|------|-------|---------|
| 0 | Slot 0 INTRO | 32 | Intro |
| 32 | Slot 1 ACC | 8 | Entrée C1 |
| 96 | Slot 2 R1 | 16 | Refrain 1 |
| 128 | Slot 4 R2 | 16 | Refrain 1 suite |
| 160 | Slot 1 ACC | 8 | Entrée C2 |
| 224 | Slot 4 R2 | 16 | Refrain 2 |
| 256 | Slot 2 R1 | 16 | Refrain 2 suite |
| 288 | Slot 5 PONT | 16 | Pont |
| 320 | Slot 1 ACC | 8 | Pont écho |
| 352 | Slot 1 ACC | 8 | Entrée C3 |
| 416 | Slot 2 R1 | 16 | Refrain final start |
| 448 | Slot 7 RFIN | 16 | Refrain final climax |
| 464 | Slot 4 R2 | 16 | Refrain final fin |
| 496 | Slot 8 OUTRO | 16 | Outro ×3 (496/512/528) |

## A faire
1. **Recréer les 9 clips session** (create_clip aux slots 0–8 avec les longueurs ci-dessus)
2. **Ajouter les notes** (données ci-dessus, copier-coller telles quelles)
3. **Nommer les clips** : "INTRO", "Couplet ACC", "Refrain 1", "Refrain 2", "Pont", "Refrain final", "Outro"
4. **Dupliquer en arrangement** selon le tableau ci-dessus
5. **Tweaker le patch Strummed Strings** : polyphony_limit 6, fx/send/1/return 0.5, global/volume ~0.8
6. **Vérifier Channel EQ** : Mid Gain 0.65 (légère coupe pour laisser la voix passer)
7. **Écouter et ajuster** volume/gain de la piste 7

## Notes importantes
- Numérotation 0-based (slot 0 = scene 0 = INTRO)
- Couplets C1/C2/C3 = slots 1/3/6 (ACC = accents légers, 8 beats)
- 9 scènes correspondent aux noms sur la piste BASSE : INTRO, Couplet 1, Refrain 1, Couplet 2, Refrain 2, Pont, Couplet 3, Refrain final, Outro
- Slots 3 (C2 ACC) et 6 (C3 ACC) = même contenu que slot 1
- La voix entre à 95.75 (barre 25), D majeur → petit retard pour la voix, puissance pente montante
- Pont : A tenu bars 15-16 (tension), troubadour montée à 304
