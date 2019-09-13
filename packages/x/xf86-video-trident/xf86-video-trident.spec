#
# spec file for package xf86-video-trident
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


Name:           xf86-video-trident
Version:        1.3.8
Release:        0
Summary:        Trident video driver for the Xorg X server
License:        MIT
Group:          System/X11/Servers/XF86_4
Url:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.bz2
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(pciaccess) >= 0.8.0
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xf86dgaproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xorg-server) >= 1.0.99.901
BuildRequires:  pkgconfig(xproto)
# This was part of the xorg-x11-driver-video package up to version 7.6
Conflicts:      xorg-x11-driver-video <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    s390 s390x
Supplements:    modalias(xorg-x11-server:pci:v00001023d00009930sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00001023d00009910sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00001023d00008820sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00001023d0000939Asv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00001023d00009397sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00001023d00009525sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00001023d00009520sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00001023d00009388sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00001023d00009320sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00001023d00009850sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00001023d00009750sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00001023d00009660sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00001023d00009440sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00001023d00009540sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00001023d00008620sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00001023d00008600sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00001023d00008520sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00001023d00008500sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00001023d00008420sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00001023d00008400sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00001023d00009880sv*sd*bc*sc*i*)

%x11_abi_videodrv_req

%description
trident is an Xorg driver for Trident video cards.

The driver is accelerated, and provides support for the following
framebuffer depths: 1, 4, 8, 15, 16, and 24. Multi-head configurations
are supported. The XvImage extension is supported on TGUI96xx and
greater cards.

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
%{_libdir}/xorg/modules/drivers/trident_drv.so
%{_datadir}/man/man4/trident.4%{?ext_man}

%changelog
