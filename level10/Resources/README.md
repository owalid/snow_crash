### English
We found out (using ltrace and gdb) that the rights to open the `token` file should be only from the right group.
We can use the attack which is called: "Cryogenic Sleep".
The idea is to pass a file in parameter where we have the rights and to modify it during a sleep. In the script we make a symbolic link on the file passed in parameter and the token file.

### Francais
Nous nous sommes appercu (en utilisant ltrace et gdb) que les droits pour ouvrir le fichier `token` devais etre uniquement du bon groupe..
Nous pouvons utiliser l'attaque qui se nomme: "Cryogenic Sleep".
L'idée est de passer un fichier en parametre ou nous avons les droit et de le modifier lors d'un sleep. Dans le script nous faisont un lien symbolique sur le fichier passer en parametre et le fichier token.


- password: woupa2yuojeeaaed06riuj63c

- getflag
```
feulo4b72j7edeahuete3no7c
```