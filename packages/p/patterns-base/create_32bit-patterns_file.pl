#!/usr/bin/perl

use strict;
use warnings;

my $verbose = 0;
my $pat_ext = "32bit";
my $product = "";
my @skip_pat = ();

sub get_file {
	my $file_to_get = shift;
	my $content = "";

	open FILE, "<$file_to_get" or return "\n";
		while (defined (my $line = <FILE>)) {
			next if ($line =~ m/^#/);
			$content .= $line;
		}
	close FILE;
	return $content;
}

sub print_usage {
	print "$0 [-v] [-h]\n";
	exit 0;
}

sub print_debug {
	my ($txt, $lvl) = @_;
	print (STDERR "DBG: ${txt}\n") if($verbose >= $lvl);
}

sub parse_line {
	my $to_parse = shift;
	my $tmp = "";
	if ($to_parse =~ /%include/) {
		# TBD
		print "%include at unexpected position, exiting\n";
		exit (1);
	}
	if ($to_parse =~ /Summary:/) {
		return "$to_parse\n";
	}
	# XXX simplify me
	if ($to_parse =~ /Recommends:\s*([^\s]*)\s*/) {
		$tmp = "$1";
		return "" if ($tmp =~ m/.*-64bit\s*$/);
		$tmp = "${tmp}-32bit" if($tmp !~ m/.*-32bit/);
		return "Recommends:     ${tmp}\n";
	}
	if ($to_parse =~ /Requires:\s*([^\s]*)\s*/) {
		$tmp = "$1";
		return "" if ($tmp =~ m/pattern()/);
		return "" if ($tmp =~ m/.*-64bit\s*$/);
		$tmp = "${tmp}-32bit" if($tmp !~ m/.*-32bit/);
		return "Recommends:     ${tmp}\n";
	}
	return "";
}

sub parse_main_file {
	my $main_file = shift;
	my $spec_file = "";
	my $cur_pattern = "";
	my $skip_it = 1;
	my %skip_pat_hash;
	if(! open (MAIN_FILE, "<$main_file")) {
		print STDERR "${main_file} not found, exiting\n";
		exit 1;
	}
	while (defined (my $line = <MAIN_FILE>)) {
		chomp($line);
		next if ($line =~ m/^#/);
		if ($line =~ m/\%package/) {
			if(($line =~ m/32bit/) or 
			   ($line =~ m/64bit/)
			  ) {
			    $skip_it = 1;
			} else {
			  %skip_pat_hash =  map { $_ => 1 } @skip_pat;
			  if($skip_it==0&&!exists($skip_pat_hash{$cur_pattern})) {
			      $spec_file .=  ""
					    ."Provides:       pattern() = ${cur_pattern}%2d32bit\n"
					    ."Group:          Metapackages\n"
					    ."Supplements:    packageand(patterns-${product}-${pat_ext}:patterns-${product}-${cur_pattern})\n"
					    ."\n"
					    ."%files ${cur_pattern}-32bit\n"
					    ."%defattr(-,root,root)\n"
					    ."%dir /usr/share/doc/packages/patterns\n"
						."/usr/share/doc/packages/patterns/${cur_pattern}-${pat_ext}.txt\n"
					    ."\n"
					    ."%description ${cur_pattern}-${pat_ext}\n"
					    ."The ${pat_ext} pattern complementing ${cur_pattern}.\n"
					    ."#\n"
					    ."#-------------------------------------------------------------------\n"
					    ."#\n";
			  }
			  $skip_it = 0 ;
			  $line =~ m/package\s*([^\s]*)\s*/;
			  $cur_pattern = $1;
			  if (!exists($skip_pat_hash{$cur_pattern})) {
			  	$spec_file .= "%package ${cur_pattern}-32bit\n";
			  }
			}
		}
		next if($skip_it == 1 );
		if ($line =~ /%include/) {
			my $file_to_check = ($line =~ m/%include.*?([^\/\s]*)$/)[0]; # beware the non-greedy '?'
			next if($file_to_check =~ m/32bit/);
			if( open TMP_FILE, "<$file_to_check") {
				print_debug(" Checking INCLUDE: $file_to_check", 2);
				while (defined (my $include_line = <TMP_FILE>)) {
					if (!exists($skip_pat_hash{$cur_pattern})) {
						$spec_file .= parse_line($include_line);
					}
				}
				close TMP_FILE;
			}
			next;
		}
		if (!exists($skip_pat_hash{$cur_pattern})) {
			$spec_file .= parse_line($line);
		}
	}
	
	%skip_pat_hash =  map { $_ => 1 } @skip_pat;	
	if (!exists($skip_pat_hash{$cur_pattern})) {
		# I hate this, but need a fast workaround
		$spec_file .=  "Provides:       pattern-invisible()\n"
			      ."Provides:       pattern() = ${cur_pattern}%2d${pat_ext}\n"
			      ."Group:          Metapackages\n"
			      ."Supplements:    packageand(patterns-${product}-${pat_ext}:patterns-${product}-${cur_pattern})\n"
			      ."\n"
			      ."%files ${cur_pattern}-32bit\n"
			      ."%defattr(-,root,root)\n"
			      ."%dir /usr/share/doc/packages/patterns\n"
				  ."/usr/share/doc/packages/patterns/${cur_pattern}-${pat_ext}.txt\n"
			      ."\n"
			      ."%description ${cur_pattern}-${pat_ext}\n"
			      ."The ${pat_ext} pattern complementing ${cur_pattern}.\n"
			      ."\n";
	}

	close MAIN_FILE;

	my $new_file = $spec_file;

	return $new_file;
}

while ($ARGV[0] && $ARGV[0] =~ /^-/) {
	my $arg = shift;
	if ($arg =~ /-v/) {
		$verbose += 1;
	} elsif($arg =~ /-h/) {
		print_usage();
		exit();
	} elsif($arg =~ /-p/) {
		$product=shift;
	} elsif($arg =~ /-e/) {
		$pat_ext=shift;
	} elsif($arg =~ /-s/) {
		push @skip_pat, shift;
	}
	
}

print_debug("product = ${product}\n     pat_ext=${pat_ext}\n", 1);
my $result = parse_main_file("patterns-${product}.spec");
print "${result}\n";
exit 0;

