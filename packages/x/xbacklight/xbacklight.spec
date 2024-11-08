#
# spec file for package xbacklight
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


Name:           xbacklight
Version:        1.2.4
Release:        0
Summary:        Utility to adjust the screen backlight brightness
License:        MIT
Group:          System/X11/Utilities
URL:            https://xorg.freedesktop.org/
Source0:        https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE xcb-util-0_3_6.diff
Patch0:         xcb-util-0_3_6.diff
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xrandr) >= 1.2.0
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
%if 0%{?suse_version} > 1210
BuildRequires:  pkgconfig(xcb-util)
%else
BuildRequires:  xcb-util-0_3_6-devel
%endif

%description
Xbacklight is used to adjust the backlight brightness where supported.
It uses the RandR extension to find all outputs on the X server
supporting backlight brightness control and changes them all in the
same way.

%prep
%setup -q
%if 0%{?suse_version} < 1220
%patch -P 0
%endif

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc README.md
%{_bindir}/xbacklight
%{_mandir}/man1/xbacklight.1%{?ext_man}

%changelog
