#
# spec file for package kwin6
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


# Internal QML imports
%global __requires_exclude qt6qmlimport\\(org\\.kde\\.KWin\\.Effect\\.WindowView.*

%global kf6_version 6.2.0
%define qt6_version 6.6.0

%define rname   kwin
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kwin6
Version:        6.1.1
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
BuildRequires:  libcap-progs
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel >= %{qt6_version}
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake(Breeze) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KDecoration2) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Declarative) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IdleTime) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Package) >= %{kf6_version}
BuildRequires:  cmake(KF6Runner) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6Svg) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KGlobalAccelD) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KScreenLocker) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KWayland) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaActivities) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(QAccessibilityClient6)
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sensors) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm) >= 2.4.112
BuildRequires:  pkgconfig(libeis-1.0)
BuildRequires:  pkgconfig(libinput) >= 1.19
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.3.29
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libxcvt)
BuildRequires:  pkgconfig(wayland-cursor) >= 1.22
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.34
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb) >= 1.10
BuildRequires:  pkgconfig(xcb-composite) >= 1.10
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-damage) >= 1.10
BuildRequires:  pkgconfig(xcb-dri3) >= 1.10
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
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xfixes) >= 1.10
BuildRequires:  pkgconfig(xcb-xinerama) >= 1.10
BuildRequires:  pkgconfig(xcb-xkb) >= 1.10
BuildRequires:  pkgconfig(xkbcommon) >= 0.7.0
BuildRequires:  pkgconfig(xkbcommon-x11)
Requires:       breeze6-decoration >= %{_plasma6_bugfix}
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kglobalacceld6  >= %{_plasma6_bugfix}
Requires:       libkwin6 = %{version}
# SECTION QML dependencies
Requires:       kf6-kdeclarative-imports >= %{kf6_version}
Requires:       kf6-kitemmodels-imports >= %{kf6_version}
Requires:       plasma6-framework-components >= %{_plasma6_bugfix}
Requires:       qt6-declarative-imports >= %{qt6_version}
Requires:       qt6-multimedia-imports >= %{qt6_version}
# /SECTION
# For post and verifyscript
Requires(post): permissions
Requires(verify): permissions
# For displaying full monitor vendor names
Recommends:     hwdata
# xorg-x11-server-wayland is required by plasma6-session-wayland, but not kwin6 itself
Recommends:     xorg-x11-server-wayland
Provides:       kwin5 = %{version}
Obsoletes:      kwin5 < %{version}
Obsoletes:      kwin5-lang < %{version}
# /usr/share/kwin/tabbox/thumbnail_grid/metadata.json conflicts with plasma5-addons
# (Use a version check as plasma6-addons provides plasma5-addons)
Conflicts:      plasma5-addons < 6.0
Conflicts:      plasma5-addons-lang < 6.0
# Needed to show dialogs
Requires:       kdialog
Provides:       windowmanager
Provides:       qt6qmlimport(org.kde.kwin)
Provides:       qt6qmlimport(org.kde.kwin.3) = 0

%description
KWin is Plasma window manager.

%package x11
Summary:        KDE Window Manager for X11
Requires:       kwin6 = %{version}
Requires:       xorg-x11-server

%description x11
KWin is Plasma window manager.
This package provides the X11 window manager.

%package -n libkwin6
Summary:        KWin library

%description -n libkwin6
KWin is Plasma window manager.
This package provides the kwin library.

%package devel
Summary:        KDE Window Manager - development files
Requires:       kdecoration6-devel >= %{_plasma6_bugfix}
Requires:       libkwin6 = %{version}
Requires:       pkgconfig(epoxy)
Provides:       kwin5-devel = %{version}
Obsoletes:      kwin5-devel < %{version}

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

%find_lang kwin6 --with-html --all-name

%fdupes %{buildroot}%{_kf6_libdir}
%fdupes %{buildroot}%{_kf6_sharedir}

%preun
%{systemd_user_preun plasma-kwin_wayland.service}

%post
%ldconfig
%ldconfig -n libkwin6
%set_permissions %{_kf6_bindir}/kwin_wayland
%{systemd_user_post plasma-kwin_wayland.service}

%postun
%ldconfig
%ldconfig -n libkwin6
%{systemd_user_postun plasma-kwin_wayland.service}

%ldconfig_scriptlets -n libkwin6

%preun x11
%{systemd_user_preun plasma-kwin_x11.service}

%post x11
%{systemd_user_post plasma-kwin_x11.service}

%postun x11
%{systemd_user_postun plasma-kwin_x11.service}

%verifyscript
%verify_permissions -e %{_kf6_bindir}/kwin_wayland

%files
%verify(not caps) %{_kf6_bindir}/kwin_wayland
%license LICENSES/*
%doc README.md
%doc %lang(en) %{_kf6_htmldir}/en/*
%{_kf6_applicationsdir}/kcm_kwin_effects.desktop
%{_kf6_applicationsdir}/kcm_kwin_scripts.desktop
%{_kf6_applicationsdir}/kcm_kwin_virtualdesktops.desktop
%{_kf6_applicationsdir}/kcm_kwindecoration.desktop
%{_kf6_applicationsdir}/kcm_kwinoptions.desktop
%{_kf6_applicationsdir}/kcm_kwinrules.desktop
%{_kf6_applicationsdir}/kcm_kwintabbox.desktop
%{_kf6_applicationsdir}/kcm_kwinxwayland.desktop
%{_kf6_applicationsdir}/kcm_virtualkeyboard.desktop
%{_kf6_applicationsdir}/kwincompositing.desktop
%{_kf6_applicationsdir}/org.kde.kwin.killer.desktop
%{_kf6_bindir}/kwin_wayland_wrapper
%{_kf6_configkcfgdir}/*
%{_kf6_debugdir}/org_kde_kwin.categories
%{_kf6_iconsdir}/hicolor/*/apps/kwin.png
%{_kf6_iconsdir}/hicolor/scalable/apps/kwin.svgz
%{_kf6_knsrcfilesdir}/*.knsrc
%{_kf6_libdir}/kconf_update_bin/kwin5_update_default_rules
%{_kf6_libdir}/kconf_update_bin/kwin-6.0-delete-desktop-switching-shortcuts
%{_kf6_libdir}/kconf_update_bin/kwin-6.0-remove-breeze-tabbox-default
%{_kf6_libdir}/kconf_update_bin/kwin-6.0-reset-active-mouse-screen
%{_kf6_libdir}/kconf_update_bin/kwin-6.1-remove-gridview-expose-shortcuts
%{_kf6_libdir}/libkcmkwincommon.so.*
%{_kf6_notificationsdir}/kwin.notifyrc
%dir %{_kf6_plugindir}/kwin
%dir %{_kf6_plugindir}/kwin/effects
%dir %{_kf6_plugindir}/kwin/effects/configs
%{_kf6_plugindir}/kwin/effects/configs/kcm_kwin4_genericscripted.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_blur_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_colorblindnesscorrection_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_diminactive_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_glide_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_hidecursor_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_invert_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_magiclamp_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_magnifier_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_mouseclick_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_mousemark_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_overview_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_showpaint_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_slide_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_thumbnailaside_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_tileseditor_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_trackmouse_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_windowview_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_wobblywindows_config.so
%{_kf6_plugindir}/kwin/effects/configs/kwin_zoom_config.so
%dir %{_kf6_plugindir}/kwin/plugins
%{_kf6_plugindir}/kwin/plugins/StickyKeysPlugin.so
%{_kf6_plugindir}/kwin/plugins/BounceKeysPlugin.so
%{_kf6_plugindir}/kwin/plugins/buttonsrebind.so
%{_kf6_plugindir}/kwin/plugins/eis.so
%{_kf6_plugindir}/kwin/plugins/krunnerintegration.so
%{_kf6_plugindir}/kwin/plugins/nightlight.so
%{_kf6_plugindir}/kwin/plugins/screencast.so
%dir %{_kf6_plugindir}/org.kde.kdecoration2.kcm
%{_kf6_plugindir}/org.kde.kdecoration2.kcm/kcm_auroraedecoration.so
%dir %{_kf6_plugindir}/org.kde.kdecoration2
%{_kf6_plugindir}/org.kde.kdecoration2/org.kde.kwin.aurorae.so
%dir %{_kf6_plugindir}/kf6/packagestructure
%{_kf6_plugindir}/kf6/packagestructure/kwin_aurorae.so
%{_kf6_plugindir}/kf6/packagestructure/kwin_decoration.so
%{_kf6_plugindir}/kf6/packagestructure/kwin_effect.so
%{_kf6_plugindir}/kf6/packagestructure/kwin_scripts.so
%{_kf6_plugindir}/kf6/packagestructure/kwin_windowswitcher.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm*.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_kwin*.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kwincompositing.so
%dir %{_kf6_qmldir}/org/kde/kwin/
%{_kf6_qmldir}/org/kde/kwin/decoration/
%{_kf6_qmldir}/org/kde/kwin/decorations/
%{_kf6_qmldir}/org/kde/kwin/private/
%{_kf6_sharedir}/kconf_update/kwin.upd
%{_kf6_sharedir}/krunner/dbusplugins/kwin-runner-windows.desktop
%{_kf6_sharedir}/kwin/
%{_libexecdir}/kwin-applywindowdecoration
%{_libexecdir}/kwin_killer_helper
%{_userunitdir}/plasma-kwin_wayland.service

%files x11
%{_kf6_bindir}/kwin_x11
%{_userunitdir}/plasma-kwin_x11.service

%files -n libkwin6
%{_kf6_libdir}/libkwin.so.6
%{_kf6_libdir}/libkwin.so.*

%files devel
%{_includedir}/kwin/
%{_kf6_cmakedir}/KWin/
%{_kf6_cmakedir}/KWinDBusInterface/
%{_kf6_dbusinterfacesdir}/org.kde.kwin.*
%{_kf6_dbusinterfacesdir}/org.kde.KWin.*
%{_kf6_libdir}/libkwin.so

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en

%changelog
