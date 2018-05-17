#!/bin/bash
# nicenumber--Given a number, shows it in comma-separated form. Expects DD
#(decimal point delimiter) and TD (thousands delimiter) to be instantiated.
#Instantiates nicenum or, if a second arg is specified, the output is
#echoed to stdout

nicenum()
{
	integer=$(echo $1 | cut -d. -f1) #left of the decimal 
	decimal=$(echo $1 | cut -d. -f2) #right of the decimal

	
}