#
# spec file for package libosmo-sccp
#
# Copyright (c) 2024 SUSE LLC
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


Name:           libosmo-sccp
Version:        1.8.2
Release:        0
%define libversion %(echo "%version" | sed 's/\\./_/g')
Summary:        Osmocom library for the A-bis interface between BTS and BSC
License:        AGPL-3.0-or-later AND GPL-2.0-or-later
Group:          Hardware/Mobile
URL:            https://projects.osmocom.org/projects/libosmo-sccp
#Git-Clone:	https://git.osmocom.org/libosmo-sccp
Source:         https://github.com/osmocom/libosmo-sccp/archive/%version.tar.gz
Patch1:         0001-build-fixes.patch
Patch2:         harden_osmo-stp.service.patch
BuildRequires:  automake >= 1.6
BuildRequires:  libtool >= 2
BuildRequires:  lksctp-tools-devel
BuildRequires:  pkg-config >= 0.20
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libosmo-netif) >= 1.4.0
BuildRequires:  pkgconfig(libosmocore) >= 1.9.0
BuildRequires:  pkgconfig(libosmogsm) >= 1.9.0
BuildRequires:  pkgconfig(libosmovty) >= 1.9.0

%description
SCCP is a network layer protocol that provides extended routing, flow
control, segmentation, connection-orientation, and error correction
facilities in Signaling System 7 telecommunications networks. SCCP is
heavily used in cellular networks such as GSM.

%package -n libosmo-mtp-%libversion
Summary:        Osmocom Message Transfer Part library
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n libosmo-mtp-%libversion
The Message Transfer Part (MTP) is part of the Signaling System 7
(SS7) used for communication in Public Switched Telephone Networks.
MTP is responsible for reliable, unduplicated and in-sequence
transport of SS7 messages between communication partners.

%package -n libosmo-mtp-devel
Summary:        Development files for the Osmocom MTP library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libosmo-mtp-%libversion = %version

%description -n libosmo-mtp-devel
MTP is part of SS7 used for communication in Public Switched
Telephone Networks.

This subpackage contains the development files for the Osmocom MTP
library.

%package -n libosmo-sccp-%libversion
Summary:        Osmocom Signalling Connection Control Part library
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n libosmo-sccp-%libversion
The Signalling Connection Control Part (SCCP) is a network layer
protocol that provides extended routing, flow control, segmentation,
connection-orientation, and error correction facilities in Signaling
System 7 telecommunications networks. SCCP relies on the services of
MTP for basic routing and error detection.

%package -n libosmo-sccp-devel
Summary:        Development files for the Osmocom SCCP library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libosmo-sccp-%libversion = %version
# previously wrongly shipped .so file
Conflicts:      libosmo-sccp-1_0_0

%description -n libosmo-sccp-devel
SCCP is a network layer protocol that provides routing, flow control,
segmentation, connection-orientation, and error correction facilities
in SS7 telecommunications networks.

This subpackage contains the development files for the Osmocom SCCP
library.

%package -n libosmo-sigtran9
Summary:        Osmocom SIGTRAN library
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n libosmo-sigtran9
Osmocom implementation of (parts of) SIGTRAN.

%package -n libosmo-sigtran-devel
Summary:        Development files for the Osmocom sigtran library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libosmo-sigtran9 = %version

%description -n libosmo-sigtran-devel
Osmocom implementation of (parts of) SIGTRAN.

This subpackage contains the development files for the Osmocom
SIGTRAN library.

%package -n libosmo-xua-%libversion
Summary:        Osmocom Message Transfer Part 2 User Adaptation library
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n libosmo-xua-%libversion
M2UA (RFC 3331) provides an SCTP (RFC 3873) adaptation layer for the
seamless backhaul of MTP Level 2 user messages and service interface
across an IP network.

%package -n libosmo-xua-devel
Summary:        Development files for the Osmocom M2UA library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libosmo-sigtran-devel = %version
Requires:       libosmo-xua-%libversion = %version

%description -n libosmo-xua-devel
M2UA provides an SCTP adaptation layer for MTP level 2 user messages
and service interface across an IP network.

This subpackage contains the development files for the Osmocom M2UA
library.

%package -n osmo-stp
Summary:        Osmocom SIGTRAN STP (Signaling Transfer Point)
License:        GPL-2.0-or-later
Group:          Productivity/Telephony/Servers

%description -n osmo-stp
This is the Osmocom (Open Source Mobile Communications)
implementation of a Signaling Transfer Point (STP) for SS7/SIGTRAN
telecommunication networks. At this point, it is a minimal
implementation, missing lots of the functionality usually present in
a STP, such as Global Title Routing, Global Title Translation.

%prep
%autosetup -p1

%build
echo "%version" >.tarball-version
autoreconf -fiv
# bugzilla.opensuse.org/795968 for rationale
%configure --includedir="%_includedir/%name" \
	--docdir="%_defaultdocdir/%name" \
	--with-systemdsystemunitdir="%_unitdir" \
	--disable-static CFLAGS="%optflags -fcommon"
%make_build

%install
%make_install
find "%buildroot/%_libdir" -type f -name "*.la" -delete
install -d "%buildroot/%_unitdir" "%buildroot/%_sbindir"
ln -s service "%buildroot/%_sbindir/rcosmo-stp"

%check
if ! %make_build check; then
	find . -name testsuite.log -exec cat "{}" "+"
%ifnarch ppc64 sparc64 s390x
	# still BE problems?
	exit 1
%endif
fi

%ldconfig_scriptlets -n libosmo-mtp-%libversion
%ldconfig_scriptlets -n libosmo-sccp-%libversion
%ldconfig_scriptlets -n libosmo-sigtran9
%ldconfig_scriptlets -n libosmo-xua-%libversion

%preun -n osmo-stp
%service_del_preun osmo-stp.service

%postun -n osmo-stp
%service_del_postun osmo-stp.service

%pre -n osmo-stp
%service_add_pre osmo-stp.service

%post -n osmo-stp
%service_add_post osmo-stp.service

%files -n libosmo-mtp-%libversion
%_libdir/libosmo-mtp-%version.so

%files -n libosmo-mtp-devel
%dir %_includedir/%name/
%dir %_includedir/%name/osmocom/
%_includedir/%name/osmocom/mtp/
%_libdir/libosmo-mtp.so
%_libdir/pkgconfig/libosmo-mtp.pc

%files -n libosmo-sccp-%libversion
%_libdir/libosmo-sccp-%version.so

%files -n libosmo-sccp-devel
%dir %_includedir/%name/
%dir %_includedir/%name/osmocom/
%_includedir/%name/osmocom/sccp/
%_libdir/libosmo-sccp.so
%_libdir/pkgconfig/libosmo-sccp.pc

%files -n libosmo-sigtran9
%_libdir/libosmo-sigtran.so.*

%files -n libosmo-sigtran-devel
%dir %_includedir/%name/
%dir %_includedir/%name/osmocom/
%_includedir/%name/osmocom/sigtran/
%_libdir/libosmo-sigtran.so
%_libdir/pkgconfig/libosmo-sigtran.pc

%files -n libosmo-xua-%libversion
%_libdir/libosmo-xua-%version.so

%files -n libosmo-xua-devel
%_libdir/libosmo-xua.so
%_libdir/pkgconfig/libosmo-xua.pc

%files -n osmo-stp
%dir %_sysconfdir/osmocom
%config %_sysconfdir/osmocom/osmo-stp.cfg
%_bindir/osmo-stp
%_sbindir/rcosmo-stp
%_unitdir/osmo-stp.service
%_defaultdocdir/%name/
%license COPYING

%changelog
