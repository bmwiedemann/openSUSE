#
# spec file for package kwin5
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


%global kf5_version 5.54.0
%global qt5_version 5.11.0
%global wayland (0%{?suse_version} >= 1330)
%bcond_without lang
Name:           kwin5
Version:        5.20.2
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
%if %{with lang}
Source1:        https://download.kde.org/stable/plasma/%{version}/kwin-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch100:       0001-Revert-Make-WindowSwitching-Alt-Tab-the-default-left.patch
# PATCH-FEATURE-OPENSUSE
Patch101:       0001-Use-Xauthority-for-Xwayland.patch
# PATCH-FIX-OPENSUSE
Patch102:       0001-Use-fixed-absolute-path-instead-of-usr-bin-env-in-sh.patch
# PATCH-FIX-OPENSUSE
Patch103:       0001-Bypass-wayland-interface-blacklisting.patch
BuildRequires:  extra-cmake-modules >= 0.0.11
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  libQt5Core-private-headers-devel >= 5.5.0
BuildRequires:  libQt5Gui-private-headers-devel >= 5.5.0
BuildRequires:  libQt5PlatformSupport-private-headers-devel >= 5.5.0
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
BuildRequires:  cmake(KF5Service) >= %{kf5_version}
BuildRequires:  cmake(KF5TextWidgets) >= %{kf5_version}
BuildRequires:  cmake(KF5Wayland) >= %{kf5_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{kf5_version}
BuildRequires:  cmake(KF5XmlGui) >= %{kf5_version}
BuildRequires:  cmake(KScreenLocker) >= %{_plasma5_version}
BuildRequires:  cmake(KWaylandServer) >= %{_plasma5_version}
BuildRequires:  cmake(Qt5Concurrent) >= %{qt5_version}
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_version}
BuildRequires:  cmake(Qt5Quick) >= %{qt5_version}
BuildRequires:  cmake(Qt5QuickWidgets) >= %{qt5_version}
BuildRequires:  cmake(Qt5Script) >= %{qt5_version}
BuildRequires:  cmake(Qt5Sensors) >= %{qt5_version}
BuildRequires:  cmake(Qt5UiTools) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
BuildRequires:  cmake(Qt5X11Extras) >= %{qt5_version}
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(wayland-cursor) >= 1.2.0
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
BuildRequires:  pkgconfig(libinput) >= 1.9
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wayland-egl)
# Don't use pkgconfig here as that would cause unresolvables on 0.1 -> 0.2 -> 0.3 bumps
BuildRequires:  pipewire-devel
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
Requires(verify): permissions
%requires_ge Mesa-libEGL1
%requires_ge libKF5WindowSystem5
%requires_ge plasma-framework
Recommends:     %{name}-lang

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
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
  %cmake_build

%install
  %kf5_makeinstall -C build
%if !%{wayland}
  rm -f %{buildroot}%{_kf5_bindir}/kwin_wayland
%endif
%if %{with lang}
  %kf5_find_lang
  %kf5_find_htmldocs
%endif
  %fdupes %{buildroot}%{_kf5_libdir}
  %fdupes %{buildroot}%{_datadir}

%preun
%systemd_user_preun plasma-kwin_wayland.service
%systemd_user_preun plasma-kwin_x11.service

%post
/sbin/ldconfig
%if %{wayland}
%set_permissions %{_kf5_bindir}/kwin_wayland
%endif
%systemd_user_post plasma-kwin_wayland.service plasma-kwin_x11.service

%postun
/sbin/ldconfig
%systemd_user_postun plasma-kwin_wayland.service plasma-kwin_x11.service

%if %{wayland}
%verifyscript
%verify_permissions -e %{_kf5_bindir}/kwin_wayland
%endif

%files
%license LICENSES/*
%if %{wayland}
%verify(not caps) %{_kf5_bindir}/kwin_wayland
%endif
%{_kf5_bindir}/kwin_x11
%{_kf5_debugdir}/org_kde_kwin.categories
%{_kf5_knsrcfilesdir}/*.knsrc
%{_kf5_libdir}/kconf_update_bin/
%{_kf5_libdir}/libexec/
%{_kf5_libdir}/libkwin.so.*
%{_kf5_libdir}/libkwin4_effect_builtins.so.*
%{_kf5_libdir}/libkwineffects.so.*
%{_kf5_libdir}/libkwingl*utils.so.*
%{_kf5_libdir}/libkwinxrenderutils.so.*
%{_kf5_libdir}/libkcmkwincommon.so.5
%{_kf5_libdir}/libkcmkwincommon.so.5.*
%{_kf5_plugindir}/kcm_kwin_scripts.so
%{_kf5_plugindir}/kcm_kwinoptions.so
%{_kf5_plugindir}/kcm_kwinscreenedges.so
%{_kf5_plugindir}/kcm_kwintabbox.so
%{_kf5_plugindir}/kcm_kwintouchscreen.so
%dir %{_kf5_plugindir}/kcms/
%{_kf5_plugindir}/kcms/kcm_kwin_effects.so
%{_kf5_plugindir}/kcms/kcm_kwin_virtualdesktops.so
%{_kf5_plugindir}/kcms/kcm_kwindecoration.so
%{_kf5_plugindir}/kcms/kcm_kwinrules.so
%dir %{_kf5_plugindir}/kf5/
%dir %{_kf5_plugindir}/kf5/org.kde.kidletime.platforms/
%{_kf5_plugindir}/kf5/org.kde.kidletime.platforms/KF5IdleTimeKWinWaylandPrivatePlugin.so
%dir %{_kf5_plugindir}/kf5/kwindowsystem/
%{_kf5_plugindir}/kf5/kwindowsystem/KF5WindowSystemKWinPrivatePlugin.so
%dir %{_kf5_plugindir}/kpackage/
%dir %{_kf5_plugindir}/kpackage/packagestructure/
%{_kf5_plugindir}/kpackage/packagestructure/kwin_packagestructure_aurorae.so
%{_kf5_plugindir}/kpackage/packagestructure/kwin_packagestructure_decoration.so
%{_kf5_plugindir}/kpackage/packagestructure/kwin_packagestructure_effect.so
%{_kf5_plugindir}/kpackage/packagestructure/kwin_packagestructure_scripts.so
%{_kf5_plugindir}/kpackage/packagestructure/kwin_packagestructure_windowswitcher.so
%dir %{_kf5_plugindir}/kwin/
%dir %{_kf5_plugindir}/kwin/effects/
%dir %{_kf5_plugindir}/kwin/effects/configs/
%{_kf5_plugindir}/kwin/effects/configs/kcm_kwin4_genericscripted.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_blur_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_coverswitch_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_cube_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_cubeslide_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_desktopgrid_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_diminactive_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_flipswitch_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_glide_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_invert_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_lookingglass_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_magiclamp_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_magnifier_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_mouseclick_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_mousemark_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_presentwindows_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_resize_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_showfps_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_showpaint_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_slide_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_thumbnailaside_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_trackmouse_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_windowgeometry_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_wobblywindows_config.so
%{_kf5_plugindir}/kwin/effects/configs/kwin_zoom_config.so
%{_kf5_plugindir}/kwincompositing.so
%dir %{_kf5_plugindir}/org.kde.kdecoration2/
%{_kf5_plugindir}/org.kde.kdecoration2/kwin5_aurorae.so
%dir %{_kf5_plugindir}/org.kde.kglobalaccel5.platforms/
%{_kf5_plugindir}/org.kde.kglobalaccel5.platforms/KF5GlobalAccelPrivateKWin.so
%dir %{_kf5_plugindir}/org.kde.kwin.platforms/
%{_kf5_plugindir}/org.kde.kwin.platforms/KWinX11Platform.so
%dir %{_kf5_plugindir}/org.kde.kwin.scenes/
%{_kf5_plugindir}/org.kde.kwin.scenes/KWinSceneOpenGL.so
%{_kf5_plugindir}/org.kde.kwin.scenes/KWinSceneQPainter.so
%{_kf5_plugindir}/org.kde.kwin.scenes/KWinSceneXRender.so
%dir %{_kf5_plugindir}/org.kde.kwin.waylandbackends/
%{_kf5_plugindir}/org.kde.kwin.waylandbackends/KWinWaylandDrmBackend.so
%{_kf5_plugindir}/org.kde.kwin.waylandbackends/KWinWaylandFbdevBackend.so
%{_kf5_plugindir}/org.kde.kwin.waylandbackends/KWinWaylandVirtualBackend.so
%{_kf5_plugindir}/org.kde.kwin.waylandbackends/KWinWaylandWaylandBackend.so
%{_kf5_plugindir}/org.kde.kwin.waylandbackends/KWinWaylandX11Backend.so
%{_kf5_plugindir}/platforms/KWinQpaPlugin.so

%dir %{_kf5_qmldir}/org/
%dir %{_kf5_qmldir}/org/kde/
%dir %{_kf5_qmldir}/org/kde/kwin/
%{_kf5_qmldir}/org/kde/kwin/decoration/
%{_kf5_qmldir}/org/kde/kwin/decorations/
%{_kf5_qmldir}/org/kde/kwin/private/

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
%{_userunitdir}/plasma-kwin_wayland.service
%{_userunitdir}/plasma-kwin_x11.service

%files devel
%license LICENSES/*
%{_kf5_prefix}/include/*.h
%{_kf5_libdir}/libkwin4_effect_builtins.so
%{_kf5_libdir}/libkwineffects.so
%{_kf5_libdir}/libkwingl*utils.so
%{_kf5_libdir}/libkwinxrenderutils.so
%{_kf5_libdir}/cmake/KWinDBusInterface/
%{_kf5_sharedir}/dbus-1/interfaces/

%if %{with lang}
%files lang -f %{name}.lang
%license LICENSES/*
%endif

%changelog
