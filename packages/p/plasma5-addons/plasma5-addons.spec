#
# spec file for package plasma5-addons
#
# Copyright (c) 2023 SUSE LLC
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


%bcond_without released
Name:           plasma5-addons
Version:        5.26.5
Release:        0
# Full Plasma 5 version (e.g. 5.8.95)
%{!?_plasma5_bugfix: %define _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.8.95 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        Additional Plasma5 Widgets
License:        GPL-2.0-or-later AND LGPL-2.1-only AND GPL-3.0-only
Group:          System/GUI/KDE
URL:            http://www.kde.org/
Source:         https://download.kde.org/stable/plasma/%{version}/kdeplasma-addons-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/kdeplasma-addons-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  kf5-filesystem
BuildRequires:  libicu-devel
BuildRequires:  cmake(KF5Activities) >= 5.98.0
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5Holidays)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Kross)
BuildRequires:  cmake(KF5NetworkManagerQt)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5Purpose)
BuildRequires:  cmake(KF5Runner)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5UnitConversion)
#!BuildIgnore: kwin5
BuildRequires:  xz
BuildRequires:  cmake(LibTaskManager) >= %{_plasma5_version}
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
%ifnarch ppc ppc64 ppc64le s390 s390x riscv64
BuildRequires:  cmake(Qt5WebEngine)
%endif
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
%if 0%{?suse_version} < 1550
BuildRequires:  gcc10-PIE
BuildRequires:  gcc10-c++
%endif
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
%if 0%{?suse_version} < 1550
  export CXX=g++-10
%endif
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
  %cmake_build

%install
  %kf5_makeinstall -C build
%if %{with released}
  %kf5_find_lang
%endif

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENSES/*
%{_kf5_knsrcfilesdir}/comic.knsrc
%{_kf5_libdir}/libplasmapotdprovidercore.so.*
%{_kf5_plugindir}/
%{_kf5_qmldir}/
%{_kf5_plasmadir}/
%{_kf5_sharedir}/kwin/
%{_kf5_iconsdir}/hicolor/*/*/*.*
%{_kf5_appstreamdir}/
%{_kf5_debugdir}/plasma_comic.categories
%{_kf5_servicetypesdir}/plasma-comic.desktop

%files devel
%license LICENSES/*
%dir %{_includedir}/plasma
%dir %{_kf5_sharedir}/kdevappwizard/
%dir %{_kf5_sharedir}/kdevappwizard/templates
%{_includedir}/plasma/potdprovider
%{_kf5_cmakedir}/PlasmaPotdProvider/
%{_kf5_libdir}/libplasmapotdprovidercore.so
%{_kf5_sharedir}/kdevappwizard/templates/plasmapotdprovider.tar.bz2

%if %{with released}
%files lang -f %{name}.lang
%license LICENSES/*
%endif

%changelog
