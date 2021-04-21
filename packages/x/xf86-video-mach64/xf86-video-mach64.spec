#
# spec file for package xf86-video-mach64
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


Name:           xf86-video-mach64
Version:        6.9.6
Release:        0
Summary:        ATI Mach64 series video driver for the Xorg X server
License:        MIT
Group:          System/X11/Servers/XF86_4
URL:            https://xorg.freedesktop.org/
Source0:        https://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.bz2
BuildRequires:  Mesa-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(libdrm) >= 2.2
BuildRequires:  pkgconfig(pciaccess) >= 0.12.901
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xf86driproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xorg-server) >= 1.2
BuildRequires:  pkgconfig(xproto)
Supplements:    modalias(xorg-x11-server:pci:v00001002d*sv*sd*bc03sc*i*)
# This was part of the xorg-x11-driver-video package up to version 7.6
Conflicts:      xorg-x11-driver-video <= 7.6
ExcludeArch:    s390 s390x
%{x11_abi_videodrv_req}

%description
mach64 is an Xorg driver for ATI Mach64 series video cards.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%files
%license COPYING
%doc ChangeLog README
%dir %{_libdir}/xorg/modules/drivers
%{_libdir}/xorg/modules/drivers/mach64_drv.so

%changelog
