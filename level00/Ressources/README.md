# Level 00

- Premiere solution:
  - `cd /rofs/usr/sbin`
  - `ls -al`
  - `un fichier non executable s'appel john`
- Deuxieme solution:
  - find / -user flag00 2>&-
- `cat john`
```
cdiiddwpgswtgt
```
- une serie de charactere sans charatere special ni de chiffre, j'ai essayer un rot13 = fail
- puis j'ai fait tout les rot jusqu'a voir si la string renvoyer quelquechose de comprehensible.
```
rot11: nottoohardhere
```
- getflag: `x24ti5gi3x0ol2eh4esiuxias`
