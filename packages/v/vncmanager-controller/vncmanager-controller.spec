#
# spec file for package vncmanager-controller
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


Name:           vncmanager-controller
Version:        1.0.2
Release:        0
Summary:        Configuration application for VNC session
License:        MIT
Group:          System/X11/Utilities
URL:            https://github.com/openSUSE/vncmanager-controller
Source:         %{name}-%{version}.tar
Patch1:         n_UsrEtc.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libQt5Core-devel
BuildRequires:  libQt5Network-devel
BuildRequires:  libQt5Widgets-devel
BuildRequires:  libXvnc-devel
BuildRequires:  libqt5-qtx11extras-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xproto)

Requires:       vncmanager

%description
This is configuration application to configure sharing and security from inside VNC session.

%package gnome
Requires:       gnome-shell
Requires:       vncmanager-controller
Supplements:    (%{name}:gnome-shell)
Summary:        Configuration application for VNC session
Group:          System/GUI/GNOME
BuildArch:      noarch

%description gnome
This is configuration application to configure sharing and security from inside VNC session.

%prep
%setup
%if 0%{?suse_version} >= 1550
%patch1 -p1
%endif

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_VERBOSE_MAKEFILE=ON
%make_jobs

%install
%cmake_install

%files
%defattr(-,root,root)
%{_bindir}/vncmanager-controller
%if 0%{?suse_version} >= 1550
%dir %{_distconfdir}/xdg
%dir %{_distconfdir}/xdg/autostart
%{_distconfdir}/xdg/autostart/vncmanager-controller.desktop
%else
%dir %{_sysconfdir}/xdg/autostart
%{_sysconfdir}/xdg/autostart/vncmanager-controller.desktop
%endif
%doc LICENSE

%files gnome
%defattr(-,root,root)
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/extensions
%{_datadir}/gnome-shell/extensions/*

%changelog
