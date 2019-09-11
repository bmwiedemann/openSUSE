#
# spec file for package gpart
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gpart
Version:        0.3
Release:        0
Summary:        Tool That Can Guess a Lost Partition Table
License:        GPL-2.0+
Group:          System/Filesystems
Url:            http://www.brzitwa.de/mb/gpart/index.html
Source:         https://github.com/baruch/gpart/archive/%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake

%description
Gpart is a small tool that tries to guess what partitions are on a PC
type hard disk in case the primary partition table was damaged. Gpart
supports, among others, partitions formatted as ext2, FAT 12/16/32,
ReiserFS, NTFS, and HPFS. Read the file
%{_docdir}/gpart/README and the gpart man page before
using gpart.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install
rm -rf %{buildroot}%{_datadir}/doc

%files
%defattr(-,root,root)
%doc COPYING Changes LSM README.md
%{_sbindir}/gpart
%{_mandir}/man8/gpart.8%{ext_man}

%changelog
