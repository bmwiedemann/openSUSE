#
# spec file for package usbip
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


%define version %(rpm -q --qf '%%{VERSION}' kernel-source)
Name:           usbip
Version:        %{version}
Release:        0
Summary:        The USB/IP shared USB system over IP network
License:        GPL-2.0-or-later
Group:          Hardware/Other
URL:            https://usbip.sourceforge.net/
BuildRequires:  kernel-source >= 3.17
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  tcpd-devel
BuildRequires:  pkgconfig(libudev)

%description
USB/IP protocol allows to pass USB device from server to client over the
network. Server is a machine which provides (shares) a USB device. Client is
a machine which uses USB device provided by server over the network.
The USB device may be either physical device connected to a server or
software entity created on a server using USB gadget subsystem.

%package devel
Summary:        The USB/IP shared USB system over IP network
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
This package contains headers and static libraries for USB/IP
development

%package rebuild
Summary:        Empty package to ensure rebuilding usbip in OBS
%requires_eq    kernel-source

%description rebuild
This is an empty package that ensures usbip is rebuilt every time
kernel-default is rebuilt in OBS.

There is no reason to install this package.

%prep
# create an empty work folder
%setup -c -T
# copy the sources from the kernel sources
cp -a %{_prefix}/src/linux/tools/usb/usbip/* .

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%build
./autogen.sh
%configure \
    --disable-static \
    --with-tcp-wrappers
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%files devel
%dir %{_includedir}/usbip
%{_includedir}/usbip/*.h
%{_libdir}/libusbip.so

%files
%license COPYING
%doc AUTHORS README
%{_sbindir}/usbip
%{_sbindir}/usbipd
%{_libdir}/libusbip.so.0*
%{_mandir}/man8/usbip*.8%{?ext_man}

%files rebuild
%license COPYING

%changelog
