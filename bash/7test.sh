#!/usr/bin/bash

# testing if a variable has content

if test $my_variable
then
	echo "the my_variable variable has content and return a True"
	echo "the my_variable variable content is: $my_variable"
else
	echo "the my_variable variable doesn't have content"
	echo "and returns a False"
fi
