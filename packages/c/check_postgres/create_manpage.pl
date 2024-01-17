#!/usr/bin/perl 
use Pod::Man;
my $parser = Pod::Man->new (release => $ARGV[0], section => $ARGV[1]);
$parser->parse_from_file ($ARGV[2], $ARGV[3]);
