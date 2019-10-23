#
# spec file for package xdg-desktop-portal-kde
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%bcond_without lang
%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150000
%bcond_without screencast
%else
%bcond_with screencast
%endif

%define kf5_version 5.50.0
Name:           xdg-desktop-portal-kde
Version:        5.17.1
Release:        0
Summary:        QT/KF5 backend for xdg-desktop-portal
License:        LGPL-2.1-or-later
Group:          System/Libraries
Url:            http://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/xdg-desktop-portal-kde-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/plasma/%{version}/xdg-desktop-portal-kde-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  libQt5PrintSupport-private-headers-devel
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5Notifications) >= %{kf5_version}
BuildRequires:  cmake(KF5Wayland) >= %{kf5_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{kf5_version}
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core) >= 5.11.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Widgets)
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

%if %{with lang}
%lang_package
%endif

%prep
%setup -q

%build
%cmake_kf5 -d build
%make_jobs

%install
%make_install -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
%endif

%files
%license COPYING
%{_libdir}/libexec/xdg-desktop-portal-kde
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.kde.service
%dir %{_datadir}/xdg-desktop-portal
%dir %{_datadir}/xdg-desktop-portal/portals
%{_datadir}/xdg-desktop-portal/portals/kde.portal

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING
%endif

%changelog
