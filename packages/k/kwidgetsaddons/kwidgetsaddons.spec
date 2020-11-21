#
# spec file for package kwidgetsaddons
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


%define lname   libKF5WidgetsAddons5
%define _tar_path 5.75
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kwidgetsaddons
Version:        5.75.0
Release:        0
Summary:        Large set of desktop widgets
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
BuildRequires:  cmake(Qt5Test) >= 5.12.0
BuildRequires:  cmake(Qt5UiPlugin) >= 5.12.0
BuildRequires:  cmake(Qt5UiTools) >= 5.12.0
BuildRequires:  cmake(Qt5Widgets) >= 5.12.0
%if %{with lang}
BuildRequires:  cmake(Qt5LinguistTools) >= 5.12.0
%endif

%description
This repository contains add-on widgets and classes for applications
that use the Qt Widgets module. If you are porting applications from
KDE Platform 4 "kdeui" library, you will find many of its classes here.

%package -n %{lname}
Summary:        Large set of desktop widgets
Group:          System/GUI/KDE
%requires_ge    libQt5Widgets5
Obsoletes:      libKF5WidgetsAddons4
%if %{with lang}
Recommends:     %{lname}-lang = %{version}
%endif

%description -n %{lname}
This repository contains add-on widgets and classes for applications
that use the Qt Widgets module. If you are porting applications from
KDE Platform 4 "kdeui" library, you will find many of its classes here.

%package devel
Summary:        Large set of desktop widgets: Build Environment
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(Qt5Widgets) >= 5.12.0

%description devel
This repository contains add-on widgets and classes for applications
that use the Qt Widgets module. If you are porting applications from
KDE Platform 4 "kdeui" library, you will find many of its classes here.
Development files.

%lang_package -n %{lname}

%prep
%setup -q

%build
  %cmake_kf5 -d build -- -Dlconvert_executable=%{_kf5_libdir}/qt5/bin/lconvert
  %cmake_build

%install
  %kf5_makeinstall -C build
  %fdupes %{buildroot}

%if %{with lang}
%find_lang %{name}5 --with-qt --without-mo
%endif

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%if %{with lang}
%files -n %{lname}-lang -f %{name}5.lang
%endif

%files -n %{lname}
%license LICENSES/*
%doc README*
%{_kf5_datadir}/kcharselect/
%{_kf5_libdir}/libKF5WidgetsAddons.so.*
%{_kf5_debugdir}/kwidgetsaddons.categories

%files devel
%{_kf5_libdir}/libKF5WidgetsAddons.so
%{_kf5_libdir}/cmake/KF5WidgetsAddons/
%{_kf5_includedir}/
%dir %{_kf5_plugindir}/designer
%{_kf5_plugindir}/designer/kwidgetsaddons5widgets.so
%{_kf5_mkspecsdir}/qt_KWidgetsAddons.pri

%changelog
