#!/bin/bash
# the program is designed to create file of shell

# obtain user file name
file_name=$1.sh

# create file
$(touch "$file_name")

# grant running permission
$(chmod u+x "$file_name")

# add basic character to file
echo "#!/usr/bin/bash" > $file_name

# outputing information about creating file
if [ -f $file_name ];
then
	if [ -e $file_name ];
	then
		echo the $file_name is created at $(date)
	else
		echo "can't add information to $file_name"
	fi
else
	echo sorry the $file_name is not created
fi
