#!/usr/bin/env bash
#
# Remove documentation files from source archives 
# 
# Copyright (c) Andreas Stieger <Andreas.Stieger@gmx.de>
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
set -ev

FIREBIRD_VERSION=`rpm -q --queryformat "%{version}\n" --specfile firebird.spec | head -n1`
FIREBIRD_VERSION=${FIREBIRD_VERSION}-0

bzip2 -dkv Firebird-${FIREBIRD_VERSION}.tar.bz2
tar -v --wildcards --delete -f Firebird-${FIREBIRD_VERSION}.tar \
	"Firebird-${FIREBIRD_VERSION}/extern/SfIO"
xz -9 -v Firebird-${FIREBIRD_VERSION}.tar

