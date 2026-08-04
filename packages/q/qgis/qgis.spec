#
# spec file for package qgis
#
# Copyright (c) 2026 SUSE LLC and contributors
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
%if %{is_ltr}
Name:           qgis-ltr
%else
Name:           qgis
%endif

%define pythons python3
%define mypython %{pythons}
%define __mypython %{expand:%%__%{mypython}}

# QGIS links a very large number of C++ libraries and LTO regularly runs the
# builders out of memory here; the build is slow enough without it.
%define _lto_cflags %{nil}

Version:        4.2.1
Release:        0
Summary:        A Geographic Information System (GIS)
# The COPYING file carries the GPL-2.0 text, but the source headers throughout
# grant "version 2 of the License, or (at your option) any later version".
License:        GPL-2.0-or-later
URL:            https://qgis.org/
Source:         https://qgis.org/downloads/qgis-%{version}.tar.bz2
Source1:        https://qgis.org/downloads/qgis-%{version}.tar.bz2.sha256
Source2:        %{name}.rpmlintrc
Source3:        https://download.qgis.org/downloads/data/qgis_sample_data.zip
# PATCH-FIX-OPENSUSE - adapt include path of fastcgi
Patch1:         fix-fastcgi-include.patch
# PATCH-FIX-OPENSUSE - upstream looks for the pdal binary, which lives in the
# runtime package; only PDAL-devel (and thus pdal-config) is available here
Patch2:         qgis-fix-cmake-findpdal.patch
BuildRequires:  %{mypython}-GDAL
BuildRequires:  %{mypython}-Jinja2
BuildRequires:  %{mypython}-OWSLib
BuildRequires:  %{mypython}-PyQt6-QScintilla
BuildRequires:  %{mypython}-PyQt6-devel
BuildRequires:  %{mypython}-PyYAML
BuildRequires:  %{mypython}-devel >= 3.7
BuildRequires:  %{mypython}-psycopg2
BuildRequires:  %{mypython}-pygments
BuildRequires:  %{mypython}-pyqt-builder
BuildRequires:  %{mypython}-sip-devel
BuildRequires:  %{mypython}-termcolor
BuildRequires:  FastCGI-devel
BuildRequires:  PDAL-devel
BuildRequires:  bison >= 2.4
BuildRequires:  cmake >= 3.12.0
# %%build runs crssync, which loads libgdal and through it, via libarmadillo
# and libarpack, libopenblas.so.0. That path is a %%ghost created by
# update-alternatives from compatlibopenblas_serial0, and openblas advertises
# that package only via Supplements -- which OBS does not honour when it
# assembles a build root. So the soname is absent and crssync dies with
# "libopenblas.so.0: cannot open shared object file". Requiring it explicitly
# is a workaround for a defect in openblas, where the flavour package claims a
# soname it cannot make loadable; drop this once science/openblas#8 is in.
BuildRequires:  compatlibopenblas_serial0
BuildRequires:  fdupes
BuildRequires:  flex >= 2.5.6
BuildRequires:  gcc-c++
BuildRequires:  geos-devel >= 3.9
BuildRequires:  libspatialindex-devel
BuildRequires:  memory-constraints
BuildRequires:  opencl-cpp-headers
BuildRequires:  pkgconfig
BuildRequires:  poppler-tools
BuildRequires:  qscintilla-qt6-devel
# WITH_DESKTOP pulls in Qml/Quick unconditionally since 4.0; the devel package
# carries the Qt6Qml and Qt6Quick cmake configs but generates no cmake() provides
BuildRequires:  qt6-declarative-devel
BuildRequires:  qt6-sql-mysql
BuildRequires:  qt6-sql-postgresql
BuildRequires:  qt6-sql-private-devel
# Add the 3 main db we should access
# also have them in requires
BuildRequires:  qt6-sql-sqlite
BuildRequires:  qwt6-qt6-devel
BuildRequires:  sqlite-devel >= 3.12.0
BuildRequires:  unzip
BuildRequires:  cmake(Qca-qt6)
BuildRequires:  cmake(Qt63DCore)
BuildRequires:  cmake(Qt63DExtras)
BuildRequires:  cmake(Qt63DInput)
BuildRequires:  cmake(Qt63DLogic)
BuildRequires:  cmake(Qt63DRender)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Keychain) >= 0.5
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6MultimediaWidgets)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Positioning)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6SerialPort)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6UiTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  pkgconfig(Qt6Qwt6)
BuildRequires:  pkgconfig(draco)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(expat) >= 1.95
# Requires at least gdal 3.1 for GeoTIFF and Proj >= 6 - https://github.com/qgis/QGIS/issues/36699#issuecomment-633539864
BuildRequires:  pkgconfig(gdal) >= 3.2.0
BuildRequires:  pkgconfig(gsl) >= 1.8
BuildRequires:  pkgconfig(libpq) > 9.4
BuildRequires:  pkgconfig(libtasn1)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(netcdf)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(ocl-icd)
BuildRequires:  pkgconfig(pdal) >= 2.2.0
BuildRequires:  pkgconfig(proj) >= 7.2.0
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(protobuf-lite)
BuildRequires:  pkgconfig(spatialite) >= 4.2.0
Requires:       %{mypython}-GDAL
Requires:       %{mypython}-Jinja2
Requires:       %{mypython}-OWSLib
# Those are not picked by obs
Requires:       %{mypython}-PyQt6-QScintilla
Requires:       %{mypython}-PyYAML
Requires:       %{mypython}-Pygments
Requires:       %{mypython}-numpy
Requires:       %{mypython}-packaging
Requires:       %{mypython}-psycopg2
Requires:       %{mypython}-termcolor
Requires:       pdal
# proj.db is required
Requires:       proj
# Force requires of those 3 main component.
Requires:       qt6-sql-mysql
Requires:       qt6-sql-postgresql
Requires:       qt6-sql-sqlite
Recommends:     %{name}-sample-data
Recommends:     apache2-mod_fcgid
Recommends:     gpsbabel
Recommends:     mod_spatialite
# It's in Application:Geo, but not in Factory
Suggests:       saga-gis
%if %{is_ltr}
Conflicts:      qgis
%else
Conflicts:      qgis-ltr
%endif
Conflicts:      qgis-master
Obsoletes:      qgis2 < %{version}
%if %{with grass}
BuildRequires:  grass-devel >= 7.2
%endif
%ifarch aarch64
# Picked up by x86_64 and ppc64le, but not aarch64
BuildRequires:  pkgconfig(gl)
%endif

%description
QGIS is a Geographic Information System (GIS). QGIS supports vector,
raster, OWS and database formats. QGIS can be used to browse and
create map data on the computer. It supports many common spatial data
formats (e.g. ESRI ShapeFile, geotiff). QGIS supports plugins to do
things like display tracks from a GPS.

%package devel
Summary:        Development Libraries for QGIS
Requires:       %{mypython}-PyQt6-devel
Requires:       %{name} = %{version}

%description devel
Development packages for QGIS, including the C header files.

%if %{with grass}
%package plugin-grass
Summary:        GRASS Support Libraries for QGIS
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
BuildArch:      noarch

%description sample-data
QGIS sample data with raster, vector, gps files and a GRASS location from the Alaska area.

%lang_package

%prep
%autosetup -p1 -n qgis-%{version}
# Remove bad env and python version in grass plugin
sed -i 's,^#!%{_bindir}/env python$,#!%{__mypython},g' src/plugins/grass/scripts/*.py
sed -i 's,^#!%{_bindir}/env python3$,#!%{__mypython},g' src/plugins/grass/scripts/*.py

%build
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
  -DGRASS_PREFIX7=$(cat %{_sysconfdir}/GRASSDIR) \
  -DGRASS_PREFIX8=$(cat %{_sysconfdir}/GRASSDIR) \
%endif
  -DWITH_QSPATIALITE=TRUE \
  -DWITH_SERVER=TRUE \
  -DWITH_SERVER_PLUGINS=TRUE \
  -DWITH_POSTGRESQL=TRUE \
  -DWITH_PDAL=TRUE \
  -DWITH_INTERNAL_NLOHMANN_JSON=FALSE \
  -DWITH_QTWEBENGINE=FALSE \
  -DFCGI_INCLUDE_DIR=%{_includedir}/fastcgi \
  -DPOSTGRES_LIBRARY=%{_libdir}/libpq.so \
  -DPOSTGRES_INCLUDE_DIR=%{_includedir}/pgsql \
  -DQGIS_PLUGIN_SUBDIR=%{_lib}/qgis \
  -DQGIS_MANUAL_SUBDIR=share/man \
  -DQGIS_CGIBIN_SUBDIR=bin \
  -DQWT_INCLUDE_DIR=%{_includedir}/qt6/qwt6 \
  -DQCA_INCLUDE_DIR=%{_includedir}/qt6/Qca-qt6/QtCrypto \
  -DCMAKE_SKIP_RPATH=OFF \
  -DOpenCL_INCLUDE_DIR=%{_includedir} \
  -Wno-dev

# The SIP-generated Python binding translation units (sip_corepart*.cpp) are
# enormous and each cc1plus on them peaks well past 3 GB, so an unrestricted
# job count runs any builder out of memory -- this used to be capped for
# ppc64le only, but QGIS 4 needs it everywhere.
%limit_build -m 4000
%cmake_build

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

%ldconfig_scriptlets

%if %{with grass}
%ldconfig_scriptlets plugin-grass
%endif

%files
%{_bindir}/*
%{_libdir}/libqgis*so*
%{_libdir}/qt6/plugins/sqldrivers/libqsqlspatialite.so
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
