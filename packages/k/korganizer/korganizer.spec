#
# spec file for package korganizer
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


# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           korganizer
Version:        22.12.0
Release:        0
Summary:        Personal Organizer
License:        GPL-2.0-only
URL:            https://apps.kde.org/korganizer
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch1:         0001-Look-for-designer-qt5-on-openSUSE.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  libboost_headers-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiCalendar)
BuildRequires:  cmake(KF5AkonadiContact)
BuildRequires:  cmake(KF5AkonadiMime)
BuildRequires:  cmake(KF5AkonadiNotes)
BuildRequires:  cmake(KF5AkonadiSearch)
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5CalendarSupport)
BuildRequires:  cmake(KF5CalendarUtils)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5EventViews)
BuildRequires:  cmake(KF5Holidays)
BuildRequires:  cmake(KF5IdentityManagement)
BuildRequires:  cmake(KF5IncidenceEditor)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KontactInterface)
BuildRequires:  cmake(KF5Ldap)
BuildRequires:  cmake(KF5Libkdepim)
BuildRequires:  cmake(KF5MailTransport)
BuildRequires:  cmake(KF5Mime)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5PimCommon)
BuildRequires:  cmake(KF5PimTextEdit)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
Requires:       akonadi-calendar-tools
Requires:       kalendarac
Requires:       kdepim-addons
Requires:       kdepim-runtime
Provides:       korganizer5 = %{version}
Obsoletes:      korganizer5 < %{version}

%description
KOrganizer is a calendar application by KDE.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

rm %{buildroot}%{_kf5_libdir}/*.so
%suse_update_desktop_file org.kde.korganizer Office Calendar

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES/*
%doc %lang(en) %{_kf5_htmldir}/en/korganizer/
%{_kf5_applicationsdir}/korganizer*.desktop
%{_kf5_applicationsdir}/org.kde.korganizer.desktop
%{_kf5_appstreamdir}/org.kde.korganizer.appdata.xml
%{_kf5_bindir}/korganizer
%{_kf5_configkcfgdir}/korganizer.kcfg
%{_kf5_dbusinterfacesdir}/org.kde.Korganizer.*.xml
%{_kf5_dbusinterfacesdir}/org.kde.korganizer.*.xml
%{_kf5_debugdir}/korganizer.categories
%{_kf5_debugdir}/korganizer.renamecategories
%dir %{_kf5_iconsdir}/hicolor/256x256
%dir %{_kf5_iconsdir}/hicolor/256x256/apps
%{_kf5_iconsdir}/hicolor/*/apps/*.png
%{_kf5_iconsdir}/hicolor/scalable/apps/korg-journal.svgz
%{_kf5_iconsdir}/hicolor/scalable/apps/korg-todo.svg
%{_kf5_iconsdir}/hicolor/scalable/apps/korganizer.svg
%{_kf5_iconsdir}/hicolor/scalable/apps/quickview.svgz
%{_kf5_knsrcfilesdir}/korganizer.knsrc
%{_kf5_libdir}/libkorganizer_core.so.*
%{_kf5_libdir}/libkorganizer_interfaces.so.*
%{_kf5_libdir}/libkorganizerprivate.so.*
%dir %{_kf5_plugindir}/pim5/
%dir %{_kf5_plugindir}/pim5/kcms
%dir %{_kf5_plugindir}/pim5/kcms/korganizer
%dir %{_kf5_plugindir}/pim5/kontact
%{_kf5_plugindir}/pim5/kcms/korganizer/korganizer_configcolorsandfonts.so
%{_kf5_plugindir}/pim5/kcms/korganizer/korganizer_configdesignerfields.so
%{_kf5_plugindir}/pim5/kcms/korganizer/korganizer_configfreebusy.so
%{_kf5_plugindir}/pim5/kcms/korganizer/korganizer_configgroupscheduling.so
%{_kf5_plugindir}/pim5/kcms/korganizer/korganizer_configmain.so
%{_kf5_plugindir}/pim5/kcms/korganizer/korganizer_configplugins.so
%{_kf5_plugindir}/pim5/kcms/korganizer/korganizer_configtime.so
%{_kf5_plugindir}/pim5/kcms/korganizer/korganizer_configviews.so
%{_kf5_plugindir}/pim5/kcms/korganizer/korganizer_userfeedback.so
%dir %{_kf5_plugindir}/pim5/kcms/summary
%{_kf5_plugindir}/pim5/kcms/summary/kcmapptsummary.so
%{_kf5_plugindir}/pim5/kcms/summary/kcmsdsummary.so
%{_kf5_plugindir}/pim5/kcms/summary/kcmtodosummary.so
%{_kf5_plugindir}/pim5/kontact/kontact_*.so
%{_kf5_plugindir}/korganizerpart.so
%dir %{_kf5_sharedir}/dbus-1/services/
%{_kf5_sharedir}/dbus-1/services/org.kde.korganizer.service
%{_kf5_sharedir}/korganizer/

%files lang -f %{name}.lang

%changelog
