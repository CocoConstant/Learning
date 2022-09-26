#!/usr/bin/perl

# 1.scalar
$age = 19; # integer
$name = ouyangkang; #character
$height = 172.42; # float

print "Age = $age\n";
print "Name = $name\n";
print "Height = $height\n";


# 2.array
@ages = (19,20);
@names = ('ouyangkang','kangqianqian');

print "the age of $names[0] = $ages[0]\n";
print "the age of $names[1] = $ages[1]\n";


# 3.hash
%data = ('google',45,'runoob',30,'taobao',40);
print "\$data{'google} = $data{'google'}\n";
print "\$data{'runoob'} = $data{'runoob'}\n";
print "\$data{'taobao'} = $data{'taobao'}\n";


# 4. variable context
@brand = ('taobao','jingdon','wechat','microblog');
@copy = @brand; # copy array of brand
$size = @brand; # it will return the number of arrar elements when make the value @array to $scalar
print "name is @copy\n";
print "the number of name is $size\n";






