#
# spec file for package kfind
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
Name:           kfind
Version:        22.12.1
Release:        0
Summary:        KDE Find File Utility
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kfind
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  hicolor-icon-theme
BuildRequires:  kf5-filesystem
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5FileMetaData)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Widgets)

%description
KFind allows you to search for directories and files.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%suse_update_desktop_file org.kde.kfind System Filesystem core

%files
%license LICENSES/*
%doc %lang(en) %{_kf5_htmldir}/en/kfind/
%doc %{_kf5_mandir}/man1/kfind.*
%{_kf5_applicationsdir}/org.kde.kfind.desktop
%{_kf5_appstreamdir}/org.kde.kfind.appdata.xml
%{_kf5_bindir}/kfind
%{_kf5_debugdir}/kfind.categories
%{_kf5_iconsdir}/hicolor/*/apps/kfind.*

%files lang -f %{name}.lang

%changelog
