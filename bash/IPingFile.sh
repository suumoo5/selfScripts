#!/bin/bash
f="$1";

pingIP(){
	result=$(ping -c 1 $1 | grep "received" | cut -d " " -f 4);	
	if [ $result -eq 0 ];
	then
		return 1; #False
	else
		return 0; #True
	fi
}

if [ '$1' == '' ];
then
	echo "Error: Syntax error"
	echo "Syntax: ./IPingFile.sh [filename]"
	echo "Example: ./IPingFile.sh someFile.txt"
else
	
	while read line;
	do
		if pingIP "$line";
		then
			echo "$line is responding"
		else
			echo "$line is not responding"
		fi
	done < $f
fi


