#
# spec file for package kdepim-addons
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
Name:           kdepim-addons
Version:        22.12.0
Release:        0
Summary:        Addons for KDE PIM applications
License:        GPL-2.0-only
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch0:         0001-Enable-the-expert-plugin-by-default.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  libboost_headers-devel
BuildRequires:  libmarkdown-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Grantlee5)
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiCalendar)
BuildRequires:  cmake(KF5AkonadiNotes)
BuildRequires:  cmake(KF5CalendarSupport)
BuildRequires:  cmake(KF5CalendarUtils)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5EventViews)
BuildRequires:  cmake(KF5GrantleeTheme)
BuildRequires:  cmake(KF5Gravatar)
BuildRequires:  cmake(KF5Holidays)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IncidenceEditor)
BuildRequires:  cmake(KF5KontactInterface)
BuildRequires:  cmake(KF5LibKSieve)
BuildRequires:  cmake(KF5Libkdepim)
BuildRequires:  cmake(KF5Libkleo)
BuildRequires:  cmake(KF5MailCommon)
BuildRequires:  cmake(KF5MailImporter)
BuildRequires:  cmake(KF5MailTransport)
BuildRequires:  cmake(KF5MessageCore)
BuildRequires:  cmake(KF5PimCommon)
BuildRequires:  cmake(KF5Prison)
BuildRequires:  cmake(KF5Tnef)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KPimAddressbookImportExport)
BuildRequires:  cmake(KPimGAPI)
BuildRequires:  cmake(KPimImportWizard)
BuildRequires:  cmake(KPimItinerary)
BuildRequires:  cmake(KPimPkPass)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(Qt5WebEngine)
BuildRequires:  cmake(Qt5WebEngineWidgets)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5XmlPatterns)
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64

%description
Addons for KDE PIM applications, such as extensions for KMail, additional
themes, and plugins providing extra or advanced functionality.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -DKDEPIMADDONS_BUILD_EXAMPLES=FALSE -DQTCREATOR_TEMPLATE_INSTALL_DIR=%{_kf5_sharedir}/qtcreator/templates
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES/*
%dir %{_kf5_qmldir}/org/kde/plasma
%dir %{_kf5_sharedir}/qtcreator
%dir %{_kf5_sharedir}/qtcreator/templates/
%dir %{_kf5_sharedir}/qtcreator/templates/kmaileditorconvertertextplugins/
%dir %{_kf5_sharedir}/qtcreator/templates/kmaileditorplugins/
%{_kf5_bindir}/kmail_antivir.sh
%{_kf5_bindir}/kmail_clamav.sh
%{_kf5_bindir}/kmail_fprot.sh
%{_kf5_bindir}/kmail_sav.sh
%{_kf5_configdir}/kmail.antispamrc
%{_kf5_configdir}/kmail.antivirusrc
%{_kf5_debugdir}/kdepim-addons.categories
%{_kf5_debugdir}/kdepim-addons.renamecategories
%{_kf5_iconsdir}/hicolor/scalable/status/*.svg
%{_kf5_libdir}/libadblocklibprivate.so.*
%{_kf5_libdir}/libakonadidatasetools.so.5
%{_kf5_libdir}/libakonadidatasetools.so.5.*
%{_kf5_libdir}/libdkimverifyconfigure.so.*
%{_kf5_libdir}/libgrammarcommon.so.5
%{_kf5_libdir}/libgrammarcommon.so.5.*
%{_kf5_libdir}/libkaddressbookmergelibprivate.so.*
%{_kf5_libdir}/libkmailgrammalecte.so.5
%{_kf5_libdir}/libkmailgrammalecte.so.5.*
%{_kf5_libdir}/libkmaillanguagetool.so.5
%{_kf5_libdir}/libkmaillanguagetool.so.5.*
%{_kf5_libdir}/libkmailmarkdown.so.5
%{_kf5_libdir}/libkmailmarkdown.so.5.*
%{_kf5_libdir}/libkmailquicktextpluginprivate.so.5
%{_kf5_libdir}/libkmailquicktextpluginprivate.so.5.*
%{_kf5_libdir}/libshorturlpluginprivate.so.*
%{_kf5_libdir}/libfolderconfiguresettings.so.5
%{_kf5_libdir}/libfolderconfiguresettings.so.5.*
%{_kf5_libdir}/libexpireaccounttrashfolderconfig.so.5
%{_kf5_libdir}/libexpireaccounttrashfolderconfig.so.5.*
%{_kf5_libdir}/libkmailconfirmbeforedeleting.so.5
%{_kf5_libdir}/libkmailconfirmbeforedeleting.so.5.*
%{_kf5_libdir}/libscamconfiguresettings.so.5
%{_kf5_libdir}/libscamconfiguresettings.so.5.*
%{_kf5_libdir}/libopenurlwithconfigure.so.5
%{_kf5_libdir}/libopenurlwithconfigure.so.5.*
%dir %{_kf5_plugindir}/pim5/
%dir %{_kf5_plugindir}/pim5/contacteditor/
%dir %{_kf5_plugindir}/pim5/korganizer/
%dir %{_kf5_plugindir}/pim5/kmail/
%dir %{_kf5_plugindir}/pim5/mailtransport/
%dir %{_kf5_plugindir}/pim5/messageviewer/
%dir %{_kf5_plugindir}/pim5/messageviewer/grantlee
%dir %{_kf5_plugindir}/pim5/messageviewer/grantlee/5.0
%dir %{_kf5_plugindir}/pim5/pimcommon
%dir %{_kf5_plugindir}/pim5/importwizard/
%dir %{_kf5_plugindir}/pim5/kaddressbook/
%dir %{_kf5_plugindir}/pim5/libksieve/
%dir %{_kf5_plugindir}/pim5/webengineviewer/
%{_kf5_plugindir}/pim5/akonadi/
%{_kf5_plugindir}/pim5/contacteditor/editorpageplugins
%{_kf5_plugindir}/pim5/importwizard/
%{_kf5_plugindir}/pim5/kaddressbook/importexportplugin/
%{_kf5_plugindir}/pim5/kaddressbook/mainview/
%{_kf5_plugindir}/pim5/kmail/mainview/
%{_kf5_plugindir}/pim5/mailtransport/mailtransport_sendplugin.so
%{_kf5_plugindir}/pim5/messageviewer/bodypartformatter/
%{_kf5_plugindir}/pim5/messageviewer/checkbeforedeleting/
%{_kf5_plugindir}/pim5/messageviewer/configuresettings/
%{_kf5_plugindir}/pim5/messageviewer/configuresettings/
%{_kf5_plugindir}/pim5/messageviewer/headerstyle/
%{_kf5_plugindir}/pim5/messageviewer/viewercommonplugin/
%{_kf5_plugindir}/pim5/messageviewer/viewerplugin/
%{_kf5_plugindir}/pim5/templateparser/
%{_kf5_plugindir}/pim5/pimcommon/customtools/
%{_kf5_plugindir}/pim5/pimcommon/shorturlengine/
%{_kf5_plugindir}/pim5/kmail/plugincheckbeforesend/
%{_kf5_plugindir}/pim5/kmail/plugineditor/
%{_kf5_plugindir}/pim5/kmail/plugineditorconverttext/
%{_kf5_plugindir}/pim5/kmail/plugineditorgrammar/
%{_kf5_plugindir}/pim5/kmail/plugineditorinit/
%{_kf5_plugindir}/pim5/libksieve/
%{_kf5_plugindir}/pim5/webengineviewer/urlinterceptor/
%{_kf5_plugindir}/pim5/korganizer/datenums.so
%{_kf5_plugindir}/pim5/korganizer/picoftheday.so
%{_kf5_plugindir}/pim5/korganizer/thisdayinhistory.so
%{_kf5_plugindir}/pim5/korganizer/lunarphases.so
%{_kf5_plugindir}/pim5/messageviewer/grantlee/5.0/kitinerary_grantlee_extension.so
%{_kf5_plugindir}/plasmacalendarplugins/
%{_kf5_qmldir}/org/kde/plasma/PimCalendars/
%{_kf5_sharedir}/kconf_update/languagetool_kmail.upd
%{_kf5_sharedir}/kconf_update/webengineurlinterceptoradblock.upd
%{_kf5_sharedir}/qtcreator/templates/kmaileditorconvertertextplugins/CMakeLists.txt
%{_kf5_sharedir}/qtcreator/templates/kmaileditorconvertertextplugins/plugin.json.impl
%{_kf5_sharedir}/qtcreator/templates/kmaileditorconvertertextplugins/plugineditor.cpp
%{_kf5_sharedir}/qtcreator/templates/kmaileditorconvertertextplugins/plugineditor.h
%{_kf5_sharedir}/qtcreator/templates/kmaileditorconvertertextplugins/plugineditorinterface.cpp
%{_kf5_sharedir}/qtcreator/templates/kmaileditorconvertertextplugins/plugineditorinterface.h
%{_kf5_sharedir}/qtcreator/templates/kmaileditorconvertertextplugins/wizard.json
%{_kf5_sharedir}/qtcreator/templates/kmaileditorplugins/*.json
%{_kf5_sharedir}/qtcreator/templates/kmaileditorplugins/CMakeLists.txt
%{_kf5_sharedir}/qtcreator/templates/kmaileditorplugins/plugin.json.impl
%{_kf5_sharedir}/qtcreator/templates/kmaileditorplugins/plugineditor.*
%{_kf5_sharedir}/qtcreator/templates/kmaileditorplugins/plugineditorinterface.*

%files lang -f %{name}.lang

%changelog
