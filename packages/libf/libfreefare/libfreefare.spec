#
# spec file for package libfreefare
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libfreefare
%define lname	libfreefare0
Version:        0.4.0
Release:        0
Summary:        API for Mifare card manipulations
License:        LGPL-3.0+
Group:          Development/Libraries/C and C++
URL:            https://github.com/nfc-tools/libfreefare/
Source:         https://github.com/nfc-tools/libfreefare/archive/%name-%version.tar.gz
Patch1:         gcc14.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libnfc) >= 1.7.0

%description
The libfreefare project aims to provide a convenient API for Mifare
card manipulations. Supported tags include: Classic 1k/4k, DESFire
2K/4K/8K, Ultralight/C. Supported features include: Mifare
Application Directory (MAD) v1-v3.

%package -n %lname
Summary:        Library for Mifare card manipulations
Group:          System/Libraries

%description -n %lname
The libfreefare project aims to provide a convenient API for Mifare
card manipulations. Supported tags include: Classic 1k/4k, DESFire
2K/4K/8K, Ultralight/C. Supported features include: Mifare
Application Directory (MAD) v1-v3.

%package devel
Summary:        Development files for the Mifare card manipulation library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
The libfreefare project aims to provide a convenient API for Mifare
card manipulations. Supported tags include: Classic 1k/4k, DESFire
2K/4K/8K, Ultralight/C. Supported features include: Mifare
Application Directory (MAD) v1-v3.

This package contains the libfreefare development files.

%package tools
Summary:        Tools for Mifare cards
Group:          Hardware/Other

%description tools
The libfreefare project aims to provide a convenient API for Mifare
card manipulations. Supported tags include: Classic 1k/4k, DESFire
2K/4K/8K, Ultralight/C. Supported features include: Mifare
Application Directory (MAD) v1-v3.

This package contains example programs using libfreefare for
inspecting and manipulating Mifare cards.

%prep
%autosetup -n %name-%name-%version -p1

%build
if [ ! -e configure ]; then
	autoreconf -fi
fi
%configure --disable-static
%make_build

%install
b="%buildroot";
%make_install
rm -f "$b/%_libdir"/*.la;

%ldconfig_scriptlets -n %lname

%files -n %lname
%_libdir/libfreefare.so.0*

%files devel
%_includedir/freefare.h
%_mandir/man3/*.3*
%_libdir/libfreefare.so
%_libdir/pkgconfig/libfreefare.pc

%files tools
%_bindir/mifare-*

%changelog
