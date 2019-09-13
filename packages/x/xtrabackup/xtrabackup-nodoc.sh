#!/usr/bin/env bash
#
# Remove documentation files from source archives 
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

XTRABACKUP_VERSION=`rpm -q --queryformat "%{version}\n" --specfile xtrabackup.spec | head -n1`

gunzip -v < percona-xtrabackup-${XTRABACKUP_VERSION}.tar.gz > percona-xtrabackup-${XTRABACKUP_VERSION}.tar && \
tar -v --wildcards --delete -f percona-xtrabackup-${XTRABACKUP_VERSION}.tar \
	"percona-xtrabackup-${XTRABACKUP_VERSION}/Docs" \
	"percona-xtrabackup-${XTRABACKUP_VERSION}/storage/innobase/xtrabackup/doc" \
	&& \
mv -v percona-xtrabackup-${XTRABACKUP_VERSION}.tar percona-xtrabackup-${XTRABACKUP_VERSION}-nodoc.tar && \
xz -9 -v percona-xtrabackup-${XTRABACKUP_VERSION}-nodoc.tar

