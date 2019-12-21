#
# spec file for package gf2x
#
# Copyright (c) 2019 SUSE LLC
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


Name:           gf2x
%define lname	libgf2x3
Version:        1.3.0
Release:        0
Summary:        Library for multiplication over the GF(2) field
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gforge.inria.fr/projects/gf2x/

# Caution: the filename does not matter - the ID (38243) determines which source you get.
Source:         https://gforge.inria.fr/frs/download.php/file/38243/gf2x-1.3.0.tar.gz
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkg-config

%description
gf2x is a library for multiplication of polynomials over the
GF(2) binary field.

%package -n %lname
Summary:        Library for multiplication over the GF(2) field
Group:          System/Libraries

%description -n %lname
gf2x is a library for multiplication of polynomials over the
GF(2) binary field.

%package devel
Summary:        Development headers for libgf2x
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
gf2x is a library for fast multiplication of polynomials over the
GF(2) binary field.

This package contains the interface definitions for the gf2x library.
 
%prep
%autosetup -p1

%build
autoreconf -fi
# SSE2 may not be available on all x86_32 machines.
# PCLMUL may not be available on all machines.
%configure --disable-static \
%ifarch %ix86
	--disable-sse2 \
%endif
	--disable-pclmul \
	--enable-fft-interface
make %{?_smp_mflags}

%check
make check %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libgf2x.so.*
%_libdir/libgf2x-fft.so.*
%license COPYING

%files devel
%_includedir/gf2x*
%_libdir/libgf2x.so
%_libdir/libgf2x-fft.so
%_libdir/pkgconfig/*.pc

%changelog
