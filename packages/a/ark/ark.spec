#
# spec file for package ark
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


%define SOMAJOR 22
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           ark
Version:        22.12.0
Release:        0
Summary:        KDE Archiver Tool
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/ark
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch0:         0001-Support-building-against-libarchive-3.3.2-again.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  libarchive-devel
BuildRequires:  libzip-devel >= 1.2.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Pty)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(bzip2)
# Recommend the most used compression programs (bnc#872010)
Recommends:     xz
Obsoletes:      ark-devel
Recommends:     p7zip-full
Recommends:     unar

%description
This is a KDE application to work with compressed archives.

%package -n libkerfuffle%{SOMAJOR}
Summary:        KDE Archiver Tool

%description -n libkerfuffle%{SOMAJOR}
This is a KDE application to work with compressed archives.

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

%suse_update_desktop_file org.kde.ark System Archiving

%post -n libkerfuffle%{SOMAJOR} -p /sbin/ldconfig
%postun -n libkerfuffle%{SOMAJOR} -p /sbin/ldconfig

%files
%doc %lang(en) %{_kf5_htmldir}/en/ark/
%doc %{_kf5_mandir}/man1/ark.*
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/kfileitemaction
%dir %{_kf5_plugindir}/kf5/kio_dnd
%dir %{_kf5_plugindir}/kf5/parts
%{_kf5_applicationsdir}/org.kde.ark.desktop
%{_kf5_appstreamdir}/org.kde.ark.appdata.xml
%{_kf5_bindir}/ark
%{_kf5_configkcfgdir}/ark.kcfg
%{_kf5_configdir}/arkrc
%dir %{_kf5_sharedir}/kconf_update
%{_kf5_sharedir}/kconf_update/ark.upd
%{_kf5_sharedir}/kconf_update/ark_add_hamburgermenu_to_toolbar.sh
%{_kf5_debugdir}/ark.categories
%{_kf5_iconsdir}/hicolor/*/apps/*
%{_kf5_plugindir}/kf5/parts/arkpart.so
%{_kf5_plugindir}/kerfuffle/
%{_kf5_plugindir}/kf5/kfileitemaction/compressfileitemaction.so
%{_kf5_plugindir}/kf5/kfileitemaction/extractfileitemaction.so
%{_kf5_plugindir}/kf5/kio_dnd/extracthere.so

%files -n libkerfuffle%{SOMAJOR}
%license COPYING*
%{_kf5_libdir}/libkerfuffle.so.%{SOMAJOR}
%{_kf5_libdir}/libkerfuffle.so.*

%files lang -f %{name}.lang

%changelog
