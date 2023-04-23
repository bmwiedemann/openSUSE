# spec file for kongress
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
Name:           kongress
Version:        23.04.0
Release:        0
License:        GPL-3.0-or-later
Summary:        Companion application for conferences
Url:            https://apps.kde.org/kongress/
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
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
Requires:       kirigami2

%description
Kongress provides practical information about conferences.
It supports conferences that offer their schedule in iCalendar
format. In Kongress, the data of the talks are shown in various
ways, e.g. in daily views, by talk category, etc. The users can
also create a list of favorite conference talks/events as well as
they can navigate to the web page of each talk. A map of the
conference venue, location information and link to OpenStreetMap
can also be added.

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
%license LICENSES/*
%doc README.md
%{_kf5_applicationsdir}/org.kde.kongress.desktop
%{_kf5_appstreamdir}/org.kde.kongress.appdata.xml
%{_kf5_bindir}/kongress
%{_kf5_bindir}/kongressac
%{_kf5_iconsdir}/hicolor/scalable/apps/org.kde.kongress.svg
%{_kf5_notifydir}/kongressac.notifyrc
%{_kf5_sharedir}/dbus-1/services/org.kde.kongressac.service

%files lang -f %{name}.lang

%changelog
