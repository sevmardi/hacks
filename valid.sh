#!/bin/bash

#In-path -- Verifies that a spccified program is either a valid as is or can be found in the PATH directory list 

in_path(){
	#Given a command and the PATH, tries to find the command. Returns 0 if found and executable; 1 if not. Note that this is temp modifies 
	#The IFS (internal field seperator) but restores it upon completion.

	cmd=$1 ourpath=$2 result=1
	odlIFS=$IFS  IFS=":"

	for directory in "$ourpath"
	do 
		if [ -x $directory/$cmd ] ; then
			result=0 #if we're here, we found the command. 
		fi
	done 

	IFS=$odlIFS
	return $result	
}

checkForCmdInPath(){
	var=$1
	if [ "$var" != "" ] ; then
		if [ "${var%${var#?}}" = "/" ] ; then
			if [! -x $var]; then
				return 1
			fi
		elif ! in_path $var "$PATH"; then
			return 2
		fi
	fi

}

if [ $# -ne 1 ] ; then
	echo "Usage: $0 command" >&2
	exit 1
fi

checkForCmdInPath "$1"
case $? in 
	0 ) echo "$1 found in PATH";;
	1 ) echo "$1 not found or not executable";;
	2 ) echo "$1 not found in PATH" ;;
esac

exit 0