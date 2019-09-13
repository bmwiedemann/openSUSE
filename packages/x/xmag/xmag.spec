#
# spec file for package xmag
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xmag
Version:        1.0.6
Release:        0
Summary:        Screen magnifier
License:        X11
Group:          System/X11/Utilities
Url:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1:        xmag.desktop
Source2:        xmag.png
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xt)
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
xmag displays a magnified snapshot of a portion of an X11 screen.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
%suse_update_desktop_file -i -u xmag Utility Accessibility DesktopUtility
install -m0644 -D %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/xmag.png

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README
%{_bindir}/xmag
%{_datadir}/applications/xmag.desktop
%{_datadir}/pixmaps/xmag.png
%dir %{_datadir}/X11/app-defaults
%{_datadir}/X11/app-defaults/Xmag
%{_mandir}/man1/xmag.1%{?ext_man}

%changelog
