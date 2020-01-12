#
# spec file for package osmo-pcap
#
# Copyright (c) 2015, Martin Hauke <mardnh@gmx.de>
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

Name:           osmo-pcap
Version:        0.1.2
Release:        0
Summary:        Osmocom's PCAP client and server
License:        AGPL-3.0-or-later AND GPL-2.0-or-later
Group:          Productivity/Telephony/Servers
URL:            https://openbsc.osmocom.org
Source:         %{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake >= 1.6
BuildRequires:  libpcap-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libosmocore) >= 0.11.0
BuildRequires:  pkgconfig(libosmogb)
BuildRequires:  pkgconfig(libosmogsm) >= 0.11.0
BuildRequires:  pkgconfig(libosmovty) >= 0.11.0
BuildRequires:  pkgconfig(libzmq) >= 3.2.2

%description
Osmocom tools to help with pcap tracing.
Run osmo_pcap_client locally and send traces to a different system.

%prep
%setup -q

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
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rcosmo-pcap-client
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rcosmo-pcap-server

%preun
%service_del_preun osmo-pcap-client.service osmo-pcap-server.service

%postun
%service_del_postun osmo-pcap-client.service osmo-pcap-server.service

%pre
%service_add_pre osmo-pcap-client.service osmo-pcap-server.service

%post
%service_add_post osmo-pcap-client.service osmo-pcap-server.service

%check
make %{?_smp_mflags} check || (find . -name testsuite.log -exec cat {} +)

%files
%license COPYING
%doc AUTHORS
%doc %{_docdir}/%{name}/examples
%dir %{_sysconfdir}/osmocom
%config(noreplace) %{_sysconfdir}/osmocom/osmo-pcap-client.cfg
%config(noreplace) %{_sysconfdir}/osmocom/osmo-pcap-server.cfg
%{_bindir}/osmo-pcap-client
%{_bindir}/osmo-pcap-server
%{_unitdir}/osmo-pcap-client.service
%{_unitdir}/osmo-pcap-server.service
%dir %{_datadir}/osmo-pcap
%{_datadir}/osmo-pcap/osmo_pcap_clean_old
%{_sbindir}/rcosmo-pcap-client
%{_sbindir}/rcosmo-pcap-server

%changelog
