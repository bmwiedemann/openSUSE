# spec file for kongress
#
# Copyright (c) 2024 SUSE LLC
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without  released
Name:           kongress
Version:        24.05.1
Release:        0
License:        GPL-3.0-or-later
Summary:        Companion application for conferences
Url:            https://apps.kde.org/kongress/
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6CalendarCore) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6Kirigami) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       kf6-kirigami-imports >= %{kf6_version}

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
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%files
%license LICENSES/*
%doc README.md
%{_kf6_applicationsdir}/org.kde.kongress.desktop
%{_kf6_appstreamdir}/org.kde.kongress.appdata.xml
%{_kf6_bindir}/kongress
%{_kf6_bindir}/kongressac
%{_kf6_iconsdir}/hicolor/scalable/apps/org.kde.kongress.svg
%{_kf6_notificationsdir}/kongressac.notifyrc
%{_kf6_sharedir}/dbus-1/services/org.kde.kongressac.service

%files lang -f %{name}.lang

%changelog
