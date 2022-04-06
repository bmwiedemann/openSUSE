#
# spec file for package xf86-video-dummy
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


Name:           xf86-video-dummy
Version:        0.4.0
Release:        0
Summary:        Virtual/offscreen frame buffer video driver for the Xorg X server
License:        MIT
Group:          System/X11/Servers/XF86_4
URL:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.xz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(xf86dgaproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.3
BuildRequires:  pkgconfig(xorg-server) >= 1.0.99.901
BuildRequires:  pkgconfig(xproto)
# This was part of the xorg-x11-driver-video package up to version 7.6
Conflicts:      xorg-x11-driver-video <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    s390 s390x
%x11_abi_videodrv_req

%description
dummy is an Xorg driver for virtual/offscreen frame buffer.

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
%doc ChangeLog COPYING README.md
%dir %{_libdir}/xorg/modules/drivers
%{_libdir}/xorg/modules/drivers/dummy_drv.so

%changelog
