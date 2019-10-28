#
# spec file for package xf86-video-cirrus
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           xf86-video-cirrus
Version:        1.5.3
Release:        0
Summary:        Cirrus Logic video driver for the Xorg X server
License:        MIT
Group:          System/X11/Servers/XF86_4
Url:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM cirrus-1.2.0-qemu.patch fcrozat@suse.com -- Avoid 10x7 heuristic, handled by server (Fedora)
Patch0:         u_cirrus-qemu.patch
# PATCH-FIX-UPSTREAM cirrus-1.3.2-virt-16bpp.patch fcrozat@suse.com -- Use 16bpp when running in virt (Fedora)
Patch1:         u_cirrus-virt-16bpp.patch

BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(pciaccess) >= 0.8.0
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.2
BuildRequires:  pkgconfig(xorg-server) >= 1.4
BuildRequires:  pkgconfig(xproto)
# This was part of the xorg-x11-driver-video package up to version 7.6
Conflicts:      xorg-x11-driver-video <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    s390 s390x
Supplements:    modalias(xorg-x11-server:pci:v00001013d*sv*sd*bc03sc*i*)
%x11_abi_videodrv_req

%description
cirrus is an Xorg driver for Cirrus Logic video cards.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
%{_libdir}/xorg/modules/drivers/cirrus_alpine.so
%{_libdir}/xorg/modules/drivers/cirrus_laguna.so
%{_libdir}/xorg/modules/drivers/cirrus_drv.so
%{_datadir}/man/man4/cirrus.4%{?ext_man}

%changelog
