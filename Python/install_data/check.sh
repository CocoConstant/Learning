#!/usr/bin/bash

location=$1

for fasta_file in $( ls $1/*.fasta )
do
	if [ $( grep -oP '^(>)[A-Z]{1,2}\d{5,6}' $fasta_file | wc -l ) -eq 20 ]
	then
		continue
	else
		echo $fasta_file
	fi
done
