#
# spec file for package xf86-video-fbturbo
#
# Copyright (c) 2021 SUSE LLC
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


Name:           xf86-video-fbturbo
Version:        0.4.0
Release:        0
Summary:        Xorg DDX driver for ARM devices (Allwinner, RPi and others)
License:        X11 AND GPL-2.0-or-later
Group:          System/X11/Servers/XF86_4
URL:            https://github.com/ssvb/xf86-video-fbturbo
# https://github.com/ssvb/%{name}/archive/%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz
Source1:        99-fbturbo.conf
Patch0:         n_xorg-server-1.20.patch
Patch1:         n_xorg-server-21.1.patch
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(pciaccess) >= 0.8.0
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xorg-server) >= 1.0.99.901
BuildRequires:  pkgconfig(xproto)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    s390 s390x
%{x11_abi_videodrv_req}

%description
Video driver, primarily optimized for the devices powered by the Allwinner SoC
(A10, A13, A20). It can use some of the 2D/3D hardware acceleration features.

And because this driver is based on xf86-video-fbdev (with none of the original
features stripped), it actually supports all the same hardware as
xf86-video-fbdev. Essentially, xf86-video-fbturbo can be just used as a drop-in
replacement and run on practically any Linux system. There will be no real
difference on x86, but any ARM based system should see better performance
thanks to some additional optimizations (the elimination of ShadowFB layer, ARM
NEON/VFP code for dealing with uncached framebuffer reads, automatic backing
store management for faster window moves).

%prep
%autosetup -p1

%build
%configure
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
install %{S:1} -m 0644 -D %{buildroot}%{_datadir}/X11/xorg.conf.d/99-fbturbo.conf

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README
%dir %{_libdir}/xorg/modules/drivers
%{_libdir}/xorg/modules/drivers/fbturbo_drv.so
%{_mandir}/man4/fbturbo.4%{?ext_man}
%dir %{_datadir}/X11/xorg.conf.d
%{_datadir}/X11/xorg.conf.d/99-fbturbo.conf

%changelog
