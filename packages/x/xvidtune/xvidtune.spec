#
# spec file for package xvidtune
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


Name:           xvidtune
Version:        1.0.4
Release:        0
Summary:        Video mode tuner for the X server
License:        MIT
Group:          System/X11/Utilities
URL:            https://xorg.freedesktop.org
Source0:        %{url}/releases/individual/app/%{name}-%{version}.tar.xz

BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.4
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xxf86vm)
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6

%description
xvidtune is a client interface to the X server video mode
extension (XFree86-VidModeExtension).

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc ChangeLog README.md
%{_bindir}/xvidtune
%dir %{_datadir}/X11/app-defaults
%{_datadir}/X11/app-defaults/Xvidtune
%{_mandir}/man1/xvidtune.1%{?ext_man}

%changelog
