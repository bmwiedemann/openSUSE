#
# spec file for package palapeli
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
Name:           palapeli
Version:        22.12.1
Release:        0
Summary:        Jigsaw puzzle game
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/palapeli
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  shared-mime-info
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KDEGames)
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
Requires:       palapeli-data = %{version}

%description
Palapeli is a jigsaw puzzle game. Unlike other games in that genre, you are not
limited to aligning pieces on imaginary grids. The pieces are freely moveable.
Also, Palapeli features real persistency, i.e. everything you do is saved on
your disk immediately.

%package data
Summary:        Palapeli's standard puzzle files
Requires:       palapeli = %{version}
BuildArch:      noarch

%description data
This package contains the standard puzzle files for Palapeli.

%package devel
Summary:        Development package for Palapeli
Requires:       palapeli = %{version}

%description devel
This package contains the development files for Palapeli.

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

%suse_update_desktop_file -r org.kde.palapeli Game BoardGame

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES/*
%doc %lang(en) %{_kf5_htmldir}/en/palapeli/
%dir %{_kf5_iconsdir}/hicolor/128x128/
%dir %{_kf5_iconsdir}/hicolor/128x128/apps
%dir %{_kf5_iconsdir}/hicolor/128x128/mimetypes/
%dir %{_kf5_iconsdir}/hicolor/16x16
%dir %{_kf5_iconsdir}/hicolor/16x16/apps
%dir %{_kf5_iconsdir}/hicolor/16x16/mimetypes
%dir %{_kf5_iconsdir}/hicolor/24x24
%dir %{_kf5_iconsdir}/hicolor/24x24/apps
%dir %{_kf5_iconsdir}/hicolor/24x24/mimetypes
%dir %{_kf5_iconsdir}/hicolor/32x32
%dir %{_kf5_iconsdir}/hicolor/32x32/apps
%dir %{_kf5_iconsdir}/hicolor/32x32/mimetypes
%dir %{_kf5_iconsdir}/hicolor/64x64
%dir %{_kf5_iconsdir}/hicolor/64x64/apps
%dir %{_kf5_iconsdir}/hicolor/64x64/mimetypes
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/thumbcreator
%dir %{_kf5_sharedir}/kio
%dir %{_kf5_sharedir}/kio/servicemenus
%{_kf5_applicationsdir}/org.kde.palapeli.desktop
%{_kf5_appstreamdir}/org.kde.palapeli.appdata.xml
%{_kf5_bindir}/palapeli
%{_kf5_debugdir}/palapeli.categories
%{_kf5_iconsdir}/hicolor/*/apps/palapeli.png
%{_kf5_iconsdir}/hicolor/*/mimetypes/application-x-palapeli.png
%{_kf5_libdir}/libpala.so.*
%{_kf5_notifydir}/palapeli.notifyrc
%{_kf5_plugindir}/pala*
%{_kf5_sharedir}/mime/packages/palapeli-mimetypes.xml
%{_kf5_plugindir}/kf5/thumbcreator/palathumbcreator.so
%{_kf5_sharedir}/kio/servicemenus/palapeli_servicemenu.desktop

%files data
%{_kf5_appsdir}/palapeli/
%config %{_kf5_configdir}/palapeli-collectionrc

%files devel
%{_includedir}/Pala
%{_kf5_libdir}/libpala.so
%{_kf5_cmakedir}/Pala/

%files lang -f %{name}.lang

%changelog
