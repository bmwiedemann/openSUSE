#!/usr/bin/perl -w
#
# Modify the linker version in the EFI/PE header
# 
# NOTE: only use this script when the signature doesn't match after 
#       a binutils upgrade
#

use strict;

# The target version of binutils: 2.32
my $major_linker_version = 2;
my $minor_linker_version = 32;

my ($file) = @ARGV;

die "$file: $!\n" unless open(my $fh, '+<', $file);
# Set MajorLinkerVersion at 0x9a
die "seek $file: $!\n" unless seek($fh, 0x9a, 0);
die "write $file: $!\n" unless print $fh pack('C', $major_linker_version);
# Set MinorLinkerVersion at 0x9b
die "seek $file: $!\n" unless seek($fh, 0x9b, 0);
die "write $file: $!\n" unless print $fh pack('C', $minor_linker_version);
close($fh);
