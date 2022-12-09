#
# spec file for package kmail
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


%define kf5_version 5.99.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kmail
Version:        22.12.0
Release:        0
Summary:        Mail Client
License:        GPL-2.0-only
URL:            https://apps.kde.org/kmail2
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  gettext-devel
BuildRequires:  libgpgmepp-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiContact)
BuildRequires:  cmake(KF5AkonadiMime)
BuildRequires:  cmake(KF5AkonadiSearch)
BuildRequires:  cmake(KF5Bookmarks)
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5CalendarUtils)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GrantleeTheme)
BuildRequires:  cmake(KF5Gravatar)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IdentityManagement)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5KontactInterface)
BuildRequires:  cmake(KF5Ldap)
BuildRequires:  cmake(KF5LibKSieve)
BuildRequires:  cmake(KF5Libkdepim)
BuildRequires:  cmake(KF5Libkleo)
BuildRequires:  cmake(KF5MailCommon)
BuildRequires:  cmake(KF5MailTransport)
BuildRequires:  cmake(KF5MessageComposer)
BuildRequires:  cmake(KF5MessageCore)
BuildRequires:  cmake(KF5MessageList)
BuildRequires:  cmake(KF5MessageViewer)
BuildRequires:  cmake(KF5Mime)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5PimCommon)
BuildRequires:  cmake(KF5PimTextEdit)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5Sonnet)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(KF5TemplateParser)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5Tnef)
BuildRequires:  cmake(KF5WebEngineViewer)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(QGpgme)
BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5WebEngine)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
Requires:       %{name}-application-icons
Requires:       kdepim-addons
Requires:       kdepim-runtime
Requires:       kmail-account-wizard
Recommends:     akonadi-import-wizard
Recommends:     akonadi-search
Recommends:     kleopatra
Recommends:     ktnef
Recommends:     mbox-importer
Recommends:     pim-data-exporter
Recommends:     pim-sieve-editor
Provides:       kmail5 = %{version}
Obsoletes:      kmail5 < %{version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64
%if %{with released}
%requires_eq    libKF5PimCommon5
%requires_eq    libKF5PimCommonAkonadi5
%requires_eq    messagelib
%endif

%description
KMail is the KDE mail client.

%package application-icons
Summary:        mail client icon

%description application-icons
The KMail application icon that is shared with a number of applications

%package -n ktnef
Summary:        Viewer for email attachments in TNEF format
Requires:       kdepim-runtime
Obsoletes:      ktnef5 < %{version}
Provides:       ktnef5 = %{version}

%description -n ktnef
KTNEF is a viewer for email attachments in the TNEF format.

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

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n ktnef
%doc %lang(en) %{_kf5_htmldir}/en/ktnef/
%{_kf5_applicationsdir}/org.kde.ktnef.desktop
%{_kf5_bindir}/ktnef
%{_kf5_iconsdir}/*/*/*/ktnef*.png

%files
%license LICENSES/*
%{_kf5_debugdir}/kmail.categories
%{_kf5_debugdir}/kmail.renamecategories
%doc %lang(en) %{_kf5_htmldir}/en/akonadi_archivemail_agent/
%doc %lang(en) %{_kf5_htmldir}/en/akonadi_followupreminder_agent/
%doc %lang(en) %{_kf5_htmldir}/en/akonadi_sendlater_agent/
%doc %lang(en) %{_kf5_htmldir}/en/kmail2/
%{_kf5_applicationsdir}/kmail_view.desktop
%{_kf5_applicationsdir}/org.kde.kmail2.desktop
%{_kf5_applicationsdir}/org.kde.kmail-refresh-settings.desktop
%{_kf5_appstreamdir}/org.kde.kmail2.appdata.xml
%{_kf5_bindir}/akonadi_archivemail_agent
%{_kf5_bindir}/akonadi_followupreminder_agent
%{_kf5_bindir}/akonadi_mailfilter_agent
%{_kf5_bindir}/akonadi_mailmerge_agent
%{_kf5_bindir}/akonadi_sendlater_agent
%{_kf5_bindir}/akonadi_unifiedmailbox_agent
%{_kf5_bindir}/kmail*
%{_kf5_configkcfgdir}/archivemailagentsettings.kcfg
%{_kf5_configkcfgdir}/kmail.kcfg
%{_kf5_dbusinterfacesdir}/org.kde.kmail.*.xml
%{_kf5_kxmlguidir}/kontactsummary/
%{_kf5_libdir}/libkmailprivate.so.*
%{_kf5_notifydir}/akonadi_*_agent.notifyrc
%{_kf5_notifydir}/kmail2.notifyrc
%dir %{_kf5_plugindir}/pim5
%dir %{_kf5_plugindir}/pim5/akonadi/
%dir %{_kf5_plugindir}/pim5/kcms/
%dir %{_kf5_plugindir}/pim5/kontact/
%dir %{_kf5_plugindir}/pim5/kcms/kmail
%dir %{_kf5_plugindir}/pim5/kcms/summary
%{_kf5_plugindir}/pim5/kcms/kmail/kcm_kmail_accounts.so
%{_kf5_plugindir}/pim5/kcms/kmail/kcm_kmail_appearance.so
%{_kf5_plugindir}/pim5/kcms/kmail/kcm_kmail_composer.so
%{_kf5_plugindir}/pim5/kcms/kmail/kcm_kmail_misc.so
%{_kf5_plugindir}/pim5/kcms/kmail/kcm_kmail_plugins.so
%{_kf5_plugindir}/pim5/kcms/kmail/kcm_kmail_security.so
%{_kf5_plugindir}/pim5/kcms/summary/kcmkmailsummary.so
%{_kf5_plugindir}/pim5/kcms/summary/kcmkontactsummary.so
%{_kf5_plugindir}/kmailpart.so
%{_kf5_plugindir}/pim5/kontact/kontact_kmailplugin.so
%{_kf5_plugindir}/pim5/kontact/kontact_summaryplugin.so
%{_kf5_plugindir}/pim5/akonadi/config/
%{_kf5_sharedir}/akonadi/agents/
%dir %{_kf5_sharedir}/dbus-1/services/
%{_kf5_sharedir}/dbus-1/services/org.kde.kmail.service
%{_kf5_sharedir}/kmail2/

%files application-icons
%dir %{_kf5_iconsdir}/hicolor/16x16/emblems
%dir %{_kf5_iconsdir}/hicolor/22x22/emblems
%dir %{_kf5_iconsdir}/hicolor/8x8
%dir %{_kf5_iconsdir}/hicolor/8x8/emblems
%dir %{_kf5_iconsdir}/breeze-dark/
%dir %{_kf5_iconsdir}/breeze-dark/16x16
%dir %{_kf5_iconsdir}/breeze-dark/16x16/emblems
%dir %{_kf5_iconsdir}/breeze-dark/22x22
%dir %{_kf5_iconsdir}/breeze-dark/8x8
%dir %{_kf5_iconsdir}/breeze-dark/8x8/emblems
%dir %{_kf5_iconsdir}/breeze-dark/22x22/emblems
%{_kf5_iconsdir}/hicolor/*/apps/kmail.png
%{_kf5_iconsdir}/hicolor/*/emblems/gpg-key-trust-level*.svg
%{_kf5_iconsdir}/hicolor/scalable/apps/kmail.svg
%{_kf5_iconsdir}/breeze-dark/*/emblems/gpg-key-trust-level-*.svg

%files lang -f %{name}.lang

%changelog
