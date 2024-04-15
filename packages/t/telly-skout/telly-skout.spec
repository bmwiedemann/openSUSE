#
# spec file for package telly-skout
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2021, Martin Hauke <mardnh@gmx.de>
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


%define kf5_version 5.75.0
%define qt5_version 5.15.0

%bcond_without released
Name:           telly-skout
Version:        24.02.2
Release:        0
Summary:        Kirigami TV guide
License:        LGPL-2.1-or-later
URL:            https://apps.kde.org/telly-skout/
Source0:        %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5Crash) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5KirigamiAddons)
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5Gui) >= %{qt5_version}
BuildRequires:  cmake(Qt5Quick) >= %{qt5_version}
BuildRequires:  cmake(Qt5QuickControls2) >= %{qt5_version}
BuildRequires:  cmake(Qt5Sql) >= %{qt5_version}
BuildRequires:  cmake(Qt5Test) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
BuildRequires:  cmake(Qt5Xml) >= %{qt5_version}
Requires:       kirigami2 >= %{kf5_version}
Requires:       kirigami-addons
Requires:       libQtQuick5 >= %{qt5_version}
Requires:       libQt5Sql5-sqlite >= %{qt5_version}

%description
Telly Skout is a convergent Kirigami TV guide. It shows the TV program for your
favorite channels from TV Spielfilm or an XMLTV file.

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
%doc README.md
%{_kf5_applicationsdir}/org.kde.telly-skout.desktop
%{_kf5_appstreamdir}/org.kde.telly-skout.appdata.xml
%{_kf5_bindir}/telly-skout
%{_kf5_iconsdir}/hicolor/scalable/apps/org.kde.telly-skout.svg

%files lang -f %{name}.lang

%changelog
