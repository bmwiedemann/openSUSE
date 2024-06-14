#
# spec file for package skanpage
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
Name:           skanpage
Version:        24.05.1
Release:        0
Summary:        Multi-Page Scanning Application
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/skanpage/
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
# Both kquickimageeditor flavors provide the same CMake target name, use the devel package name instead
# BuildRequires:  cmake(KQuickImageEditor)
BuildRequires:  kquickimageeditor6-devel
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6Kirigami2) >= %{kf6_version}
BuildRequires:  cmake(KF6Purpose) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KSaneCore6)
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Pdf) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
# For OCR
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
BuildRequires:  pkgconfig(tesseract) >= 4
BuildRequires:  pkgconfig(lept)
%endif
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kquickimageeditor6-imports >= 0.2
Requires:       qt6-declarative-imports >= %{qt6_version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  x86_64 %{x86_64} aarch64 riscv64

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
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name}

%files
%license LICENSES/*
%doc README.md
%{_kf6_applicationsdir}/org.kde.skanpage.desktop
%{_kf6_appstreamdir}/org.kde.skanpage.appdata.xml
%{_kf6_bindir}/skanpage
%{_kf6_debugdir}/skanpage.categories
%{_kf6_iconsdir}/hicolor/*/apps/skanpage.*

%files lang -f %{name}.lang

%changelog
