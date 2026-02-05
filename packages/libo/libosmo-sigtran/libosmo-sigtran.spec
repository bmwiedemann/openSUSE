#
# spec file for package libosmo-sigtran
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


Name:           libosmo-sigtran
%define lname   libosmo-sigtran12
Version:        2.2.1
Release:        0
Summary:        Osmocom library for the A-bis interface between BTS and BSC
License:        AGPL-3.0-or-later AND GPL-2.0-or-later
Group:          Productivity/Telephony/Utilities
URL:            https://gitea.osmocom.org/osmocom/libosmo-sigtran
Source:         %name-%version.tar.xz
Patch2:         0001-build-fixes.patch
Patch3:         harden_osmo-stp.service.patch
BuildRequires:  automake >= 1.6
BuildRequires:  libtool >= 2
BuildRequires:  lksctp-tools-devel
BuildRequires:  pkg-config >= 0.20
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libosmo-netif) >= 1.6.0
BuildRequires:  pkgconfig(libosmocore) >= 1.11.0
BuildRequires:  pkgconfig(libosmogsm) >= 1.11.0
BuildRequires:  pkgconfig(libosmovty) >= 1.11.0
BuildRequires:  pkgconfig(libosmo-asn1-tcap) >= 0.2.1

%description
libosmo-sigtran is a C-language library implementation of a variety
of telecom signaling protocols, such as M3UA, SUA, SCCP.

%package -n %lname
Summary:        Osmocom SIGTRAN library
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n %lname
libosmo-sigtran is a C-language library implementation of a variety
of telecom signaling protocols, such as M3UA, SUA, SCCP (connection
oriented and connectionless). SCCP is a network layer protocol that
provides extended routing, flow control, segmentation,
connection-orientation, and error correction facilities in Signaling
System 7 telecommunications networks. SCCP is heavily used in
cellular networks such as GSM.

OsmoSTP is a SS7 Transfer Point that can be used to act as router and
translator between M3UA, SUA and/or SCCPlite.

%package devel
Summary:        Development files for the Osmocom sigtran library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
Osmocom implementation of (parts of) SIGTRAN.

This subpackage contains the development files for the Osmocom
SIGTRAN library.

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
	--disable-static CFLAGS="%optflags -fcommon" --enable-tcap-loadsharing
%make_build

%install
%make_install
find "%buildroot/%_libdir" -type f -name "*.la" -delete

#%check
# TS fails to build because it references a static library that does not exist,
# and the shared library has symbols hidden

%ldconfig_scriptlets -n %lname

%preun -n osmo-stp
%service_del_preun osmo-stp.service

%postun -n osmo-stp
%service_del_postun osmo-stp.service

%pre -n osmo-stp
%service_add_pre osmo-stp.service

%post -n osmo-stp
%service_add_post osmo-stp.service

%files -n %lname
%_libdir/libosmo-sigtran.so.*

%files devel
%_includedir/%name/
%_libdir/libosmo-sigtran.so
%_libdir/pkgconfig/libosmo-sigtran.pc

%files -n osmo-stp
%dir %_sysconfdir/osmocom
%config %_sysconfdir/osmocom/osmo-stp.cfg
%_bindir/osmo-stp
%_unitdir/osmo-stp.service
%_defaultdocdir/%name/
%license COPYING

%changelog
