#
# spec file for package xf86-video-savage
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xf86-video-savage
Version:        2.3.9
Release:        0
Summary:        S3 Savage video driver for the Xorg X server
License:        MIT
Group:          System/X11/Servers/XF86_4
Url:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.bz2
# https://lists.x.org/archives/xorg-devel/2018-June/057207.html
Patch0:         u_Add-check-for-max-HV-Value-to-ValidMode-hook.patch
BuildRequires:  Mesa-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(libdrm) >= 2.0
BuildRequires:  pkgconfig(pciaccess) >= 0.10
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xf86driproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xorg-server) >= 1.1.0
BuildRequires:  pkgconfig(xproto)
Supplements:    modalias(xorg-x11-server:pci:v00005333d*sv*sd*bc03sc*i*)
# This was part of the xorg-x11-driver-video package up to version 7.6
Conflicts:      xorg-x11-driver-video <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    s390 s390x
%x11_abi_videodrv_req

%description
savage is an Xorg driver for S3 Savage video cards.

2D, 3D, and Xv acceleration is supported on all chips except the
Savage2000 (2D only). Dualhead operation is supported on MX, IX, and
SuperSavage chips.

%prep
%setup -q
%patch0 -p1

%build
%configure
make %{?_smp_mflags}

%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

%files
%defattr(-,root,root)
%doc ChangeLog README
%license COPYING
%dir %{_libdir}/xorg/modules/drivers
%{_libdir}/xorg/modules/drivers/savage_drv.so
%{_datadir}/man/man4/savage.4%{?ext_man}

%changelog
