#!/bin/sh
#
# Copyright (c) 2001 SUSE GmbH, Nuernberg, Germany
# Copyright (c) 2002 SUSE Linux AG, Nuernberg, Germany
#
# Author: Vladimír Linek <vinil@suse.cz>
#
# Postprocessor for 'less'.
# Use with environment variable:  LESSCLOSE="lessclose.sh %s %s"
#

test "$1" = "$2" || rm -f "$2"
