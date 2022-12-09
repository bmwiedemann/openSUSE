#
# spec file for package konqueror
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
Name:           konqueror
Version:        22.12.0
Release:        0
Summary:        KDE File Manager and Browser
# Note for legal: konqueror-17.04.2/webenginepart/autotests/webengine_testutils.h is Qt commercial OR GPL-3.0
# but it is neither built nor installed in our package.
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/konqueror
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  libtidy-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KDED)
BuildRequires:  cmake(KF5Activities)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  cmake(KF5KHtml)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Su)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Script)
BuildRequires:  cmake(Qt5TextToSpeech)
BuildRequires:  cmake(Qt5WebEngine)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
Requires:       webenginepart
Recommends:     %{name}-plugins
Recommends:     dolphin-part
Obsoletes:      kde-baseapps5-libkonq < %{version}
Provides:       kde-baseapps5-libkonq = %{version}
Obsoletes:      kde-baseapps-libkonq < %{version}
Provides:       kde-baseapps-libkonq = %{version}
Obsoletes:      %{name}-libkonq < %{version}
Provides:       %{name}-libkonq = %{version}
Obsoletes:      kdebase4-libkonq
Obsoletes:      libKF5Konq6 < 17.04
Provides:       libKF5Konq6 = 17.04
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64

%description
Konqueror allows you to manage your files and browse the web in a
unified interface.

%package -n webenginepart
Summary:        KDE WebEngine web browser component

%description -n webenginepart
This package contains a HTML rendering engine for Konqueror that is based on QtWebEngine.

%package -n konqueror-plugins
Summary:        KDE File Manager and Browser
Requires:       %{name} = %{version}
Obsoletes:      fsview5 < %{version}
Provides:       fsview5 = %{version}
Obsoletes:      konqueror5-plugins < %{version}
Provides:       konqueror5-plugins = %{version}

%description -n konqueror-plugins
These plugins extend the functionality of Konqueror.

%package  devel
Summary:        KDE Konqueror Libraries: Build Environment
Requires:       %{name} = %{version}
Obsoletes:      kdebase4-devel
# FIXME 4.x variants of DBus interfaces need to go to devel package
Obsoletes:      kde-baseapps5-devel < %{version}
Provides:       kde-baseapps5-devel = %{version}
Obsoletes:      kde-baseapps-devel < %{version}
Provides:       kde-baseapps-devel = %{version}
Obsoletes:      libkonq-devel < %{version}
Provides:       libkonq-devel = %{version}

%description devel
Development package for the konqueror libraries.

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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post   -n konqueror-plugins -p /sbin/ldconfig
%postun -n konqueror-plugins -p /sbin/ldconfig

%files
%license LICENSES/*
%config %{_kf5_configdir}/autostart/konqy_preload.desktop
%{_kf5_debugdir}/konqueror.categories
%dir %{_kf5_sharedir}/konqsidebartng
%dir %{_kf5_sharedir}/konqsidebartng/entries
%dir %{_kf5_sharedir}/konqsidebartng/plugins
%dir %{_kf5_sharedir}/kcontrol
%dir %{_kf5_sharedir}/kcontrol/pics
%dir %{_kf5_sharedir}/kxmlgui5
%dir %{_kf5_plugindir}/konqueror_kcms
%doc %lang(en) %{_kf5_htmldir}/en
%{_datadir}/kcmcss/
%{_kf5_applicationsdir}/kfmclient.desktop
%{_kf5_applicationsdir}/kfmclient_dir.desktop
%{_kf5_applicationsdir}/kfmclient_html.desktop
%{_kf5_applicationsdir}/kfmclient_war.desktop
%{_kf5_applicationsdir}/konqbrowser.desktop
%{_kf5_applicationsdir}/org.kde.konqueror.desktop
%{_kf5_appstreamdir}/org.kde.konqueror.appdata.xml
%{_kf5_bindir}/kfmclient
%{_kf5_bindir}/konqueror
%{_kf5_configkcfgdir}/konqueror.kcfg
%{_kf5_datadir}/kbookmark/
%{_kf5_dbusinterfacesdir}/org.kde.Konqueror.Main.xml
%{_kf5_dbusinterfacesdir}/org.kde.Konqueror.MainWindow.xml
%{_kf5_iconsdir}/hicolor/*/*/konqueror.*
%{_kf5_libdir}/libKF5Konq.so.*
%{_kf5_libdir}/libkdeinit5_kfmclient.so
%{_kf5_libdir}/libkdeinit5_konqueror.so
%{_kf5_libdir}/libkonquerorprivate.so.*
%{_kf5_plugindir}/konqueror_kcms/kcm_bookmarks.so
%{_kf5_plugindir}/konqueror_kcms/kcm_konq.so
%{_kf5_plugindir}/konqueror_kcms/kcm_performance.so
%{_kf5_plugindir}/konqueror_kcms/khtml_appearance.so
%{_kf5_plugindir}/konqueror_kcms/khtml_behavior.so
%{_kf5_plugindir}/konqueror_kcms/khtml_filter.so
%{_kf5_plugindir}/konqueror_kcms/khtml_general.so
%{_kf5_plugindir}/konqueror_kcms/khtml_java_js.so
%{_kf5_servicesdir}/org.kde.konqueror.desktop
%{_kf5_sharedir}/kconf_update/webenginepart.upd
%{_kf5_sharedir}/kcontrol/pics/onlyone.png
%{_kf5_sharedir}/kcontrol/pics/overlapping.png
%{_kf5_sharedir}/konqueror/

%files -n webenginepart
%dir %{_kf5_plugindir}/kf5/
%dir %{_kf5_plugindir}/kf5/parts/
%dir %{_kf5_sharedir}/webenginepart/
%{_kf5_iconsdir}/hicolor/*/*/webengine.*
%{_kf5_kxmlguidir}/webenginepart/
%{_kf5_libdir}/libkwebenginepart.so
%{_kf5_plugindir}/kf5/parts/webenginepart.so
%{_kf5_servicesdir}/webenginepart.desktop
%{_kf5_sharedir}/webenginepart/error.html

%files -n konqueror-plugins
%config %{_kf5_configdir}/konqsidebartngrc
%config %{_kf5_configdir}/translaterc
%dir %{_kf5_kxmlguidir}/fsview
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/parts
%dir %{_kf5_plugindir}/khtml
%dir %{_kf5_plugindir}/khtml/kpartplugins
%dir %{_kf5_plugindir}/dolphinpart
%dir %{_kf5_plugindir}/dolphinpart/kpartplugins
%dir %{_kf5_plugindir}/konqueror
%dir %{_kf5_plugindir}/konqueror/kpartplugins
%dir %{_kf5_plugindir}/kwebkitpart
%dir %{_kf5_plugindir}/kwebkitpart/kpartplugins
%dir %{_kf5_plugindir}/webenginepart
%dir %{_kf5_plugindir}/webenginepart/kpartplugins
%{_kf5_bindir}/fsview
%{_kf5_bindir}/kcreatewebarchive
%{_kf5_configkcfgdir}/kcreatewebarchive.kcfg
%{_kf5_debugdir}/akregatorplugin.categories
%{_kf5_debugdir}/fsview.categories
%{_kf5_iconsdir}/*/*/actions/babelfish.*
%{_kf5_iconsdir}/*/*/actions/imagegallery.png
%{_kf5_iconsdir}/*/*/actions/webarchiver.*
%{_kf5_iconsdir}/hicolor/*/apps/fsview.png
%{_kf5_kxmlguidir}/fsview/fsview_part.rc
%{_kf5_libdir}/libkonqsidebarplugin.so.*
%{_kf5_plugindir}/akregatorkonqfeedicon.so
%dir %{_kf5_plugindir}/kf5/kfileitemaction/
%{_kf5_plugindir}/kf5/kfileitemaction/akregatorplugin.so
%{_kf5_plugindir}/autorefresh.so
%{_kf5_plugindir}/babelfishplugin.so
%{_kf5_plugindir}/khtmlttsplugin.so
%{_kf5_plugindir}/konqueror_kcms/kcm_history.so
%{_kf5_plugindir}/kf5/parts/fsviewpart.so
%{_kf5_plugindir}/kf5/parts/konq_sidebar.so
%{_kf5_plugindir}/khtmlsettingsplugin.so
%{_kf5_plugindir}/konqsidebar_bookmarks.so
%{_kf5_plugindir}/konqsidebar_history.so
%{_kf5_plugindir}/konqsidebar_places.so
%{_kf5_plugindir}/konqsidebar_tree.so
%{_kf5_plugindir}/konqueror_kget_browser_integration.so
%{_kf5_plugindir}/uachangerplugin.so
%{_kf5_plugindir}/webarchiverplugin.so
%{_kf5_plugindir}/webarchivethumbnail.so
%{_kf5_plugindir}/dolphinpart/kpartplugins/kimgallery.so
%{_kf5_plugindir}/dolphinpart/kpartplugins/konq_shellcmdplugin.so
%{_kf5_plugindir}/dolphinpart/kpartplugins/dirfilterplugin.so
%{_kf5_plugindir}/khtml/kpartplugins/akregatorkonqfeediconkhtml_kpartplugins.so
%{_kf5_plugindir}/khtml/kpartplugins/autorefreshkhtml_kpartplugins.so
%{_kf5_plugindir}/khtml/kpartplugins/babelfishpluginkhtml_kpartplugins.so
%{_kf5_plugindir}/khtml/kpartplugins/khtmlsettingspluginkhtml_kpartplugins.so
%{_kf5_plugindir}/khtml/kpartplugins/khtmlttspluginkhtml_kpartplugins.so
%{_kf5_plugindir}/khtml/kpartplugins/konqueror_kget_browser_integrationkhtml_kpartplugins.so
%{_kf5_plugindir}/khtml/kpartplugins/uachangerpluginkhtml_kpartplugins.so
%{_kf5_plugindir}/khtml/kpartplugins/webarchiverpluginkhtml_kpartplugins.so
%{_kf5_plugindir}/konqueror/kpartplugins/searchbarplugin.so
%{_kf5_plugindir}/kwebkitpart/kpartplugins/akregatorkonqfeediconkwebkitpart_kpartplugins.so
%{_kf5_plugindir}/kwebkitpart/kpartplugins/autorefreshkwebkitpart_kpartplugins.so
%{_kf5_plugindir}/kwebkitpart/kpartplugins/babelfishpluginkwebkitpart_kpartplugins.so
%{_kf5_plugindir}/kwebkitpart/kpartplugins/khtmlsettingspluginkwebkitpart_kpartplugins.so
%{_kf5_plugindir}/kwebkitpart/kpartplugins/khtmlttspluginkwebkitpart_kpartplugins.so
%{_kf5_plugindir}/kwebkitpart/kpartplugins/konqueror_kget_browser_integrationkwebkitpart_kpartplugins.so
%{_kf5_plugindir}/kwebkitpart/kpartplugins/uachangerpluginkwebkitpart_kpartplugins.so
%{_kf5_plugindir}/kwebkitpart/kpartplugins/webarchiverpluginkwebkitpart_kpartplugins.so
%{_kf5_plugindir}/webenginepart/kpartplugins/akregatorkonqfeediconwebenginepart_kpartplugins.so
%{_kf5_plugindir}/webenginepart/kpartplugins/autorefreshwebenginepart_kpartplugins.so
%{_kf5_plugindir}/webenginepart/kpartplugins/babelfishpluginwebenginepart_kpartplugins.so
%{_kf5_plugindir}/webenginepart/kpartplugins/khtmlsettingspluginwebenginepart_kpartplugins.so
%{_kf5_plugindir}/webenginepart/kpartplugins/khtmlttspluginwebenginepart_kpartplugins.so
%{_kf5_plugindir}/webenginepart/kpartplugins/konqueror_kget_browser_integrationwebenginepart_kpartplugins.so
%{_kf5_plugindir}/webenginepart/kpartplugins/uachangerpluginwebenginepart_kpartplugins.so
%{_kf5_plugindir}/webenginepart/kpartplugins/webarchiverpluginwebenginepart_kpartplugins.so
%{_kf5_servicesdir}/fsview_part.desktop
%{_kf5_servicesdir}/konq_sidebartng.desktop
%{_kf5_servicesdir}/webarchivethumbnail.desktop
%{_kf5_sharedir}/akregator/
%{_kf5_sharedir}/konqsidebartng/entries/bookmarks.desktop
%{_kf5_sharedir}/konqsidebartng/entries/fonts.desktop
%{_kf5_sharedir}/konqsidebartng/entries/history.desktop
%{_kf5_sharedir}/konqsidebartng/entries/home.desktop
%{_kf5_sharedir}/konqsidebartng/entries/places.desktop
%{_kf5_sharedir}/konqsidebartng/entries/remote.desktop
%{_kf5_sharedir}/konqsidebartng/entries/root.desktop
%{_kf5_sharedir}/konqsidebartng/entries/services.desktop
%{_kf5_sharedir}/konqsidebartng/plugins/konqsidebar_bookmarks.desktop
%{_kf5_sharedir}/konqsidebartng/plugins/konqsidebar_history.desktop
%{_kf5_sharedir}/konqsidebartng/plugins/konqsidebar_places.desktop
%{_kf5_sharedir}/konqsidebartng/plugins/konqsidebar_tree.desktop

%files devel
%{_kf5_cmakedir}/KF5Konq/
%{_kf5_libdir}/libKF5Konq.so
%{_kf5_libdir}/libkonqsidebarplugin.so
%{_kf5_includedir}/
%{_includedir}/konqsidebarplugin.h

%files lang -f %{name}.lang

%changelog
