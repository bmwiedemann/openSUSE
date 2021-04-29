#
# spec file for package dSFMT
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


%define lib_ver 2_2
Name:           dSFMT
Version:        2.2.5
Release:        0
Summary:        Double precision SIMD-oriented Fast Mersenne Twister
License:        BSD-3-Clause
Group:          System/Libraries
URL:            http://www.math.sci.hiroshima-u.ac.jp/m-mat/MT/SFMT/
Source0:        https://github.com/MersenneTwister-Lab/dSFMT/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE dSFMT-sharedlib-makefile.patch -- Build target for shared library
Patch0:         dSFMT-sharedlib-makefile.patch

%description
Double precision SIMD-oriented Fast Mersenne Twister (dSFMT)

The purpose of dSFMT is to speed up the generation by avoiding the expensive
conversion of integer to double (floating point). dSFMT directly generates
double precision floating point pseudorandom numbers which have the IEEE
Standard for Binary Floating-Point Arithmetic (ANSI/IEEE Std 754-1985) format.
dSFMT is only available on the CPUs which use IEEE 754 format double
precision floating point numbers.

%package     -n lib%{name}%{lib_ver}
Summary:        Double precision SIMD-oriented Fast Mersenne Twister
Group:          System/Libraries

%description -n lib%{name}%{lib_ver}
Double precision SIMD-oriented Fast Mersenne Twister (dSFMT)

The purpose of dSFMT is to speed up the generation by avoiding the expensive
conversion of integer to double (floating point). dSFMT directly generates
double precision floating point pseudorandom numbers which have the IEEE
Standard for Binary Floating-Point Arithmetic (ANSI/IEEE Std 754-1985) format.
dSFMT is only available on the CPUs which use IEEE 754 format double
precision floating point numbers.

%package        devel
Summary:        Double precision SIMD-oriented Fast Mersenne Twister
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{lib_ver} = %{version}

%description    devel
Double precision SIMD-oriented Fast Mersenne Twister (dSFMT)

The purpose of dSFMT is to speed up the generation by avoiding the expensive
conversion of integer to double (floating point). dSFMT directly generates
double precision floating point pseudorandom numbers which have the IEEE
Standard for Binary Floating-Point Arithmetic (ANSI/IEEE Std 754-1985) format.
dSFMT is only available on the CPUs which use IEEE 754 format double
precision floating point numbers.

This package provides libraries and header files for developing applications
that use dSFMT.

%prep
%setup -q
%patch0 -p1

%build
%ifarch x86_64
%make_build sse2_shared CFLAGS="%{optflags}"
%endif
%make_build sharedlib CFLAGS="%{optflags}"

%install
make install DESTDIR=%{buildroot} libdir="%{_libdir}"

%post -n lib%{name}%{lib_ver} -p /sbin/ldconfig
%postun -n lib%{name}%{lib_ver} -p /sbin/ldconfig

%files -n lib%{name}%{lib_ver}
%license LICENSE.txt
%{_libdir}/lib%{name}.so.*

%files devel
%doc CHANGE-LOG.txt README.txt
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}*

%changelog
