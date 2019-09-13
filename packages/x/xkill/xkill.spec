#
# spec file for package xkill
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xkill
Version:        1.0.5
Release:        0
Summary:        Utility to kill a client by its X resource
License:        X11
Group:          System/X11/Utilities
Url:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1:        xkill.desktop
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmuu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.22
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
xkill is a utility for forcing the X server to close connections to
clients. This program is very dangerous, but is useful for aborting
programs that have displayed undesired windows on a user's screen.

%prep
%setup -q
cp %{SOURCE1} .

%build
%configure
make %{?_smp_mflags}

%install
%make_install
%suse_update_desktop_file -i -u xkill Utility DesktopUtility

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README
%{_bindir}/xkill
%{_datadir}/applications/xkill.desktop
%{_mandir}/man1/xkill.1%{?ext_man}

%changelog
