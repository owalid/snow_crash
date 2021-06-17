#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

int main()
{
	printf("%d\n", setuid(4242));
	// system("./level13");
	execve("level13", NULL, NULL);
}
