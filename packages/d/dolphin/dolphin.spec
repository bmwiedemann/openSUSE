#
# spec file for package dolphin
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
Name:           dolphin
Version:        20.08.1
Release:        0
Summary:        KDE File Manager
License:        GPL-2.0-or-later
Group:          Productivity/File utilities
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
Source3:        dolphinsu.desktop
Patch0:         dolphin-go_up.diff
# PATCH-FIX-OPENSUSE
Patch1:         0001-Revert-Disallow-executing-Dolphin-as-root-on-Linux.patch
BuildRequires:  extra-cmake-modules >= 1.6.0
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Activities) >= 5.7.0
BuildRequires:  cmake(KF5Baloo)
BuildRequires:  cmake(KF5BalooWidgets)
BuildRequires:  cmake(KF5Bookmarks) >= 5.7.0
BuildRequires:  cmake(KF5Completion) >= 5.7.0
BuildRequires:  cmake(KF5Config) >= 5.7.0
BuildRequires:  cmake(KF5CoreAddons) >= 5.7.0
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons) >= 5.7.0
BuildRequires:  cmake(KF5DocTools) >= 5.7.0
BuildRequires:  cmake(KF5FileMetaData)
BuildRequires:  cmake(KF5I18n) >= 5.7.0
BuildRequires:  cmake(KF5IconThemes) >= 5.7.0
BuildRequires:  cmake(KF5Init) >= 5.7.0
BuildRequires:  cmake(KF5KCMUtils) >= 5.7.0
BuildRequires:  cmake(KF5KIO) >= 5.7.0
BuildRequires:  cmake(KF5NewStuff) >= 5.7.0
BuildRequires:  cmake(KF5Notifications) >= 5.7.0
BuildRequires:  cmake(KF5Parts) >= 5.7.0
BuildRequires:  cmake(KF5Solid) >= 5.7.0
BuildRequires:  cmake(KF5TextEditor) >= 5.7.0
BuildRequires:  cmake(KF5WindowSystem) >= 5.7.0
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5Concurrent) >= 5.4.0
BuildRequires:  cmake(Qt5Core) >= 5.4.0
BuildRequires:  cmake(Qt5DBus) >= 5.4.0
BuildRequires:  cmake(Qt5Gui) >= 5.4.0
BuildRequires:  cmake(Qt5Widgets) >= 5.4.0
Requires:       baloo5-kioslaves
Requires:       dolphin-part = %{version}-%{release}
Recommends:     kio-extras5
Recommends:     konsole-part
Obsoletes:      dolphin5
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
This package contains the default file manager of KDE Workspaces.

%package part
Summary:        KDE File Manager
Group:          Productivity/File utilities
%requires_ge    kio
Recommends:     %{name}-part-lang
Obsoletes:      dolphin5-part

%description part
This package contains the libraries used by Dolphin and Konqueror.

%package -n libdolphinvcs5
Summary:        KDE File Manager
Group:          Productivity/File utilities

%description -n libdolphinvcs5
This package contains the libraries used by Dolphin and Konqueror.

%package devel
Summary:        KDE File Manager
Group:          Productivity/File utilities
Requires:       libdolphinvcs5 = %{version}
Obsoletes:      dolphin5-devel < %{version}
Provides:       dolphin5-devel = %{version}

%description devel
This package contains the libraries used by Dolphin and Konqueror.

%if %{with lang}
%package -n %{name}-part-lang
Summary:        Translations for package %{name}
Group:          System/Localization
Requires:       %{name}-part = %{version}
Supplements:    (bundle-lang-other and %{name}-part)
Provides:       %{name}-lang = %{version}
Obsoletes:      %{name}-lang < %{version}
Provides:       %{name}-part-lang-all = %{version}
BuildArch:      noarch

%description -n %{name}-part-lang

Provides translations for the "%{name}" package.
%endif

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

  install -D -m 0644 %{SOURCE3} %{buildroot}%{_kf5_applicationsdir}/org.kde.dolphinsu.desktop
  %suse_update_desktop_file org.kde.dolphin          System FileManager

%post part -p /sbin/ldconfig
%postun part -p /sbin/ldconfig
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post -n libdolphinvcs5 -p /sbin/ldconfig
%postun -n libdolphinvcs5 -p /sbin/ldconfig

%files
%license COPYING*
%doc README.md
%dir %{_kf5_appstreamdir}
%dir %{_kf5_htmldir}
%dir %{_kf5_htmldir}/en
%dir %{_kf5_sharedir}/kglobalaccel/
%doc %lang(en) %{_kf5_htmldir}/en/dolphin/
%{_kf5_applicationsdir}/org.kde.dolphin.desktop
%{_kf5_applicationsdir}/org.kde.dolphinsu.desktop
%{_kf5_appstreamdir}/org.kde.dolphin.appdata.xml
%{_kf5_bindir}/dolphin
%{_kf5_bindir}/servicemenuinstaller
%{_kf5_dbusinterfacesdir}/org.freedesktop.FileManager1.xml
%{_kf5_libdir}/libkdeinit5_dolphin.so
%{_kf5_sharedir}/dbus-1/services/org.kde.dolphin.FileManager1.service
%{_kf5_sharedir}/kglobalaccel/org.kde.dolphin.desktop

%files part
%license COPYING*
%doc README.md
%dir %{_kf5_configkcfgdir}
%dir %{_kf5_plugindir}
%dir %{_kf5_servicesdir}
%dir %{_kf5_servicetypesdir}
%{_kf5_configkcfgdir}/dolphin_*.kcfg
%{_kf5_debugdir}/dolphin.categories
%{_kf5_knsrcfilesdir}/servicemenu.knsrc
%{_kf5_libdir}/libdolphinprivate.so.*
%{_kf5_plugindir}/dolphinpart.so
%{_kf5_plugindir}/kcm_dolphin*.so
%{_kf5_servicesdir}/dolphinpart.desktop
%{_kf5_servicesdir}/kcmdolphingeneral.desktop
%{_kf5_servicesdir}/kcmdolphinnavigation.desktop
%{_kf5_servicesdir}/kcmdolphinservices.desktop
%{_kf5_servicesdir}/kcmdolphinviewmodes.desktop
%{_kf5_servicetypesdir}/fileviewversioncontrolplugin.desktop

%files -n libdolphinvcs5
%license COPYING*
%doc README.md
%{_kf5_libdir}/libdolphinvcs.so.*

%files devel
%license COPYING*
%doc README.md
%{_includedir}/dolphinvcs_export.h
%{_kf5_cmakedir}/DolphinVcs/
%{_kf5_libdir}/libdolphinvcs.so
%{_kf5_prefix}/include/Dolphin/
%{_kf5_prefix}/include/dolphin_export.h

%if %{with lang}
%files part-lang -f %{name}.lang
%license COPYING*
%dir %{_kf5_sharedir}/locale/fi/LC_SCRIPTS/
%lang(fi) %{_kf5_sharedir}/locale/fi/LC_SCRIPTS/dolphin/
%endif

%changelog
