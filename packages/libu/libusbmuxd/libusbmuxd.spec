#
# spec file for package libusbmuxd
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


%define major 4

Name:           libusbmuxd
Version:        1.0.10
Release:        0
Summary:        A client library to multiplex connections from and to iOS devices
License:        LGPL-2.1+ and GPL-2.0+
Group:          Development/Libraries/C and C++
Url:            http://cgit.sukimashita.com/libusbmuxd.git
Source:         http://www.libimobiledevice.org/downloads/%{name}-%{version}.tar.bz2
Source99:       baselibs.conf
# PATCH-FIX-UPSTREAM libusbmuxd-CVE-2016-5104.patch CVE-2016-5104 boo#982014 dimstar@opensuse.org - Make sure sockets only listen locally
Patch0:         libusbmuxd-CVE-2016-5104.patch
BuildRequires:  gcc-c++
BuildRequires:  libplist-devel >= 1.11
BuildRequires:  libusb-1_0-devel >= 1.0.3
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
'usbmuxd' stands for "USB multiplexing daemon". This daemon is in charge of
multiplexing connections over USB to an iPhone or iPod touch. To users, it means
you can sync your music, contacts, photos, etc. over USB. To developers, it
means you can connect to any listening localhost socket on the device. usbmuxd
is not used for tethering data transfer, which uses a dedicated USB interface as
a virtual network device.

This package contains the usbmuxd communication interface library 'libusbmuxd'.

%package -n %{name}%{major}
Summary:        A client library to multiplex connections from and to iOS devices
Group:          System/Libraries
Recommends:     usbmuxd

%description -n %{name}%{major}
'usbmuxd' stands for "USB multiplexing daemon". This daemon is in charge of
multiplexing connections over USB to an iPhone or iPod touch. To users, it means
you can sync your music, contacts, photos, etc. over USB. To developers, it
means you can connect to any listening localhost socket on the device. usbmuxd
is not used for tethering data transfer, which uses a dedicated USB interface as
a virtual network device.

This package contains the usbmuxd communication interface library 'libusbmuxd'.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}%{major} = %{version}

%description devel
'usbmuxd' stands for "USB multiplexing daemon". This daemon is in charge of
multiplexing connections over USB to an iPhone or iPod touch. To users, it means
you can sync your music, contacts, photos, etc. over USB. To developers, it
means you can connect to any listening localhost socket on the device. usbmuxd
is not used for tethering data transfer, which uses a dedicated USB interface as
a virtual network device.

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n iproxy
Summary:        An example tool to forward localhost ports to iOS devices
Group:          Productivity/Networking/Other

%description -n iproxy
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
%patch0 -p1

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

rm %{buildroot}%{_libdir}/%{name}.*a

%post -n %{name}%{major} -p /sbin/ldconfig

%postun -n %{name}%{major} -p /sbin/ldconfig

%files -n %{name}%{major}
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_libdir}/libusbmuxd.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/usbmuxd.h
%{_includedir}/usbmuxd-proto.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n iproxy
%defattr(-,root,root)
%{_bindir}/iproxy

%changelog
