#
# spec file for package zanshin
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


%bcond_without released
Name:           zanshin
Version:        22.12.0
Release:        0
Summary:        TODO Application
License:        GPL-2.0-only
URL:            https://zanshin.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  boost-devel
BuildRequires:  kf5-filesystem
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiCalendar)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KontactInterface)
BuildRequires:  cmake(KF5Runner)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)

%description
Zanshin Todo is an application for managing your day-to-day actions.
It helps you organize and reduce the cognitive pressure of what one has to do in his
job and personal life. You will never forget anything anymore.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%suse_update_desktop_file org.kde.zanshin Utility TimeUtility

%find_lang %{name}

%files
%license LICENSES/*
%doc AUTHORS
%dir %{_kf5_iconsdir}/hicolor/256x256
%dir %{_kf5_iconsdir}/hicolor/256x256/apps
%dir %{_kf5_plugindir}/pim5
%dir %{_kf5_plugindir}/pim5/kontact
%{_kf5_applicationsdir}/org.kde.zanshin.desktop
%{_kf5_appstreamdir}/org.kde.zanshin.metainfo.xml
%{_kf5_bindir}/zanshin
%{_kf5_bindir}/zanshin-migrator
%{_kf5_iconsdir}/hicolor/*/apps/zanshin.png
%{_kf5_iconsdir}/hicolor/scalable/apps/zanshin.svgz
%{_kf5_kxmlguidir}/zanshin/
%{_kf5_plugindir}/pim5/kontact/kontact_zanshinplugin.so
%{_kf5_plugindir}/krunner_zanshin.so
%{_kf5_plugindir}/zanshin_part.so
%{_kf5_servicesdir}/plasma-runner-zanshin.desktop
%{_kf5_servicesdir}/zanshin_part.desktop

%files lang -f %{name}.lang

%changelog
