#
# spec file for package xrefresh
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


Name:           xrefresh
Version:        1.0.7
Release:        0
Summary:        Utility to refresh all or part of an X screen
License:        MIT
Group:          System/X11/Utilities
URL:            https://xorg.freedesktop.org/
Source0:        https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
Source1:        https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz.sig
Source2:        xrefresh.keyring
Source3:        xrefresh.desktop
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6

%description
Xrefresh is a simple X program that causes all or part of your screen
to be repainted. This is useful when system messages have messed up
your screen.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install
%suse_update_desktop_file -i -u xrefresh Utility DesktopUtility

%files
%license COPYING
%doc ChangeLog README.md
%{_bindir}/xrefresh
%{_datadir}/applications/xrefresh.desktop
%{_mandir}/man1/xrefresh.1%{?ext_man}

%changelog
