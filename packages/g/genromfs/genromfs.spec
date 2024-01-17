#
# spec file for package genromfs
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


Name:           genromfs
Version:        0.5.7
Release:        0
Summary:        Utility for Creating romfs File Systems
License:        GPL-2.0-or-later
Group:          System/Boot
URL:            http://romfs.sourceforge.net
Source:         https://github.com/chexum/genromfs/archive/refs/tags/%version.tar.gz

%description
Genromfs is a tool for creating romfs file systems, which are
lightweight, read-only file systems supported by the Linux kernel.
Romfs file systems were traditionally used for the initial RAM disks
used during installation.

%prep
%autosetup

%build
%make_build CC="gcc" CFLAGS="%{optflags} -DVERSION=\\\"%{version}\\\"" LDFLAGS=

%install
%make_install PREFIX="%{buildroot}" mandir="%{_mandir}"

%files
%license COPYING
%doc NEWS ChangeLog genromfs.lsm romfs.txt
%doc %{_mandir}/man8/genromfs.8.gz
%{_bindir}/genromfs

%changelog
