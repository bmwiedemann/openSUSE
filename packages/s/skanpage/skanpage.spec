#
# spec file for package skanpage
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


%define qt5_version 5.15.2
%define kf5_version 5.94.0
%bcond_without released
Name:           skanpage
Version:        22.12.1
Release:        0
Summary:        Multi-Page Scanning Application
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/skanpage/
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5Crash) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5Kirigami2) >= %{kf5_version}
BuildRequires:  cmake(KF5Purpose) >= %{kf5_version}
BuildRequires:  cmake(KSaneCore)
BuildRequires:  cmake(Qt5Concurrent) >= %{qt5_version}
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5PrintSupport) >= %{qt5_version}
BuildRequires:  cmake(Qt5Qml) >= %{qt5_version}
BuildRequires:  cmake(Qt5Quick) >= %{qt5_version}
BuildRequires:  cmake(Qt5QuickControls2) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
# For OCR
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
BuildRequires:  pkgconfig(tesseract) >= 4
BuildRequires:  pkgconfig(lept)
%endif
Requires:       kirigami2 >= %{kf5_version}
Requires:       libqt5-qtquickcontrols >= %{qt5_version}

%description
Skanpage is a simple scanning application designed for
multi-page scanning and saving of documents and images.

Features:
- Scanning from flatbed and ADF scanners
- Configurable options for scanning device
- Reordering, rotation and deletion of scanned pages
- Saving to multi-page PDF documents and image files

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name}

%files
%license LICENSES/*
%doc README.md
%{_kf5_applicationsdir}/org.kde.skanpage.desktop
%{_kf5_appstreamdir}/org.kde.skanpage.appdata.xml
%{_kf5_bindir}/skanpage
%{_kf5_debugdir}/skanpage.categories
%{_kf5_iconsdir}/hicolor/*/apps/skanpage.*

%files lang -f %{name}.lang

%changelog
