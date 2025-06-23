#
# spec file for package ktimetracker
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


%define kf6_version 6.14.0
%define qt6_version 6.4.0

%bcond_without released
Name:           ktimetracker
Version:        6.0.0
Release:        0
Summary:        Personal Time Tracker
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/ktimetracker
Source0:        https://download.kde.org/unstable/ktimetracker/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/unstable/ktimetracker/%{name}-%{version}.tar.xz.sig
# https://invent.kde.org/sysadmin/release-keyring/-/blob/master/keys/thiagosueto@key1.asc
Source2:        ktimetracker.keyring
%endif
# PATCH-FIX-UPSTREAM
Patch0:         0001-Fix-icons-installation.patch
# PATCH-FIX-UPSTREAM
Patch1:         0001-Install-docs-translations.patch
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6CalendarCore) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6IdleTime) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}

%description
KTimeTracker tracks time spent on various tasks.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html

%files
%license LICENSES/*
%doc README.md ChangeLog.md
%doc %lang(en) %{_kf6_htmldir}/en/ktimetracker/
%{_kf6_applicationsdir}/org.kde.ktimetracker.desktop
%{_kf6_appstreamdir}/org.kde.ktimetracker.appdata.xml
%{_kf6_bindir}/ktimetracker
%{_kf6_dbusinterfacesdir}/org.kde.ktimetracker.ktimetracker.xml
%{_kf6_iconsdir}/hicolor/*/apps/ktimetracker.png

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/ktimetracker/

%changelog
