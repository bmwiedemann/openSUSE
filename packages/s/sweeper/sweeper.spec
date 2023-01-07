#
# spec file for package sweeper
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


# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           sweeper
Version:        22.12.1
Release:        0
Summary:        KDE Privacy Utility
License:        LGPL-2.1-or-later
URL:            https://apps.kde.org/sweeper
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  breeze5-icons
BuildRequires:  extra-cmake-modules
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5ActivitiesStats)
BuildRequires:  cmake(KF5Bookmarks)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Widgets)

%description
Helps clean unwanted traces the user leaves on the system.

%lang_package

%prep
%autosetup -p1 -n sweeper-%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%suse_update_desktop_file org.kde.sweeper Utility Security
mkdir -p %{buildroot}%{_kf5_iconsdir}/hicolor/scalable/actions
mkdir -p %{buildroot}%{_kf5_iconsdir}/hicolor/scalable/apps/
cp %{_kf5_iconsdir}/breeze/actions/24/trash-empty.svg %{buildroot}%{_kf5_iconsdir}/hicolor/scalable/actions/
cp %{_kf5_iconsdir}/breeze/apps/48/sweeper.svg %{buildroot}%{_kf5_iconsdir}/hicolor/scalable/apps/

%files
%license LICENSES/*
%doc %lang(en) %{_kf5_htmldir}/en/sweeper/
%{_kf5_applicationsdir}/org.kde.sweeper.desktop
%{_kf5_appstreamdir}/org.kde.sweeper.appdata.xml
%{_kf5_bindir}/sweeper
%{_kf5_debugdir}/sweeper.categories
%{_kf5_iconsdir}/hicolor/scalable/*/*
%{_kf5_kxmlguidir}/sweeper/
%{_kf5_sharedir}/dbus-1/interfaces/*.xml

%files lang -f %{name}.lang

%changelog
