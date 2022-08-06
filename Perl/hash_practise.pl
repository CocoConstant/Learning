#!/usr/bin/perl
# simple example
%data = ('google', 'google.com', 'runoob', 'runoob.com', 'taobao', 'taobao.com');
print "\$data{'google'} = $data{'google'}\n";
print "\$data{'runoob'} = $data{'runoob'}\n";
print "\$data{'taobao'} = $data{'taobao'}\n";


# create hash
%hash = ('google','fucking','taobao','money','name','dong');
print("$hash{'google'}\n");

# visit hash using key
print("$data{'taobao'}\n");

# read value of hash
@arr = @hash{'taobao', 'name'};
print "array is @arr\n";


# read key
# keys %hash
@keys = keys %data;
print "the keys are @keys\n";

# read value
# values %hash
@values = values %data;
print "the values are @values\n";


# testify element are exsting
# exists($var{'key'})
%brand = (-apple=>15,-banana=>20,-strawberry=>50);
if ( exists($brand{-apple}) ){
	print "the price of apple is $brand{-apple}\n";
}
else
{
	print "don't have apple\n";
}


# obtain the size of hash can first geting its size of keys or values
@keys = keys %brand;
$size = @keys;
print "the %brand size is $size\n";


# add or delete elements
$brand{-pear} = 5; # add elements
print "add element $brand{-pear}\n";

delete $brand{-apple};
if ( exists($brand{-apple}) ){
	print "don't delete\n";
}
else
{
	print "deleted\n";
}


# iterate
# using foreach and while
while(($key, $value) = each(%brand)){
	print "$brand{$key}\n";
}

foreach $key (keys %brand){
	print "the price is $brand{$key}\n";
}
