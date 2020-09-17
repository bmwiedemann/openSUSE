#
# spec file for package libosmo-abis
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


%define version_unconverted 1.0.1

Name:           libosmo-abis
Version:        1.0.1
Release:        0
Summary:        Osmocom library for A-bis interface between BTS and BSC
License:        AGPL-3.0-or-later AND GPL-2.0-or-later
Group:          Productivity/Telephony/Utilities
URL:            https://osmocom.org/projects/libosmo-abis/wiki/Libosmo-abis

Source:         %name-%version.tar.xz
Patch1:         osmo-talloc.diff
Patch2:         e1dapi.diff
BuildRequires:  automake >= 1.6
BuildRequires:  libtool >= 2
BuildRequires:  pkgconfig >= 0.20
BuildRequires:  xz
BuildRequires:  pkgconfig(libosmo-e1d)
BuildRequires:  pkgconfig(libosmocodec) >= 1.4.0
BuildRequires:  pkgconfig(libosmocore) >= 1.4.0
BuildRequires:  pkgconfig(libosmogsm) >= 1.4.0
BuildRequires:  pkgconfig(libosmovty) >= 1.4.0
BuildRequires:  pkgconfig(ortp) >= 0.22
BuildRequires:  pkgconfig(talloc)

%description
In GSM, A-bis is a BSS-internal interface link between the BTS and
BSC. This interface allows control of the radio equipment and radio
frequency allocation in the BTS.

%package -n libosmoabis9
Summary:        Osmocom GSM A-bis interface library
License:        AGPL-3.0-or-later
Group:          System/Libraries

%description -n libosmoabis9
In the GSM system architecture, A-bis is a Base Station
System-internal interface linking the Base Transceiver Stations (BTS)
and Base Station Controller (BSC). This interface allows control of
the radio equipment and radio frequency allocation in the BTS.

This library contains common/shared code regarding this A-bis
interface. It also implements drivers for mISDN and DAHDI-based E1
cards, as well as some A-bis/IP dialects.

%package -n libosmoabis-devel
Summary:        Development files for the Osmocom GSM A-bis library
License:        AGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libosmoabis9 = %version
Requires:       libosmocore-devel >= 1.4.0
Requires:       libosmogsm-devel >= 1.4.0

%description -n libosmoabis-devel
This library contains common/shared code regarding the GSM A-bis
interface. It also implements drivers for mISDN and DAHDI-based E1
cards, as well as some A-bis/IP dialects.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmoabis.

%package -n libosmotrau2
Summary:        Osmocom GSM TRAU (E1/RTP) library
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n libosmotrau2
This library implements the Transcoder and Rate Adaptation Unit (TRAU) for
GSM systems.
The TRAU enables the use of lower rates (32, 16 or 8 kbps) over the
A-bis interface instead of the 64 kbps ISDN rate for which the Mobile
Switching Center (MSC) is designed.

%package -n libosmotrau-devel
Summary:        Development files for the Osmocom TRAU (E1/RTP) library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libosmotrau2 = %version

%description -n libosmotrau-devel
This library implements the Transcoder and Rate Adaptation Unit
(TRAU) for GSM systems.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmotrau.

%prep
%autosetup -p1

%build
echo "%version" >.tarball-version
autoreconf -fiv
# bugzilla.opensuse.org/795968 for rationale
%configure --includedir="%_includedir/%name" \
	--enable-shared --disable-static --disable-dahdi --enable-e1d
%make_build

%install
%make_install
find "%buildroot/%_libdir" -type f -name "*.la" -delete

%check
if ! %make_build check; then
	find . -name testsuite.log -exec cat "{}" "+"
%ifarch %ix86 x86_64
	exit 1
%endif
fi

%post   -n libosmoabis9 -p /sbin/ldconfig
%postun -n libosmoabis9 -p /sbin/ldconfig
%post   -n libosmotrau2 -p /sbin/ldconfig
%postun -n libosmotrau2 -p /sbin/ldconfig

%files -n libosmoabis9
%_libdir/libosmoabis.so.9*

%files -n libosmoabis-devel
%license COPYING
%dir %_includedir/%name/
%dir %_includedir/%name/osmocom/
%_includedir/%name/osmocom/abis/
%_libdir/libosmoabis.so
%_libdir/pkgconfig/libosmoabis.pc

%files -n libosmotrau2
%_libdir/libosmotrau.so.2*

%files -n libosmotrau-devel
%license COPYING
%dir %_includedir/%name/
%dir %_includedir/%name/osmocom/
%_includedir/%name/osmocom/trau/
%_libdir/libosmotrau.so
%_libdir/pkgconfig/libosmotrau.pc

%changelog
