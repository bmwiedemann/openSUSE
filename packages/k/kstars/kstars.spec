#
# spec file for package kstars
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


# Internal QML import
%global __requires_exclude qmlimport\\((KStarsLiteEnums|TelescopeLiteEnums).*
%bcond_without lang
Name:           kstars
Version:        3.6.2
Release:        0
Summary:        Desktop Planetarium
# Note for legal: the Apache licensed files in the tarball are for the
# Android version - they're neither built nor installed
# Likewise, the non-commercial files in  kstars-17.04.2/README.images are not
# used nor installed
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          Productivity/Scientific/Astronomy
URL:            https://edu.kde.org/kstars/
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
BuildRequires:  Mesa-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  libnova-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xplanet
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5Plotting)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5DataVisualization)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5WebSockets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(StellarSolver) >= 2.2
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(libindi) >= 1.9.9
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(wcslib)
Requires:       libqt5-qtquickcontrols
Recommends:     /usr/bin/dbus-send
Recommends:     libindi
Recommends:     xplanet

%description
KStars is astronomy software. It provides an accurate graphical
simulation of the night sky, for any time and location on Earth.

%lang_package

%prep
%autosetup -p1
# remove Catalan docs due to https://invent.kde.org/education/kstars/-/issues/186
%if %{pkg_vcmp cmake(KF5DocTools) < 5.92}
rm -r po/ca/docs po/ca@valencia/docs
%endif

# remove FR docs due to https://bugs.kde.org/show_bug.cgi?id=459821
rm -r po/fr/docs

%build
%ifarch ppc ppc64
export RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %{kf5_find_htmldocs}
%endif

# Remove static library
rm %{buildroot}%{_kf5_libdir}/libhtmesh.a

%fdupes -s %{buildroot}

%files
%license LICENSES/GPL-2.0-or-later.txt LICENSES/GPL-3.0-or-later.txt
%doc AUTHORS ChangeLog README.md README.customize README.ephemerides README.images
%doc %{_kf5_htmldir}/en/kstars/
%{_datadir}/sounds/*.ogg
%{_kf5_applicationsdir}/org.kde.kstars.desktop
%{_kf5_appsdir}/kstars/
%{_kf5_appstreamdir}/org.kde.kstars.appdata.xml
%{_kf5_bindir}/kstars
%{_kf5_configkcfgdir}/kstars.kcfg
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_notifydir}/kstars.notifyrc

%if %{with lang}
%files lang -f %{name}.lang
%license LICENSES/GPL-2.0-or-later.txt LICENSES/GPL-3.0-or-later.txt
%endif

%changelog
