#
# spec file for package xf86-video-nouveau
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           xf86-video-nouveau
BuildRequires:  libtool
BuildRequires:  pciutils-devel
BuildRequires:  xorg-x11-sdk
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libdrm) >= 2.4.25
BuildRequires:  pkgconfig(libdrm_nouveau) >= 2.4.25
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(xorg-macros)
Url:            http://nouveau.freedesktop.org/wiki/
Version:        1.0.16
Release:        0
Summary:        Accelerated Open Source driver for nVidia cards
License:        MIT
Group:          System/X11/Servers/XF86_4
Requires:       xorg-x11-server
Provides:       xorg-x11-driver-video-nouveau  = %{version}
Obsoletes:      xorg-x11-driver-video-nouveau  < %{version}
ExclusiveArch:  %ix86 x86_64 ppc ppc64 ppc64le %arm aarch64
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.bz2
Patch0:         N_xf86-video-nouveau_nva3-noaccel-info.patch
Supplements:    modalias(xorg-x11-server:pci:v000012D2d*sv*sd*bc03sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v000010DEd*sv*sd*bc03sc*i*)

%x11_abi_videodrv_req

%description
The nouveau project aims to build high-quality, open source drivers for nVidia
cards. “Nouveau” [nuvo] is the French word for “new”.

%prep
%setup -q
%patch0 -p1 -F 1 -b .nva3info

%build
autoreconf -fi
%configure CFLAGS="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

%files
%defattr(-,root,root)
%dir %{_libdir}/xorg/modules/drivers
%{_libdir}/xorg/modules/drivers/*_drv.so
%{_mandir}/man4/*

%changelog
