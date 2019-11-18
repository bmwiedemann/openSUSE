#
# spec file for package c-ares
#
# Copyright (c) 2019 SUSE LLC.
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


%define libname libcares2
%define realver 1.15.0-20191108
Name:           c-ares
Version:        1.15.0+20191108
Release:        0
Summary:        Library for asynchronous name resolves
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://c-ares.haxx.se/
#Source0:        https://c-ares.haxx.se/daily-snapshot/c-ares-%{realver}.tar.gz
Source0:        c-ares-%{realver}.tar.gz
#Source0:        http://c-ares.haxx.se/download/%{name}-%{version}.tar.gz
#Source1:        http://c-ares.haxx.se/download/%{name}-%{version}.tar.gz.asc
Source3:        %{name}.keyring
Source4:        baselibs.conf
Patch0:         0001-Use-RPM-compiler-options.patch
Patch1:         disable-live-tests.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
c-ares is a C library that performs DNS requests and name resolves
asynchronously. c-ares is a fork of the library named 'ares', written
by Greg Hudson at MIT.

%package -n %{libname}
Summary:        Library for asynchronous name resolves
Group:          System/Libraries

%description -n %{libname}
c-ares is a C library that performs DNS requests and name resolves
asynchronously. c-ares is a fork of the library named 'ares', written
by Greg Hudson at MIT.

%package devel
Summary:        Library for asynchronous name resolves
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       glibc-devel
Provides:       libcares-devel = %{version}
Obsoletes:      libcares-devel < %{version}

%description devel
c-ares is a C library that performs DNS requests and name resolves
asynchronously. c-ares is a fork of the library named 'ares', written
by Greg Hudson at MIT.

%prep
%autosetup -p1 -n %{name}-%{realver}

# Remove bogus cflags checking
sed -i -e '/XC_CHECK_BUILD_FLAGS/d' configure.ac
sed -i -e '/XC_CHECK_USER_FLAGS/d' m4/xc-cc-check.m4

%build
autoreconf -fiv
%configure \
	--disable-silent-rules \
	--enable-symbol-hiding \
	--enable-nonblocking \
	--enable-shared \
	--disable-static \
	--enable-tests
make %{?_smp_mflags}

%check
make -C test %{?_smp_mflags}
./test/arestest

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE.md
%{_libdir}/libcares.so.2*

%files devel
%{_libdir}/libcares.so
%{_includedir}/*.h
%{_mandir}/man3/ares_*
%{_libdir}/pkgconfig/libcares.pc

%changelog
