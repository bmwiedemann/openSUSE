#
# spec file for package brial
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


%define lname	libbrial3
Name:           brial
Version:        1.2.10
Release:        0
Summary:        The Polynomials over Boolean Rings Computer Algebra System
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://github.com/BRiAl/BRiAl
Source:         https://github.com/BRiAl/BRiAl/releases/download/%version/%name-%version.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  libboost_headers-devel >= 1.58
BuildRequires:  libboost_test-devel >= 1.58
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig(m4ri)
Provides:       bundled(cudd) = 2.5.0

%description
PolyBoRi/BRiAl is a special purpose computer algebra system for
computations in Boolean Rings. The core is a C++ library, which
provides high-level data types for Boolean polynomials and related
structures. As a unique approach, binary decision diagrams are used
as internal storage type for polynomial structures.

%package -n %lname
Summary:        The Polynomials over Boolean Rings Computer Algebra System library
Group:          System/Libraries

%description -n %lname
The core of PolyBoRi/BRiAl is a C++ library, which provides
high-level data types for Boolean polynomials and monomials, exponent
vectors, as well as for the underlying polynomial rings and subsets
of the powerset of the Boolean variables. As a unique approach,
binary decision diagrams are used as internal storage type for
polynomial structures.

%package devel
Summary:        Development files for polybori, a CAS for Boolean Polynomials
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       boost-devel

%description devel
The core of PolyBoRi/BRiAl is a C++ library, which provides
high-level data types for Boolean polynomials and monomials, exponent
vectors, as well as for the underlying polynomial rings and subsets
of the powerset of the Boolean variables. As a unique approach,
binary decision diagrams are used as internal storage type for
polynomial structures.

This subpackage contains the include files and library links for
developing with polybori/brial libraries.

%prep
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install
find %buildroot -type f -name "*.la" -delete -print

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libbrial.so.3*
%_libdir/libbrial_groebner.so.3*

%files devel
%license LICENSE
%_includedir/polybori/
%_includedir/polybori.h
%_libdir/libbrial.so
%_libdir/libbrial_groebner.so

%changelog
