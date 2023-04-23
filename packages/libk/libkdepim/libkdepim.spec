#
# spec file for package libkdepim
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
Name:           libkdepim
Version:        23.04.0
Release:        0
Summary:        Base package of kdepim
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KPim5Akonadi)
BuildRequires:  cmake(KPim5AkonadiContact)
BuildRequires:  cmake(KPim5AkonadiSearch)
BuildRequires:  cmake(KPim5Ldap)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(Qt5Widgets)
Conflicts:      libKF5Libkdepim5 < %{version}

%description
This package contains the libkdepim library.

%package -n libKPim5Libkdepim5
Summary:        libkdepim library
License:        LGPL-2.1-or-later
Requires:       libkdepim >= %{version}

%description -n libKPim5Libkdepim5
The libkdepim library

%package -n libKPim5LibkdepimAkonadi5
Summary:        libkdepim Akonadi library
License:        LGPL-2.1-or-later
Requires:       libkdepim >= %{version}

%description -n libKPim5LibkdepimAkonadi5
The libkdepim library for Akonadi related functions

%package devel
Summary:        Development package for libkdepim
License:        LGPL-2.1-or-later
# For the DBus interfaces
Requires:       libkdepim >= %{version}
Requires:       libKPim5Libkdepim5 = %{version}
Requires:       cmake(KPim5Akonadi)
Requires:       cmake(KPim5AkonadiContact)

%description devel
The development package for the libkdepim libraries

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%ldconfig_scriptlets -n libKPim5Libkdepim5
%ldconfig_scriptlets -n libKPim5LibkdepimAkonadi5

%files
%license LICENSES/*
%{_kf5_dbusinterfacesdir}/org.kde.addressbook.service.xml
%{_kf5_dbusinterfacesdir}/org.kde.mailtransport.service.xml
%{_kf5_debugdir}/libkdepim.categories
%{_kf5_debugdir}/libkdepim.renamecategories
%{_kf5_plugindir}/designer/

%files -n libKPim5Libkdepim5
%{_kf5_libdir}/libKPim5Libkdepim.so.*

%files devel
%dir %{_includedir}/KPim5
%{_includedir}/KPim5/Libkdepim/
%{_kf5_cmakedir}/KF5Libkdepim/
%{_kf5_cmakedir}/KPim5Libkdepim/
%{_kf5_cmakedir}/KPim5MailTransportDBusService/
%{_kf5_cmakedir}/MailTransportDBusService/
%{_kf5_libdir}/libKPim5Libkdepim.so
%{_kf5_mkspecsdir}/qt_Libkdepim.pri

%files lang -f %{name}.lang

%changelog
