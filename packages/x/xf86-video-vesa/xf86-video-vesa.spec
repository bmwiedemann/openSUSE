#
# spec file for package xf86-video-vesa
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


%{?x11_abi_has_dpms_get_capabilities: %{x11_abi_has_dpms_get_capabilities}}
Name:           xf86-video-vesa
Version:        2.6.0
Release:        0
Summary:        Generic VESA video driver for the Xorg X server
License:        MIT
Group:          System/X11/Servers/XF86_4
URL:            https://xorg.freedesktop.org/
Source0:        https://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.xz
Source1:        https://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
Patch1:         u_Restore-palette-on-LeaveVT.patch
Patch2:         u_DPMS-Query-DPMS-capabilites-and-query-current-state-before-changing.patch
Patch3:         u_DPMS-Check-for-broken-DPMSGet.patch
Patch4:         u_Refuse-to-run-on-machines-with-simpledrmfb-too.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(pciaccess) >= 0.10
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.3
BuildRequires:  pkgconfig(xorg-server) >= 1.6
BuildRequires:  pkgconfig(xproto)
Supplements:    xorg-x11-server
# This was part of the xorg-x11-driver-video package up to version 7.6
Conflicts:      xorg-x11-driver-video <= 7.6
ExcludeArch:    s390 s390x
%{?x11_abi_videodrv_req}

%description
vesa is an Xorg driver for Generic VESA video cards.

It can drive most VESA-compatible video cards, but only makes use of the
basic standard VESA core that is common to these cards. The driver
supports depths 8, 15 16 and 24.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
# We have some -z now related errors during X default startup (boo#1197994):
# this is directly visible on startup, so easy to test later on.
export SUSE_ZNOW=0
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%files
%license COPYING
%doc ChangeLog README.md
%dir %{_libdir}/xorg/modules/drivers
%{_libdir}/xorg/modules/drivers/vesa_drv.so
%{_mandir}/man4/vesa.4%{?ext_man}

%changelog
