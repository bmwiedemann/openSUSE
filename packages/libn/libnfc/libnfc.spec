#
# spec file for package libnfc
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


Name:           libnfc
%define lname	libnfc6
Version:        1.8.0
Release:        0
Summary:        Library for Near Field Communication
License:        LGPL-3.0-or-later AND GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://libnfc.org/

#Git-Clone:	https://github.com/nfc-tools/libnfc
Source:         https://github.com/nfc-tools/libnfc/releases/download/%name-%version/%name-%version.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  pkg-config
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(libusb)

%description
libnfc is a low-level SDK for various RFID and NFC applications.

It supports various NFC hardware devices: dongles, flat and OEM
devices. The library currently supports modulations for ISO/IEC 14443
(A and B), FeliCa, Jewel tags and Data Exchange Protocol (P2P) as
target and as initiator.

%package -n %lname
Summary:        Library for Near Field Communication
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %lname
libnfc is a low-level SDK for various RFID and NFC applications.

It supports various NFC hardware devices: dongles, flat and OEM
devices. The library currently supports modulations for ISO/IEC 14443
(A and B), FeliCa, Jewel tags and Data Exchange Protocol (P2P) as
target and as initiator.

%package devel
Summary:        Development files for the Near Field Communications library
License:        LGPL-3.0-or-later AND GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libnfc is a low-level SDK for various RFID and NFC applications.

It supports various NFC hardware devices: dongles, flat and OEM
devices. The library currently supports modulations for ISO/IEC 14443
(A and B), FeliCa, Jewel tags and Data Exchange Protocol (P2P) as
target and as initiator.

This package contains the libnfc development files.

%package tools
Summary:        Tools for Near Field Communication
License:        LGPL-3.0-or-later AND GPL-2.0-or-later
Group:          Hardware/Other

%description tools
libnfc is a low-level SDK for various RFID and NFC applications.

It supports various NFC hardware devices: dongles, flat and OEM
devices. The library currently supports modulations for ISO/IEC 14443
(A and B), FeliCa, Jewel tags and Data Exchange Protocol (P2P) as
target and as initiator.

This package contains the NFC utilities.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
rm -fv "%buildroot/%_libdir"/*.la
mkdir -p "%buildroot/%_sysconfdir/nfc"

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libnfc.so.6*

%files devel
%_includedir/nfc
%_libdir/libnfc.so
%_libdir/pkgconfig/libnfc.pc

%files tools
%_bindir/nfc-*
%_bindir/pn53x-*
%_mandir/man*/*.1*
%dir %_sysconfdir/nfc
%doc libnfc.conf.sample

%changelog
