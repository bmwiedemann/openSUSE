#
# spec file for package ktrip
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
Name:           ktrip
Version:        23.04.0
Release:        0
Summary:        Public transport assistant targeted towards mobile Linux and Android
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/ktrip
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  breeze5-icons
BuildRequires:  extra-cmake-modules
BuildRequires:  hicolor-icon-theme
BuildRequires:  kf5-filesystem
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5QQC2DesktopStyle)
BuildRequires:  cmake(KPublicTransport)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Widgets)
# Breeze is used as the fallback icon theme
Requires:       breeze5-icons
# QML imports
Requires:       kpublictransport
Requires:       kirigami2

%description
KTrip is a public transport assistant targeted towards mobile Linux and
Android. It allows to query journeys for a wide range of countries/public
transport providers by leveraging KPublicTransport.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%suse_update_desktop_file org.kde.ktrip Utility Maps

%find_lang %{name}

%files
%license LICENSES/*
%doc README.md
%{_kf5_bindir}/ktrip
%{_kf5_iconsdir}/hicolor/scalable/apps/org.kde.ktrip.svg
%{_kf5_applicationsdir}/org.kde.ktrip.desktop
%{_kf5_appstreamdir}/org.kde.ktrip.appdata.xml

%files lang -f %{name}.lang

%changelog
