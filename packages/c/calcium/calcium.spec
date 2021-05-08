#
# spec file for package calcium
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


Name:           calcium
%define lname   libcalcium0
Version:        0.3.0
Release:        0
Summary:        Library for exact computation with real and complex numbers
License:        LGPL-2.1-or-later
Group:          Productivity/Scientific/Math
URL:            http://fredrikj.net/calcium/
#Git-Clone:	https://github.com/fredrik-johansson/calcium/
Source:         https://github.com/fredrik-johansson/calcium/archive/%version.tar.gz
BuildRequires:  antic-devel
BuildRequires:  arb-devel
BuildRequires:  flint-devel
BuildRequires:  gcc-c++

%description
A C library for exact computation with real and complex numbers.

%package -n %lname
Summary:        Library for exact computation with real and complex numbers
Group:          System/Libraries

%description -n %lname
A C library for exact computation with real and complex numbers.

The basic idea behind Calcium is to represent numbers as elements of
formal fields Q(a_1,…,a_n) where the extension numbers a_k can be
algebraic or transcendental.

%package devel
Summary:        Development files for Calcium, an exact number computation library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
A C library for exact computation with real and complex numbers.

This subpackage contains libraries and header files for developing
applications that want to make use of Calcium.

%prep
%autosetup -p1

%build
# Not autoconf
./configure --prefix="%_prefix" --disable-static CFLAGS="%optflags"
%make_build QUIET_CC= QUIET_CXX= QUIET_AR=

%install
%make_install LIBDIR="%_lib"

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libcalcium.so.0*

%files devel
%_includedir/*
%_libdir/libcalcium.so
%license LICENSE

%changelog
