sub truc {
  print("lol");
  return 11;
}

$lol = "truc";
# $lol =~ "s/(.*)/truc()\e";
$lol =~ s/(.*)/truc()/e;
print($lol);
