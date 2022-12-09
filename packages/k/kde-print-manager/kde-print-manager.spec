#
# spec file for package kde-print-manager
#
# Copyright (c) 2022 SUSE LLC
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


%define rname print-manager
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kde-print-manager
Version:        22.12.0
Release:        0
Summary:        Tools for managing print jobs and printers
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  cups
BuildRequires:  cups-backends
BuildRequires:  cups-client
BuildRequires:  cups-devel
BuildRequires:  cups-pk-helper
BuildRequires:  extra-cmake-modules
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Designer)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Widgets)
Conflicts:      kde4-print-manager
Obsoletes:      kde4-print-manager < %{version}
Obsoletes:      print-manager5 < %{version}
Provides:       print-manager5 = %{version}
Provides:       dbus(com.redhat.NewPrinterNotification)

%description
kde-print-manager provides tools for managing print jobs and printers.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf5 -d build -- -DCUPS_INCLUDE_DIR=%{_includedir}/cups
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%suse_update_desktop_file -r org.kde.PrintQueue Utility DesktopUtility
%suse_update_desktop_file -r org.kde.kde-add-printer Utility DesktopUtility

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES/*
%doc README
%dir %{_kf5_plasmadir}/plasmoids
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/kded
%dir %{_kf5_plugindir}/plasma
%dir %{_kf5_plugindir}/plasma/kcms
%dir %{_kf5_plugindir}/plasma/kcms/systemsettings_qwidgets
%{_kf5_applicationsdir}/kcm_printer_manager.desktop
%{_kf5_applicationsdir}/org.kde.ConfigurePrinter.desktop
%{_kf5_applicationsdir}/org.kde.PrintQueue.desktop
%{_kf5_applicationsdir}/org.kde.kde-add-printer.desktop
%{_kf5_appstreamdir}/org.kde.plasma.printmanager.appdata.xml
%{_kf5_appstreamdir}/org.kde.print-manager.metainfo.xml
%{_kf5_bindir}/configure-printer
%{_kf5_bindir}/kde-add-printer
%{_kf5_bindir}/kde-print-queue
%{_kf5_libdir}/libkcupslib.so*
%{_kf5_notifydir}/printmanager.notifyrc
%{_kf5_plasmadir}/plasmoids/org.kde.plasma.printmanager/
%{_kf5_plugindir}/kf5/kded/printmanager.so
%{_kf5_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_printer_manager.so
%{_kf5_qmldir}/org/kde/plasma/printmanager/

%files lang -f %{name}.lang

%changelog
