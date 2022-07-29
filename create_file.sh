#!/bin/bash
# the program is designed to create file of perl and you should give the running permission to this file.

# obtain user file name
file_name=$1.pl

# create file
$(touch "$file_name")

# get running permission to user
$(chmod u+x "$file_name")

# add information of running environment to file
echo "#!/usr/bin/perl" > $file_name

# outputing information about creating file
if [ -f $file_name ];  # judging whether the file exist 
then
	if [ -e $file_name ]; # judging whether the content of file exist
	then
		echo the $file_name is created at $(date)
	else
		echo "can't add information to $file_name"
	fi
else
	echo sorry the $file_name is not created
fi
