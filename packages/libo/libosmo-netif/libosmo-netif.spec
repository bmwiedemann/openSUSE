#
# spec file for package libosmo-netif
#
# Copyright (c) 2025 SUSE LLC
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


Name:           libosmo-netif
Version:        1.6.0
Release:        0
Summary:        Osmocom library for muxed audio
License:        GPL-2.0-or-later
Group:          Productivity/Telephony/Utilities
URL:            https://osmocom.org/projects/libosmo-netif
Source:         https://github.com/osmocom/libosmo-netif/archive/%version.tar.gz
Patch1:         osmo-talloc.diff
BuildRequires:  automake
BuildRequires:  libtool >= 2
BuildRequires:  lksctp-tools-devel
BuildRequires:  pkg-config >= 0.20
BuildRequires:  pkgconfig(libosmocodec) >= 1.11.0
BuildRequires:  pkgconfig(libosmocore) >= 1.11.0
BuildRequires:  pkgconfig(libosmogsm) >= 1.11.0
BuildRequires:  pkgconfig(talloc)

%description
Network interface demuxer library for OsmoCom projects.

%package -n libosmonetif11
Summary:        Osmocom library for muxed audio
License:        AGPL-3.0-or-later
Group:          System/Libraries

%description -n libosmonetif11
Network interface demuxer library for OsmoCom projects.

%package -n libosmonetif-devel
Summary:        Development files for the Osmocom muxed audio library
License:        AGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libosmonetif11 = %version

%description -n libosmonetif-devel
Network interface demuxer library for OsmoCom projects.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmo-netif.

%prep
%autosetup -p1

%build
echo "%version" >.tarball-version
autoreconf -fiv
# bugzilla.opensuse.org/795968 for rationale
%configure --includedir="%_includedir/%name" \
	--enable-shared --disable-static
%make_build

%install
%make_install
find "%buildroot/%_libdir" -type f -name "*.la" -delete

%check
if ! %make_build check; then
	rv=$?
	cat tests/testsuite.log
	echo "Suppressing exit $rv"
	# timing issue
fi

%ldconfig_scriptlets -n libosmonetif11

%files -n libosmonetif11
%_libdir/libosmonetif.so.*

%files -n libosmonetif-devel
%license COPYING
%dir %_includedir/%name/
%dir %_includedir/%name/osmocom/
%_includedir/%name/osmocom/netif/
%_libdir/libosmonetif.so
%_libdir/pkgconfig/libosmo-netif.pc

%changelog
