#
# spec file for package plasma6-desktop
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


# TODO sort
# Internal QML imports
%global __requires_exclude qt6qmlimport\\((org\\.kde\\.plasma\\.shell\\.panel|org\\.kde\\.plasma\\.private).*
# %%global __requires_exclude qt6qmlimport\\((org\\.kde\\.private\\.kcms|org\\.kde\\.plasma\\.kcm|org\\.kde\\.desktopsession\\.private|org\\.kde\\.plasma\\.tablet|org\\.kde\\.plasma\\.touchscreen\\.kcm).*

%define kf6_version 6.2.0
%define qt6_version 6.6.0

%define rname plasma-desktop
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           plasma6-desktop
Version:        6.1.0
Release:        0
Summary:        The KDE Plasma Workspace Components
License:        GPL-2.0-only
URL:            https://www.kde.org/
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch100:       0001-Apply-branding-to-default-favorites.patch
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
# Due to KWinDBusInterface not having a cmake version config file, we need to BR kwin6-devel instead
# BuildRequires:  cmake(KWinDBusInterface) >= %%{_plasma6_bugfix}
# Also applies to ScreenSaverDBusInterface
# BuildRequires:  cmake(ScreenSaverDBusInterface) >= %%{_plasma6_bugfix}
BuildRequires:  kscreenlocker6-devel >= %{_plasma6_bugfix}
BuildRequires:  kwin6-devel >= %{_plasma6_bugfix}
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  update-desktop-files
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
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
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
BuildRequires:  cmake(LibColorCorrect) >= %{_plasma6_bugfix}
BuildRequires:  cmake(LibKWorkspace) >= %{_plasma6_bugfix}
BuildRequires:  cmake(LibNotificationManager) >= %{_plasma6_bugfix}
BuildRequires:  cmake(LibTaskManager) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Plasma) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Plasma5Support) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaActivities) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaActivitiesStats) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaQuick) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaWaylandProtocols) >= 1.10.0
BuildRequires:  cmake(Qt6Concurrent)  >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
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
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(scim)
BuildRequires:  pkgconfig(signon-oauth2plugin)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-atom)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-record)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-xinput)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xkbregistry)
%ifnarch s390x
BuildRequires:  pkgconfig(xorg-evdev)
BuildRequires:  pkgconfig(xorg-libinput)
BuildRequires:  pkgconfig(xorg-server)
%endif
BuildRequires:  xkeyboard-config
Requires:       plasma6-desktop-branding = %{version}
Requires:       plasma6-workspace >= %{_plasma6_bugfix}
# Required by the 'recent files' kcm
Requires:       qt6-sql-sqlite >= %{qt6_version}
# Hardcode versions of plasma6-framework-components, as upstream doesn't keep backwards compability there
%requires_ge    plasma6-framework-components
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
Requires:       (plasma6-kimpanel-scim if scim)

%if %{pkg_vcmp cmake(sdl2) >= 2.0.16}
%bcond_without gamecontroller_kcm
%endif

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

%package -n plasma6-kimpanel-scim
Summary:        Plasma 6 SCIM Configuration
Requires:       %{name} = %{version}

%description -n plasma6-kimpanel-scim
Plasma 6 Input Method Backend for SCIM (Smart Chinese/Common Input Method) support.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 \
%ifarch s390x
  -DBUILD_KCM_TOUCHPAD_X11:BOOL=FALSE \
  -DBUILD_KCM_MOUSE_X11=OFF
%endif

%kf6_build

%install
%kf6_install

# no devel files needed here
rm -rv %{buildroot}%{_kf6_sharedir}/dbus-1/interfaces/

%find_lang %{name} --all-name --with-html

%fdupes %{buildroot}%{_prefix}

%ldconfig_scriptlets

%files
%license COPYING*
%doc %lang(en) %{_kf6_htmldir}/en/*/
%{_kf6_applicationsdir}/kaccess.desktop
%{_kf6_applicationsdir}/kcm_access.desktop
%{_kf6_applicationsdir}/kcm_activities.desktop
%{_kf6_applicationsdir}/kcm_baloofile.desktop
%{_kf6_applicationsdir}/kcm_clock.desktop
%{_kf6_applicationsdir}/kcm_componentchooser.desktop
%{_kf6_applicationsdir}/kcm_desktoppaths.desktop
%if %{with gamecontroller_kcm}
%{_kf6_applicationsdir}/kcm_gamecontroller.desktop
%endif
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
%{_kf6_applicationsdir}/kcmspellchecking.desktop
%{_kf6_applicationsdir}/kde-mimeapps.list
%{_kf6_applicationsdir}/org.kde.knetattach.desktop
%{_kf6_applicationsdir}/kcm_mouse.desktop
%{_kf6_applicationsdir}/kcm_touchpad.desktop
%{_kf6_appstreamdir}/*.xml
%{_kf6_bindir}/kaccess
%{_kf6_bindir}/knetattach
%{_kf6_bindir}/krunner-plugininstaller
%{_kf6_bindir}/solid-action-desktop-gen
%{_kf6_bindir}/tastenbrett
%{_kf6_configdir}/autostart/kaccess.desktop
%{_kf6_configkcfgdir}/*.kcfg
%{_kf6_dbuspolicydir}/org.kde.kcontrol.kcmclock.conf
%{_kf6_debugdir}/*.categories
%{_kf6_knsrcfilesdir}/krunner.knsrc
%{_kf6_knsrcfilesdir}/ksplash.knsrc
%{_kf6_notificationsdir}/kaccess.notifyrc
%{_kf6_plasmadir}/layout-templates/
%{_kf6_plasmadir}/packages/
%{_kf6_plasmadir}/plasmoids/
%{_kf6_plasmadir}/shells/
%{_kf6_plugindir}/attica_kde.so
%{_kf6_plugindir}/kf6/kded/device_automounter.so
%{_kf6_plugindir}/kf6/kded/keyboard.so
%{_kf6_plugindir}/kf6/kded/kded_touchpad.so
%{_kf6_plugindir}/kf6/krunner/
%dir %{_kf6_plugindir}/plasma/kcms/desktop/
%{_kf6_plugindir}/plasma/kcms/desktop/kcm_krunnersettings.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_access.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_activities.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_baloofile.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_componentchooser.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_desktoppaths.so
%if %{with gamecontroller_kcm}
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_gamecontroller.so
%endif
%dir %{_kf6_plugindir}/plasma/kcminit
%{_kf6_plugindir}/plasma/kcminit/kcm_mouse_init.so
%{_kf6_plugindir}/plasma/kcminit/kcm_touchpad_init.so
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
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcmspellchecking.so
%{_kf6_qmldir}/org/kde/plasma/
%{_kf6_qmldir}/org/kde/private/
%dir %{_kf6_sharedir}/accounts/
%dir %{_kf6_sharedir}/accounts/providers
%dir %{_kf6_sharedir}/accounts/providers/kde/
%{_kf6_sharedir}/accounts/providers/kde/opendesktop.provider
%dir %{_kf6_sharedir}/accounts/services
%dir %{_kf6_sharedir}/accounts/services/kde/
%{_kf6_sharedir}/accounts/services/kde/opendesktop-rating.service
%{_kf6_sharedir}/dbus-1/system-services/org.kde.kcontrol.kcmclock.service
%{_kf6_sharedir}/kcm_recentFiles/
%{_kf6_sharedir}/kcmkeys/
%{_kf6_sharedir}/kcmsolidactions/
%{_kf6_sharedir}/polkit-1/actions/org.kde.kcontrol.kcmclock.policy
%dir %{_kf6_sharedir}/sddm
%dir %{_kf6_sharedir}/sddm/themes
%{_kf6_sharedir}/sddm/themes/breeze/
%{_kf6_sharedir}/solid/
%{_kf6_libexecdir}/kauth/kcmdatetimehelper
%{_kf6_iconsdir}/hicolor/*/devices/input-touchpad.*
%{_kf6_sharedir}/kcmmouse/
%{_kf6_notificationsdir}/kcm_touchpad.notifyrc
%exclude %{_kf6_plasmadir}/emoji/
%ifnarch s390 s390x
%{_kf6_bindir}/kapplymousetheme
%{_kf6_bindir}/kcm-touchpad-list-devices
%endif

%files emojier
%{_kf6_applicationsdir}/org.kde.plasma.emojier.desktop
%{_kf6_bindir}/plasma-emojier
%{_kf6_plasmadir}/emoji/
%{_kf6_sharedir}/kglobalaccel/org.kde.plasma.emojier.desktop

%files -n plasma6-kimpanel-ibus
%{_libexecdir}/kimpanel-ibus-panel
%{_libexecdir}/kimpanel-ibus-panel-launcher

%files -n plasma6-kimpanel-scim
%{_libexecdir}/kimpanel-scim-panel

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en
%{_kf6_sharedir}/locale/sr*/LC_SCRIPTS/

%changelog
