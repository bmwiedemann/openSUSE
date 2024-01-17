#!/usr/bin/perl -w
# Merge several PCI ID lists to a single one. This script tries to be as agnostic
# of the details of the ID list as possible, so it should not break with future
# changes of the ID list format as long as they follow the same block structure.
#
# Options:
# -v: Verbose mode. Warn if multiple files provide different definitions for
#     the same device.
#
# (c) 2007 Martin Mares <mj@ucw.cz>, GPLv2
# (c) 2013, 2015 Jean Delvare <jdelvare@suse.de>

use strict;
use Getopt::Std;
use File::Copy;
use vars qw($IDSD_PATH $MASTER_IDS $PCI_IDS @idsd_files $output);

$IDSD_PATH	= "/usr/share/pci.ids.d";
$MASTER_IDS	= "/usr/share/pci.ids.d/pci.ids.dist";
$PCI_IDS	= "/usr/share/pci.ids";

our $opt_v;
getopts('v');

if (! -f $MASTER_IDS) {
	print STDERR "ERROR: $MASTER_IDS not found, giving up\n";
	exit 1;
}

sub collect_files($)
{
	my ($dir) = @_;
	my ($file, @files);

	opendir(my $dh, $dir) || die "Could not open directory $dir: $!";
	# Ignore non-files and hidden files
	while (defined ($file = readdir($dh))) {
		push @files, "$dir/$file" if $file !~ m/^\./ && -f "$dir/$file";
	}
	closedir($dh);

	return @files;
}

my %ids = ();
my %comments = ();
@idsd_files = collect_files($IDSD_PATH);
foreach our $file (@idsd_files) {
	my $fn = ($file =~ /\.gz$/) ? "zcat $file |" : ($file =~ /\.bz2$/) ? "bzcat $file |" : $file;
	open F, $fn or die "Unable to open $file: $!";
	my @id = ();
	my $comm = "";
	my $class = 0;
	sub err($) {
		print STDERR "Error in $file, line $.: @_\n";
		# If merging fails for whatever reason, fallback to master file copy
		print STDERR "WARNING: Merge not successful, using master pci.ids file\n";
		copy($MASTER_IDS, $PCI_IDS) || die "Could not copy $MASTER_IDS to $PCI_IDS: $!";
		chmod(0644, "$PCI_IDS");
		exit 1;
	}
	while (<F>) {
		if (/^(#.*|\s*$)/) {
			$comm .= $_;
			next;
		}
		chomp;
		if (/^(\t|C\s+|)([0-9a-fA-F]+)\s+(.*)$/ ||
		    (!$class && /^(\t\t)([0-9a-fA-F]+\s+[0-9a-fA-F]+)\s+(.*)$/) ||
		    ($class && /^(\t\t)([0-9a-fA-F]+)\s+(.*)$/)) {
			my $indent = $1;
			my $id = lc($2);
			my $name = $3;
			if ($indent =~ /^C\s+$/) {
				$indent = "";
				$id = "C $id";
			}
			my $depth = length $indent;
			$depth <= @id or err "Mismatched indentation";
			@id = (@id[0..$depth-1], $id);
			$class = ($id =~ /^C\s/) if !$depth;		# Remember if we are in a vendor or a class section
			my $i = join(":", @id);
			my $j = $class ? "~$i" : $i;			# We want to sort special entries last
			if ($opt_v && exists $ids{$j} && $ids{$j} ne $name) {
				print STDERR "Warning: ID $i has two different definitions, using the one from $file\n";
			}
			$ids{$j} = $name;
			$comments{$j} = $comm if $comm;
		} else {
			err "Parse error";
		}
		$comm = "";
	}
	close F;
}

# Write to a temporary file to avoid a race condition with lspci
open($output, ">", "$PCI_IDS.part") || die "Could not write to $PCI_IDS.part: $!";
print $output "# This file has been merged automatically from the following files:\n#\t", join("\n#\t", @idsd_files), "\n\n";
foreach my $id (sort keys %ids) {
	my ($i, $j) = ($id, $id);
	$i =~ s/[^:]//g;
	$i =~ tr/:/\t/;
	$j =~ s/.*://g;	
	$j =~ s/^~//;
	print $output $comments{$id} if $comments{$id};
	print $output "$i$j  $ids{$id}\n";
}
close($output);
rename("$PCI_IDS.part", "$PCI_IDS") || die "Could not rename $PCI_IDS.part to $PCI_IDS: $!";
chmod(0644, "$PCI_IDS");
