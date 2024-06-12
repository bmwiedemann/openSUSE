#
# spec file for package c-ares
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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
%define pkg_suffix %nil

%if "@BUILD_FLAVOR@"%nil == "testsuite"%nil
%define pkg_suffix -testsuite
%endif

Name:           c-ares%pkg_suffix
Version:        1.30.0
Release:        0
Summary:        Library for asynchronous name resolves
License:        MIT
URL:            https://c-ares.org/
Source0:        https://github.com/c-ares/c-ares/releases/download/v%{version}/c-ares-%{version}.tar.gz
Source1:        https://github.com/c-ares/c-ares/releases/download/v%{version}/c-ares-%{version}.tar.gz.asc
Source3:        c-ares.keyring
Source4:        baselibs.conf
BuildRequires:  c++_compiler
BuildRequires:  cmake
# Needed for getservbyport_r function to work properly.
BuildRequires:  netcfg
BuildRequires:  pkgconfig
%if ("@BUILD_FLAVOR@" == "testsuite")
BuildRequires:  gmock
BuildRequires:  gtest
%endif

%description
c-ares is a C library that performs DNS requests and name resolves
asynchronously. c-ares is a fork of the library named 'ares', written
by Greg Hudson at MIT.

%if ("@BUILD_FLAVOR@" != "testsuite")
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
Summary:        Development files for c-ares
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

%endif

%prep
%autosetup -n c-ares-%{version}

%build
%cmake \
%if ("@BUILD_FLAVOR@" == "testsuite")
	-DCARES_BUILD_TESTS:BOOL=ON \
%endif
	%{nil}
%cmake_build

%install
%if ("@BUILD_FLAVOR@" != "testsuite")
%cmake_install
%endif

%if ("@BUILD_FLAVOR@" != "testsuite")
%ldconfig_scriptlets -n %{libname}
%endif

%check
%if ("@BUILD_FLAVOR@" == "testsuite")
pushd build
%cmake_build -C test
LD_LIBRARY_PATH=.%{_libdir}:./%{_lib} ./bin/arestest --gtest_filter=-*.Live*
%endif

%if ("@BUILD_FLAVOR@" != "testsuite")
%files utils
%license LICENSE.md
%{_bindir}/adig
%{_bindir}/ahost
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
