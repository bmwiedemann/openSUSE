#
# spec file for package osmo-sgsn
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

%define with_iu 1
Name:           osmo-sgsn
Version:        1.6.2
Release:        0
Summary:        Osmocom's SGSN for 2G and 3G packet-switched mobile networks
License:        AGPL-3.0-or-later AND GPL-2.0-or-later
Group:          Productivity/Telephony/Servers
URL:            https://osmocom.org/projects/osmosgsn/wiki/OsmoSGSN
Source:         %{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(libcrypto) >= 0.9.5
BuildRequires:  pkgconfig(libgtp) >= 1.5.0
BuildRequires:  pkgconfig(libosmo-gsup-client) >= 1.0.0
BuildRequires:  pkgconfig(libosmo-netif) >= 0.4.0
BuildRequires:  pkgconfig(libosmoabis) >= 0.6.0
BuildRequires:  pkgconfig(libosmocore) >= 1.2.0
BuildRequires:  pkgconfig(libosmoctrl) >= 1.2.0
BuildRequires:  pkgconfig(libosmogb) >= 1.2.0
BuildRequires:  pkgconfig(libosmogsm) >= 1.2.0
BuildRequires:  pkgconfig(libosmovty) >= 1.2.0
%{?systemd_requires}
%if %{with_iu}
BuildRequires:  pkgconfig(libasn1c) >= 0.9.30
BuildRequires:  pkgconfig(libosmo-ranap) >= 0.6.0
BuildRequires:  pkgconfig(libosmo-sigtran) >= 1.0.0
%endif

%description
OsmoSGSN is Osmocom's Serving GPRS Support Node for 2G and 3G
packet-switched mobile networks.

%package -n osmo-gtphub
Summary:        Osmocom GTP Hub: Proxy for GTP traffic between multiple SGSNs and GGSNs
Group:          Productivity/Telephony/Servers

%description -n osmo-gtphub
Osmocom GTP Hub: Proxy for GTP traffic between multiple SGSNs and GGSNs.

%package -n osmo-gbproxy
Summary:        Osmocom GPRS Gb Interface Proxy
Group:          Productivity/Telephony/Servers

%description -n osmo-gbproxy
The purpose of the Gb proxy is to aggregate the Gb links of multiple
BSS's and present them in one Gb link to the SGSN.

%prep
%setup -q

%build
echo "%{version}" >.tarball-version
autoreconf -fi
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
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rcosmo-gbproxy
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rcosmo-gtphub
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rcosmo-sgsn

%preun
%service_del_preun %{name}.service
%postun
%service_del_postun %{name}.service
%pre
%service_add_pre %{name}.service
%post
%service_add_post %{name}.service

%preun -n osmo-gtphub
%service_del_preun osmo-gtphub.service
%postun -n osmo-gtphub
%service_del_postun osmo-gtphub.service
%pre -n osmo-gtphub
%service_add_pre osmo-gtphub.service
%post -n osmo-gtphub
%service_add_post osmo-gtphub.service

%preun -n osmo-gbproxy
%service_del_preun osmo-gbproxy.service
%postun -n osmo-gbproxy
%service_del_postun osmo-gbproxy.service
%pre -n osmo-gbproxy
%service_add_pre osmo-gbproxy.service
%post -n osmo-gbproxy
%service_add_post osmo-gbproxy.service

%check
make %{?_smp_mflags} check || (find . -name testsuite.log -exec cat {} +)

%files
%doc AUTHORS README
%dir %{_docdir}/%{name}/examples
%dir %{_docdir}/%{name}/examples/osmo-sgsn
%exclude %{_docdir}/%{name}/examples/osmo-gtphub
%exclude %{_docdir}/%{name}/examples/osmo-gbproxy
%{_docdir}/%{name}/examples/osmo-sgsn/osmo-sgsn-accept-all.cfg
%{_docdir}/%{name}/examples/osmo-sgsn/osmo-sgsn_custom-sccp.cfg
%{_docdir}/%{name}/examples/osmo-sgsn/osmo-sgsn.cfg
%{_bindir}/osmo-sgsn
%dir %{_sysconfdir}/osmocom
%config %{_sysconfdir}/osmocom/osmo-sgsn.cfg
%{_unitdir}/%{name}.service
%{_sbindir}/rcosmo-sgsn

%files -n osmo-gtphub
%dir %{_docdir}/%{name}/examples
%dir %{_docdir}/%{name}/examples/osmo-gtphub
%{_docdir}/%{name}/examples/osmo-gtphub/osmo-gtphub-1iface.cfg
%{_docdir}/%{name}/examples/osmo-gtphub/osmo-gtphub.cfg
%{_bindir}/osmo-gtphub
%dir %{_sysconfdir}/osmocom
%config %{_sysconfdir}/osmocom/osmo-gtphub.cfg
%{_unitdir}/osmo-gtphub.service
%{_sbindir}/rcosmo-gtphub

%files -n osmo-gbproxy
%dir %{_docdir}/%{name}/examples
%dir %{_docdir}/%{name}/examples/osmo-gbproxy
%{_docdir}/%{name}/examples/osmo-gbproxy/osmo-gbproxy-legacy.cfg
%{_docdir}/%{name}/examples/osmo-gbproxy/osmo-gbproxy.cfg
%{_bindir}/osmo-gbproxy
%dir %{_sysconfdir}/osmocom
%config %{_sysconfdir}/osmocom/osmo-gbproxy.cfg
%{_unitdir}/osmo-gbproxy.service
%{_sbindir}/rcosmo-gbproxy

%changelog
