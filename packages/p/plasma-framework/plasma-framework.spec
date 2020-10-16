#
# spec file for package plasma-framework
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


%define lname libKF5Plasma5
%define _tar_path 5.75
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           plasma-framework
Version:        5.75.0
Release:        0
Summary:        Plasma library and runtime components based upon KF5 and Qt5
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
# PATCH-FIX-UPSTREAM
Patch1:         0001-BusyIndicator-Do-not-rotate-when-invisible.patch
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  libxcb-devel
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  cmake(KF5Activities) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Archive) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Config) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5ConfigWidgets) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Declarative) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5DocTools) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5GlobalAccel) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5GuiAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5IconThemes) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5KIO) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Kirigami2) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Notifications) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Package) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Parts) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Service) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Wayland) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5XmlGui) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5Concurrent) >= 5.12.0
BuildRequires:  cmake(Qt5Gui) >= 5.12.0
BuildRequires:  cmake(Qt5Qml) >= 5.12.0
BuildRequires:  cmake(Qt5Quick) >= 5.12.0
BuildRequires:  cmake(Qt5QuickControls2) >= 5.12.0
BuildRequires:  cmake(Qt5Sql) >= 5.12.0
BuildRequires:  cmake(Qt5Svg) >= 5.12.0
BuildRequires:  cmake(Qt5Test) >= 5.12.0
BuildRequires:  cmake(Qt5Widgets) >= 5.12.0
BuildRequires:  cmake(Qt5X11Extras) >= 5.12.0
#FIXME: Figure how to add it properly
BuildRequires:  libQt5PlatformHeaders-devel
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(x11)
Recommends:     %{name}-components = %{version}
Recommends:     %{name}-lang = %{version}
Provides:       %{name}-private = %{version}
Obsoletes:      %{name}-private < %{version}
%ifarch %{arm} aarch64
BuildRequires:  pkgconfig(glesv2)
%else
BuildRequires:  pkgconfig(gl)
%endif

%description
Plasma library and runtime components based upon KF5 and Qt5

%package -n %{lname}
Summary:        Plasma framework - core libraries
Group:          System/GUI/KDE
Conflicts:      %{name} < 5.49
Conflicts:      %{name}-private < 5.49

%description -n %{lname}
This package contains the core libraries needed by the Plasma framework.

%package components
Summary:        Plasma QML components
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}
Requires:       %{name}-private = %{version}
Requires:       libqt5-qtquickcontrols
Requires:       libqt5-qtquickcontrols2
%requires_ge    kdeclarative-components

%description components
Plasma QML and runtime components based upon KF5 and Qt5

%package devel
Summary:        Plasma library and runtime components
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       %{name} = %{version}
Requires:       %{name}-components = %{version}
Requires:       %{name}-private = %{version}
Requires:       extra-cmake-modules >= 1.7.0
Requires:       kf5-filesystem
Requires:       cmake(KF5Package) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5Service) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5WindowSystem) >= %{_kf5_bugfix_version}
Requires:       cmake(Qt5Gui) >= 5.12.0
Requires:       cmake(Qt5Qml) >= 5.12.0
Requires:       cmake(Qt5Quick) >= 5.12.0
Conflicts:      kapptemplate <= 15.12.3

%description devel
Plasma library and runtime components based upon KF5 and Qt5

%lang_package

%prep
%autosetup -p1

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %fdupes %{buildroot}

%if %{with lang}
%find_lang %{name} --with-man --all-name
%endif

%pre
# Was part of plasma-framework previously, so remove it
if [ $1 -eq 2 ] ; then
  update-alternatives --remove input.svgz \
    %{_datadir}/plasma/desktoptheme/default/icons/input.svgz-kdeorg
fi

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%if %{with lang}
%files lang -f %{name}.lang
# LC_SCRIPTS is not recognized by find-lang.sh
%lang(lt) %{_datadir}/locale/lt/LC_SCRIPTS
%endif

%files -n %{lname}
%license LICENSES/*
%{_kf5_libdir}/libKF5Plasma.so.*
%{_kf5_libdir}/libKF5PlasmaQuick.so.*
%{_kf5_debugdir}/plasma-framework.categories
%{_kf5_debugdir}/*.renamecategories

%files
%license LICENSES/*
%{_kf5_bindir}/*
%{_kf5_plugindir}/
%{_kf5_plasmadir}/
%{_kf5_servicesdir}/
%{_kf5_servicetypesdir}/
%{_kf5_mandir}/man1/plasmapkg*.*

%files components
%license LICENSES/*
%{_kf5_qmldir}/

%files devel
%license LICENSES/*
%{_kf5_includedir}/Plasma/
%{_kf5_includedir}/PlasmaQuick/
%{_kf5_includedir}/plasma/
%{_kf5_includedir}/plasma_version.h
%{_kf5_includedir}/plasmaquick/
%{_kf5_libdir}/cmake/*/
%{_kf5_libdir}/libKF5Plasma.so
%{_kf5_libdir}/libKF5PlasmaQuick.so
%{_kf5_sharedir}/kdevappwizard

%changelog
