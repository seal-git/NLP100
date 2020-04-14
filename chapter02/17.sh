#!/bin/bash
if [ $# -ne 1 ]; then
	echo "args must be 1" 
	exit 1
fi

#arg1=text name, arg2=N

cut  -f 1 -d "	" <$1|sort|uniq
cut  -f 1 -d "	" <$1|sort|uniq|wc -l
