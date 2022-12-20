#
# spec file for package kirigami-addons
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


%bcond_without released

Name:           kirigami-addons
Version:        0.6.1
Release:        0
Summary:        Add-ons for the Kirigami framework
License:        LGPL-3.0-only
URL:            https://invent.kde.org/libraries/kirigami-addons
Source:         https://download.kde.org/stable/kirigami-addons/kirigami-addons-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/kirigami-addons/kirigami-addons-%{version}.tar.xz.sig
Source2:        kirigami-addons.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
Requires:       kirigami2

%description
A set of "widgets" i.e visual end user components along with a
code to support them. Components are usable by both touch and
desktop experiences providing a native experience on both, and
look native with any QQC2 style (qqc2-desktop-theme, Material
or Plasma).

%package devel
Summary: Development files for kirigami-addons
Requires: %{name} = %{version}

%description devel
A set of "widgets" i.e visual end user components along with a
code to support them. Components are usable by both touch and
desktop experiences providing a native experience on both, and
look native with any QQC2 style (qqc2-desktop-theme, Material
or Plasma). This package provides development files to build 
applications with kirigami-addons.

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
%dir %{_kf5_qmldir}/org/
%dir %{_kf5_qmldir}/org/kde/
%{_kf5_qmldir}/org/kde/kirigamiaddons/

%files devel
%{_kf5_cmakedir}/KF5KirigamiAddons/

%files lang -f %{name}.lang

%changelog
