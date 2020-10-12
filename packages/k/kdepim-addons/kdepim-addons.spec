#
# spec file for package kdepim-addons
#
# Copyright (c) 2020 SUSE LLC
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


%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kdepim-addons
Version:        20.08.2
Release:        0
Summary:        Addons for KDEPIM applications
License:        GPL-2.0-only
Group:          Productivity/Graphics/Other
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE
Patch0:         0001-Enable-the-expert-plugin-by-default.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kdepim-apps-libs-devel
BuildRequires:  kf5-filesystem
BuildRequires:  libmarkdown-devel
BuildRequires:  update-desktop-files
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
BuildRequires:  cmake(KPimGAPI)
BuildRequires:  cmake(KPimImportWizard)
BuildRequires:  cmake(KPimItinerary)
BuildRequires:  cmake(KPimPkPass)
BuildRequires:  cmake(Qt5Concurrent) >= 5.6.0
BuildRequires:  cmake(Qt5DBus) >= 5.6.0
BuildRequires:  cmake(Qt5OpenGL) >= 5.6.0
BuildRequires:  cmake(Qt5Test) >= 5.6.0
BuildRequires:  cmake(Qt5UiTools) >= 5.6.0
BuildRequires:  cmake(Qt5WebEngine) >= 5.6.0
BuildRequires:  cmake(Qt5WebEngineWidgets) >= 5.6.0
BuildRequires:  cmake(Qt5Widgets) >= 5.6.0
BuildRequires:  cmake(Qt5X11Extras) >= 5.6.0
BuildRequires:  cmake(Qt5XmlPatterns) >= 5.6.0
Requires(post): shared-mime-info
Requires(postun): shared-mime-info
Recommends:     %{name}-lang
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  libboost_headers-devel

%description
Addons for KDE PIM applications, such as extensions for KMail, additional
themes, and plugins providing extra or advanced functionality.

%lang_package

%prep
%setup -q
%autopatch -p1

%build
%cmake_kf5 -d build -- -DKDEPIMADDONS_BUILD_EXAMPLES=FALSE -DQTCREATOR_TEMPLATE_INSTALL_DIR=%{_kf5_sharedir}/qtcreator/templates
%cmake_build

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING*
%{_kf5_debugdir}/kdepim-addons.categories
%{_kf5_debugdir}/kdepim-addons.renamecategories
%{_kf5_configdir}/kmail.antispamrc
%{_kf5_configdir}/kmail.antivirusrc
%dir %{_kf5_plugindir}
%dir %{_kf5_plugindir}/akonadi
%dir %{_kf5_libdir}/contacteditor
%dir %{_kf5_libdir}/contacteditor/editorpageplugins
%dir %{_kf5_plugindir}/messageviewer
%dir %{_kf5_plugindir}/messageviewer/bodypartformatter
%dir %{_kf5_plugindir}/messageviewer/configuresettings
%dir %{_kf5_plugindir}/messageviewer/headerstyle
%dir %{_kf5_plugindir}/messageviewer/viewercommonplugin
%dir %{_kf5_plugindir}/messageviewer/viewerplugin
%dir %{_kf5_plugindir}/messageviewer/grantlee
%dir %{_kf5_plugindir}/messageviewer/grantlee/5.0
%dir %{_kf5_qmldir}/org/kde/plasma
%{_kf5_bindir}/kmail_antivir.sh
%{_kf5_bindir}/kmail_clamav.sh
%{_kf5_bindir}/kmail_fprot.sh
%{_kf5_bindir}/kmail_sav.sh
%{_kf5_libdir}/contacteditor/editorpageplugins/cryptopageplugin.so
%{_kf5_libdir}/libadblocklibprivate.so.*
%{_kf5_libdir}/libdkimverifyconfigure.so.*
%{_kf5_libdir}/libkaddressbookimportexportlibprivate.so.*
%{_kf5_libdir}/libkaddressbookmergelibprivate.so.*
%{_kf5_libdir}/libshorturlpluginprivate.so.*
%{_kf5_libdir}/libkmailgrammalecte.so.5.*
%{_kf5_libdir}/libkmailgrammalecte.so.5
%{_kf5_libdir}/libgrammarcommon.so.5
%{_kf5_libdir}/libgrammarcommon.so.5.*
%{_kf5_libdir}/libkmaillanguagetool.so.5
%{_kf5_libdir}/libkmaillanguagetool.so.5.*
%{_kf5_libdir}/libkmailquicktextpluginprivate.so.5
%{_kf5_libdir}/libkmailquicktextpluginprivate.so.5.*
%{_kf5_libdir}/libkmailmarkdown.so.5
%{_kf5_libdir}/libkmailmarkdown.so.5.*
%{_kf5_plugindir}/akonadi/emailaddressselectionldapdialogplugin.so
%{_kf5_plugindir}/importwizard/
%{_kf5_plugindir}/kaddressbook/
%{_kf5_plugindir}/kmail/
%{_kf5_plugindir}/korg_datenums.so
%{_kf5_plugindir}/korg_picoftheday.so
%{_kf5_plugindir}/korg_thisdayinhistory.so
%{_kf5_plugindir}/libksieve/
%{_kf5_plugindir}/mailtransport/
%{_kf5_plugindir}/pimcommon/
%{_kf5_plugindir}/plasmacalendarplugins/
%{_kf5_plugindir}/templateparser/
%{_kf5_plugindir}/webengineviewer/
%{_kf5_plugindir}/messageviewer/bodypartformatter/messageviewer_bodypartformatter*.so
%{_kf5_plugindir}/messageviewer/grantlee/5.0/kitinerary_grantlee_extension.so
%{_kf5_plugindir}/messageviewer/configuresettings/messageviewer_dkimconfigplugin.so
%{_kf5_plugindir}/messageviewer/configuresettings/messageviewer_gravatarconfigplugin.so
%{_kf5_plugindir}/messageviewer/headerstyle/messageviewer_briefheaderstyleplugin.so
%{_kf5_plugindir}/messageviewer/headerstyle/messageviewer_fancyheaderstyleplugin.so
%{_kf5_plugindir}/messageviewer/headerstyle/messageviewer_grantleeheaderstyleplugin.so
%{_kf5_plugindir}/messageviewer/headerstyle/messageviewer_longheaderstyleplugin.so
%{_kf5_plugindir}/messageviewer/headerstyle/messageviewer_standardsheaderstyleplugin.so
%{_kf5_plugindir}/messageviewer/viewercommonplugin/messageviewer_expandurlplugin.so
%{_kf5_plugindir}/messageviewer/viewercommonplugin/messageviewer_translatorplugin.so
%{_kf5_plugindir}/messageviewer/viewerplugin/messageviewer_createeventplugin.so
%{_kf5_plugindir}/messageviewer/viewerplugin/messageviewer_createnoteplugin.so
%{_kf5_plugindir}/messageviewer/viewerplugin/messageviewer_createtodoplugin.so
%{_kf5_plugindir}/messageviewer/viewerplugin/messageviewer_externalscriptplugin.so
%{_kf5_qmldir}/org/kde/plasma/PimCalendars/
%{_kf5_servicesdir}/korganizer/
%{_kf5_sharedir}/kconf_update/webengineurlinterceptoradblock.upd
%{_kf5_sharedir}/kconf_update/languagetool_kmail.upd
%dir %{_kf5_sharedir}/qtcreator
%dir %{_kf5_sharedir}/qtcreator/templates/
%dir %{_kf5_sharedir}/qtcreator/templates/kmaileditorplugins/
%dir %{_kf5_sharedir}/qtcreator/templates/kmaileditorconvertertextplugins/
%{_kf5_sharedir}/qtcreator/templates/kmaileditorplugins/CMakeLists.txt
%{_kf5_sharedir}/qtcreator/templates/kmaileditorplugins/plugineditor.*
%{_kf5_sharedir}/qtcreator/templates/kmaileditorplugins/plugineditorinterface.*
%{_kf5_sharedir}/qtcreator/templates/kmaileditorplugins/*.json
%{_kf5_sharedir}/qtcreator/templates/kmaileditorplugins/plugin.json.impl
%{_kf5_sharedir}/qtcreator/templates/kmaileditorconvertertextplugins/CMakeLists.txt
%{_kf5_sharedir}/qtcreator/templates/kmaileditorconvertertextplugins/plugin.json.impl
%{_kf5_sharedir}/qtcreator/templates/kmaileditorconvertertextplugins/plugineditor.cpp
%{_kf5_sharedir}/qtcreator/templates/kmaileditorconvertertextplugins/plugineditor.h
%{_kf5_sharedir}/qtcreator/templates/kmaileditorconvertertextplugins/plugineditorinterface.cpp
%{_kf5_sharedir}/qtcreator/templates/kmaileditorconvertertextplugins/plugineditorinterface.h
%{_kf5_sharedir}/qtcreator/templates/kmaileditorconvertertextplugins/wizard.json

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
