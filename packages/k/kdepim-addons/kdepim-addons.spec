#
# spec file for package kdepim-addons
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
Name:           kdepim-addons
Version:        24.05.1
Release:        0
Summary:        Addons for KDE PIM applications
License:        GPL-2.0-only
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Source3:        vendor.tar.zst
# PATCH-FIX-OPENSUSE
Patch0:         0001-Enable-the-expert-plugin-by-default.patch
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libgpgmepp-devel
BuildRequires:  libmarkdown-devel
BuildRequires:  zstd
BuildRequires:  cmake(Corrosion)
BuildRequires:  cmake(KF6CalendarCore) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6Contacts) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Declarative) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Holidays) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6Prison) >= %{kf6_version}
BuildRequires:  cmake(KF6SyntaxHighlighting) >= %{kf6_version}
BuildRequires:  cmake(KF6TextAddonsWidgets)
BuildRequires:  cmake(KF6TextCustomEditor)
BuildRequires:  cmake(KF6TextGrammarCheck)
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(KF6TextTranslator)
BuildRequires:  cmake(KF6TextUtils)
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KPim6AddressbookImportExport) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Akonadi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiCalendar) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiContactWidgets) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiNotes) >= %{kpim6_version}
BuildRequires:  cmake(KPim6CalendarSupport) >= %{kpim6_version}
BuildRequires:  cmake(KPim6CalendarUtils) >= %{kpim6_version}
BuildRequires:  cmake(KPim6EventViews) >= %{kpim6_version}
BuildRequires:  cmake(KPim6GrantleeTheme) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Gravatar) >= %{kpim6_version}
BuildRequires:  cmake(KPim6IMAP) >= %{kpim6_version}
BuildRequires:  cmake(KPim6IdentityManagementCore) >= %{kpim6_version}
BuildRequires:  cmake(KPim6ImportWizard) >= %{kpim6_version}
BuildRequires:  cmake(KPim6IncidenceEditor) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Itinerary) >= %{kpim6_version}
BuildRequires:  cmake(KPim6KSieveUi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Libkdepim) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Libkleo) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MailCommon) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MailImporterAkonadi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MailTransport) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MessageComposer) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MessageCore) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MessageList) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MessageViewer) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Mime) >= %{kpim6_version}
BuildRequires:  cmake(KPim6PimCommonAkonadi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6PkPass) >= %{kpim6_version}
BuildRequires:  cmake(KPim6TemplateParser) >= %{kpim6_version}
BuildRequires:  cmake(KPim6TextEdit) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Tnef) >= %{kpim6_version}
BuildRequires:  cmake(KPim6WebEngineViewer) >= %{kpim6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  x86_64 %{x86_64} aarch64 riscv64

%description
Addons for KDE PIM applications, such as extensions for KMail, additional
themes, and plugins providing extra or advanced functionality.

%lang_package

%prep
%autosetup -p1 -a3

%build
%cmake_kf6 \
  -DKDEPIM_RUN_AKONADI_TEST:BOOL=FALSE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets

%files
%license LICENSES/*
%{_kf6_bindir}/kmail_antivir.sh
%{_kf6_bindir}/kmail_clamav.sh
%{_kf6_bindir}/kmail_fprot.sh
%{_kf6_bindir}/kmail_sav.sh
%{_kf6_configdir}/kmail.antispamrc
%{_kf6_configdir}/kmail.antivirusrc
%{_kf6_debugdir}/kdepim-addons.categories
%{_kf6_debugdir}/kdepim-addons.renamecategories
%{_kf6_iconsdir}/hicolor/scalable/status/*.svg
%{_kf6_libdir}/libadblockplugin.so.*
%{_kf6_libdir}/libakonadidatasetools.so.*
%{_kf6_libdir}/libdkimverifyconfigure.so.*
%{_kf6_libdir}/libexpireaccounttrashfolderconfig.so.*
%{_kf6_libdir}/libfolderconfiguresettings.so.*
%{_kf6_libdir}/libkaddressbookmergelibprivate.so.*
%{_kf6_libdir}/libkmailconfirmbeforedeleting.so.*
%{_kf6_libdir}/libkmailmarkdown.so.*
%{_kf6_libdir}/libkmailquicktextpluginprivate.so.*
%{_kf6_libdir}/libopenurlwithconfigure.so.*
%{_kf6_libdir}/libshorturlpluginprivate.so.*
%dir %{_kf6_plugindir}/pim6
%{_kf6_plugindir}/pim6/akonadi/
%{_kf6_plugindir}/pim6/contacteditor/
%{_kf6_plugindir}/pim6/importwizard/
%{_kf6_plugindir}/pim6/kaddressbook/
%{_kf6_plugindir}/pim6/kmail/
%{_kf6_plugindir}/pim6/korganizer/
%{_kf6_plugindir}/pim6/libksieve/
%{_kf6_plugindir}/pim6/mailtransport/
%{_kf6_plugindir}/pim6/messageviewer/
%{_kf6_plugindir}/pim6/pimcommon
%{_kf6_plugindir}/pim6/templateparser/
%{_kf6_plugindir}/pim6/webengineviewer/
%{_kf6_plugindir}/plasmacalendarplugins/
%dir %{_kf6_qmldir}/org/kde/plasma
%{_kf6_qmldir}/org/kde/plasma/PimCalendars/

%files lang -f %{name}.lang

%changelog
