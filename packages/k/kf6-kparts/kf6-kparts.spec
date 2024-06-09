#
# spec file for package kf6-kparts
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

%define rname kparts
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kparts
Version:        6.3.0
Release:        0
Summary:        Plugin framework for user interface components
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
BuildRequires:  cmake(KF6Config) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6KIO) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Service) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6XmlGui) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}

%description
This library implements the framework for KDE parts, which are
elaborate widgets with a user-interface defined in terms of actions
(menu items, toolbar icons).

%package -n libKF6Parts6
Summary:        Plugin framework for user interface components
Requires:       kf6-kparts >= %{version}

%description -n libKF6Parts6
This library implements the framework for KDE parts, which are
elaborate widgets with a user-interface defined in terms of actions
(menu items, toolbar icons).

%package devel
Summary:        Plugin framework for user interface components
Requires:       libKF6Parts6 = %{version}
Requires:       cmake(KF6KIO) >= %{_kf6_bugfix_version}
Requires:       cmake(KF6Service) >= %{_kf6_bugfix_version}
Requires:       cmake(KF6TextWidgets) >= %{_kf6_bugfix_version}
Requires:       cmake(KF6XmlGui) >= %{_kf6_bugfix_version}

%description devel
This library implements the framework for KDE parts, which are
elaborate widgets with a user-interface defined in terms of actions
(menu items, toolbar icons). Development files.

%lang_package -n libKF6Parts6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kparts6

%ldconfig_scriptlets -n libKF6Parts6

%files
%{_kf6_debugdir}/kparts.categories

%files -n libKF6Parts6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6Parts.so.*

%files devel
%doc %{_kf6_qchdir}/KF6Parts.*
%{_kf6_cmakedir}/KF6Parts/
%{_kf6_includedir}/KParts/
%{_kf6_libdir}/libKF6Parts.so
%{_kf6_sharedir}/kdevappwizard/templates/

%files -n libKF6Parts6-lang -f kparts6.lang

%changelog
