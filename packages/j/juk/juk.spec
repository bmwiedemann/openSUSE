#
# spec file for package juk
#
# Copyright (c) 2021 SUSE LLC
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


%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without  lang
Name:           juk
Version:        21.04.0
Release:        0
Summary:        Jukebox
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            https://apps.kde.org/juk
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  libtag-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
%if 0%{?suse_version} == 1500
# Needed when building with Qt < 5.13.0
BuildRequires:  cmake(KF5ItemModels)
%endif
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
Recommends:     %{name}-lang

%description
Jukebox and music manager by KDE

%lang_package

%prep
%autosetup -p1

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %{kf5_find_htmldocs}
%endif
  %suse_update_desktop_file org.kde.juk            AudioVideo Player

%files
%license COPYING
%{_kf5_applicationsdir}/org.kde.juk.desktop
%{_kf5_appsdir}/juk/
%{_kf5_appstreamdir}/org.kde.juk.appdata.xml
%{_kf5_bindir}/juk
%{_kf5_dbusinterfacesdir}/org.kde.juk.*
%{_kf5_htmldir}/en/juk/
%{_kf5_iconsdir}/hicolor/*/apps/juk.*
%{_kf5_kxmlguidir}/juk
%{_kf5_notifydir}/juk.notifyrc
%dir %{_kf5_servicesdir}/ServiceMenus/
%{_kf5_servicesdir}/ServiceMenus/jukservicemenu.desktop

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
