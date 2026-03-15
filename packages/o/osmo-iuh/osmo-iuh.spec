#
# spec file for package osmo-iuh
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        1.8.0
Release:        0
Summary:        Osmocom code for the Iuh interface (HNBAP, RUA, RANAP)
License:        AGPL-3.0-or-later
Group:          Hardware/Mobile
URL:            https://osmocom.org/projects/osmohnbgw/wiki
#Git-Clone:     https://gitea.osmocom.org/cellular-infrastructure/osmo-iuh
#Git-Clone:     https://github.com/osmocom/osmo-iuh
#DL-URL:        https://downloads.osmocom.org/releases/osmo-iuh/
Source:         https://downloads.osmocom.org/releases/%name/%name-%version.tar.bz2
BuildRequires:  automake >= 1.9
BuildRequires:  libtool >= 2
BuildRequires:  lksctp-tools-devel
BuildRequires:  pkg-config >= 0.20
# python3 for asn1tostruct.py
BuildRequires:  python3
BuildRequires:  pkgconfig(libasn1c) >= 0.9.30
BuildRequires:  pkgconfig(libosmo-netif) >= 1.7.0
BuildRequires:  pkgconfig(libosmo-sigtran) >= 2.2.0
BuildRequires:  pkgconfig(libosmocore) >= 1.12.0
BuildRequires:  pkgconfig(libosmoctrl) >= 1.12.0
BuildRequires:  pkgconfig(libosmogb) >= 1.12.0
BuildRequires:  pkgconfig(libosmogsm) >= 1.12.0
BuildRequires:  pkgconfig(libosmovty) >= 1.12.0

%description
Osmocom code for the Iuh interface (HNBAP, RUA, RANAP)

%package -n libosmo-hnbap0
Summary:        Home Node B Application Part library
Group:          System/Libraries

%description -n libosmo-hnbap0
Osmocom code for the Home Node B Application Part. HNBAP is a control protocol
found in Home Node B networks on the Iu-h interface.

%package -n libosmo-ranap7
Summary:        Radio Access Network Application Part library
Group:          System/Libraries

%description -n libosmo-ranap7
Osmocom code for the Radio Access Network Application Part of the Iu-h
interface.

%package -n libosmo-rua0
Summary:        RANAP User Adaption signalling library
Group:          System/Libraries

%description -n libosmo-rua0
Osmocom code for the RANAP User Adaption signalling.

%package -n libosmo-sabp1
Summary:        Osmocom Service Area Broadcast Protocol library
Group:          System/Libraries

%description -n libosmo-sabp1
Osmocom code for the Service Area Broadcast Protocol interface.

%package devel
Summary:        Header files for the Osmocom Iuh libraries
Group:          Development/Libraries/C and C++
Requires:       libosmo-hnbap0 = %version-%release
Requires:       libosmo-ranap7 = %version-%release
Requires:       libosmo-rua0 = %version-%release
Requires:       libosmo-sabp1 = %version-%release
Obsoletes:      libosmo-hnbap-devel = %version-%release
Obsoletes:      libosmo-hnbap-devel < %version-%release
Obsoletes:      libosmo-ranap-devel = %version-%release
Obsoletes:      libosmo-ranap-devel < %version-%release
Obsoletes:      libosmo-rua-devel = %version-%release
Obsoletes:      libosmo-rua-devel < %version-%release
Obsoletes:      libosmo-sabp-devel = %version-%release
Obsoletes:      libosmo-sabp-devel < %version-%release

%description devel
Osmocom code for the Service Area Broadcast Protocol interface.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmo-sabp.

%prep
%autosetup -p1

%build
echo "%version" >.tarball-version
autoreconf -fi
%configure --disable-static --docdir="%_docdir/%name" \
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

%ldconfig_scriptlets -n libosmo-hnbap0
%ldconfig_scriptlets -n libosmo-ranap7
%ldconfig_scriptlets -n libosmo-rua0
%ldconfig_scriptlets -n libosmo-sabp1

%files -n libosmo-hnbap0
%license COPYING
%_libdir/libosmo-hnbap.so.*

%files -n libosmo-ranap7
%_libdir/libosmo-ranap.so.*

%files -n libosmo-rua0
%_libdir/libosmo-rua.so.*

%files -n libosmo-sabp1
%_libdir/libosmo-sabp.so.1*

%files devel
%_includedir/osmocom/
%_libdir/pkgconfig/*.pc
%_libdir/*.so

%changelog
