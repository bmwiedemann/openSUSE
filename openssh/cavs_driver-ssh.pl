#!/usr/bin/perl
#
# CAVS test driver for OpenSSH
#
# Copyright (C) 2015, Stephan Mueller <smueller@chronox.de>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
#                            NO WARRANTY
#
#    BECAUSE THE PROGRAM IS LICENSED FREE OF CHARGE, THERE IS NO WARRANTY
#    FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW.  EXCEPT WHEN
#    OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES
#    PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED
#    OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
#    MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS
#    TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.  SHOULD THE
#    PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING,
#    REPAIR OR CORRECTION.
#
#    IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
#    WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY AND/OR
#    REDISTRIBUTE THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES,
#    INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING
#    OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED
#    TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY
#    YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER
#    PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE
#    POSSIBILITY OF SUCH DAMAGES.
#
use strict;
use warnings;
use IPC::Open2;

# Executing a program by feeding STDIN and retrieving
# STDOUT
# $1: data string to be piped to the app on STDIN
# rest: program and args
# returns: STDOUT of program as string
sub pipe_through_program($@) {
	my $in = shift;
	my @args = @_;

	my ($CO, $CI);
	my $pid = open2($CO, $CI, @args);

	my $out = "";
	my $len = length($in);
	my $first = 1;
	while (1) {
		my $rin = "";
		my $win = "";
		# Output of prog is FD that we read
		vec($rin,fileno($CO),1) = 1;
		# Input of prog is FD that we write
		# check for $first is needed because we can have NULL input
		# that is to be written to the app
		if ( $len > 0 || $first) {
			(vec($win,fileno($CI),1) = 1);
			$first=0;
		}
		# Let us wait for 100ms
		my $nfound = select(my $rout=$rin, my $wout=$win, undef, 0.1);
		if ( $wout ) {
			my $written = syswrite($CI, $in, $len);
			die "broken pipe" if !defined $written;
			$len -= $written;
			substr($in, 0, $written) = "";
			if ($len <= 0) {
				close $CI or die "broken pipe: $!";
			}
		}
		if ( $rout ) {
			my $tmp_out = "";
			my $bytes_read = sysread($CO, $tmp_out, 4096);
			$out .= $tmp_out;
			last if ($bytes_read == 0);
		}
	}
	close $CO or die "broken pipe: $!";
	waitpid $pid, 0;

	return $out;
}

# Parser of CAVS test vector file
# $1: Test vector file
# $2: Output file for test results
# return: nothing
sub parse($$) {
	my $infile = shift;
	my $outfile = shift;

	my $out = "";

	my $K = "";
	my $H = "";
	my $session_id = "";
	my $ivlen = 0;
	my $eklen = "";
	my $iklen = "";

	open(IN, "<$infile");
	while(<IN>) {

		my $line = $_;
		chomp($line);
		$line =~ s/\r//;

		if ($line =~ /\[SHA-1\]/) {
			$iklen = 20;
		} elsif ($line =~ /\[SHA-256\]/) {
			$iklen = 32;
		} elsif ($line =~ /\[SHA-384\]/) {
			$iklen = 48;
		} elsif ($line =~ /\[SHA-512\]/) {
			$iklen = 64;
		} elsif ($line =~ /^\[IV length\s*=\s*(.*)\]/) {
			$ivlen = $1;
			$ivlen = $ivlen / 8;
		} elsif ($line =~ /^\[encryption key length\s*=\s*(.*)\]/) {
			$eklen = $1;
			$eklen = $eklen / 8;
		} elsif ($line =~ /^K\s*=\s*(.*)/) {
			$K = $1;
			$K = substr($K, 8);
			$K = "00" . $K;
		} elsif ($line =~ /^H\s*=\s*(.*)/) {
			$H = $1;
		} elsif ($line =~ /^session_id\s*=\s*(.*)/) {
			$session_id = $1;
		}
		$out .= $line . "\n";

		if ($K ne "" && $H ne "" && $session_id ne "" &&
		    $ivlen ne "" && $eklen ne "" && $iklen > 0) {
			$out .= pipe_through_program("", "@LIBEXECDIR@/ssh/cavstest-kdf -H $H -K $K -s $session_id -i $ivlen -e $eklen -m $iklen");

			$K = "";
			$H = "";
			$session_id = "";
		}
	}
	close IN;
	$out =~ s/\n/\r\n/g; # make it a dos file
	open(OUT, ">$outfile") or die "Cannot create output file $outfile: $?";
	print OUT $out;
	close OUT;
}

############################################################
#
# let us pretend to be C :-)
sub main() {

	my $infile=$ARGV[0];
	die "Error: Test vector file $infile not found" if (! -f $infile);

	my $outfile = $infile;
	# let us add .rsp regardless whether we could strip .req
	$outfile =~ s/\.req$//;
	$outfile .= ".rsp";
	if (-f $outfile) {
		die "Output file $outfile could not be removed: $?"
			unless unlink($outfile);
	}
	print STDERR "Performing tests from source file $infile with results stored in destination file $outfile\n";

	# Do the job
	parse($infile, $outfile);
}

###########################################
# Call it
main();
1;
