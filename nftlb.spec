#
# spec file for package nftlb
#
# Copyright (c) 2023 SUSE LLC
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


Name:           nftlb
Version:        1.0.9
Release:        0
Summary:        nftables load balancer
License:        AGPL-3.0-or-later
Group:          Productivity/Networking/Security
URL:            https://www.zevenet.com/knowledge-base/nftlb/what-is-nftlb/
#Git-Clone:     https://github.com/relianoid/nftlb
Source:         https://github.com/relianoid/nftlb/archive/v%version.tar.gz

BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(jansson) >= 2.3
BuildRequires:  pkgconfig(libev)
BuildRequires:  pkgconfig(libmnl) >= 1.0.4
BuildRequires:  pkgconfig(libnftables) >= 0.9

%description
nftlb a user-space tool that builds a complete load balancer and
traffic distributor using nftables.

* Topologies supported: Destination NAT, Source NAT, Direct Server
  Return and Stateless DNAT. This enables the use of the load
  balancer in one-armed and two-armed network architectures.
* Support for both IPv4 and IPv6 families.
* Multilayer load balancer: DSR in layer 2, IP based load balancing
  with protocol agnostic at layer 3, and support of load balancing of
  UDP, TCP and SCTP at layer 4.
* Multiport support for ranges and lists of ports.
* Multiple virtual services (or farms) support.
* Schedulers available: weight, round robin, configurable hash (per
  IP, port, MAC or combination of them) and symmetric hash.
* Support of configurable persistence or client-backend affinity with
  a timeout (per IP, port, MAC or combination of them).
* Support of security policies per service: white and blacklists
  (from ingress), queuing to user space filter, filtering of bogus
  TCP frames, maximum number of established connections, limit TCP
  RST per second, limit new connections per second and more.
* Priority support per backend.
* Live management of virtual services and backends programmatically
  through a JSON API.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%files
%_sbindir/nftlb
%license LICENSE
%doc README.md

%changelog
