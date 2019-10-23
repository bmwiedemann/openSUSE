#
# spec file for package dbench4
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           dbench4
Version:        4.0
Release:        0
Summary:        File System Benchmark Similar to Netbench
License:        GPL-3.0-only
Group:          System/Benchmark
URL:            https://dbench.samba.org
Source:         https://www.samba.org/ftp/tridge/dbench/dbench-%{version}.tar.gz
Patch1:         fileio_leak_repair.diff
Patch2:         build-fix-paths.diff
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  popt-devel

%description
Dbench is a file system benchmark that generates load patterns similar
to those of the commercial Netbench benchmark, but without requiring a
lab of Windows load generators to run. It is now considered a de facto
standard for generating load on the Linux VFS.

This is version 4 of dbench that does not produce results comparable
with older versions.

%prep
%setup -q -n dbench-%{version}
%patch1 -p1
%patch2 -p1

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc README
%dir %{_datadir}/dbench4
%attr(644,root,root) %{_datadir}/dbench4/client.txt
%{_mandir}/man1/dbench4.1%{?ext_man}
%{_mandir}/man1/tbench4.1%{?ext_man}
%{_mandir}/man1/tbench4_srv.1%{?ext_man}
%{_bindir}/dbench4
%{_bindir}/tbench4
%{_bindir}/tbench4_srv

%changelog
