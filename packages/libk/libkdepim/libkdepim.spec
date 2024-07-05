#
# spec file for package libkdepim
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
Name:           libkdepim
Version:        24.05.2
Release:        0
Summary:        Base package of kdepim
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
This package contains the libkdepim library.

%package -n libKPim6Libkdepim6
Summary:        libkdepim library
Requires:       libkdepim >= %{version}

%description -n libKPim6Libkdepim6
The libkdepim library

%package devel
Summary:        Development package for libkdepim
Requires:       libKPim6Libkdepim6 = %{version}

%description devel
The development package for the libkdepim libraries

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libKPim6Libkdepim6

%files
%{_kf6_debugdir}/libkdepim.categories
%{_kf6_debugdir}/libkdepim.renamecategories

%files -n libKPim6Libkdepim6
%license LICENSES/*
%{_kf6_libdir}/libKPim6Libkdepim.so.*

%files devel
%doc %{_kf6_qchdir}/KPim6Libkdepim.*
%{_includedir}/KPim6/Libkdepim/
%{_kf6_cmakedir}/KPim6Libkdepim/
%{_kf6_cmakedir}/KPim6MailTransportDBusService/
%{_kf6_dbusinterfacesdir}/org.kde.addressbook.service.xml
%{_kf6_dbusinterfacesdir}/org.kde.mailtransport.service.xml
%{_kf6_libdir}/libKPim6Libkdepim.so
%dir %{_kf6_plugindir}/designer/
%{_kf6_plugindir}/designer/kdepim6widgets.so

%files lang -f %{name}.lang

%changelog
