#
# spec file for package powerdevil6
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


%define kf6_version 6.2.0
%define qt6_version 6.6.0

%define rname powerdevil
%bcond_without released
Name:           powerdevil6
Version:        6.1.0
Release:        0
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        KDE Power Management module
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
# PATCH-BREAK-OPENSUSE waiting for review (boo#1226424)
Patch1:         0001-Revert-Added-setting-for-battery-conservation-mode-L.patch
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
# Needed by FindLibcap.cmake
BuildRequires:  libcap-progs
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IdleTime) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6NotifyConfig) >= %{kf6_version}
BuildRequires:  cmake(KF6Screen) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(LibKWorkspace) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaActivities) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(ddcutil)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-dpms)
BuildRequires:  pkgconfig(xcb-randr)
Requires:       kf6-kidletime-plugins
#PrepareForSleep is added to systemd 198, and with Plasma 5.2, will be unconditionaly called
Requires:       systemd >= 198
%requires_ge    plasma6-workspace-libs
Provides:       powerdevil5 = %{version}
Obsoletes:      powerdevil5 < %{version}
Obsoletes:      powerdevil5-lang < %{version}
# Needed for battery / brightness detection
Recommends:     upower
# For i2c dev handling and permissions
Recommends:     ddcutil-i2c-udev-rules
# For switching power profiles
Recommends:     power-profiles-daemon

%description
KDE Power Management module. Provides kded daemon, DBus helper and KCM for
configuring Power settings.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name --with-html

rm -rv %{buildroot}%{_kf6_libdir}/libpowerdevil{core,configcommonprivate}.so

%post
%ldconfig
%{systemd_user_post plasma-powerdevil.service plasma-powerprofile-osd.service}

%preun
%{systemd_user_preun plasma-powerdevil.service plasma-powerprofile-osd.service}

%postun
%ldconfig
%{systemd_user_postun plasma-powerdevil.service plasma-powerprofile-osd.service}

%files
%license COPYING*
%doc %{_kf6_htmldir}/en/kcontrol/
%{_kf6_applicationsdir}/kcm_powerdevilprofilesconfig.desktop
%{_kf6_configdir}/autostart/powerdevil.desktop
%{_kf6_dbuspolicydir}/org.kde.powerdevil.backlighthelper.conf
%{_kf6_dbuspolicydir}/org.kde.powerdevil.discretegpuhelper.conf
%{_kf6_debugdir}/powerdevil.categories
%{_kf6_libdir}/libpowerdevilconfigcommonprivate.so.*
%{_kf6_libdir}/libpowerdevilcore.so.*
%{_kf6_notificationsdir}/powerdevil.notifyrc
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_powerdevilprofilesconfig.so
%dir %{_kf6_plugindir}/powerdevil/
%dir %{_kf6_plugindir}/powerdevil/action
%{_kf6_plugindir}/powerdevil/action/powerdevil_brightnesscontrolaction.so
%{_kf6_plugindir}/powerdevil/action/powerdevil_dimdisplayaction.so
%{_kf6_plugindir}/powerdevil/action/powerdevil_dpmsaction.so
%{_kf6_plugindir}/powerdevil/action/powerdevil_handlebuttoneventsaction.so
%{_kf6_plugindir}/powerdevil/action/powerdevil_keyboardbrightnesscontrolaction.so
%{_kf6_plugindir}/powerdevil/action/powerdevil_powerprofileaction.so
%{_kf6_plugindir}/powerdevil/action/powerdevil_runscriptaction.so
%{_kf6_plugindir}/powerdevil/action/powerdevil_suspendsessionaction.so
%{_kf6_sharedir}/dbus-1/services/org.kde.powerdevil.powerProfileOsdService.service
%{_kf6_sharedir}/dbus-1/system-services/org.kde.powerdevil.backlighthelper.service
%{_kf6_sharedir}/dbus-1/system-services/org.kde.powerdevil.chargethresholdhelper.service
%{_kf6_sharedir}/dbus-1/system-services/org.kde.powerdevil.discretegpuhelper.service
%{_kf6_sharedir}/dbus-1/system.d/org.kde.powerdevil.chargethresholdhelper.conf
%{_kf6_sharedir}/polkit-1/actions/org.kde.powerdevil.backlighthelper.policy
%{_kf6_sharedir}/polkit-1/actions/org.kde.powerdevil.chargethresholdhelper.policy
%{_kf6_sharedir}/polkit-1/actions/org.kde.powerdevil.discretegpuhelper.policy
%{_kf6_libexecdir}/kauth/backlighthelper
%{_kf6_libexecdir}/kauth/chargethresholdhelper
%{_kf6_libexecdir}/kauth/discretegpuhelper
%{_libexecdir}/org_kde_powerdevil
%{_libexecdir}/power_profile_osd_service
%{_userunitdir}/plasma-powerdevil.service
%{_userunitdir}/plasma-powerprofile-osd.service

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kcontrol

%changelog
