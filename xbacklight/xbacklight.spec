#
# spec file for package xbacklight
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.2.3
Release:        0
Summary:        Utility to adjust the screen backlight brightness
License:        MIT
Group:          System/X11/Utilities
Url:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE xcb-util-0_3_6.diff
Patch0:         xcb-util-0_3_6.diff
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
%if 0%{?suse_version} > 1210
BuildRequires:  pkgconfig(xcb-util)
%else
BuildRequires:  xcb-util-0_3_6-devel
%endif
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xrandr) >= 1.2.0
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Xbacklight is used to adjust the backlight brightness where supported.
It uses the RandR extension to find all outputs on the X server
supporting backlight brightness control and changes them all in the
same way.

%prep
%setup -q
%if 0%{?suse_version} < 1220
%patch0 -p0
%endif

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc COPYING README.md
%{_bindir}/xbacklight
%{_mandir}/man1/xbacklight.1%{?ext_man}

%changelog
