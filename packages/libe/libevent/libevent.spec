#
# spec file for package libevent
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


Name:           libevent
%define     version_base 2
%define     version_minor 1
%define     version_release 12
%define     abi_release 7
%define     version_suffix stable
%define     libsoname %{name}-%{version_base}_%{version_minor}-%{abi_release}

Version:        %{version_base}.%{version_minor}.%{version_release}
Release:        0
Summary:        An event notification library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            http://libevent.org/
Source0:        https://github.com/%{name}/%{name}/releases/download/release-%{version}-%{version_suffix}/%{name}-%{version}-%{version_suffix}.tar.gz
Source1:        https://github.com/%{name}/%{name}/releases/download/release-%{version}-%{version_suffix}/%{name}-%{version}-%{version_suffix}.tar.gz.asc
Source2:        %{name}.keyring
Source3:        libevent-rpmlintrc
Source99:       baselibs.conf
Patch0:         python3-shebang.patch
# PATCH-FEATURE-UPSTREAM 0001-evwatch-Add-prepare-and-check-watchers.patch
Patch1:         0001-evwatch-Add-prepare-and-check-watchers.patch
# PATCH-FEATURE-UPSTREAM 0002-evwatch-fix-race-condition.patch
Patch2:         0002-evwatch-fix-race-condition.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  openssl-devel
%if 0%{?fedora_version} || 0%{?rhel_version}
BuildRequires:  pkgconfig
%else
BuildRequires:  pkg-config
%endif
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The libevent API provides a mechanism to execute a callback function
when a specific event occurs on a file descriptor or after a timeout
has been reached. Furthermore, libevent also support callbacks due to
signals or regular timeouts.

%package -n %{libsoname}
Summary:        An event notification library
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n %{libsoname}
The libevent API provides a mechanism to execute a callback function
when a specific event occurs on a file descriptor or after a timeout
has been reached. Furthermore, libevent also support callbacks due to
signals or regular timeouts.

Currently, libevent supports /dev/poll, kqueue(2), event ports,
POSIX select(2), Windows select(), poll(2), and epoll(4).

Libevent additionally provides a sophisticated framework for buffered
network IO, with support for sockets, filters, rate-limiting, SSL,
zero-copy file transmission, and IOCP. Libevent includes support for
several useful protocols, including DNS, HTTP, and a minimal RPC
framework.

This package holds the shared libraries for libevent.

%package devel
Summary:        Development files for libevent2
Group:          Development/Libraries/C and C++
Requires:       %{libsoname} = %{version}
Requires:       glibc-devel
# Both have /usr/include/event.h
Conflicts:      libev-devel
Provides:       %{name}:%{_includedir}/event.h

%description devel
The libevent API provides a mechanism to execute a callback function
when a specific event occurs on a file descriptor or after a timeout
has been reached. Furthermore, libevent also support callbacks due to
signals or regular timeouts.

This package holds the development files for libevent2.

%package devel-static
Summary:        Static libraries for libevent2
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}

%description devel-static
The libevent API provides a mechanism to execute a callback function
when a specific event occurs on a file descriptor or after a timeout
has been reached. Furthermore, libevent also support callbacks due to
signals or regular timeouts.

This package holds the static libraries for libevent2.

%prep
%setup -q  -n %{name}-%{version}-%{version_suffix}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
./autogen.sh
export ac_cv_func_select=no
%configure \
	--disable-libevent-regress
make %{?_smp_mflags}

%check
make check

%install
%make_install %{?_smp_mflags}
find %{buildroot}%{_libdir} -type f -name "*.la" -delete -print

%post    -n %{libsoname} -p /sbin/ldconfig

%postun  -n %{libsoname} -p /sbin/ldconfig

%files -n %{libsoname}
%defattr(-,root,root,-)
%license LICENSE
%doc ChangeLog whatsnew-2.0.txt whatsnew-2.1.txt
%{_libdir}/%{name}-%{version_base}.%{version_minor}.so.%{abi_release}*
%{_libdir}/%{name}_core-%{version_base}.%{version_minor}.so.%{abi_release}*
%{_libdir}/%{name}_extra-%{version_base}.%{version_minor}.so.%{abi_release}*
%{_libdir}/%{name}_pthreads-%{version_base}.%{version_minor}.so.%{abi_release}*
%{_libdir}/%{name}_openssl-%{version_base}.%{version_minor}.so.%{abi_release}*

%files devel
%defattr(-,root,root)
%{_bindir}/event_rpcgen.py
%{_includedir}/evdns.h
%{_includedir}/event.h
%{_includedir}/evhttp.h
%{_includedir}/evrpc.h
%{_includedir}/evutil.h
%{_includedir}/event2
%{_libdir}/%{name}.so
%{_libdir}/%{name}_core.so
%{_libdir}/%{name}_extra.so
%{_libdir}/%{name}_pthreads.so
%{_libdir}/%{name}_openssl.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}_pthreads.pc
%{_libdir}/pkgconfig/%{name}_openssl.pc
%{_libdir}/pkgconfig/%{name}_core.pc
%{_libdir}/pkgconfig/%{name}_extra.pc

%files devel-static
%defattr(-,root,root)
%{_libdir}/%{name}.a
%{_libdir}/%{name}_core.a
%{_libdir}/%{name}_extra.a
%{_libdir}/%{name}_openssl.a
%{_libdir}/%{name}_pthreads.a

%changelog
