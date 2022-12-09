#
# spec file for package marble
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


%define _so -28
%define _so_astro 1
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           marble
Version:        22.12.0
Release:        0
Summary:        Generic map viewer
# License note: the tools directory contains GPL-3 tools, but they are neither built nor installed by the package
License:        LGPL-2.1-or-later
URL:            https://apps.kde.org/marble
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  gpsd-devel
BuildRequires:  kf5-filesystem
BuildRequires:  libqt5-qtlocation-devel
BuildRequires:  libshp-devel
BuildRequires:  perl
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5Runner)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Designer)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Script)
BuildRequires:  cmake(Qt5SerialPort)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
Requires:       %{name}-data = %{version}
Requires:       libastro%{_so_astro} = %{version}
Requires:       libmarblewidget-qt5%{_so} = %{version}
Requires:       marble-frontend = %{version}
Recommends:     %{name}-doc = %{version}
Obsoletes:      marble5 < %{version}
Provides:       marble5 < %{version}
%ifarch %{ix86} x86_64 %{arm} aarch64 mips mips64
# Only include WebEngine on platforms where it is available
BuildRequires:  cmake(Qt5WebEngineWidgets)
%endif

%description
Marble is a viewer of map data.

%package qt
Summary:        Qt Frontend for Marble
Requires:       %{name} = %{version}
Conflicts:      marble-frontend
Provides:       marble-frontend = %{version}

%description qt
The Qt frontend for the Marble map viewer

%package kde
Summary:        The KDE optimized frontend for Marble and several Plasmoids/Wallpapers
Requires:       %{name} = %{version}
Supplements:    (marble and plasma5-desktop)
Conflicts:      marble-frontend
Provides:       marble-frontend = %{version}

%description kde
The KDE frontend for the Marble map viewer. It also includes several plasmoids and wallpapers for Plasma

%package data
Summary:        Generic map viewer: data
Requires:       %{name} = %{version}
Obsoletes:      marble5-data < %{version}
Provides:       marble5-data < %{version}
BuildArch:      noarch

%description data
Marble is a viewer of map data. This package contains its data.

%package devel
Summary:        Generic map viewer: Build Environment
Requires:       libastro%{_so_astro} = %{version}
Requires:       libmarblewidget-qt5%{_so} = %{version}
Requires:       cmake(Qt5Widgets)
Requires:       cmake(Qt5Xml)
Obsoletes:      marble5-devel < %{version}
Provides:       marble5-devel = %{version}
%ifarch %{ix86} x86_64 %{arm} aarch64 mips mips64
Requires:       cmake(Qt5WebEngineWidgets)
%endif

%description devel
Development headers and libraries for Marble.

%package doc
Summary:        Marble documentation
Requires:       %{name} = %{version}
Obsoletes:      marble5-doc < %{version}
Provides:       marble5-doc = %{version}
BuildArch:      noarch

%description doc
Marble is a viewer of map data. This package contains its documentation.

%package -n libmarblewidget-qt5%{_so}
Summary:        Generic map viewer: Shared Library

%description -n libmarblewidget-qt5%{_so}
The shared library for the MarbleWidget shared library.

%package -n libastro%{_so_astro}
Summary:        Astronomy: Shared Library
Requires:       libmarblewidget-qt5%{_so}
Obsoletes:      libastro-qt5-%{_so_astro} < %{version}
Provides:       libastro-qt5-%{_so_astro} = %{version}

%description -n libastro%{_so_astro}
The astronomy library for the satellites plugin.

%lang_package

%prep
%autosetup -p1 -n marble-%{version}

%build
export SUSE_ASNEEDED=0
%ifarch ppc ppc64
export RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
%cmake_kf5 -d build -- -DBUILD_MARBLE_TESTS=NO -DMOBILE=OFF -DQT_PLUGINS_DIR=%{_kf5_plugindir}
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name --with-qt
%{kf5_find_htmldocs}

%fdupes %{buildroot}

%post   -n libmarblewidget-qt5%{_so} -p /sbin/ldconfig
%postun -n libmarblewidget-qt5%{_so} -p /sbin/ldconfig
%post   -n libastro%{_so_astro} -p /sbin/ldconfig
%postun -n libastro%{_so_astro} -p /sbin/ldconfig

%files
%license COPYING* LICENSE*
%doc CREDITS ChangeLog MANIFESTO.txt
%{_kf5_knsrcfilesdir}/marble.knsrc
%exclude %{_datadir}/marble/data
%dir %{_kf5_plugindir}/kf5/
%dir %{_kf5_plugindir}/kf5/krunner/
%{_kf5_applicationsdir}/marble_geo.desktop
%{_kf5_applicationsdir}/marble_geojson.desktop
%{_kf5_applicationsdir}/marble_gpx.desktop
%{_kf5_applicationsdir}/marble_kml.desktop
%{_kf5_applicationsdir}/marble_kmz.desktop
%{_kf5_applicationsdir}/marble_shp.desktop
%{_kf5_applicationsdir}/marble_worldwind.desktop
%{_kf5_appstreamdir}/org.kde.marble.appdata.xml
%{_kf5_appstreamdir}/org.kde.plasma.worldclock.appdata.xml
%{_kf5_appstreamdir}/org.kde.plasma.worldmap.appdata.xml
%{_kf5_configkcfgdir}/marble.kcfg
%{_kf5_iconsdir}/hicolor/*/apps/marble.*
%{_kf5_kxmlguidir}/marble/
%{_kf5_libdir}/libmarbledeclarative.so
%{_kf5_libdir}/marble/
%{_kf5_plugindir}/designer/
%{_kf5_plugindir}/kf5/krunner/plasma_runner_marble.so
%{_kf5_plugindir}/libmarble*so
%{_kf5_plugindir}/marblethumbnail.so
%{_kf5_qmldir}/org/kde/marble/
%{_kf5_servicesdir}/*desktop
%{_kf5_sharedir}/marble/
%{_kf5_sharedir}/mime/packages/geo.xml

%files devel
%doc BUGS CODING
%{_includedir}/astro/
%{_includedir}/marble/
%{_kf5_cmakedir}/Astro/
%{_kf5_cmakedir}/Marble/
%{_kf5_libdir}/libastro.so
%{_kf5_libdir}/libmarblewidget-qt5.so
%{_kf5_mkspecsdir}/qt_Marble.pri

%files data
%{_datadir}/marble/data

%files doc
%doc %lang(en) %{_kf5_htmldir}/en/marble/

%files -n libmarblewidget-qt5%{_so}
%{_kf5_libdir}/libmarblewidget-qt5.so.*

%files -n libastro%{_so_astro}
%{_kf5_libdir}/libastro.so.*

%files qt
%{_kf5_applicationsdir}/org.kde.marble-qt.desktop
%{_kf5_bindir}/marble-qt

%files kde
%{_kf5_applicationsdir}/org.kde.marble.desktop
%{_kf5_bindir}/marble
%dir %{_datadir}/plasma
%{_datadir}/plasma/plasmoids/
%{_datadir}/plasma/wallpapers/

%files lang -f %{name}.lang

%changelog
