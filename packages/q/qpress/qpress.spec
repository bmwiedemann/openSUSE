#
# spec file for package qpress
#
# Copyright (c) 2025 Andreas Stieger <andreas.stieger@gmx.de>
# Copyright (c) 2020 SUSE LLC
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


Name:           qpress
Version:        20230507
Release:        0
Summary:        File archiver designed for speed
License:        GPL-1.0-only AND GPL-2.0-only AND GPL-3.0-only
Group:          Productivity/Archiving/Compression
URL:            https://github.com/PierreLvx/qpress
Source0:        https://github.com/PierreLvx/qpress/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  c++_compiler

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
%autosetup -p1

%build
export CFLAGS="%{optflags}"
%if %{do_profiling}
  %make_build CFLAGS="$CFLAGS %{cflags_profile_generate}" LDFLAGS="-fprofile-arcs"
  ./qpress -o *.cpp | ./qpress -dio > /dev/null
  %make_build CFLAGS="$CFLAGS %{cflags_profile_feedback}" LDFLAGS="-fprofile-arcs"
%else
  %make_build
%endif

%install
mkdir -p %{buildroot}/usr/bin
%make_install PREFIX=%{buildroot}/usr

%files
%license LICENSE.GPL-1.0
%license LICENSE.GPL-2.0
%license LICENSE.GPL-3.0
%doc readme.md
%{_bindir}/qpress

%changelog
