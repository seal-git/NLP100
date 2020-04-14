#!/bin/bash
if [ $# -ne 1 ]; then
	echo "args must be 1" 
	exit 1
fi

cut  -f 1 -d "	" <$1 >col1.txt
cut  -f 2 -d "	" <$1 >col2.txt