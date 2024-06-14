#
# spec file for package kmail
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
Name:           kmail
Version:        24.05.1
Release:        0
Summary:        Mail Client
License:        GPL-2.0-only
URL:            https://apps.kde.org/kmail2
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libgpgmepp-devel
BuildRequires:  cmake(KF6Bookmarks) >= %{kf6_version}
BuildRequires:  cmake(KF6CalendarCore) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6Contacts) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemViews) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6NotifyConfig) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6Sonnet) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6TextAutoCorrectionWidgets)
BuildRequires:  cmake(KF6TextCustomEditor)
BuildRequires:  cmake(KF6TextEditTextToSpeech)
BuildRequires:  cmake(KF6TextEditTextToSpeech)
BuildRequires:  cmake(KF6TextUtils)
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6UserFeedback) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KPim6Akonadi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiContactWidgets) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiMime) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiSearch) >= %{kpim6_version}
BuildRequires:  cmake(KPim6CalendarUtils) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Gravatar) >= %{kpim6_version}
BuildRequires:  cmake(KPim6IdentityManagementCore) >= %{kpim6_version}
BuildRequires:  cmake(KPim6KSieveUi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6KontactInterface) >= %{kpim6_version}
BuildRequires:  cmake(KPim6LdapWidgets) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Libkdepim) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Libkleo) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MailCommon) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MailTransport) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MailTransportDBusService) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MessageComposer) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MessageCore) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MessageList) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MessageViewer) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Mime) >= %{kpim6_version}
BuildRequires:  cmake(KPim6PimCommonAkonadi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6TemplateParser) >= %{kpim6_version}
BuildRequires:  cmake(KPim6TextEdit) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Tnef) >= %{kpim6_version}
BuildRequires:  cmake(KPim6WebEngineViewer) >= %{kpim6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Keychain) >= 0.14.2
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       kmail-application-icons
Requires:       kdepim-addons
Requires:       kdepim-runtime
Requires:       kmail-account-wizard
Requires:       ktextaddons
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
ExclusiveArch:  x86_64 %{x86_64} aarch64 riscv64

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
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%ldconfig_scriptlets

%files -n ktnef
%doc %lang(en) %{_kf6_htmldir}/en/ktnef/
%{_kf6_applicationsdir}/org.kde.ktnef.desktop
%{_kf6_bindir}/ktnef
%{_kf6_iconsdir}/*/*/*/ktnef*.png

%files
%license LICENSES/*
%{_kf6_debugdir}/kmail.categories
%{_kf6_debugdir}/kmail.renamecategories
%doc %lang(en) %{_kf6_htmldir}/en/akonadi_archivemail_agent/
%doc %lang(en) %{_kf6_htmldir}/en/akonadi_followupreminder_agent/
%doc %lang(en) %{_kf6_htmldir}/en/akonadi_sendlater_agent/
%doc %lang(en) %{_kf6_htmldir}/en/kmail2/
%{_kf6_applicationsdir}/kmail_view.desktop
%{_kf6_applicationsdir}/org.kde.kmail2.desktop
%{_kf6_applicationsdir}/org.kde.kmail-refresh-settings.desktop
%{_kf6_appstreamdir}/org.kde.kmail2.appdata.xml
%{_kf6_bindir}/akonadi_archivemail_agent
%{_kf6_bindir}/akonadi_followupreminder_agent
%{_kf6_bindir}/akonadi_mailfilter_agent
%{_kf6_bindir}/akonadi_mailmerge_agent
%{_kf6_bindir}/akonadi_sendlater_agent
%{_kf6_bindir}/akonadi_unifiedmailbox_agent
%{_kf6_bindir}/kmail
%{_kf6_bindir}/kmail-refresh-settings
%{_kf6_configkcfgdir}/archivemailagentsettings.kcfg
%{_kf6_configkcfgdir}/kmail.kcfg
%{_kf6_dbusinterfacesdir}/org.kde.kmail.kmail.xml
%{_kf6_dbusinterfacesdir}/org.kde.kmail.kmailpart.xml
%{_kf6_libdir}/libkmailprivate.so.*
%{_kf6_libdir}/libmailfilteragentprivate.so.*
%{_kf6_notificationsdir}/akonadi_*_agent.notifyrc
%{_kf6_notificationsdir}/kmail2.notifyrc
%dir %{_kf6_plugindir}/pim6
%dir %{_kf6_plugindir}/pim6/akonadi/
%{_kf6_plugindir}/pim6/akonadi/config/
%dir %{_kf6_plugindir}/pim6/kcms/
%dir %{_kf6_plugindir}/pim6/kcms/kmail
%{_kf6_plugindir}/pim6/kcms/kmail/kcm_kmail_accounts.so
%{_kf6_plugindir}/pim6/kcms/kmail/kcm_kmail_appearance.so
%{_kf6_plugindir}/pim6/kcms/kmail/kcm_kmail_composer.so
%{_kf6_plugindir}/pim6/kcms/kmail/kcm_kmail_misc.so
%{_kf6_plugindir}/pim6/kcms/kmail/kcm_kmail_plugins.so
%{_kf6_plugindir}/pim6/kcms/kmail/kcm_kmail_security.so
%dir %{_kf6_plugindir}/pim6/kcms/summary
%{_kf6_plugindir}/pim6/kcms/summary/kcmkmailsummary.so
%{_kf6_plugindir}/pim6/kcms/summary/kcmkontactsummary.so
%dir %{_kf6_plugindir}/pim6/kontact/
%{_kf6_plugindir}/pim6/kontact/kontact_kmailplugin.so
%{_kf6_plugindir}/pim6/kontact/kontact_summaryplugin.so
%{_kf6_plugindir}/kmailpart.so
%{_kf6_sharedir}/akonadi/agents/*.desktop
%{_kf6_sharedir}/dbus-1/services/org.kde.kmail.service
%{_kf6_sharedir}/kmail2/

%files application-icons
%dir %{_kf6_iconsdir}/breeze-dark/
%dir %{_kf6_iconsdir}/breeze-dark/16x16
%dir %{_kf6_iconsdir}/breeze-dark/16x16/emblems
%dir %{_kf6_iconsdir}/breeze-dark/22x22
%dir %{_kf6_iconsdir}/breeze-dark/8x8
%dir %{_kf6_iconsdir}/breeze-dark/8x8/emblems
%dir %{_kf6_iconsdir}/breeze-dark/22x22/emblems
%{_kf6_iconsdir}/breeze-dark/*/emblems/gpg-key-trust-level-*.svg
%dir %{_kf6_iconsdir}/hicolor/8x8
%dir %{_kf6_iconsdir}/hicolor/8x8/emblems
%{_kf6_iconsdir}/hicolor/*/apps/kmail.png
%{_kf6_iconsdir}/hicolor/*/emblems/gpg-key-trust-level*.svg
%{_kf6_iconsdir}/hicolor/scalable/apps/kmail.svg

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/akonadi_archivemail_agent/
%exclude %{_kf6_htmldir}/en/akonadi_followupreminder_agent/
%exclude %{_kf6_htmldir}/en/akonadi_sendlater_agent/
%exclude %{_kf6_htmldir}/en/kmail2/
%exclude %{_kf6_htmldir}/en/ktnef/

%changelog
