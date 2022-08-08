#!/usr/bin/perl

############scalar##########
# this is a number beginning with a sign "$"
$scalar_1 = 123;
print "the number scalar is $scalar_1\n";

# this is a character
$scalar_2 = "1234";
print "the character scalar is $scalar_2\n";


##########array##########
# this is an array beginning with a sign "@" and its index begin from 0
@arr = (1,2,3);


##########hash##########
# this is a hash beginning with a sign "%", which is an unordered mated set with key/value
%hash = ('a'=>1, 'b'=>2);


# 数字字面量
# 1.integer
$x = 12345;
if (1217 + 116 == 1333){
	print "the integer is $x\n";
}

# 2.float
$var = 9.01e+21 + 0.01 - 9.01e+21;
print "first number is $var\n";
$var_2 = 9.01e+21 - 9.01e+21 + 0.01;
print "second number is $var_2\n";

# 3.characters
$char = "this is an example
	using many
	lines with characters";
print("$char\n");


