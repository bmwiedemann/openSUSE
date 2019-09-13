#!/usr/bin/perl

use warnings;
use strict;

# Script from Boris Zentner (Maxmind)
# This script converts the IPv4 csv database to the same
# format as the IPv6 database.

sub _x {
	sprintf("%02x%02x:%02x%02x", split(/\./, $_[0]));
}

while(<STDIN>){
	chomp;
	my($f, $t, $tail) = split /,/, $_, 3;

	for($t, $f){
		s/^"//;
		s/"$//;
	}
	my $xxxxf = _x($f);
	my $xxxxt = _x($t);
	print <<__OUT__;
"::$f", "::$t", $tail
"::ffff:$f", "::ffff:$t", $tail
"2002:${xxxxf}::", "2002:${xxxxt}:ffff:ffff:ffff:ffff:ffff", $tail
__OUT__
}

exit(0);
