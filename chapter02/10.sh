#!/bin/bash
if [ $# -ne 1 ]; then
	echo "args must be 1" 
	exit 1
fi
	
wc $1