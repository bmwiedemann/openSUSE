#
# spec file for package qgis
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


%define is_ltr 0

%bcond_without grass
%if %is_ltr
Name:           qgis-ltr
%else
Name:           qgis
%endif

%if 0%{suse_version} >= 1600
%define pythons python3
%else
%define gccver 13
%{?sle15_python_module_pythons}
%endif
%define mypython %pythons
%define __mypython %{expand:%%__%{mypython}}

Version:        3.44.2
Release:        0
Summary:        A Geographic Information System (GIS)
License:        GPL-2.0-only
Group:          Productivity/Graphics/Visualization/Other
URL:            https://qgis.org/
Source:         https://qgis.org/downloads/qgis-%{version}.tar.bz2
Source1:        https://qgis.org/downloads/qgis-%{version}.tar.bz2.sha256
Source2:        %{name}.rpmlintrc
Source3:        https://download.qgis.org/downloads/data/qgis_sample_data.zip
# PATCH-FIX-OPENSUSE - adapt include path of fastcgi
Patch1:         fix-fastcgi-include.patch
# PATCH-FIX-UPSTREAM - scan for pdal-config instead of pdal in cmake
Patch2:         qgis-fix-cmake-findpdal.patch
BuildRequires:  FastCGI-devel
BuildRequires:  PDAL-devel
BuildRequires:  bison >= 2.4
BuildRequires:  cmake >= 3.12.0
BuildRequires:  fdupes
BuildRequires:  filesystem
BuildRequires:  flex >= 2.5.6
BuildRequires:  gcc%{?gccver}-c++
BuildRequires:  geos-devel >= 3.9
BuildRequires:  libQt5Sql-private-headers-devel
BuildRequires:  libQt5Sql5-mysql
BuildRequires:  libQt5Sql5-postgresql
# Add the 3 main db we should access
# also have them in requires
BuildRequires:  libQt5Sql5-sqlite
BuildRequires:  %{mypython}-GDAL
BuildRequires:  %{mypython}-Jinja2
BuildRequires:  %{mypython}-OWSLib
BuildRequires:  %{mypython}-PyYAML
BuildRequires:  %{mypython}-devel >= 3.7
BuildRequires:  %{mypython}-psycopg2
BuildRequires:  %{mypython}-pygments
BuildRequires:  %{mypython}-pyqt-builder
BuildRequires:  %{mypython}-qscintilla-qt5
BuildRequires:  %{mypython}-qscintilla-qt5-sip
BuildRequires:  %{mypython}-qt5-devel
BuildRequires:  %{mypython}-sip-devel
BuildRequires:  %{mypython}-termcolor
BuildRequires:  libexiv2-devel
BuildRequires:  libqscintilla_qt5-devel
BuildRequires:  libspatialindex-devel
BuildRequires:  libzstd-devel
BuildRequires:  ocl-icd-devel
BuildRequires:  opencl-cpp-headers
BuildRequires:  pkgconfig
BuildRequires:  poppler-tools
BuildRequires:  protobuf-devel
BuildRequires:  sqlite-devel >= 3.12.0
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  (qwt6-devel or qwt6-qt5-devel)
BuildRequires:  cmake(Qt53DAnimation)
BuildRequires:  cmake(Qt53DCore)
BuildRequires:  cmake(Qt53DExtras)
BuildRequires:  cmake(Qt53DInput)
BuildRequires:  cmake(Qt53DLogic)
BuildRequires:  cmake(Qt53DQuick)
BuildRequires:  cmake(Qt53DQuickAnimation)
BuildRequires:  cmake(Qt53DQuickExtras)
BuildRequires:  cmake(Qt53DQuickInput)
BuildRequires:  cmake(Qt53DQuickRender)
BuildRequires:  cmake(Qt53DQuickScene2D)
BuildRequires:  cmake(Qt53DRender)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Keychain) >= 0.5
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Positioning)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Script)
BuildRequires:  cmake(Qt5SerialPort)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(draco)
BuildRequires:  pkgconfig(expat) >= 1.95
# Requires at least gdal 3.1 for GeoTIFF and Proj >= 6 - https://github.com/qgis/QGIS/issues/36699#issuecomment-633539864
BuildRequires:  pkgconfig(gdal) >= 3.2.0
BuildRequires:  pkgconfig(Qt5Qwt6)
BuildRequires:  pkgconfig(gsl) >= 1.8
BuildRequires:  pkgconfig(libpq) > 9.4
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(netcdf)
BuildRequires:  pkgconfig(pdal) >= 2.2.0
BuildRequires:  pkgconfig(proj) >= 7.2.0
BuildRequires:  pkgconfig(qca2-qt5)
BuildRequires:  pkgconfig(spatialite) >= 4.2.0
# Force requires of those 3 main component.
Requires:       libQt5Sql5-mysql
Requires:       libQt5Sql5-postgresql
Requires:       libQt5Sql5-sqlite
# proj.db is required
Requires:       proj
Requires:       %{mypython}-GDAL
Requires:       %{mypython}-Jinja2
Requires:       %{mypython}-OWSLib
Requires:       %{mypython}-PyYAML
Requires:       %{mypython}-Pygments
Requires:       %{mypython}-numpy
Requires:       %{mypython}-packaging
Requires:       %{mypython}-psycopg2
Requires:       pdal
# Those are not picked by obs
Requires:       %{mypython}-qscintilla-qt5
Requires:       %{mypython}-termcolor
Recommends:     %{name}-sample-data
Recommends:     apache2-mod_fcgid
Recommends:     gpsbabel
Recommends:     mod_spatialite
# It's in Application:Geo, but not in Factory
Suggests:       saga-gis
%if %is_ltr
Conflicts:      qgis
%else
Conflicts:      qgis-ltr
%endif
Conflicts:      qgis-master
Obsoletes:      qgis2 < %{version}
%if %{with grass}
BuildRequires:  grass-devel >= 7.2
%endif
%ifarch ppc64le
BuildRequires:  memory-constraints
%endif
%ifarch aarch64
# Picked up by x86_64 and ppc64le, but not aarch64
BuildRequires:  Mesa-libGL-devel
%endif

%package devel
Summary:        Development Libraries for QGIS
Group:          Development/Libraries/C and C++
Requires:       %{mypython}-qt5-devel
Requires:       %{name} = %{version}
%if %{with grass}
%package plugin-grass
Summary:        GRASS Support Libraries for QGIS
Group:          Productivity/Graphics/Visualization/Other
Requires:       %{name} = %{version}
Requires:       grass > 7.0
Requires:       grass-doc
Obsoletes:      %{name}-plugin-grass < %{version}

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

%lang_package

%prep
%autosetup -p1 -n qgis-%{version}
# Remove bad env and python version in grass plugin
sed -i 's,^#!%{_bindir}/env python$,#!%{__mypython},g' src/plugins/grass/scripts/*.py
sed -i 's,^#!%{_bindir}/env python3$,#!%{__mypython},g' src/plugins/grass/scripts/*.py

%build
%define _lto_cflags %{nil}
%{?gccver:export CC=gcc-%{gccver}}
%{?gccver:export CXX=g++-%{gccver}}

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
  -DWITH_GRASS8=TRUE \
%if 0%{?suse_version} > 1500
  -DGRASS_PREFIX7=`cat %{_sysconfdir}/GRASSDIR` \
  -DGRASS_PREFIX8=`cat %{_sysconfdir}/GRASSDIR` \
%else
  -DGRASS_PREFIX7=%{_libdir}/grass78 \
  -DGRASS_PREFIX8=%{_libdir}/grass82 \
%endif
%endif
  -DWITH_QSPATIALITE=TRUE \
  -DWITH_SERVER=TRUE \
  -DWITH_SERVER_PLUGINS=TRUE \
  -DWITH_POSTGRESQL=TRUE \
  -DWITH_PDAL=TRUE \
  -DWITH_QTWEBKIT=FALSE \
  -DFCGI_INCLUDE_DIR=%{_includedir}/fastcgi \
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

%find_lang %{name} --with-qt %{?no_lang_C}

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
%exclude %{_datadir}/qgis/i18n/*
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
%exclude %{_libdir}/libqgisgrass?.so
%exclude %{_libdir}/libqgisgrass?.so.*
%exclude %{_libdir}/qgis/libplugin_grass?.so
%exclude %{_libdir}/qgis/libprovider_grass?.so
%exclude %{_libdir}/qgis/libprovider_grassraster?.so
%exclude %{_libdir}/qgis/grass
%endif
%exclude %{_datadir}/qgis/%{sampledir}
%license COPYING
%doc BUGS README.md

%files devel
%{_includedir}/qgis/

%if %{with grass}
%files plugin-grass
%{_libdir}/qgis/libplugin_grass?.so
%{_libdir}/qgis/libprovider_grass?.so
%{_libdir}/qgis/libprovider_grassraster?.so
%{_libdir}/libqgisgrass?.so
%{_libdir}/libqgisgrass?.so.*
%defattr(755,root,root)
%{_libdir}/qgis/grass
%endif

%files sample-data
%dir %{_datadir}/qgis
%{_datadir}/qgis/%{sampledir}

%files lang -f %{name}.lang

%changelog
