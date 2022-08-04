#
# spec file for package osmo-iuh
#
# Copyright (c) 2022 SUSE LLC
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
Version:        1.3.0
Release:        0
Summary:        Osmocom code for the Iuh interface (HNBAP, RUA, RANAP)
License:        AGPL-3.0-or-later AND GPL-2.0-or-later
Group:          Hardware/Mobile
URL:            https://osmocom.org/projects/osmohnbgw/wiki

Source:         https://github.com/osmocom/osmo-iuh/archive/%version.tar.gz
BuildRequires:  automake >= 1.9
BuildRequires:  libtool >= 2
BuildRequires:  lksctp-tools-devel
BuildRequires:  pkg-config >= 0.20
# python3 for asn1tostruct.py
BuildRequires:  python3
BuildRequires:  pkgconfig(libasn1c) >= 0.9.30
BuildRequires:  pkgconfig(libosmo-netif) >= 1.2.0
BuildRequires:  pkgconfig(libosmo-sigtran) >= 1.6.0
BuildRequires:  pkgconfig(libosmocore) >= 1.7.0
BuildRequires:  pkgconfig(libosmoctrl) >= 1.7.0
BuildRequires:  pkgconfig(libosmogb) >= 1.7.0
BuildRequires:  pkgconfig(libosmogsm) >= 1.7.0
BuildRequires:  pkgconfig(libosmovty) >= 1.7.0

%description
Osmocom code for the Iuh interface (HNBAP, RUA, RANAP)

%package -n libosmo-hnbap0
Summary:        Home Node B Application Part library
Group:          System/Libraries

%description -n libosmo-hnbap0
Osmocom code for the Home Node B Application Part. HNBAP is a control protocol
found in Home Node B networks on the Iu-h interface.

%package -n libosmo-hnbap-devel
Summary:        Development files for Osmocom HNBAP library
Group:          Development/Libraries/C and C++
Requires:       libosmo-hnbap0 = %version-%release

%description -n libosmo-hnbap-devel
This subpackage contains libraries and header files for developing
applications that want to make use of libosmo-hnbap.

%package -n libosmo-ranap5
Summary:        Radio Access Network Application Part library
Group:          System/Libraries

%description -n libosmo-ranap5
Osmocom code for the Radio Access Network Application Part of the Iu-h
interface.

%package -n libosmo-ranap-devel
Summary:        Header files for the Osmocom RANAP library
Group:          Development/Libraries/C and C++
Requires:       libosmo-ranap5 = %version-%release

%description -n libosmo-ranap-devel
Osmocom code for the Radio Access Network Application Part of the Iu-h
interface.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmo-ranap.

%package -n libosmo-rua0
Summary:        RANAP User Adaption signalling library
Group:          System/Libraries

%description -n libosmo-rua0
Osmocom code for the RANAP User Adaption signalling.

%package -n libosmo-rua-devel
Summary:        Header files for the Osmocom RUA library
Group:          Development/Libraries/C and C++
Requires:       libosmo-rua0 = %version-%release

%description -n libosmo-rua-devel
Osmocom code for the RANAP User Adaption signalling.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmo-rua.

%package -n libosmo-sabp1
Summary:        Osmocom Service Area Broadcast Protocol library
Group:          System/Libraries

%description -n libosmo-sabp1
Osmocom code for the Service Area Broadcast Protocol interface.

%package -n libosmo-sabp-devel
Summary:        Header files for the Osmocom SABP library
Group:          Development/Libraries/C and C++
Requires:       libosmo-sabp1 = %version-%release

%description -n libosmo-sabp-devel
Osmocom code for the Service Area Broadcast Protocol interface.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmo-sabp.

%prep
%autosetup -p1

%build
echo "%version" >.tarball-version
autoreconf -fi
%configure \
    --disable-static \
    --docdir="%_docdir/%name" \
    --with-systemdsystemunitdir="%_unitdir"
%make_build

%install
%make_install
find "%buildroot" -type f -name "*.la" -delete -print

%check
if ! %make_build check; then
	find . -type f -name testsuite.log -exec cat "{}" "+"
%ifnarch ppc ppc64
	exit 1
%endif
fi

%post   -n libosmo-hnbap0 -p /sbin/ldconfig
%postun -n libosmo-hnbap0 -p /sbin/ldconfig
%post   -n libosmo-ranap5 -p /sbin/ldconfig
%postun -n libosmo-ranap5 -p /sbin/ldconfig
%post   -n libosmo-rua0 -p /sbin/ldconfig
%postun -n libosmo-rua0 -p /sbin/ldconfig
%post   -n libosmo-sabp1 -p /sbin/ldconfig
%postun -n libosmo-sabp1 -p /sbin/ldconfig

%files -n libosmo-hnbap0
%license COPYING
%_libdir/libosmo-hnbap.so.*

%files -n libosmo-hnbap-devel
%dir %_includedir/osmocom/
%dir %_includedir/osmocom/hnbap/
%_includedir/osmocom/hnbap/*
%_libdir/libosmo-hnbap.so
%_libdir/pkgconfig/libosmo-hnbap.pc

%files -n libosmo-ranap5
%_libdir/libosmo-ranap.so.*

%files -n libosmo-ranap-devel
%dir %_includedir/osmocom/
%_includedir/osmocom/ranap/
%_libdir/libosmo-ranap.so
%_libdir/pkgconfig/libosmo-ranap.pc

%files -n libosmo-rua0
%_libdir/libosmo-rua.so.*

%files -n libosmo-rua-devel
%dir %_includedir/osmocom/
%_includedir/osmocom/rua/
%_libdir/libosmo-rua.so
%_libdir/pkgconfig/libosmo-rua.pc

%files -n libosmo-sabp1
%_libdir/libosmo-sabp.so.1*

%files -n libosmo-sabp-devel
%dir %_includedir/osmocom/
%_includedir/osmocom/sabp/
%_libdir/libosmo-sabp.so
%_libdir/pkgconfig/libosmo-sabp.pc

%changelog
