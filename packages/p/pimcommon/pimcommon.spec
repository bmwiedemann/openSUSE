#
# spec file for package pimcommon
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
Name:           pimcommon
Version:        24.05.1
Release:        0
Summary:        Base package of KDE PIM PimCommon library
License:        GPL-2.0-only AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
# For xsltproc
BuildRequires:  libxslt-tools
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6Contacts) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Purpose) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6TextAddonsWidgets)
BuildRequires:  cmake(KF6TextAutoCorrectionWidgets)
BuildRequires:  cmake(KF6TextCustomEditor)
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KPim6Akonadi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiContactWidgets) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiSearch) >= %{kpim6_version}
BuildRequires:  cmake(KPim6IMAP) >= %{kpim6_version}
BuildRequires:  cmake(KPim6LdapWidgets) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Libkdepim) >= %{kpim6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiPlugin) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}

%description
This package contains the pimcommon library, used by several KDE PIM
applications.

%package devel
Summary:        Development package for pimcommon
License:        LGPL-2.1-or-later
Requires:       libKPim6PimCommon6 = %{version}
Requires:       libKPim6PimCommonAkonadi6 = %{version}
Requires:       cmake(KF6Config) >= %{kf6_version}
Requires:       cmake(KF6Contacts) >= %{kf6_version}
Requires:       cmake(KF6KIO) >= %{kf6_version}
Requires:       cmake(KF6TextAutoCorrectionWidgets)
Requires:       cmake(KF6TextCustomEditor)
Requires:       cmake(KPim6Akonadi) >= %{kpim6_version}
Requires:       cmake(KPim6AkonadiContactWidgets) >= %{kpim6_version}
Requires:       cmake(KPim6IMAP) >= %{kpim6_version}
Requires:       cmake(KPim6Libkdepim) >= %{kpim6_version}
Requires:       cmake(Qt6DBus) >= %{qt6_version}
Requires:       cmake(Qt6Gui) >= %{qt6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}

%description devel
The development package for the pimcommon libraries

%package -n libKPim6PimCommon6
Summary:        The PimCommon Library
License:        LGPL-2.1-or-later
Requires:       pimcommon >= %{version}
Obsoletes:      libKF5PimCommon5 < %{version}
Obsoletes:      libKPim5PimCommon5 < %{version}

%description -n libKPim6PimCommon6
The PimCommon library

%package -n libKPim6PimCommonAkonadi6
Summary:        The PimCommon Akonadi Library
License:        LGPL-2.1-or-later
Requires:       pimcommon >= %{version}
Obsoletes:      libKF5PimCommonAkonadi5 < %{version}
Obsoletes:      libKPim5PimCommonAkonadi5 < %{version}

%description -n libKPim6PimCommonAkonadi6
The PimCommon Akonadi library

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libKPim6PimCommon6
%ldconfig_scriptlets -n libKPim6PimCommonAkonadi6

%files
%{_kf6_debugdir}/pimcommon.categories
%{_kf6_debugdir}/pimcommon.renamecategories

%files -n libKPim6PimCommon6
%license LICENSES/*
%{_kf6_libdir}/libKPim6PimCommon.so.*

%files -n libKPim6PimCommonAkonadi6
%{_kf6_libdir}/libKPim6PimCommonAkonadi.so.*

%files devel
%doc %{_kf6_qchdir}/KPim6PimCommon*.*
%{_includedir}/KPim6/PimCommon/
%{_includedir}/KPim6/PimCommonAkonadi/
%{_kf6_cmakedir}/KPim6PimCommon/
%{_kf6_cmakedir}/KPim6PimCommonAkonadi/
%{_kf6_libdir}/libKPim6PimCommon.so
%{_kf6_libdir}/libKPim6PimCommonAkonadi.so
%{_kf6_plugindir}/designer/

%files lang -f %{name}.lang

%changelog
