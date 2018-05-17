#include <stdio.h>
#include <string.h>

#define true 1


struct Books
{
	char title[50];
	char author[50];
	char subject[100];

	int book_id;


};

union Data{
	int i;
	float f;
	char str[20];

}data;

struct 
{
	unsigned int widhth : 1; 
	unsigned int 	height : 1;

} status;

struct
{
	unsigned int age : 3;
}Age;

typedef unsigned char BYTE;


void printBook(struct Books book);
int main(int argc, char const *argv[])
{

// 	struct Books book1;
// 	struct Books book2;
// struct Books *struct_pointer; 
// struct_pointer = &book1;


	// union Data data;
	// data.i = 225;
	// printf("Memory size occuiped by data: %d\n", data.i);

	// strcpy(book1.title, "C programing");

	// printf("Book 1 title is: %s\n", struct_pointer->title);

	char str[100];

	printf("Enter a value: \n");
	gets(str);

	printf("You entered: \n");
	puts(str);

	

	return 0;
}

void printBook(struct Books book){
	printf( "Book title : %s\n", book.title);
}



