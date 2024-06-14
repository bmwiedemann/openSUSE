#
# spec file for package libkmahjongg
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
Name:           libkmahjongg
Version:        24.05.1
Release:        0
Summary:        General Data for KDE Games
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
Obsoletes:      %{name}-kf5 < %{version}
Provides:       %{name}-kf5 = %{version}

%description
Common code, backgrounds and tile sets for games using Mahjongg tiles.

%package -n libKMahjongg6
Summary:        Library for Mahjongg tiles
Requires:       libkmahjongg >= %{version}

%description -n libKMahjongg6
Common code, backgrounds and tile sets for games using Mahjongg tiles.

%package devel
Summary:        Library for Mahjongg tiles: Build Environment
Requires:       libKMahjongg6 = %{version}
Requires:       cmake(KF6ConfigWidgets) >= %{kf6_version}
Requires:       cmake(Qt6Gui) >= %{qt6_version}
Obsoletes:      %{name}-kf5-devel < %{version}
Provides:       %{name}-kf5-devel = %{version}

%description devel
This package contains all necessary files and libraries needed to
develop games that uses Mahjongg tiles.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%fdupes -s %{buildroot}

%ldconfig_scriptlets -n libKMahjongg6

%files
%{_kf6_debugdir}/libkmahjongg.categories
%{_kf6_sharedir}/kmahjongglib/

%files -n libKMahjongg6
%license LICENSES/*
%doc README
%{_kf6_libdir}/libKMahjongg6.so.*

%files devel
%{_includedir}/KMahjongg6/
%{_kf6_cmakedir}/KMahjongglib6/
%{_kf6_libdir}/libKMahjongg6.so

%files lang -f %{name}.lang

%changelog
