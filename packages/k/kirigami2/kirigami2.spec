#
# spec file for package kirigami2
#
# Copyright (c) 2021 SUSE LLC
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


%define lname libKF5Kirigami2-5
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%define qt5_version 5.15.2
%bcond_without released
Name:           kirigami2
Version:        5.116.0
Release:        0
Summary:        Set of QtQuick components
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_version}
%if 0%{?suse_version} == 1500
BuildRequires:  gcc13-c++
BuildRequires:  gcc13-PIE
%endif
BuildRequires:  libQt5Gui-private-headers-devel >= %{qt5_version}
BuildRequires:  cmake(Qt5Concurrent) >= %{qt5_version}
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_version}
BuildRequires:  cmake(Qt5Gui) >= %{qt5_version}
BuildRequires:  cmake(Qt5LinguistTools) >= %{qt5_version}
BuildRequires:  cmake(Qt5Quick) >= %{qt5_version}
BuildRequires:  cmake(Qt5QuickControls2) >= %{qt5_version}
BuildRequires:  cmake(Qt5Svg) >= %{qt5_version}
BuildRequires:  cmake(Qt5Test) >= %{qt5_version}
Requires:       libqt5-qtgraphicaleffects
Requires:       libqt5-qtquickcontrols2

%description
QtQuick plugins to build user interfaces based on the KDE UX guidelines.

%package -n %{lname}
Summary:        Set of QtQuick components
Recommends:     %{name} = %{version}

%description -n %{lname}
QtQuick plugins to build user interfaces based on the KDE UX guidelines.
Based on Qt Quick Controls 2. This package contains the base shared libraries.

%package devel
Summary:        Development package for kirigami
Requires:       %{lname} = %{version}
Requires:       %{name} = %{version}

%description devel
QtQuick plugins to build user interfaces based on the KDE UX guidelines.
Development files.

%lang_package

%prep
%autosetup -p1

%build
%if 0%{?suse_version} == 1500
export CXX=g++-13
%endif

%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang libkirigami2plugin --with-qt --without-mo

%ldconfig_scriptlets -n %{lname}

%files
%dir %{_kf5_sharedir}/kdevappwizard/
%{_kf5_qmldir}/
%{_kf5_sharedir}/kdevappwizard/templates/

%files -n %{lname}
%license LICENSES/*
%{_kf5_libdir}/libKF5Kirigami2.so.*

%files devel
%{_kf5_includedir}/Kirigami2/
%{_kf5_libdir}/libKF5Kirigami2.so
%{_kf5_mkspecsdir}/qt_Kirigami2.pri
%{_libdir}/cmake/KF5Kirigami2/

%files lang -f libkirigami2plugin.lang

%changelog
