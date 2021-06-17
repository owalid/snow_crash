# Level 01

- `cat /etc/passwd | grep flag01`
```
flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
```
- `scp -P 4242 level01@192.168.56.101:/etc/passwd .`
- `./john -w:password.lst passwd`
<pre>
Warning: detected hash type "descrypt", but the string is also recognized as "descrypt-opencl"
Use the "--format=descrypt-opencl" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (descrypt, traditional crypt(3) [DES 128/128 AVX])
Press 'q' or Ctrl-C to abort, almost any other key for status
<strong>abcdefg          (flag01)</strong>
1g 0:00:00:00 DONE (2021-06-10 16:22) 100.0g/s 76800p/s 76800c/s 76800C/s raquel..bigman
Use the "--show" option to display all of the cracked passwords reliably
</pre>
- flag: `f2av5il02puano7naaf6adaaf`
