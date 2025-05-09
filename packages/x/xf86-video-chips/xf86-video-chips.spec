#
# spec file for package xf86-video-chips
#
# Copyright (c) 2024 SUSE LLC
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


Name:           xf86-video-chips
Version:        1.5.0
Release:        0
Summary:        Chips and Technologies video driver for the Xorg X server
License:        MIT
Group:          System/X11/Servers/XF86_4
URL:            http://xorg.freedesktop.org/
#Source0:        http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.bz2
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(pciaccess) >= 0.8.0
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xorg-server) >= 1.0.99.901
BuildRequires:  pkgconfig(xproto)
Supplements:    modalias(xorg-x11-server:pci:v0000102Cd*sv*sd*bc03sc*i*)
# This was part of the xorg-x11-driver-video package up to version 7.6
Conflicts:      xorg-x11-driver-video <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    aarch64 %{arm} s390 s390x
%x11_abi_videodrv_req

%description
chips is an Xorg driver for Chips and Technologies video cards.

The majority of the Chips and Technologies chipsets are supported by
this driver. In general the limitation on the capabilities of this
driver are determined by the chipset on which it is run. Where possible,
this driver provides full acceleration and supports the following
depths: 1, 4, 8, 15, 16, 24 and on the latest chipsets an 8+16 overlay
mode. All visual types are supported for depth 1, 4 and 8 and both
TrueColor and DirectColor visuals are supported where possible.
Multi-head configurations are supported on PCI or AGP buses.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README
%dir %{_libdir}/xorg/modules/drivers
%{_libdir}/xorg/modules/drivers/chips_drv.so
%{_mandir}/man4/chips.4%{?ext_man}

%changelog
