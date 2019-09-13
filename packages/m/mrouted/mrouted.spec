#
# spec file for package mrouted
#
# Copyright (c) 2018, Martin Hauke <mardnh@gmx.de>
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


Name:           mrouted
Version:        3.9.8
Release:        0
Summary:        An implementation of the DVMRP multicast routing protocol
License:        BSD-3-Clause AND BSD-4-Clause
Group:          Productivity/Networking/Routing
URL:            https://github.com/troglobit/mrouted
#Git-Clone:     https://github.com/troglobit/mrouted.git
Source:         https://github.com/troglobit/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  bison

%description
Mrouted is an implementation of the Distance-Vector Multicast Routing
Protocol (DVMRP), an earlier version of which is specified in RFC-1075.

Mrouted turns a UNIX workstation into a DVMRP multicast router with tunnel
support, in order to cross non-multicast-aware routers.  The tunnels are
virtual point-to-point, IP-IP tunnel, links between a pair of mrouted routers.

%prep
%setup -q

%build
./configure
make %{?_smp_mflags}

%install
%make_install prefix=/usr
rm -rf %{buildroot}/%{_datadir}/doc

%files
%doc AUTHORS ChangeLog README.md
%license LICENSE
%{_sbindir}/map-mbone
%{_sbindir}/mrinfo
%{_sbindir}/mrouted
%{_sbindir}/mtrace
%config %{_sysconfdir}/mrouted.conf
%{_mandir}/man8/map-mbone.8%{?ext_man}
%{_mandir}/man8/mrinfo.8%{?ext_man}
%{_mandir}/man8/mrouted.8%{?ext_man}
%{_mandir}/man8/mtrace.8%{?ext_man}

%changelog
