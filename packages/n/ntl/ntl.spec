#
# spec file for package ntl
#
# Copyright (c) 2021 SUSE LLC
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


Name:           ntl
%define lname	libntl44
Version:        11.5.1
Release:        0
Summary:        Library for Number Theory
License:        LGPL-2.1-or-later
Group:          Productivity/Scientific/Math
URL:            https://shoup.net/ntl/

#Git-Clone:     https://github.com/libntl/ntl
Source:         https://shoup.net/ntl/ntl-%version.tar.gz
Patch1:         no-static.diff
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gf2x-devel
BuildRequires:  gmp-devel >= 3.1

%description
NTL is a C++ library providing data structures and algorithms for
manipulating signed, arbitrary length integers, and for vectors,
matrices, and polynomials over the integers and over finite fields.

%package -n %lname
Summary:        Library for Number Theory
Group:          System/Libraries

%description -n %lname
NTL is a C++ library providing data structures and algorithms for
manipulating signed, arbitrary length integers, and for vectors,
matrices, and polynomials over the integers and over finite fields.

%package devel
Summary:        Development files for libntl
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
NTL is a C++ library providing data structures and algorithms for
manipulating signed, arbitrary length integers, and for vectors,
matrices, and polynomials over the integers and over finite fields.

This package contains the headers and library links to libntl.

%package doc
Summary:        Documentation for NTL, a number theory library
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
NTL is a C++ library providing data structures and algorithms for
manipulating signed, arbitrary length integers, and for vectors,
matrices, and polynomials over the integers and over finite fields.

This package contains the documentation for the NTL API.

%prep
%autosetup -p1

%build
pushd src/
./configure CXXFLAGS="%optflags" DEF_PREFIX="%_prefix" LIBDIR="%_libdir" \
	DOCDIR="%_defaultdocdir" NTL_GF2X_LIB=on SHARED=on NATIVE=off
make %{?_smp_mflags}
popd

%install
pushd src/
%make_install
mv "%buildroot/%_defaultdocdir/NTL" "%buildroot/%_defaultdocdir/ntl"
popd
rm -fv "%buildroot/%_libdir"/*.la
%fdupes %buildroot/%_prefix

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libntl.so.*
%license doc/copying.txt

%files devel
%_includedir/NTL/
%_libdir/libntl.so

%files doc
%_defaultdocdir/%name/

%changelog
