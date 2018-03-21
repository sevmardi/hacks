#include <stdio.h>

int main(int argc, char const *argv[])
{
	const int length = 10;
	const int width = 5;

	const char newLine = '\n';

	int area;

	area = length  * width;
	printf("Value of area: %d", area );
	printf("%c", newLine);

	return 0;

}