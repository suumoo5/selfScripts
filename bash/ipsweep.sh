#!/bin/bash

if ["$1" == ""]
then
	echo "You forgot an ip address!"
	echo "Syntax: ./ipsweep.sh [ip]"
	echo "Example: ./ipsweep.sh 192.168.1"

else
	for ip in seq 1 254; do
		ping -c 1 $1.$ip | grep "bytes" | cut -d " " -f 4 | tr -d ":" &
done
fi