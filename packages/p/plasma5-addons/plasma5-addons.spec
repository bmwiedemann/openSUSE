#
# spec file for package plasma5-addons
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


%bcond_without lang
Name:           plasma5-addons
Version:        5.20.0
Release:        0
# Full Plasma 5 version (e.g. 5.8.95)
%{!?_plasma5_bugfix: %define _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.8.95 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        Additional Plasma5 Widgets
License:        LGPL-2.1-only AND GPL-2.0-or-later AND GPL-3.0-only
Group:          System/GUI/KDE
URL:            http://www.kde.org/
Source:         kdeplasma-addons-%{version}.tar.xz
%if %{with lang}
Source1:        kdeplasma-addons-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Activities) >= 5.25.0
BuildRequires:  cmake(KF5Config) >= 5.25.0
BuildRequires:  cmake(KF5ConfigWidgets) >= 5.25.0
BuildRequires:  cmake(KF5CoreAddons) >= 5.25.0
BuildRequires:  cmake(KF5Declarative) >= 5.25.0
BuildRequires:  cmake(KF5Holidays) >= 5.25.0
BuildRequires:  cmake(KF5I18n) >= 5.25.0
BuildRequires:  cmake(KF5KCMUtils) >= 5.25.0
BuildRequires:  cmake(KF5KDELibs4Support) >= 5.25.0
BuildRequires:  cmake(KF5KIO) >= 5.25.0
BuildRequires:  cmake(KF5Kross) >= 5.25.0
BuildRequires:  cmake(KF5NewStuff) >= 5.25.0
BuildRequires:  cmake(KF5Plasma) >= 5.25.0
BuildRequires:  cmake(KF5Runner) >= 5.25.0
BuildRequires:  cmake(KF5Service) >= 5.25.0
BuildRequires:  cmake(KF5UnitConversion) >= 5.25.0
#!BuildIgnore: kwin5
BuildRequires:  cmake(LibTaskManager) >= %{_plasma5_version}
%if 0%{?suse_version} > 1314 && "%{suse_version}" != "1320"
BuildRequires:  cmake(KDEExperimentalPurpose)
%endif
BuildRequires:  xz
BuildRequires:  cmake(Qt5Core) >= 5.4.0
BuildRequires:  cmake(Qt5DBus) >= 5.4.0
BuildRequires:  cmake(Qt5Gui) >= 5.4.0
BuildRequires:  cmake(Qt5Qml) >= 5.4.0
BuildRequires:  cmake(Qt5Quick) >= 5.4.0
BuildRequires:  cmake(Qt5WebEngine) >= 5.7.0
BuildRequires:  cmake(Qt5Widgets) >= 5.4.0
BuildRequires:  cmake(Qt5X11Extras) >= 5.4.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
Requires:       purpose
Recommends:     %{name}-lang
%if 0%{?suse_version} > 1314 && "%{suse_version}" != "1320"
Provides:       plasma-addons = %{version}
Obsoletes:      plasma-addons < %{version}
%else
Conflicts:      plasma-addons
%endif

%description
Additional plasmoids from upstream for use on the Plasma workspace.

%lang_package

%package devel
Summary:        Additional plasmoid widgets - development files
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}

%description devel
This package contains development files to develop additional widgets for 
the Plasma desktop.

%prep
%setup -q -n kdeplasma-addons-%{version}

%build
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
  %cmake_build

%install
  %kf5_makeinstall -C build
%if %{with lang}
  %kf5_find_lang
%endif

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING*
%{_kf5_knsrcfilesdir}/comic.knsrc
%{_kf5_libdir}/libplasmacomicprovidercore.so.*
%{_libdir}/libplasmapotdprovidercore.so*
%{_kf5_servicetypesdir}/
%{_kf5_plugindir}/
%{_kf5_qmldir}/
%{_kf5_servicesdir}/
%{_kf5_plasmadir}/
%{_kf5_sharedir}/kwin/
%{_kf5_iconsdir}/hicolor/*/*/*.*
%{_kf5_appstreamdir}/

%files devel
%license COPYING*
%dir %{_includedir}/plasma
%dir %{_includedir}/plasma/potdprovider
%{_includedir}/plasma/potdprovider/plasma_potd_export.h
%{_includedir}/plasma/potdprovider/potdprovider.h
%dir %{_kf5_cmakedir}/PlasmaPotdProvider/
%{_kf5_cmakedir}/PlasmaPotdProvider/PlasmaPotdProviderConfig.cmake
%{_kf5_cmakedir}/PlasmaPotdProvider/PlasmaPotdProviderConfigVersion.cmake
%{_kf5_cmakedir}/PlasmaPotdProvider/PlasmaPotdProviderTargets-none.cmake
%{_kf5_cmakedir}/PlasmaPotdProvider/PlasmaPotdProviderTargets.cmake
%dir %{_kf5_sharedir}/kdevappwizard
%dir %{_kf5_sharedir}/kdevappwizard/templates/
%{_kf5_sharedir}/kdevappwizard/templates/plasmapotdprovider.tar.bz2

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
