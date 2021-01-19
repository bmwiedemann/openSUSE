#
# spec file for package c-ares
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


%global flavor @BUILD_FLAVOR@%{nil}

%if "%{flavor}" == "%{nil}"
ExclusiveArch:  do_not_build
%define pname   c-ares
%endif

%if "%{flavor}" == "tests"
%define pname   c-ares-tests
%bcond_without  tests
%endif

%if "%{flavor}" == "main"
%define pname   c-ares
%bcond_with     tests
%endif

%define sonum   2
%define libname libcares%{sonum}

%if 0%{!?cmake_build:1}
%define cmake_build make -O VERBOSE=1 %{?_smp_mflags}
%endif

Name:           %{pname}
Version:        1.17.1
Release:        0
Summary:        Library for asynchronous name resolves
License:        MIT
URL:            https://c-ares.haxx.se/
Source0:        http://c-ares.haxx.se/download/c-ares-%{version}.tar.gz
Source1:        http://c-ares.haxx.se/download/c-ares-%{version}.tar.gz.asc
Source3:        c-ares.keyring
Source4:        baselibs.conf
### REMOVE when upstream fixes https://github.com/c-ares/c-ares/issues/373
Source5:        libcares.pc.cmake
Source6:        c-ares-config.cmake.in
Source7:        ares_dns.h
Patch0:         0001-Use-RPM-compiler-options.patch
Patch1:         disable-live-tests.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
%if %{with tests}
# Needed for getservbyport_r function to work properly.
BuildRequires:  netcfg
%endif
BuildRequires:  pkg-config

%description
c-ares is a C library that performs DNS requests and name resolves
asynchronously. c-ares is a fork of the library named 'ares', written
by Greg Hudson at MIT.

%package        utils
Summary:        Tools for asynchronous name resolves

%description    utils
c-ares is a C library that performs DNS requests and name resolves
asynchronously. c-ares is a fork of the library named 'ares', written
by Greg Hudson at MIT.

This package provides some tools that make use of c-ares.

%package     -n %{libname}
Summary:        Library for asynchronous name resolves
# Needed for getservbyport_r function to work properly.
Requires:       netcfg

%description -n %{libname}
c-ares is a C library that performs DNS requests and name resolves
asynchronously. c-ares is a fork of the library named 'ares', written
by Greg Hudson at MIT.

This package provides the shared libraries for c-ares.

%package devel
Summary:        Development files for %{name}
Requires:       %{libname} = %{version}
Requires:       glibc-devel
Provides:       libcares-devel = %{version}
Obsoletes:      libcares-devel < %{version}

%description devel
c-ares is a C library that performs DNS requests and name resolves
asynchronously. c-ares is a fork of the library named 'ares', written
by Greg Hudson at MIT.

This package provides the development libraries and headers needed
to build packages that depend on c-ares.


%prep
%autosetup -p1 -n c-ares-%{version}

cp %{S:5} %{S:6} .
cp %{S:7} include

%build

%cmake \
%if %{with tests}
    -DCARES_BUILD_TESTS:BOOL=ON \
%endif
    %{nil}
%cmake_build

%install
%if !%{with tests}
%cmake_install
%endif

%if %{with tests}
%check
pushd build
%cmake_build -C test
./bin/arestest
%endif

%if !%{with tests}

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files utils
%license LICENSE.md
%{_bindir}/acountry
%{_bindir}/adig
%{_bindir}/ahost
%{_mandir}/man1/acountry.1%{?ext_man}
%{_mandir}/man1/adig.1%{?ext_man}
%{_mandir}/man1/ahost.1%{?ext_man}

%files -n %{libname}
%license LICENSE.md
%{_libdir}/libcares.so.%{sonum}*

%files devel
%license LICENSE.md
%{_libdir}/libcares.so
%{_includedir}/*.h
%{_mandir}/man3/ares_*.3%{?ext_man}
%{_libdir}/pkgconfig/libcares.pc
%{_libdir}/cmake/c-ares/

%endif

%changelog
