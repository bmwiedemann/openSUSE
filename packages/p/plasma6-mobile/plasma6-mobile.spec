#
# spec file for package plasma6-mobile
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


# org.kde.phone.homescreen, org.kde.plasma.phone.taskpanel and org.kde.private.mobile.homescreen.folio are internal,
# MeeGo.QOfono is optional and not packaged yet
%global __requires_exclude qmlimport\\((org\\.kde\\.phone\\.homescreen|org\\.kde\\.plasma\\.phone\\.taskpanel|org\\.kde\\.private\\.mobile\\.homescreen\\.folio|MeeGo\\.QOfono|).*

%define kf6_version 6.2.0
%define qt6_version 6.6.0

%define rname plasma-mobile
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           plasma6-mobile
Version:        6.1.1
Release:        0
# Full Plasma 6 version (e.g. 5.9.3)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        Plasma shell for mobile devices
License:        GPL-2.0-or-later
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6ModemManagerQt) >= %{kf6_version}
BuildRequires:  cmake(KF6NetworkManagerQt) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Package) >= %{kf6_version}
BuildRequires:  cmake(KF6Screen) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KPipeWire) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KWayland) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KWin) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KWinDBusInterface) >= %{_plasma6_bugfix}
BuildRequires:  cmake(LibKWorkspace) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Plasma) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaQuick) >= %{_plasma6_bugfix}
BuildRequires:  cmake(QCoro6)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sensors) >= %{qt6_version}
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(xcb)
# For plasma-open-settings
Requires:       kde-cli-tools6 >= %{_plasma6_bugfix}
Provides:       plasma5-mobile = %{version}
Obsoletes:      plasma5-mobile < %{version}
Obsoletes:      plasma5-mobile-lang < %{version}
# Forced on startup
Requires:       qqc2-breeze-style6
# QML imports
Requires:       kf6-bluez-qt-imports >= %{kf6_version}
Requires:       kf6-kdeclarative-imports >= %{kf6_version}
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kwin6 >= %{_plasma6_bugfix}
Requires:       milou6 >= %{_plasma6_bugfix}
Requires:       plasma6-nano >= %{_plasma6_bugfix}
Requires:       plasma6-nm >= %{_plasma6_bugfix}
Requires:       plasma6-pa >= %{_plasma6_bugfix}
Requires:       plasma6-workspace >= %{_plasma6_bugfix}
Requires:       qt6-declarative-imports >= %{qt6_version}
Requires:       qt6-qt5compat-imports >= %{qt6_version}
Requires:       qt6-wayland >= %{qt6_version}
# For KCM .desktop files
Requires:       systemsettings6 >= %{_plasma6_bugfix}

%description
Plasma shell for mobile devices.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%fdupes %{buildroot}

%files
%license LICENSES/*
%{_kf6_applicationsdir}/kcm_cellular_network.desktop
%{_kf6_applicationsdir}/kcm_mobile_hotspot.desktop
%{_kf6_applicationsdir}/kcm_mobile_info.desktop
%{_kf6_applicationsdir}/kcm_mobile_onscreenkeyboard.desktop
%{_kf6_applicationsdir}/kcm_mobile_power.desktop
%{_kf6_applicationsdir}/kcm_mobile_time.desktop
%{_kf6_applicationsdir}/kcm_mobile_wifi.desktop
%{_kf6_applicationsdir}/kcm_mobileshell.desktop
%{_kf6_appstreamdir}/org.kde.breeze.mobile.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.mobile.homescreen.folio.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.mobile.homescreen.halcyon.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.mobile.panel.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.mobile.taskpanel.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.mobileinitialstart.cellular.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.mobileinitialstart.finished.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.mobileinitialstart.prepare.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.mobileinitialstart.time.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.mobileinitialstart.wifi.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.mobileshell.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.quicksetting.airplanemode.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.quicksetting.audio.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.quicksetting.battery.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.quicksetting.bluetooth.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.quicksetting.caffeine.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.quicksetting.donotdisturb.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.quicksetting.flashlight.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.quicksetting.hotspot.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.quicksetting.keyboardtoggle.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.quicksetting.mobiledata.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.quicksetting.nightcolor.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.quicksetting.powermenu.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.quicksetting.screenrotation.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.quicksetting.screenshot.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.quicksetting.settingsapp.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.quicksetting.wifi.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.quicksettings.docked.appdata.xml
%{_kf6_bindir}/plasma-mobile-envmanager
%{_kf6_bindir}/plasma-mobile-initial-start
%{_kf6_bindir}/startplasmamobile
%{_kf6_dbusinterfacesdir}/org.kde.plasmashell.Mobile.xml
%{_kf6_notificationsdir}/plasma_mobile_quicksetting_screenshot.notifyrc
%dir %{_kf6_plasmadir}/look-and-feel
%{_kf6_plasmadir}/look-and-feel/org.kde.breeze.mobile/
%dir %{_kf6_plasmadir}/mobileinitialstart
%{_kf6_plasmadir}/mobileinitialstart/org.kde.plasma.mobileinitialstart.cellular/
%{_kf6_plasmadir}/mobileinitialstart/org.kde.plasma.mobileinitialstart.finished/
%{_kf6_plasmadir}/mobileinitialstart/org.kde.plasma.mobileinitialstart.prepare/
%{_kf6_plasmadir}/mobileinitialstart/org.kde.plasma.mobileinitialstart.time/
%{_kf6_plasmadir}/mobileinitialstart/org.kde.plasma.mobileinitialstart.wifi/
%dir %{_kf6_plasmadir}/plasmoids/
%{_kf6_plasmadir}/plasmoids/org.kde.plasma.mobile.homescreen.folio/
%{_kf6_plasmadir}/plasmoids/org.kde.plasma.mobile.homescreen.halcyon/
%{_kf6_plasmadir}/plasmoids/org.kde.plasma.mobile.panel/
%{_kf6_plasmadir}/plasmoids/org.kde.plasma.mobile.taskpanel/
%dir %{_kf6_plasmadir}/quicksettings
%{_kf6_plasmadir}/quicksettings/org.kde.plasma.quicksetting.airplanemode/
%{_kf6_plasmadir}/quicksettings/org.kde.plasma.quicksetting.audio/
%{_kf6_plasmadir}/quicksettings/org.kde.plasma.quicksetting.battery/
%{_kf6_plasmadir}/quicksettings/org.kde.plasma.quicksetting.bluetooth/
%{_kf6_plasmadir}/quicksettings/org.kde.plasma.quicksetting.caffeine/
%{_kf6_plasmadir}/quicksettings/org.kde.plasma.quicksetting.donotdisturb/
%{_kf6_plasmadir}/quicksettings/org.kde.plasma.quicksetting.flashlight/
%{_kf6_plasmadir}/quicksettings/org.kde.plasma.quicksetting.hotspot/
%{_kf6_plasmadir}/quicksettings/org.kde.plasma.quicksetting.keyboardtoggle/
%{_kf6_plasmadir}/quicksettings/org.kde.plasma.quicksetting.mobiledata/
%{_kf6_plasmadir}/quicksettings/org.kde.plasma.quicksetting.nightcolor/
%{_kf6_plasmadir}/quicksettings/org.kde.plasma.quicksetting.powermenu/
%{_kf6_plasmadir}/quicksettings/org.kde.plasma.quicksetting.screenrotation/
%{_kf6_plasmadir}/quicksettings/org.kde.plasma.quicksetting.screenshot/
%{_kf6_plasmadir}/quicksettings/org.kde.plasma.quicksetting.settingsapp/
%{_kf6_plasmadir}/quicksettings/org.kde.plasma.quicksetting.wifi/
%{_kf6_plasmadir}/quicksettings/org.kde.plasma.quicksettings.docked/
%dir %{_kf6_plasmadir}/shells
%{_kf6_plasmadir}/shells/org.kde.plasma.mobileshell/
%{_kf6_plugindir}/kf6/kded/kded_plasma_mobile_autodetect_apn.so
%{_kf6_plugindir}/kf6/kded/kded_plasma_mobile_start.so
%dir %{_kf6_plugindir}/kwin
%dir %{_kf6_plugindir}/kwin/effects
%dir %{_kf6_plugindir}/kwin/effects/plugins
%{_kf6_plugindir}/kwin/effects/plugins/mobiletaskswitcher.so
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.mobile.homescreen.folio.so
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.mobile.homescreen.halcyon.so
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.mobile.panel.so
%{_kf6_plugindir}/plasma/applets/org.kde.plasma.mobile.taskpanel.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_cellular_network.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_mobile_hotspot.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_mobile_info.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_mobile_onscreenkeyboard.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_mobile_power.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_mobile_time.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_mobile_wifi.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_mobileshell.so
%dir %{_kf6_qmldir}/org/kde/plasma/
%{_kf6_qmldir}/org/kde/plasma/mm/
%{_kf6_qmldir}/org/kde/plasma/mobileinitialstart/
%dir %{_kf6_qmldir}/org/kde/plasma/private/
%{_kf6_qmldir}/org/kde/plasma/private/mobileshell/
%dir %{_kf6_qmldir}/org/kde/plasma/quicksetting/
%{_kf6_qmldir}/org/kde/plasma/quicksetting/flashlight/
%{_kf6_qmldir}/org/kde/plasma/quicksetting/nightcolor/
%{_kf6_qmldir}/org/kde/plasma/quicksetting/powermenu/
%{_kf6_qmldir}/org/kde/plasma/quicksetting/screenrotation/
%{_kf6_qmldir}/org/kde/plasma/quicksetting/screenshot/
%{_kf6_qmldir}/org/kde/private/mobile/
%dir %{_kf6_sharedir}/kwin
%dir %{_kf6_sharedir}/kwin/effects
%{_kf6_sharedir}/kwin/effects/mobiletaskswitcher/
%dir %{_kf6_sharedir}/kwin/scripts
%{_kf6_sharedir}/kwin/scripts/convergentwindows/
%dir %{_kf6_sharedir}/plasma-mobile-apn-info
%{_kf6_sharedir}/plasma-mobile-apn-info/apns-full-conf.xml
%dir %{_kf6_sharedir}/wayland-sessions
%{_kf6_sharedir}/wayland-sessions/plasma-mobile.desktop

%files lang -f %{name}.lang

%changelog
