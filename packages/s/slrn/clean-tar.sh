#!/bin/sh
#
# Remove restrictive licenses from slrn tarball - bsc#1036331
# 
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#

SLRN_VERSION=`rpm -q --queryformat "%{version}\n" --specfile slrn.spec | head -n1`
bzip2 -dv < slrn-${SLRN_VERSION}.tar.bz2 > slrn-${SLRN_VERSION}.tar

# handle unused help text
tar -xvf slrn-${SLRN_VERSION}.tar slrn-${SLRN_VERSION}/src/help.c
sed '/^#if ! SLRN_USE_SLTCP$/,/^#endif$/d' -i slrn-${SLRN_VERSION}/src/help.c
# remove restrictive license files
# src/clientlib.* are actually clean in the upstream distributed tarball
tar -v --wildcards --delete -f slrn-${SLRN_VERSION}.tar \
	"slrn-${SLRN_VERSION}/src/vms.c" \
	"slrn-${SLRN_VERSION}/src/help.c"
# put in modified help.c
tar -v --append -f slrn-${SLRN_VERSION}.tar slrn-${SLRN_VERSION}/src/help.c

# clean up
rm slrn-${SLRN_VERSION}/src/help.c
rmdir slrn-${SLRN_VERSION}/src
rmdir slrn-${SLRN_VERSION}

# make a tarball
mv -v slrn-${SLRN_VERSION}.tar slrn-${SLRN_VERSION}-gpl.tar && \
bzip2 -9 -v slrn-${SLRN_VERSION}-gpl.tar


