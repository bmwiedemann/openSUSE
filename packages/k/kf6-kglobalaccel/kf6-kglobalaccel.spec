#
# spec file for package kf6-kglobalaccel
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

%define rname kglobalaccel
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kglobalaccel
Version:        6.3.0
Release:        0
Summary:        Global desktop keyboard shortcuts
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
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake(KF6Config) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Crash) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)

%description
KGlobalAccel allows you to have global accelerators that are independent of
the focused window.  Unlike regular shortcuts, the application's window does not
need focus for them to be activated.

%package -n libKF6GlobalAccel6
Summary:        Global desktop keyboard shortcuts
Requires:       kf6-kglobalaccel >= %{version}

%description -n libKF6GlobalAccel6
KGlobalAccel allows you to have global accelerators that are independent of
the focused window.  Unlike regular shortcuts, the application's window does not
need focus for them to be activated.

%package devel
Summary:        Global desktop keyboard shortcuts: Build Environment
Requires:       libKF6GlobalAccel6 = %{version}
Requires:       cmake(Qt6DBus) >= %{qt6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}

%description devel
KGlobalAccel allows you to have global accelerators that are independent of
the focused window.  Unlike regular shortcuts, the application's window does not
need focus for them to be activated. Development files.

%lang_package -n libKF6GlobalAccel6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kglobalaccel6 --with-qt --without-mo

%ldconfig_scriptlets -n libKF6GlobalAccel6

%files
%{_kf6_debugdir}/kglobalaccel.categories
%{_kf6_debugdir}/kglobalaccel.renamecategories

%files -n libKF6GlobalAccel6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6GlobalAccel.so.*

%files devel
%doc %{_kf6_qchdir}/KF6GlobalAccel.*
%{_kf6_libdir}/libKF6GlobalAccel.so
%{_kf6_cmakedir}/KF6GlobalAccel/
%{_kf6_includedir}/KGlobalAccel/
%{_kf6_dbusinterfacesdir}/kf6_org.kde.KGlobalAccel.xml
%{_kf6_dbusinterfacesdir}/kf6_org.kde.kglobalaccel.Component.xml

%files -n libKF6GlobalAccel6-lang -f kglobalaccel6.lang

%changelog
