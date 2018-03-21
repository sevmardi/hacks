package main

import (
	"fmt"
	"math"

)

func main() {

	var a, b, c int

	a = 20
	b = 10
	c = a + b
	fmt.Printf("value of a = %d, b = %d and c = %d", a,b,c)

	var blaanace [10] int
	blaanace[4] = 50.0

	for i :=0; i < 10; i++{

	}	

}

func max(x1, x2 int) int {
	res int 
	
}

func swap(int x, int y) int  {
	var temp int;

	temp  = x 
	x = y
	y = temp


	return temp
}

func getAverage(arr[] int, int size) float32 {
	var i int 
	var avg, sum float32

	for i = 0; i < size; ++i{
		sum += arr[i]

	}

	avg = sum / size

	return avg
	
}
