#
# spec file for package plasma6-desktop
#
# Copyright (c) 2026 SUSE LLC and contributors
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
%global __requires_exclude qt6qmlimport\\((org\\.kde\\.plasma\\.shell\\.panel|org\\.kde\\.plasma\\.private).*

%define kf6_version 6.26.0
%define qt6_version 6.10.0

%define rname plasma-desktop
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           plasma6-desktop
Version:        6.8.2
Release:        0
Summary:        The KDE Plasma Workspace Components
License:        GPL-2.0-only
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch100:       0001-Apply-branding-to-default-favorites.patch
# PATCH-FIX-OPENSUSE
Patch101:       0001-Revert-sddm-theme-drop-vkb-wrapper-use-KWinVirtualKe.patch
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
# Due to KWinDBusInterface not having a cmake version config file, we need to BR kwin6-devel instead
# BuildRequires:  cmake(KWinDBusInterface) >= %%{_plasma6_bugfix}
# Also applies to ScreenSaverDBusInterface
# BuildRequires:  cmake(ScreenSaverDBusInterface) >= %%{_plasma6_bugfix}
BuildRequires:  kscreenlocker6-devel >= %{_plasma6_bugfix}
BuildRequires:  kwin6-devel >= %{_plasma6_bugfix}
BuildRequires:  cmake(KAccounts6)
BuildRequires:  cmake(KF6Attica) >= %{kf6_version}
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6Baloo) >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KDED) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Kirigami) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6NotifyConfig) >= %{kf6_version}
BuildRequires:  cmake(KF6Package) >= %{kf6_version}
BuildRequires:  cmake(KF6QQC2DesktopStyle) >= %{kf6_version}
BuildRequires:  cmake(KF6Runner) >= %{kf6_version}
BuildRequires:  cmake(KF6Sonnet) >= %{kf6_version}
BuildRequires:  cmake(KF6Svg) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KRunnerAppDBusInterface) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KSMServerDBusInterface) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KSysGuard) >= %{_plasma6_bugfix}
BuildRequires:  cmake(LibKLookAndFeel) >= %{_plasma6_bugfix}
BuildRequires:  cmake(LibKWorkspace) >= %{_plasma6_bugfix}
BuildRequires:  cmake(LibNotificationManager) >= %{_plasma6_bugfix}
BuildRequires:  cmake(LibTaskManager) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Plasma) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Plasma5Support) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaActivities) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaActivitiesStats) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaQuick) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:  cmake(Qt6Concurrent)  >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6GuiPrivate) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6ShaderTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(packagekitqt6)
BuildRequires:  cmake(sdl2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libwacom)
BuildRequires:  pkgconfig(signon-oauth2plugin)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.44
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-atom)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xkbregistry)
%ifnarch s390x
BuildRequires:  pkgconfig(xorg-evdev)
%endif
BuildRequires:  xkeyboard-config
Requires:       plasma6-desktop-branding = %{version}
Requires:       plasma6-workspace >= %{_plasma6_bugfix}
# Required by the 'recent files' kcm
Requires:       qt6-sql-sqlite >= %{qt6_version}
# Hardcode versions of libplasma6-components, as upstream doesn't keep backwards compability there
%requires_ge    libplasma6-components
# Various KCMs use it
Requires:       kinfocenter6
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kirigami-addons6 >= 1.0.0
Requires:       kmenuedit6
# Needed for sensors
Requires:       libksysguard6-imports  >= %{_plasma6_bugfix}
# kcm_style does DBus calls to the KDED module.
# However, that depends on xsettingsd and gio, so
# let the Supplements in kde-gtk-config5 handle it.
Requires:       kde-gtk-config6
# Needed for several KCMs
Requires:       kf6-knewstuff-imports >= %{kf6_version}
# needed for the ActivityManager
Requires:       plasma6-activities-imports >= %{_plasma6_bugfix}
# Needed by Kickoff
Requires:       qt6qmlimport(org.kde.plasma.plasma5support)
# Only when WebEngine is available
%ifarch aarch64 x86_64 riscv64
# Needed for the OpenDesktop integration
Requires:       signon-plugin-oauth2
%endif
Conflicts:      kactivities5 < 5.20.0
Recommends:     plasma6-addons
Recommends:     plasma6-desktop-emojier
Recommends:     xdg-user-dirs
Provides:       kdebase4-workspace = 5.3.0
Obsoletes:      kdebase4-workspace < 5.3.0
Provides:       kcm-touchpad = %{version}
Obsoletes:      kcm-touchpad < %{version}
Provides:       kdebase4-workspace-plasma-calendar = %{version}
Obsoletes:      kdebase4-workspace-plasma-calendar < %{version}
Provides:       kdebase4-workspace-plasma-engine-akonadi = %{version}
Obsoletes:      kdebase4-workspace-plasma-engine-akonadi < %{version}
Conflicts:      kio-extras5 <= 5.3.2
Provides:       kcm-touchpad5 = %{version}
Obsoletes:      kcm-touchpad5 < %{version}
Provides:       plasma5-desktop-branding-upstream = %{version}
Provides:       plasma6-desktop-branding = %{version}
Obsoletes:      plasma5-desktop-branding-upstream < %{version}
Provides:       plasma5-desktop = %{version}
Obsoletes:      plasma5-desktop < %{version}
Obsoletes:      plasma5-desktop-lang < %{version}
Provides:       plasma5-addons-kimpanel = %{version}
Obsoletes:      plasma5-addons-kimpanel < %{version}
Provides:       plasma5-desktop-kimpanel = %{version}
Obsoletes:      plasma5-desktop-kimpanel < %{version}
Requires:       (plasma6-kimpanel-ibus if ibus)

%description
This package contains the basic packages for a Plasma workspace.

%package emojier
Summary:        Selection window for emoji text input
Requires:       plasma6-desktop = %{version}
# Other color fonts don't really work that well
Recommends:     noto-coloremoji-fonts
Provides:       plasma5-desktop-emojier = %{version}
Obsoletes:      plasma5-desktop-emojier < %{version}

%description emojier
Press Meta+. to open an emoji selection window.

%package -n plasma6-kimpanel-ibus
Summary:        Plasma 6 IBus Configuration
Requires:       %{name} = %{version}

%description -n plasma6-kimpanel-ibus
Plasma 6 Input Method Backend for IBus support.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name --with-html

%fdupes %{buildroot}%{_prefix}

%post
%ldconfig
%{systemd_user_post plasma-kaccess.service}

%preun
%{systemd_user_preun plasma-kaccess.service}

%postun
%ldconfig
%{systemd_user_postun plasma-kaccess.service}

%files
%license COPYING*
%doc %lang(en) %{_kf6_htmldir}/en/*/
%{_kf6_applicationsdir}/kaccess.desktop
%{_kf6_applicationsdir}/kcm_access.desktop
%{_kf6_applicationsdir}/kcm_activities.desktop
%{_kf6_applicationsdir}/kcm_baloofile.desktop
%{_kf6_applicationsdir}/kcm_clock.desktop
%{_kf6_applicationsdir}/kcm_desktoppaths.desktop
%{_kf6_applicationsdir}/kcm_gamecontroller.desktop
%{_kf6_applicationsdir}/kcm_kded.desktop
%{_kf6_applicationsdir}/kcm_keyboard.desktop
%{_kf6_applicationsdir}/kcm_keys.desktop
%{_kf6_applicationsdir}/kcm_krunnersettings.desktop
%{_kf6_applicationsdir}/kcm_landingpage.desktop
%{_kf6_applicationsdir}/kcm_plasmasearch.desktop
%{_kf6_applicationsdir}/kcm_qtquicksettings.desktop
%{_kf6_applicationsdir}/kcm_recentFiles.desktop
%{_kf6_applicationsdir}/kcm_smserver.desktop
%{_kf6_applicationsdir}/kcm_solid_actions.desktop
%{_kf6_applicationsdir}/kcm_splashscreen.desktop
%{_kf6_applicationsdir}/kcm_tablet.desktop
%{_kf6_applicationsdir}/kcm_touchscreen.desktop
%{_kf6_applicationsdir}/kcm_workspace.desktop
%{_kf6_applicationsdir}/kde-mimeapps.list
%{_kf6_applicationsdir}/org.kde.knetattach.desktop
%{_kf6_applicationsdir}/kcm_mouse.desktop
%{_kf6_applicationsdir}/kcm_spellchecking.desktop
%{_kf6_applicationsdir}/kcm_touchpad.desktop
%{_kf6_appstreamdir}/*.xml
%{_kf6_bindir}/kaccess
%{_kf6_bindir}/knetattach
%{_kf6_bindir}/krunner-plugininstaller
%{_kf6_bindir}/solid-action-desktop-gen
%{_kf6_bindir}/tastenbrett
%{_kf6_configdir}/autostart/kaccess.desktop
%{_kf6_configkcfgdir}/*.kcfg
%{_kf6_debugdir}/*.categories
%{_kf6_knsrcfilesdir}/krunner.knsrc
%{_kf6_knsrcfilesdir}/ksplash.knsrc
%{_kf6_libdir}/libkglobalaccelmodel.so.*
%{_kf6_notificationsdir}/kaccess.notifyrc
%{_kf6_plasmadir}/layout-templates/
%{_kf6_plasmadir}/packages/
%{_kf6_plasmadir}/plasmoids/
%{_kf6_plasmadir}/shells/
%{_kf6_plugindir}/attica_kde.so
%{_kf6_plugindir}/kf6/kded/device_automounter.so
%{_kf6_plugindir}/kf6/kded/screenreader.so
%{_kf6_plugindir}/kf6/krunner/
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.dwellclicker.so
%{_kf6_plugindir}/plasma/applets/org.kde.panel.so
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.keyboardlayout.so
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.kicker.so
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.kickoff.so
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.kimpanel.so
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.pager.so
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.showActivityManager.so
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.showdesktop.so
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.taskmanager.so
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.trash.so
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.windowlist.so
%dir %{_kf6_plugindir}/plasma/kcms/desktop/
%{_kf6_plugindir}/plasma/kcms/desktop/kcm_krunnersettings.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_access.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_activities.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_baloofile.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_desktoppaths.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_gamecontroller.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_mouse.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_touchpad.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_kded.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_keyboard.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_keys.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_landingpage.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_plasmasearch.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_smserver.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_splashscreen.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_tablet.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_touchscreen.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_workspace.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_clock.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_device_automounter.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_qtquicksettings.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_recentFiles.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_solid_actions.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_spellchecking.so
%{_kf6_qmldir}/org/kde/plasma/
%{_kf6_qmldir}/org/kde/private/
%dir %{_kf6_sharedir}/accounts/
%dir %{_kf6_sharedir}/accounts/providers
%dir %{_kf6_sharedir}/accounts/providers/kde/
%{_kf6_sharedir}/accounts/providers/kde/opendesktop.provider
%dir %{_kf6_sharedir}/accounts/services
%dir %{_kf6_sharedir}/accounts/services/kde/
%{_kf6_sharedir}/accounts/services/kde/opendesktop-rating.service
%{_kf6_sharedir}/kcm_recentFiles/
%{_kf6_sharedir}/kcmkeys/
%{_kf6_sharedir}/kcmsolidactions/
%{_kf6_sharedir}/kconf_update/50-krunner-activate-typing.sh
%{_kf6_sharedir}/kconf_update/50-krunner-activate-typing.upd
%{_kf6_sharedir}/kglobalaccel/org.kde.touchpadshortcuts.desktop
%{_kf6_sharedir}/kglobalaccel/org.kde.screenreader.desktop
%dir %{_kf6_sharedir}/sddm
%dir %{_kf6_sharedir}/sddm/themes
%{_kf6_sharedir}/sddm/themes/breeze/
%{_kf6_sharedir}/solid/
%{_kf6_iconsdir}/hicolor/*/devices/input-touchpad.*
%{_kf6_sharedir}/kcmmouse/
%exclude %{_kf6_plasmadir}/emoji/
%{_userunitdir}/plasma-kaccess.service

%files emojier
%{_kf6_applicationsdir}/org.kde.plasma.emojier.desktop
%{_kf6_bindir}/plasma-emojier
%{_kf6_plasmadir}/emoji/
%{_kf6_sharedir}/kglobalaccel/org.kde.plasma.emojier.desktop

%files -n plasma6-kimpanel-ibus
%{_libexecdir}/kimpanel-ibus-panel
%{_libexecdir}/kimpanel-ibus-panel-launcher

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en
%{_kf6_sharedir}/locale/sr*/LC_SCRIPTS/

%changelog
