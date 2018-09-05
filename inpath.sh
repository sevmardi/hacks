#!/bin/bash
#inpath--Verifies that a specified program is either valid as is
#	or can be found in the PATH directory list

in_path()
{
cmd=$1
ourpath=$2
result=1
oldIFS=$IFS
IFS=":"

	
	for dir in "$ourpath"
	do
		if[-x $directory/$cmd];then
			result=0
		fi
	done

	IFS=$oldIFS
	return result
}

checkForCmdPath()
{

}