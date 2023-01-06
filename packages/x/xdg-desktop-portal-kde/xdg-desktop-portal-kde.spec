#
# spec file for package xdg-desktop-portal-kde
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


%bcond_without released
%bcond_without screencast

# Internal QML import
%global __requires_exclude qmlimport\\(org\\.kde\\.xdgdesktopportal

%define kf5_version 5.98.0
Name:           xdg-desktop-portal-kde
Version:        5.26.5
Release:        0
Summary:        QT/KF5 backend for xdg-desktop-portal
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            http://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/xdg-desktop-portal-kde-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/xdg-desktop-portal-kde-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  libQt5PrintSupport-private-headers-devel
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5Declarative) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5IconThemes) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5Kirigami2) >= %{kf5_version}
BuildRequires:  cmake(KF5Notifications) >= %{kf5_version}
BuildRequires:  cmake(KF5Plasma) >= %{kf5_version}
BuildRequires:  cmake(KF5Wayland) >= %{kf5_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{kf5_version}
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core) >= 5.11.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5WaylandClient)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(wayland-client) >= 1.15
%if %{with screencast}
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gbm)
# Don't use pkgconfig here as that would cause unresolvables on 0.1 -> 0.2 -> 0.3 bumps
BuildRequires:  pipewire-devel
# Without pipewire, screencasting won't work. Not a hard dep though.
Recommends:     pipewire
%endif
Requires:       xdg-desktop-portal
Recommends:     %{name}-lang
Supplements:    packageand(xdg-desktop-portal:plasma5-desktop)

%description
A Qt/KF5 backend implementation for xdg-desktop-portal

%if %{with released}
%lang_package
%endif

%prep
%setup -q

%build
%cmake_kf5 -d build
%cmake_build

%install
%make_install -C build
%if %{with released}
  %find_lang %{name} --with-man --all-name
%endif

%post
%{systemd_user_post plasma-xdg-desktop-portal-kde.service}

%preun
%{systemd_user_preun plasma-xdg-desktop-portal-kde.service}

%postun
%{systemd_user_postun plasma-xdg-desktop-portal-kde.service}

%files
%license LICENSES/*
%dir %{_kf5_sharedir}/xdg-desktop-portal
%dir %{_kf5_sharedir}/xdg-desktop-portal/portals
%{_kf5_applicationsdir}/org.freedesktop.impl.portal.desktop.kde.desktop
%{_kf5_notifydir}/xdg-desktop-portal-kde.notifyrc
%{_kf5_sharedir}/dbus-1/services/org.freedesktop.impl.portal.desktop.kde.service
%{_kf5_sharedir}/xdg-desktop-portal/portals/kde.portal
%{_libexecdir}/xdg-desktop-portal-kde
%{_userunitdir}/plasma-xdg-desktop-portal-kde.service

%if %{with released}
%files lang -f %{name}.lang
%license LICENSES/*
%endif

%changelog
