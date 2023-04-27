#
# spec file for package xf86-video-ati
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


%define xserver_glamor 1
Name:           xf86-video-ati
Version:        22.0.0
Release:        0
Summary:        ATI video driver for the Xorg X server
License:        MIT
Group:          System/X11/Servers/XF86_4
URL:            https://xorg.freedesktop.org/
Source0:        https://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.xz
Source1:        https://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
BuildRequires:  autoconf >= 2.60
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(damageproto)
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(gbm)
# Libdrm 2.4.36 needed for kms
BuildRequires:  pkgconfig(libdrm) >= 2.4.58
BuildRequires:  pkgconfig(libdrm_radeon) >= 2.4.58
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pciaccess) >= 0.8.0
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xf86driproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xorg-server) >= 1.15
BuildRequires:  pkgconfig(xproto)
# This was part of the xorg-x11-driver-video package up to version 7.6
Conflicts:      xorg-x11-driver-video <= 7.6
ExcludeArch:    s390 s390x
%{x11_abi_videodrv_req}
# Glamor is new and we want that now
%if !%{xserver_glamor}
BuildRequires:  pkgconfig(glamor) >= 0.3.1
%endif

%description
ati is an Xorg driver for ATI/AMD video cards.

It autodetects whether your hardware has a Radeon, Rage 128, or Mach64
or earlier class of chipset, and loads the radeon, r128, or mach64
driver as appropriate.

%prep
%autosetup -p1

%build
# We have some -z now related errors during X default startup (boo#1197994):
# this is directly visible on startup, so easy to test later on.
export SUSE_ZNOW=0
autoreconf -fiv
%configure \
  --enable-glamor
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%files
%license COPYING
%doc README.md
%dir %{_libdir}/xorg/modules/drivers
%{_datadir}/X11/xorg.conf.d/10-radeon.conf
%{_libdir}/xorg/modules/drivers/ati_drv.so
%{_libdir}/xorg/modules/drivers/radeon_drv.so
%{_mandir}/man4/ati.4%{?ext_man}
%{_mandir}/man4/radeon.4%{?ext_man}

%changelog
