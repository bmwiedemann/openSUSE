#!/usr/bin/perl -w
# SPDX-License-Identifier: LGPL-3.0-or-later
# written by Bernhard M. Wiedemann in 2024
# to normalize the .gir file values
# for reproducible builds of the gegl package
use strict;

my $property = "";
while(<>) {
    if(m/<property name="([^"]+)"/) {
        $property = $1;
    }
    if($property eq "threads") {
        s/(default-value=)"[^"]+"/$1"4"/;
    }
    if($property eq "tile-cache-size") {
        s/(default-value=)"[^"]+"/$1"4000000000"/;
    }
    print;
}
