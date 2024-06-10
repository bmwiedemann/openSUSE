#
# spec file for package kstars
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


%if 0%{?suse_version} && 0%{?suse_version} < 1590
%global force_gcc_version 12
%endif

# Internal QML import
%global __requires_exclude qmlimport\\((KStarsLiteEnums|TelescopeLiteEnums).*
Name:           kstars
Version:        3.7.1
Release:        0
Summary:        Desktop Planetarium
# Note for legal: the Apache licensed files in the tarball are for the
# Android version - they're neither built nor installed
# Likewise, the non-commercial files in  kstars-17.04.2/README.images are not
# used nor installed
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          Productivity/Scientific/Astronomy
URL:            https://edu.kde.org/kstars/
# For whatever reason, they aren't uploading releases anymore on DKO, so we use the one from gitlab instead.
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  Mesa-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  gcc%{?force_gcc_version}-c++ >= 12
BuildRequires:  libXISF-devel
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
BuildRequires:  pkgconfig(libindi) >= 2.0.0
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(wcslib)
Requires:       libqt5-qtquickcontrols
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
%if %{pkg_vcmp cmake(KF5DocTools) < 5.92}
rm -r po/ca/docs po/ca@valencia/docs
%endif

# remove FR docs due to https://bugs.kde.org/show_bug.cgi?id=459821
rm -r po/fr/docs

%build
%ifarch ppc ppc64
export RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
%if 0%{?force_gcc_version}
export CC="gcc-%{?force_gcc_version}"
export CXX="g++-%{?force_gcc_version}"
%endif
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

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

%files lang -f %{name}.lang
%license LICENSES/GPL-2.0-or-later.txt LICENSES/GPL-3.0-or-later.txt

%changelog
