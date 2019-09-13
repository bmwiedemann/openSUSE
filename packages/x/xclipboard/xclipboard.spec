#
# spec file for package xclipboard
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


Name:           xclipboard
Version:        1.1.3
Release:        0
Summary:        X clipboard client
License:        MIT
Group:          System/X11/Utilities
Url:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1:        xclipboard.desktop
Source2:        xclipboard.png
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17
BuildRequires:  pkgconfig(xt)
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
xclipboard is used to collect and display text selections that are
sent to the CLIPBOARD by other clients.  It is typically used to save
CLIPBOARD selections for later use.  It stores each CLIPBOARD
selection as a separate string, each of which can be selected.

%prep
%setup -q
cp %{SOURCE1} .

%build
%configure
make %{?_smp_mflags}

%install
%make_install
%suse_update_desktop_file -i -u xclipboard Utility DesktopUtility
install -m0644 -D %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/xclipboard.png

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README
%{_bindir}/xclipboard
%{_bindir}/xcutsel
%{_datadir}/applications/xclipboard.desktop
%{_datadir}/pixmaps/xclipboard.png
%dir %{_datadir}/X11/app-defaults
%{_datadir}/X11/app-defaults/XClipboard
%{_mandir}/man1/xclipboard.1%{?ext_man}
%{_mandir}/man1/xcutsel.1%{?ext_man}

%changelog
