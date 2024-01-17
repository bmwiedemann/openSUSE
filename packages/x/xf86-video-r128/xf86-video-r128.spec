#
# spec file for package xf86-video-r128
#
# Copyright (c) 2022 SUSE LLC
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


Name:           xf86-video-r128
Version:        6.12.1
Release:        0
Summary:        ATI Rage 128 video driver for the Xorg X server
License:        MIT
Group:          System/X11/Servers/XF86_4
URL:            https://xorg.freedesktop.org/
Source0:        https://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.xz
# https://lists.x.org/archives/xorg-devel/2018-June/057208.html
BuildRequires:  Mesa-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(libdrm) >= 2.2
BuildRequires:  pkgconfig(pciaccess) >= 0.8.0
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xf86driproto)
BuildRequires:  pkgconfig(xineramaproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.2
BuildRequires:  pkgconfig(xorg-server) >= 1.2
BuildRequires:  pkgconfig(xproto)
Supplements:    modalias(xorg-x11-server:pci:v00001002d*sv*sd*bc03sc*i*)
# This was part of the xorg-x11-driver-video package up to version 7.6
Conflicts:      xorg-x11-driver-video <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    s390 s390x
%x11_abi_videodrv_req

%description
r128 is an Xorg driver for ATI Rage 128 video cards.

It contains full support for 8, 15, 16 and 24 bit pixel depths, hardware
acceleration of drawing primitives, hardware cursor, video modes up to
1800x1440 @ 70Hz, doublescan modes (e.g., 320x200 and 320x240), gamma
correction at all pixel depths, a fully programming dot clock and robust
text mode restoration for VT switching. Dualhead is supported on M3/M4
mobile chips.

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
%doc ChangeLog README
%license COPYING
%dir %{_libdir}/xorg/modules/drivers
%{_libdir}/xorg/modules/drivers/r128_drv.so
%{_datadir}/man/man4/r128.4%{?ext_man}

%changelog
