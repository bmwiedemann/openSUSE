#
# spec file for package xf86-video-nouveau
#
# Copyright (c) 2024 SUSE LLC
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
Version:        1.0.17
Release:        0
Summary:        Accelerated Open Source driver for nVidia cards
License:        MIT
Group:          System/X11/Servers/XF86_4
URL:            https://nouveau.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.bz2
Patch0:         N_xf86-video-nouveau_nva3-noaccel-info.patch
Patch1:         U_nouveau-fixup-driver-for-new-X-server-ABI.patch
BuildRequires:  libtool
BuildRequires:  pciutils-devel
BuildRequires:  pkgconfig
BuildRequires:  xorg-x11-sdk
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libdrm) >= 2.4.25
BuildRequires:  pkgconfig(libdrm_nouveau) >= 2.4.25
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(xorg-macros)
Requires:       xorg-x11-server
Provides:       xorg-x11-driver-video-nouveau = %{version}
Obsoletes:      xorg-x11-driver-video-nouveau < %{version}
ExclusiveArch:  %{ix86} x86_64 ppc ppc64 ppc64le %{arm} aarch64
%{x11_abi_videodrv_req}

%description
The nouveau project aims to build high-quality, open source drivers for nVidia
cards. “Nouveau” [nuvo] is the French word for “new”.

%prep
%setup -q
%patch -P 0 -p1 -F 1 -b .nva3info
%patch -P 1 -p1

%build
# We have some -z now related errors during X default startup (boo#1197994):
# this is directly visible on startup, so easy to test later on.
export SUSE_ZNOW=0
# Workaround for boo#1225956
export CFLAGS="%optflags -fpermissive"
autoreconf -fi
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%files
%dir %{_libdir}/xorg/modules/drivers
%{_libdir}/xorg/modules/drivers/*_drv.so
%{_mandir}/man4/*

%changelog
