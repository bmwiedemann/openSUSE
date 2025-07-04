#
# spec file for package libiec61883
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


Name:           libiec61883
Version:        1.2.0
Release:        0
Summary:        An isochronous streaming media library for IEEE 1394
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Hardware/Other
URL:            https://ieee1394.wiki.kernel.org/index.php/Main_Page
#Git-Web:	https://git.kernel.org/cgit/libs/ieee1394/libiec61883.git
#Git-Clone:	git://git.kernel.org/pub/scm/libs/ieee1394/libiec61883
Source:         https://www.kernel.org/pub/linux/libs/ieee1394/%name-%version.tar.xz
Source2:        https://www.kernel.org/pub/linux/libs/ieee1394/%name-%version.tar.sign
Source3:        %name.keyring
Source4:        baselibs.conf
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  pkgconfig(libraw1394)

%description
This library is an implementation of IEC 61883, part 1 (CIP, plug
registers, and CMP), part 2 (DV-SD), part 4 (MPEG2-TS), and part 6
(AMDTP). Outside of IIDC, nearly all FireWire multimedia devices use
IEC 61883 protocols.

%package -n libiec61883-0
Summary:        An isochronous streaming media library for IEEE 1394
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libiec61883-0
This library is an implementation of IEC 61883, part 1 (CIP, plug
registers, and CMP), part 2 (DV-SD), part 4 (MPEG2-TS), and part 6
(AMDTP). Outside of IIDC, nearly all FireWire multimedia devices use
IEC 61883 protocols.

The libiec61883 library provides a higher level API for streaming DV,
MPEG-2 and audio over Linux IEEE 1394. This includes both reception and
transmission. It uses the new "rawiso" API of libraw1394, which
transparently provides mmap-ed DMA for efficient data transfer. It also
represents the third generation of I/O technology for Linux 1394 for
these media types thereby removing the complexities of additional
kernel modules, /dev nodes, and procfs. It also consolidates features
for plug control registers and connection management that previously
existed in experimental form in an unreleased version of libavc1394.

%package devel
Summary:        Development files for libiec61883
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       libiec61883-0 = %version

%description devel
This library is an implementation of IEC 61883, part 1 (CIP, plug
registers, and CMP), part 2 (DV-SD), part 4 (MPEG2-TS), and part 6
(AMDTP). Outside of IIDC, nearly all FireWire multimedia devices use
IEC 61883 protocols.

The libiec61883 library provides a higher level API for streaming DV,
MPEG-2 and audio over Linux IEEE 1394.

%package tools
Summary:        Command-line utilities for IEC 61883 devices
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Hardware/Other
# added on 2015-11-14
Obsoletes:      %name < %version-%release
Provides:       %name = %version-%release

%description tools
Utilities to inspect and control IEC 61883 hardware.

%prep
%autosetup -p1

%build
export CFLAGS="%optflags -fno-strict-aliasing"
%configure --disable-static
%make_build all

%install
%make_install
libtool --mode=install install -m 755 examples/test-mpeg2 %{buildroot}%{_bindir}
rm -f %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets -n libiec61883-0

%files tools
%doc AUTHORS NEWS README
%{_bindir}/*
%doc %{_mandir}/man1/*%{?ext_man}

%files -n libiec61883-0
%license COPYING*
%{_libdir}/libiec61883.so.*

%files devel
%{_includedir}/libiec61883
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%changelog
