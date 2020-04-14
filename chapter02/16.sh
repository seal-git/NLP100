#!/bin/bash
if [ $# -ne 2 ]; then
	echo "args must be 2" 
	exit 1
fi

#arg1=text name, arg2=N
i=`cat $1 | wc -l`
echo $i 
p=$(($i % $2))
if [ $p -ne 0 ]; then
	echo "lines must be multiple of N " 
	exit 1
fi

line=$(($i / $2))
split -l $line -d $1 --additional-suffix=".txt" split_file_