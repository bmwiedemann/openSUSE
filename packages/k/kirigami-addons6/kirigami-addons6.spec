#
# spec file for package kirigami-addons6
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define kf6_version 6.15.0
%define qt6_version 6.6.0

%bcond_without released

%define rname kirigami-addons
Name:           kirigami-addons6
Version:        1.10.0
Release:        0
Summary:        Add-ons for the Kirigami framework
License:        LGPL-3.0-only
URL:            https://invent.kde.org/libraries/kirigami-addons
Source:         https://download.kde.org/stable/%{rname}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/%{rname}/%{rname}-%{version}.tar.xz.sig
Source2:        kirigami-addons.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6ColorScheme) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Tools) >= %{qt6_version}
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       libKF6Svg6 >= %{kf6_version}
Requires:       libKirigamiAddonsStatefulApp6 >= %{version}

%description
A set of "widgets" i.e visual end user components along with a
code to support them. Components are usable by both touch and
desktop experiences providing a native experience on both, and
look native with any QQC2 style (qqc2-desktop-theme, Material
or Plasma).

%package -n libKirigamiApp6
Summary:        KirigamiApp library

%description -n libKirigamiApp6
A set of "widgets" i.e visual end user components along with a
code to support them. Components are usable by both touch and
desktop experiences providing a native experience on both, and
look native with any QQC2 style (qqc2-desktop-theme, Material
or Plasma). This package provides a helper to properly
run a Kirigami app on all OSes.

%package -n libKirigamiAddonsStatefulApp6
Summary:        Stateful application suppport library for kirigami-addons

%description -n libKirigamiAddonsStatefulApp6
A set of "widgets" i.e visual end user components along with a
code to support them. Components are usable by both touch and
desktop experiences providing a native experience on both, and
look native with any QQC2 style (qqc2-desktop-theme, Material
or Plasma). This package provides a library to add standard
stateful functionality to applications using kirigami-addons.

%package devel
Summary:        Development files for kirigami-addons6
Requires:       kirigami-addons6 = %{version}
Requires:       libKirigamiAddonsStatefulApp6 = %{version}
Requires:       libKirigamiApp6 = %{version}

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
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libKirigamiAddonsStatefulApp6
%ldconfig_scriptlets -n libKirigamiApp6

%files
%license LICENSES/*
%{_kf6_qmldir}/org/kde/kirigamiaddons/

%files -n libKirigamiAddonsStatefulApp6
%{_kf6_libdir}/libKirigamiAddonsStatefulApp.so.*

%files -n libKirigamiApp6
%{_kf6_libdir}/libKirigamiApp.so.*

%files devel
%{_kf6_cmakedir}/KF6KirigamiAddons/
%{_includedir}/KirigamiAddons/
%{_includedir}/KirigamiAddonsStatefulApp/
%{_kf6_libdir}/libKirigamiAddonsStatefulApp.so
%{_kf6_libdir}/libKirigamiApp.so
%dir %{_kf6_sharedir}/kdevappwizard/
%dir %{_kf6_sharedir}/kdevappwizard/templates/
%{_kf6_sharedir}/kdevappwizard/templates/kirigamiaddons6.tar.bz2
%{_kf6_sharedir}/kdevappwizard/templates/librarymanager6.tar.bz2

%files lang -f %{name}.lang

%changelog
