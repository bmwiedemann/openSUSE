#
# spec file for package tellico
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


Name:           tellico
Version:        3.5.5
Release:        0
Summary:        A Collection Manager
License:        GPL-2.0-or-later
URL:            https://tellico-project.org/
Source0:        https://tellico-project.org/files/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM
Patch0:         0001-Remove-Allocine-data-source.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  libcsv-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Cddb)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5FileMetaData)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Sane)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5Sonnet)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Charts)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(exempi-2.0)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(poppler-qt5)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(yaz)
# Needed to install/uninstall knewstuff downloads
Requires:       /usr/bin/dbus-send
# QWebEngine is not available on ppc
%ifarch %{ix86} x86_64 %{x86_64} %{arm} aarch64
BuildRequires:  cmake(Qt5WebEngineWidgets)
%else
BuildRequires:  cmake(KF5KHtml)
%endif

%description
Tellico is an application for organizing your collections. It provides
default templates for books, bibliographies, videos, music, video games, coins,
stamps, trading cards, comic books, and wines.

%lang_package

%prep
%autosetup -p1

# E: env-script-interpreter
sed -i 's#env perl$#perl#' src/config/*-update.pl
sed -i 's#env python$#python3#' src/fetch/scripts/*.py

%build
%cmake_kf5 "-DENABLE_WEBCAM=true" -d build

%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name}

%{kf5_find_htmldocs}

%{kf5_post_install}

%fdupes %{buildroot}

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%config %{_kf5_configdir}/tellicorc
%dir %{_kf5_appsdir}/kconf_update
%doc %lang(en) %{_kf5_htmldir}/en/tellico/
%{_datadir}/mime/packages/tellico.xml
%{_kf5_applicationsdir}/org.kde.tellico.desktop
%{_kf5_appsdir}/kconf_update/tellico*
%{_kf5_appsdir}/tellico/
%{_kf5_appstreamdir}/org.kde.tellico.appdata.xml
%{_kf5_bindir}/tellico
%{_kf5_configkcfgdir}/tellico_config.kcfg
%{_kf5_iconsdir}/hicolor/*/apps/tellico.png
%{_kf5_iconsdir}/hicolor/*/mimetypes/application-x-tellico.png
%{_kf5_knsrcfilesdir}/tellico*
%{_kf5_kxmlguidir}/tellico/

%files lang -f %{name}.lang

%changelog
