#
# spec file for package c-ares
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           c-ares
Version:        1.15.0
Release:        0
Summary:        Library for asynchronous name resolves
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://c-ares.haxx.se/
Source0:        http://c-ares.haxx.se/download/%{name}-%{version}.tar.gz
Source1:        http://c-ares.haxx.se/download/%{name}-%{version}.tar.gz.asc
Source3:        %{name}.keyring
Source4:        baselibs.conf
Patch0:         0001-Use-RPM-compiler-options.patch
Patch1:         disable-live-tests.patch
Patch2:         onion-crash.patch
# PATCH-FEATURE-UPSTREAM 0001-Add-initial-implementation-for-ares_getaddrinfo-112.patch
Patch3:         0001-Add-initial-implementation-for-ares_getaddrinfo-112.patch
# PATCH-FEATURE-UPSTREAM 0002-Remaining-queries-counter-fix-additional-unit-tests-.patch
Patch4:         0002-Remaining-queries-counter-fix-additional-unit-tests-.patch
# PATCH-FEATURE-UPSTREAM 0003-Bugfix-for-ares_getaddrinfo-and-additional-unit-test.patch
Patch5:         0003-Bugfix-for-ares_getaddrinfo-and-additional-unit-test.patch
# PATCH-FEATURE-UPSTREAM 0004-Add-ares__sortaddrinfo-to-support-getaddrinfo-sorted.patch
Patch6:         0004-Add-ares__sortaddrinfo-to-support-getaddrinfo-sorted.patch
# PATCH-FEATURE-UPSTREAM 0005-getaddrinfo-avoid-infinite-loop-in-case-of-NXDOMAIN-.patch
Patch7:         0005-getaddrinfo-avoid-infinite-loop-in-case-of-NXDOMAIN-.patch
# PATCH-FEATURE-UPSTREAM 0006-getaddrinfo-callback-must-be-called-on-bad-domain-24.patch
Patch8:         0006-getaddrinfo-callback-must-be-called-on-bad-domain-24.patch
# PATCH-FEATURE-UPSTREAM 0007-getaddrinfo-enhancements-257.patch
Patch9:         0007-getaddrinfo-enhancements-257.patch
# PATCH-FEATURE-UPSTREAM 0008-Add-missing-limits.h-include-from-ares_getaddrinfo.c.patch
Patch10:        0008-Add-missing-limits.h-include-from-ares_getaddrinfo.c.patch
# PATCH-FEATURE-UPSTREAM 0009-Increase-portability-of-ares-test-mock-ai.cc-235.patch
Patch11:        0009-Increase-portability-of-ares-test-mock-ai.cc-235.patch
# PATCH-FIX-OPENSUSE 0010-Disable-failing-test.patch
Patch12:        0010-Disable-failing-test.patch
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
%autosetup -p1

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
