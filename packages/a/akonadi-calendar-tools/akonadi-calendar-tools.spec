#
# spec file for package akonadi-calendar-tools
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
Name:           akonadi-calendar-tools
Version:        23.04.0
Release:        0
Summary:        Console applications and utilities for managing calendars
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KPim5Akonadi)
BuildRequires:  cmake(KPim5AkonadiCalendar)
BuildRequires:  cmake(KPim5CalendarSupport)
BuildRequires:  cmake(KPim5CalendarUtils)
BuildRequires:  cmake(Qt5Widgets)

%description
Console applications and utilities for managing calendars in Akonadi.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=OFF
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%files
%license LICENSES/*
%doc %lang(en) %{_kf5_htmldir}/en/konsolekalendar/
%{_kf5_applicationsdir}/konsolekalendar.desktop
%{_kf5_bindir}/calendarjanitor
%{_kf5_bindir}/konsolekalendar
%{_kf5_debugdir}/console.categories
%{_kf5_debugdir}/console.renamecategories
%{_kf5_iconsdir}/hicolor/*/apps/konsolekalendar.png

%files lang -f %{name}.lang

%changelog
