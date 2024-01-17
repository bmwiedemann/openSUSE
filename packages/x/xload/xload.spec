#
# spec file for package xload
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


Name:           xload
Version:        1.1.4
Release:        0
Summary:        X utility to display system load average
License:        MIT
Group:          System/X11/Utilities
URL:            https://xorg.freedesktop.org/
Source0:        https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
Source1:        xload.desktop
Source2:        xload.png
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17
BuildRequires:  pkgconfig(xt)
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6

%description
xload displays a periodically updating histogram of the system load
average.

%prep
%setup -q
cp %{SOURCE1} .

%build
%configure
%make_build

%install
%make_install
%suse_update_desktop_file -i -u xload System Monitor
install -m0644 -D %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/xload.png

%files
%license COPYING
%doc ChangeLog README.md
%{_bindir}/xload
%{_datadir}/applications/xload.desktop
%{_datadir}/pixmaps/xload.png
%dir %{_datadir}/X11/app-defaults
%{_datadir}/X11/app-defaults/XLoad
%{_mandir}/man1/xload.1%{?ext_man}

%changelog
