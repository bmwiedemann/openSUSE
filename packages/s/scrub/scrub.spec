#
# spec file for package scrub
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           scrub
Version:        2.6.1
Release:        1
Summary:        Disk scrubbing program
License:        GPL-2.0
Group:          Productivity/File utilities
Url:            https://code.google.com/p/diskscrub/
Source0:        https://github.com/chaos/scrub/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Scrub writes patterns on files or disk devices to make
retrieving the data more difficult.  It operates in one of three modes: 
1) the special file corresponding to an entire disk is scrubbed 
   and all data on it is destroyed.
2) a regular file is scrubbed and only the data in the file 
   (and optionally its name in the directory entry) is destroyed.
3) a regular file is created, expanded until 
   the file system is full, then scrubbed as in 2).

%prep
%setup -q

%build
%configure --program-prefix=%{?_program_prefix:%{_program_prefix}}
make %{?_smp_mflags}

%check
make check

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog NEWS DISCLAIMER COPYING README
%{_bindir}/scrub
%{_mandir}/man1/*

%changelog
