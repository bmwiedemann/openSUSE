#
# spec file for package libpcap
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libpcap
Version:        1.9.0
Release:        0
Summary:        A Library for Network Sniffers
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            http://www.tcpdump.org/
Source:         http://www.tcpdump.org/release/%{name}-%{version}.tar.gz
Source2:        baselibs.conf
Source3:        http://www.tcpdump.org/tcpdump-workers.asc#/%{name}.keyring
Source4:        http://www.tcpdump.org/release/%{name}-%{version}.tar.gz.sig
# https://github.com/the-tcpdump-group/libpcap/pull/556
Patch2:         libpcap-1.0.0-ppp.patch
Patch3:         libpcap-1.0.0-s390.patch
Patch5:         libpcap-no-old-socket.patch
Patch6:         Check-only-VID-in-VLAN-test-issue-461.patch
BuildRequires:  autoconf >= 2.64
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  bluez-devel
BuildRequires:  dbus-1-devel
BuildRequires:  flex
BuildRequires:  libnl3-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libusb-1.0)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libpcap is a library used by packet sniffer programs. It provides an
interface for them to capture and analyze packets from network devices.
This package is only needed if you plan to compile or write such a
program yourself.

%package -n libpcap1
Summary:        A Library for Network Sniffers
Group:          System/Libraries
Provides:       libpcap = %{version}
Obsoletes:      libpcap < %{version}

%description -n libpcap1
libpcap is a library used by packet sniffer programs. It provides an
interface for them to capture and analyze packets from network devices.
This package is only needed if you plan to compile or write such a
program yourself.

%package devel
Summary:        A Library for Network Sniffers
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libpcap1 = %{version}

%description devel
libpcap is a library used by packet sniffer programs. It provides an
interface for them to capture and analyze packets from network devices.
This package is only needed if you plan to compile or write such a
program yourself.

%package devel-static
Summary:        A Library for Network Sniffers
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Requires:       bluez-devel
Requires:       dbus-1-devel
Requires:       libnl3-devel
Requires:       pkgconfig(libusb-1.0)

%description devel-static
libpcap static libraries

%prep
%setup -q
%patch2
%patch3 -p1
%patch5 -p1
%patch6 -p1

%build
autoreconf -fiv
%ifarch %sparc
pic="PIC"
%else
pic="pic"
%endif
export CFLAGS="%{optflags} -f$pic" CXXFLAGS="%{optflags} -f$pic"
%configure \
	--enable-bluetooth=yes \
	--enable-ipv6
make %{?_smp_mflags} all shared

%install
mkdir -p %{buildroot}%{_bindir}
make DESTDIR=%{buildroot} install install-shared

%post -n libpcap1 -p /sbin/ldconfig
%postun -n libpcap1 -p /sbin/ldconfig

%files -n libpcap1
%defattr(-, root, root)
%doc CHANGES CREDITS LICENSE README.md doc/README.linux.md TODO
%{_libdir}/*.so.*
%{_mandir}/man7/*

%files devel-static
%defattr(-, root, root)
%{_libdir}/*.*a

%files devel
%defattr(-, root, root)
%{_mandir}/man[1-6]/*
%{_includedir}/*
%{_bindir}/pcap-config
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
