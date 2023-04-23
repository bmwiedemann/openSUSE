#
# spec file for package kalk
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


%bcond_without  released
Name:           kalk
Version:        23.04.0
Release:        0
Summary:        Convergent calculator
License:        GPL-3.0-or-later
URL:            https://apps.kde.org/kalk
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  bison
BuildRequires:  extra-cmake-modules
BuildRequires:  flex
BuildRequires:  gmp-devel
BuildRequires:  mpfr-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5UnitConversion)
BuildRequires:  cmake(Qt5Core) >= 5.15.2
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickCompiler)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
Requires:       kirigami2

%description
Kalk is a convergent calculator application built with the Kirigami framework.
Although it is mainly targeted for mobile platforms, it can also be used on the
desktop.

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
%{_kf5_applicationsdir}/org.kde.kalk.desktop
%{_kf5_appstreamdir}/org.kde.kalk.appdata.xml
%{_kf5_bindir}/kalk
%{_kf5_iconsdir}/hicolor/scalable/apps/org.kde.kalk.svg

%files lang -f %{name}.lang

%changelog
