#
# spec file for package korganizer
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0
%define kpim6_version 6.1.1

%bcond_without released
Name:           korganizer
Version:        24.05.1
Release:        0
Summary:        Personal Organizer
License:        GPL-2.0-only
URL:            https://apps.kde.org/korganizer
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6CalendarCore) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6Contacts) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6Holidays) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemViews) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6UserFeedback) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KPim6Akonadi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiCalendar) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiContactWidgets) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiNotes) >= %{kpim6_version}
BuildRequires:  cmake(KPim6CalendarSupport) >= %{kpim6_version}
BuildRequires:  cmake(KPim6CalendarUtils) >= %{kpim6_version}
BuildRequires:  cmake(KPim6EventViews) >= %{kpim6_version}
BuildRequires:  cmake(KPim6IdentityManagementCore) >= %{kpim6_version}
BuildRequires:  cmake(KPim6IncidenceEditor) >= %{kpim6_version}
BuildRequires:  cmake(KPim6KontactInterface) >= %{kpim6_version}
BuildRequires:  cmake(KPim6LdapWidgets) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Libkdepim) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MailTransport) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Mime) >= %{kpim6_version}
BuildRequires:  cmake(KPim6PimCommonAkonadi) >= %{kpim6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(x11)
Requires:       akonadi-calendar-tools
Requires:       kalendarac
Requires:       kdepim-addons
Requires:       kdepim-runtime
Provides:       korganizer5 = %{version}
Obsoletes:      korganizer5 < %{version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  x86_64 %{x86_64} aarch64 riscv64

%description
KOrganizer is a calendar application by KDE.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc %lang(en) %{_kf6_htmldir}/en/korganizer/
%{_kf6_applicationsdir}/korganizer*.desktop
%{_kf6_applicationsdir}/org.kde.korganizer.desktop
%{_kf6_appstreamdir}/org.kde.korganizer.appdata.xml
%{_kf6_bindir}/korganizer
%{_kf6_configkcfgdir}/korganizer.kcfg
%{_kf6_dbusinterfacesdir}/org.kde.Korganizer.Calendar.xml
%{_kf6_dbusinterfacesdir}/org.kde.korganizer.Korganizer.xml
%{_kf6_debugdir}/korganizer.categories
%{_kf6_debugdir}/korganizer.renamecategories
%{_kf6_iconsdir}/hicolor/*/apps/*.png
%{_kf6_iconsdir}/hicolor/scalable/apps/korg-journal.svgz
%{_kf6_iconsdir}/hicolor/scalable/apps/korg-todo.svg
%{_kf6_iconsdir}/hicolor/scalable/apps/korganizer.svg
%{_kf6_iconsdir}/hicolor/scalable/apps/quickview.svgz
%{_kf6_knsrcfilesdir}/korganizer.knsrc
%{_kf6_libdir}/libkorganizer_core.so.*
%{_kf6_libdir}/libkorganizer_interfaces.so.*
%{_kf6_libdir}/libkorganizerprivate.so.*
%{_kf6_plugindir}/korganizerpart.so
%dir %{_kf6_plugindir}/pim6/
%dir %{_kf6_plugindir}/pim6/kcms
%dir %{_kf6_plugindir}/pim6/kcms/korganizer
%{_kf6_plugindir}/pim6/kcms/korganizer/korganizer_configcolorsandfonts.so
%{_kf6_plugindir}/pim6/kcms/korganizer/korganizer_configfreebusy.so
%{_kf6_plugindir}/pim6/kcms/korganizer/korganizer_configgroupscheduling.so
%{_kf6_plugindir}/pim6/kcms/korganizer/korganizer_configmain.so
%{_kf6_plugindir}/pim6/kcms/korganizer/korganizer_configplugins.so
%{_kf6_plugindir}/pim6/kcms/korganizer/korganizer_configtime.so
%{_kf6_plugindir}/pim6/kcms/korganizer/korganizer_configviews.so
%{_kf6_plugindir}/pim6/kcms/korganizer/korganizer_userfeedback.so
%dir %{_kf6_plugindir}/pim6/kcms/summary
%{_kf6_plugindir}/pim6/kcms/summary/kcmapptsummary.so
%{_kf6_plugindir}/pim6/kcms/summary/kcmsdsummary.so
%{_kf6_plugindir}/pim6/kcms/summary/kcmtodosummary.so
%dir %{_kf6_plugindir}/pim6/kontact
%{_kf6_plugindir}/pim6/kontact/kontact_*.so
%dir %{_kf6_sharedir}/dbus-1/services/
%{_kf6_sharedir}/dbus-1/services/org.kde.korganizer.service
%{_kf6_sharedir}/korganizer/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/korganizer/

%changelog
