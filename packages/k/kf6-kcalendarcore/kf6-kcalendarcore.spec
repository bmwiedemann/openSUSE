#
# spec file for package kf6-kcalendarcore
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define qt6_version 6.9.0

%define sonum 6
%define rname kcalendarcore

%bcond_without kde_python_bindings
%if %{with kde_python_bindings}
%define pythons %{primary_python}
%define mypython %pythons
%define __mypython %{expand:%%__%{mypython}}
%define mypython_sitearch %{expand:%%%{mypython}_sitearch}
%endif

# Full KF6 version (e.g. 6.27.0)
%{!?_kf6_version: %global _kf6_version %{version}}
%bcond_without released
Name:           kf6-kcalendarcore
Version:        6.27.0
Release:        0
Summary:        Library to access and handle calendar data
License:        LGPL-2.0-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(LibIcal) >= 3.0
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
# SECTION bindings
%if %{with kde_python_bindings}
BuildRequires:  %{mypython}-build
BuildRequires:  %{mypython}-devel >= 3.9
BuildRequires:  %{mypython}-setuptools
BuildRequires:  %{mypython}-wheel
BuildRequires:  cmake(Shiboken6)
BuildRequires:  cmake(PySide6)
%endif
# /SECTION

%description
KCalendarCore is a library to provide access to and handling of calendar data.
It supports the standard formats iCalendar and vCalendar and the group
scheduling standard iTIP.

%package -n libKF6CalendarCore%{sonum}
Summary:        Library to access to and handle calendar data

%description  -n libKF6CalendarCore%{sonum}
KCalendarCore is a library to provide access to and handling of calendar data.
It supports the standard formats iCalendar and vCalendar and the group
scheduling standard iTIP.

%package imports 
Summary:        Library to access to and handle calendar data - QtQuick bindings
Requires:       libKF6CalendarCore%{sonum} = %{version}

%description imports
KCalendarCore is a library to provide access to and handling of calendar data.
It supports the standard formats iCalendar and vCalendar and the group
scheduling standard iTIP. This package provides QtQuick bindings for KCalendarCore,
allowing its use from QML.

%package devel
Summary:        Development files for kcalendarcore, a library to handle calendar data
Requires:       libKF6CalendarCore%{sonum} = %{version}
Requires:       cmake(LibIcal) >= 3.0

%description devel
KCalendarCore is a library to provide access to and handling of calendar data.
It supports the standard formats iCalendar and vCalendar and the group
scheduling standard iTIP. This package contains the headers necessary to
develop applications making use of KCalendarCore.

%if %{with kde_python_bindings}
%package -n python3-kf6-kcalendarcore
Summary:        Python bindings for kf6-kcalendarcore

%description -n python3-kf6-kcalendarcore
This package provides Python bindings for kf6-kcalendarcore.
%endif

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%ifarch ppc64
%define _lto_cflags %{nil}
%endif

%cmake_kf6 \
%if %{with kde_python_bindings}
  -DPython_EXECUTABLE:STRING=%{__mypython}
%endif
%{nil}

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}%{_kf6_includedir}

%ldconfig_scriptlets -n libKF6CalendarCore%{sonum}

%files -n libKF6CalendarCore%{sonum}
%license LICENSES/*
%doc README.md
%{_kf6_debugdir}/kcalendarcore.categories
%{_kf6_debugdir}/kcalendarcore.renamecategories
%{_kf6_libdir}/libKF6CalendarCore.so.*

%files imports
%{_kf6_qmldir}/org/kde/calendarcore

%files devel
%{_kf6_cmakedir}/KF6CalendarCore/
%{_kf6_includedir}/KCalendarCore/
%{_kf6_libdir}/libKF6CalendarCore.so
%{_kf6_pkgconfigdir}/KF6CalendarCore.pc
%if %{with kde_python_bindings}
%dir %{_includedir}/PySide6/
%{_includedir}/PySide6/KCalendarCore/
%endif

%if %{with kde_python_bindings}
%files -n python3-kf6-kcalendarcore
%{mypython_sitearch}/*.so
%{_kf6_sharedir}/PySide6/typesystems/typesystem_kcalendarcore.xml
%endif

%changelog
