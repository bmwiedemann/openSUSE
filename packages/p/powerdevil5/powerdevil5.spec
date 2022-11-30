#
# spec file for package powerdevil5
#
# Copyright (c) 2022 SUSE LLC
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


%bcond_without released
Name:           powerdevil5
Version:        5.26.4
Release:        0
# Full Plasma 5 version (e.g. 5.8.95)
%{!?_plasma5_bugfix: %define _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.8.95 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        KDE Power Management module
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            http://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/powerdevil-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/powerdevil-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  extra-cmake-modules >= 1.2.0
BuildRequires:  kf5-filesystem
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz
BuildRequires:  cmake(KF5Activities)
BuildRequires:  cmake(KF5Auth)
BuildRequires:  cmake(KF5BluezQt)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IdleTime)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5NetworkManagerQt)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5Screen) >= %{_plasma5_version}
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5Wayland)
#!BuildIgnore:  kwin5
BuildRequires:  cmake(LibKWorkspace) >= %{_plasma5_version}
BuildRequires:  cmake(Qt5DBus) >= 5.4.0
BuildRequires:  cmake(Qt5Widgets) >= 5.4.0
BuildRequires:  cmake(Qt5X11Extras) >= 5.4.0
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-dpms)
BuildRequires:  pkgconfig(xcb-randr)
#PrepareForSleep is added to systemd 198, and with Plasma 5.2, will be unconditionaly called
Requires:       systemd >= 198
%requires_ge plasma5-workspace-libs
Recommends:     %{name}-lang
Conflicts:      kdebase4-workspace < 5.3.0
# Needed for battery / brightness detection
Recommends:     upower
# For switching power profiles
Recommends:     power-profiles-daemon

%description
KDE Power Management module. Provides kded daemon,
DBus helper and KCM for configuring Power settings.

%lang_package

%prep
%autosetup -p1 -n powerdevil-%{version}

%build
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
  %cmake_build

%install
  %kf5_makeinstall -C build
%if %{with released}
  %kf5_find_lang
  %kf5_find_htmldocs
%endif

  rm -rfv %{buildroot}%{_kf5_libdir}/libpowerdevil{ui,core,configcommonprivate}.so

%post
/sbin/ldconfig
%{systemd_user_post plasma-powerdevil.service}

%preun
%{systemd_user_preun plasma-powerdevil.service}

%postun
/sbin/ldconfig
%{systemd_user_postun plasma-powerdevil.service}

%files
%license COPYING*
%{_kf5_applicationsdir}/kcm_powerdevilactivitiesconfig.desktop
%{_kf5_applicationsdir}/kcm_powerdevilglobalconfig.desktop
%{_kf5_applicationsdir}/kcm_powerdevilprofilesconfig.desktop
%{_kf5_debugdir}/powerdevil.categories
%{_kf5_libdir}/libpowerdevilconfigcommonprivate.so.*
%{_kf5_libdir}/libpowerdevilcore.so.*
%{_kf5_libdir}/libpowerdevilui.so.*
%doc %{_kf5_htmldir}/en
%dir %{_kf5_plugindir}/kf5/
%dir %{_kf5_plugindir}/powerdevil/
%dir %{_kf5_plugindir}/powerdevil/action
%dir %{_kf5_plugindir}/kf5/powerdevil/
%dir %{_kf5_plugindir}/plasma
%dir %{_kf5_plugindir}/plasma/kcms/
%dir %{_kf5_plugindir}/plasma/kcms/systemsettings_qwidgets
%{_kf5_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_powerdevilactivitiesconfig.so
%{_kf5_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_powerdevilglobalconfig.so
%{_kf5_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_powerdevilprofilesconfig.so
%{_kf5_plugindir}/powerdevil/action/powerdevil_brightnesscontrolaction.so
%{_kf5_plugindir}/powerdevil/action/powerdevil_dimdisplayaction.so
%{_kf5_plugindir}/powerdevil/action/powerdevil_dpmsaction.so
%{_kf5_plugindir}/powerdevil/action/powerdevil_handlebuttoneventsaction.so
%{_kf5_plugindir}/powerdevil/action/powerdevil_keyboardbrightnesscontrolaction.so
%{_kf5_plugindir}/powerdevil/action/powerdevil_powerprofileaction.so
%{_kf5_plugindir}/powerdevil/action/powerdevil_runscriptaction.so
%{_kf5_plugindir}/powerdevil/action/powerdevil_suspendsessionaction.so
%{_kf5_plugindir}/powerdevil/action/powerdevil_wirelesspowersavingaction.so
%{_kf5_plugindir}/kf5/powerdevil/powerdevilupowerbackend.so
%{_kf5_plugindir}/powerdevilbrightnesscontrolaction_config.so
%{_kf5_plugindir}/powerdevildimdisplayaction_config.so
%{_kf5_plugindir}/powerdevildpmsaction_config.so
%{_kf5_plugindir}/powerdevilhandlebuttoneventsaction_config.so
%{_kf5_plugindir}/powerdevilkeyboardbrightnesscontrolaction_config.so
%{_kf5_plugindir}/powerdevilrunscriptaction_config.so
%{_kf5_plugindir}/powerdevilpowerprofileaction_config.so
%{_kf5_plugindir}/powerdevilsuspendsessionaction_config.so
%{_kf5_plugindir}/powerdevilwirelesspowersavingaction_config.so
%{_kf5_notifydir}/
%{_kf5_sharedir}/dbus-1/system-services/org.kde.powerdevil.backlighthelper.service
%{_kf5_dbuspolicydir}/org.kde.powerdevil.backlighthelper.conf
%{_kf5_sharedir}/polkit-1/actions/org.kde.powerdevil.backlighthelper.policy
%{_kf5_sharedir}/dbus-1/system-services/org.kde.powerdevil.discretegpuhelper.service
%{_kf5_dbuspolicydir}/org.kde.powerdevil.discretegpuhelper.conf
%{_kf5_sharedir}/polkit-1/actions/org.kde.powerdevil.discretegpuhelper.policy
%{_kf5_sharedir}/dbus-1/system-services/org.kde.powerdevil.chargethresholdhelper.service
%{_kf5_sharedir}/dbus-1/system.d/org.kde.powerdevil.chargethresholdhelper.conf
%{_kf5_sharedir}/polkit-1/actions/org.kde.powerdevil.chargethresholdhelper.policy
%{_libexecdir}/kauth/
%{_libexecdir}/org_kde_powerdevil
%{_userunitdir}/plasma-powerdevil.service

%{_kf5_configdir}/autostart/powerdevil.desktop

%if %{with released}
%files lang -f %{name}.lang
%endif

%changelog
