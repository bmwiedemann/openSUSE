#
# spec file for package ktrip
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

%bcond_without released
Name:           ktrip
Version:        24.05.2
Release:        0
Summary:        Public transport assistant targeted towards mobile Linux and Android
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/ktrip
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-breeze-icons >= %{kf6_version}
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6QQC2DesktopStyle) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiAddons) >= 0.11.0
BuildRequires:  cmake(KPublicTransport)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
# Breeze is used as the fallback icon theme
Requires:       kf6-breeze-icons
# QML imports
Requires:       kf6-kitemmodels-imports >= %{kf6_version}
Requires:       kirigami-addons6 >= 0.11.0
Requires:       kpublictransport
Requires:       kf6-kirigami-imports >= %{kf6_version}

%description
KTrip is a public transport assistant targeted towards mobile Linux and
Android. It allows to query journeys for a wide range of countries/public
transport providers by leveraging KPublicTransport.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%suse_update_desktop_file org.kde.ktrip Utility Maps

%find_lang %{name}

%files
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/ktrip
%{_kf6_iconsdir}/hicolor/scalable/apps/org.kde.ktrip.svg
%{_kf6_applicationsdir}/org.kde.ktrip.desktop
%{_kf6_appstreamdir}/org.kde.ktrip.appdata.xml

%files lang -f %{name}.lang

%changelog
