#
# spec file for package marble
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


%define _so -28
%define _so_astro 1

%define kf6_version 6.6.0
%define qt6_version 6.6.0

%ifarch x86_64 aarch64 riscv64
%define with_webengine 1
%endif

%bcond_without released
Name:           marble
Version:        24.12.0
Release:        0
Summary:        Generic map viewer
# License note: the tools directory contains GPL-3 tools, but they are neither built nor installed by the package
License:        LGPL-2.1-or-later
URL:            https://apps.kde.org/marble
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6Runner) >= %{kf6_version}
BuildRequires:  cmake(Phonon4Qt6)
BuildRequires:  cmake(Plasma) >= 6.0.0
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Designer) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Positioning) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6SerialPort) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6SvgWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebChannel) >= %{qt6_version}
%if 0%{?with_webengine}
# Only include WebEngine on platforms where it is available
BuildRequires:  cmake(Qt6WebEngineQuick) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
%endif
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  cmake(absl)
BuildRequires:  pkgconfig(libgps)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(Qgpsmm)
BuildRequires:  pkgconfig(shapelib)
BuildRequires:  pkgconfig(zlib)
Requires:       libastro%{_so_astro} = %{version}
Requires:       libmarblewidget-qt6%{_so} = %{version}
Requires:       marble-data = %{version}
Requires:       marble-frontend = %{version}
Recommends:     marble-doc = %{version}
Obsoletes:      marble5 < %{version}
Provides:       marble5 < %{version}

%description
Marble is a viewer of map data.

%package qt
Summary:        Qt Frontend for Marble
Requires:       marble = %{version}
Conflicts:      marble-frontend
Provides:       marble-frontend = %{version}

%description qt
The Qt frontend for the Marble map viewer

%package kde
Summary:        The KDE optimized frontend for Marble and several Plasmoids/Wallpapers
Requires:       marble = %{version}
Supplements:    (marble and plasma6-desktop)
Conflicts:      marble-frontend
Provides:       marble-frontend = %{version}

%description kde
The KDE frontend for the Marble map viewer. It also includes several plasmoids and wallpapers for Plasma

%package data
Summary:        Generic map viewer: data
Requires:       marble = %{version}
Obsoletes:      marble5-data < %{version}
Provides:       marble5-data < %{version}
BuildArch:      noarch

%description data
Marble is a viewer of map data. This package contains its data.

%package devel
Summary:        Generic map viewer: Build Environment
Requires:       libastro%{_so_astro} = %{version}
Requires:       libmarblewidget-qt6%{_so} = %{version}
Requires:       cmake(Qt6Core5Compat) >= %{qt6_version}
%if 0%{?with_webengine}
Requires:       cmake(Qt6WebEngineWidgets) >= %{qt6_version}
%endif
Requires:       cmake(Qt6Widgets) >= %{qt6_version}
Requires:       cmake(Qt6Xml) >= %{qt6_version}
Obsoletes:      marble5-devel < %{version}
Provides:       marble5-devel = %{version}

%description devel
Development headers and libraries for Marble.

%package doc
Summary:        Marble documentation
Requires:       marble = %{version}
Obsoletes:      marble5-doc < %{version}
Provides:       marble5-doc = %{version}
BuildArch:      noarch

%description doc
Marble is a viewer of map data. This package contains its documentation.

%package -n libmarblewidget-qt6%{_so}
Summary:        Generic map viewer: Shared Library

%description -n libmarblewidget-qt6%{_so}
The shared library for the MarbleWidget shared library.

%package -n libastro%{_so_astro}
Summary:        Astronomy: Shared Library
Requires:       libmarblewidget-qt6%{_so}
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

%cmake_kf6 \
  -DMOBILE:BOOL=FALSE \
  -DQT_PLUGINS_DIR:STRING=%{_kf6_plugindir} \
  -DBUILD_QT_AND_KDE:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name --with-qt

%fdupes %{buildroot}

%ldconfig_scriptlets -n libmarblewidget-qt6%{_so}
%ldconfig_scriptlets -n libastro%{_so_astro}

%files
%license COPYING* LICENSE*
%doc CREDITS ChangeLog MANIFESTO.txt
%{_kf6_applicationsdir}/marble_geo.desktop
%{_kf6_applicationsdir}/marble_geojson.desktop
%{_kf6_applicationsdir}/marble_gpx.desktop
%{_kf6_applicationsdir}/marble_kml.desktop
%{_kf6_applicationsdir}/marble_kmz.desktop
%{_kf6_applicationsdir}/marble_shp.desktop
%{_kf6_applicationsdir}/marble_worldwind.desktop
%{_kf6_appstreamdir}/org.kde.marble.appdata.xml
%{_kf6_appstreamdir}/org.kde.marble.behaim.appdata.xml
%{_kf6_appstreamdir}/org.kde.marble.maps.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.worldclock.appdata.xml
%{_kf6_appstreamdir}/org.kde.plasma.worldmap.appdata.xml
%{_kf6_configkcfgdir}/marble.kcfg
%{_kf6_debugdir}/marble.categories
%{_kf6_iconsdir}/hicolor/*/apps/marble.*
%{_kf6_iconsdir}/hicolor/scalable/apps/org.kde.marble.{behaim,maps}.svg
%{_kf6_kxmlguidir}/marble/
%{_kf6_libdir}/marble/
%{_kf6_plugindir}/designer/
%dir %{_kf6_plugindir}/kf6/krunner/
%{_kf6_plugindir}/kf6/krunner/plasma_runner_marble.so
%{_kf6_plugindir}/libmarble_part.so
%{_kf6_plugindir}/marblethumbnail.so
%{_kf6_qmldir}/org/kde/marble/
%{_kf6_sharedir}/mime/packages/geo.xml

%files devel
%doc BUGS CODING
%{_includedir}/astro/
%{_includedir}/marble/
%{_kf6_cmakedir}/Astro/
%{_kf6_cmakedir}/Marble/
%{_kf6_libdir}/libastro.so
%{_kf6_libdir}/libmarblewidget-qt6.so
%{_kf6_mkspecsdir}/qt_Marble.pri

%files data
%dir %{_kf6_sharedir}/marble
%{_kf6_sharedir}/marble/data/

%files doc
%doc %lang(en) %{_kf6_htmldir}/en/marble/

%files -n libmarblewidget-qt6%{_so}
%{_kf6_libdir}/libmarblewidget-qt6.so.*

%files -n libastro%{_so_astro}
%{_kf6_libdir}/libastro.so.*

%files qt
%{_kf6_applicationsdir}/org.kde.marble-qt.desktop
%{_kf6_bindir}/marble-qt

%files kde
%{_kf6_applicationsdir}/marble_thumbnail_kml.desktop
%{_kf6_applicationsdir}/marble_thumbnail_kmz.desktop
%{_kf6_applicationsdir}/marble_thumbnail_osm.desktop
%{_kf6_applicationsdir}/marble_thumbnail_shp.desktop
%{_kf6_applicationsdir}/org.kde.marble.behaim.desktop
%{_kf6_applicationsdir}/org.kde.marble.desktop
%{_kf6_applicationsdir}/org.kde.marble.maps.desktop
%{_kf6_bindir}/marble
%{_kf6_bindir}/marble-behaim
%{_kf6_bindir}/marble-maps
%{_kf6_plasmadir}/plasmoids/org.kde.plasma.worldclock
%{_kf6_plasmadir}/wallpapers/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/marble/

%changelog
