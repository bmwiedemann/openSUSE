#
# spec file for package kdeplasma6-addons
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

%define rname kdeplasma-addons
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kdeplasma6-addons
Version:        6.1.2
Release:        0
Summary:        Additional Plasma6 Widgets
License:        GPL-2.0-or-later AND LGPL-2.1-only AND GPL-3.0-only
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Declarative) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6Holidays) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Runner) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6Sonnet) >= %{kf6_version}
BuildRequires:  cmake(KF6UnitConversion) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Plasma) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Plasma5Support) >= %{_plasma6_bugfix}
BuildRequires:  cmake(PlasmaQuick) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
%ifarch x86_64 aarch64 riscv64
BuildRequires:  cmake(Qt6WebEngineQuick) >= %{qt6_version}
%endif
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
Requires:       kf6-kitemmodels-imports >= %{kf6_version}
Requires:       kf6-purpose >= %{kf6_version}
Requires:       kirigami-addons6
Provides:       plasma-addons = %{version}
Obsoletes:      plasma-addons < %{version}
Provides:       plasma5-addons = %{version}
Obsoletes:      plasma5-addons < %{version}
Obsoletes:      plasma5-addons-lang < %{version}

%description
Additional plasmoids from upstream for use on the Plasma workspace.

%package devel
Summary:        Additional plasmoid widgets - development files
Requires:       kdeplasma6-addons = %{version}
Conflicts:      plasma5-addons-devel

%description devel
This package contains development files to develop additional widgets for
the Plasma desktop.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}
# Waiting for boo#1226306
echo > kdeds/kameleon/CMakeLists.txt

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets

%files
%license LICENSES/*
%{_kf6_appstreamdir}/*.xml
# %%{_kf6_dbuspolicydir}/org.kde.kameleonhelper.conf
%{_kf6_debugdir}/kdeplasma-addons.categories
%ifarch x86_64 aarch64 riscv64
%{_kf6_iconsdir}/hicolor/scalable/apps/accessories-dictionary.svgz
%endif
%{_kf6_iconsdir}/hicolor/scalable/apps/fifteenpuzzle.svgz
%{_kf6_knsrcfilesdir}/comic.knsrc
%{_kf6_libdir}/libplasmapotdprovidercore.so.*
# %%{_kf6_libexecdir}/kauth/kameleonhelper
%{_kf6_notificationsdir}/plasma_applet_timer.notifyrc
%{_kf6_plasmadir}/desktoptheme/
%{_kf6_plasmadir}/plasmoids/
%{_kf6_plasmadir}/wallpapers/
# %%{_kf6_plugindir}/kf6/kded/kameleon.so
%dir %{_kf6_plugindir}/kf6/krunner
%{_kf6_plugindir}/kf6/krunner/*
%dir %{_kf6_plugindir}/kf6/packagestructure
%{_kf6_plugindir}/kf6/packagestructure/plasma_comic.so
%dir %{_kf6_plugindir}/kwin
%dir %{_kf6_plugindir}/kwin/effects
%dir %{_kf6_plugindir}/kwin/effects/configs
%{_kf6_plugindir}/kwin/effects/configs/kwin_cube_config.so
%{_kf6_plugindir}/plasma/applets/*
%{_kf6_plugindir}/plasmacalendarplugins/
%{_kf6_plugindir}/potd/
%{_kf6_qmldir}/org/kde/plasma/*
%{_kf6_qmldir}/org/kde/plasmacalendar/
# %%{_kf6_sharedir}/dbus-1/system-services/org.kde.kameleonhelper.service
%{_kf6_sharedir}/kwin/
# %%{_kf6_sharedir}/polkit-1/actions/org.kde.kameleonhelper.policy

%files devel
%dir %{_includedir}/plasma
%{_includedir}/plasma/potdprovider/
%{_kf6_cmakedir}/PlasmaPotdProvider/
%{_kf6_libdir}/libplasmapotdprovidercore.so
%{_kf6_sharedir}/kdevappwizard/templates/plasmapotdprovider.tar.bz2

%files lang -f %{name}.lang

%changelog
