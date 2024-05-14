#!/usr/bin/env perl -w

#ipad Pro 11 relative to stock
$xs = 2.04;
$ys = 1.1;
$xd = 0;
$yd = 0;

#iphone 13 Mini relative to stock
#$xs = 0.92;
#$ys = 0.981;
#$xd = -1;
#$yd = 0;

while (<>){
  if (/frame/) {
    $str = $_;
    $str =~ /^(\s*)/;
    my $scount = length( $1 );
    s/.*:\s*\"(.*)\"\s*,/$1/;
    s/[\{\},]//g;
    @arr = split(' ', $_);
    $#arr == 3 or die "wrong array size";
    $x0 = int(0.5 + $arr[0] * $xs + $xd);
    $x1 = int(0.5 + $arr[2] * $xs + $xd);
    $y0 = int(0.5 + $arr[1] * $ys + $yd);
    $y1 = int(0.5 + $arr[3] * $ys + $yd);
    print " "x$scount . "\"frame\" : \"{{$x0, $y0}, {$x1, $y1}}\",\n";
  }else{
    print;
  }
}
