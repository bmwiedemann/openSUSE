#
# spec file for package usbutils
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


Name:           usbutils
Version:        012
Release:        0
Summary:        Tools and libraries for USB devices
License:        GPL-2.0-or-later
Group:          Hardware/Other
URL:            https://sourceforge.net/projects/linux-usb/
Source0:        https://www.kernel.org/pub/linux/utils/usb/%{name}/%{name}-%{version}.tar.xz
Source1:        usbutils-rpmlintrc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  libusb-1_0-devel >= 1.0.14
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libudev) >= 196
Requires:       hwdata

%description
This package contains a utility for inspecting devices connected to USB
ports.

%prep
%setup -q

%build
autoreconf -fiv
%configure \
  --datadir=%{_datadir}/hwdata \
  --disable-usbids
%make_build

%install
%make_install

%files
%doc NEWS
%license LICENSES/*
%{_bindir}/lsusb
%{_bindir}/lsusb.py
%{_bindir}/usb-devices
%{_bindir}/usbhid-dump
%{_mandir}/man1/usb-devices.1%{?ext_man}
%{_mandir}/man8/lsusb.8%{?ext_man}
%{_mandir}/man8/usbhid-dump.8%{?ext_man}

%changelog
