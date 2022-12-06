#
# spec file for package xorgxrdp
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


Name:           xorgxrdp
Version:        0.9.19
Release:        0
Summary:        Xorg drivers for xrdp
License:        X11
Group:          System/X11/Utilities
URL:            https://github.com/neutrinolabs/xorgxrdp
Source0:        https://github.com/neutrinolabs/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/neutrinolabs/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  nasm
BuildRequires:  pkgconfig
BuildRequires:  xorg-x11-server-sdk
BuildRequires:  xrdp-devel
BuildRequires:  pkgconfig(xorg-macros)
Requires:       xrdp >= 0.9.1
ExcludeArch:    s390 s390x
%{x11_abi_videodrv_req}
%{x11_abi_xinput_req}
# For Leap 42.x and SLE 12.x <= 12.3, keep to use libXfont-devel
%if 0%{?suse_version} > 1320 || 0%{?sle_version}  > 120300
BuildRequires:  libXfont2-devel
%else
BuildRequires:  libXfont-devel
%endif

%description
This package contains Xorg driver modules for xrdp

%prep
%setup -q

%build
sh ./bootstrap
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%files
%license COPYING
%doc README.md
%{_libdir}/xorg/modules/drivers/xrdpdev_drv.so
%dir %{_libdir}/xorg/modules/input
%{_libdir}/xorg/modules/input/xrdpkeyb_drv.so
%{_libdir}/xorg/modules/input/xrdpmouse_drv.so
%{_libdir}/xorg/modules/libxorgxrdp.so
%dir %{_sysconfdir}/X11/xrdp
%config %{_sysconfdir}/X11/xrdp/xorg.conf

%changelog
