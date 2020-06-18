#
# spec file for package osmo-msc
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


%define with_iu 1
%define _lto_cflags %{nil}
Name:           osmo-msc
Version:        1.6.1
Release:        0
Summary:        Osmocom's MSC for 2G and 3G circuit-switched mobile networks
License:        AGPL-3.0-or-later AND GPL-2.0-only
Group:          Productivity/Telephony/Servers
URL:            https://osmocom.org/projects/osmomsc/wiki
Source:         %{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libdbi-drivers-dbd-sqlite3
BuildRequires:  libtool
BuildRequires:  lksctp-tools-devel
BuildRequires:  pkgconfig >= 0.20
BuildRequires:  pkgconfig(dbi)
BuildRequires:  pkgconfig(libcrypto) >= 0.9.5
BuildRequires:  pkgconfig(libosmo-gsup-client) >= 1.0.0
BuildRequires:  pkgconfig(libosmo-mgcp-client) >= 1.7.0
BuildRequires:  pkgconfig(libosmo-netif) >= 0.6.0
BuildRequires:  pkgconfig(libosmo-sccp) >= 1.1.0
BuildRequires:  pkgconfig(libosmo-sigtran) >= 1.1.0
BuildRequires:  pkgconfig(libosmoabis) >= 0.6.0
BuildRequires:  pkgconfig(libosmocore) >= 1.3.0
BuildRequires:  pkgconfig(libosmoctrl) >= 1.3.0
BuildRequires:  pkgconfig(libosmogsm) >= 1.3.0
BuildRequires:  pkgconfig(libosmovty) >= 1.3.0
BuildRequires:  pkgconfig(libsmpp34) >= 1.13.0
%{?systemd_requires}
%if %{with_iu}
BuildRequires:  pkgconfig(libasn1c) >= 0.9.30
BuildRequires:  pkgconfig(libosmo-ranap) >= 0.3.0
%endif

%description
The Mobile Switching Center (MSC) is the heart of 2G/3G
circuit-switched services.  It terminates the A-interface links from the
Base Station Controllers (BSC) and handles the MM and CC sub-layers of
the Layer 3 protocol from the phones (MS).

This Osmocom implementation of the MSC handles A interfaces via 3GPP
AoIP in an ASP role.  It furthermore implements IETF MGCP against an
external media gateway, such as OsmoMGW.  It does *not* implement MAP
towards a HLR, but the much simpler Osmocom GSUP protocol, which can
be translated to MAP if needed.

%prep
%setup -q

%build
echo "%{version}" >.tarball-version
autoreconf -fi
export CFLAGS="%optflags -fcommon"
%configure \
%if %{with_iu}
  --enable-iu \
%endif
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
%dir %{_docdir}/%{name}/examples
%dir %{_docdir}/%{name}/examples/osmo-msc
%{_docdir}/%{name}/examples/osmo-msc/osmo-msc.cfg
%{_docdir}/%{name}/examples/osmo-msc/osmo-msc_custom-sccp.cfg
%{_docdir}/%{name}/examples/osmo-msc/osmo-msc_multi-cs7.cfg
%{_bindir}/osmo-msc
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}
%dir %{_sysconfdir}/osmocom
%config %{_sysconfdir}/osmocom/osmo-msc.cfg

%changelog
