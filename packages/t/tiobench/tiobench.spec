#
# spec file for package tiobench
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           tiobench
Version:        0.4.1
Release:        0
Summary:        Fully-threaded I/O benchmark program
License:        GPL-2.0
Group:          System/Benchmark
Url:            http://sourceforge.net/projects/tiobench
Source:         tiobench-%{version}.tar.bz2
Patch1:         tiobench-moredigits.diff
Patch2:         tiobench-warnings-makefile.diff
Patch3:         tiobench-rename-conflicting-functions.diff
Recommends:     perl(Term::ProgressBar)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A simple multithreaded I/O benchmark, popular amongst kernel developers.
The results tend to be realistic enough to have some bearing on real
world results, while the tests are simple enough for kernel engineers to
analyze changes ...

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
make CFLAGS="%{optflags} -fgnu89-inline" %{?_smp_mflags}

%install
make install PREFIX="%{buildroot}%{_prefix}" DOCDIR="%{buildroot}%{_docdir}/%{name}"
chmod -x %{buildroot}%{_docdir}/%{name}/*

%files
%defattr(-,root,root)
%{_bindir}/tio*
%doc %{_docdir}/%{name}

%changelog
