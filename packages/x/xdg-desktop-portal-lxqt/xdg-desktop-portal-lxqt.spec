#
# spec file for package xdg-desktop-portal-lxqt
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           xdg-desktop-portal-lxqt
Version:        1.3.0
Release:        0
Summary:        A backend implementation for xdg-desktop-portal
License:        LGPL-2.1-or-later
URL:            https://github.com/lxqt/xdg-desktop-portal-lxqt
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.5.0
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(fm-qt6)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libmenu-cache)
Requires:       xdg-desktop-portal
Supplements:    (xdg-desktop-portal and lxqt-session)

%description
A backend implementation for xdg-desktop-portal that is using Qt/KF5/libfm-qt.
functionality needed by nearly all of its components.

%prep
%autosetup -p1

%build
%cmake_qt6
%{qt6_build}

%install
%{qt6_install}

%pre
%systemd_user_pre %{name}.service

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%files
%doc README.md
%{_libexecdir}/%{name}
%dir %{_datadir}/xdg-desktop-portal
%{_datadir}/xdg-desktop-portal/lxqt-portals.conf
%dir %{_datadir}/xdg-desktop-portal/portals
%{_datadir}/xdg-desktop-portal/portals/lxqt.portal
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.lxqt.service
%{_datadir}/applications/org.freedesktop.impl.portal.desktop.lxqt.desktop
%{_userunitdir}/%{name}.service
%license LICENSE

%changelog
