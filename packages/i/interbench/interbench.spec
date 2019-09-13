#
# spec file for package interbench
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


Name:           interbench
Version:        0.31
Release:        0
Summary:        Tool to benchmark interactivity in Linux
License:        GPL-2.0
Group:          System/Benchmark
Url:            http://users.on.net/~ckolivas/interbench/
Source0:        http://ck.kolivas.org/apps/interbench/interbench-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This benchmark application is designed to benchmark interactivity in Linux. See
the included file readme.interactivity for a brief definition.

It is designed to measure the effect of changes in Linux kernel design or system
configuration changes such as cpu, I/O scheduler and filesystem changes and
options. With careful benchmarking, different hardware can be compared.

%prep
%setup -q

%build
make %{?_smp_mflags} clean
make %{?_smp_mflags} CFLAGS="%{optflags}" LDLIBS="-lrt -lm"

%install
install -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -m 0644 %{name}.8 %{buildroot}%{_mandir}/man8/%{name}.8

%files
%defattr(-,root,root)
%doc COPYING readme readme.interactivity
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.*

%changelog
