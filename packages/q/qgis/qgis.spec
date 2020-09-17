#
# spec file for package qgis
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


%bcond_without grass
Name:           qgis
Version:        3.14.16
Release:        0
Summary:        A Geographic Information System (GIS)
License:        GPL-2.0-only
Group:          Productivity/Graphics/Visualization/Other
URL:            https://qgis.org/
Source:         https://qgis.org/downloads/%{name}-%{version}.tar.bz2
Source1:        https://qgis.org/downloads/%{name}-%{version}.tar.bz2.sha256
Source2:        %{name}.rpmlintrc
Source3:        qgis_sample_data.zip
BuildRequires:  FastCGI-devel
BuildRequires:  bison >= 2.4
BuildRequires:  cmake >= 3.0.0
BuildRequires:  fdupes
BuildRequires:  filesystem
BuildRequires:  flex >= 2.5.6
BuildRequires:  geos-devel >= 3.4
BuildRequires:  libQt5Sql-private-headers-devel
BuildRequires:  libQt5Sql5-mysql
BuildRequires:  libQt5Sql5-postgresql
# Add the 3 main db we should access
# also have them in requires
BuildRequires:  libQt5Sql5-sqlite
BuildRequires:  libexiv2-devel
BuildRequires:  libqscintilla_qt5-devel
BuildRequires:  libspatialindex-devel
BuildRequires:  ocl-icd-devel
BuildRequires:  opencl-cpp-headers
BuildRequires:  pkgconfig
BuildRequires:  poppler-tools
BuildRequires:  protobuf-devel
BuildRequires:  python-qscintilla-qt5-sip
BuildRequires:  python3-GDAL
BuildRequires:  python3-Jinja2
BuildRequires:  python3-OWSLib
BuildRequires:  python3-PyYAML
BuildRequires:  python3-future
BuildRequires:  python3-psycopg2
BuildRequires:  python3-pygments
BuildRequires:  python3-qscintilla-qt5
BuildRequires:  python3-qt5-devel
BuildRequires:  python3-sip-devel > 4.12
BuildRequires:  python3-six
BuildRequires:  python3-termcolor
BuildRequires:  qtkeychain-qt5-devel >= 0.5
BuildRequires:  qwt6-devel
BuildRequires:  sqlite-devel >= 3.0
BuildRequires:  txt2tags
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt53DAnimation)
BuildRequires:  pkgconfig(Qt53DCore)
BuildRequires:  pkgconfig(Qt53DExtras)
BuildRequires:  pkgconfig(Qt53DInput)
BuildRequires:  pkgconfig(Qt53DLogic)
BuildRequires:  pkgconfig(Qt53DQuick)
BuildRequires:  pkgconfig(Qt53DQuickAnimation)
BuildRequires:  pkgconfig(Qt53DQuickExtras)
BuildRequires:  pkgconfig(Qt53DQuickInput)
BuildRequires:  pkgconfig(Qt53DQuickRender)
BuildRequires:  pkgconfig(Qt53DQuickScene2D)
BuildRequires:  pkgconfig(Qt53DRender)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Location)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Positioning)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Qwt6)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5Sensors)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
BuildRequires:  pkgconfig(expat) >= 1.95
# Requires at least gdal 3.1 for GeoTIFF and Proj >= 6 - https://github.com/qgis/QGIS/issues/36699#issuecomment-633539864
BuildRequires:  pkgconfig(gdal) >= 3.1
BuildRequires:  pkgconfig(gsl) >= 1.8
BuildRequires:  pkgconfig(libpq) > 9.4
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(proj) >= 6.3.1
BuildRequires:  pkgconfig(python3) >= 3.4
BuildRequires:  pkgconfig(qca2-qt5)
BuildRequires:  pkgconfig(spatialite) >= 4.2.0
# Force requires of those 3 main component.
Requires:       libQt5Sql5-mysql
Requires:       libQt5Sql5-postgresql
Requires:       libQt5Sql5-sqlite
# proj.db is required
Requires:       proj
Requires:       python3-GDAL
Requires:       python3-Jinja2
Requires:       python3-OWSLib
Requires:       python3-PyYAML
Requires:       python3-Pygments
Requires:       python3-future
Requires:       python3-psycopg2
# Those are not picked by obs
Requires:       python3-qscintilla-qt5
Requires:       python3-sip > 4.12
Requires:       python3-six
Requires:       python3-termcolor
Recommends:     %{name}-sample-data
Recommends:     apache2-mod_fcgid
Recommends:     gpsbabel
Conflicts:      qgis-ltr
Conflicts:      qgis-master
Obsoletes:      qgis2
%if %{with grass}
BuildRequires:  grass-devel >= 7.2
%endif
%ifarch ppc64le
BuildRequires:  memory-constraints
%endif

%package devel
Summary:        Development Libraries for QGIS
Group:          Development/Libraries/C and C++
Requires:       python3-qt5-devel
Requires:       qgis = %{version}
%if %{with grass}
%package plugin-grass
Summary:        GRASS Support Libraries for QGIS
Group:          Productivity/Graphics/Visualization/Other
Requires:       grass > 7.0
Requires:       grass-doc
Requires:       qgis = %{version}
Obsoletes:      qgis-plugin-grass < %{version}

%description plugin-grass
GRASS plugin for QGIS required to interface with GRASS system.
%endif

%package sample-data
%define sampledir sample-data
Summary:        QGIS sample data
Group:          Productivity/Graphics/Visualization/Other
BuildArch:      noarch

%description
QGIS is a Geographic Information System (GIS). QGIS supports vector,
raster, OWS and database formats. QGIS can be used to browse and
create map data on the computer. It supports many common spatial data
formats (e.g. ESRI ShapeFile, geotiff). QGIS supports plugins to do
things like display tracks from a GPS.

%description devel
Development packages for QGIS, including the C header files.

%description sample-data
QGIS sample data with raster, vector, gps files and a GRASS location from the Alaska area.

%prep
%autosetup -p1
# Remove bad env and python version in grass plugin
sed -i 's,^#!%{_bindir}/env python$,#!%{_bindir}/python3,g' src/plugins/grass/scripts/*.py
sed -i 's,^#!%{_bindir}/env python3$,#!%{_bindir}/python3,g' src/plugins/grass/scripts/*.py

%build
%define _lto_cflags %{nil}

export CFLAGS="%{optflags}"
export QTDIR=%{_prefix}
export PATH=$PATH:$QTDIR/bin

%cmake \
  -DQGIS_LIB_SUBDIR=%{_lib} \
  -DWITH_3D=TRUE \
  -DWITH_BINDINGS=TRUE \
%if %{with grass}
  -DWITH_GRASS=TRUE \
  -DWITH_GRASS7=TRUE \
%if 0%{?suse_version} > 1500
  -DGRASS_PREFIX7=`cat %{_sysconfdir}/GRASSDIR` \
%else
  -DGRASS_PREFIX7=%{_libdir}/grass78 \
%endif
%endif
  -DWITH_QSPATIALITE=TRUE \
  -DWITH_SERVER=TRUE \
  -DWITH_SERVER_PLUGINS=TRUE \
  -DWITH_POSTGRESQL=TRUE \
  -DPOSTGRES_LIBRARY=%{_libdir}/libpq.so \
  -DPOSTGRES_INCLUDE_DIR=%{_includedir}/pgsql \
  -DQGIS_PLUGIN_SUBDIR=%{_lib}/qgis \
  -DQGIS_MANUAL_SUBDIR=share/man \
  -DQWT_INCLUDE_DIR=%{_includedir}/qt5/qwt6 \
  -DQCA_INCLUDE_DIR=%{_includedir}/qt5/Qca-qt5/QtCrypto \
  -DCMAKE_SKIP_RPATH=OFF \
  -DOpenCL_INCLUDE_DIR=%{_includedir} \
  -Wno-dev

export QTDIR=%{_prefix}
export PATH=$PATH:$QTDIR/bin
%ifarch ppc64le
# avoid OOM failure on power8-01 builder
%limit_build -m 1300
%endif
%make_jobs

%install
%cmake_install

mkdir -p %{buildroot}%{_datadir}/pixmaps
ln -s ../qgis/images/icons/qgis-icon-512x512.png %{buildroot}/%{_datadir}/pixmaps/qgis.png

# Rename .desktop file
mv %{buildroot}%{_datadir}/applications/org.qgis.qgis.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

# Install sample data
pushd %{buildroot}%{_datadir}/qgis
unzip %{SOURCE3}
mv qgis_sample_data %{sampledir}
find %{sampledir} -depth \( -name .tmp -o -name .bash\* -o -name \*~ \) -exec rm -r {} +
popd

%fdupes -s %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post plugin-grass -p /sbin/ldconfig
%postun plugin-grass -p /sbin/ldconfig

%files
%{_bindir}/*
%{_libdir}/libqgis*so*
%{_libdir}/qt5/plugins/sqldrivers/libqsqlspatialite.so
%{_mandir}/man1/*
%{_datadir}/qgis
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/qgis.png
# Own directories for icon size not provided by hicolor-icon-theme
%dir %{_datadir}/icons/hicolor/42x42
%dir %{_datadir}/icons/hicolor/42x42/apps
%dir %{_datadir}/icons/hicolor/42x42/mimetypes
%dir %{_datadir}/icons/hicolor/80x80
%dir %{_datadir}/icons/hicolor/80x80/apps
%dir %{_datadir}/icons/hicolor/80x80/mimetypes
%dir %{_datadir}/icons/hicolor/8x8
%dir %{_datadir}/icons/hicolor/8x8/apps
%dir %{_datadir}/icons/hicolor/8x8/mimetypes
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_datadir}/icons/hicolor/*/mimetypes/*.png
%{_datadir}/icons/hicolor/*/mimetypes/*.svg
%{_datadir}/metainfo/org.qgis.qgis.appdata.xml
%dir %{_libdir}/qgis/
%{_libdir}/qgis/*
%if %{with grass}
%exclude %{_libdir}/libqgisgrass7.so
%exclude %{_libdir}/libqgisgrass7.so.*
%exclude %{_libdir}/qgis/libgrassplugin7.so
%exclude %{_libdir}/qgis/libgrassprovider7.so
%exclude %{_libdir}/qgis/libgrassrasterprovider7.so
%exclude %{_libdir}/qgis/grass
%endif
%exclude %{_datadir}/qgis/%{sampledir}
%license COPYING
%doc BUGS README.md

%files devel
%{_includedir}/qgis/

%if %{with grass}
%files plugin-grass
%{_libdir}/qgis/libgrassplugin7.so
%{_libdir}/qgis/libgrassprovider7.so
%{_libdir}/qgis/libgrassrasterprovider7.so
%{_libdir}/libqgisgrass7.so
%{_libdir}/libqgisgrass7.so.*
%defattr(755,root,root)
%{_libdir}/qgis/grass
%endif

%files sample-data
%dir %{_datadir}/qgis
%{_datadir}/qgis/%{sampledir}

%changelog
