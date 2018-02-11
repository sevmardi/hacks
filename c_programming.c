#include <stdio.h>

int main(int argc, char const *argv[])
{
	int a, b;
	a = 5;
	b = a++ * 6;
	printf("%d\n", b);
	return 0;
}