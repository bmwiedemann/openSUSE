#!/usr/bin/perl -w
## $Id: count_file.pl 232 2006-10-01 15:23:55Z touche $
##	julien.touche@touche.fr.st
##
## modified from http://answers.tveasy.co.uk/c.l.p.misc/count-fd.htm

use strict;

$ENV{'PATH'}='';
$ENV{'BASH_ENV'}='';
$ENV{'ENV'}='';

#use lib "/usr/local/libexec/nagios";
#use lib "T:\\sysshare\\unattended\\install\\packages\\admin\\nrpe_nt\\bin\\utils.pm";
#use utils qw(%ERRORS);

if($#ARGV+1!=3 || ! -d $ARGV[0]){
        print "Usage: \"Filename\" \"Critical number of files\" \"Warning number of files\"\n";
        print " examples: $0 <dir> 1 10\n";
        print " examples: $0 <dir> 3:10 1:3\n";
        exit 0;
}
my $exit=0;
my ($dir,$maxwarn,$maxcrit,$minwarn,$mincrit);
$dir = $ARGV[0];
$maxcrit = $ARGV[1];
if ($maxcrit =~ m/([0-9].+):([0-9].+)/) {
        $mincrit = $1;
        $maxcrit = $2;
}
$maxwarn = $ARGV[2];
if ($maxwarn =~ m/([0-9].+):([0-9].+)/) {
        $minwarn = $1;
        $maxwarn = $2;
}


my ($count);

opendir DIR, $dir or die "Could not opendir $dir; Reason: $!";

my @files = grep !/^\.\.?$/ => readdir DIR;

$count = @files ;

closedir DIR;

if ($count>$maxcrit) {
        print "Critical: Filecount of '$dir' too large $count > $maxcrit.\n";$exit=2;
} elsif (defined($mincrit) && $count < $mincrit) {
        print "Critical: Filecount of '$dir' too small $count < $mincrit.\n";$exit=2;
} elsif ($count>$maxwarn) {
        print "Warning: Filecount of '$dir' $count > $maxwarn.\n";$exit=1;
} elsif (defined($minwarn) && $count < $minwarn) {
        print "Warning: Filecount of '$dir' $count < $minwarn.\n";$exit=1;
} else {
	print "OK: Filecount of '$dir' $count.\n"; $exit = 0;
}
exit $exit;

