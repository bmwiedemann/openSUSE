#
# spec file for package ark
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
Name:           ark
Version:        24.05.2
Release:        0
Summary:        KDE Archiver Tool
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/ark
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6FileMetaData) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6Pty) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(libarchive) >= 3.3.3
BuildRequires:  pkgconfig(libzip) >= 1.3.0
BuildRequires:  pkgconfig(zlib)
Recommends:     /usr/bin/lzop
Recommends:     7zip
Recommends:     lrzip
Recommends:     lzop
Recommends:     unar
Recommends:     unzip
Recommends:     xz
Recommends:     zstd
Suggests:       arj
Obsoletes:      ark-devel

%description
This is a KDE application to work with compressed archives.

%package -n libkerfuffle24
Summary:        KDE Archiver Tool

%description -n libkerfuffle24
This is a KDE application to work with compressed archives.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-man --with-html --all-name


%ldconfig_scriptlets -n libkerfuffle24

%files
%doc %lang(en) %{_kf6_htmldir}/en/ark/
%doc %{_kf6_mandir}/man1/ark.1%{?ext_man}
%{_kf6_applicationsdir}/org.kde.ark.desktop
%{_kf6_appstreamdir}/org.kde.ark.appdata.xml
%{_kf6_bindir}/ark
%{_kf6_configkcfgdir}/ark.kcfg
%{_kf6_configdir}/arkrc
%{_kf6_sharedir}/kconf_update/ark.upd
%{_kf6_sharedir}/kconf_update/ark_add_hamburgermenu_to_toolbar.sh
%{_kf6_debugdir}/ark.categories
%{_kf6_iconsdir}/hicolor/*/apps/*
%{_kf6_plugindir}/kf6/parts/arkpart.so
%{_kf6_plugindir}/kerfuffle/
%dir %{_kf6_plugindir}/kf6/kfileitemaction
%{_kf6_plugindir}/kf6/kfileitemaction/compressfileitemaction.so
%{_kf6_plugindir}/kf6/kfileitemaction/extractfileitemaction.so
%dir %{_kf6_plugindir}/kf6/kio_dnd
%{_kf6_plugindir}/kf6/kio_dnd/extracthere.so

%files -n libkerfuffle24
%{_kf6_libdir}/libkerfuffle.so.*

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/ark/

%changelog
