#
# spec file for package kirigami-addons6
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


%define kf6_version 6.1.0
%define qt6_version 6.6.0

%bcond_without released

%define rname kirigami-addons
Name:           kirigami-addons6
Version:        1.3.0
Release:        0
Summary:        Add-ons for the Kirigami framework
License:        LGPL-3.0-only
URL:            https://invent.kde.org/libraries/kirigami-addons
Source:         https://download.kde.org/stable/%{rname}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/%{rname}/%{rname}-%{version}.tar.xz.sig
Source2:        kirigami-addons.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       libKF6Svg6 >= %{kf6_version}
Requires:       qt6-qt5compat-imports >= %{qt6_version}

%description
A set of "widgets" i.e visual end user components along with a
code to support them. Components are usable by both touch and
desktop experiences providing a native experience on both, and
look native with any QQC2 style (qqc2-desktop-theme, Material
or Plasma).

%package devel
Summary:        Development files for kirigami-addons6
Requires:       kirigami-addons6 = %{version}

%description devel
A set of "widgets" i.e visual end user components along with a
code to support them. Components are usable by both touch and
desktop experiences providing a native experience on both, and
look native with any QQC2 style (qqc2-desktop-theme, Material
or Plasma). This package provides development files to build
applications with kirigami-addons.

%package lang
Summary:        Translations for package %{name}
Requires:       %{name} = %{version}
Provides:       %{name}-lang-all = %{version}
# Same file names, needs to be fixed upstream
Conflicts:      kirigami-addons-lang
BuildArch:      noarch

%description lang
Provides translations for %{name}.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
# A DBUILD_QCH option exists but does nothing
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}%{_kf6_qmldir}

%find_lang %{name} --all-name

%files
%license LICENSES/*
%{_kf6_qmldir}/org/kde/kirigamiaddons/

%files devel
%{_kf6_cmakedir}/KF6KirigamiAddons/

%files lang -f %{name}.lang

%changelog
