#
# spec file for package xf86-input-libinput
#
# Copyright (c) 2023 SUSE LLC
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


Name:           xf86-input-libinput
Version:        1.3.0
Release:        0
Summary:        Libinput driver for the Xorg X server
License:        MIT
Group:          System/X11/Servers/XF86_4
URL:            https://xorg.freedesktop.org
Source0:        %{url}/releases/individual/driver/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/individual/driver/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
Patch0:         n_enable-tapping.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(inputproto) >= 2.2
BuildRequires:  pkgconfig(libinput) >= 1.11.0
BuildRequires:  pkgconfig(xorg-macros) >= 1.13
BuildRequires:  pkgconfig(xorg-server) >= 1.10
BuildRequires:  pkgconfig(xproto)
Supplements:    xorg-x11-server
# This was part of the xorg-x11-driver-input package up to version 7.6
Conflicts:      xorg-x11-driver-input <= 7.6
%{x11_abi_xinput_req}

%description
xf86-input-libinput is a libinput-based X.Org driver. The actual driver bit
is quite limited, most of the work is done by libinput, the driver itself
passes on the events (and wrangles them a bit where needed).

%package devel
Summary:        Libinput driver for the Xorg X server -- Development Files
Group:          Development/Libraries/X11
Requires:       %{name} = %{version}

%description devel
xf86-input-libinput is a libinput-based X.Org driver. The actual driver bit
is quite limited, most of the work is done by libinput, the driver itself
passes on the events (and wrangles them a bit where needed).

%prep
%autosetup -p1

%build
%configure --with-xorg-conf-dir="%{_datadir}/X11/xorg.conf.d/"
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%files
%license COPYING*
%dir %{_libdir}/xorg/modules/input
%{_datadir}/X11/xorg.conf.d/40-libinput.conf
%dir %{_datadir}/X11/xorg.conf.d
%{_libdir}/xorg/modules/input/libinput_drv.so
%{_mandir}/man4/libinput.4%{?ext_man}

%files devel
%{_includedir}/xorg/libinput-properties.h
%{_libdir}/pkgconfig/xorg-libinput.pc

%changelog
