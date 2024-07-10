#
# spec file for package osmo-mgw
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2017-2021, Martin Hauke <mardnh@gmx.de>
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


Name:           osmo-mgw
Version:        1.9.0
Release:        0
Summary:        Osmocom's Media Gateway for 2G and 3G circuit-switched mobile networks
License:        AGPL-3.0-or-later AND GPL-2.0-or-later
Group:          Hardware/Mobile
URL:            https://osmocom.org/projects/osmo-mgw
Source:         %{name}-%{version}.tar.xz
Patch0:         fix-build.patch
Patch1:         harden_osmo-mgw.service.patch
BuildRequires:  automake >= 1.9
BuildRequires:  libtool >= 2
BuildRequires:  pkgconfig >= 0.20
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libosmo-netif) >= 1.1.0
BuildRequires:  pkgconfig(libosmoabis) >= 1.2.0
BuildRequires:  pkgconfig(libosmocodec) >= 1.6.0
BuildRequires:  pkgconfig(libosmocore) >= 1.6.0
BuildRequires:  pkgconfig(libosmoctrl) >= 1.6.0
BuildRequires:  pkgconfig(libosmogsm) >= 1.6.0
BuildRequires:  pkgconfig(libosmotrau) >= 1.2.0
BuildRequires:  pkgconfig(libosmovty) >= 1.6.0
%{?systemd_requires}

%description
OsmoMGW is Osmocom's Media Gateway for 2G and 3G circuit-switched mobile networks.

%package -n libosmo-mgcp-client9
Summary:        Osmocom's Media Gateway Control Protocol client library
Group:          System/Libraries

%description -n libosmo-mgcp-client9
Osmocom's Media Gateway Control Protocol client library.

%package -n libosmo-mgcp-client-devel
Summary:        Development files for Osmocom's Media Gateway Control Protocol client library
Group:          Development/Libraries/C and C++
Requires:       libosmo-mgcp-client9 = %{version}

%description -n libosmo-mgcp-client-devel
Osmocom's Media Gateway Control Protocol client librarary.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmo-mgcp-client.

%package -n libosmo-mgcp-devel
Summary:        Development files for Osmocom's Media Gateway server library
Group:          Development/Libraries/C and C++

%description -n libosmo-mgcp-devel
Osmocom's Media Gateway Control Protocol server library.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmo-mgcp.

%prep
%autosetup -p1

%build
echo "%{version}" >.tarball-version
autoreconf -fi
%configure \
  --disable-static \
  --docdir=%{_docdir}/%{name} \
  --with-systemdsystemunitdir=%{_unitdir}

make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

install -d "%{buildroot}/%{_sbindir}"
ln -s service "%{buildroot}/%{_sbindir}/rcosmo-mgw"

%check
make %{?_smp_mflags} check || (find . -name testsuite.log -exec cat {} +)

%post   -n libosmo-mgcp-client9 -p /sbin/ldconfig
%postun -n libosmo-mgcp-client9 -p /sbin/ldconfig

%preun
%service_del_preun osmo-mgw.service

%postun
%service_del_postun osmo-mgw.service

%pre
%service_add_pre osmo-mgw.service

%post
%service_add_post osmo-mgw.service

%files
%license COPYING
%doc AUTHORS README
%dir %{_docdir}/%{name}/examples
%dir %{_docdir}/%{name}/examples/osmo-mgw
%{_docdir}/%{name}/examples/osmo-mgw/osmo-mgw.cfg
%{_docdir}/%{name}/examples/osmo-mgw/osmo-mgw-abis_e1.cfg
%{_bindir}/osmo-mgw
%{_unitdir}/osmo-mgw.service
%{_sbindir}/rcosmo-mgw
%dir %{_sysconfdir}/osmocom
%config(noreplace) %{_sysconfdir}/osmocom/osmo-mgw.cfg

%files -n libosmo-mgcp-client9
%{_libdir}/libosmo-mgcp-client.so.9*

%files -n libosmo-mgcp-client-devel
%{_libdir}/libosmo-mgcp-client.so
%{_libdir}/pkgconfig/libosmo-mgcp-client.pc
%dir %{_includedir}/osmocom
%dir %{_includedir}/osmocom/mgcp_client
%{_includedir}/osmocom/mgcp_client/*.h

%files -n libosmo-mgcp-devel
%dir %{_includedir}/osmocom
%dir %{_includedir}/osmocom/mgcp
%{_includedir}/osmocom/mgcp/*.h

%changelog
