#
# spec file for package konqueror
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

%bcond_without released
Name:           konqueror
Version:        24.05.1
Release:        0
Summary:        KDE File Manager and Browser
# Note for legal: webenginepart/autotests/webengine_testutils.h is neither built nor installed in our package.
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/konqueror
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Bookmarks) >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6Sonnet) >= %{kf6_version}
BuildRequires:  cmake(KF6Su) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6Wallet) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6TextToSpeech) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(zlib)
Requires:       webenginepart
Recommends:     konqueror-plugins
Recommends:     dolphin-part
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  x86_64 %{x86_64} aarch64 riscv64

%description
Konqueror allows you to manage your files and browse the web in a
unified interface.

%package -n webenginepart
Summary:        KDE WebEngine web browser component

%description -n webenginepart
This package contains a HTML rendering engine for Konqueror using Qt web engine.

%package -n konqueror-plugins
Summary:        KDE File Manager and Browser
Requires:       konqueror = %{version}
Obsoletes:      fsview5 < %{version}
Provides:       fsview5 = %{version}
Obsoletes:      konqueror5-plugins < %{version}
Provides:       konqueror5-plugins = %{version}

%description -n konqueror-plugins
These plugins extend the functionality of Konqueror.

%package  devel
Summary:        KDE Konqueror Libraries: Build Environment
Requires:       konqueror = %{version}
Obsoletes:      libkonq-devel < %{version}
Provides:       libkonq-devel = %{version}

%description devel
Development package for the konqueror libraries.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

# No webkit anymore
rm -r %{buildroot}%{_kf6_plugindir}/kwebkitpart

%find_lang %{name} --with-html --all-name

%ldconfig_scriptlets
%ldconfig_scriptlets -n konqueror-plugins

%files
%license LICENSES/*
%config %{_kf6_configdir}/autostart/konqy_preload.desktop
%{_kf6_sharedir}/kcontrol/
%doc %lang(en) %{_kf6_htmldir}/en
%{_kf6_applicationsdir}/bookmarks.desktop
%{_kf6_applicationsdir}/kcm_bookmarks.desktop
%{_kf6_applicationsdir}/kfmclient.desktop
%{_kf6_applicationsdir}/kfmclient_dir.desktop
%{_kf6_applicationsdir}/kfmclient_html.desktop
%{_kf6_applicationsdir}/kfmclient_war.desktop
%{_kf6_applicationsdir}/konqbrowser.desktop
%{_kf6_applicationsdir}/org.kde.konqueror.desktop
%{_kf6_appstreamdir}/org.kde.konqueror.appdata.xml
%{_kf6_bindir}/kfmclient
%{_kf6_bindir}/konqueror
%{_kf6_configdir}/useragenttemplatesrc
%{_kf6_configkcfgdir}/konqueror.kcfg
%{_kf6_datadir}/kbookmark/
%{_kf6_dbusinterfacesdir}/org.kde.Konqueror.Main.xml
%{_kf6_dbusinterfacesdir}/org.kde.Konqueror.MainWindow.xml
%{_kf6_debugdir}/konqueror.categories
%{_kf6_iconsdir}/hicolor/*/*/konqueror.*
%{_kf6_libdir}/libKF6Konq.so.*
%{_kf6_libdir}/libkonquerorprivate.so.*
%dir %{_kf6_plugindir}/konqueror_kcms
%{_kf6_plugindir}/konqueror_kcms/kcm_bookmarks.so
%{_kf6_plugindir}/konqueror_kcms/kcm_history.so
%{_kf6_plugindir}/konqueror_kcms/kcm_konq.so
%{_kf6_plugindir}/konqueror_kcms/kcm_performance.so
%{_kf6_plugindir}/konqueror_kcms/khtml_*.so
%{_kf6_sharedir}/kcmcss/
%{_kf6_sharedir}/kconf_update/webenginepart.upd
%{_kf6_sharedir}/konqueror/

%files -n webenginepart
%{_kf6_iconsdir}/hicolor/*/*/webengine.*
%{_kf6_libdir}/libkwebenginepart.so
%{_kf6_plugindir}/kf6/parts/webenginepart.so
%{_kf6_sharedir}/webenginepart/

%files -n konqueror-plugins
%config %{_kf6_configdir}/konqsidebartngrc
%config %{_kf6_configdir}/translaterc
%{_kf6_bindir}/fsview
%{_kf6_bindir}/kcreatewebarchive
%{_kf6_configkcfgdir}/kcreatewebarchive.kcfg
%{_kf6_debugdir}/akregatorplugin.categories
%{_kf6_debugdir}/fsview.categories
%{_kf6_iconsdir}/*/*/actions/babelfish.png
%{_kf6_iconsdir}/*/*/actions/imagegallery.png
%{_kf6_iconsdir}/*/*/actions/webarchiver.png
%{_kf6_iconsdir}/hicolor/*/apps/fsview.png
%{_kf6_libdir}/libkonqsidebarplugin.so.*
%{_kf6_plugindir}/akregatorkonqfeedicon.so
%{_kf6_plugindir}/autorefresh.so
%{_kf6_plugindir}/babelfishplugin.so
%dir %{_kf6_plugindir}/dolphinpart
%dir %{_kf6_plugindir}/dolphinpart/kpartplugins
%{_kf6_plugindir}/dolphinpart/kpartplugins/dirfilterplugin.so
%{_kf6_plugindir}/dolphinpart/kpartplugins/kimgallery.so
%{_kf6_plugindir}/dolphinpart/kpartplugins/konq_shellcmdplugin.so
%dir %{_kf6_plugindir}/kf6/kfileitemaction/
%{_kf6_plugindir}/kf6/kfileitemaction/akregatorplugin.so
%{_kf6_plugindir}/kf6/kio/bookmarks.so
%{_kf6_plugindir}/kf6/parts/fsviewpart.so
%{_kf6_plugindir}/kf6/parts/konq_sidebar.so
%dir %{_kf6_plugindir}/kf6/thumbcreator
%{_kf6_plugindir}/kf6/thumbcreator/webarchivethumbnail.so
# webenginepart/kpartplugins/khtmlsettingspluginwebenginepart_kpartplugins.so is a symlink to this file
%{_kf6_plugindir}/khtmlsettingsplugin.so
%{_kf6_plugindir}/khtml/
%dir %{_kf6_plugindir}/konqueror
%dir %{_kf6_plugindir}/konqueror/kpartplugins
%{_kf6_plugindir}/konqueror/kpartplugins/searchbarplugin.so
%{_kf6_plugindir}/konqueror/sidebar/
%{_kf6_plugindir}/konqueror_kget_browser_integration.so
%{_kf6_plugindir}/uachangerplugin.so
%{_kf6_plugindir}/webarchiverplugin.so
%{_kf6_plugindir}/webenginepart/
%{_kf6_sharedir}/akregator/
%{_kf6_sharedir}/kio_bookmarks/
%{_kf6_sharedir}/konqsidebartng/

%files devel
%{_kf6_cmakedir}/KF6Konq/
%{_kf6_includedir}/asyncselectorinterface.h
%{_kf6_includedir}/*konq*.h
%{_kf6_libdir}/libKF6Konq.so
%{_kf6_libdir}/libkonqsidebarplugin.so

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en

%changelog
