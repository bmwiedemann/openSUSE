#
# spec file for package hackbench
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


Name:           hackbench
Version:        svn1649
Release:        0
Summary:        Performance, overhead, and scalability benchmark for the Linux scheduler
License:        GPL-2.0+
Group:          System/Benchmark
Url:            http://devresources.linux-foundation.org/craiger/hackbench/
Source0:        %{name}-%{version}.tar.bz2
Patch0:         gcc-warning-fixes.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The hackbench test is a benchmark for measuring the performance,
overhead, and scalability of the Linux scheduler.

%prep
%setup -q
%patch0

%build
cc %{optflags} hackbench.c -o hackbench

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 755 hackbench %{buildroot}/%{_bindir}
install -m 755 hackbench_run.sh %{buildroot}/%{_bindir}
install -m 755 hackbench_plot.sh %{buildroot}/%{_bindir}

%files
%defattr(-, root, root)
%doc README
%{_bindir}/hackbench
%{_bindir}/hackbench_run.sh
%{_bindir}/hackbench_plot.sh

%changelog
