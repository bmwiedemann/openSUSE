#
# spec file for package kglobalaccel
#
# Copyright (c) 2022 SUSE LLC
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


%define lname   libKF5GlobalAccel5
%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kglobalaccel
Version:        5.101.0
Release:        0
Summary:        Global desktop keyboard shortcuts
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  libxcb-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake(KF5Config) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Crash) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5DBus) >= 5.15.0
BuildRequires:  cmake(Qt5LinguistTools) >= 5.15.0
BuildRequires:  cmake(Qt5Test) >= 5.15.0
BuildRequires:  cmake(Qt5Widgets) >= 5.15.0
BuildRequires:  cmake(Qt5X11Extras) >= 5.15.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb-keysyms)

%description
KGlobalAccel allows you to have global accelerators that are independent of
the focused window.  Unlike regular shortcuts, the application's window does not
need focus for them to be activated.

%package -n %{lname}
Summary:        Global desktop keyboard shortcuts
%requires_ge    libQt5DBus5
%requires_ge    libQt5Widgets5
Recommends:     kglobalaccel5

%description -n %{lname}
KGlobalAccel allows you to have global accelerators that are independent of
the focused window.  Unlike regular shortcuts, the application's window does not
need focus for them to be activated.

%package -n libKF5GlobalAccelPrivate5
Summary:        Global desktop keyboard shortcuts

%description -n libKF5GlobalAccelPrivate5
KGlobalAccel allows you to have global accelerators that are independent of
the focused window.  Unlike regular shortcuts, the application's window does not
need focus for them to be activated.

%package devel
Summary:        Global desktop keyboard shortcuts: Build Environment
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       libKF5GlobalAccelPrivate5 = %{version}
Requires:       cmake(Qt5DBus) >= 5.15.0
Requires:       cmake(Qt5Widgets) >= 5.15.0

%description devel
KGlobalAccel allows you to have global accelerators that are independent of
the focused window.  Unlike regular shortcuts, the application's window does not
need focus for them to be activated. Development files.

%package -n kglobalaccel5
Summary:        Configurable global shortcut support

%description -n kglobalaccel5
KGlobalAccel allows you to have global accelerators that are independent
of the focused window. Unlike regular shortcuts, the application's window
does not need focus for them to be activated.

%lang_package -n %{lname}

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -Dlconvert_executable=%{_kf5_libdir}/qt5/bin/lconvert
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%find_lang kglobalaccel5 --with-qt --without-mo

%post -n kglobalaccel5
%{systemd_user_post plasma-kglobalaccel.service}

%preun -n kglobalaccel5
%{systemd_user_preun}

%postun -n kglobalaccel5
%{systemd_user_postun}

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig
%post -n libKF5GlobalAccelPrivate5 -p /sbin/ldconfig
%postun -n libKF5GlobalAccelPrivate5 -p /sbin/ldconfig

%files -n %{lname}-lang -f kglobalaccel5.lang

%files -n %{lname}
%license LICENSES/*
%doc README*
%{_kf5_libdir}/libKF5GlobalAccel.so.*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories

%files -n libKF5GlobalAccelPrivate5
%{_kf5_libdir}/libKF5GlobalAccelPrivate.so.*

%files devel
%{_kf5_libdir}/libKF5GlobalAccel.so
%{_kf5_libdir}/cmake/KF5GlobalAccel/
%{_kf5_includedir}/
%{_kf5_dbusinterfacesdir}/kf5_org.kde.KGlobalAccel.xml
%{_kf5_dbusinterfacesdir}/kf5_org.kde.kglobalaccel.Component.xml
%{_kf5_mkspecsdir}/qt_KGlobalAccel.pri

%files -n kglobalaccel5
%{_kf5_bindir}/kglobalaccel5
%dir %{_kf5_plugindir}/org.kde.kglobalaccel5.platforms
%{_kf5_plugindir}/org.kde.kglobalaccel5.platforms/KF5GlobalAccelPrivateXcb.so
%{_kf5_sharedir}/dbus-1/services/org.kde.kglobalaccel.service
%{_kf5_servicesdir}/kglobalaccel5.desktop
%{_userunitdir}/plasma-kglobalaccel.service

%changelog
