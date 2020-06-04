#
# spec file for package qtcurve
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


%bcond_with lang
Name:           qtcurve
Version:        1.9.0
Release:        0
Summary:        QtCurve style for Qt and GTK+
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://invent.kde.org/system/qtcurve
Source0:        qtcurve-%{version}.tar.gz
Source1:        baselibs.conf
Patch0:         0001-utils-gtkprops-Remove-unnecessary-constexpr-this-is-.patch
# PATCH-FIX-UPSTREAM
Patch1:         0001-Fix-build-with-Qt-5.15-missing-QPainterPath-include.patch
BuildRequires:  cmake >= 2.8.12
BuildRequires:  extra-cmake-modules
BuildRequires:  frameworkintegration-devel
BuildRequires:  gtk2-devel
BuildRequires:  libQt5Widgets-private-headers-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
%if 0%{?suse_version} <= 1500 && 0%{?sle_version} < 150200
BuildRequires:  kde4-filesystem
BuildRequires:  kdebase4-workspace-devel
%endif

%description
QtCurve is a set of widget styles available for Qt and GTK+.

%package -n libqtcurve-utils2
Summary:        QtCurve style for Qt and GTK+
Group:          System/GUI/KDE

%description -n libqtcurve-utils2
QtCurve is a set of widget styles available for Qt and GTK+.
This package cointains basic helper library needed for qtcurve.

%package -n libqtcurve-cairo1
Summary:        QtCurve style for Qt and GTK+
Group:          System/GUI/KDE

%description -n libqtcurve-cairo1
QtCurve is a set of widget styles available for Qt and GTK+.
This package cointains library for common drawing routines.

%if 0%{?suse_version} <= 1500 && 0%{?sle_version} < 150200
%package kde4
Summary:        QtCurve style for KDE 4
Group:          System/GUI/KDE
Requires:       libqtcurve-utils2 = %{version}
%{kde4_runtime_requires}

%description kde4
This is the QtCurve style for KDE 4. QtCurve is a set of widget
styles available for Qt and GTK+.
%endif

%package gtk2
Summary:        QtCurve style for GTK+ 2
Group:          System/GUI/GNOME
Requires:       libqtcurve-cairo1 = %{version}

%description gtk2
This package contains the QtCurve engine for GTK+ 2. QtCurve is a set
of widget styles available for Qt and GTK+.

%package qt5
Summary:        QtCurve style for Qt 5
Group:          System/GUI/KDE

%description qt5
This package contains the QtCurve style for Qt 5. QtCurve is a set
of widget styles available for Qt and GTK+.

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -DLIB_INSTALL_DIR=%{_libdir}

%cmake_build

%install
%kf5_makeinstall -C build

%if %{with lang}
%find_lang %{name}
%endif

%post -n libqtcurve-utils2   -p /sbin/ldconfig
%postun -n libqtcurve-utils2 -p /sbin/ldconfig
%post -n libqtcurve-cairo1   -p /sbin/ldconfig
%postun -n libqtcurve-cairo1 -p /sbin/ldconfig

%files -n libqtcurve-utils2
%{_libdir}/libqtcurve-utils.so.*
# We don't need the devel symlink
%exclude %{_libdir}/libqtcurve-utils.so

%files -n libqtcurve-cairo1
%{_libdir}/libqtcurve-cairo.so.*
# We don't need the devel symlink
%exclude %{_libdir}/libqtcurve-cairo.so

%if 0%{?suse_version} <= 1500 && 0%{?sle_version} < 150200
%files kde4
%license COPYING
%doc ChangeLog.md README.md TODO.md
%{_kde4_modulesdir}/kstyle_qtcurve_config.so
%{_kde4_modulesdir}/kwin_qtcurve_config.so
%{_kde4_modulesdir}/kwin3_qtcurve.so
%{_kde4_modulesdir}/plugins/styles
%{_kde4_appsdir}/QtCurve
%{_kde4_appsdir}/kstyle
%{_kde4_appsdir}/color-schemes/QtCurve.colors
%{_kde4_appsdir}/color-schemes/QtCurveAgua.colors
%{_kde4_appsdir}/kwin/qtcurve.desktop
%endif

%if %{with lang}
%files lang -f qtcurve.lang
%endif

%files gtk2
%license COPYING
%doc ChangeLog.md README.md TODO.md
%{_libdir}/gtk-2.0/*/engines/libqtcurve.*
%{_datadir}/themes/QtCurve/

%files qt5
%license COPYING
%doc ChangeLog.md README.md TODO.md
%{_libqt5_plugindir}/
%{_kf5_sharedir}/kstyle/
%{_kf5_kxmlguidir}/QtCurve

%changelog
