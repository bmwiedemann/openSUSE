#
# spec file for package kwin5
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


# Internal QML imports
%global __requires_exclude qmlimport\\((org\\.kde\\.private\\.kcms\\.kwin\\.effects|org\\.kde\\.kcms\\.kwinrules|org\\.kde\\.kwin\\.private\\.overview|org\\.kde.kwin\\.private\\.desktopgrid|org\\.kde\\.KWin\\.Effect\\.WindowView).*

%global kf5_version 5.98.0
%global qt5_version 5.15.0
%global wayland (0%{?suse_version} >= 1330)
%bcond_without released
Name:           kwin5
Version:        5.26.5
%define _plasma5_bugfix 5.26.2
Release:        0
# Full Plasma 5 version (e.g. 5.8.95)
%{!?_plasma5_bugfix: %define _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.8.95 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        KDE Window Manager
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          System/GUI/KDE
URL:            http://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/kwin-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/kwin-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
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
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz
BuildRequires:  cmake(Breeze) >= 5.9.0
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
%if %{wayland}
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libdrm) >= 2.4.62
BuildRequires:  pkgconfig(libinput) >= 1.14
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wayland-egl)
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
# For post and verifyscript
Requires(post): permissions
Requires(verify):permissions
%requires_ge Mesa-libEGL1
%requires_ge libKF5WindowSystem5
%requires_ge plasma-framework
Recommends:     %{name}-lang
# For displaying full monitor vendor names
Recommends:     hwdata
Provides:       qt5qmlimport(org.kde.kwin.2) = 0
Provides:       qt5qmlimport(org.kde.kwin.3) = 0

%description
KWin is the window manager of the K desktop environment.

%package devel
Summary:        KDE Window Manager - development files
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}
Requires:       libepoxy-devel
Requires:       libkdecoration2-devel >= %{_plasma5_version}
Conflicts:      kdebase4-workspace-devel

%description devel
KWin is the window manager of the K desktop environment.
This package provides development files.

%lang_package

%prep
%autosetup -p1 -n kwin-%{version}

%build
%if 0%{?suse_version} < 1550
  export CXX=g++-10
%endif
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
  %cmake_build

%install
  %kf5_makeinstall -C build
%if !%{wayland}
  rm -f %{buildroot}%{_kf5_bindir}/kwin_wayland
%endif
  sed -i 's#/usr/bin/env python3#/usr/bin/python3#' %{buildroot}%{_kf5_sharedir}/kconf_update/*.py
%if %{with released}
  %kf5_find_lang
  %kf5_find_htmldocs
%endif
  %fdupes %{buildroot}%{_kf5_libdir}
  %fdupes %{buildroot}%{_datadir}

%preun
%{systemd_user_preun plasma-kwin_x11.service plasma-kwin_wayland.service}

%post
/sbin/ldconfig
%if %{wayland}
%set_permissions %{_kf5_bindir}/kwin_wayland
%endif
%{systemd_user_post plasma-kwin_x11.service plasma-kwin_wayland.service}

%postun
/sbin/ldconfig
%{systemd_user_postun plasma-kwin_x11.service plasma-kwin_wayland.service}

%if %{wayland}
%verifyscript
%verify_permissions -e %{_kf5_bindir}/kwin_wayland
%endif

%files
%license LICENSES/*
%if %{wayland}
%verify(not caps) %{_kf5_bindir}/kwin_wayland
%{_kf5_bindir}/kwin_wayland_wrapper
%endif
%{_kf5_applicationsdir}/org.kde.kwin_rules_dialog.desktop
%{_kf5_applicationsdir}/kcm_kwin_effects.desktop
%{_kf5_applicationsdir}/kcm_kwin_virtualdesktops.desktop
%{_kf5_applicationsdir}/kcm_kwinrules.desktop
%{_kf5_applicationsdir}/kcm_virtualkeyboard.desktop
%{_kf5_applicationsdir}/kcm_kwin_scripts.desktop
%{_kf5_applicationsdir}/kcm_kwindecoration.desktop
%{_kf5_applicationsdir}/kcm_kwinoptions.desktop
%{_kf5_applicationsdir}/kcm_kwintabbox.desktop
%{_kf5_applicationsdir}/kwincompositing.desktop
%{_kf5_bindir}/kwin_x11
%{_kf5_debugdir}/org_kde_kwin.categories
%{_kf5_knsrcfilesdir}/*.knsrc
%{_kf5_libdir}/kconf_update_bin/
%{_kf5_libdir}/libkwin.so.*
%{_kf5_libdir}/libkwineffects.so.*
%{_kf5_libdir}/libkwingl*utils.so.*
%{_kf5_libdir}/libkcmkwincommon.so.5
%{_kf5_libdir}/libkcmkwincommon.so.5.*
%dir %{_kf5_plugindir}/plasma/
%dir %{_kf5_plugindir}/plasma/kcms/
%dir %{_kf5_plugindir}/plasma/kcms/systemsettings/
%dir %{_kf5_plugindir}/plasma/kcms/systemsettings_qwidgets/
%{_kf5_plugindir}/plasma/kcms/systemsettings/kcm*.so
%{_kf5_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_kwin*.so
%{_kf5_plugindir}/plasma/kcms/systemsettings_qwidgets/kwincompositing.so
%dir %{_kf5_plugindir}/kpackage/
%dir %{_kf5_plugindir}/kpackage/packagestructure/
%{_kf5_plugindir}/kpackage/packagestructure/kwin_aurorae.so
%{_kf5_plugindir}/kpackage/packagestructure/kwin_decoration.so
%{_kf5_plugindir}/kpackage/packagestructure/kwin_effect.so
%{_kf5_plugindir}/kpackage/packagestructure/kwin_script.so
%{_kf5_plugindir}/kpackage/packagestructure/kwin_windowswitcher.so
%dir %{_kf5_sharedir}/kpackage/kcms
%{_kf5_sharedir}/kpackage/kcms/kcm_kwin_scripts/
%dir %{_kf5_plugindir}/kwin/
%dir %{_kf5_plugindir}/kwin/effects/
%dir %{_kf5_plugindir}/kwin/effects/configs/
%dir %{_kf5_plugindir}/kwin/plugins/
%{_kf5_plugindir}/kwin/plugins/colordintegration.so
%{_kf5_plugindir}/kwin/plugins/MouseButtonToKeyPlugin.so
%dir %{_kf5_sharedir}/krunner
%dir %{_kf5_sharedir}/krunner/dbusplugins
%{_kf5_sharedir}/krunner/dbusplugins/kwin-runner-windows.desktop
%{_kf5_plugindir}/kwin/plugins/krunnerintegration.so
%{_kf5_plugindir}/kwin/plugins/libKWinNightColorPlugin.so
%{_kf5_plugindir}/kwin/effects/configs/kcm_kwin4_genericscripted.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_blur_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_desktopgrid_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_diminactive_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_glide_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_invert_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_magiclamp_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_magnifier_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_mouseclick_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_mousemark_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_showpaint_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_slide_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_thumbnailaside_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_trackmouse_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_windowview_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_wobblywindows_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_zoom_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_overview_config.so
%dir %{_kf5_plugindir}/org.kde.kdecoration2/
%{_kf5_plugindir}/org.kde.kdecoration2/kwin5_aurorae.so

%dir %{_kf5_qmldir}/org/
%dir %{_kf5_qmldir}/org/kde/
%dir %{_kf5_qmldir}/org/kde/kwin/
%{_kf5_qmldir}/org/kde/kwin/decoration/
%{_kf5_qmldir}/org/kde/kwin/decorations/
%{_kf5_qmldir}/org/kde/kwin/private/
%{_kf5_qmldir}/org/kde/kwin.2/

%{_kf5_sharedir}/config.kcfg/
%{_kf5_sharedir}/icons/hicolor/*/apps/kwin.png
%{_kf5_sharedir}/icons/hicolor/scalable/apps/kwin.svgz
%{_kf5_servicesdir}/
%{_kf5_servicetypesdir}/
%{_kf5_sharedir}/kwin/
%{_kf5_sharedir}/kconf_update/
%{_kf5_notifydir}/
%doc %{_kf5_htmldir}/en/
%dir %{_kf5_sharedir}/kpackage/
%dir %{_kf5_sharedir}/kpackage/kcms/
%{_kf5_sharedir}/kpackage/kcms/kcm_kwin_virtualdesktops
%{_kf5_sharedir}/kpackage/kcms/kcm_kwindecoration
%{_kf5_sharedir}/kpackage/kcms/kcm_kwin_effects
%{_kf5_sharedir}/kpackage/kcms/kcm_kwinrules
%{_kf5_sharedir}/kpackage/kcms/kcm_virtualkeyboard
%{_libexecdir}/kwin-applywindowdecoration
%{_libexecdir}/kwin_killer_helper
%{_libexecdir}/kwin_rules_dialog
%{_userunitdir}/plasma-kwin_x11.service
%{_userunitdir}/plasma-kwin_wayland.service

%files devel
%license LICENSES/*
%{_kf5_prefix}/include/*.h
%{_kf5_libdir}/libkwineffects.so
%{_kf5_libdir}/libkwingl*utils.so
%{_kf5_libdir}/cmake/KWinDBusInterface/
%{_kf5_sharedir}/dbus-1/interfaces/
%{_kf5_cmakedir}/KWinEffects/

%if %{with released}
%files lang -f %{name}.lang
%license LICENSES/*
%endif

%changelog
