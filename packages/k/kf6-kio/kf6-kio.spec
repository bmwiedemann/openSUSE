#
# spec file for package kf6-kio
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


%define qt6_version 6.6.0

%define rname kio
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kio
Version:        6.3.0
Release:        0
Summary:        Network transparent access to files and data
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  libattr-devel
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Archive) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Auth) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Bookmarks) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6ColorScheme) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Completion) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Crash) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6DocTools) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6IconThemes) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6ItemViews) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6KDED) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Service) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Solid) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Wallet) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiPlugin) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(x11)
Requires:       kf6-kded >= %{_kf6_bugfix_version}
# For discrete GPU discovery
Recommends:     switcheroo-control

%description
This framework implements almost all the file management functions you
will ever need. In fact, the KDE file manager (Dolphin) and the KDE
file dialog also uses this to provide its network-enabled file management.

%package doc
Summary:        HTML documentation for KIO

%description doc
This package contains documentation for the KIO framework.

%package -n libKF6KIO6
Summary:        KIO Libraries
Requires:       kf6-kio >= %{version}

%description -n libKF6KIO6
Network transparent access to files and data

%package devel
Summary:        Network transparent access to files and data
Requires:       libKF6KIO6 = %{version}
Requires:       cmake(KF6Bookmarks) >= %{_kf6_bugfix_version}
Requires:       cmake(KF6Completion) >= %{_kf6_bugfix_version}
Requires:       cmake(KF6Config) >= %{_kf6_bugfix_version}
Requires:       cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}
Requires:       cmake(KF6ItemViews) >= %{_kf6_bugfix_version}
Requires:       cmake(KF6JobWidgets) >= %{_kf6_bugfix_version}
Requires:       cmake(KF6Service) >= %{_kf6_bugfix_version}
Requires:       cmake(KF6Solid) >= %{_kf6_bugfix_version}
Requires:       cmake(KF6WindowSystem) >= %{_kf6_bugfix_version}
Requires:       cmake(KF6XmlGui) >= %{_kf6_bugfix_version}
Requires:       cmake(Qt6Concurrent) >= %{qt6_version}
Requires:       cmake(Qt6DBus) >= %{qt6_version}
Requires:       cmake(Qt6Network) >= %{qt6_version}

%description devel
This framework implements almost all the file management functions you
will ever need. In fact, the KDE file manager (Dolphin) and the KDE
file dialog also uses this to provide its network-enabled file management.
Development files.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%ifarch ppc64
%define _lto_cflags %{nil}
%endif

%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kio --with-man --all-name

%ldconfig_scriptlets -n libKF6KIO6

%files
%{_kf6_applicationsdir}/ktelnetservice6.desktop
%{_kf6_bindir}/ktelnetservice6
%{_kf6_bindir}/ktrash6
%{_kf6_datadir}/searchproviders/
%{_kf6_debugdir}/kio.categories
%{_kf6_debugdir}/kio.renamecategories
%{_kf6_libdir}/libkuriikwsfiltereng_private.so
%{_kf6_libexecdir}/kiod6
%{_kf6_libexecdir}/kioexec
%{_kf6_libexecdir}/kioworker
%{_kf6_plugindir}/designer/kio6widgets.so
%{_kf6_plugindir}/kf6/kded/remotenotifier.so
%{_kf6_plugindir}/kf6/kio/kio_file.so
%{_kf6_plugindir}/kf6/kio/kio_ftp.so
%{_kf6_plugindir}/kf6/kio/kio_ghelp.so
%{_kf6_plugindir}/kf6/kio/kio_help.so
%{_kf6_plugindir}/kf6/kio/kio_http.so
%{_kf6_plugindir}/kf6/kio/kio_remote.so
%{_kf6_plugindir}/kf6/kio/kio_trash.so
%dir %{_kf6_plugindir}/kf6/kiod
%{_kf6_plugindir}/kf6/kiod/kioexecd.so
%{_kf6_plugindir}/kf6/kiod/kpasswdserver.so
%{_kf6_plugindir}/kf6/kiod/kssld.so
%{_kf6_plugindir}/kf6/urifilters/
%{_kf6_sharedir}/dbus-1/services/org.kde.kiod6.service
%{_kf6_sharedir}/dbus-1/services/org.kde.kioexecd6.service
%{_kf6_sharedir}/dbus-1/services/org.kde.kpasswdserver6.service
%{_kf6_sharedir}/dbus-1/services/org.kde.kssld6.service

%files doc
%{_kf6_htmldir}/*

%files -n libKF6KIO6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6KIOCore.so.*
%{_kf6_libdir}/libKF6KIOFileWidgets.so.*
%{_kf6_libdir}/libKF6KIOGui.so.*
%{_kf6_libdir}/libKF6KIOWidgets.so.*

%files devel
%doc %{_kf6_qchdir}/KF6KIO.*
%{_kf6_cmakedir}/KF6KIO/
%{_kf6_includedir}/KIO/
%{_kf6_includedir}/KIOCore/
%{_kf6_includedir}/KIOFileWidgets/
%{_kf6_includedir}/KIOGui/
%{_kf6_includedir}/KIOWidgets/
%{_kf6_libdir}/libKF6KIOCore.so
%{_kf6_libdir}/libKF6KIOFileWidgets.so
%{_kf6_libdir}/libKF6KIOGui.so
%{_kf6_libdir}/libKF6KIOWidgets.so
%{_kf6_sharedir}/kdevappwizard/templates/kioworker6.tar.bz2

%files lang -f kio.lang

%changelog
