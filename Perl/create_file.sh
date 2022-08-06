#!/bin/bash
# the program is designed to create file of perl

# obtain user file name
file_name=$1.pl

# create file
$(touch "$file_name")

# get running permission
$(chmod u+x "$file_name")

# add basic character to file
echo "#!/usr/bin/perl" > $file_name

# outputing information about creating file
if [ -f $file_name ];
then
	if [ -e $file_name ];
	then
		echo the $file_name is created at $(date) >> train.log
		echo the $file_name is created at $(date)
	else
		echo "can't add information to $file_name"
	fi
else
	echo sorry the $file_name is not created
fi
