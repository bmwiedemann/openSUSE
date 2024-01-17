#
# spec file for package jfsutils
#
# Copyright (c) 2022 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           jfsutils
Version:        1.1.15
Release:        0
Summary:        IBM JFS Utility Programs
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            http://jfs.sourceforge.net/
Source0:        http://jfs.sourceforge.net/project/pub/%{name}-%{version}.tar.gz
Source1:        jfs.pdf
Source2:        jfslayout.pdf
Source3:        jfslog.pdf
Source4:        jfsroot.html
Source5:        jfs.txt
Patch1:         jfs-headers.patch
Patch2:         sysmacros.patch
Patch3:         libfs-Fixing-issue-with-variable-name-collision.patch
Patch4:         jfsutils_format-security_ftbs.patch
BuildRequires:  e2fsprogs-devel
Provides:       jfsprogs = %{version}
Obsoletes:      jfsprogs < %{version}
Supplements:    filesystem(jfs)

%description
This package contains utilities for managing IBM's Journaled File
System (JFS) under Linux.  The following utilities are available:

o fsck.jfs--initiate replay of the JFS transaction log and check and
repair a JFS formatted device o logdump--dump a JFS formatted device's
journal log o logredo--replay a JFS formatted device's journal log o
mkfs.jfs--create a JFS formatted partition o xchkdmp--dump the contents
of a JFS fsck log file created with xchklog o xchklog--extract a log
from the JFS fsck workspace into a file o xpeek--shell-type JFS file
system editor

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
sed -i -e 's@^\./"@\." @' fsck/jfs_fsck.8 \
	 fscklog/jfs_fscklog.8 \
	 logdump/jfs_logdump.8 \
	 mkfs/jfs_mkfs.8 \
	 tune/jfs_tune.8 \
	 xpeek/jfs_debugfs.8
tail +35 mkfs/jfs_mkfs.8 | head -10
%configure
make %{?_smp_mflags}

%install
mkdir ./jfsdocs
install -m 644 %{SOURCE1} ./jfsdocs
install -m 644 %{SOURCE2} ./jfsdocs
install -m 644 %{SOURCE3} ./jfsdocs
install -m 644 %{SOURCE4} ./jfsdocs
install -m 644 %{SOURCE5} ./jfsdocs
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%files
%license COPYING
%doc AUTHORS NEWS ChangeLog jfsdocs/*
%{_mandir}/man8/*
%{_sbindir}/*

%changelog
