#
# spec file for package dbench
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           dbench
Version:        3.04
Release:        0
Summary:        File System Benchmark Similar to Netbench
License:        GPL-2.0+
Group:          System/Benchmark
Url:            http://dbench.samba.org/
Source:         http://samba.org/ftp/tridge/dbench/%{name}-%{version}.tar.gz
Patch1:         verbose.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Dbench is a file system benchmark that generates load patterns similar
to those of the commercial Netbench benchmark, but without requiring a
lab of Windows load generators to run. It is now considered a de facto
standard for generating load on the Linux VFS.

%prep
%setup -q
%patch1 -p1

%build
%configure --datadir="%{_datadir}/dbench"
make %{?_smp_mflags}

%install
# install dbench
make install prefix="%{buildroot}/%{_prefix}" bindir="%{buildroot}/%{_bindir}" \
	datadir="%{buildroot}/%{_datadir}/dbench" mandir="%{buildroot}/%{_mandir}/man1"
mkdir -p %{buildroot}/%{_docdir}/dbench
install -m 644 README %{buildroot}/%{_docdir}/dbench/README
# create directories
find %{buildroot}%{_datadir}/dbench -name "*.txt" -type f -print0 | xargs -r -0 chmod a-x

%files
%defattr(-,root,root)
%{_bindir}/dbench
%{_bindir}/tbench
%{_bindir}/tbench_srv
%{_mandir}/man1/dbench.1.gz
%{_mandir}/man1/tbench.1.gz
%{_mandir}/man1/tbench_srv.1.gz
%{_datadir}/dbench
%doc %{_docdir}/dbench

%changelog
