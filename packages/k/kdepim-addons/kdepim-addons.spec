#
# spec file for package kdepim-addons
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kdepim-addons
Version:        19.08.1
Release:        0
Summary:        Addons for KDEPIM applications
License:        GPL-2.0-only
Group:          Productivity/Graphics/Other
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch0:         0001-Enable-the-expert-plugin-by-default.patch
BuildRequires:  akonadi-calendar-devel
BuildRequires:  akonadi-import-wizard-devel
BuildRequires:  akonadi-notes-devel
BuildRequires:  akonadi-server-devel
BuildRequires:  calendarsupport-devel
BuildRequires:  eventviews-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  grantleetheme-devel
BuildRequires:  incidenceeditor-devel
BuildRequires:  kcalutils-devel
BuildRequires:  kconfig-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdeclarative-devel
BuildRequires:  kdepim-apps-libs-devel
BuildRequires:  kf5-filesystem
BuildRequires:  kholidays-devel
BuildRequires:  ki18n-devel
BuildRequires:  kitinerary-devel
BuildRequires:  kmailtransport-devel
BuildRequires:  kontactinterface-devel
BuildRequires:  kpkpass-devel
BuildRequires:  ktnef-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libgravatar-devel
BuildRequires:  libkdepim-devel
BuildRequires:  libkgapi-devel
BuildRequires:  libkleo-devel
BuildRequires:  mailcommon-devel
BuildRequires:  mailimporter-devel
BuildRequires:  messagelib-devel
BuildRequires:  pimcommon-devel
BuildRequires:  pkgconfig
BuildRequires:  prison-qt5-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5LibKSieve)
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.6.0
BuildRequires:  pkgconfig(Qt5DBus) >= 5.6.0
BuildRequires:  pkgconfig(Qt5OpenGL) >= 5.6.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.6.0
BuildRequires:  pkgconfig(Qt5UiTools) >= 5.6.0
BuildRequires:  pkgconfig(Qt5WebEngine) >= 5.6.0
BuildRequires:  pkgconfig(Qt5WebEngineWidgets) >= 5.6.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.6.0
BuildRequires:  pkgconfig(Qt5X11Extras) >= 5.6.0
BuildRequires:  pkgconfig(Qt5XmlPatterns) >= 5.6.0
Requires(post): shared-mime-info
Requires(postun): shared-mime-info
Recommends:     %{name}-lang
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif

%description
Addons for KDE PIM applications, such as extensions for KMail, additional
themes, and plugins providing extra or advanced functionality.

%lang_package

%prep
%setup -q
%autopatch -p1

%build
%cmake_kf5 -d build -- -DKDEPIMADDONS_BUILD_EXAMPLES=FALSE -DQTCREATOR_TEMPLATE_INSTALL_DIR=%{_kf5_sharedir}/qtcreator/templates
%make_jobs

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
%dir %{_kf5_libdir}/contacteditor
%dir %{_kf5_libdir}/contacteditor/editorpageplugins
%dir %{_kf5_plugindir}
%dir %{_kf5_plugindir}/messageviewer
%dir %{_kf5_plugindir}/messageviewer/bodypartformatter
%dir %{_kf5_plugindir}/messageviewer/grantlee
%dir %{_kf5_plugindir}/messageviewer/grantlee/5.0
%dir %{_kf5_qmldir}/org/kde/plasma
%{_kf5_bindir}/kmail_antivir.sh
%{_kf5_bindir}/kmail_clamav.sh
%{_kf5_bindir}/kmail_fprot.sh
%{_kf5_bindir}/kmail_sav.sh
%{_kf5_libdir}/contacteditor/editorpageplugins/cryptopageplugin.so
%{_kf5_libdir}/libadblocklibprivate.so.*
%{_kf5_libdir}/libkaddressbookimportexportlibprivate.so.*
%{_kf5_libdir}/libkaddressbookmergelibprivate.so.*
%{_kf5_libdir}/libshorturlpluginprivate.so.*
%{_kf5_libdir}/libkmailgrammalecte.so.5.*
%{_kf5_libdir}/libkmailgrammalecte.so.5
%{_kf5_libdir}/libgrammarcommon.so.5
%{_kf5_libdir}/libgrammarcommon.so.5.*
%{_kf5_libdir}/libkmaillanguagetool.so.5
%{_kf5_libdir}/libkmaillanguagetool.so.5.*
%{_kf5_plugindir}/importwizard/
%{_kf5_plugindir}/contacteditor/
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
%{_kf5_plugindir}/messageviewer/messageviewer_*.so
%{_kf5_plugindir}/messageviewer/grantlee/5.0/kitinerary_grantlee_extension.so
%{_kf5_qmldir}/org/kde/plasma/PimCalendars/
%{_kf5_servicesdir}/korganizer/
%{_kf5_sharedir}/contacteditor/
%{_kf5_sharedir}/kconf_update/webengineurlinterceptoradblock.upd
%{_kf5_sharedir}/kconf_update/languagetool_kmail.upd
%{_kf5_sharedir}/kmail2/
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
