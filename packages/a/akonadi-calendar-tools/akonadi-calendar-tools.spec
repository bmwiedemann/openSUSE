#
# spec file for package akonadi-calendar-tools
#
# Copyright (c) 2020 SUSE LLC
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
%bcond_without lang
Name:           akonadi-calendar-tools
Version:        20.08.2
Release:        0
Summary:        Console applications and utilities for managing calendars
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  fdupes
BuildRequires:  gettext-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiCalendar)
BuildRequires:  cmake(KF5AkonadiContact)
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5CalendarSupport)
BuildRequires:  cmake(KF5CalendarUtils)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5Libkdepim)
BuildRequires:  cmake(Qt5Gui) >= 5.2.0
BuildRequires:  cmake(Qt5Widgets) >= 5.2.0
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Recommends:     %{name}-lang

%description
Console applications and utilities for managing calendars in Akonadi.

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=OFF
%cmake_build

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %{kf5_find_htmldocs}
%endif

%files
%license COPYING*
%{_kf5_debugdir}/console.categories
%{_kf5_debugdir}/console.renamecategories
%doc %lang(en) %{_kf5_htmldir}/en/konsolekalendar/
%{_kf5_applicationsdir}/konsolekalendar.desktop
%{_kf5_bindir}/calendarjanitor
%{_kf5_bindir}/konsolekalendar
%{_kf5_iconsdir}/hicolor/*/apps/konsolekalendar.png

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
