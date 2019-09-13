#
# spec file for package libmemcached
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


%define libsoname %{name}11
Name:           libmemcached
Version:        1.0.18
Release:        0
Summary:        A C/C++ client library and tools for the memcached server
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            http://libmemcached.org
Source0:        https://launchpad.net/libmemcached/1.0/%{version}/+download/libmemcached-%{version}.tar.gz
Source1:        https://launchpad.net/libmemcached/1.0/%{version}/+download/libmemcached-%{version}.tar.gz.asc
Source2:        %{name}.keyring
# PATCH-FIX-UPSTREAM libmemcached-pthread.patch lp#133614 dimstar@opensuse.org -- Fix pthread detection
Patch0:         libmemcached-pthread.patch
Patch1:         libmemcached-automake1_14.diff
# PATCH-FIX-UPSTREAM libmemcached-no-docs-available.patch dimstar@opensuse.org -- Do not build docs if not VCS checkout
Patch2:         libmemcached-no-docs-available.patch
# PATCH-FIX-UPSTREAM libmemcached-1.0.18-fix-build-gcc7.patch -- Fix build with GCC 7
Patch3:         libmemcached-1.0.18-fix-build-gcc7.patch
# List of additional build dependencies
BuildRequires:  automake >= 1.13
BuildRequires:  bison
BuildRequires:  cyrus-sasl-devel
# needed for man pages
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libevent-devel
BuildRequires:  libtool
BuildRequires:  memcached
BuildRequires:  pkgconfig
BuildRequires:  python3-Sphinx

%description
Libmemcached is a C/C++ client library and tools for the memcached server
(http://memcached.org/). It has been designed to be light on memory
usage, thread safe, and provide full access to server side methods.

%package -n %{libsoname}
Summary:        Libmemcached is a C/C++ client library and tools for the memcached server
Group:          System/Libraries

%description -n %{libsoname}
Libmemcached is a C/C++ client library and tools for the memcached server
(http://memcached.org/). It has been designed to be light on memory
usage, thread safe, and provide full access to server side methods.

%package -n libmemcachedutil2
Summary:        Libmemcached is a C/C++ client library and tools for the memcached server
Group:          System/Libraries

%description -n libmemcachedutil2
Libmemcached is a C/C++ client library and tools for the memcached server
(http://memcached.org/). It has been designed to be light on memory
usage, thread safe, and provide full access to server side methods.

The libmemcachedutil library contains utility functions used by
libmemcached.

%package devel
Summary:        Libmemcached is a C/C++ client library and tools for the memcached server
Group:          Development/Libraries/C and C++
Requires:       %{libsoname} = %{version}
Requires:       %{name} = %{version}
# memcached.h includes memcached-1.0/struct/sasl.h, which in turn includes sasl/sasl.h
Requires:       cyrus-sasl-devel
Requires:       glibc-devel
Requires:       libmemcachedutil2 = %{version}

%description devel
Libmemcached is a C/C++ client library and tools for the memcached server
(http://memcached.org/). It has been designed to be light on memory
usage, thread safe, and provide full access to server side methods.

%prep
%setup -q
%patch -P 0 -P 1 -p1
%patch2 -p1
%patch3 -p1

%build
autoreconf -fiv
%configure \
  --disable-static \
  --enable-libmemcachedprotocol \
  --with-memcached=%{_sbindir}/memcached
make V=1 CFLAGS="-std=c99 %{optflags}" CXXFLAGS="%{optflags}" %{?_smp_mflags}

%install
%make_install V=1 CFLAGS="-std=c99 %{optflags}" CXXFLAGS="%{optflags}"
find %{buildroot} -type f -name "*.la" -delete -print
# create symlinks for man pages
%fdupes -s %{buildroot}%{_mandir}

# remove not needed files
rm -f %{buildroot}%{_datadir}/aclocal/ax_libmemcached.m4

%post -n %{libsoname} -p /sbin/ldconfig
%postun -n %{libsoname} -p /sbin/ldconfig
%post -n libmemcachedutil2 -p /sbin/ldconfig
%postun -n libmemcachedutil2 -p /sbin/ldconfig

%files
%{_bindir}/memcapable
%{_bindir}/memcat
%{_bindir}/memcp
%{_bindir}/memdump
%{_bindir}/memerror
%{_bindir}/memexist
%{_bindir}/memflush
%{_bindir}/memparse
%{_bindir}/memping
%{_bindir}/memrm
%{_bindir}/memslap
%{_bindir}/memstat
%{_bindir}/memtouch
%{_mandir}/man1/mem*.1%{?ext_man}

%files -n %{libsoname}
%license COPYING
%{_libdir}/%{name}.so.*

%files -n libmemcachedutil2
%{_libdir}/libhashkit.so.2
%{_libdir}/libhashkit.so.2.*.*
%{_libdir}/libmemcachedutil.so.2
%{_libdir}/libmemcachedutil.so.2.*.*
%{_libdir}/libmemcachedprotocol.so.0
%{_libdir}/libmemcachedprotocol.so.0.*.*

%files devel
%dir %{_includedir}/%{name}
%dir %{_includedir}/%{name}-1.0
%dir %{_includedir}/libhashkit
%dir %{_includedir}/libhashkit-1.0
%dir %{_includedir}/libmemcachedprotocol-0.0
%dir %{_includedir}/libmemcachedutil-1.0
%{_includedir}/libhashkit/*
%{_includedir}/libhashkit-1.0/*
%{_includedir}/%{name}/*
%{_includedir}/%{name}-1.0/*
%{_includedir}/libmemcachedprotocol-0.0/*
%{_includedir}/libmemcachedutil-1.0/*
%{_libdir}/pkgconfig/libmemcached.pc
%{_libdir}/libhashkit.so
%{_libdir}/%{name}.so
%{_libdir}/libmemcachedutil.so
%{_libdir}/libmemcachedprotocol.so
%{_mandir}/man3/*.3%{?ext_man}

%changelog
