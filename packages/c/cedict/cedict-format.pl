#!/usr/bin/perl --  # -*- coding: utf-8 -*-
#
# Author: Mike Fabian <mfabian@suse.de>, 2005
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.

require 5.008;
use Encode;
use Unicode::Normalize;
use utf8;
use English;

binmode STDIN,  ":encoding(utf8)";
binmode STDOUT, ":encoding(utf8)";

while (<>) {

    $ARG =~ s/^([^ ]+) ([^ ]+)/$1　$2/g;
    $ARG =~ s/coding: utf-8-dos/coding: utf-8/g;
    $ARG=NFC($ARG);
    print $ARG;
}



