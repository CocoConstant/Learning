#!/usr/bin/bash

for fasta_file in $( ls /home/bio_kang/data/virus_data/*.fasta )
do
	if [ $( grep -oP '^(>)[A-Z]{1,2}\d{5,6}' | wc -l ) -eq 20 ]
	then
		continue
	else
		echo $fasta_file
	fi
done
