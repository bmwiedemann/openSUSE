#
# spec file for package konqueror
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
Name:           konqueror
Version:        20.08.1
Release:        0
Summary:        KDE File Manager and Browser
# Note for legal: konqueror-17.04.2/webenginepart/autotests/webengine_testutils.h is Qt commercial OR GPL-3.0
# but it is neither built nor installed in our package.
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
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
BuildRequires:  cmake(Qt5WebEngine)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
Recommends:     %{name}-lang
Recommends:     dolphin-part
Recommends:     kwebkitpart
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
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
Konqueror allows you to manage your files and browse the web in a
unified interface.

%package -n webenginepart
Summary:        KDE WebEngine web browser component
Group:          System/GUI/KDE

%description -n webenginepart
This package contains a HTML rendering engine for Konqueror that is based on QtWebEngine.

%package -n konqueror-plugins
Summary:        KDE File Manager and Browser
Group:          Productivity/Networking/Web/Browsers
Requires:       %{name} = %{version}
Obsoletes:      fsview5 < %{version}
Provides:       fsview5 = %{version}
Obsoletes:      konqueror5-plugins < %{version}
Provides:       konqueror5-plugins = %{version}

%description -n konqueror-plugins
These plugins extend the functionality of Konqueror.

%package  devel
Summary:        KDE Konqueror Libraries: Build Environment
Group:          Development/Libraries/KDE
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
%setup -q

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %{kf5_find_htmldocs}
%endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post   -n konqueror-plugins -p /sbin/ldconfig
%postun -n konqueror-plugins -p /sbin/ldconfig

%files
%license COPYING*
%config %{_kf5_configdir}/autostart/konqy_preload.desktop
%{_kf5_debugdir}/konqueror.categories
%dir %{_kf5_appstreamdir}
%dir %{_kf5_configkcfgdir}
%dir %{_kf5_datadir}
%dir %{_kf5_plugindir}
%dir %{_kf5_servicesdir}
%dir %{_kf5_sharedir}/konqsidebartng
%dir %{_kf5_sharedir}/konqsidebartng/entries
%dir %{_kf5_sharedir}/konqsidebartng/plugins
%dir %{_kf5_sharedir}/kcontrol
%dir %{_kf5_sharedir}/kcontrol/pics
%dir %{_kf5_sharedir}/khtml
%dir %{_kf5_sharedir}/khtml/kpartplugins
%dir %{_kf5_sharedir}/kwebkitpart
%dir %{_kf5_sharedir}/kwebkitpart/kpartplugins
%dir %{_kf5_sharedir}/webenginepart/kpartplugins
%dir %{_kf5_sharedir}/kxmlgui5
%doc %lang(en) %{_kf5_htmldir}/en
%{_datadir}/kcmcss/
%{_kf5_applicationsdir}/kfmclient.desktop
%{_kf5_applicationsdir}/kfmclient_dir.desktop
%{_kf5_applicationsdir}/kfmclient_html.desktop
%{_kf5_applicationsdir}/kfmclient_war.desktop
%{_kf5_applicationsdir}/konqbrowser.desktop
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
%{_kf5_plugindir}/kcm_bookmarks.so
%{_kf5_plugindir}/kcm_konq.so
%{_kf5_plugindir}/kcm_konqhtml.so
%{_kf5_plugindir}/kcm_performance.so
%{_kf5_servicesdir}/bookmarks.desktop
%{_kf5_servicesdir}/filebehavior.desktop
%{_kf5_servicesdir}/kcmkonqyperformance.desktop
%{_kf5_servicesdir}/kcmperformance.desktop
%{_kf5_servicesdir}/khtml_*.desktop
%{_kf5_servicesdir}/org.kde.konqueror.desktop
%{_kf5_sharedir}/kcontrol/pics/onlyone.png
%{_kf5_sharedir}/kcontrol/pics/overlapping.png
%{_kf5_sharedir}/konqueror/

%files -n webenginepart
%license COPYING*
%{_kf5_libdir}/libkwebenginepart.so
%{_kf5_iconsdir}/hicolor/*/*/webengine.*
%{_kf5_kxmlguidir}/webenginepart/
%{_kf5_plugindir}/kf5/
%{_kf5_servicesdir}/webenginepart.desktop
%dir %{_kf5_sharedir}/webenginepart/
%{_kf5_sharedir}/webenginepart/error.html

%files -n konqueror-plugins
%license COPYING*
%{_kf5_bindir}/fsview
%config %{_kf5_configdir}/konqsidebartngrc
%{_kf5_debugdir}/akregatorplugin.categories
%{_kf5_debugdir}/fsview.categories
%{_kf5_plugindir}/fsviewpart.so
%{_kf5_iconsdir}/hicolor/*/apps/fsview.png
%{_kf5_servicesdir}/fsview_part.desktop
%{_kf5_libdir}/libkonqsidebarplugin.so.*
%{_kf5_plugindir}/akregatorkonqfeedicon.so
%{_kf5_plugindir}/babelfishplugin.so
%{_kf5_plugindir}/khtmlsettingsplugin.so
%{_kf5_plugindir}/dirfilterplugin.so
%{_kf5_plugindir}/kcm_history.so
%{_kf5_plugindir}/konq_sidebar.so
%{_kf5_plugindir}/konqsidebar_bookmarks.so
%{_kf5_plugindir}/konqsidebar_history.so
%{_kf5_plugindir}/konqsidebar_places.so
%{_kf5_plugindir}/konqsidebar_tree.so
%{_kf5_plugindir}/konq_shellcmdplugin.so
%{_kf5_plugindir}/autorefresh.so
%{_kf5_plugindir}/kimgallery.so
%{_kf5_plugindir}/searchbarplugin.so
%{_kf5_plugindir}/uachangerplugin.so
%{_kf5_iconsdir}/*/*/actions/imagegallery.png
%{_kf5_iconsdir}/*/*/actions/babelfish.*
%{_kf5_sharedir}/akregator/
%{_kf5_sharedir}/konqsidebartng/entries/bookmarks.desktop
%{_kf5_sharedir}/konqsidebartng/entries/fonts.desktop
%{_kf5_sharedir}/konqsidebartng/entries/history.desktop
%{_kf5_sharedir}/konqsidebartng/entries/home.desktop
%{_kf5_sharedir}/konqsidebartng/entries/places.desktop
%{_kf5_sharedir}/konqsidebartng/entries/remote.desktop
%{_kf5_sharedir}/konqsidebartng/entries/root.desktop
%{_kf5_sharedir}/konqsidebartng/entries/services.desktop
%{_kf5_sharedir}/konqsidebartng/entries/settings.desktop
%{_kf5_sharedir}/konqsidebartng/plugins/konqsidebar_bookmarks.desktop
%{_kf5_sharedir}/konqsidebartng/plugins/konqsidebar_history.desktop
%{_kf5_sharedir}/konqsidebartng/plugins/konqsidebar_places.desktop
%{_kf5_sharedir}/konqsidebartng/plugins/konqsidebar_tree.desktop
%{_kf5_sharedir}/khtml/kpartplugins/akregator_konqfeedicon.*
%{_kf5_sharedir}/khtml/kpartplugins/plugin_babelfish.*
%{_kf5_sharedir}/khtml/kpartplugins/plugin_translator.*
%{_kf5_sharedir}/khtml/kpartplugins/autorefresh.*
%{_kf5_sharedir}/khtml/kpartplugins/khtmlsettingsplugin.*
%{_kf5_sharedir}/khtml/kpartplugins/uachangerplugin.*
%{_kf5_sharedir}/kwebkitpart/kpartplugins/akregator_konqfeedicon.*
%{_kf5_sharedir}/kwebkitpart/kpartplugins/plugin_babelfish.*
%{_kf5_sharedir}/kwebkitpart/kpartplugins/plugin_translator.*
%{_kf5_sharedir}/kwebkitpart/kpartplugins/autorefresh.*
%{_kf5_sharedir}/kwebkitpart/kpartplugins/khtmlsettingsplugin.*
%{_kf5_sharedir}/kwebkitpart/kpartplugins/uachangerplugin.*
%{_kf5_sharedir}/webenginepart/kpartplugins/akregator_konqfeedicon.desktop
%{_kf5_sharedir}/webenginepart/kpartplugins/akregator_konqfeedicon.rc
%{_kf5_sharedir}/webenginepart/kpartplugins/autorefresh.desktop
%{_kf5_sharedir}/webenginepart/kpartplugins/autorefresh.rc
%{_kf5_sharedir}/webenginepart/kpartplugins/khtmlsettingsplugin.desktop
%{_kf5_sharedir}/webenginepart/kpartplugins/khtmlsettingsplugin.rc
%{_kf5_sharedir}/webenginepart/kpartplugins/plugin_babelfish.rc
%{_kf5_sharedir}/webenginepart/kpartplugins/plugin_translator.desktop
%{_kf5_sharedir}/webenginepart/kpartplugins/uachangerplugin.*
%{_kf5_servicesdir}/akregator_konqplugin.desktop
%{_kf5_servicesdir}/kcmhistory.desktop
%{_kf5_servicesdir}/konq_sidebartng.desktop
%dir %{_kf5_kxmlguidir}/fsview
%{_kf5_kxmlguidir}/fsview/fsview_part.rc
%config %{_kf5_configdir}/translaterc
%dir %{_kf5_sharedir}/dolphinpart
%{_kf5_sharedir}/dolphinpart/kpartplugins/

%files devel
%license COPYING*
#doc README
%{_kf5_cmakedir}/KF5Konq/
%{_kf5_libdir}/libKF5Konq.so
%{_kf5_libdir}/libkonqsidebarplugin.so
%{_kf5_includedir}/
%{_includedir}/konqsidebarplugin.h

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
