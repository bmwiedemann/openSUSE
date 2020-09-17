#
# spec file for package libasn1c
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


Name:           libasn1c
Version:        0.9.32
Release:        0
Summary:        Osmocon ASN.1 decoder and encoder library
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
URL:            https://git.osmocom.org/libasn1c

Source:         %name-%version.tar.xz
BuildRequires:  libtool >= 2
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  pkgconfig(libosmocore) >= 0.1.13

%description
Lev Walkins's asn1c runtime, as a shared library and with
modifications for Osmocom.

Compiles ASN.1 data structures into C source structures that can be
simply (un)marshalled from and to: BER, DER, CER, BASIC-XER, CXER,
EXTENDED-XER, PER.

%package -n libasn1c1
Summary:        Osmocon ASN.1 decoder and encoder library
Group:          System/Libraries

%description -n libasn1c1
Lev Walkins's asn1c runtime, as a shared library and with
modifications for Osmocom.

Compiles ASN.1 data structures into C source structures that can be
simply (un)marshalled from and to: BER, DER, CER, BASIC-XER, CXER,
EXTENDED-XER, PER.

%package -n libasn1c-devel
Summary:        Development files for libasn1c, Osmocom's ASN.1 decoder and encoder library
Group:          Development/Libraries/C and C++
Requires:       libasn1c1 = %version
Requires:       pkgconfig(talloc)

%description -n libasn1c-devel
Compiles ASN.1 data structures into C source structures that can be
simply (un)marshalled from and to: BER, DER, CER, BASIC-XER, CXER,
EXTENDED-XER, PER.

This subpackage contains libraries and header files for developing
applications that want to make use of libasn1c.

%prep
%autosetup -p1

%build
echo "%version" >.tarball-version
autoreconf -fi
# bugzilla.opensuse.org/795968 for rationale
%configure --disable-static --includedir="%_includedir/%name"
%make_build

%install
%make_install
find "%buildroot/%_libdir" -type f -name "*.la" -delete

%check
if ! %make_build check; then
	find . -name testsuite.log -exec cat "{}" "+"
fi

%post   -n libasn1c1 -p /sbin/ldconfig
%postun -n libasn1c1 -p /sbin/ldconfig

%files -n libasn1c1
%_libdir/libasn1c.so.1*

%files -n libasn1c-devel
%license COPYING
%_includedir/%name/
%_libdir/pkgconfig/*.pc
%_libdir/libasn1c.so

%changelog
