#
# spec file for package plasma6-print-manager
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 24.9.90 Raymond Wooninck <tittiatcoke@gmail.com>
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

%define rname print-manager
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           plasma6-print-manager
Version:        6.1.0
Release:        0
Summary:        Tools for managing print jobs and printers
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch1:         0001-Revert-Require-CUPS-version-2.4.x.patch
BuildRequires:  cups-devel >= 1.5
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  system-config-printer-dbus-service
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(Plasma) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kirigami-addons6 >= 0.10
Requires:       system-config-printer-dbus-service
Recommends:     samba-client
Obsoletes:      print-manager5 < %{version}
Provides:       print-manager5 = %{version}
# 23.08.4 in factory, 24.04.70git(+date) in unstable repo
Provides:       kde-print-manager = 24.05
Obsoletes:      kde-print-manager < 24.05
Obsoletes:      kde-print-manager-lang < 24.05
Provides:       dbus(com.redhat.NewPrinterNotification)

%description
plasma6-print-manager provides tools for managing print jobs and printers.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc README.md
%{_kf6_applicationsdir}/kcm_printer_manager.desktop
%{_kf6_applicationsdir}/org.kde.ConfigurePrinter.desktop
%{_kf6_applicationsdir}/org.kde.PrintQueue.desktop
%{_kf6_applicationsdir}/org.kde.kde-add-printer.desktop
%{_kf6_appstreamdir}/org.kde.plasma.printmanager.appdata.xml
%{_kf6_appstreamdir}/org.kde.print-manager.metainfo.xml
%{_kf6_bindir}/configure-printer
%{_kf6_bindir}/kde-add-printer
%{_kf6_bindir}/kde-print-queue
%{_kf6_debugdir}/pmlogs.categories
%{_kf6_libdir}/libkcupslib.so.*
%{_kf6_notificationsdir}/printmanager.notifyrc
%dir %{_kf6_plasmadir}/plasmoids
%{_kf6_plasmadir}/plasmoids/org.kde.plasma.printmanager/
%{_kf6_plugindir}/kf6/kded/printmanager.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_printer_manager.so
%{_kf6_qmldir}/org/kde/plasma/printmanager/

%files lang -f %{name}.lang

%changelog
