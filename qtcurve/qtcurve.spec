#
# spec file for package qtcurve
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
URL:            https://github.com/KDE/qtcurve
Source0:        qtcurve-%{version}.tar.gz
Source1:        baselibs.conf
Patch0:         0001-utils-gtkprops-Remove-unnecessary-constexpr-this-is-.patch
BuildRequires:  cmake >= 2.8.12
BuildRequires:  extra-cmake-modules
BuildRequires:  frameworkintegration-devel
BuildRequires:  gtk2-devel
BuildRequires:  karchive-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kdebase4-workspace-devel
BuildRequires:  kdelibs4support-devel
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libQt5Widgets-private-headers-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)

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

%package kde4
Summary:        QtCurve style for KDE 4
Group:          System/GUI/KDE
Requires:       libqtcurve-utils2 = %{version}
%kde4_runtime_requires

%description kde4
This is the QtCurve style for KDE 4. QtCurve is a set of widget
styles available for Qt and GTK+.

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
%setup -q
%patch0 -p1

%build
 %cmake_kde4 -d build -- -DENABLE_QT5=ON -DQTC_QT5_ENABLE_KDE=ON
 %make_jobs

%install
  pushd build
  %make_install
  popd
%if %{with lang}
  %find_lang %{name}
%endif
  %kde_post_install

%post -n libqtcurve-utils2   -p /sbin/ldconfig
%postun -n libqtcurve-utils2 -p /sbin/ldconfig
%post -n libqtcurve-cairo1   -p /sbin/ldconfig
%postun -n libqtcurve-cairo1 -p /sbin/ldconfig

%files -n libqtcurve-utils2
%{_kde4_libdir}/libqtcurve-utils.so.*
# We don't need the devel symlink
%exclude %{_kde4_libdir}/libqtcurve-utils.so

%files -n libqtcurve-cairo1
%{_kde4_libdir}/libqtcurve-cairo.so.*
# We don't need the devel symlink
%exclude %{_kde4_libdir}/libqtcurve-cairo.so

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

%if %{with lang}
%files lang -f qtcurve.lang
%endif

%files gtk2
%license COPYING
%doc ChangeLog.md README.md TODO.md
%{_kde4_libdir}/gtk-2.0/*/engines/libqtcurve.*
%{_kde4_datadir}/themes/QtCurve/

%files qt5
%license COPYING
%doc ChangeLog.md README.md TODO.md
%{_libqt5_plugindir}/
%{_kf5_sharedir}/kstyle/
%{_kf5_kxmlguidir}/QtCurve

%changelog
