#include <stdio.h>
#include <string.h>
int main(int argc, char const *argv[])
{

// char greetings[6] = {'H', 'e', 'l', 'l', 'o', '\0'};
char str1[12] = "Hello";
char str2[12] = "World";

char str3[12];

strcpy(str3, str1);

strcat( str1, str2);
printf("strcat( str1, str2): %s\n", str1 );

	
	

}
