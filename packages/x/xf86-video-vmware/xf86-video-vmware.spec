#
# spec file for package xf86-video-vmware
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


Name:           xf86-video-vmware
Version:        13.4.0
Release:        0
Summary:        VMware SVGA video driver for the Xorg X server
License:        MIT
Group:          System/X11/Servers/XF86_4
URL:            http://xorg.freedesktop.org/
#http://xorg.freedesktop.org/releases/individual/driver/
# Source url disabled, we are using a git checkout via source service
#Source0:        http://xorg.freedesktop.org/releases/individual/driver/%%{name}-%%{version}.tar.bz2
Source0:        %{name}-%{version}.tar.xz
ExclusiveArch:  %ix86 x86_64
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(pciaccess) >= 0.8.0
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(xatracker) >= 0.4.0
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xineramaproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xorg-server) >= 1.0.1
BuildRequires:  pkgconfig(xproto)
Supplements:    modalias(xorg-x11-server:pci:v000015ADd*sv*sd*bc03sc*i*)
# This was part of the xorg-x11-driver-video package up to version 7.6
Conflicts:      xorg-x11-driver-video <= 7.6
%x11_abi_videodrv_req

%description
vmware is an Xorg driver for VMware virtual video cards.

%prep
%autosetup -p1

%build
# We have some -z now related errors during X default startup (boo#1197994):
# this is directly visible on startup, so easy to test later on.
export SUSE_ZNOW=0
NOCONFIGURE=1 autoreconf -fi
%configure
%make_build

%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

%files
%license COPYING
%doc README
%dir %{_libdir}/xorg/modules/drivers
%{_libdir}/xorg/modules/drivers/vmware_drv.so
%{_datadir}/man/man4/vmware.4%{?ext_man}

%changelog
