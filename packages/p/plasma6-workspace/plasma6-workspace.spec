#
# spec file for package plasma6-workspace
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


# TODO Remove when gpsd has a qt6 flavor
%global __qml_requires_opts --qtver 6

%global __requires_exclude qt6qmlimport\\((org\\.kde\\.plasma\\.private|org\\.kde\\.plasma\\.workspace|org\\.kde\\.notificationmanager|org\\.kde\\.plasma\\.lookandfeel|org\\.kde\\.plasma\\.wallpapers|org\\.kde\\.taskmanager|org\\.kde\\.holidayeventshelperplugin|org\\.kde\\.kscreenlocker).*

%define kf6_version 6.0.0
%define qt6_version 6.6.0
%define rname plasma-workspace
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %global _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           plasma6-workspace
Version:        6.0.5
Release:        0
Summary:        The KDE Plasma Workspace Components
License:        GPL-2.0-or-later
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
Source3:        sddm.conf
Source4:        waitforkded.conf
# PATCH-FIX-UPSTREAM
Patch1:         0001-Authenticate-local-clients.patch
Patch2:         0002-Remove-iceauth-dependency.patch
Patch3:         0001-Fix-writing-ICEAuthority-file.patch
# PATCHES 501-??? are PATCH-FIX-OPENSUSE
Patch501:       0001-Use-qdbus6.patch
Patch502:       0001-Ignore-default-sddm-face-icons.patch
# boo#951888
Patch503:       dont-show-yast-modules-in-the-applications-menu.patch
# As long as migration from Leap < 15.4 is still relevant, breaks openQA otherwise.
Patch504:       0001-Revert-krunner-Remove-kconf_update-code.patch
# PATCH-FEATURE-OPENSUSE
Patch506:       0001-Revert-No-icons-on-the-desktop-by-default.patch
BuildRequires:  fdupes
BuildRequires:  kf6-breeze-icons
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
# Due to KWinDBusInterface not having a cmake version config file, we need to BR kwin6-devel instead
# BuildRequires:  cmake(KWinDBusInterface) >= %%{_plasma6_bugfix}
BuildRequires:  kwin6-devel >= %{_plasma6_bugfix}
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  qt6-waylandclient-private-devel >= %{qt6_version}
BuildRequires:  update-desktop-files
BuildRequires:  cmake(AppStreamQt) >= 1.0
BuildRequires:  cmake(Breeze) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KExiv2Qt6)
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6Baloo) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Declarative) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Holidays) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6IdleTime) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KDED) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  cmake(KF6NetworkManagerQt) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6NotifyConfig) >= %{kf6_version}
BuildRequires:  cmake(KF6Package) >= %{kf6_version}
BuildRequires:  cmake(KF6Prison) >= %{kf6_version}
BuildRequires:  cmake(KF6QuickCharts) >= %{kf6_version}
BuildRequires:  cmake(KF6Runner) >= %{kf6_version}
BuildRequires:  cmake(KF6Screen) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6Svg) >= %{kf6_version}
BuildRequires:  cmake(KF6TextEditor) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6UnitConversion) >= %{kf6_version}
BuildRequires:  cmake(KF6UserFeedback) >= %{kf6_version}
BuildRequires:  cmake(KF6Wallet) >= %{kf6_version}
BuildRequires:  cmake(KPipeWire) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KScreenLocker) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KSysGuard) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KWayland) >= %{_plasma6_bugfix}
BuildRequires:  cmake(LayerShellQt) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Phonon4Qt6)
BuildRequires:  cmake(Plasma) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Plasma5Support) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaActivities) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaActivitiesStats) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaQuick) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaWaylandProtocols) >= 1.6
BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6ShaderTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandCompositor) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(ScreenSaverDBusInterface) >= %{_plasma6_bugfix}
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libgps)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libqalculate) >= 2.0
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(wayland-client) >= 1.15
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-damage)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(zlib)
Requires:       iso-codes
Requires:       iso-codes-lang
Requires:       plasma6-workspace-libs = %{version}-%{release}
# Needed for kcm_users
Requires:       accountsservice
# contains default style, cursors, etc
Requires:       breeze6 >= %{_plasma6_bugfix}
# Only recommended due to poor performances with LTO (https://sourceware.org/bugzilla/show_bug.cgi?id=23710)
Recommends:     drkonqi6 >= %{_plasma6_bugfix}
# dialog/platformtheme/etc
Requires:       kf6-frameworkintegration-plugin
Requires:       kactivitymanagerd6
# used within startup
Requires:       kde-cli-tools6 >= %{_plasma6_bugfix}
Requires:       kf6-kded
Requires:       kf6-kquickcharts
Requires:       kglobalacceld6 >= %{_plasma6_bugfix}
Requires:       kirigami-addons6 >= 0.10.0
Requires:       kscreen6 >= %{_plasma6_bugfix}
Requires:       kscreenlocker6 >= %{_plasma6_bugfix}
Requires:       kwin6 >= %{_plasma6_bugfix}
Requires:       libkscreen6-plugin >= %{_plasma6_bugfix}
Requires:       qt6-tools-qdbus
# heavily used by plasma
Requires:       qt6-declarative-imports >= %{qt6_version}
Requires:       kf6-kconfig-imports
# needed by krunner
Requires:       milou6 >= %{_plasma6_bugfix}
Requires:       qt6-sql-sqlite >= %{qt6_version}
Recommends:     ocean-sound-theme6 >= %{_plasma6_bugfix}
# Used by KCMs
Requires:       kf6-knewstuff-imports >= %{kf6_version}
# Used by system monitoring applets
Requires:       ksystemstats6
# Used by the user feedback KCM
Requires:       kf6-kuserfeedback-imports
# krdb uses xrdb with cpp preprocessing
Requires:       cpp
Requires:       xrdb
Requires:       xsetroot
# Used by the zsh completion script
Requires:       %{_bindir}/grep
# Qt6 SDDM greeter
Requires:       (sddm-greeter-qt6 if sddm)
# For wallpaper thumbnails
# Not to be mistaken for kio-extras5
Requires:       kio-extras
# Hardcode versions of plasma6-framework-components, as upstream doesn't keep backwards compability there
%requires_ge    plasma6-framework-components
# The lockscreen has a button to open a virtual keyboard
Recommends:     qt6-virtualkeyboard-imports >= %{qt6_version}
# For dmenudbusmenuproxy
Recommends:     (appmenu-gtk2-module if libgtk-2_0-0)
Recommends:     (appmenu-gtk3-module if libgtk-3-0)
# plasma6-desktop 'Provides' kdebase4-workspace < 5.3.0
Conflicts:      kdebase4-workspace < 5.3.0
Provides:       plasma5-workspace = %{version}
Obsoletes:      plasma5-workspace < %{version}
Obsoletes:      plasma5-workspace-lang < %{version}
# Use to be a separate package in plasma5
Provides:       gmenudbusmenuproxy = %{version}
Obsoletes:      gmenudbusmenuproxy < %{version}
# If installed, it force-enables itself which can cause issues
# gmenudbusmenuproxy used to conflict with this package
Conflicts:      unity-gtk-module-common
# Use to be a separate package in plasma5
Provides:       xembedsniproxy = %{version}
Obsoletes:      xembedsniproxy < %{version}
# Used to be provided/obsoleted by xembedsniproxy
Provides:       xembed-sni-proxy = %{version}
Obsoletes:      xembed-sni-proxy < %{version}
# Dropped functionality
Obsoletes:      khotkeys5 < %{version}
Obsoletes:      khotkeys5-lang < %{version}
Obsoletes:      ksysguard5 < %{version}
Obsoletes:      ksysguard5-lang < %{version}
# Some files have been moved from kio-extras5 to plasma5-workspace in 5.4. This should prevent a possible file conflict. (boo#944656)
Conflicts:      kio-extras5 < 15.08.0
Provides:       plasma6-workspace-branding = %{_plasma6_bugfix}
Provides:       plasma6-workspace-branding-upstream = %{version}
# plasmashell implements the dbus interface org.freedesktop.Notifications directly
Provides:       dbus(org.freedesktop.Notifications)
Provides:       qt6qmlimport(org.kde.plasma.shell)
Provides:       qt6qmlimport(org.kde.plasma.shell.2) = 0
Provides:       qt6qmlimport(org.kde.plasma.shell.panel)
Provides:       qt6qmlimport(org.kde.plasma.shell.panel.0) = 1
# Was dropped in 5.20, replaced by kcm_users from p-d
Provides:       kde-user-manager = %{version}
Obsoletes:      kde-user-manager < %{version}

%description
This package contains the basic packages for a Plasma workspace.

%package libs
Summary:        The KDE Plasma Workspace Components
%requires_ge    plasma6-framework
Provides:       plasma5-workspace-libs = %{version}
Obsoletes:      plasma5-workspace-libs < %{version}

%description libs
This package contains the basic packages for a KDE Plasma 6 workspace.

%package devel
Summary:        The KDE Plasma Workspace Components
Requires:       plasma6-workspace-libs = %{version}-%{release}
Requires:       cmake(KF6ItemModels) >= %{kf6_version}
Requires:       cmake(LayerShellQt) >= %{_plasma6_bugfix}
Requires:       cmake(Plasma) >= %{_plasma6_bugfix}
Requires:       cmake(Qt6Core) >= %{qt6_version}
Requires:       cmake(Qt6Gui) >= %{qt6_version}
Requires:       cmake(Qt6Quick) >= %{qt6_version}
Conflicts:      kapptemplate <= 16.03.80
Provides:       plasma5-workspace-devel = %{version}
Obsoletes:      plasma5-workspace-devel < %{version}

%description devel
This package contains the basic packages for a KDE Plasma 6 workspace.
Development files.

%package -n plasma6-session
Summary:        KDE Plasma 6 Session
Requires:       breeze6 >= %{_plasma6_bugfix}
Requires:       breeze6-decoration >= %{_plasma6_bugfix}
Requires:       kf6-kwindowsystem >= %{kf6_version}
Requires:       plasma6-desktop >= %{_plasma6_bugfix}
Requires:       plasma6-workspace >= %{_plasma6_bugfix}
Requires:       polkit-kde-agent-6 >= %{_plasma6_bugfix}
Requires:       powerdevil6 >= %{_plasma6_bugfix}
Requires:       systemsettings6 >= %{_plasma6_bugfix}
# For KF5 kwayland (!)
Requires:       (kwayland-integration6 if kwayland)
Requires:       qt6-wayland
# For screen sharing and window thumbnails in plasmashell
Requires:       pipewire
Requires:       xdg-user-dirs
Requires:       xorg-x11-server-wayland
Provides:       plasma5-session-wayland = %{version}
Obsoletes:      plasma5-session-wayland < %{version}
# People may want the X11 session
Recommends:     plasma6-session-x11 = %{version}
BuildArch:      noarch

%description -n plasma6-session
This package contains the startup scripts necessary to start a KDE
Plasma 6 session.

%package -n plasma6-session-x11
Summary:        KDE Plasma 6 Session on X11
Requires:       kwin6-x11 >= %{_plasma6_bugfix}
Requires:       plasma6-session = %{version}
Requires:       xf86-input-libinput
Requires:       xorg-x11-server
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       kdebase4-session = %{version}
Obsoletes:      kdebase4-session < %{version}
Provides:       plasma5-session = %{version}
Obsoletes:      plasma5-session < %{version}

%description -n plasma6-session-x11
This package contains the startup scripts and programs necessary to
start a KDE Plasma 6 session on X11.

%package -n sddm-qt6-branding-openSUSE
Summary:        Plasma 6 branding for SDDM
Requires:       %{name} = %{version}
Requires:       sddm-greeter-qt6
Supplements:    (%{name} and sddm)

%description -n sddm-qt6-branding-openSUSE
This package confirms defaults for SDDM suitable for Plasma 6.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 \
  -DGLIBC_LOCALE_GENERATED:BOOL=TRUE \
  -DGLIBC_LOCALE_GEN:BOOL=FALSE \
  -DPLASMA_X11_DEFAULT_SESSION:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

# Copy the icon for org.kde.kcolorschemeeditor.desktop
mkdir -p %{buildroot}%{_kf6_iconsdir}/hicolor/32x32/apps/
cp %{_kf6_iconsdir}/breeze/preferences/32/preferences-desktop-color.svg %{buildroot}%{_kf6_iconsdir}/hicolor/32x32/apps/

# Rename upstream session file to oS location
mv %{buildroot}%{_kf6_sharedir}/xsessions/{plasma,plasma6}.desktop

# Install compatibility symlink
ln -s %{_kf6_sharedir}/xsessions/plasma6.desktop %{buildroot}%{_kf6_sharedir}/xsessions/kde-plasma.desktop

mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/default-xsession.desktop
ln -s %{_sysconfdir}/alternatives/default-xsession.desktop %{buildroot}%{_datadir}/xsessions/default.desktop

install -Dm 0644 %{SOURCE3} %{buildroot}%{_prefix}/lib/sddm/sddm.conf.d/10-plasma.conf
install -Dm 0644 %{SOURCE4} %{buildroot}%{_userunitdir}/plasma-plasmashell.service.d/waitforkded.conf

%fdupes %{buildroot}%{_prefix}

%post
%ldconfig
%{systemd_user_post plasma-gmenudbusmenuproxy.service plasma-kcminit-phase1.service plasma-kcminit.service \
  plasma-krunner.service plasma-ksmserver.service plasma-ksplash-ready.service plasma-plasmashell.service \
  plasma-xembedsniproxy.service plasma-baloorunner.service plasma-restoresession.service plasma-ksplash.service}

%preun
%{systemd_user_preun plasma-gmenudbusmenuproxy.service plasma-kcminit-phase1.service plasma-kcminit.service \
  plasma-krunner.service plasma-ksmserver.service plasma-ksplash-ready.service plasma-plasmashell.service \
  plasma-xembedsniproxy.service plasma-baloorunner.service plasma-restoresession.service plasma-ksplash.service}

%postun
%ldconfig
%{systemd_user_postun plasma-gmenudbusmenuproxy.service plasma-kcminit-phase1.service plasma-kcminit.service \
  plasma-krunner.service plasma-ksmserver.service plasma-ksplash-ready.service plasma-plasmashell.service \
  plasma-xembedsniproxy.service plasma-baloorunner.service plasma-restoresession.service plasma-ksplash.service}

%ldconfig_scriptlets libs

%post -n plasma6-session-x11
%{_sbindir}/update-alternatives --install %{_datadir}/xsessions/default.desktop \
  default-xsession.desktop %{_datadir}/xsessions/plasma6.desktop 25

%postun -n plasma6-session-x11
[ -f %{_datadir}/xsessions/plasma6.desktop ] || %{_sbindir}/update-alternatives \
  --remove default-xsession.desktop %{_datadir}/xsessions/plasma6.desktop

%files
%license LICENSES/*
%dir %{_kf6_configdir}/menus
%config %{_kf6_configdir}/menus/plasma-applications.menu
%config %{_kf6_configdir}/plasmanotifyrc
%config %{_kf6_configdir}/taskmanagerrulesrc
%doc %lang(en) %{_kf6_htmldir}/en/PolicyKit-kde/
%doc %lang(en) %{_kf6_htmldir}/en/kcontrol/
%doc %lang(en) %{_kf6_htmldir}/en/klipper/
%exclude %{_kf6_libdir}/libkfontinst.so
%exclude %{_kf6_libdir}/libkfontinstui.so
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_plasmashell
%{_datadir}/zsh/site-functions/_krunner
%{_kf6_applicationsdir}/kcm_autostart.desktop
%{_kf6_applicationsdir}/kcm_colors.desktop
%{_kf6_applicationsdir}/kcm_cursortheme.desktop
%{_kf6_applicationsdir}/kcm_desktoptheme.desktop
%{_kf6_applicationsdir}/kcm_feedback.desktop
%{_kf6_applicationsdir}/kcm_fontinst.desktop
%{_kf6_applicationsdir}/kcm_fonts.desktop
%{_kf6_applicationsdir}/kcm_icons.desktop
%{_kf6_applicationsdir}/kcm_lookandfeel.desktop
%{_kf6_applicationsdir}/kcm_nightcolor.desktop
%{_kf6_applicationsdir}/kcm_notifications.desktop
%{_kf6_applicationsdir}/kcm_regionandlang.desktop
%{_kf6_applicationsdir}/kcm_soundtheme.desktop
%{_kf6_applicationsdir}/kcm_style.desktop
%{_kf6_applicationsdir}/kcm_users.desktop
%{_kf6_applicationsdir}/kcm_wallpaper.desktop
%{_kf6_applicationsdir}/org.kde.kcolorschemeeditor.desktop
%{_kf6_applicationsdir}/org.kde.kfontview.desktop
%{_kf6_applicationsdir}/org.kde.plasmashell.desktop
%{_kf6_applicationsdir}/org.kde.plasmawindowed.desktop
%{_kf6_appstreamdir}/*.xml
%{_kf6_bindir}/gmenudbusmenuproxy
%{_kf6_bindir}/kcminit
%{_kf6_bindir}/kcminit_startup
%{_kf6_bindir}/kcolorschemeeditor
%{_kf6_bindir}/kde-systemd-start-condition
%{_kf6_bindir}/kfontinst
%{_kf6_bindir}/kfontview
%{_kf6_bindir}/krunner
%{_kf6_bindir}/ksmserver
%{_kf6_bindir}/ksplashqml
%{_kf6_bindir}/lookandfeeltool
%{_kf6_bindir}/plasma-apply-colorscheme
%{_kf6_bindir}/plasma-apply-cursortheme
%{_kf6_bindir}/plasma-apply-desktoptheme
%{_kf6_bindir}/plasma-apply-lookandfeel
%{_kf6_bindir}/plasma-apply-wallpaperimage
%{_kf6_bindir}/plasma-interactiveconsole
%{_kf6_bindir}/plasma-shutdown
%{_kf6_bindir}/plasma_session
%{_kf6_bindir}/plasma_waitforname
%{_kf6_bindir}/plasmashell
%{_kf6_bindir}/plasmawindowed
%{_kf6_bindir}/startplasma-wayland
%{_kf6_bindir}/xembedsniproxy
%{_kf6_configdir}/autostart/gmenudbusmenuproxy.desktop
%{_kf6_configdir}/autostart/org.kde.plasmashell.desktop
%{_kf6_configdir}/autostart/xembedsniproxy.desktop
%{_kf6_configkcfgdir}/colorssettings.kcfg
%{_kf6_configkcfgdir}/cursorthemesettings.kcfg
%{_kf6_configkcfgdir}/feedbacksettings.kcfg
%{_kf6_configkcfgdir}/fontssettings.kcfg
%{_kf6_configkcfgdir}/freespacenotifier.kcfg
%{_kf6_configkcfgdir}/iconssettingsbase.kcfg
%{_kf6_configkcfgdir}/launchfeedbacksettings.kcfg
%{_kf6_configkcfgdir}/lookandfeelsettings.kcfg
%{_kf6_configkcfgdir}/stylesettings.kcfg
%{_kf6_debugdir}/*.categories
%{_kf6_iconsdir}/hicolor/*/apps/kfontview.png
%{_kf6_iconsdir}/hicolor/*/mimetypes/fonts-package.png
%{_kf6_iconsdir}/hicolor/32x32/apps/preferences-desktop-color.svg
%{_kf6_iconsdir}/hicolor/scalable/apps/preferences-desktop-font-installer.svgz
%{_kf6_knsrcfilesdir}/colorschemes.knsrc
%{_kf6_knsrcfilesdir}/gtk_themes.knsrc
%{_kf6_knsrcfilesdir}/icons.knsrc
%{_kf6_knsrcfilesdir}/kfontinst.knsrc
%{_kf6_knsrcfilesdir}/lookandfeel.knsrc
%{_kf6_knsrcfilesdir}/plasma-themes.knsrc
%{_kf6_knsrcfilesdir}/plasmoids.knsrc
%{_kf6_knsrcfilesdir}/wallpaper-mobile.knsrc
%{_kf6_knsrcfilesdir}/wallpaper.knsrc
%{_kf6_knsrcfilesdir}/wallpaperplugin.knsrc
%{_kf6_knsrcfilesdir}/xcursor.knsrc
%{_kf6_kxmlguidir}/kfontview
%{_kf6_libdir}/kconf_update_bin/krunnerglobalshortcuts
%{_kf6_libdir}/kconf_update_bin/krunnerhistory
%{_kf6_libdir}/kconf_update_bin/plasmashell-6.0-keep-custom-position-of-panels
%{_kf6_libdir}/kconf_update_bin/plasmashell-6.0-keep-default-floating-setting-for-plasma-5-panels
%{_kf6_libdir}/kconf_update_bin/plasma6.0-remove-dpi-settings
%{_kf6_libdir}/kconf_update_bin/plasma6.0-remove-old-shortcuts
%{_kf6_libdir}/libkfontinst.so.*
%{_kf6_libdir}/libkfontinstui.so.*
%{_kf6_notificationsdir}/devicenotifications.notifyrc
%{_kf6_notificationsdir}/freespacenotifier.notifyrc
%{_kf6_notificationsdir}/phonon.notifyrc
%{_kf6_plasmadir}/avatars/
%{_kf6_plasmadir}/look-and-feel/
%{_kf6_plasmadir}/plasmoids/
%{_kf6_plasmadir}/wallpapers/
%{_kf6_plugindir}/kf6/kded/
%{_kf6_plugindir}/kf6/kfileitemaction/
%{_kf6_plugindir}/kf6/kio/
%{_kf6_plugindir}/kf6/krunner/
%{_kf6_plugindir}/kf6/packagestructure/
%{_kf6_plugindir}/kf6/parts/
%{_kf6_plugindir}/kf6/thumbcreator/
%{_kf6_plugindir}/phonon_platform/
%{_kf6_plugindir}/plasma/
%{_kf6_plugindir}/plasma5support/
%{_kf6_plugindir}/plasmacalendarplugins/
%{_kf6_qmldir}/org/kde/breeze/
%{_kf6_qmldir}/org/kde/colorcorrect/
%{_kf6_qmldir}/org/kde/holidayeventshelperplugin/
%{_kf6_qmldir}/org/kde/notificationmanager/
%{_kf6_qmldir}/org/kde/plasma/
%{_kf6_qmldir}/org/kde/taskmanager/
%{_kf6_sharedir}/dbus-1/services/org.kde.KSplash.service
%{_kf6_sharedir}/dbus-1/services/org.kde.LogoutPrompt.service
%{_kf6_sharedir}/dbus-1/services/org.kde.Shutdown.service
%{_kf6_sharedir}/dbus-1/services/org.kde.fontinst.service
%{_kf6_sharedir}/dbus-1/services/org.kde.krunner.service
%{_kf6_sharedir}/dbus-1/services/org.kde.plasma.Notifications.service
%{_kf6_sharedir}/dbus-1/services/org.kde.runners.baloo.service
%{_kf6_sharedir}/dbus-1/system-services/org.kde.fontinst.service
%{_kf6_sharedir}/dbus-1/system.d/org.kde.fontinst.conf
%{_kf6_sharedir}/desktop-directories/
%{_kf6_sharedir}/kconf_update/
%{_kf6_sharedir}/kfontinst/
%{_kf6_sharedir}/kglobalaccel/org.kde.krunner.desktop
%dir %{_kf6_sharedir}/kio
%dir %{_kf6_sharedir}/kio/servicemenus
%{_kf6_sharedir}/kio/servicemenus/installfont.desktop
%{_kf6_sharedir}/kio_desktop/
%{_kf6_sharedir}/konqsidebartng/
%{_kf6_sharedir}/krunner/dbusplugins/plasma-runner-baloosearch.desktop
%{_kf6_sharedir}/kstyle/
%{_kf6_sharedir}/plasma5support/
%{_kf6_sharedir}/polkit-1/actions/org.kde.fontinst.policy
%dir %{_kf6_sharedir}/sddm
%dir %{_kf6_sharedir}/sddm/themes
%{_kf6_sharedir}/sddm/themes/breeze/
%{_kf6_sharedir}/solid/
%{_libexecdir}/baloorunner
%{_kf6_libexecdir}/kauth/fontinst
%{_kf6_libexecdir}/kauth/fontinst_helper
%{_kf6_libexecdir}/kauth/fontinst_x11
%{_libexecdir}/kfontprint
%{_libexecdir}/ksmserver-logout-greeter
%{_libexecdir}/plasma-changeicons
%{_libexecdir}/plasma-dbus-run-session-if-needed
%{_libexecdir}/plasma-sourceenv.sh
%{_userunitdir}/plasma-baloorunner.service
%{_userunitdir}/plasma-core.target
%{_userunitdir}/plasma-gmenudbusmenuproxy.service
%{_userunitdir}/plasma-kcminit-phase1.service
%{_userunitdir}/plasma-kcminit.service
%{_userunitdir}/plasma-krunner.service
%{_userunitdir}/plasma-ksmserver.service
%{_userunitdir}/plasma-ksplash-ready.service
%{_userunitdir}/plasma-ksplash.service
%{_userunitdir}/plasma-plasmashell.service
%dir %{_userunitdir}/plasma-plasmashell.service.d/
%{_userunitdir}/plasma-plasmashell.service.d/waitforkded.conf
%{_userunitdir}/plasma-restoresession.service
%{_userunitdir}/plasma-workspace-{wayland,x11}.target
%{_userunitdir}/plasma-workspace.target
%{_userunitdir}/plasma-xembedsniproxy.service

%files libs
%license LICENSES/*
%{_kf6_libdir}/libcolorcorrect.so.*
%{_kf6_libdir}/libkmpris.so.*
%{_kf6_libdir}/libkrdb.so
%{_kf6_libdir}/libkworkspace6.so.*
%{_kf6_libdir}/libnotificationmanager.so.*
%{_kf6_libdir}/libplasma-geolocation-interface.so.*
%{_kf6_libdir}/libtaskmanager.so.*
%{_kf6_libdir}/libweather_ion.so.*

%files devel
%license LICENSES/*
%{_includedir}/colorcorrect/
%{_includedir}/krdb/
%{_includedir}/kworkspace6/
%{_includedir}/notificationmanager/
%{_includedir}/plasma/
%{_includedir}/plasma5support/
%{_includedir}/taskmanager/
%{_kf6_libdir}/cmake/KRunnerAppDBusInterface/
%{_kf6_libdir}/cmake/KSMServerDBusInterface/
%{_kf6_libdir}/cmake/LibColorCorrect/
%{_kf6_libdir}/cmake/LibKWorkspace/
%{_kf6_libdir}/cmake/LibNotificationManager/
%{_kf6_libdir}/cmake/LibTaskManager/
%{_kf6_libdir}/libcolorcorrect.so
%{_kf6_libdir}/libkmpris.so
%{_kf6_libdir}/libkworkspace6.so
%{_kf6_libdir}/libnotificationmanager.so
%{_kf6_libdir}/libplasma-geolocation-interface.so
%{_kf6_libdir}/libtaskmanager.so
%{_kf6_libdir}/libweather_ion.so
%{_kf6_sharedir}/dbus-1/interfaces/

%files -n plasma6-session
%license LICENSES/*
%dir %{_datadir}/wayland-sessions/
%{_kf6_sharedir}/wayland-sessions/plasmawayland.desktop

%files -n plasma6-session-x11
%{_kf6_bindir}/startplasma-x11
%ghost %{_sysconfdir}/alternatives/default-xsession.desktop
%{_kf6_sharedir}/xsessions/default.desktop
%{_kf6_sharedir}/xsessions/kde-plasma.desktop
%{_kf6_sharedir}/xsessions/plasma6.desktop

%files -n sddm-qt6-branding-openSUSE
%dir %{_prefix}/lib/sddm/
%dir %{_prefix}/lib/sddm/sddm.conf.d/
%{_prefix}/lib/sddm/sddm.conf.d/10-plasma.conf

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/PolicyKit-kde
%exclude %{_kf6_htmldir}/en/kcontrol
%exclude %{_kf6_htmldir}/en/klipper

%changelog
