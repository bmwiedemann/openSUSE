#
# spec file for package francis
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


%bcond_without released
Name:           francis
Version:        1.0.1
Release:        0
Summary:        Productivity tool
License:        LGPL-2.1-or-later AND GPL-3.0-or-later
URL:            https://apps.kde.org/francis
Source:         https://download.kde.org/stable/francis/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/francis/%{name}-%{version}.tar.xz.sig
Source2:        francis.keyring
%endif
BuildRequires:  extra-cmake-modules >= 5.92
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5KirigamiAddons) >= 0.10
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(Qt5Core) >= 5.15
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
Requires:       knotifications-imports
Requires:       kirigami-addons
Requires:       kirigami2

%description
Francis uses the well-known pomodoro technique to help you get more productive.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --all-name

%files
%license LICENSES/*
%{_kf5_applicationsdir}/org.kde.francis.desktop
%{_kf5_appstreamdir}/org.kde.francis.metainfo.xml
%{_kf5_bindir}/francis
%{_kf5_iconsdir}/hicolor/scalable/apps/org.kde.francis.svg

%files lang -f %{name}.lang

%changelog
