#
# spec file for package kf6-knewstuff
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


%define qt6_version 6.6.0

%define rname knewstuff
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-knewstuff
Version:        6.3.0
Release:        0
Summary:        Framework for downloading and sharing additional application data
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Archive) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Attica) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Package) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Syndication) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiPlugin) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}

%description
The KNewStuff library implements collaborative data sharing for
applications. It uses libattica to support the Open Collaboration Services
specification.

%package -n libKF6NewStuffCore6
Summary:        Framework for downloading and sharing additional application data
Requires:       kf6-knewstuff >= %{version}

%description -n libKF6NewStuffCore6
The KNewStuff library implements collaborative data sharing for
applications. It uses libattica to support the Open Collaboration Services
specification.

%package -n libKF6NewStuffWidgets6
Summary:        Framework for downloading and sharing additional application data

%description -n libKF6NewStuffWidgets6
The KNewStuff library implements collaborative data sharing for
applications. It uses libattica to support the Open Collaboration Services
specification.

%package imports
Summary:        Framework for downloading and sharing additional application data
Requires:       kf6-kirigami-imports >= %{_kf6_bugfix_version}

%description imports
The KNewStuff library implements collaborative data sharing for
applications. It uses libattica to support the Open Collaboration Services
specification.

%package core-devel
Summary:        Framework for downloading and sharing additional application data
Requires:       libKF6NewStuffCore6 = %{version}
Requires:       cmake(KF6Attica) >= %{_kf6_bugfix_version}
Requires:       cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}

%description core-devel
The KNewStuff library implements collaborative data sharing for
applications. It uses libattica to support the Open Collaboration Services
specification. Development files.

%package devel
Summary:        Framework for downloading and sharing additional application data
Requires:       kf6-knewstuff-core-devel = %{version}
Requires:       libKF6NewStuffWidgets6 = %{version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}

%description devel
The KNewStuff library implements collaborative data sharing for
applications. It uses libattica to support the Open Collaboration Services
specification. Development files.

%lang_package -n libKF6NewStuffCore6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang knewstuff6

%ldconfig_scriptlets -n libKF6NewStuffCore6
%ldconfig_scriptlets -n libKF6NewStuffWidgets6

%files
%{_kf6_applicationsdir}/org.kde.knewstuff-dialog6.desktop
%{_kf6_bindir}/knewstuff-dialog6
%{_kf6_debugdir}/knewstuff.categories
%{_kf6_debugdir}/knewstuff.renamecategories

%files -n libKF6NewStuffCore6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6NewStuffCore.so.*

%files -n libKF6NewStuffWidgets6
%{_kf6_libdir}/libKF6NewStuffWidgets.so.*

%files imports
%{_kf6_qmldir}/org/kde/newstuff/

%files core-devel
%doc %{_kf6_qchdir}/KF6NewStuffCore.*
%{_kf6_includedir}/KNewStuffCore/
%{_kf6_cmakedir}/KF6NewStuffCore/
%{_kf6_libdir}/libKF6NewStuffCore.so

%files devel
%doc %{_kf6_qchdir}/KF6NewStuffWidgets.*
%{_kf6_cmakedir}/KF6NewStuff/
%{_kf6_includedir}/KNewStuff/
%{_kf6_includedir}/KNewStuffWidgets/
%{_kf6_libdir}/libKF6NewStuffWidgets.so
%{_kf6_plugindir}/designer/knewstuff6widgets.so

%files -n libKF6NewStuffCore6-lang -f knewstuff6.lang

%changelog
