#
# spec file for package osmo-e1d
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2019-2021, Martin Hauke <mardnh@gmx.de>
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


Name:           osmo-e1d
Version:        0.7.1
Release:        0
Summary:        Osmocom E1 Daemon
License:        GPL-2.0-or-later
Group:          Productivity/Telephony/Utilities
URL:            https://osmocom.org/projects/osmo-e1d/wiki/Wiki
Source:         https://github.com/osmocom/osmo-e1d/archive/%version.tar.gz
BuildRequires:  automake >= 1.9
BuildRequires:  libtool >= 2
BuildRequires:  pkg-config >= 0.20
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libosmocore) >= 1.10.0
BuildRequires:  pkgconfig(libosmousb) >= 1.10.0
BuildRequires:  pkgconfig(libosmovty) >= 1.10.0
BuildRequires:  pkgconfig(libusb-1.0) >= 1.0.20
BuildRequires:  pkgconfig(talloc) >= 2.0.1

%description
osmo-e1d is an E1 interface daemon that is part of the Osmocom E1
interface driver architecture. It was primarily written for the
ICE40_E1_USB_interface (ICE40 based E1 framer IP core developed by
tnt).

osmo-e1d acts as an interface between the hardware/firmware of the E1
interface on the bottom side, and applications wanting to use E1
timeslots on the top side.

%package -n libosmo-e1d3
Summary:        Osmocom E1 daemon protocol library
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n libosmo-e1d3
Osmocom E1 Daemon Protocol Library.

%package -n libosmo-octoi3
Summary:        Library for the Osmocom Community TDMoIP network
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n libosmo-octoi3
Library for the Osmocom Community TDMoIP network.

%package devel
Summary:        Header files for the Osmocom E1 daemon protocol library
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libosmo-e1d3 = %version-%release
Requires:       libosmo-octoi3 = %version-%release
Provides:       libosmo-e1d-devel = %version-%release
Obsoletes:      libosmo-e1d-devel < %version-%release

%description devel
This subpackage contains libraries and header files for developing
applications that want to make use of libosmo-e1d.

%prep
%autosetup -p1

%build
echo "%version" >.tarball-version
autoreconf -fiv
# bugzilla.opensuse.org/795968 for rationale
%configure --includedir="%_includedir/%name" --disable-static \
	--docdir="%_docdir/%name" \
	--with-systemdsystemunitdir="%_unitdir"
%make_build

%install
%make_install
find "%buildroot" -type f -name "*.la" -delete -print
# https://en.opensuse.org/openSUSE:Packaging_UsrEtc
rm -Rf "%buildroot/%_sysconfdir/osmocom"

%check
%make_build check || find . -name testsuite.log -exec cat {} +

%ldconfig_scriptlets -n libosmo-e1d3
%ldconfig_scriptlets -n libosmo-octoi3

%preun
%service_del_preun %name.service

%postun
%service_del_postun %name.service

%pre
%service_add_pre %name.service

%post
%service_add_post %name.service

%files
%license COPYING COPYING.gpl2 COPYING.lgpl3
%doc README.md
%_bindir/osmo-e1d
%_bindir/osmo-e1d-pipe
%dir %_docdir/%name
%dir %_docdir/%name/examples
%_docdir/%name/examples/
%_unitdir/osmo-e1d.service

%files -n libosmo-e1d3
%_libdir/libosmo-e1d.so.*

%files -n libosmo-octoi3
%_libdir/libosmo-octoi.so.*

%files devel
%_includedir/%name/
%_libdir/libosmo-e1d.so
%_libdir/libosmo-octoi.so
%_libdir/pkgconfig/*.pc

%changelog
