#!/usr/bin/perl -w
# Copyright (c) 2012-2021 SUSE LLC
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
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

=head1 timestamp.pl

timestamp.pl - show or set pe timestamp in file

=head1 SYNOPSIS

timestamp.pl [OPTIONS] FILE...

=head1 OPTIONS

=over 4

=item B<--set-form-file=FILE>

parse timestamp, checksum, and linker version from file

=item B<--help, -h>

print help

=back

=head1 DESCRIPTION

lorem ipsum ...

=cut

use strict;
use Getopt::Long;
Getopt::Long::Configure("no_ignore_case");
use POSIX qw/strftime/;

my %options;

sub usage($) {
	my $r = shift;
	eval "use Pod::Usage; pod2usage($r);";
	if ($@) {
		die "cannot display help, install perl(Pod::Usage)\n";
	}
}

GetOptions(
	\%options,
	"set-from-file=s",
	"verbose|v",
	"help|h",
) or usage(1);

usage(1) unless @ARGV;
usage(0) if ($options{'help'});

my $set_timestamp;
my $set_checksum;
my $set_linker;

if ($options{'set-from-file'}) {
	die "$options{'set-from-file'}: $!\n" unless open(my $fh, '<', $options{'set-from-file'});
	while (<$fh>) {
		chomp;
		if (/^timestamp: ([0-9a-f]+)/) {
			$set_timestamp = pack('L', hex($1));
			next;
		} elsif (/^linker: ([0-9a-f]+)/) {
			$set_linker = pack('S', hex($1));
			next;
		} elsif (/^checksum: ([0-9a-f]+)/) {
			$set_checksum = pack('S', hex($1));
			next;
		}
		last if $set_timestamp && $set_checksum && $set_linker;
	}
	close($fh);
	die "file didn't contain timestamp, checksum, or linker\n" unless $set_timestamp && $set_checksum && $set_linker;
}

sub do_show($)
{
	my $file = shift;
	die "$file: $!\n" unless open(my $fh, '<', $file);
	die "seek $file: $!\n" unless seek($fh, 136, 0);
	my $value;
	die "read $file: $!\n" unless read($fh, $value, 4);

	my $timestamp = unpack('L', $value);
	print strftime("# %Y-%m-%d %H:%M:%S\n", gmtime($timestamp));
	printf ("timestamp: %x\n", $timestamp);

	die "seek $file: $!\n" unless seek($fh, 154, 0);
	die "read $file: $!\n" unless read($fh, $value, 2);

	printf ("linker: %x\n", unpack('S', $value));

	die "seek $file: $!\n" unless seek($fh, 216, 0);
	die "read $file: $!\n" unless read($fh, $value, 2);

	printf ("checksum: %x\n", unpack('S', $value));

	close($fh);
}

sub do_set($)
{
	my $file = shift;
	die "$file: $!\n" unless open(my $fh, '+<', $file);
	die "seek $file: $!\n" unless seek($fh, 136, 0);
	die "write $file: $!\n" unless print $fh $set_timestamp;

	die "seek $file: $!\n" unless seek($fh, 154, 0);
	die "write $file: $!\n" unless print $fh $set_linker;

	die "seek $file: $!\n" unless seek($fh, 216, 0);
	die "read $file: $!\n" unless print $fh $set_checksum;
	close($fh);
}

for my $file (@ARGV) {
	if ($options{'set-from-file'}) {
		do_set($file);
	} else {
		do_show($file);
	}

}
