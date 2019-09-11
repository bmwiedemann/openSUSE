#
# spec file for package subnetcalc
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           subnetcalc
Version:        2.4.3
Release:        0
Summary:        IPv4/IPv6 Subnet Calculator
Group:          Productivity/Networking/Routing
License:        GPL-3.0+
Url:            https://www.uni-due.de/~be0001/subnetcalc/
Source:         https://www.uni-due.de/~be0001/subnetcalc/download/%{name}-%{version}.tar.gz
BuildRequires:  GeoIP-devel
BuildRequires:  gcc-c++
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
%configure
make %{?_smp_mflags}

%install
%make_install

%check
%{buildroot}%{_bindir}/%name 192.168.1.0/255.255.0.0

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%if 0%{?leap_version} >= 420200 || 0%{?suse_version} > 1320
%license COPYING
%else
%doc COPYING
%endif
%{_bindir}/%name
%{_mandir}/man1/%name.1*

%changelog
