#
# spec file for package ktnef
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
%define kpim6_version 6.1.2

%bcond_without released
Name:           ktnef
Version:        24.05.2
Release:        0
Summary:        TNEF support
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6CalendarCore) >= %{kf6_version}
BuildRequires:  cmake(KF6Contacts) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KPim6CalendarUtils) >= %{kpim6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
Library to work with TNEF Email Attachments.

# A ktnef subpackage is already created by kmail.spec, we need a different name
# for debug categories
%package debug-categories
Summary:        Debug categories files needed by libKPim6Tnef6

%description debug-categories
Debug categories files needed by libKPim6Tnef6.

%package -n libKPim6Tnef6
Summary:        TNEF Support
Requires:       ktnef-debug-categories >= %{version}
Obsoletes:      libKF5Tnef5 < %{version}
Obsoletes:      libKPim5Tnef5 < %{version}
Obsoletes:      libKPim5Tnef5-lang < %{version}

%description  -n libKPim6Tnef6
Library to work with TNEF Email Attachments.

%package devel
Summary:        Development files for ktnef
Requires:       libKPim6Tnef6 = %{version}
Requires:       cmake(KF6CalendarCore) >= %{kf6_version}

%description devel
Development files for ktnef.

%lang_package -n libKPim6Tnef6

%prep
%autosetup -p1 -n ktnef-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libKPim6Tnef6

%files debug-categories
%{_kf6_debugdir}/ktnef.categories
%{_kf6_debugdir}/ktnef.renamecategories

%files -n libKPim6Tnef6
%license LICENSES/*
%{_kf6_libdir}/libKPim6Tnef.so.*

%files devel
%doc %{_kf6_qchdir}/KPim6Tnef.*
%{_includedir}/KPim6/KTNEF/
%{_kf6_cmakedir}/KPim6Tnef/
%{_kf6_libdir}/libKPim6Tnef.so

%files -n libKPim6Tnef6-lang -f %{name}.lang

%changelog
