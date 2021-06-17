# Level 14

- cat /etc/passwd

```bash
....
flag14:x:3014:3014::/home/flag/flag14:/bin/bash
....
```
- get binary file named: getflag, go to another VM:

```bash
su root
# change etc/passwd of any user to change the uuid to 3014
su <user_with_uuid_3014>
./getflag
```
