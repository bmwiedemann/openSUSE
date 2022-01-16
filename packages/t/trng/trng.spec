#
# spec file for package trng
#
# Copyright (c) 2022 SUSE LLC
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


%global shlib libtrng4-24
Name:           trng
Version:        4.24
Release:        0
Summary:        A Random Number Generator Library
License:        BSD-3-Clause
URL:            https://www.numbercrunch.de/trng/
Source:         https://github.com/rabauke/trng4/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM trng-drop-findtbb-cmake-module.patch gh#rabauke/trng4#26 badshah400@gmail.com -- Drop outdated FindTBB.cmake module and depend on TBB's bundled cmake module
Patch0:         trng-drop-findtbb-cmake-module.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_test-devel
BuildRequires:  tbb-devel

%description
TRNG is a pseudo random number generator C++ library.

%package -n %{shlib}
Summary:        A Random Number Generator Library

%description -n %{shlib}
TRNG is a C++ pseudo random number generator library.

Key features:
* compatible with the C++11 random number facility as defined in
  <random>
* implements various pseudo random number algorithms
* supports multiple streams of random numbers for parallel
  (multi-threaded) applications
* may be used with any threading library or MPI
* pseudo random numbers can be sampled from many different distributions

%package devel
Summary:        Headers and devel files for TRNG
Requires:       %{shlib} = %{version}

%description devel
TRNG is a C++ pseudo random number generator library.

This package provides the headers and devel files for developing
applications against TRNG.

%prep
%autosetup -p1 -n %{name}4-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install
find %{buildroot}%{_libdir} -name *.a -delete -print

%check
export LD_LIBRARY_PATH="%{buildroot}%{_libdir}"
./%{__builddir}/tests/test_all --no_color_output -l test_suite -r short

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files -n %{shlib}
%license COPYING
%{_libdir}/libtrng4.so.*

%files devel
%license COPYING
%doc AUTHORS NEWS README.md doc/trng.pdf examples/
%{_libdir}/libtrng4.so
%{_includedir}/trng/

%changelog
