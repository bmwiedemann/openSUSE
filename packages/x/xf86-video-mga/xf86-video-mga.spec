#
# spec file for package xf86-video-mga
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xf86-video-mga
Version:        2.0.0
Release:        0
Summary:        Matrox video driver for the Xorg X server
License:        MIT
Group:          System/X11/Servers/XF86_4
Url:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.bz2
Patch0:         u_Change-shadow-fb-implementation-from-DDX-based-to-miext-damage-based.patch
Patch1:         u_Fix-compiler-warnings.patch
Patch4:         u_shadow-Calulate-the-shadow-buffer-size-correctly.patch
Patch5:         n_xorg-server-1.20.patch
BuildRequires:  Mesa-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(libdrm) >= 2.0
BuildRequires:  pkgconfig(pciaccess) >= 0.8.0
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xf86driproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xorg-server) >= 1.1.0
BuildRequires:  pkgconfig(xproto)
Supplements:    modalias(xorg-x11-server:pci:v0000102Bd*sv*sd*bc03sc*i*)
# This was part of the xorg-x11-driver-video package up to version 7.6
Conflicts:      xorg-x11-driver-video <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    s390 s390x
%x11_abi_videodrv_req

%description
mga is an Xorg driver for Matrox video cards.

The driver is fully accelerated, and provides support for the following
framebuffer depths: 8, 15, 16, 24, and an 8+24 overlay mode. All visual
types are supported for depth 8, and both TrueColor and DirectColor
visuals are supported for the other depths except 8+24 mode which
supports PseudoColor, GrayScale and TrueColor. Multi-card configurations
are supported. XVideo is supported on G200 and newer systems, with
either TexturedVideo or video overlay. The second head of dual-head
cards is supported for the G450 and G550. Support for the second head on
G400 cards requires a binary-only "mga_hal" module that is available
from Matrox, and may be on the CD supplied with the card. That module
also provides various other enhancements, and may be necessary to use
the DVI (digital) output on the G550 (and other cards).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch4 -p1
%patch5 -p1

%build
%configure
make %{?_smp_mflags}

%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README.md
%dir %{_libdir}/xorg/modules/drivers
%{_libdir}/xorg/modules/drivers/mga_drv.so
%{_datadir}/man/man4/mga.4%{?ext_man}

%changelog
