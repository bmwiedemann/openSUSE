#
# spec file for package xrefresh
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


Name:           xrefresh
Version:        1.0.6
Release:        0
Summary:        Utility to refresh all or part of an X screen
License:        MIT
Group:          System/X11/Utilities
Url:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1:        xrefresh.desktop
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Xrefresh is a simple X program that causes all or part of your screen
to be repainted. This is useful when system messages have messed up
your screen.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
%suse_update_desktop_file -i -u xrefresh Utility DesktopUtility

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README
%{_bindir}/xrefresh
%{_datadir}/applications/xrefresh.desktop
%{_mandir}/man1/xrefresh.1%{?ext_man}

%changelog
