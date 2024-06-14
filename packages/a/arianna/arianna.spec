#
# spec file for package arianna
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
Name:           arianna
Version:        24.05.1
Release:        0
Summary:        Ebook reader and library management app
License:        GPL-3.0-only
URL:            https://apps.kde.org/arianna/
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Baloo) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6FileMetaData) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6Kirigami) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiAddons) >= 0.11
BuildRequires:  cmake(KF6QQC2DesktopStyle) >= %{kf6_version}
BuildRequires:  cmake(KF6QuickCharts) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6HttpServer) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebChannel) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineQuick) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebSockets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
Requires:       kirigami-addons6
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kf6-kquickcharts  >= %{kf6_version}
Requires:       qt6-sql-sqlite >= %{qt6_version}
Requires:       qt6-declarative-imports >= %{qt6_version}
# No QtWebEngine for other archs
ExclusiveArch:  x86_64 %{x86_64} aarch64 riscv64

%description
An ebook reader and library management app supporting ".epub" files. Arianna
discovers your books automatically, and sorts them by categories, genres and
authors.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name}

%files
%license LICENSES/*
%doc README.md
%{_kf6_applicationsdir}/org.kde.arianna.desktop
%{_kf6_appstreamdir}/org.kde.arianna.appdata.xml
%{_kf6_bindir}/arianna
%{_kf6_debugdir}/arianna.categories
%{_kf6_iconsdir}/hicolor/scalable/apps/org.kde.arianna.svg

%files lang -f %{name}.lang

%changelog
