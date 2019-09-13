#! /usr/bin/perl

use Cwd 'abs_path';
use File::Basename;

$dir=dirname(abs_path($0));


$command=$dir . "/elfdeps";
$dlinfo=$dir . "/dlinfo";
$arglist = "";

sub usage {
    my $message = <<EOF;
Usage: $0 [-?] [-P|--provides] [-R|--requires] [--filter-private]
        [--soname-only] [--no-fake-soname] [--assume-exec] [-?|--help]
        [--usage]
EOF
    print $message;
    exit (0);
}

sub help {
    my $message = <<EOF;
Usage: $0 [OPTION...]
  -P, --provides
  -R, --requires
      --filter-private
      --soname-only
      --no-fake-soname
      --assume-exec

Help options:
  -?, --help               Show this help message
      --usage              Display brief usage message
EOF
    print $message;
    exit (0);
}

while ( $a = shift @ARGV ) {
    if ( $a =~ /--assume-exec/ ||
	 $a =~ /--provides/ ||
	 $a =~ /-P/ ||
	 $a =~ /--requires/ ||
	 $a =~ /-R/ ||
	 $a =~ /--filter-private/ ||
	 $a =~ /--soname-only/ ||
	 $a =~ /--no-fake-soname/ ||
	 $a =~ /--filter-private/ ) {
	 $arglist .= " " . $a;
    } elsif ( $a =~ /--modules/ ) {
	$modules = shift @ARGV;
    } elsif ( $a =~ /--help/ || $a =~ /-?/ ) {
	help;
    } elsif ( $a =~ /--usage/ ) {
	usage;
#    } elsif ( $a = ~ / / ) {
#    } else {
    }
}

open HANDLE, "$command $arglist |";

if ( $modules ) {
    $ldlibrarypath = `module load $modules; echo \$LD_LIBRARY_PATH`;
    chop $ldlibrarypath;
}

while ((chop($line = <HANDLE>))) {
    $line =~ /([^\(]+)(.*)/;
    $libs{$1}{$2} = 1;
}

foreach $lib ( keys %libs ) {
    $full=`$dlinfo $lib`;
    chop $full;
    if (!$full) {
	delete $libs{$lib};
    } elsif ( $ldlibrarypath ) {
	$hpc = `LD_LIBRARY_PATH=$ldlibrarypath $dlinfo $lib`;
	chop $hpc;
	if ( $full ne $hpc) {
	    delete $libs{$lib};
	}
    }
}
foreach $lib ( keys %libs ) {
    foreach $key ( keys %{ $libs{$lib} } ) {
	print "$lib$key\n";
    }
}

