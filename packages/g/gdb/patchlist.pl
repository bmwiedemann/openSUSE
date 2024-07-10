#!/usr/bin/perl

die "need gdb-Fedora directory" unless -d $ARGV[0];

my $gdbFedora = $ARGV[0];
my $dir = `pwd`;
chomp($dir);

system "rm \$(grep \"^Patch[0-9]\\{1,3\\}:\" gdb.spec | awk '{print \$2}') 2>/dev/null";
system "rm *.tar.bz2";
system "cp -p $gdbFedora/*.tar.bz2 ./";
system "pushd $gdbFedora ; sh $dir/patchname_get.sh -v gdb.spec 2>$dir/test.txt; popd";
system "grep \"^Patch\" test.txt > test2.txt";

my @patchliste = `cat test2.txt`;
my @patchdeklarationen = ();
my @patchstatements = ();
my %seenpatches = ();
my $blockcounter = 0;
my @patchcopy = ();

foreach my $line (@patchliste) {
	chomp($line);
	if ($line =~ /\((.*)\)/) {
		$patchname = $1;
		if (exists $seenpatches{$patchname}){
			my $oldcount = $seenpatches{$patchname};
			push @patchstatements, "%patch$oldcount -p1 -R\n";
		}
		else {
			$count = $count + 1;
			push @patchdeklarationen, "Patch$count:       ". (($count < 10) ? "  " : (($count < 100) ? " " : "")) ."$patchname\n";
			push @patchstatements, "%patch$count -p1\n";
			$seenpatches{$patchname} = $count;
			push @patchcopy, $patchname;
		}
	}
}

foreach my $copy (@patchcopy) {
	system "cp \"$gdbFedora/$copy\" ./";
}

open F, ">gdb.spec.new";
foreach my $line (`cat gdb.spec`) {
	if ($line eq "#Fedora Packages begin\n") {
		print F $line;
		$blockcounter = 1;
	}
	elsif ($line eq "#Fedora Packages end\n") {
		$blockcounter = 0;
	}
	elsif($line eq "#Fedora patching start\n") {
                print F $line;
		$blockcounter = 3;
	}
	elsif($line eq "#Fedora patching end\n") {
		$blockcounter = 0;
	}
	if ($blockcounter == 0){
		print F $line;	
	} elsif ($blockcounter == 1) {
		print F @patchdeklarationen;
		$blockcounter = 2;
	} elsif ($blockcounter == 3) {
		print F @patchstatements;
		$blockcounter = 4;
	}
}
close F;

system "mv gdb.spec.new gdb.spec";
system "rm test.txt test2.txt";
system "osc addremove";
