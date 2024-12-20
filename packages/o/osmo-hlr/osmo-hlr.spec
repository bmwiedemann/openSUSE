#
# spec file for package osmo-hlr
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2016-2021, Martin Hauke <mardnh@gmx.de>
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


Name:           osmo-hlr
Version:        1.4.0
Release:        0
Summary:        Osmocom Home Location Register for GSUP protocol towards OsmoSGSN and OsmoCSCN
License:        AGPL-3.0-or-later AND GPL-2.0-or-later
Group:          Productivity/Telephony/Servers
URL:            https://projects.osmocom.org/projects/osmo-hlr
Source:         %{name}-%{version}.tar.xz
Patch0:         harden_osmo-hlr.service.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig >= 0.20
BuildRequires:  python3
BuildRequires:  sqlite3
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libosmoabis) >= 1.1.0
BuildRequires:  pkgconfig(libosmocore) >= 1.5.0
BuildRequires:  pkgconfig(libosmoctrl) >= 1.5.0
BuildRequires:  pkgconfig(libosmogsm) >= 1.5.0
BuildRequires:  pkgconfig(libosmovty) >= 1.5.0
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(talloc) >= 2.0.1
# only needed for populate_hlr_db.pl
Requires:       libdbi-drivers-dbd-sqlite3

%description
The GSUP HLR is a stand-alone HLR (Home Location Register) for SIM
and USIM based subscribers which exposes the GSUP protocol towards
its users. OsmoSGSN supports this protocol.

osmo-gsup-hlr is still very simplistic. It is a single-threaded
architecture and uses only sqlite3 tables as back-end.  It is suitable
for installations of the scale that OsmoNITB was able to handle.  It
also lacks various features like fine-grained control of subscribed
services (like supplementary services).

%package -n libosmo-gsup-client0
Summary:        Osmocom GSUP (General Subscriber Update Protocol) client library
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n libosmo-gsup-client0
This is a shared library that can be used to implement client programs for
the GSUP protocol. The typical GSUP server is OsmoHLR, with OsmoMSC, OsmoSGSN
and External USSD Entities (EUSEs) using this library to implement clients.

%package -n libosmo-gsup-client-devel
Summary:        Development files for the Osmocom GSUP client library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libosmo-gsup-client0 = %{version}

%description -n libosmo-gsup-client-devel
This is a shared library that can be used to implement client programs for
the GSUP protocol. The typical GSUP server is OsmoHLR, with OsmoMSC, OsmoSGSN
and External USSD Entities (EUSEs) using this library to implement clients.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmo-gsup-client.

%package -n libosmo-mslookup0
Summary:        Osmocom MS lookup library
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n libosmo-mslookup0
This shared library contains routines for looking up mobile subscribers.

%package -n libosmo-mslookup-devel
Summary:        Development files for the Osmocom MS lookup library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libosmo-mslookup0 = %{version}

%description -n libosmo-mslookup-devel
This shared library contains routines for looking up mobile subscribers.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmo-mslookup.

%package -n osmo-mslookup-client
Summary:        Standalone program using libosmo-mslookup
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++

%description -n osmo-mslookup-client
Standalone program using libosmo-mslookup to easily integrate with programs
that want to connect services (SIP, SMS,...) to the current location of a
subscriber.

%prep
%autosetup -p1

%build
echo "%{version}" >.tarball-version
autoreconf -fi
%configure \
  --docdir="%{_docdir}/%{name}" \
  --with-systemdsystemunitdir=%{_unitdir} \
  --enable-shared \
  --disable-static
make V=1 %{?_smp_mflags}

%install
%make_install
install -d "%{buildroot}/%{_localstatedir}/lib/osmocom"
find %{buildroot} -type f -name "*.la" -delete -print
install -d %{buildroot}/%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rcosmo-hlr

%check
make %{?_smp_mflags} check || (find . -name testsuite.log -exec cat {} +)

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%post   -n libosmo-gsup-client0 -p /sbin/ldconfig
%postun -n libosmo-gsup-client0 -p /sbin/ldconfig
%post   -n libosmo-mslookup0 -p /sbin/ldconfig
%postun -n libosmo-mslookup0 -p /sbin/ldconfig

%files
%license COPYING
%dir %{_docdir}/%{name}
%dir %{_docdir}/%{name}/examples
%{_docdir}/%{name}/examples/osmo-hlr.cfg
%{_docdir}/%{name}/examples/osmo-hlr-dgsm.cfg
%dir %{_docdir}/%{name}/sql
%{_docdir}/%{name}/sql/hlr.sql
%{_docdir}/%{name}/sql//hlr_data.sql
%dir %{_sysconfdir}/osmocom
%dir %{_localstatedir}/lib/osmocom
%{_bindir}/osmo-hlr
%{_bindir}/osmo-hlr-db-tool
%dir %{_sysconfdir}/osmocom
%config(noreplace) %{_sysconfdir}/osmocom/osmo-hlr.cfg
%{_unitdir}/osmo-hlr.service
%{_sbindir}/rcosmo-hlr
%dir %{_datadir}/osmocom
%{_datadir}/osmocom/osmo-hlr-post-upgrade.sh

%files -n libosmo-gsup-client0
%{_libdir}/libosmo-gsup-client.so.0*

%files -n libosmo-gsup-client-devel
%{_bindir}/osmo-euse-demo
%dir %{_includedir}/osmocom
%dir %{_includedir}/osmocom/gsupclient
%{_includedir}/osmocom/gsupclient/*.h
%{_libdir}/libosmo-gsup-client.so
%{_libdir}/pkgconfig/libosmo-gsup-client.pc

%files -n libosmo-mslookup0
%{_libdir}/libosmo-mslookup.so.0*

%files -n libosmo-mslookup-devel
%dir %{_includedir}/osmocom
%dir %{_includedir}/osmocom/mslookup
%{_includedir}/osmocom/mslookup/*.h
%{_libdir}/libosmo-mslookup.so
%{_libdir}/pkgconfig/libosmo-mslookup.pc

%files -n osmo-mslookup-client
%{_bindir}/osmo-mslookup-client

%changelog
