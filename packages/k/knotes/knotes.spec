#
# spec file for package knotes
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
%define kpim6_version 6.1.2

%bcond_without released
Name:           knotes
Version:        24.05.2
Release:        0
Summary:        Popup Notes
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/knotes
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DNSSD) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemViews) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6NotifyConfig) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6TextAutoCorrectionWidgets)
BuildRequires:  cmake(KF6TextCustomEditor)
BuildRequires:  cmake(KF6TextUtils)
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KPim6Akonadi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiNotes) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiSearch) >= %{kpim6_version}
BuildRequires:  cmake(KPim6CalendarUtils) >= %{kpim6_version}
BuildRequires:  cmake(KPim6GrantleeTheme) >= %{kpim6_version}
BuildRequires:  cmake(KPim6KontactInterface) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Mime) >= %{kpim6_version}
BuildRequires:  cmake(KPim6PimCommonAkonadi) >= %{kpim6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
Obsoletes:      knotes5 < %{version}
Provides:       knotes5 = %{version}

%description
KNotes is a note taking application by KDE.

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
%doc README
%doc %lang(en) %{_kf6_htmldir}/en/akonadi_notes_agent/
%doc %lang(en) %{_kf6_htmldir}/en/knotes/
%{_datadir}/akonadi/agents/notesagent.desktop
%{_kf6_applicationsdir}/org.kde.knotes.desktop
%{_kf6_appstreamdir}/org.kde.knotes.appdata.xml
%{_kf6_bindir}/akonadi_notes_agent
%{_kf6_bindir}/knotes
%{_kf6_configkcfgdir}/knotesglobalconfig.kcfg
%{_kf6_configkcfgdir}/notesagentsettings.kcfg
%{_kf6_dbusinterfacesdir}/org.kde.KNotes.xml
%{_kf6_dbusinterfacesdir}/org.kde.kontact.KNotes.xml
%{_kf6_debugdir}/knotes.categories
%{_kf6_debugdir}/knotes.renamecategories
%{_kf6_iconsdir}/hicolor/*/*/*
%{_kf6_knsrcfilesdir}/knotes_printing_theme.knsrc
%{_kf6_kxmlguidir}/knotes/
%{_kf6_notificationsdir}/akonadi_notes_agent.notifyrc

%dir %{_kf6_plugindir}/pim6/kontact
%dir %{_kf6_plugindir}/pim6
%dir %{_kf6_plugindir}/pim6/kcms
%dir %{_kf6_plugindir}/pim6/kcms/knotes
%{_kf6_plugindir}/pim6/kcms/knotes/kcm_knote_action.so
%{_kf6_plugindir}/pim6/kcms/knotes/kcm_knote_collection.so
%{_kf6_plugindir}/pim6/kcms/knotes/kcm_knote_display.so
%{_kf6_plugindir}/pim6/kcms/knotes/kcm_knote_editor.so
%{_kf6_plugindir}/pim6/kcms/knotes/kcm_knote_misc.so
%{_kf6_plugindir}/pim6/kcms/knotes/kcm_knote_network.so
%{_kf6_plugindir}/pim6/kcms/knotes/kcm_knote_print.so
%dir %{_kf6_plugindir}/pim6/kcms/summary
%{_kf6_plugindir}/pim6/kcms/summary/kcmknotessummary.so
%dir %{_kf6_plugindir}/pim6/kontact
%{_kf6_plugindir}/pim6/kontact/kontact_knotesplugin.so
%{_kf6_sharedir}/knotes/
%{_libdir}/libknotesprivate.so.*
%{_libdir}/libnotesharedprivate.so.*

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/akonadi_notes_agent/
%exclude %{_kf6_htmldir}/en/knotes/

%changelog
