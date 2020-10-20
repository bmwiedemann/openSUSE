#
# spec file for package libdnet
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


Name:           libdnet
Version:        1.14
Release:        0
Summary:        Library for Portable Interface to Low-Level Networking Routines
License:        BSD-3-Clause
URL:            https://github.com/dugsong/libdnet
Source0:        https://github.com/dugsong/libdnet/archive/%{name}-%{version}.tar.gz
# Skip the test subdir, as installing that is not necessary
Patch1:         skip-test-subdir.patch
BuildRequires:  libbsd-devel
BuildRequires:  libtool

%description
libdnet provides a portable interface to several low-level
networking routines, including:
* network address manipulation
* kernel arp(4) cache and route(4) table lookup and manipulation
* network firewalling (IP filter, ipfw, ipchains, pf, PktFilter, ...)
* network interface lookup and manipulation
* IP tunnelling (BSD/Linux tun, Universal TUN/TAP device)
* raw IP packet and Ethernet frame transmission

%package -n libdnet1
Summary:        Library for Portable Interface to Low-Level Networking Routines

%description -n libdnet1
libdnet provides a portable interface to several low-level
networking routines, including:
* network address manipulation
* kernel arp(4) cache and route(4) table lookup and manipulation
* network firewalling (IP filter, ipfw, ipchains, pf, PktFilter, ...)
* network interface lookup and manipulation
* IP tunnelling (BSD/Linux tun, Universal TUN/TAP device)
* raw IP packet and Ethernet frame transmission

%package devel
Summary:        Development files for libdnet
Requires:       glibc-devel
Requires:       libdnet1 = %{version}

%description devel
libdnet provides a portable interface to several low-level
networking routines, including:
- network address manipulation
- kernel arp(4) cache and route(4) table lookup and manipulation
- network firewalling (IP filter, ipfw, ipchains, pf, PktFilter, ...)
- network interface lookup and manipulation
- IP tunnelling (BSD/Linux tun, Universal TUN/TAP device)
- raw IP packet and Ethernet frame transmission

%prep
%setup -q -n %{name}-%{name}-%{version}
%autopatch -p1

%build
ACLOCAL="aclocal -I config" autoreconf -fvi
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libdnet1 -p /sbin/ldconfig
%postun -n libdnet1 -p /sbin/ldconfig

%files -n libdnet1
%{_libdir}/libdnet.so.1*

%files devel
%license LICENSE
%doc README.md TODO THANKS
%{_bindir}/dnet-config
%{_includedir}/dnet.h
%dir %{_includedir}/dnet
%{_includedir}/dnet/*.h
%{_libdir}/libdnet.so
%{_mandir}/man?/dnet.*%{ext_man}

%changelog
