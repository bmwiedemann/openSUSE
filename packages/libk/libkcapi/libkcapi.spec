#
# spec file for package libkcapi
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           libkcapi
Version:        0.13.0
Release:        0
Summary:        Linux Kernel Crypto API User Space Interface Library
License:        GPL-2.0
Group:          Productivity/Security
Url:            http://www.chronox.de/libkcapi.html
#Source:		https://github.com/smuellerDD/libkcapi/archive/v0.13.0.zip
Source:         libkcapi-0.13.0.tar.bz2
Patch0:         libkcapi-use-external-fipshmac.patch
# PATCH-FIX-UPSTREAM rewritten upstream in https://github.com/smuellerDD/libkcapi/commit/0e7b2b0300782
Patch1:         reproduciblesort.patch
# PATCH-FIX-UPSTREAM https://github.com/smuellerDD/libkcapi/pull/12
Patch2:         reproducibledate.patch
BuildRequires:  fipscheck
BuildRequires:  openssl
BuildRequires:  xmlto

%description
libkcapi exports APIs so that developers need not consider the low-level
Netlink interface handling that is used for accesing the Linux kernel crypto
API.

%package -n libkcapi0
Summary:        Linux Kernel Crypto API User Space Interface Library
Group:          System/Libraries

%description -n libkcapi0
libkcapi allows user-space to access the Linux kernel crypto API.

%package devel
Summary:        Linux Kernel Crypto API User Space Interface Library
Group:          Development/Languages/C and C++
Requires:       libkcapi0 = %{version}

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
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cd lib
make %{?_smp_mflags}
make man
cd ../apps
make %{?_smp_mflags}

%install
cd lib
make install maninstall DESTDIR=%{buildroot} LIBDIR="%{_libdir}" %{?_smp_mflags}
cd ../apps
make install DESTDIR=%{buildroot} %{?_smp_mflags} BINDIR=/usr/%_lib/libkcapi/

# Add generation of HMAC checksums of the final fipshmac fipscheck stripped binaries
%define __spec_install_post \
	%{?__debug_package:%{__debug_install_post}} \
	%{__arch_install_post} \
	%{__os_install_post} \
	openssl sha256 -hmac orboDeJITITejsirpADONivirpUkvarP $RPM_BUILD_ROOT/usr/%_lib/libkcapi/fipscheck |sed -e 's/.* //;' > $RPM_BUILD_ROOT/usr/%_lib/libkcapi/.fipscheck.hmac \
	openssl sha256 -hmac orboDeJITITejsirpADONivirpUkvarP $RPM_BUILD_ROOT/usr/%_lib/libkcapi/fipshmac  |sed -e 's/.* //;' > $RPM_BUILD_ROOT/usr/%_lib/libkcapi/.fipshmac.hmac \
	openssl sha256 -hmac orboDeJITITejsirpADONivirpUkvarP $RPM_BUILD_ROOT/usr/%_lib/libkcapi/sha1sum   |sed -e 's/.* //;' > $RPM_BUILD_ROOT/usr/%_lib/libkcapi/.sha1sum.hmac \
	openssl sha256 -hmac orboDeJITITejsirpADONivirpUkvarP $RPM_BUILD_ROOT/usr/%_lib/libkcapi/sha256sum |sed -e 's/.* //;' > $RPM_BUILD_ROOT/usr/%_lib/libkcapi/.sha256sum.hmac \
	openssl sha256 -hmac orboDeJITITejsirpADONivirpUkvarP $RPM_BUILD_ROOT/usr/%_lib/libkcapi/sha384sum |sed -e 's/.* //;' > $RPM_BUILD_ROOT/usr/%_lib/libkcapi/.sha384sum.hmac \
	openssl sha256 -hmac orboDeJITITejsirpADONivirpUkvarP $RPM_BUILD_ROOT/usr/%_lib/libkcapi/sha512sum |sed -e 's/.* //;' > $RPM_BUILD_ROOT/usr/%_lib/libkcapi/.sha512sum.hmac \
	openssl sha512 -hmac FIPS-FTW-RHT2009 $RPM_BUILD_ROOT/usr/%_lib/libkcapi/sha1hmac   |sed -e 's/.* //;' > $RPM_BUILD_ROOT/usr/%_lib/libkcapi/.sha1hmac.hmac \
	openssl sha512 -hmac FIPS-FTW-RHT2009 $RPM_BUILD_ROOT/usr/%_lib/libkcapi/sha256hmac |sed -e 's/.* //;' > $RPM_BUILD_ROOT/usr/%_lib/libkcapi/.sha256hmac.hmac \
	openssl sha512 -hmac FIPS-FTW-RHT2009 $RPM_BUILD_ROOT/usr/%_lib/libkcapi/sha384hmac |sed -e 's/.* //;' > $RPM_BUILD_ROOT/usr/%_lib/libkcapi/.sha384hmac.hmac \
	openssl sha512 -hmac FIPS-FTW-RHT2009 $RPM_BUILD_ROOT/usr/%_lib/libkcapi/sha512hmac |sed -e 's/.* //;' > $RPM_BUILD_ROOT/usr/%_lib/libkcapi/.sha512hmac.hmac \
	%{nil}

%post -n libkcapi0 -p /sbin/ldconfig

%postun -n libkcapi0 -p /sbin/ldconfig

%files -n libkcapi0
%license COPYING
%doc CHANGES
%{_libdir}/libkcapi.so.0.13.*
%{_libdir}/libkcapi.so.0

%files devel
%{_includedir}/kcapi.h
%{_mandir}/man3/*

%files tools
%dir %{_libdir}/libkcapi
%{_libdir}/libkcapi/*
%{_libdir}/libkcapi/.*hmac

%changelog
