#
# spec file for package kwin6-x11
#
# Copyright (c) 2025 SUSE LLC
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
%global __requires_exclude qt6qmlimport\\(org\\.kde\\.KWin\\.Effect\\.WindowView.*

%define kf6_version 6.18.0
%define qt6_version 6.9.0

%define rname   kwin-x11
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kwin6-x11
Version:        6.6.1
Release:        0
Summary:        KDE Window Manager
License:        GPL-2.0-or-later AND GPL-3.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel >= %{qt6_version}
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake(Breeze) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KDecoration3) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6ColorScheme) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Declarative) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IdleTime) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Package) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6Svg) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KGlobalAccelD) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KNightTime) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KScreenLocker) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KWayland) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Plasma) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaActivities) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaWaylandProtocols) >= 1.14.0
BuildRequires:  cmake(QAccessibilityClient6)
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sensors) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libdisplay-info) >= 0.2.0
BuildRequires:  pkgconfig(libdrm) >= 2.4.116
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wayland-client) >= 1.22
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.38
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb) >= 1.10
BuildRequires:  pkgconfig(xcb-composite) >= 1.10
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-damage) >= 1.10
BuildRequires:  pkgconfig(xcb-dri3) >= 1.10
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-glx) >= 1.10
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-present) >= 1.10
BuildRequires:  pkgconfig(xcb-randr) >= 1.10
BuildRequires:  pkgconfig(xcb-render) >= 1.10
BuildRequires:  pkgconfig(xcb-shape) >= 1.10
BuildRequires:  pkgconfig(xcb-shm) >= 1.10
BuildRequires:  pkgconfig(xcb-sync) >= 1.10
BuildRequires:  pkgconfig(xcb-xfixes) >= 1.10
BuildRequires:  pkgconfig(xcb-xinerama) >= 1.10
BuildRequires:  pkgconfig(xcb-xinput)
BuildRequires:  pkgconfig(xcb-xkb) >= 1.10
BuildRequires:  pkgconfig(xkbcommon) >= 0.7.0
BuildRequires:  pkgconfig(xkbcommon-x11)
Requires:       xwayland
Requires:       breeze6-decoration >= %{_plasma6_bugfix}
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kglobalacceld6  >= %{_plasma6_bugfix}
Requires:       libkwin-x11-6 = %{version}
# SECTION QML dependencies
Requires:       kf6-kdeclarative-imports >= %{kf6_version}
Requires:       kf6-kitemmodels-imports >= %{kf6_version}
Requires:       plasma6-framework-components >= %{_plasma6_bugfix}
Requires:       qt6-declarative-imports >= %{qt6_version}
Requires:       qt6-multimedia-imports >= %{qt6_version}
# /SECTION
# # For displaying full monitor vendor names
Recommends:     hwdata
Provides:       kwin5 = %{version}
Obsoletes:      kwin5 < %{version}
Obsoletes:      kwin5-lang < %{version}
# Needed to show dialogs
Requires:       kdialog
Provides:       windowmanager
Provides:       qt6qmlimport(org.kde.kwin_x11)
Provides:       qt6qmlimport(org.kde.kwin_x11.3) = 0

%description
KWin is Plasma window manager.

%package -n libkwin-x11-6
Summary:        KWin library

%description -n libkwin-x11-6
KWin is Plasma window manager.
This package provides the kwin library.

%package devel
Summary:        KDE Window Manager - development files
Requires:       kdecoration6-devel >= %{_plasma6_bugfix}
Requires:       libkwin-x11-6 = %{version}
Requires:       pkgconfig(epoxy)

%description devel
KWin is Plasma window manager.
This package provides development files.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%fdupes %{buildroot}%{_kf6_libdir}
%fdupes %{buildroot}%{_kf6_sharedir}

%preun
%{systemd_user_preun plasma-kwin_x11.service}

%post
%ldconfig
%ldconfig -n libkwin-x11-6
%{systemd_user_post plasma-kwin_x11.service}

%postun
%ldconfig
%ldconfig -n libkwin-x11-6
%{systemd_user_postun plasma-kwin_x11.service}

%ldconfig_scriptlets -n libkwin-x11-6

%files
%license LICENSES/*
%doc README.md
%doc %lang(en) %{_kf6_htmldir}/en/*
%{_kf6_applicationsdir}/kcm_kwin_effects_x11.desktop
%{_kf6_applicationsdir}/kcm_kwin_scripts_x11.desktop
%{_kf6_applicationsdir}/kcm_kwin_virtualdesktops_x11.desktop
%{_kf6_applicationsdir}/kcm_kwindecoration_x11.desktop
%{_kf6_applicationsdir}/kcm_kwinoptions_x11.desktop
%{_kf6_applicationsdir}/kcm_kwinrules_x11.desktop
%{_kf6_applicationsdir}/kcm_kwintabbox_x11.desktop
%{_kf6_applicationsdir}/kwincompositing.desktop
%{_kf6_applicationsdir}/org.kde.kwin_x11.killer.desktop
%{_kf6_applicationsdir}/kcm_animations_x11.desktop
%{_kf6_bindir}/kwin_x11
%{_kf6_debugdir}/org_kde_kwin_x11.categories
%{_kf6_iconsdir}/hicolor/*/apps/kwin-x11.png
%{_kf6_iconsdir}/hicolor/scalable/apps/kwin-x11.svgz
%{_kf6_knsrcfilesdir}/*.knsrc
%{_kf6_libdir}/kconf_update_bin/kwin-6.0-delete-desktop-switching-shortcuts-x11
%{_kf6_libdir}/kconf_update_bin/kwin-6.0-remove-breeze-tabbox-default-x11
%{_kf6_libdir}/kconf_update_bin/kwin-6.0-reset-active-mouse-screen-x11
%{_kf6_libdir}/kconf_update_bin/kwin-6.1-remove-gridview-expose-shortcuts-x11
%{_kf6_libdir}/kconf_update_bin/kwin-6.5-showpaint-changes-x11
%{_kf6_libdir}/kconf_update_bin/kwin5_update_default_rules_x11
%{_kf6_libdir}/libkcmkwincommon-x11.so.*
%{_kf6_notificationsdir}/kwin-x11.notifyrc
%dir %{_kf6_plugindir}/kwin-x11
%dir %{_kf6_plugindir}/kwin-x11/effects
%dir %{_kf6_plugindir}/kwin-x11/effects/configs
%{_kf6_plugindir}/kwin-x11/effects/configs/kcm_kwin4_genericscripted.so
%{_kf6_plugindir}/kwin-x11/effects/configs/kwin_blur_config.so
%{_kf6_plugindir}/kwin-x11/effects/configs/kwin_diminactive_config.so
%{_kf6_plugindir}/kwin-x11/effects/configs/kwin_glide_config.so
%{_kf6_plugindir}/kwin-x11/effects/configs/kwin_magiclamp_config.so
%{_kf6_plugindir}/kwin-x11/effects/configs/kwin_mouseclick_config.so
%{_kf6_plugindir}/kwin-x11/effects/configs/kwin_mousemark_config.so
%{_kf6_plugindir}/kwin-x11/effects/configs/kwin_overview_config.so
%{_kf6_plugindir}/kwin-x11/effects/configs/kwin_slide_config.so
%{_kf6_plugindir}/kwin-x11/effects/configs/kwin_thumbnailaside_config.so
%{_kf6_plugindir}/kwin-x11/effects/configs/kwin_tileseditor_config.so
%{_kf6_plugindir}/kwin-x11/effects/configs/kwin_trackmouse_config.so
%{_kf6_plugindir}/kwin-x11/effects/configs/kwin_windowview_config.so
%{_kf6_plugindir}/kwin-x11/effects/configs/kwin_wobblywindows_config.so
%dir %{_kf6_plugindir}/kwin-x11/plugins
%{_kf6_plugindir}/kwin-x11/plugins/krunnerintegration.so
%{_kf6_plugindir}/kwin-x11/plugins/nightlight.so
%dir %{_kf6_plugindir}/kf6/packagestructure
%{_kf6_plugindir}/kf6/packagestructure/kwin_aurorae_x11.so
%{_kf6_plugindir}/kf6/packagestructure/kwin_decoration_x11.so
%{_kf6_plugindir}/kf6/packagestructure/kwin_effect_x11.so
%{_kf6_plugindir}/kf6/packagestructure/kwin_scripts_x11.so
%{_kf6_plugindir}/kf6/packagestructure/kwin_windowswitcher_x11.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm*.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_kwin*.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kwincompositing.so
%dir %{_kf6_qmldir}/org/kde/kwin_x11/
%{_kf6_qmldir}/org/kde/kwin_x11/private/
%{_kf6_sharedir}/kconf_update/kwin-x11.upd
%{_kf6_sharedir}/krunner/dbusplugins/kwin-runner-windows-x11.desktop
%{_kf6_sharedir}/kwin-x11/
%{_libexecdir}/kwin-applywindowdecoration-x11
%{_libexecdir}/kwin_killer_helper_x11
%{_userunitdir}/plasma-kwin_x11.service

%files -n libkwin-x11-6
%{_kf6_libdir}/libkwin-x11.so.*

%files devel
%{_includedir}/kwin-x11/
%{_kf6_cmakedir}/KWinX11/
%{_kf6_cmakedir}/KWinX11DBusInterface/
%{_kf6_dbusinterfacesdir}/kwin_x11_org.kde.kwin.*
%{_kf6_dbusinterfacesdir}/kwin_x11_org.kde.KWin.*
%{_kf6_libdir}/libkwin-x11.so

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en

%changelog
