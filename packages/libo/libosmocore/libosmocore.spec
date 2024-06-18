#
# spec file for package libosmocore
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


Name:           libosmocore
Version:        1.9.3
Release:        0
Summary:        The Open Source Mobile Communications Core Library
License:        AGPL-3.0-or-later AND GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Telephony/Utilities
URL:            https://osmocom.org/projects/libosmocore/wiki/Libosmocore
Source:         https://github.com/osmocom/libosmocore/archive/%version.tar.gz
BuildRequires:  automake >= 1.6
BuildRequires:  libtool >= 2
BuildRequires:  lksctp-tools-devel
BuildRequires:  pkg-config >= 0.20
BuildRequires:  python3
BuildRequires:  xz
BuildRequires:  pkgconfig(gnutls) >= 2.12.0
BuildRequires:  pkgconfig(libmnl)
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(liburing)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(talloc) >= 2.1.0

%description
libosmocore is a package with various utility functions that were
originally developed as part of the OpenBSC project, but which are of
a more generic nature and thus useful to (at least) other programs
that Osmocom develops w.r.t. mobile communications.

There is no clear scope of it. It simply houses all code shared
between OsmocomBB and OpenBSC to avoid code duplication.

%package tools
Summary:        GSM utilities from the osmocore project
License:        AGPL-3.0-or-later AND GPL-2.0-only AND GPL-2.0-or-later AND LGPL-3.0-or-later
Group:          Productivity/Telephony/Utilities
Provides:       %name-utils = %version-%release

%description tools
libosmocore is a package with various utility functions that were
originally developed as part of the OpenBSC project.

This package contains a program for frequency calculation for GSM
called "osmo-arfcn", and a program called "osmo-auc-gen" that is used
for testing GSM authentication.

%package -n libosmocodec4
Summary:        GSM 06.10, 06.20, 06.60, 06.90 codec library
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n libosmocodec4
The libosmocodec library contains an implementation of multiple
GSM codecs:

* GSM 06.10 Full Rate (FR) codec
* GSM 06.20 Half Rate (HR) codec
* GSM 06.60 Enhanced Full Range (EFR) codec
* GSM 06.90 Adaptive Multi-Rate (AMR) codec

%package -n libosmocodec-devel
Summary:        Development files for the Osmocom GSM codec library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libosmocodec4 = %version

%description -n libosmocodec-devel
The libosmocodec library contains an implementation of multiple
GSM codecs.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmocodec.

%package -n libosmocoding0
Summary:        GSM/GPRS/EDGE transcoding routines library
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n libosmocoding0
libosmocoding is a library which provides GSM, GPRS and EDGE
transcoding routines.

The following data types are currently supported: xCCH, PDTCH (CS 1-4
and MCS 1-9), TCH/FR, TCH/HR, TCH/AFS, RCH/AHS, RACH and SCH.

%package -n libosmocoding-devel
Summary:        Development files for the Osmocom transcoding library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libosmocoding0 = %version
Requires:       libosmocore-devel = %version

%description -n libosmocoding-devel
libosmocoding is a library which provides GSM, GPRS and EDGE
transcoding routines.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmocoding.

%package -n libosmocore21
Summary:        Osmocom core library
# crc16.c has GPL2-only clauses, the rest (*.c) is GPL-2.0+
License:        GPL-2.0-only AND GPL-2.0-or-later
Group:          System/Libraries

%description -n libosmocore21
libosmocore is a library with various utility functions shared
between OpenBSC and OsmocomBB.

%package -n libosmocore-devel
Summary:        Development files for the Osmocom core library
# crc16.h has GPL2-only clauses, the rest (*.h) is GPL-2.0+
License:        GPL-2.0-only AND GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libosmocore21 = %version
Requires:       libtalloc-devel

%description -n libosmocore-devel
libosmocore is a library with various utility functions shared
between OpenBSC and OsmocomBB.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmocore.

%package -n libosmoctrl0
Summary:        Osmocom SNMP-like control interface library
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n libosmoctrl0
libosmocore is a package with various utility functions that were
originally developed as part of the OpenBSC project.

libosmoctrl is an SNMP-like control interface. In contrast to the VTY
interface, the control interface is meant to be used by programs.

%package -n libosmoctrl-devel
Summary:        Osmocom control interface library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libosmocore-devel = %version
Requires:       libosmoctrl0 = %version
Requires:       libosmovty-devel = %version

%description -n libosmoctrl-devel
libosmoctrl is an SNMP-like control interface. In contrast to the VTY
interface, the control interface is meant to be used by programs.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmoctrl.

%package -n libosmogb14
Summary:        Osmocom GPRS Gb Interface (NS/BSSGP) library
License:        AGPL-3.0-or-later
Group:          System/Libraries

%description -n libosmogb14
libosmocore is a package with various utility functions that were
originally developed as part of the OpenBSC project.

The libosmogb library contains a GPRS BSSGP protocol implementation.

%package -n libosmogb-devel
Summary:        Development files for the Osmocom GPRS Gb interface library
License:        AGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libosmocore-devel = %version
Requires:       libosmogb14 = %version
Requires:       libosmogsm-devel = %version

%description -n libosmogb-devel
The libosmogb library contains a GPRS BSSGP protocol implementation.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmogb.

%package -n libosmogsm20
Summary:        Osmocom GSM utility library
License:        AGPL-3.0-or-later AND GPL-2.0-or-later
Group:          System/Libraries

%description -n libosmogsm20
libosmocore is a package with various utility functions that were
originally developed as part of the OpenBSC project.

The libosmogsm library in particular is a collection of common code
used in various GSM related sub-projects inside the Osmocom family of
projects. It includes A5/1 and A5/2 ciphers, COMP148v1, a LAPDm
implementation, a GSM TLV parser, SMS utility routines as well as
protocol definitions for a series of protocols.

%package -n libosmogsm-devel
Summary:        Development files for the Osmocom GSM utility library
License:        AGPL-3.0-or-later AND GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libosmocore-devel = %version
Requires:       libosmogsm20 = %version

%description -n libosmogsm-devel
The libosmogsm library in particular is a collection of common code
used in various GSM related sub-projects inside the Osmocom family of
projects. It includes A5/1 and A5/2 ciphers, COMP148v1, a LAPDm
implementation, a GSM TLV parser, SMS utility routines as well as
protocol definitions for a series of protocols.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmogsm.

%package -n libosmoisdn0
Summary:        Osmo ISDN utility library
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n libosmoisdn0
The libosmocore library contains various utility functions, a
collection of common code used in various ISDN related sub-projects
inside the Osmocom family of projects. It includes an I.460
sub-channel multiplex and a generic LAPD core.

%package -n libosmoisdn-devel
Summary:        Development files for the Osmo ISDN utility library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++

%description -n libosmoisdn-devel
The libosmocore library contains various utility functions, a
collection of common code used in various ISDN related sub-projects
inside the Osmocom family of projects. It includes an I.460
sub-channel multiplex and a generic LAPD core.

%package -n libosmosim2
Summary:        Osmocom SIM card related utility library
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n libosmosim2
libosmocore is a package with various utility functions that were
originally developed as part of the OpenBSC project.

The libosmosim library in particular contains routines for SIM card
access.

%package -n libosmosim-devel
Summary:        Development files for the Osmocom SIM card utility library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libosmocore-devel = %version
Requires:       libosmosim2 = %version

%description -n libosmosim-devel
The libosmosim library in particular contains routines for SIM card
access.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmosim.

%package -n libosmousb0
Summary:        Osmocom USB library
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n libosmousb0
libosmocore is a package with various utility functions that were
originally developed as part of the OpenBSC project.

The libosmosub library in particular contains routines for USB device
access via libusb-1.0, integrated into the libosmocore select event loop.

%package -n libosmousb-devel
Summary:        Development files for the Osmocom USB library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libosmocore-devel = %version
Requires:       libosmousb0 = %version
Requires:       libusb-1_0-devel

%description -n libosmousb-devel
The libosmosub library in particular contains routines for USB device
access via libusb-1.0, integrated into the libosmocore select event loop.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmousb.

%package -n libosmovty13
Summary:        Osmocom VTY interface library
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n libosmovty13
libosmocore is a package with various utility functions that were
originally developed as part of the OpenBSC project.

The libosmovty library implements the interactive command-line on the
VTY (Virtual TTY), as well as configuration file parsing.

%package -n libosmovty-devel
Summary:        Development files for the Osmocom VTY interface library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libosmocore-devel = %version
Requires:       libosmovty13 = %version

%description -n libosmovty-devel
The libosmovty library implements the interactive command-line on the
VTY (Virtual TTY), as well as configuration file parsing.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmovty.

%prep
%autosetup -p1

%build
echo "%version" >.tarball-version
autoreconf -fiv
# bugzilla.opensuse.org/795968 for rationale
%configure --includedir="%_includedir/%name" \
	CFLAGS="%optflags -fcommon" \
	--enable-shared --disable-static
%make_build

%install
%make_install
find "%buildroot/%_libdir" -type f -name "*.la" -delete

%check
%make_build check || (find . -name testsuite.log -exec cat {} +)

%ldconfig_scriptlets -n libosmocodec4
%ldconfig_scriptlets -n libosmocoding0
%ldconfig_scriptlets -n libosmocore21
%ldconfig_scriptlets -n libosmoctrl0
%ldconfig_scriptlets -n libosmogb14
%ldconfig_scriptlets -n libosmogsm20
%ldconfig_scriptlets -n libosmosim2
%ldconfig_scriptlets -n libosmousb0
%ldconfig_scriptlets -n libosmovty13

%files tools
%_bindir/osmo-*

%files -n libosmocodec4
%_libdir/libosmocodec.so.*

%files -n libosmocodec-devel
%dir %_includedir/%name/
%dir %_includedir/%name/osmocom/
%_includedir/%name/osmocom/codec/
%_libdir/libosmocodec.so
%_libdir/pkgconfig/libosmocodec.pc

%files -n libosmocoding0
%_libdir/libosmocoding.so.*

%files -n libosmocoding-devel
%dir %_includedir/%name/
%dir %_includedir/%name/osmocom/
%_includedir/%name/osmocom/coding/
%_libdir/libosmocoding.so
%_libdir/pkgconfig/libosmocoding.pc

%files -n libosmocore21
%_libdir/libosmocore.so.*

%files -n libosmocore-devel
%dir %_includedir/%name/
%dir %_includedir/%name/osmocom/
%_includedir/%name/osmocom/core/
%_libdir/libosmocore.so
%_libdir/pkgconfig/libosmocore.pc
%_datadir/aclocal/osmo_ax_code_coverage.m4
%_datadir/aclocal/osmo_ac_code_coverage.m4

%files -n libosmoctrl0
%_libdir/libosmoctrl.so.*

%files -n libosmoctrl-devel
%dir %_includedir/%name/
%dir %_includedir/%name/osmocom/
%_includedir/%name/osmocom/ctrl/
%_libdir/libosmoctrl.so
%_libdir/pkgconfig/libosmoctrl.pc

%files -n libosmogb14
%_libdir/libosmogb.so.*

%files -n libosmogb-devel
%dir %_includedir/%name/
%dir %_includedir/%name/osmocom/
%_includedir/%name/osmocom/gprs/
%_libdir/libosmogb.so
%_libdir/pkgconfig/libosmogb.pc

%files -n libosmogsm20
%_libdir/libosmogsm.so.*

%files -n libosmogsm-devel
%dir %_includedir/%name/
%dir %_includedir/%name/osmocom/
%_includedir/%name/osmocom/gsm/
%_includedir/%name/osmocom/crypt/
%_libdir/libosmogsm.so
%_libdir/pkgconfig/libosmogsm.pc

%files -n libosmoisdn0
%_libdir/libosmoisdn.so.*

%files -n libosmoisdn-devel
%dir %_includedir/%name/
%dir %_includedir/%name/osmocom/
%_includedir/%name/osmocom/isdn/
%_libdir/libosmoisdn.so
%_libdir/pkgconfig/libosmoisdn.pc

%files -n libosmosim2
%_libdir/libosmosim.so.*

%files -n libosmosim-devel
%dir %_includedir/%name/
%dir %_includedir/%name/osmocom/
%_includedir/%name/osmocom/sim/
%_libdir/libosmosim.so
%_libdir/pkgconfig/libosmosim.pc

%files -n libosmousb0
%_libdir/libosmousb.so.*

%files -n libosmousb-devel
%dir %_includedir/%name/
%dir %_includedir/%name/osmocom/
%_includedir/%name/osmocom/usb/
%_libdir/libosmousb.so
%_libdir/pkgconfig/libosmousb.pc

%files -n libosmovty13
%_libdir/libosmovty.so.*

%files -n libosmovty-devel
%dir %_includedir/%name/
%dir %_includedir/%name/osmocom/
%_includedir/%name/osmocom/vty/
%_includedir/%name/osmo-release.mk
%_libdir/libosmovty.so
%_libdir/pkgconfig/libosmovty.pc

%changelog
