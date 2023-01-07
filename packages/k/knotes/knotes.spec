#
# spec file for package knotes
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
Name:           knotes
Version:        22.12.1
Release:        0
Summary:        Popup Notes
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/knotes
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  libxslt-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Grantlee5)
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiNotes)
BuildRequires:  cmake(KF5AkonadiSearch)
BuildRequires:  cmake(KF5CalendarUtils)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DNSSD)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5GrantleeTheme)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KontactInterface)
BuildRequires:  cmake(KF5Libkdepim)
BuildRequires:  cmake(KF5Mime)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5PimCommon)
BuildRequires:  cmake(KF5PimTextEdit)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5Xml)
Obsoletes:      knotes5 < %{version}
Provides:       knotes5 = %{version}

%description
KNotes is a note taking application by KDE.

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

%suse_update_desktop_file org.kde.knotes Utility DesktopUtility

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES/*
%doc README
%doc %lang(en) %{_kf5_htmldir}/en/akonadi_notes_agent/
%doc %lang(en) %{_kf5_htmldir}/en/knotes/
%{_datadir}/akonadi/agents/notesagent.desktop
%{_kf5_applicationsdir}/org.kde.knotes.desktop
%{_kf5_appstreamdir}/org.kde.knotes.appdata.xml
%{_kf5_bindir}/akonadi_notes_agent
%{_kf5_bindir}/knotes
%{_kf5_configkcfgdir}/knotesglobalconfig.kcfg
%{_kf5_configkcfgdir}/notesagentsettings.kcfg
%{_kf5_dbusinterfacesdir}/org.kde.KNotes.xml
%{_kf5_dbusinterfacesdir}/org.kde.kontact.*.xml
%{_kf5_debugdir}/knotes.categories
%{_kf5_debugdir}/knotes.renamecategories
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_knsrcfilesdir}/knotes_printing_theme.knsrc
%{_kf5_kxmlguidir}/knotes/
%{_kf5_notifydir}/akonadi_notes_agent.notifyrc
%dir %{_kf5_plugindir}/pim5
%dir %{_kf5_plugindir}/pim5/kcms
%dir %{_kf5_plugindir}/pim5/kcms/knotes
%dir %{_kf5_plugindir}/pim5/kcms/summary
%dir %{_kf5_plugindir}/pim5/kontact
%{_kf5_plugindir}/pim5/kcms/knotes/kcm_knote_action.so
%{_kf5_plugindir}/pim5/kcms/knotes/kcm_knote_collection.so
%{_kf5_plugindir}/pim5/kcms/knotes/kcm_knote_display.so
%{_kf5_plugindir}/pim5/kcms/knotes/kcm_knote_editor.so
%{_kf5_plugindir}/pim5/kcms/knotes/kcm_knote_misc.so
%{_kf5_plugindir}/pim5/kcms/knotes/kcm_knote_network.so
%{_kf5_plugindir}/pim5/kcms/knotes/kcm_knote_print.so
%{_kf5_plugindir}/pim5/kcms/summary/kcmknotessummary.so
%{_kf5_plugindir}/pim5/kontact/kontact_knotesplugin.so
%{_kf5_sharedir}/knotes/
%{_libdir}/libknotesprivate.so.*
%{_libdir}/libnotesharedprivate.so.*

%files lang -f %{name}.lang

%changelog
