#
# spec file for package xf86-video-omap
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           xf86-video-omap
Summary:        X.Org X server -- Omapdrm display driver
License:        MIT
Group:          System/X11/Servers/XF86_4
Version:        0.4.3
Release:        0.0
ExclusiveArch:  armv7l armv7hl
Url:            https://github.com/robclark/xf86-video-omap
Source0:        xf86-video-omap-%{version}.tar.bz2
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
BuildRequires:  pkgconfig(xorg-server)
BuildRequires:  pkgconfig(xproto)

%description
Open-source X.org graphics driver for TI OMAP graphics

Currently relies on a closed-source submodule for EXA acceleration on
the following chipsets:
  + OMAP3430
  + OMAP3630
  + OMAP4430
  + OMAP4460
  + OMAP5430
  + OMAP5432


%prep
%setup -q

%build
export CFLAGS="%{optflags} -mfpu=neon"
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root,-)
%dir %{_libdir}/xorg/modules/drivers
%{_libdir}/xorg/modules/drivers/*.so
%{_libdir}/xorg/modules/drivers/*.la
%doc /usr/share/man/man4/omap.4.gz

%changelog
