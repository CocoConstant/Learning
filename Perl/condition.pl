#!/usr/bin/perl

# IF
# 数字 0, 字符串 '0' 、 "" , 空 list() , 和 undef 为 false ，其他值均为 true。 true 前面使用 ! 或 not则返回 false
$var = 10;
if ( $var < 20 ){
	print "var is smaller than 20\n";
}


# if else
if ( $var > 20 ){
	print "heihei";
}
else{
	print "var is smaller than 20\n";	
}


# if else elsif
if ( $var == 20 ){
	print "the value of a is 20\n";
}elsif ( $var == 10){
	print "the value of var is 10\n";
}else{
	print "no condition\n";
}


# unless
unless( $var > 20 ){
	printf "var is smaller than 20\n";
}

# switch
@arr = (10, 20, 30);
%hash = (-apple=>10,-strawberry=>20);









