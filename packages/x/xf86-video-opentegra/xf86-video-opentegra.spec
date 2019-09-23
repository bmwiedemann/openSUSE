#
# spec file for package xf86-video-opentegra
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           xf86-video-opentegra
Summary:        X.Org X server -- opentegra display driver
License:        MIT
Group:          System/X11/Servers/XF86_4
Version:        0.7.0
Release:        0.0
ExclusiveArch:  %arm
Url:            http://cgit.freedesktop.org/xorg/driver/xf86-video-opentegra/
Source0:        http://xorg.freedesktop.org/releases/individual/driver/%{name}-%{version}.tar.xz
Requires:       xorg-x11-server
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libdrm-devel
BuildRequires:  libdrm2
BuildRequires:  libtool
BuildRequires:  libudev-devel
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xorg-server)
BuildRequires:  pkgconfig(xproto)

%x11_abi_videodrv_req

%description
Open-source X.org graphics driver for Nvidia Tegra graphics

%prep
%setup -q

%build
export CFLAGS="%{optflags}"

%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

%files
%defattr(-,root,root,-)
%doc COPYING
%dir %{_libdir}/xorg/modules/drivers
%{_libdir}/xorg/modules/drivers/*.so
/usr/share/X11/xorg.conf.d/opentegra.conf
%doc %{_mandir}/man4/opentegra.4.gz

%changelog
