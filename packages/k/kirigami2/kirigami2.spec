#
# spec file for package kirigami2
#
# Copyright (c) 2020 SUSE LLC
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
%define _tar_path 5.75
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kirigami2
Version:        5.75.0
Release:        0
Summary:        Set of QtQuick components
License:        LGPL-2.1-or-later
Group:          Development/Libraries/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch:          0001-Revert-Watch-for-language-change-events-and-forward-.patch
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(Qt5Concurrent) >= 5.12.0
BuildRequires:  cmake(Qt5Core) >= 5.12.0
BuildRequires:  cmake(Qt5DBus) >= 5.12.0
BuildRequires:  cmake(Qt5Gui) >= 5.12.0
BuildRequires:  cmake(Qt5Quick) >= 5.12.0
BuildRequires:  cmake(Qt5QuickControls2) >= 5.12.0
BuildRequires:  cmake(Qt5Svg) >= 5.12.0
BuildRequires:  cmake(Qt5Test) >= 5.12.0
Requires:       libqt5-qtgraphicaleffects
Requires:       libqt5-qtquickcontrols2
Recommends:     %{name}-lang = %{version}
%if %{with lang}
BuildRequires:  cmake(Qt5LinguistTools) >= 5.12.0
%endif

%description
QtQuick plugins to build user interfaces based on the KDE UX guidelines.

%package -n %{lname}
Summary:        Set of QtQuick components
Group:          System/Libraries
Recommends:     %{name} = %{version}

%description -n %{lname}
QtQuick plugins to build user interfaces based on the KDE UX guidelines.
Based on Qt Quick Controls 2. This package contains the base shared libraries.

%package devel
Summary:        Development package for kirigami
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       %{name} = %{version}

%description devel
QtQuick plugins to build user interfaces based on the KDE UX guidelines.
Development files.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%if %{with lang}
%find_lang libkirigami2plugin --with-qt --without-mo
%endif

%if %{with lang}
%files lang -f libkirigami2plugin.lang
%endif

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%license LICENSES/*
%dir %{_kf5_sharedir}/kdevappwizard/
%{_kf5_qmldir}/
%{_kf5_sharedir}/kdevappwizard/templates/

%files -n %{lname}
%license LICENSES/*
%{_kf5_libdir}/libKF5Kirigami2.so.*

%files devel
%license LICENSES/*
%dir %{_kf5_includedir}/Kirigami2/
%{_kf5_includedir}/Kirigami2/*
%{_kf5_libdir}/libKF5Kirigami2.so
%{_kf5_mkspecsdir}/qt_Kirigami2.pri
%{_libdir}/cmake/KF5Kirigami2/

%changelog
