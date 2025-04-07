#
# spec file for package libkcapi
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover 1
Name:           libkcapi
Version:        1.5.0
Release:        0
Summary:        Linux Kernel Crypto API User Space Interface Library
License:        BSD-3-Clause OR GPL-2.0-only
Group:          Productivity/Security
URL:            https://www.chronox.de/libkcapi/
Source:         https://www.chronox.de/libkcapi/releases/%{version}/%{name}-%{version}.tar.xz
Source1:        https://www.chronox.de/libkcapi/releases/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        libkcapi.keyring
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  openssl
BuildRequires:  xmlto

%description
libkcapi exports APIs so that developers need not consider the low-level
Netlink interface handling that is used for accesing the Linux kernel crypto
API.

%package -n libkcapi%{sover}
Summary:        Linux Kernel Crypto API User Space Interface Library
Group:          System/Libraries

%description -n libkcapi%{sover}
libkcapi allows user-space to access the Linux kernel crypto API.

%package devel
Summary:        Linux Kernel Crypto API User Space Interface Library
Group:          Development/Languages/C and C++
Requires:       libkcapi%{sover} = %{version}

%description devel
libkcapi exports APIs so that developers need not consider the low-level
Netlink interface handling that is used for accesing the Linux kernel crypto
API.

The library does not implement any cipher algorithms. All consumer requests are
sent to the kernel for processing. Results from the kernel crypto API are
returned to the consumer via the library API.

The kernel interface and therefore this library can be used by unprivileged
processes.

This library does not perform any memcpy for processing the cryptographic data!
The library uses scatter / gather lists to eliminate the need for moving data
around in memory.

%package tools
Summary:        Linux Kernel Crypto API User Space Tools
Group:          Development/Tools/Other

%description tools
libkcapi user space tools to access certain hash algorithms.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure \
  --disable-static		\
  --enable-kcapi-test		\
  --enable-kcapi-speed		\
  --enable-kcapi-hasher		\
  --enable-kcapi-rngapp		\
  --enable-kcapi-encapp		\
  --enable-kcapi-dgstapp	\
  %{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# do not ship hmac files unless we (re)generated them
find %{buildroot} -type f -name "*.hmac" -delete -print
# Add generation of HMAC checksums of the libary and kcapi-hasher binary
%define __spec_install_post \
	%{?__debug_package:%{__debug_install_post}} \
	%{__arch_install_post} \
	%__os_install_post \
	openssl sha512 -hmac FIPS-FTW-RHT2009 %{buildroot}/%{_bindir}/kcapi-hasher |sed -e 's/.* //;' > %{buildroot}/%{_bindir}/.kcapi-hasher.hmac \
	openssl sha512 -hmac FIPS-FTW-RHT2009 %{buildroot}/%{_libdir}/libkcapi.so.%{version}|sed -e 's/.* //;' > %{buildroot}/%{_libdir}/.libkcapi.so.%{version}.hmac \
	openssl sha512 -hmac FIPS-FTW-RHT2009 %{buildroot}/%{_libdir}/libkcapi.so.%{sover}|sed -e 's/.* //;' > %{buildroot}/%{_libdir}/.libkcapi.so.%{sover}.hmac \
	openssl sha512 -hmac FIPS-FTW-RHT2009 %{buildroot}/%{_libdir}/libkcapi.so|sed -e 's/.* //;' > %{buildroot}/%{_libdir}/.libkcapi.so.hmac \
	%{nil}

%ldconfig_scriptlets -n libkcapi%{sover}

%files -n libkcapi%{sover}
%license COPYING COPYING.bsd COPYING.gplv2
%doc CHANGES.md
%{_libdir}/libkcapi.so.%{sover}
%{_libdir}/libkcapi.so.%{sover}.*
%{_libdir}/.libkcapi.so.%{sover}.hmac
%{_libdir}/.libkcapi.so.%{version}.hmac

%files devel
%license COPYING COPYING.bsd COPYING.gplv2
%{_includedir}/kcapi.h
%{_mandir}/man3/*3%{?ext_man}
%{_libdir}/libkcapi.so
%{_libdir}/.libkcapi.so.hmac
%{_libdir}/pkgconfig/libkcapi.pc

%files tools
%license COPYING COPYING.bsd COPYING.gplv2
%{_bindir}/*
%{_libexecdir}/libkcapi
%{_bindir}/.kcapi-hasher.hmac
%{_mandir}/man1/*1%{?ext_man}

%changelog
