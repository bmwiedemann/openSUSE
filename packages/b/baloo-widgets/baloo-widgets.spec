#
# spec file for package baloo-widgets
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

%define rname baloo-widgets
%bcond_without released
Name:           baloo-widgets
Version:        24.05.2
Release:        0
Summary:        Framework for searching and managing metadata
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Source99:       baloo-widgets-rpmlintrc
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Baloo) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6FileMetaData) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
# Due to the binary it can't be SLPP compliant currently,
# but only the latest version should be needed.
Obsoletes:      libKF5BalooWidgets5 < %{version}
Obsoletes:      libKF6BalooNaturalQueryParser1 < %{version}
Obsoletes:      baloo5-widgets < %{version}
Obsoletes:      baloo5-widgets-lang < %{version}

%description
Baloo is a framework for searching and managing metada

%package devel
Summary:        Development package for baloo-widgets
Requires:       baloo-widgets = %{version}
Requires:       cmake(KF6KIO) >= %{kf6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}

%description devel
Development package for baloo-widgets

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets

%files
%license LICENSES/*
%{_kf6_bindir}/baloo_filemetadata_temp_extractor
%{_kf6_debugdir}/baloo-widgets.categories
%{_kf6_libdir}/libKF6BalooWidgets.so.*
%dir %{_kf6_plugindir}/kf6/propertiesdialog
%{_kf6_plugindir}/kf6/propertiesdialog/baloofilepropertiesplugin.so
%dir %{_kf6_plugindir}/kf6/kfileitemaction
%{_kf6_plugindir}/kf6/kfileitemaction/tagsfileitemaction.so

%files devel
%{_kf6_cmakedir}/KF6BalooWidgets/
%{_kf6_includedir}/BalooWidgets/
%{_kf6_libdir}/libKF6BalooWidgets.so

%files lang -f %{name}.lang

%changelog
