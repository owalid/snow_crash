#include <stdio.h>

void lol(char *token)
{
	int	i = 0;
	
	while (token[i])
	{
		putchar(token[i] - i);
		i++;
	}
}

int main(int argi, char **argv)
{
	lol(argv[1]);
	return 1;
}
