#
# spec file for package osmo-iuh
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define lname	libosmo-ranap2
Version:        0.4.0
Release:        0
Summary:        Osmocom code for the Iuh interface (HNBAP, RUA, RANAP)
License:        AGPL-3.0-or-later AND GPL-2.0-or-later
Group:          Hardware/Mobile
Url:            https://osmocom.org/projects/osmohnbgw/wiki
Source:         %name-%version.tar.xz
Patch3:         0001-iu_client-uses-gprs_msgb.h.patch
BuildRequires:  automake >= 1.9
BuildRequires:  libtool >= 2
BuildRequires:  lksctp-tools-devel
BuildRequires:  pkg-config >= 0.20
# python2 for asn1tostruct.py
BuildRequires:  python2
BuildRequires:  xz
BuildRequires:  pkgconfig(libasn1c) >= 0.9.30
BuildRequires:  pkgconfig(libosmo-netif) >= 0.2.0
BuildRequires:  pkgconfig(libosmo-sigtran) >= 0.9.0
BuildRequires:  pkgconfig(libosmocore) >= 0.11.0
BuildRequires:  pkgconfig(libosmoctrl) >= 0.11.0
BuildRequires:  pkgconfig(libosmogb)
BuildRequires:  pkgconfig(libosmogsm) >= 0.11.0
BuildRequires:  pkgconfig(libosmovty) >= 0.11.0

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

%prep
%autosetup -p1

%build
echo "%version" >.tarball-version
autoreconf -fi
%configure \
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
%_libdir/libosmo-ranap.so.2*

%files -n libosmo-ranap-devel
%_includedir/*
%_libdir/libosmo-ranap.so
%_libdir/pkgconfig/*.pc

%changelog
