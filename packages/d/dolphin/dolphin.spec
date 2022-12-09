#
# spec file for package dolphin
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
Name:           dolphin
Version:        22.12.0
Release:        0
Summary:        KDE File Manager
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/dolphin
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Source3:        dolphinsu.desktop
Patch0:         dolphin-go_up.diff
# PATCH-FIX-OPENSUSE
Patch1:         0001-Revert-Disallow-executing-Dolphin-as-root-on-Linux.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  systemd-rpm-macros
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Activities)
BuildRequires:  cmake(KF5Baloo)
BuildRequires:  cmake(KF5BalooWidgets)
BuildRequires:  cmake(KF5Bookmarks)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5FileMetaData)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
Requires:       baloo5-kioslaves
Requires:       dolphin-part = %{version}-%{release}
Recommends:     kio-extras5
Recommends:     konsole-part
Obsoletes:      dolphin5

%description
This package contains the default file manager of KDE Workspaces.

%package part
Summary:        KDE File Manager
%requires_ge    kio
Obsoletes:      dolphin5-part

%description part
This package contains the libraries used by Dolphin and Konqueror.

%package -n libdolphinvcs5
Summary:        KDE File Manager

%description -n libdolphinvcs5
This package contains the libraries used by Dolphin and Konqueror.

%package devel
Summary:        KDE File Manager
Requires:       libdolphinvcs5 = %{version}
Obsoletes:      dolphin5-devel < %{version}
Provides:       dolphin5-devel = %{version}

%description devel
This package contains the libraries used by Dolphin and Konqueror.

%package -n %{name}-part-lang
Summary:        Translations for package %{name}
Requires:       %{name}-part = %{version}
Supplements:    (bundle-lang-other and %{name}-part)
Provides:       %{name}-lang = %{version}
Obsoletes:      %{name}-lang < %{version}
Provides:       %{name}-part-lang-all = %{version}
BuildArch:      noarch

%description -n %{name}-part-lang
Provides translations for the "%{name}" package.

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

install -D -m 0644 %{SOURCE3} %{buildroot}%{_kf5_applicationsdir}/org.kde.dolphinsu.desktop
%suse_update_desktop_file org.kde.dolphin System FileManager

%post -n libdolphinvcs5 -p /sbin/ldconfig
%post -p /sbin/ldconfig
%post part -p /sbin/ldconfig
%postun -n libdolphinvcs5 -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%postun part -p /sbin/ldconfig

%files
%license COPYING*
%doc README.md
%doc %lang(en) %{_kf5_htmldir}/en/dolphin/
%dir %{_kf5_sharedir}/kglobalaccel/
%{_kf5_applicationsdir}/org.kde.dolphin.desktop
%{_kf5_applicationsdir}/org.kde.dolphinsu.desktop
%{_kf5_appstreamdir}/org.kde.dolphin.appdata.xml
%{_kf5_bindir}/dolphin
%{_kf5_bindir}/servicemenuinstaller
%{_kf5_dbusinterfacesdir}/org.freedesktop.FileManager1.xml
%{_kf5_sharedir}/dbus-1/services/org.kde.dolphin.FileManager1.service
%{_kf5_sharedir}/kglobalaccel/org.kde.dolphin.desktop
%dir %{_kf5_sharedir}/kconf_update
%{_kf5_sharedir}/kconf_update/dolphin_detailsmodesettings.upd
%{_userunitdir}/plasma-dolphin.service

%files part
%{_kf5_configkcfgdir}/dolphin_*.kcfg
%{_kf5_debugdir}/dolphin.categories
%{_kf5_knsrcfilesdir}/servicemenu.knsrc
%{_kf5_libdir}/libdolphinprivate.so.*
%dir %{_kf5_plugindir}/dolphin
%dir %{_kf5_plugindir}/dolphin/kcms
%{_kf5_plugindir}/dolphin/kcms/kcm_dolphin*.so
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/parts
%{_kf5_plugindir}/kf5/parts/dolphinpart.so
%dir %{_kf5_sharedir}/dolphin
%{_kf5_sharedir}/dolphin/dolphinpartactions.desktop

%files -n libdolphinvcs5
%{_kf5_libdir}/libdolphinvcs.so.*

%files devel
%{_includedir}/dolphinvcs_export.h
%{_kf5_cmakedir}/DolphinVcs/
%{_kf5_libdir}/libdolphinvcs.so
%{_kf5_prefix}/include/Dolphin/
%{_kf5_prefix}/include/dolphin_export.h

%files part-lang -f %{name}.lang
# Not detected by find-lang.sh
%dir %{_kf5_sharedir}/locale/fi/LC_SCRIPTS/
%lang(fi) %{_kf5_sharedir}/locale/fi/LC_SCRIPTS/dolphin/

%changelog
