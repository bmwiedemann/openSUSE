#
# spec file for package libgravatar
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
%define kpim6_version 6.1.1

%bcond_without released
Name:           libgravatar
Version:        24.05.1
Release:        0
Summary:        Library to download and display gravatars
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KPim6PimCommon) >= %{kpim6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
This package contains the debug categories for the libgravatar library.

%package -n libKPim6Gravatar6
Summary:        Libgravatar library for KDE PIM applications
Requires:       libgravatar
Obsoletes:      libKF5Gravatar5 < %{version}
Obsoletes:      libKPim5Gravatar5 < %{version}
# Renamed
Obsoletes:      libgravatar-lang <= 23.04.0

%description -n libKPim6Gravatar6
libgravatar adds support for downloading and displaying gravatars in
applications.

%package devel
Summary:        Development package for libgravatar
Requires:       libKPim6Gravatar6 = %{version}

%description devel
The development package for the libgravatar library.

%lang_package -n libKPim6Gravatar6

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang libKPim6Gravatar6 --all-name

%ldconfig_scriptlets -n libKPim6Gravatar6

%files
%{_kf6_debugdir}/libgravatar.categories
%{_kf6_debugdir}/libgravatar.renamecategories

%files -n libKPim6Gravatar6
%license LICENSES/*
%{_libdir}/libKPim6Gravatar.so.*

%files devel
%doc %{_kf6_qchdir}/KPim6Gravatar.*
%{_includedir}/KPim6/Gravatar/
%{_kf6_cmakedir}/KPim6Gravatar/
%{_kf6_libdir}/libKPim6Gravatar.so

%files -n libKPim6Gravatar6-lang -f libKPim6Gravatar6.lang

%changelog
