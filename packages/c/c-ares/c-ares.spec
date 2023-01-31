#
# spec file for package c-ares
#
# Copyright (c) 2023 SUSE LLC
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


%define sonum   2
%define libname libcares%{sonum}
%if 0%{!?cmake_build:1}
%define cmake_build make -O VERBOSE=1 %{?_smp_mflags}
%endif
Name:           c-ares
Version:        1.19.0
Release:        0
Summary:        Library for asynchronous name resolves
License:        MIT
URL:            https://c-ares.org/
Source0:        https://c-ares.org/download/c-ares-%{version}.tar.gz
Source1:        https://c-ares.org/download/c-ares-%{version}.tar.gz.asc
Source3:        c-ares.keyring
Source4:        baselibs.conf
Patch0:         0001-Use-RPM-compiler-options.patch
Patch1:         disable-live-tests.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
# Needed for getservbyport_r function to work properly.
BuildRequires:  netcfg
BuildRequires:  pkgconfig

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

%build
%cmake \
%if 0%{?suse_version} >= 1500
    -DCARES_BUILD_TESTS:BOOL=ON \
%endif
     %nil

%cmake_build

%install
%cmake_install

%check
%if 0%{?suse_version} >= 1500
pushd build
%cmake_build -C test
LD_LIBRARY_PATH=.%_libdir:./%_lib ./bin/arestest
%endif

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

%changelog
