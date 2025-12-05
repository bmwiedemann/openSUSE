#
# spec file for package kstars
#
# Copyright (c) 2025 SUSE LLC and contributors
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
# Internal QML import
%global __requires_exclude qmlimport\\((KStarsLiteEnums|TelescopeLiteEnums).*
Name:           kstars
Version:        3.8.0
Release:        0
Summary:        Desktop Planetarium
# Note for legal: the Apache licensed files in the tarball are for the
# Android version - they're neither built nor installed
# Likewise, the non-commercial files in  kstars-17.04.2/README.images are not
# used nor installed
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          Productivity/Scientific/Astronomy
URL:            https://kstars.kde.org
Source0:        https://download.kde.org/stable/kstars/%{version}/kstars-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/kstars/%{version}/kstars-%{version}.tar.xz.sig
# https://invent.kde.org/sysadmin/release-keyring/-/blob/master/keys/mutlaqja@key1.asc?ref_type=heads
Source2:        kstars.keyring
%endif
Patch0:         fix-eigen3-max.patch
Patch1:         fix-build-gcc15.patch
BuildRequires:  Mesa-devel
BuildRequires:  curl-devel
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  libXISF-devel
BuildRequires:  libnova-devel
BuildRequires:  pkgconfig
BuildRequires:  xplanet
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6Plotting)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6DataVisualization)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6WebSockets)
BuildRequires:  cmake(Qt6Xml)
# the library was renamed in 2.7, better require (at least) this version
BuildRequires:  cmake(StellarSolver) >= 2.7
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(libindi) >= 2.0.0
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(wcslib)
Requires:       qt6-declarative-imports
Requires:       qt6-positioning-imports
Requires:       qt6-sql-sqlite
Recommends:     /usr/bin/dbus-send
%if 0%{?suse_version} > 1500
Recommends:     indi
%else
Recommends:     libindi
%endif
Recommends:     xplanet

%description
KStars is astronomy software. It provides an accurate graphical
simulation of the night sky, for any time and location on Earth.

%lang_package

%prep
%autosetup -p1
# remove Catalan docs due to https://invent.kde.org/education/kstars/-/issues/186
%if %{pkg_vcmp cmake(KF6DocTools) < 5.92}
rm -r po/ca/docs po/ca@valencia/docs
%endif

%build
%cmake_kf6 \
  -DBUILD_WITH_QT6:BOOL=TRUE \
  -DBUILD_QT5:BOOL=FALSE

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-man --all-name --with-html

# Remove static library
rm %{buildroot}%{_kf6_libdir}/libhtmesh.a

%fdupes %{buildroot}

%files
%license LICENSES/GPL-2.0-or-later.txt LICENSES/GPL-3.0-or-later.txt
%doc AUTHORS ChangeLog README.md README.customize README.ephemerides README.images
%{_datadir}/sounds/*.ogg
%{_kf6_applicationsdir}/org.kde.kstars.desktop
%{_kf6_appsdir}/kstars/
%{_kf6_appstreamdir}/org.kde.kstars.appdata.xml
%{_kf6_bindir}/kstars
%{_kf6_configkcfgdir}/kstars.kcfg
%{_kf6_iconsdir}/hicolor/*/*/*
%{_kf6_notificationsdir}/kstars.notifyrc

%files lang -f %{name}.lang
%license LICENSES/GPL-2.0-or-later.txt LICENSES/GPL-3.0-or-later.txt

%changelog
