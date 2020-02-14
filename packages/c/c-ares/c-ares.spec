#
# spec file for package c-ares
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define realver 1.15.0-20200117
Name:           c-ares
Version:        1.15.0+20200117
Release:        0
Summary:        Library for asynchronous name resolves
License:        MIT
URL:            https://c-ares.haxx.se/
#Source0:        https://c-ares.haxx.se/daily-snapshot/c-ares-%{realver}.tar.gz
Source0:        c-ares-%{realver}.tar.gz
#Source0:        http://c-ares.haxx.se/download/%{name}-%{version}.tar.gz
#Source1:        http://c-ares.haxx.se/download/%{name}-%{version}.tar.gz.asc
Source3:        %{name}.keyring
Source4:        baselibs.conf
Patch0:         0001-Use-RPM-compiler-options.patch
Patch1:         disable-live-tests.patch
Patch2:         regression.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libtool
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
%autosetup -p1 -n %{name}-%{realver}

# Remove bogus cflags checking
sed -i -e '/XC_CHECK_BUILD_FLAGS/d' configure.ac
sed -i -e '/XC_CHECK_USER_FLAGS/d' m4/xc-cc-check.m4

%build
%cmake \
    -DCARES_STATIC:BOOL=OFF \
    -DCARES_SHARED:BOOL=ON \
    -DCARES_INSTALL:BOOL=ON \
    -DCARES_BUILD_TESTS:BOOL=ON \
    -DCARES_BUILD_TOOLS:BOOL=ON
make %{?_smp_mflags}

%install
%cmake_install
install -m 644 -Dt %{buildroot}%{_mandir}/man1/ *.1
install -m 644 -Dt %{buildroot}%{_mandir}/man3/ *.3
find %{buildroot} -type f -name "*.la" -delete -print

%check
pushd build
make -C test %{?_smp_mflags}
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:./lib
./bin/arestest

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files utils
%license LICENSE.md
%{_bindir}/acountry
%{_bindir}/adig
%{_bindir}/ahost
%{_mandir}/man1/acountry.1%{ext_man}
%{_mandir}/man1/adig.1%{ext_man}
%{_mandir}/man1/ahost.1%{ext_man}

%files -n %{libname}
%license LICENSE.md
%{_libdir}/libcares.so.2*

%files devel
%license LICENSE.md
%{_libdir}/libcares.so
%{_includedir}/*.h
%{_mandir}/man3/ares_*.3%{ext_man}
%{_libdir}/pkgconfig/libcares.pc
%{_libdir}/cmake/c-ares/

%changelog
