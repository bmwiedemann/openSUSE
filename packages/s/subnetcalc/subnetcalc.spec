#
# spec file for package subnetcalc
#
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


Name:           subnetcalc
Version:        2.4.16
Release:        0
Summary:        IPv4/IPv6 Subnet Calculator
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Routing
URL:            https://www.uni-due.de/~be0001/subnetcalc/
Source:         https://www.uni-due.de/~be0001/subnetcalc/download/%{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
SubNetCalc is an IPv4/IPv6 subnet address calculator. For a given IPv4 or IPv6
address and netmask or prefix length, it calculates network address, broadcast
address, maximum number of hosts and host address range. It also prints the
addresses in binary format for better understandability. Furthermore, it
prints information on specific address types (e.g. type, scope,
interface ID, etc.).

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%{buildroot}%{_bindir}/%{name} 192.168.1.0/255.255.0.0

%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
