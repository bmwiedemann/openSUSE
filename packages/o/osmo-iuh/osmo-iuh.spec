#
# spec file for package osmo-iuh
#
# Copyright (c) 2020 SUSE LLC
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


Name:           osmo-iuh
%define lname	libosmo-ranap3
Version:        0.6.0
Release:        0
Summary:        Osmocom code for the Iuh interface (HNBAP, RUA, RANAP)
License:        AGPL-3.0-or-later AND GPL-2.0-or-later
Group:          Hardware/Mobile
URL:            https://osmocom.org/projects/osmohnbgw/wiki

Source:         %name-%version.tar.xz
Patch1:         damncode.diff
Patch3:         0001-iu_client-uses-gprs_msgb.h.patch
BuildRequires:  automake >= 1.9
BuildRequires:  libtool >= 2
BuildRequires:  lksctp-tools-devel
BuildRequires:  pkg-config >= 0.20
# python3 for asn1tostruct.py
BuildRequires:  python3
BuildRequires:  xz
BuildRequires:  pkgconfig(libasn1c) >= 0.9.30
BuildRequires:  pkgconfig(libosmo-netif) >= 0.3.0
BuildRequires:  pkgconfig(libosmo-sigtran) >= 0.10.0
BuildRequires:  pkgconfig(libosmocore) >= 0.12.0
BuildRequires:  pkgconfig(libosmoctrl) >= 0.12.0
BuildRequires:  pkgconfig(libosmogb)
BuildRequires:  pkgconfig(libosmogsm) >= 0.12.0
BuildRequires:  pkgconfig(libosmovty) >= 0.12.0

%description
Osmocom code for the Iuh interface (HNBAP, RUA, RANAP)

%package -n %lname
Summary:        Shared Library part of libosmo-ranap
Group:          System/Libraries

%description -n %lname
Osmocom code for the Iuh interface (HNBAP, RUA, RANAP)

%package -n libosmo-ranap-devel
Summary:        Development files for Osmocom RANAP library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description -n libosmo-ranap-devel
Osmocom code for the Iuh interface (HNBAP, RUA, RANAP)

This subpackage contains libraries and header files for developing
applications that want to make use of libosmoranap.

%package -n libosmo-sabp0
Summary:        Osmocom Service Area Broadcast Protocol library
Group:          System/Libraries

%description -n libosmo-sabp0
Osmocom code for the Service Area Broadcast Protocol interface.

%package -n libosmo-sabp-devel
Summary:        Development files for Osmocom SABP library
Group:          Development/Libraries/C and C++
Requires:       libosmo-sabp0 = %version

%description -n libosmo-sabp-devel
Osmocom code for the Service Area Broadcast Protocol interface.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmo-sabp.

%prep
%autosetup -p1

%build
echo "%version" >.tarball-version
autoreconf -fi
%configure CFLAGS="%optflags -fcommon" \
    --disable-static \
    --docdir="%_docdir/%name" \
    --with-systemdsystemunitdir="%_unitdir"
make %{?_smp_mflags}

%install
%make_install
find "%buildroot" -type f -name "*.la" -delete -print
install -d %buildroot/%_sbindir
ln -s %_sbindir/service %buildroot/%_sbindir/rcosmo-hnbgw

%check
if ! make %{?_smp_mflags} check; then
	find . -type f -name testsuite.log -exec cat "{}" "+"
%ifnarch ppc ppc64
	exit 1
%endif
fi

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig
%post   -n libosmo-sabp0 -p /sbin/ldconfig
%postun -n libosmo-sabp0 -p /sbin/ldconfig

%pre
%service_add_pre    osmo-hnbgw.service

%post
%service_add_post   osmo-hnbgw.service

%preun
%service_del_preun  osmo-hnbgw.service

%postun
%service_del_postun osmo-hnbgw.service

%files
%license COPYING
%doc README.md
%dir %_sysconfdir/osmocom
%config %_sysconfdir/osmocom/osmo-hnbgw.cfg
%dir %_docdir/%name/examples
%_docdir/%name/examples/osmo-hnbgw.cfg
%_bindir/osmo-hnbgw
%_unitdir/osmo-hnbgw.service
%_sbindir/rcosmo-hnbgw

%files -n %lname
%_libdir/libosmo-ranap.so.3*

%files -n libosmo-ranap-devel
%dir %{_includedir}/osmocom
%_includedir/osmocom/ranap
%_libdir/libosmo-ranap.so
%_libdir/pkgconfig/libosmo-ranap.pc

%files -n libosmo-sabp0
%_libdir/libosmo-sabp.so.0*

%files -n libosmo-sabp-devel
%dir %{_includedir}/osmocom
%_includedir/osmocom/sabp
%_libdir/libosmo-sabp.so
%_libdir/pkgconfig/libosmo-sabp.pc

%changelog
