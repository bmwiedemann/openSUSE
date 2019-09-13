#
# spec file for package xf86-video-fbturbo-live
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


Name:           xf86-video-fbturbo-live
Version:        0.4.git.1444169281.f9a6ed7
Release:        0
Summary:        Xorg DDX driver for ARM devices (Allwinner, RPi and others)
License:        X11 AND GPL-2.0-or-later
Group:          System/X11/Servers/XF86_4
Url:            https://github.com/ssvb/xf86-video-fbturbo
# https://github.com/ssvb/%{name}/archive/%{version}.tar.gz
Source0:        xf86-video-fbturbo-%{version}.tar.xz
Patch0:         n_xorg-server-1.20.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(pciaccess) >= 0.8.0
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xorg-server) >= 1.0.99.901
BuildRequires:  pkgconfig(xproto)
Conflicts:      xf86-video-fbturbo
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
%setup -q -n xf86-video-fbturbo-%{version}
%patch0 -p1

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
install xorg.conf -m 0644 -D %{buildroot}%{_datadir}/X11/xorg.conf.d/99-fbturbo.conf

%files
%defattr(-,root,root)
%doc COPYING README
%dir %{_libdir}/xorg/modules/drivers
%{_libdir}/xorg/modules/drivers/fbturbo_drv.so
%{_mandir}/man4/fbturbo.4%{?ext_man}
%dir %{_datadir}/X11/xorg.conf.d
%{_datadir}/X11/xorg.conf.d/99-fbturbo.conf

%changelog
