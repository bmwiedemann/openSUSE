#
# spec file for package kirigami-app-components6
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define kf6_version 6.22.0
%define qt6_version 6.8.0
#
%bcond_without released
#
%define rname kirigami-app-components
Name:           kirigami-app-components6
Version:        1.0.1
Release:        0
Summary:        Kirigami addons and modules
License:        LGPL-2.1-or-later
URL:            https://invent.kde.org/libraries/kirigami-app-components
Source0:        https://download.kde.org/stable/%{rname}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/%{rname}/%{rname}-%{version}.tar.xz.sig
Source2:        kirigami-app-components.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  qt6qmlimport(org.kde.ki18n) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
Kirigami addons and modules necessary to do a full featured KDE application,
such as integration with configurable keyboard shortcuts and standard actions.

%package -n libKirigamiActionCollection6
Summary:        Kirigami addons and modules

%description -n libKirigamiActionCollection6
Kirigami addons and modules necessary to do a full featured KDE application,
such as integration with configurable keyboard shortcuts and standard actions.

%package devel
Summary:        Kirigami addons and modules
Requires:       kf6-extra-cmake-modules >= %{kf6_version}
Requires:       libKirigamiActionCollection6 = %{version}
Requires:       cmake(Qt6Core) >= %{qt6_version}
%lang_package

%description devel
Kirigami addons and modules necessary to do a full featured KDE application,
such as integration with configurable keyboard shortcuts and standard actions.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

# TODO missing ki18n_install(po) upstream
%dnl %find_lang %{name} --all-name

%ldconfig_scriptlets -n libKirigamiActionCollection6

%files
%license LICENSES/*
%doc README.md
%dir %{_kf6_qmldir}/org/kde/kirigami
%{_kf6_qmldir}/org/kde/kirigami/actioncollection/

%files -n libKirigamiActionCollection6
%license LICENSES/*
%{_kf6_libdir}/libKirigamiActionCollection.so.*

%files devel
%{_kf6_cmakedir}/KF6KirigamiAppComponents/
%dir %{_kf6_includedir}/Kirigami
%{_kf6_includedir}/Kirigami/ActionCollection/
%{_kf6_libdir}/libKirigamiActionCollection.so

%dnl %files lang -f %{name}.lang

%changelog

