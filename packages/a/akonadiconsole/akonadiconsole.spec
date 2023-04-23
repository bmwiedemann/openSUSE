#
# spec file for package akonadiconsole
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


%define kf5_version 5.104.0
%bcond_without released
Name:           akonadiconsole
Version:        23.04.0
Release:        0
Summary:        Management and debugging console for akonadi
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  libxapian-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KPim5Akonadi)
BuildRequires:  cmake(KPim5AkonadiContact)
BuildRequires:  cmake(KPim5AkonadiMime)
BuildRequires:  cmake(KPim5AkonadiSearch)
BuildRequires:  cmake(KPim5CalendarSupport)
BuildRequires:  cmake(KPim5Libkdepim)
BuildRequires:  cmake(KPim5MessageViewer)
BuildRequires:  cmake(KPim5Mime)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
Obsoletes:      akonadi_resources < %{version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64

%description
Akonadi Console is a utility that can be used to explore or manage
Akonadi. This utility exposes Akonadi internals, and can be useful
for debugging.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=OFF
%cmake_build

%install
%kf5_makeinstall -C build
%suse_update_desktop_file -u org.kde.akonadiconsole Network Email

%find_lang %{name}

%ldconfig_scriptlets

%files lang -f %{name}.lang

%files
%license LICENSES/*
%dir %{_kf5_iconsdir}/hicolor/256x256
%dir %{_kf5_iconsdir}/hicolor/256x256/apps
%{_kf5_applicationsdir}/org.kde.akonadiconsole.desktop
%{_kf5_bindir}/akonadiconsole
%{_kf5_debugdir}/akonadiconsole.categories
%{_kf5_debugdir}/akonadiconsole.renamecategories
%{_kf5_iconsdir}/hicolor/*/apps/akonadiconsole.png
%{_kf5_libdir}/libakonadiconsole.so.*

%changelog
