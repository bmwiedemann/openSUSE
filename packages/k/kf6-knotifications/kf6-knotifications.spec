#
# spec file for package kf6-knotifications
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


%define qt6_version 6.8.0

%define rname knotifications

%bcond_without kde_python_bindings
%if %{with kde_python_bindings}
%if 0%{suse_version} > 1500
%define pythons %{primary_python}
%else
%{?sle15_python_module_pythons}
%endif
%define mypython %pythons
%define __mypython %{expand:%%__%{mypython}}
%define mypython_sitearch %{expand:%%%{mypython}_sitearch}
%endif

# Full KF6 version (e.g. 6.21.0)
%{!?_kf6_version: %global _kf6_version %{version}}
%bcond_without released
Name:           kf6-knotifications
Version:        6.21.0
Release:        0
Summary:        KDE Desktop notifications
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Config) >= %{_kf6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(libcanberra)
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
KNotification is used to notify the user of an event. It covers feedback and
persistent events.

%package imports
Summary:        KDE Desktop notifications - QML files

%description imports
KNotification is used to notify the user of an event. It covers feedback and
persistent events.
This package contains files that allow using knotification in QtQuick based
applications.

%package -n libKF6Notifications6
Summary:        KDE Desktop notifications
Requires:       kf6-knotifications >= %{version}

%description -n libKF6Notifications6
KNotification is used to notify the user of an event. It covers feedback and
persistent events.

%package devel
Summary:        KDE Desktop notifications: Build Environment
Requires:       libKF6Notifications6 = %{version}
Requires:       cmake(Qt6DBus) >= %{qt6_version}
Requires:       cmake(Qt6Gui) >= %{qt6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}

%description devel
KNotification is used to notify the user of an event. It covers feedback and
persistent events. Development files.

%if %{with kde_python_bindings}
%package -n python3-kf6-knotifications
Summary:        Python interface for kf6-knotifications

%description -n python3-kf6-knotifications
This package provides a python interface for kf6-knotifications.
%endif

%lang_package -n libKF6Notifications6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 \
%if %{with kde_python_bindings}
  -DPython_EXECUTABLE:STRING=%{__mypython}
%endif
%{nil}

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang knotifications6 --with-qt --without-mo

%ldconfig_scriptlets -n libKF6Notifications6

%files -n libKF6Notifications6-lang -f knotifications6.lang

%files
%{_kf6_debugdir}/knotifications.categories
%{_kf6_debugdir}/knotifications.renamecategories

%files imports
%{_kf6_qmldir}/org/kde/notification/

%files -n libKF6Notifications6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6Notifications.so.*

%files devel
%{_kf6_cmakedir}/KF6Notifications/
%{_kf6_includedir}/KNotifications/
%{_kf6_libdir}/libKF6Notifications.so

%if %{with kde_python_bindings}
%files -n python3-kf6-knotifications
%{mypython_sitearch}/*.so
%endif

%changelog
