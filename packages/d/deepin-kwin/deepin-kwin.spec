#
# spec file for package deepin-kwin
#
# Copyright (c) 2023 SUSE LLC
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

%global __requires_exclude qmlimport\\((org\\.kde\\.private\\.kcms\\.kwin\\.effects|org\\.kde\\.kcms\\.kwinrules|org\\.kde\\.kwin\\.private\\.overview|org\\.kde.kwin\\.private\\.desktopgrid|org\\.kde\\.KWin\\.Effect\\.WindowView|org\\.kde\\.kwin\\.kwinxwaylandsettings).*

%global kf5_version 5.90.0
%global qt5_version 5.15.0
%global wayland (0%{?suse_version} >= 1330)

Name:           deepin-kwin
Version:        5.25.0
Release:        0
# Full Plasma 5 version (e.g. 5.8.95)
%{!?_plasma5_bugfix: %define _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.8.95 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        Deepin Window Manager
License:        GPL-3.0-or-later
Group:          System/GUI/Deepin
Url:            https://github.com/linuxdeepin/deepin-kwin/
Source0:        https://github.com/linuxdeepin/deepin-kwin//archive/%{version}/%{name}-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE
Patch101:       0001-Export-consistent-hostname-as-XAUTHLOCALHOSTNAME.patch
BuildRequires:  extra-cmake-modules >= 0.0.11
BuildRequires:  fdupes
%if 0%{?suse_version} < 1550
BuildRequires:  gcc10-PIE
BuildRequires:  gcc10-c++
%endif
BuildRequires:  kf5-filesystem
BuildRequires:  libQt5Core-private-headers-devel >= %{qt5_version}
BuildRequires:  libQt5Gui-private-headers-devel >= %{qt5_version}
BuildRequires:  libQt5PlatformSupport-private-headers-devel >= %{qt5_version}
BuildRequires:  libcap-devel
BuildRequires:  libcap-progs
BuildRequires:  libepoxy-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  hwdata
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz
BuildRequires:  cmake(Breeze) >= 5.9.0
BuildRequires:  cmake(DWayland)
BuildRequires:  cmake(KDecoration2) >= %{_plasma5_version}
BuildRequires:  cmake(KF5Activities) >= %{kf5_version}
BuildRequires:  cmake(KF5Completion) >= %{kf5_version}
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5ConfigWidgets) >= %{kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5Crash) >= %{kf5_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5Declarative) >= %{kf5_version}
BuildRequires:  cmake(KF5DocTools) >= %{kf5_version}
BuildRequires:  cmake(KF5GlobalAccel) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5IconThemes) >= %{kf5_version}
BuildRequires:  cmake(KF5IdleTime) >= %{kf5_version}
BuildRequires:  cmake(KF5Init) >= %{kf5_version}
BuildRequires:  cmake(KF5KCMUtils) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5NewStuff) >= %{kf5_version}
BuildRequires:  cmake(KF5Notifications) >= %{kf5_version}
BuildRequires:  cmake(KF5Package) >= %{kf5_version}
BuildRequires:  cmake(KF5Plasma) >= %{kf5_version}
BuildRequires:  cmake(KF5Runner) >= %{kf5_version}
BuildRequires:  cmake(KF5Service) >= %{kf5_version}
BuildRequires:  cmake(KF5TextWidgets) >= %{kf5_version}
BuildRequires:  cmake(KF5Wayland) >= %{kf5_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{kf5_version}
BuildRequires:  cmake(KF5XmlGui) >= %{kf5_version}
BuildRequires:  cmake(KScreenLocker) >= %{_plasma5_version}
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(QAccessibilityClient)
BuildRequires:  cmake(Qt5Concurrent) >= %{qt5_version}
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_version}
BuildRequires:  cmake(Qt5Quick) >= %{qt5_version}
BuildRequires:  cmake(Qt5QuickWidgets) >= %{qt5_version}
BuildRequires:  cmake(Qt5Script) >= %{qt5_version}
BuildRequires:  cmake(Qt5Sensors) >= %{qt5_version}
BuildRequires:  cmake(Qt5UiTools) >= %{qt5_version}
BuildRequires:  cmake(Qt5WaylandClient) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
BuildRequires:  cmake(Qt5X11Extras) >= %{qt5_version}
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libxcvt)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(wayland-cursor) >= 1.2.0
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xcb) >= 1.10
BuildRequires:  pkgconfig(xcb-composite) >= 1.10
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-damage) >= 1.10
BuildRequires:  pkgconfig(xcb-glx) >= 1.10
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-randr) >= 1.10
BuildRequires:  pkgconfig(xcb-render) >= 1.10
BuildRequires:  pkgconfig(xcb-shape) >= 1.10
BuildRequires:  pkgconfig(xcb-shm) >= 1.10
BuildRequires:  pkgconfig(xcb-sync) >= 1.10
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xfixes) >= 1.10
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xkbcommon) >= 0.7.0
BuildRequires:  pkgconfig(xtst)
%if %{wayland}
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libdrm) >= 2.4.62
BuildRequires:  pkgconfig(libinput) >= 1.14
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(xwayland)
# Don't use pkgconfig here as that would cause unresolvables on 0.1 -> 0.2 -> 0.3 bumps
BuildRequires:  pipewire-devel >= 0.3.29
# xorg-x11-server-wayland is required by plasma5-session-wayland and kwin5 can run with just X11
Recommends:     xorg-x11-server-wayland
%endif
# new default decoration
Requires:       breeze5-decoration >= %{_plasma5_version}
# Needed to show dialogs
Requires:       kdialog
# Needed for effects KCM at runtime
Requires:       libQt5Multimedia5
# Needed for the virtual desktop KCM
Requires:       kirigami2
Requires:       kitemmodels-imports
%requires_eq    libQt5Core5
%requires_eq    libQt5Gui5
Provides:       windowmanager
Provides:       deepin-kwin5
# For post and verifyscript
Requires(post): permissions
Requires(verify):permissions
%requires_ge    Mesa-libEGL1
%requires_ge    libKF5WindowSystem5
%requires_ge    plasma-framework
# For displaying full monitor vendor names
Recommends:     hwdata

%description
deepin-kWin is the window manager of the Deepin desktop environment.

%package devel
Summary:        Development tools for deepin-kwin
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
The deepin-kwin is the window manager of the Deepin desktop environment.
This package provides development files.

%lang_package

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%if 0%{?suse_version} < 1550
  export CXX=g++-10
%endif
%cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir} -DINCLUDE_INSTALL_DIR=%{_includedir}/%{name}
%cmake_build

%install
%kf5_makeinstall -C build
%if !%{wayland}
  rm %{buildroot}%{_kf5_bindir}/%{name}_wayland
%endif

sed -i 's#/usr/bin/env python3#/usr/bin/python3#' %{buildroot}%{_kf5_sharedir}/kconf_update/*.py

%kf5_find_lang
%kf5_find_htmldocs

%fdupes %{buildroot}%{_kf5_libdir}
%fdupes %{buildroot}%{_datadir}

%preun
%{systemd_user_preun %{name}_x11.service %{name}_wayland.service}

%post
/sbin/ldconfig
%if %{wayland}
%set_permissions %{_kf5_bindir}/%{name}_wayland
%endif
%{systemd_user_post %{name}_x11.service %{name}_wayland.service}

%postun
/sbin/ldconfig
%{systemd_user_postun %{name}_x11.service %{name}_wayland.service}

%files
%defattr(-,root,root,-)
#%doc CHANGELOG.md
#%license LICENSE
%config %{_sysconfdir}/deepin-*
%if %{wayland}
%verify(not caps) %{_kf5_bindir}/%{name}_wayland
%{_kf5_bindir}/%{name}_wayland_wrapper
%endif
%{_kf5_applicationsdir}/*.desktop
%{_kf5_bindir}/%{name}_x11
%{_kf5_debugdir}/org_kde_%{name}.categories
%{_kf5_knsrcfilesdir}/*.knsrc
%{_kf5_libdir}/kconf_update_bin/
%{_kf5_libdir}/lib%{name}*.so.*
%{_kf5_libdir}/libdeepin-kcmkwincommon.so.*
%{_kf5_plugindir}/%{name}
%{_kf5_plugindir}/kcms
%{_kf5_plugindir}/*.so
%dir %{_kf5_plugindir}/kpackage/
%dir %{_kf5_plugindir}/kpackage/packagestructure/
%{_kf5_plugindir}/kpackage/packagestructure/*.so
%dir %{_kf5_sharedir}/kpackage
%dir %{_kf5_sharedir}/kpackage/kcms
%{_kf5_sharedir}/kpackage/kcms/deepin-*
%{_kf5_plugindir}/org.kde.*
%{_libexecdir}/%{name}_*
%{_libexecdir}/%{name}-applywindowdecoration
%{_kf5_sharedir}/config.kcfg/
%{_kf5_sharedir}/%{name}
%{_kf5_sharedir}/icons/hicolor/*/apps/%{name}.*
%{_kf5_sharedir}/kconf_update/
%{_kf5_sharedir}/kservices5
%{_kf5_sharedir}/kservicetypes5
%{_kf5_sharedir}/knotifications5
%dir %{_datadir}/dsg
%dir %{_datadir}/dsg/configs
%dir %{_datadir}/dsg/configs/org.deepin.kwin
%{_datadir}/dsg/configs/org.deepin.kwin/org.deepin.kwin.splitmenu.display.json
%dir %{_kf5_sharedir}/krunner
%dir %{_kf5_sharedir}/krunner/dbusplugins
%{_kf5_sharedir}/krunner/dbusplugins/%{name}-runner-windows.desktop
%dir %{_kf5_qmldir}/org/
%dir %{_kf5_qmldir}/org/deepin
%dir %{_kf5_qmldir}/org/deepin/kwin
%dir %{_kf5_qmldir}/org/deepin/kwin/decoration
%{_kf5_qmldir}/org/deepin/kwin/decoration/*.qml
%{_kf5_qmldir}/org/deepin/kwin/decoration/libdecorationplugin.so
%{_kf5_qmldir}/org/deepin/kwin/decoration/qmldir
%dir %{_kf5_qmldir}/org/kde/
%{_kf5_qmldir}/org/kde/%{name}
%{_userunitdir}/%{name}_wayland.service
%{_userunitdir}/%{name}_x11.service

%dir %{_datadir}/doc/HTML
%dir %{_datadir}/doc/HTML/en
%dir %{_datadir}/doc/HTML/en/dcontrol
%{_datadir}/doc/HTML/en/dcontrol/*

%files lang -f %{name}.lang
%defattr(-,root,root,-)
%dir %{_datadir}/translations
%{_datadir}/translations/popupmenu

%files devel
%defattr(-,root,root,-)
%{_kf5_libdir}/lib%{name}*.so
%{_kf5_libdir}/cmake/DeepinKWinEffects
%{_kf5_libdir}/cmake/DeepinKWinDBusInterface
%{_includedir}/%{name}
%{_kf5_sharedir}/dbus-1/interfaces/

%changelog

