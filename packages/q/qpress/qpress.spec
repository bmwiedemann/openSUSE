#
# spec file for package qpress
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013 Andreas Stieger <andreas.stieger@gmx.de>
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


Name:           qpress
Version:        1.1
Release:        0
Summary:        File archiver designed for speed
License:        GPL-2.0
Group:          Productivity/Archiving/Compression
Url:            http://www.quicklz.com/
Source0:        http://www.quicklz.com/%{name}-11-source.zip
Source1:        COPYING
Patch0:         qpress-1.1-isatty-include.patch
BuildRequires:  gcc-c++
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
qpress is a portable file archiver using QuickLZ and designed to utilize
fast storage systems to their max. It's often faster than file copy
because the destination is smaller than the source. A few features:

* multiple cores, reaching upto 1.1 Gbyte/s in-memory compression on a
  quad core i7
* 64-bit file sizes and tested with terabyte sized archives containing
  millions of files and directories
* pipes and redirection and *nix-like behaviour for scripting and
  flexibility
* Adler32 checksums to ensure that decompressed data has not been corrupted
* data recovery of damaged archives with 64 Kbyte grannularity

%prep
%setup -q -c
%patch0 -p1
cp %{SOURCE1} .

%build
c++ %{optflags} -o qpress qpress.cpp aio.cpp quicklz.c utilities.cpp -lpthread

%install
install -D -m 0755 qpress %{buildroot}%{_bindir}/qpress

%files
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/qpress

%changelog
