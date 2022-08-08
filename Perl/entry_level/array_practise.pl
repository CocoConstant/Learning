#!/usr/bin/perl

# creat array
@arr_1 = (1,2,'hello');
@arr_2 = qw/this is a array/;
print ("@arr_2\n");

# visit elements of array "$ + variable_name + [value]"
@sites = qw/taobao wechat microblog/;
print "$sites[0]\n";
print "$sites[1]\n";
print "$sites[2]\n";
print "$sites[-1]\n";

# array index
@var_10 = (1..20);
@var_ab = ('a'..'z');
print "@var_10\n";
print "@var_ab\n";

# array length return its physical size rather than number of array
@array = (1,2,3);
$array[50] = 4;
$size = @array;
print "the size of array $size\n";

$max_index = $#array;
print "the bigest index of array is $max_index\n";


# add or delete elements of array
# 1.push: push@array,list
@name = ('kang', 'qian');
push(@name, 'ouyang'); # add element to end of array
print "@name\n";

# 2.pop:pop@array
push(@name, 'qian');
pop(@name); # delete last element of array
print "@name\n";

# 3.shift:shift@array
shift(@name); # take the first value and return it so that the index decreased

# 4.unshift:unshift@array,list
unshift(@name,"kang", "qianqian"); # take the list to front of array and return its number of arrauy


# carve array
@brand = qw/wechat redmi xiaomi apple qq microblog/;
@sub_brand = @brand[3..5];
print "@sub_brand\n";


# replace element of array
# splice(@array,begin,replace_number,substation_list)
@nums = (1..20);
print "before replace @nums\n";
splice(@nums,5,5,71..75);
print "after replace @nums\n";


# convert characters to array
# split(pattern, list, limit)
$var_str = "www-runoob-com";
@set = split('-', $var_str);
print("@set\n");

# convert array to character
# join(pattern,list or array)
$new_str = join('--', @set);
print "$new_str\n";


# sort arrat
# sort(@arrat)
print("before sort @brand\n");
@sort_brand = sort(@brand);
print("after sort @sort_brand\n");


# combind array
@odd = (1,3,5);
@even = (2,4,6);
@numbers = (@odd, @even);
print "the numbers is @numbers\n";


# select element from array
$one = @numbers[4];
print "$one\n";
print "@numbers[1..4]\n";
