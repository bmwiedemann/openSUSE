#
# spec file for package xf86-video-nv
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


Name:           xf86-video-nv
Version:        2.1.21
Release:        0
Summary:        NVIDIA video driver for the Xorg X server
License:        MIT
Group:          System/X11/Servers/XF86_4
Url:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.bz2
Patch0:         xf86-video-nv-bug519261-increase-virtual.diff
BuildRequires:  autoconf >= 2.60
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(pciaccess) >= 0.10.7
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xorg-server) >= 1.3
BuildRequires:  pkgconfig(xproto)
# better not install it by default (bnc#868732)
#Supplements:    modalias(xorg-x11-server:pci:v000010DEd*sv*sd*bc03sc*i*)
#Supplements:    modalias(xorg-x11-server:pci:v000012D2d*sv*sd*bc03sc*i*)
# This was part of the xorg-x11-driver-video package up to version 7.6
Conflicts:      xorg-x11-driver-video <= 7.6
Provides:       xorg-x11-driver-video-nvidia = %{version}
Obsoletes:      xorg-x11-driver-video-nvidia < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    s390 s390x
%x11_abi_videodrv_req

%description
nv is an Xorg driver for NVIDIA video cards.

The driver supports 2D acceleration and provides support for the
following framebuffer depths: 8, 15, 16 (except Riva128) and 24. All
visual types are supported for depth 8, TrueColor and DirectColor
visuals are supported for the other depths with the exception of the
Riva128 which only supports TrueColor in the higher depths.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

%files
%defattr(-,root,root)
%doc COPYING README
%dir %{_libdir}/xorg/modules/drivers
%{_libdir}/xorg/modules/drivers/nv_drv.so
%{_datadir}/man/man4/nv.4%{?ext_man}

%changelog
