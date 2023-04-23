#
# spec file for package calindori
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


%bcond_without  released
Name:           calindori
Version:        23.04.0
Release:        0
Summary:        Kirigami-based calendar application
License:        GPL-3.0-or-later
URL:            https://apps.kde.org/calindori
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
%if 0%{?suse_version} == 1500
BuildRequires:  gcc10-c++
BuildRequires:  gcc10-PIE
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5People)
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickCompiler)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
Requires:       kirigami2
# TODO: Check if needed
Requires:       kpeoplevcard

%description
Calindori is a touch friendly calendar application.
It has been designed for mobile devices but it can also run on desktop environments.
Users of Calindori are able to check previous and future dates and manage tasks and events.

%lang_package

%prep
%autosetup -p1

%build
%if 0%{?suse_version} == 1500
  export CXX=g++-10
%endif

%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --all-name

%files
%doc README.md
%license LICENSES/*
%{_datadir}/dbus-1/services/org.kde.calindac.service
%{_kf5_applicationsdir}/org.kde.calindori.desktop
%{_kf5_appstreamdir}/org.kde.calindori.appdata.xml
%{_kf5_bindir}/calindac
%{_kf5_bindir}/calindori
%{_kf5_configdir}/autostart/org.kde.calindac.desktop
%{_kf5_iconsdir}/hicolor/scalable/apps/calindori.svg
%{_kf5_notifydir}/calindac.notifyrc

%files lang -f %{name}.lang

%changelog
