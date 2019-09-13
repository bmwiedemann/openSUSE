#
# spec file for package dSFMT
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           dSFMT
Version:        2.2.3
%define lib_ver 2_2
Release:        0
Summary:        Double precision SIMD-oriented Fast Mersenne Twister
License:        BSD-3-Clause
Group:          System/Libraries
Url:            http://www.math.sci.hiroshima-u.ac.jp/~%20m-mat/MT/SFMT/index.html
Source0:        http://www.math.sci.hiroshima-u.ac.jp/~%20m-mat/MT/SFMT/%{name}-src-%{version}.tar.gz
# PATCH-FIX-OPENSUSE dSFMT-sharedlib.patch -- Build shared library
Patch1:         dSFMT-sharedlib.patch
# PATCH-FIX-OPENSUSE dSFMT-export_functions.patch -- Export functions required to use the library
Patch2:         dSFMT-export_functions.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
%setup -q -n %{name}-src-%{version}
%patch1 -p1
%patch2 -p1

%build
make %{?_smp_mflags} \
     sharedlib \
     libdir=%{_libdir} \
     CCFLAGS="-fPIC %{optflags}"

%install
make install DESTDIR=%{buildroot} \
             libdir=%{_libdir}

%post -n lib%{name}%{lib_ver} -p /sbin/ldconfig

%postun -n lib%{name}%{lib_ver} -p /sbin/ldconfig

%files -n lib%{name}%{lib_ver}
%defattr(-,root,root)
%{_libdir}/lib%{name}.so.*

%files devel
%defattr(-,root,root)
%doc CHANGE-LOG.txt LICENSE.txt README.txt
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}*

%changelog
