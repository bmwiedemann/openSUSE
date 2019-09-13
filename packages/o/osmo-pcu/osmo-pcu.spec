#
# spec file for package osmo-pcu
#
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           osmo-pcu
Version:        0.6.0
Release:        0
Summary:        Osmocom GPRS Packet Control Unit (PCU)
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          Productivity/Telephony/Servers
URL:            https://osmocom.org/projects/osmopcu/wiki/OsmoPCU
Source:         %{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig >= 0.20
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libosmocore) >= 0.12.0
BuildRequires:  pkgconfig(libosmogb) >= 0.12.0
BuildRequires:  pkgconfig(libosmogsm) >= 0.12.0
BuildRequires:  pkgconfig(libosmovty) >= 0.12.0
%{?systemd_ordering}

%description
Osmocom PCU code (RLC/MAC/PCU) for OpenBTS and OsmoBTS.

%prep
%setup -q

%build
echo "%{version}" >.tarball-version
autoreconf -fi
%configure \
  --enable-shared \
  --disable-static \
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
make %{?_smp_mflags} check || find . -name testsuite.log -exec cat {} +

%files
%license COPYING
%doc README.md
%doc %{_docdir}/%{name}/examples
%{_bindir}/osmo-pcu
%dir %{_sysconfdir}/osmocom
%config(noreplace) %{_sysconfdir}/osmocom/osmo-pcu.cfg
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}
%dir %{_includedir}/osmocom
%dir %{_includedir}/osmocom/pcu
%{_includedir}/osmocom/pcu/pcuif_proto.h
%{_libdir}/pkgconfig/osmo-pcu.pc

%changelog
