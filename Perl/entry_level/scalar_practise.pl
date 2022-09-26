#!/usr/bin/perl

# 1.scalar operation
$str = "hello" . 'handsome baby'; # combine characters
$num = 5 + 10; #add number
$mix = $str . $num;
print "the str is $str\n";
print "the num is $num\n";
print "the mix is $mix\n";
 

# 2.multi-line character
$string = 'hei                                 hei
	   hei				       hei
				hei
				hei
				hei
				hei
			hei		hei
			hei		hei
			hei		hei
			    hei  hei  hei 
				 hei
				 hei
			
			
		hei				    hei
		   hei            	 	 hei
		      hei		      hei
		      	 hei 		   hei
			    hei hei hei hei 
'; 
print "$strin\n";


# 3.special character
print "file name". __FILE__ . "\n";
print "line number" . __LINE__ . "\n";
print "package name" . __PACKAGE__ . "\n";


# 4.v character
# 一个以 v 开头,后面跟着一个或多个用句点分隔的整数,会被当作一个字串文本
$smile = v9786;
print "smile = $smile\n";
