#
# spec file for package ark
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


%define SOMAJOR 21
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           ark
Version:        21.04.0
Release:        0
Summary:        KDE Archiver Tool
License:        GPL-2.0-or-later
Group:          Productivity/Other
URL:            https://apps.kde.org/ark
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
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
# unrar is non-free. Avoid installing it automatically.
Suggests:       unrar
Obsoletes:      ark-devel
%if 0%{?suse_version} > 1500
Recommends:     p7zip-full
%else
Recommends:     p7zip
%endif
Recommends:     %{name}-lang

%description
This is a KDE application to work with compressed archives.

%package -n libkerfuffle%{SOMAJOR}
Summary:        KDE Archiver Tool
Group:          System/Libraries

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
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif
  %suse_update_desktop_file org.kde.ark System Archiving

%post -n libkerfuffle%{SOMAJOR} -p /sbin/ldconfig
%postun -n libkerfuffle%{SOMAJOR} -p /sbin/ldconfig

%files
%license COPYING*
%doc %lang(en) %{_kf5_htmldir}/en/ark/
%doc %{_kf5_mandir}/man1/ark.*
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/kfileitemaction
%dir %{_kf5_plugindir}/kf5/kio_dnd
%{_kf5_applicationsdir}/org.kde.ark.desktop
%{_kf5_appstreamdir}/org.kde.ark.appdata.xml
%{_kf5_bindir}/ark
%{_kf5_configkcfgdir}/ark.kcfg
%{_kf5_debugdir}/ark.categories
%{_kf5_iconsdir}/hicolor/*/apps/*
%{_kf5_plugindir}/arkpart.so
%{_kf5_plugindir}/kerfuffle/
%{_kf5_plugindir}/kf5/kfileitemaction/compressfileitemaction.so
%{_kf5_plugindir}/kf5/kfileitemaction/extractfileitemaction.so
%{_kf5_plugindir}/kf5/kio_dnd/extracthere.so
%{_kf5_servicesdir}/ark_part.desktop
%{_kf5_servicetypesdir}/kerfufflePlugin.desktop

%files -n libkerfuffle%{SOMAJOR}
%license COPYING*
%{_kf5_libdir}/libkerfuffle.so.*

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
