#
# spec file for package arianna
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
Name:           arianna
Version:        1.0.1
Release:        0
Summary:        Ebook reader and library management app
License:        GPL-3.0-only
URL:            https://apps.kde.org/arianna/
Source0:        https://download.kde.org/stable/arianna/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/arianna/%{name}-%{version}.tar.xz.sig
# https://carlschwan.eu/gpg-02325448204e452a/
Source2:        arianna.keyring
%endif
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Baloo)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5FileMetaData)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5KirigamiAddons) >= 0.8
BuildRequires:  cmake(KF5QQC2DesktopStyle)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5WebEngine)
BuildRequires:  cmake(Qt5WebSockets)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
Requires:       kirigami-addons
Requires:       kirigami2
Requires:       libQt5Sql5-sqlite
Requires:       libqt5-qtquickcontrols2
# No QtWebEngine for other archs
ExclusiveArch:  %{arm} aarch64 %{ix86} x86_64 %{riscv}

%description
An ebook reader and library management app supporting ".epub" files. Arianna
discovers your books automatically, and sorts them by categories, genres and
authors.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build

%install
%kf5_makeinstall -C build

%find_lang %{name}

%files
%license LICENSES/*
%doc README.md
%{_kf5_applicationsdir}/org.kde.arianna.desktop
%{_kf5_appstreamdir}/org.kde.arianna.appdata.xml
%{_kf5_bindir}/arianna
%{_kf5_debugdir}/arianna.categories
%{_kf5_iconsdir}/hicolor/scalable/apps/org.kde.arianna.svg

%files lang -f %{name}.lang

%changelog
