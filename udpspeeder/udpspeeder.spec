#
# spec file for package udpspeeder
#
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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

Name:           udpspeeder
Version:        20190121.0
Release:        0
Summary:        A tunnel which can improve network quality by using FEC
# Bundled libev is licenced under GPL-3.0+ or BSD-2-Clause
License:        MIT
Group:          Productivity/Networking/Other
URL:            https://github.com/wangyu-/UDPspeeder/archive/%{version}.tar.gz
#Git-Clone:     https://github.com/wangyu-/UDPspeeder.git
Source:         https://github.com/wangyu-/UDPspeeder/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++

%description
A tunnel which can improve network quality on high-latency and
lossy links by using Forward Error Correction, for all kinds of
traffic (TCP/UDP/ICMP).

When used alone, UDPspeeder improves only the UDP connection. By using
UDPspeeder and a UDP-based VPN together, any traffic can be improved.
Currently, OpenVPN/L2TP/ShadowVPN are known to be supported.

%prep
%setup -q -n UDPspeeder-%{version}
sed -i 's|-ggdb||' makefile
sed -i 's|-static||' makefile
sed -i 's|$(shell git rev-parse HEAD)|%{version}|g' makefile

%build
export OPT='%{optflags}'
make %{?_smp_mflags}

%install
install -D -m 0755 speederv2 %{buildroot}/%{_bindir}/speederv2

%files
%license LICENSE.md
%doc README.md doc/udpspeeder_openvpn.md
%{_bindir}/speederv2

%changelog
