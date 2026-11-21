#
# spec file for package libcerf
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2014 Christoph Junghans <junghans@votca.org>
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


Name:           libcerf
Version:        3.7
Release:        0
Summary:        A library that complex error functions
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://jugit.fz-juelich.de/mlz/libcerf
Source0:        https://jugit.fz-juelich.de/mlz/libcerf/-/archive/v%{version}/cerf-v%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
libcerf is a self-contained numeric library that provides an efficient and
accurate implementation of complex error functions, along with Dawson,
Faddeeva, and Voigt functions.

%package -n libcerf3
Summary:        A library that provides complex error functions
Group:          Development/Libraries/C and C++

%description -n libcerf3
libcerf is a self-contained numeric library that provides an efficient and
accurate implementation of complex error functions, along with Dawson,
Faddeeva, and Voigt functions.

%package devel
Summary:        Development headers and libraries for libcerf
Group:          Development/Libraries/C and C++
Requires:       libcerf3 = %{version}-%{release}

%description devel
libcerf is a self-contained numeric library that provides an efficient and
accurate implementation of complex error functions, along with Dawson,
Faddeeva, and Voigt functions.

This package contains development headers and libraries for libcerf

%prep
%autosetup -p0 -n cerf-v%{version}

%build
%if %{__isa_bits} == 32
export CFLAGS="%{optflags} -ffloat-store"
export CXXFLAGS="%{optflags} -ffloat-store"
%endif
%cmake -DCMAKE_SKIP_RPATH=OFF -DPORTABLE=ON
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_docdir}/%{name}
if [ -d %{buildroot}%{_datadir}/doc/cerf ]; then
    mv %{buildroot}%{_datadir}/doc/cerf/* %{buildroot}%{_docdir}/%{name}
fi
install CHANGELOG %{buildroot}%{_docdir}/%{name}
%fdupes %{buildroot}%{_prefix}

%post -n libcerf3 -p /sbin/ldconfig
%postun -n libcerf3 -p /sbin/ldconfig

%check
%ctest

%files -n libcerf3
%license LICENSE
%{_libdir}/libcerf.so.*
%{_libdir}/libcerfcpp.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/libcerf.so
%{_libdir}/libcerfcpp.so
%{_libdir}/pkgconfig/libcerf.pc
%{_mandir}/man3/*
%{_docdir}/%{name}
%{_libdir}/cmake/cerf

%changelog
