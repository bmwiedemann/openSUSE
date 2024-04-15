#
# spec file for package akonadi-calendar-tools
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
%define kpim6_version 6.0.2

%bcond_without released
Name:           akonadi-calendar-tools
Version:        24.02.2
Release:        0
Summary:        Console applications and utilities for managing calendars
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6CalendarCore) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KPim6Akonadi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiCalendar) >= %{kpim6_version}
BuildRequires:  cmake(KPim6CalendarSupport) >= %{kpim6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  x86_64 %x86_64 aarch64 riscv64

%description
Console applications and utilities for managing calendars in Akonadi.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-man --with-html --all-name

%files
%license LICENSES/*
%doc %lang(en) %{_kf6_htmldir}/en/konsolekalendar/
%{_kf6_applicationsdir}/konsolekalendar.desktop
%{_kf6_bindir}/calendarjanitor
%{_kf6_bindir}/konsolekalendar
%{_kf6_debugdir}/console.categories
%{_kf6_debugdir}/console.renamecategories
%{_kf6_iconsdir}/hicolor/*/apps/konsolekalendar.png

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/konsolekalendar/

%changelog
