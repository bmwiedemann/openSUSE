#
# spec file for package libusbmuxd
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


%define libname libusbmuxd-2_0-6
Name:           libusbmuxd
Version:        2.0.2
Release:        0
Summary:        A client library to multiplex connections from and to iOS devices
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            https://github.com/libimobiledevice/libusbmuxd
Source:         https://github.com/libimobiledevice/libusbmuxd/archive/%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libplist-2.0) >= 2.2.0

%description
'usbmuxd' stands for "USB multiplexing daemon". This daemon is in charge of
multiplexing connections over USB to an iPhone or iPod touch. To users, it means
you can sync your music, contacts, photos, etc. over USB. To developers, it
means you can connect to any listening localhost socket on the device. usbmuxd
is not used for tethering data transfer, which uses a dedicated USB interface as
a virtual network device.

This package contains the usbmuxd communication interface library 'libusbmuxd'.

%package -n %{libname}
Summary:        A client library to multiplex connections from and to iOS devices
Recommends:     usbmuxd
Provides:       libusbmuxd6 = %{version}
Obsoletes:      libusbmuxd6 < %{version}

%description -n %{libname}
'usbmuxd' stands for "USB multiplexing daemon". This daemon is in charge of
multiplexing connections over USB to an iPhone or iPod touch. To users, it means
you can sync your music, contacts, photos, etc. over USB. To developers, it
means you can connect to any listening localhost socket on the device. usbmuxd
is not used for tethering data transfer, which uses a dedicated USB interface as
a virtual network device.

This package contains the usbmuxd communication interface library 'libusbmuxd'.

%package devel
Summary:        Development files for %{name}
Requires:       %{libname} = %{version}

%description devel
'usbmuxd' stands for "USB multiplexing daemon". This daemon is in charge of
multiplexing connections over USB to an iPhone or iPod touch. To users, it means
you can sync your music, contacts, photos, etc. over USB. To developers, it
means you can connect to any listening localhost socket on the device. usbmuxd
is not used for tethering data transfer, which uses a dedicated USB interface as
a virtual network device.

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary:        An example tools to forward localhost ports to iOS devices
Provides:       iproxy = %{version}
Obsoletes:      iproxy < %{version}

%description tools
'usbmuxd' stands for "USB multiplexing daemon". This daemon is in charge of
multiplexing connections over USB to an iPhone or iPod touch. To users, it means
you can sync your music, contacts, photos, etc. over USB. To developers, it
means you can connect to any listening localhost socket on the device. usbmuxd
is not used for tethering data transfer, which uses a dedicated USB interface as
a virtual network device.

Multiple connections to different TCP ports can happen in parallel. An example
(and useful) tool called 'iproxy' is included that allows you to forward
localhost ports to the device---allows SSH over USB on jailbroken devices, or
allowing access the lockdown daemon (and then to all of the file access, sync,
notification and backup services running on the device).

%prep
%setup -q

%build
autoreconf -fvi
export CFLAGS="%{optflags} -fexceptions"
%configure \
  --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING
%doc AUTHORS README.md
%{_libdir}/libusbmuxd-2.0.so.*

%files devel
%{_includedir}/usbmuxd.h
%{_includedir}/usbmuxd-proto.h
%{_libdir}/libusbmuxd-2.0.so
%{_libdir}/pkgconfig/%{name}-2.0.pc

%files tools
%{_bindir}/iproxy
%{_bindir}/inetcat
%{_mandir}/man1/inetcat.1%{?ext_man}
%{_mandir}/man1/iproxy.1%{?ext_man}

%changelog
