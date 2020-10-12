#
# spec file for package kparts
#
# Copyright (c) 2020 SUSE LLC
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


%define lname   libKF5Parts5
%define _tar_path 5.75
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kparts
Version:        5.75.0
Release:        0
Summary:        Plugin framework for user interface components
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Bookmarks) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Completion) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5ConfigWidgets) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5GuiAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5IconThemes) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5ItemViews) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5KIO) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Service) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Solid) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5TextWidgets) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5XmlGui) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5Core) >= 5.12.0
BuildRequires:  cmake(Qt5Network) >= 5.12.0
BuildRequires:  cmake(Qt5Test) >= 5.12.0
BuildRequires:  cmake(Qt5Widgets) >= 5.12.0
BuildRequires:  cmake(Qt5Xml) >= 5.12.0

%description
This library implements the framework for KDE parts, which are
elaborate widgets with a user-interface defined in terms of actions
(menu items, toolbar icons).

%package -n %{lname}
Summary:        Plugin framework for user interface components
Group:          System/GUI/KDE
Obsoletes:      libKF5Parts4
%if %{with lang}
Recommends:     %{lname}-lang = %{version}
%endif

%description -n %{lname}
This library implements the framework for KDE parts, which are
elaborate widgets with a user-interface defined in terms of actions
(menu items, toolbar icons).

%package devel
Summary:        Plugin framework for user interface components
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(KF5KIO) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5TextWidgets) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5XmlGui) >= %{_kf5_bugfix_version}

%description devel
This library implements the framework for KDE parts, which are
elaborate widgets with a user-interface defined in terms of actions
(menu items, toolbar icons). Development files.

%lang_package -n %{lname}

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %fdupes %{buildroot}

%if %{with lang}
%find_lang %{name}5
%endif

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%if %{with lang}
%files -n %{lname}-lang -f %{name}5.lang
%endif

%files -n %{lname}
%license LICENSES/*
%dir %{_kf5_servicetypesdir}
%{_kf5_debugdir}/kparts.categories
%{_kf5_libdir}/libKF5Parts.so.*
%{_kf5_servicetypesdir}/browserview.desktop
%{_kf5_servicetypesdir}/kpart.desktop
%{_kf5_servicetypesdir}/kparts-readonlypart.desktop
%{_kf5_servicetypesdir}/kparts-readwritepart.desktop

%files devel
%dir %{_kf5_includedir}/*/
%dir %{_kf5_sharedir}/kdevappwizard
%{_kf5_includedir}/*.h
%{_kf5_includedir}/*/
%{_kf5_libdir}/cmake/KF5Parts/
%{_kf5_libdir}/libKF5Parts.so
%{_kf5_mkspecsdir}/qt_KParts.pri
%{_kf5_sharedir}/kdevappwizard/templates/

%changelog
