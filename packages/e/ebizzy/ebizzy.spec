#
# spec file for package ebizzy
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


Name:           ebizzy
Version:        0.3
Release:        0
Summary:        Web server applicatin workload generator
License:        GPL-2.0
Group:          System/Benchmark
Url:            http://ebizzy.sf.net
Source:         http://sourceforge.net/projects/ebizzy/files/ebizzy/%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
ebizzy is designed to generate a workload resembling common web application
server workloads. It is highly threaded, has a large in-memory working set, and
allocates and deallocates memory frequently.

%prep
%setup -q

%build
gcc %{optflags} -Wshadow -pthread -o ebizzy ebizzy.c

%install
install -m 0755 -D ebizzy %{buildroot}/%{_bindir}/ebizzy

%files
%defattr(-,root,root)
%doc ChangeLog README LICENSE
%{_bindir}/ebizzy
