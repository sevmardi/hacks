#include <iostream>
#include <string>

using namespace std;

#define SYMBOL  "$"
#define PRICE 100;
#define MONEY "Dollars"

int main(){

	int arr[5] = {20,-6,0,100,78};
	int max = arr[0];

	for(int n = 1; n < 5; n++) 
		if(arr[n] > max)
			max = arr[n];
	cout << "Max value = " << max << endl;

	return 0;

}