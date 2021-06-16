- get binary file named: level13, go to another VM:

```bash
su root
# change etc/passwd of any user to change the uuid to 4242
su <user_with_uuid_4242>
./level13
```

token:
```
2A31L79asukciNyi8uppkEuSx
```

================================

- recreate getuid function
```
uid_t	getuid(void)
{
	return (4242);
}
```
- compile
```
gcc -shared -fpic lib.c -o libnike.so -m32
```
- run and inject
```
LD_PRELOAD=./libnike.so ./level13
```

================================

- use setuid and excve in c
```
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

int main()
{
	printf("%d\n", setuid(4242));
	execve("level13", NULL, NULL);
}
```
