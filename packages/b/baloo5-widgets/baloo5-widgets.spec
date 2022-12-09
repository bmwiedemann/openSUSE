#
# spec file for package baloo5-widgets
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


%define rname baloo-widgets
%define kf5_version 5.90.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           baloo5-widgets
Version:        22.12.0
Release:        0
Summary:        Framework for searching and managing metadata
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Source99:       baloo5-widgets-rpmlintrc
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Baloo)
BuildRequires:  cmake(KF5FileMetaData)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
Obsoletes:      libKF5BalooWidgets5
Provides:       libKF5BalooNaturalQueryParser1 = %{version}
Obsoletes:      libKF5BalooNaturalQueryParser1 < %{version}

%description
Baloo is a framework for searching and managing metada

%package devel
Summary:        Development package for baloo5-widgets
Requires:       %{name} = %{version}
Requires:       cmake(KF5KIO)
Requires:       cmake(Qt5Widgets)
Provides:       baloo-widgets5-devel
Obsoletes:      baloo-widgets5-devel

%description devel
Development package for baloo5-widgets

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES/*
%dir %{_kf5_plugindir}/kf5/
%dir %{_kf5_plugindir}/kf5/kfileitemaction
%dir %{_kf5_plugindir}/kf5/propertiesdialog
%{_kf5_bindir}/baloo_filemetadata_temp_extractor
%{_kf5_debugdir}/baloo-widgets.categories
%{_kf5_libdir}/libKF5BalooWidgets.so.*
%{_kf5_plugindir}/kf5/propertiesdialog/baloofilepropertiesplugin.so
%{_kf5_plugindir}/kf5/kfileitemaction/tagsfileitemaction.so

%files devel
%{_kf5_cmakedir}/KF5BalooWidgets/
%{_kf5_includedir}/
%{_kf5_libdir}/libKF5BalooWidgets.so

%files lang -f %{name}.lang

%changelog
