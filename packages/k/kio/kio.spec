#
# spec file for package kio
#
# Copyright (c) 2021 SUSE LLC
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


%define _tar_path 5.82
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kio
Version:        5.82.0
Release:        0
Summary:        Network transparent access to files and data
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
# PATCH-FIX-OPENSUSE kio_help-fallback-to-kde4-docs.patch -- allow kio_help to see into kde4 documentation, needed especially for khelpcenter5
Patch0:         kio_help-fallback-to-kde4-docs.patch
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  krb5-devel
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5Archive) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Bookmarks) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Completion) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5ConfigWidgets) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Crash) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5DocTools) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5GuiAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5IconThemes) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5ItemViews) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5JobWidgets) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Notifications) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Service) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Solid) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5TextWidgets) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Wallet) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5XmlGui) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5Concurrent) >= 5.15.0
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5DBus) >= 5.15.0
BuildRequires:  cmake(Qt5Network) >= 5.15.0
BuildRequires:  cmake(Qt5Qml) >= 5.15.0
BuildRequires:  cmake(Qt5Test) >= 5.15.0
BuildRequires:  cmake(Qt5UiPlugin) >= 5.15.0
BuildRequires:  cmake(Qt5Widgets) >= 5.15.0
BuildRequires:  cmake(Qt5X11Extras) >= 5.15.0
BuildRequires:  cmake(Qt5Xml) >= 5.15.0
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(x11)
Requires:       %{name}-core = %{version}
Requires:       kded >= %{_kf5_bugfix_version}
# KIO/FileDialog uses klauncher directly, but we can't add Requires, as that would introduce dep cycle
Recommends:     kinit
%if %{with lang}
Recommends:     %{name}-lang = %{version}
%endif

%description
This framework implements almost all the file management functions you
will ever need. In fact, the KDE file manager (Dolphin) and the KDE
file dialog also uses this to provide its network-enabled file management.

%package core
Summary:        Network transparent access to files and data
Group:          System/GUI/KDE

# core subpackage created with 5.9.0
Conflicts:      kio <= 5.8.0

%description core
This framework implements almost all the file management functions you
will ever need. In fact, the KDE file manager (Dolphin) and the KDE
file dialog also uses this to provide its network-enabled file management.
KIO core libraries, ioslave and daemons.

%package devel
Summary:        Network transparent access to files and data
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}
Requires:       %{name}-core = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(KF5Bookmarks) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5Completion) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5Config) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5CoreAddons) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5ItemViews) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5JobWidgets) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5Service) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5Solid) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5WindowSystem) >= %{_kf5_bugfix_version}
Requires:       cmake(KF5XmlGui) >= %{_kf5_bugfix_version}
Requires:       cmake(Qt5Concurrent) >= 5.15.0
Requires:       cmake(Qt5DBus) >= 5.15.0
Requires:       cmake(Qt5Network) >= 5.15.0

%description devel
This framework implements almost all the file management functions you
will ever need. In fact, the KDE file manager (Dolphin) and the KDE
file dialog also uses this to provide its network-enabled file management.
Development files.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%if %{with lang}
%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}
%endif

%post core -p /sbin/ldconfig
%postun core -p /sbin/ldconfig
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%if %{with lang}
%files lang -f %{name}.lang
%endif

%files core
%doc README*
%license LICENSES/*
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/kio
%dir %{_kf5_plugindir}/kf5/kiod
%dir %{_kf5_sharedir}/kconf_update/
%{_kf5_applicationsdir}/ktelnetservice5.desktop
%{_kf5_bindir}/ktelnetservice5
%{_kf5_bindir}/ktrash5
%{_kf5_configdir}/accept-languages.codes
%{_kf5_debugdir}/kio.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5KIOCore.so.*
%{_kf5_libdir}/libKF5KIONTLM.so.*
%{_kf5_libexecdir}/kio_http_cache_cleaner
%{_kf5_libexecdir}/kiod5
%{_kf5_plugindir}/kcm_trash.so
%{_kf5_plugindir}/kf5/kio/file.so
%{_kf5_plugindir}/kf5/kio/ftp.so
%{_kf5_plugindir}/kf5/kio/ghelp.so
%{_kf5_plugindir}/kf5/kio/help.so
%{_kf5_plugindir}/kf5/kio/http.so
%{_kf5_plugindir}/kf5/kio/trash.so
%{_kf5_plugindir}/kf5/kiod/kssld.so
%{_kf5_servicesdir}/data.protocol
%{_kf5_servicesdir}/http_cache_cleaner.desktop
%{_kf5_servicesdir}/kcmtrash.desktop
%{_kf5_servicesdir}/mailto.protocol
%{_kf5_servicesdir}/mms.protocol
%{_kf5_servicesdir}/mmst.protocol
%{_kf5_servicesdir}/mmsu.protocol
%{_kf5_servicesdir}/pnm.protocol
%{_kf5_servicesdir}/rtsp.protocol
%{_kf5_servicesdir}/rtspt.protocol
%{_kf5_servicesdir}/rtspu.protocol
%{_kf5_sharedir}/dbus-1/services/org.kde.kiod5.service
%{_kf5_sharedir}/dbus-1/services/org.kde.kioexecd.service
%{_kf5_sharedir}/dbus-1/services/org.kde.kssld5.service
%{_kf5_sharedir}/kconf_update/filepicker.upd

%files
%doc README*
%license LICENSES/*
%dir %{_kf5_htmldir}
%dir %{_kf5_htmldir}/en
%dir %{_kf5_plugindir}/kf5/kded
%doc %lang(en) %{_kf5_htmldir}/en/*/
%doc %lang(en) %{_kf5_mandir}/*/kcookiejar5.*
%{_kf5_bindir}/kcookiejar5
%{_kf5_configdir}/kshorturifilterrc
%{_kf5_datadir}/kcookiejar/
%{_kf5_libdir}/libKF5KIOFileWidgets.so.*
%{_kf5_libdir}/libKF5KIOGui.so.*
%{_kf5_libdir}/libKF5KIOWidgets.so.*
%{_kf5_libexecdir}/kioexec
%{_kf5_libexecdir}/kioslave5
%{_kf5_libexecdir}/kpac_dhcp_helper
%{_kf5_notifydir}/proxyscout.notifyrc
%{_kf5_plugindir}/kcm_kio.so
%{_kf5_plugindir}/kcm_webshortcuts.so
%{_kf5_plugindir}/kf5/kded/kcookiejar.so
%{_kf5_plugindir}/kf5/kded/proxyscout.so
%{_kf5_plugindir}/kf5/kded/remotenotifier.so
%{_kf5_plugindir}/kf5/kio/remote.so
%{_kf5_plugindir}/kf5/kiod/kioexecd.so
%{_kf5_plugindir}/kf5/kiod/kpasswdserver.so
%{_kf5_plugindir}/kf5/urifilters/
%{_kf5_servicesdir}/cache.desktop
%{_kf5_servicesdir}/cookies.desktop
%{_kf5_servicesdir}/netpref.desktop
%{_kf5_servicesdir}/proxy.desktop
%{_kf5_servicesdir}/searchproviders/
%{_kf5_servicesdir}/smb.desktop
%{_kf5_servicesdir}/useragent.desktop
%{_kf5_servicesdir}/useragentstrings/
%{_kf5_servicesdir}/webshortcuts.desktop
%{_kf5_servicetypesdir}/
%{_kf5_sharedir}/dbus-1/services/org.kde.kcookiejar5.service
%{_kf5_sharedir}/dbus-1/services/org.kde.kpasswdserver.service

%files devel
%dir %{_kf5_plugindir}/designer
%{_kf5_bindir}/protocoltojson
%{_kf5_dbusinterfacesdir}/kf5_org.kde.KCookieServer.xml
%{_kf5_dbusinterfacesdir}/kf5_org.kde.KDirNotify.xml
%{_kf5_dbusinterfacesdir}/kf5_org.kde.KPasswdServer.xml
%{_kf5_dbusinterfacesdir}/kf5_org.kde.KSlaveLauncher.xml
%{_kf5_dbusinterfacesdir}/kf5_org.kde.kio.FileUndoManager.xml
%dir %{_kf5_sharedir}/kdevappwizard
%dir %{_kf5_sharedir}/kdevappwizard/templates
%{_kf5_sharedir}/kdevappwizard/templates/ioslave.tar.bz2
%{_kf5_includedir}/
%{_kf5_libdir}/cmake/KF5KIO/
%{_kf5_libdir}/libKF5KIOCore.so
%{_kf5_libdir}/libKF5KIOFileWidgets.so
%{_kf5_libdir}/libKF5KIOGui.so
%{_kf5_libdir}/libKF5KIONTLM.so
%{_kf5_libdir}/libKF5KIOWidgets.so
%{_kf5_mkspecsdir}/qt_KIOCore.pri
%{_kf5_mkspecsdir}/qt_KIOFileWidgets.pri
%{_kf5_mkspecsdir}/qt_KIOGui.pri
%{_kf5_mkspecsdir}/qt_KIOWidgets.pri
%{_kf5_mkspecsdir}/qt_KNTLM.pri
%{_kf5_plugindir}/designer/kio5widgets.so

%changelog
