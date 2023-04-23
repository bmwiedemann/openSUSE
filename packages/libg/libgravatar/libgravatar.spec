#
# spec file for package libgravatar
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


%bcond_without released
%define libname libKPim5Gravatar5
Name:           libgravatar
Version:        23.04.0
Release:        0
Summary:        Library to download and display gravatars
License:        GPL-2.0-only AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5PimCommon)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)

%description
This package contains the debug categories for the libgravatar library.

%package -n %{libname}
Summary:        Libgravatar library for KDE PIM applications
License:        LGPL-2.1-or-later
Requires:       libgravatar
# Renamed
Obsoletes:      libgravatar-lang <= 23.04.0

%description -n %{libname}
libgravatar adds support for downloading and displaying gravatars in
applications.

%package devel
Summary:        Development package for libgravatar
License:        LGPL-2.1-or-later
Requires:       %{libname} = %{version}

%description devel
The development package for the libgravatar library.

%lang_package -n %{libname}

%prep
%autosetup -p1

%build
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{libname} --with-man --all-name

%ldconfig_scriptlets -n %{libname}

%files
%{_kf5_debugdir}/libgravatar.categories
%{_kf5_debugdir}/libgravatar.renamecategories

%files -n %{libname}
%license LICENSES/*
%{_libdir}/libKPim5Gravatar.so.*

%files devel
%dir %{_includedir}/KPim5
%{_includedir}/KPim5/Gravatar/
%{_kf5_cmakedir}/KF5Gravatar/
%{_kf5_cmakedir}/KPim5Gravatar/
%{_kf5_libdir}/libKPim5Gravatar.so
%{_kf5_mkspecsdir}/qt_Gravatar.pri

%files -n %{libname}-lang -f %{libname}.lang

%changelog
