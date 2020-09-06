#
# spec file for package libkcapi
#
# Copyright (c) 2020 SUSE LLC
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


Name:           libkcapi
Version:        1.2.0
Release:        0
Summary:        Linux Kernel Crypto API User Space Interface Library
License:        GPL-2.0-only
Group:          Productivity/Security
URL:            http://www.chronox.de/libkcapi.html
Source:         https://www.chronox.de/libkcapi/libkcapi-%{version}.tar.xz
Source1:        https://www.chronox.de/libkcapi/libkcapi-%{version}.tar.xz.asc
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

%package -n libkcapi1
Summary:        Linux Kernel Crypto API User Space Interface Library
Group:          System/Libraries

%description -n libkcapi1
libkcapi allows user-space to access the Linux kernel crypto API.

%package devel
Summary:        Linux Kernel Crypto API User Space Interface Library
Group:          Development/Languages/C and C++
Requires:       libkcapi1 = %{version}

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
%setup -q

%build
autoreconf -i
%configure 			\
  --disable-static		\
  --enable-kcapi-test		\
  --enable-kcapi-speed		\
  --enable-kcapi-hasher		\
  --enable-kcapi-rngapp		\
  --enable-kcapi-encapp		\
  --enable-kcapi-dgstapp

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} LIBDIR="%{_libdir}" BINDIR=/%{_libexecdir}/libkcapi/ %{?_smp_mflags} 
rm %{buildroot}/%_libdir/libkcapi.la

mkdir -p %{buildroot}/%{_libexecdir}/libkcapi/
mv %{buildroot}/usr/bin/* %{buildroot}/%{_libexecdir}/libkcapi/
mv %{buildroot}/usr/bin/.??* %{buildroot}/%{_libexecdir}/libkcapi/

# Add generation of HMAC checksums of the final fipshmac fipscheck stripped binaries
%define __spec_install_post \
	%{?__debug_package:%{__debug_install_post}} \
	%{__arch_install_post} \
	%{__os_install_post} \
	openssl sha256 -hmac orboDeJITITejsirpADONivirpUkvarP $RPM_BUILD_ROOT/%{_libexecdir}/libkcapi/fipscheck   |sed -e 's/.* //;' > $RPM_BUILD_ROOT/%{_libexecdir}/libkcapi/.fipscheck.hmac \
	openssl sha256 -hmac orboDeJITITejsirpADONivirpUkvarP $RPM_BUILD_ROOT/%{_libexecdir}/libkcapi/fipshmac   |sed -e 's/.* //;' > $RPM_BUILD_ROOT/%{_libexecdir}/libkcapi/.fipshmac.hmac \
	openssl sha256 -hmac orboDeJITITejsirpADONivirpUkvarP $RPM_BUILD_ROOT/%{_libexecdir}/libkcapi/sha1sum   |sed -e 's/.* //;' > $RPM_BUILD_ROOT/%{_libexecdir}/libkcapi/.sha1sum.hmac \
	openssl sha256 -hmac orboDeJITITejsirpADONivirpUkvarP $RPM_BUILD_ROOT/%{_libexecdir}/libkcapi/sha256sum |sed -e 's/.* //;' > $RPM_BUILD_ROOT/%{_libexecdir}/libkcapi/.sha256sum.hmac \
	openssl sha256 -hmac orboDeJITITejsirpADONivirpUkvarP $RPM_BUILD_ROOT/%{_libexecdir}/libkcapi/sha384sum |sed -e 's/.* //;' > $RPM_BUILD_ROOT/%{_libexecdir}/libkcapi/.sha384sum.hmac \
	openssl sha256 -hmac orboDeJITITejsirpADONivirpUkvarP $RPM_BUILD_ROOT/%{_libexecdir}/libkcapi/sha512sum |sed -e 's/.* //;' > $RPM_BUILD_ROOT/%{_libexecdir}/libkcapi/.sha512sum.hmac \
	openssl sha512 -hmac FIPS-FTW-RHT2009 $RPM_BUILD_ROOT/%{_libexecdir}/libkcapi/sha1hmac   |sed -e 's/.* //;' > $RPM_BUILD_ROOT/%{_libexecdir}/libkcapi/.sha1hmac.hmac \
	openssl sha512 -hmac FIPS-FTW-RHT2009 $RPM_BUILD_ROOT/%{_libexecdir}/libkcapi/sha256hmac |sed -e 's/.* //;' > $RPM_BUILD_ROOT/%{_libexecdir}/libkcapi/.sha256hmac.hmac \
	openssl sha512 -hmac FIPS-FTW-RHT2009 $RPM_BUILD_ROOT/%{_libexecdir}/libkcapi/sha384hmac |sed -e 's/.* //;' > $RPM_BUILD_ROOT/%{_libexecdir}/libkcapi/.sha384hmac.hmac \
	openssl sha512 -hmac FIPS-FTW-RHT2009 $RPM_BUILD_ROOT/%{_libexecdir}/libkcapi/sha512hmac |sed -e 's/.* //;' > $RPM_BUILD_ROOT/%{_libexecdir}/libkcapi/.sha512hmac.hmac \
	openssl sha512 -hmac FIPS-FTW-RHT2009 $RPM_BUILD_ROOT/%_libdir/libkcapi.so|sed -e 's/.* //;' > $RPM_BUILD_ROOT/%_libdir/.libkcapi.so.hmac \
	openssl sha512 -hmac FIPS-FTW-RHT2009 $RPM_BUILD_ROOT/%_libdir/libkcapi.so.1|sed -e 's/.* //;' > $RPM_BUILD_ROOT/%_libdir/.libkcapi.so.1.hmac \
	openssl sha512 -hmac FIPS-FTW-RHT2009 $RPM_BUILD_ROOT/%_libdir/libkcapi.so.%version|sed -e 's/.* //;' > $RPM_BUILD_ROOT/%_libdir/.libkcapi.so.%version.hmac \
	%{nil}

%post -n libkcapi1 -p /sbin/ldconfig

%postun -n libkcapi1 -p /sbin/ldconfig

%files -n libkcapi1
%license COPYING
%doc CHANGES.md
%{_libdir}/libkcapi.so.1.*
%{_libdir}/libkcapi.so.1
%{_libdir}/.libkcapi.so.1*

%files devel
%{_includedir}/kcapi.h
%{_mandir}/man3/*
%{_libdir}/libkcapi.so
%{_libdir}/.libkcapi.so.hmac
%{_libdir}/pkgconfig/libkcapi.pc

%files tools
%dir %{_libexecdir}/libkcapi
%{_libexecdir}/libkcapi/*sum*
%{_libexecdir}/libkcapi/*hmac*
%{_libexecdir}/libkcapi/.*.hmac
%{_libexecdir}/libkcapi/kcapi
%{_libexecdir}/libkcapi/kcapi-convenience
%{_libexecdir}/libkcapi/compile-test.sh
%{_libexecdir}/libkcapi/hasher-test.sh
%{_libexecdir}/libkcapi/kcapi-convenience.sh
%{_libexecdir}/libkcapi/kcapi-dgst-test.sh
%{_libexecdir}/libkcapi/kcapi-enc-test-large
%{_libexecdir}/libkcapi/kcapi-enc-test-large.sh
%{_libexecdir}/libkcapi/kcapi-enc-test.sh
%{_libexecdir}/libkcapi/kcapi-fuzz-test.sh
%{_libexecdir}/libkcapi/fipscheck
%{_libexecdir}/libkcapi/kcapi-dgst
%{_libexecdir}/libkcapi/kcapi-enc
%{_libexecdir}/libkcapi/kcapi-rng
%{_libexecdir}/libkcapi/kcapi-speed
%{_libexecdir}/libkcapi/libtest.sh
%{_libexecdir}/libkcapi/test-invocation.sh
%{_libexecdir}/libkcapi/test.sh
%{_libexecdir}/libkcapi/virttest.sh
%{_mandir}/man1/kcapi*

%changelog
