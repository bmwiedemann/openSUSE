#
# spec file for package libnfc
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           libnfc
%define lname	libnfc5
Summary:        Library for Near Field Communication
License:        LGPL-3.0+ and GPL-2.0+
Group:          Development/Libraries/C and C++
Version:        1.7.1
Release:        0
Url:            http://libnfc.org/

#Git-Clone:	http://code.google.com/p/libnfc/
Source:         http://dl.bintray.com/nfc-tools/sources/%name-%version.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#BuildRequires:  autoconf
#BuildRequires:  automake
#BuildRequires:  libtool >= 2
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
%if 0%{?suse_version} == 1110
BuildRequires:  libusb-devel
BuildRequires:  pcsc-lite-devel
%else
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(libusb)
%endif

%description
libnfc is a low-level SDK for various RFID and NFC applications.

It supports various NFC hardware devices: dongles, flat and OEM
devices. The library currently supports modulations for ISO/IEC 14443
(A and B), FeliCa, Jewel tags and Data Exchange Protocol (P2P) as
target and as initiator.

%package -n %lname
Summary:        Library for Near Field Communication
License:        LGPL-3.0+
Group:          System/Libraries

%description -n %lname
libnfc is a low-level SDK for various RFID and NFC applications.

It supports various NFC hardware devices: dongles, flat and OEM
devices. The library currently supports modulations for ISO/IEC 14443
(A and B), FeliCa, Jewel tags and Data Exchange Protocol (P2P) as
target and as initiator.

%package devel
Summary:        Development files for the Near Field Communications library
License:        LGPL-3.0+ and GPL-2.0+
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
%if 0%{?suse_version} == 1110
# The include files don't need it, but libnfc.pc does. And pkgconfig()
# did not yet exist in SLE11.
Requires:       libusb-devel
%endif

%description devel
libnfc is a low-level SDK for various RFID and NFC applications.

It supports various NFC hardware devices: dongles, flat and OEM
devices. The library currently supports modulations for ISO/IEC 14443
(A and B), FeliCa, Jewel tags and Data Exchange Protocol (P2P) as
target and as initiator.

This package contains the libnfc development files.

%package tools
Summary:        Tools for Near Field Communication
License:        LGPL-3.0+ and GPL-2.0+
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
if [ ! -e configure ]; then
	autoreconf -fi
fi
%configure --disable-static
make %{?_smp_mflags}

%install
b="%buildroot"
%make_install
rm -f "$b/%_libdir"/*.la
mkdir -p "%buildroot/%_sysconfdir/nfc"

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/libnfc.so.5*

%files devel
%defattr(-,root,root)
%_includedir/nfc
%_libdir/libnfc.so
%_libdir/pkgconfig/libnfc.pc

%files tools
%defattr(-,root,root)
%_bindir/nfc-*
%_bindir/pn53x-*
%_mandir/man*/*.1*
%dir %_sysconfdir/nfc
%doc libnfc.conf.sample

%changelog
