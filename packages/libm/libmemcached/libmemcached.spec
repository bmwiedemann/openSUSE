#
# spec file for package libmemcached
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


%define libsoname %{name}11
Name:           libmemcached
Version:        1.1.4
Release:        0
Summary:        A C/C++ client library and tools for the memcached server
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://awesomized.github.io/%{name}/
Source0:        https://github.com/awesomized/%{name}/archive/refs/tags/%{version}.tar.gz
# List of additional build dependencies
BuildRequires:  automake >= 1.13
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  cyrus-sasl-devel
BuildRequires:  flex
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

%package -n libmemcachedprotocol0
Summary:        Libmemcached is a C/C++ client library and tools for the memcached server
Group:          System/Libraries

%description -n libmemcachedprotocol0
Libmemcached is a C/C++ client library and tools for the memcached server
(http://memcached.org/). It has been designed to be light on memory
usage, thread safe, and provide full access to server side methods.

The libmemcachedprotocol library contains functions with interacting with
the memcached server.

%package devel
Summary:        Libmemcached is a C/C++ client library and tools for the memcached server
Group:          Development/Libraries/C and C++
Requires:       %{libsoname} = %{version}
Requires:       %{name} = %{version}
# memcached.h includes memcached-1.0/struct/sasl.h, which in turn includes sasl/sasl.h
Requires:       cyrus-sasl-devel
Requires:       glibc-devel
Requires:       libmemcachedprotocol0 = %{version}
Requires:       libmemcachedutil2 = %{version}

%description devel
Libmemcached is a C/C++ client library and tools for the memcached server
(http://memcached.org/). It has been designed to be light on memory
usage, thread safe, and provide full access to server side methods.

%prep
%setup -q

%build
%cmake \
    -DBUILD_DOCS_HTML=OFF \
    -DBUILD_DOCS_MANGZ=ON \
    -DENABLE_SASL=ON \
    -DBUILD_TESTING=ON
%cmake_build

%check
make test

%install
%cmake_install

# remove not needed files
rm -f %{buildroot}%{_datadir}/aclocal/ax_libmemcached.m4
rm -f %{buildroot}%{_libdir}/libp9y.a
rm -f %{buildroot}%{_libdir}/cmake/*/p9y*

%post -n %{libsoname} -p /sbin/ldconfig
%postun -n %{libsoname} -p /sbin/ldconfig
%post -n libmemcachedutil2 -p /sbin/ldconfig
%postun -n libmemcachedutil2 -p /sbin/ldconfig
%post -n libmemcachedprotocol0 -p /sbin/ldconfig
%postun -n libmemcachedprotocol0 -p /sbin/ldconfig

%files
%license %{_datadir}/doc/%{name}-awesome/LICENSE
%dir %{_datadir}/doc/%{name}-awesome
%doc %{_datadir}/doc/%{name}-awesome/*
%doc %{_datadir}/%{name}-awesome/example.cnf
%dir %{_datadir}/%{name}-awesome
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
%{_bindir}/memaslap
%{_bindir}/memstat
%{_bindir}/memtouch
%{_mandir}/man1/mem*.1%{?ext_man}

%files -n %{libsoname}
%license LICENSE
%{_libdir}/%{name}.so.*

%files -n libmemcachedutil2
%{_libdir}/libhashkit.so.2
%{_libdir}/libhashkit.so.2.*.*
%{_libdir}/libmemcachedutil.so.2
%{_libdir}/libmemcachedutil.so.2.*.*

%files -n libmemcachedprotocol0
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
%dir %{_libdir}/cmake/%{name}-awesome
%{_libdir}/cmake/%{name}-awesome/%{name}-*.cmake
%{_libdir}/cmake/%{name}-awesome/libhashkit-*.cmake
%{_libdir}/cmake/%{name}-awesome/%{name}util-*.cmake
%{_libdir}/cmake/%{name}-awesome/%{name}protocol-*.cmake

%changelog
