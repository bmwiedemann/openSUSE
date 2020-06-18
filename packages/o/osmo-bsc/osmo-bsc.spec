#
# spec file for package osmo-bsc
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
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


%define _lto_cflags %{nil}

Name:           osmo-bsc
Version:        1.6.0
Release:        0
Summary:        OsmoBSC: Osmocom's Base Station Controller for 2G CS mobile networks
License:        AGPL-3.0-or-later AND GPL-2.0-or-later
Group:          Hardware/Mobile
URL:            https://osmocom.org/projects/openbsc/wiki/Osmo-bsc
Source:         %{name}-%{version}.tar.xz
Patch0:         0001-handorer.h-Fix-compilation-with-gcc-10.patch
BuildRequires:  automake >= 1.9
BuildRequires:  libtool >= 2
BuildRequires:  pkgconfig >= 0.20
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libcrypto) >= 0.9.5
BuildRequires:  pkgconfig(libosmo-mgcp-client) >= 1.6.0
BuildRequires:  pkgconfig(libosmo-netif) >= 0.6.0
BuildRequires:  pkgconfig(libosmo-sccp) >= 0.10.0
BuildRequires:  pkgconfig(libosmo-sigtran) >= 0.10.0
BuildRequires:  pkgconfig(libosmoabis) >= 0.6.0
BuildRequires:  pkgconfig(libosmocore) >= 1.3.0
BuildRequires:  pkgconfig(libosmoctrl) >= 1.3.0
BuildRequires:  pkgconfig(libosmogb)
BuildRequires:  pkgconfig(libosmogsm) >= 1.3.0
BuildRequires:  pkgconfig(libosmovty) >= 1.3.0
BuildRequires:  pkgconfig(talloc)
%{?systemd_requires}

%description
OsmoBSC: Osmocom's Base Station Controller for 2G circuit-switched mobile networks.

%package abisip-find
Summary:        CLI utility to find ip.access compatible BTS
License:        GPL-2.0-or-later
Group:          Productivity/Telephony/Utilities

%description abisip-find
Command line utility to find ip.access compatible BTS.

%package ipaccess-utils
Summary:        Command line utilities for ip.access nanoBTS
License:        GPL-2.0-or-later
Group:          Productivity/Telephony/Utilities

%description ipaccess-utils
This package contains utilities that are specific for nanoBTS when being
used together with OpenBSC. It contains mainly two tools: ipaccess-config
and ipaccess-proxy.

%package bs11-utils
Summary:        Command line utilities for Siemens BS-11 BTS
License:        GPL-2.0-or-later
Group:          Productivity/Telephony/Utilities
Conflicts:      openbsc-bs11-utils

%description bs11-utils
There is a tool in this package for configuring the Siemens BS-11 BTS.
Additionally, it contains one tool for making use of an ISDN-card and the
public telephone network as frequency standard for the E1 line.

%package meas-utils
Summary:        Command line utilities for OsmoBSC's measurement reports
License:        GPL-2.0-or-later
Group:          Productivity/Telephony/Utilities

%description meas-utils
This package contains utilities for handling OsmoBSC's measurement reports
 * meas_json to convert measurement feed into a JSON feed

%prep
%setup -q
%patch0 -p1

%build
echo "%{version}" >.tarball-version
autoreconf -fi
%configure \
  --docdir=%{_docdir}/%{name} \
  --with-systemdsystemunitdir=%{_unitdir}
make %{?_smp_mflags}

%install
%make_install
install -d %{buildroot}/%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rc%{name}

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%check
make %{?_smp_mflags} check || (find . -name testsuite.log -exec cat {} +)

%files
%license COPYING
%doc AUTHORS README
%{_bindir}/osmo-bsc
%dir %{_docdir}/%{name}/examples
%dir %{_docdir}/%{name}/examples/osmo-bsc
%{_docdir}/%{name}/examples/osmo-bsc/osmo-bsc.cfg
%{_docdir}/%{name}/examples/osmo-bsc/osmo-bsc_custom-sccp.cfg
%{_docdir}/%{name}/examples/osmo-bsc/osmo-bsc-minimal.cfg
%dir %{_sysconfdir}/osmocom
%config %{_sysconfdir}/osmocom/osmo-bsc.cfg
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}

%files abisip-find
%{_bindir}/abisip-find

%files ipaccess-utils
%{_bindir}/ipaccess-config
%{_bindir}/ipaccess-proxy

%files bs11-utils
%{_bindir}/bs11_config
%{_bindir}/isdnsync

%files meas-utils
%{_bindir}/meas_json

%changelog
