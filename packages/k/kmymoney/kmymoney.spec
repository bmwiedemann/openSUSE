#
# spec file for package kmymoney
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


%define kf6_version 6.1.0
%define qt6_version 6.7.0

%bcond_without released
Name:           kmymoney
Version:        5.2.2
Release:        0
Summary:        A Personal Finance Manager by KDE
License:        GPL-2.0-only OR GPL-3.0-only
URL:            https://www.kmymoney.org/
Source0:        https://download.kde.org/stable/kmymoney/%{version}/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/kmymoney/%{version}/%{name}-%{version}.tar.xz.sig
Source2:        kmymoney.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libofx-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  qt6-sql-private-devel >= %{qt6_version}
BuildRequires:  cmake(KChart6)
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6Contacts) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6Holidays) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemViews) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6IdentityManagementCore)
BuildRequires:  cmake(LibAlkimia6) >= 8.2.1
BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(QGpgmeQt6)
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  cmake(aqbanking) >= 6.8.4
BuildRequires:  cmake(gwengui-cpp)
BuildRequires:  cmake(gwengui-qt6)
BuildRequires:  cmake(gwenhywfar) >= 5.14.1
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(sqlcipher)
BuildRequires:  pkgconfig(sqlite3)
Requires:       qt6-sql-sqlite >= %{qt6_version}
# For users of KDE:Unstable:Extra
Provides:       kmymoney5 = %{version}
Obsoletes:      kmymoney5 < %{version}
Provides:       kmymoney-doc = %{version}
Obsoletes:      kmymoney-doc < %{version}

%description
KMyMoney is a Personal Finance Manager by KDE. It operates
similar to Quicken, supports various account types, categorization
of expenses, multiple currencies, online banking support via QIF,
OFX and HBCI, budgeting and a rich set of reports.

%package devel
Summary:        Development Files for KMyMoney
Requires:       kmymoney = %{version}

%description devel
Development files and headers need to build software using KMyMoney.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang %{name} --with-html --with-man

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc %lang(en) %{_kf6_htmldir}/en/kmymoney/
%doc README.md
%dir %{_kf6_iconsdir}/hicolor/1024x1024
%dir %{_kf6_iconsdir}/hicolor/1024x1024/apps
%dir %{_kf6_iconsdir}/hicolor/1024x1024/mimetypes
%dir %{_kf6_iconsdir}/hicolor/20x20
%dir %{_kf6_iconsdir}/hicolor/20x20/apps
%{_datadir}/mime/packages/x-kmymoney.xml
%{_kf6_applicationsdir}/org.kde.kmymoney.desktop
%{_kf6_appstreamdir}/org.kde.kmymoney.appdata.xml
%{_kf6_bindir}/kmymoney
%{_kf6_configkcfgdir}/
%{_kf6_iconsdir}/hicolor/*/*/*
%{_kf6_libdir}/libkmm_base_dialogs.so.*
%{_kf6_libdir}/libkmm_base_widgets.so.*
%{_kf6_libdir}/libkmm_codec.so.*
%{_kf6_libdir}/libkmm_csvimportercore.so.*
%{_kf6_libdir}/libkmm_extended_dialogs.so.*
%{_kf6_libdir}/libkmm_gpgfile.so.*
%{_kf6_libdir}/libkmm_icons.so.*
%{_kf6_libdir}/libkmm_keychain.so.*
%{_kf6_libdir}/libkmm_menuactionexchanger.so.*
%{_kf6_libdir}/libkmm_menus.so.*
%{_kf6_libdir}/libkmm_models.so.*
%{_kf6_libdir}/libkmm_mymoney.so.*
%{_kf6_libdir}/libkmm_payeeidentifier.so.*
%{_kf6_libdir}/libkmm_plugin.so.*
%{_kf6_libdir}/libkmm_printer.so.*
%{_kf6_libdir}/libkmm_selections.so.*
%{_kf6_libdir}/libkmm_settings.so.*
%{_kf6_libdir}/libkmm_templates.so.*
%{_kf6_libdir}/libkmm_webconnect.so.*
%{_kf6_libdir}/libkmm_widgets.so.*
%{_kf6_libdir}/libkmm_wizard.so.*
%{_kf6_libdir}/libkmm_yesno.so.*
%{_kf6_libdir}/libonlinetask_interfaces.so.*
%{_kf6_plugindir}/
%{_kf6_sharedir}/checkprinting/
%{_kf6_sharedir}/kconf_update/
%{_mandir}/man1/kmymoney.1%{?ext_man}

%files devel
%{_includedir}/kmymoney/
%{_kf6_libdir}/libkmm_base_dialogs.so
%{_kf6_libdir}/libkmm_base_widgets.so
%{_kf6_libdir}/libkmm_codec.so
%{_kf6_libdir}/libkmm_csvimportercore.so
%{_kf6_libdir}/libkmm_extended_dialogs.so
%{_kf6_libdir}/libkmm_gpgfile.so
%{_kf6_libdir}/libkmm_icons.so
%{_kf6_libdir}/libkmm_keychain.so
%{_kf6_libdir}/libkmm_menuactionexchanger.so
%{_kf6_libdir}/libkmm_menus.so
%{_kf6_libdir}/libkmm_models.so
%{_kf6_libdir}/libkmm_mymoney.so
%{_kf6_libdir}/libkmm_payeeidentifier.so
%{_kf6_libdir}/libkmm_plugin.so
%{_kf6_libdir}/libkmm_printer.so
%{_kf6_libdir}/libkmm_selections.so
%{_kf6_libdir}/libkmm_settings.so
%{_kf6_libdir}/libkmm_templates.so
%{_kf6_libdir}/libkmm_webconnect.so
%{_kf6_libdir}/libkmm_widgets.so
%{_kf6_libdir}/libkmm_wizard.so
%{_kf6_libdir}/libkmm_yesno.so
%{_kf6_libdir}/libonlinetask_interfaces.so

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kmymoney/

%changelog
