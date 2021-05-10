#
# spec file for package kglobalaccel
#
# Copyright (c) 2021 SUSE LLC
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
%define _tar_path 5.82
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kglobalaccel
Version:        5.82.0
Release:        0
Summary:        Global desktop keyboard shortcuts
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
BuildRequires:  libxcb-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake(KF5Config) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Crash) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5DBus) >= 5.15.0
BuildRequires:  cmake(Qt5Test) >= 5.15.0
BuildRequires:  cmake(Qt5Widgets) >= 5.15.0
BuildRequires:  cmake(Qt5X11Extras) >= 5.15.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb-keysyms)
%if %{with lang}
BuildRequires:  cmake(Qt5LinguistTools) >= 5.15.0
%endif

%description
KGlobalAccel allows you to have global accelerators that are independent of
the focused window.  Unlike regular shortcuts, the application's window does not
need focus for them to be activated.

%package -n %{lname}
Summary:        Global desktop keyboard shortcuts
Group:          System/GUI/KDE
%requires_ge    libQt5DBus5
%requires_ge    libQt5Widgets5
Recommends:     kglobalaccel5
%if %{with lang}
Recommends:     %{lname}-lang = %{version}
%endif

%description -n %{lname}
KGlobalAccel allows you to have global accelerators that are independent of
the focused window.  Unlike regular shortcuts, the application's window does not
need focus for them to be activated.

%package -n libKF5GlobalAccelPrivate5
Summary:        Global desktop keyboard shortcuts
Group:          System/GUI/KDE

%description -n libKF5GlobalAccelPrivate5
KGlobalAccel allows you to have global accelerators that are independent of
the focused window.  Unlike regular shortcuts, the application's window does not
need focus for them to be activated.

%package devel
Summary:        Global desktop keyboard shortcuts: Build Environment
Group:          Development/Libraries/KDE
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
Group:          System/GUI/KDE

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

%if %{with lang}
%find_lang %{name}5 --with-qt --without-mo
%endif

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

%if %{with lang}
%files -n %{lname}-lang -f %{name}5.lang
%endif

%files -n %{lname}
%license LICENSES/*
%doc README*
%{_kf5_libdir}/libKF5GlobalAccel.so.*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories

%files -n libKF5GlobalAccelPrivate5
%license LICENSES/*
%doc README*
%{_kf5_libdir}/libKF5GlobalAccelPrivate.so.*

%files devel
%{_kf5_libdir}/libKF5GlobalAccel.so
%{_kf5_libdir}/cmake/KF5GlobalAccel/
%{_kf5_includedir}/
%{_kf5_dbusinterfacesdir}/kf5_org.kde.KGlobalAccel.xml
%{_kf5_dbusinterfacesdir}/kf5_org.kde.kglobalaccel.Component.xml
%{_kf5_mkspecsdir}/qt_KGlobalAccel.pri

%files -n kglobalaccel5
%license LICENSES/*
%{_kf5_bindir}/kglobalaccel5
%dir %{_kf5_plugindir}/org.kde.kglobalaccel5.platforms
%{_kf5_plugindir}/org.kde.kglobalaccel5.platforms/KF5GlobalAccelPrivateXcb.so
%{_kf5_sharedir}/dbus-1/services/org.kde.kglobalaccel.service
%{_kf5_servicesdir}/kglobalaccel5.desktop
%{_userunitdir}/plasma-kglobalaccel.service

%changelog
