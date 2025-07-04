#
# spec file for package gdal
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define soversion 37
%define sourcename gdal
# Uppercase GDAL is the canonical name for this package in Python
%define pypi_package_name GDAL
%bcond_with ecw_support
%bcond_with ecw5_support
%bcond_with fgdb_support
%bcond_with kml_support
%bcond_with sfcgal_support
%bcond_with hdf4_support
%bcond_with heif_support
%bcond_with qhull_support
%bcond_with deflate_support
%bcond_with tests_support

%if 0%{suse_version} > 1500
%define pythons python3
%else
%{?sle15_python_module_pythons}
%define gccver 13
%endif
%define mypython %pythons
%define __mypython %{expand:%%__%{mypython}}
%define mypython_sitearch %{expand:%%%{mypython}_sitearch}

Name:           gdal
Version:        3.11.0
Release:        0
Summary:        GDAL/OGR - a translator library for raster and vector geospatial data formats
License:        BSD-3-Clause AND MIT AND SUSE-Public-Domain
URL:            https://www.gdal.org/
Source0:        https://download.osgeo.org/%{name}/%{version}/%{sourcename}-%{version}.tar.xz
Source1:        https://download.osgeo.org/%{name}/%{version}/%{sourcename}-%{version}.tar.xz.md5
Source2:        https://download.osgeo.org/%{name}/%{version}/%{sourcename}autotest-%{version}.tar.gz
Patch0:         gdal-backport-commit-b11cad7.patch
BuildRequires:  KEALib-devel
BuildRequires:  bison
BuildRequires:  blas-devel
BuildRequires:  chrpath
BuildRequires:  curl-devel
BuildRequires:  dos2unix
BuildRequires:  doxygen >= 1.4.2
BuildRequires:  fdupes
BuildRequires:  gcc%{?gccver}-c++
BuildRequires:  geos-devel >= 3.8
BuildRequires:  giflib-devel
BuildRequires:  hdf5-devel >= 1.10
BuildRequires:  lapack-devel
BuildRequires:  libcryptopp-devel
BuildRequires:  libdeflate-devel
BuildRequires:  libtool
BuildRequires:  libzstd-devel
BuildRequires:  mysql-devel
BuildRequires:  muparser-devel
# This one is needed for Leap :-(
BuildRequires:  opencl-headers
BuildRequires:  %{mypython}-base
BuildRequires:  %{mypython}-devel
BuildRequires:  %{mypython}-numpy-devel
BuildRequires:  %{mypython}-setuptools
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig
BuildRequires:  shapelib >= 1.4
BuildRequires:  swig
BuildRequires:  unixODBC-devel
BuildRequires:  pkgconfig(OpenCL)
# c++17 standard errors for older versions
BuildRequires:  pkgconfig(OpenEXR) >= 3
BuildRequires:  pkgconfig(armadillo)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(expat) >= 1.95.0
BuildRequires:  pkgconfig(freexl)
BuildRequires:  pkgconfig(json)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libgeotiff) >= 1.2.1
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libopenjp2) >= 2.3.1
BuildRequires:  pkgconfig(libpng) >= 1.6
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(libtiff-4) >= 4.1
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwebpdecoder)
BuildRequires:  pkgconfig(libwebpdemux)
BuildRequires:  pkgconfig(libwebpmux)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(netcdf)
BuildRequires:  pkgconfig(ocl-icd)
BuildRequires:  pkgconfig(poppler) >= 0.86
BuildRequires:  pkgconfig(proj) >= 6.3
BuildRequires:  pkgconfig(shapelib)
BuildRequires:  pkgconfig(spatialite) >= 4.1.2
BuildRequires:  pkgconfig(sqlite3) >= 3.31
BuildRequires:  pkgconfig(xerces-c)
BuildRequires:  pkgconfig(zlib) >= 1.1.4
%if %{with tests_support}
BuildRequires:  cmake-full
%else
BuildRequires:  cmake
%endif
%if 0%{?sle_version} == 150300 && 0%{?is_opensuse}
BuildRequires:  python-rpm-macros
%endif
%if %{with tests_support}
BuildRequires:  %{mypython}-lxml
BuildRequires:  %{mypython}-pytest
BuildRequires:  %{mypython}-pytest-env
BuildRequires:  %{mypython}-pytest-sugar
BuildRequires:  proj
%endif
%if %{with deflate_support}
BuildRequires:  libdeflate-devel
%endif
%if %{with fgdb_support}
BuildRequires:  filegdb_api-devel
%endif
%if %{with kml_support}
BuildRequires:  pkgconfig(libkml)
%endif
%if %{with sfcgal_support}
BuildRequires:  pkgconfig(sfcgal)
%endif
%if %{with heif_support}
BuildRequires:  libheif-devel
%endif
%if %{with hdf4_support}
BuildRequires:  hdf-devel
%endif
%if %{with qhull_support}
BuildRequires:  pkgconfig(qhull_r)
%endif
%if %{with ecw5_support}
BuildRequires:  ERDAS-ECW_JPEG_2000_SDK-devel
%else
%if %{with ecw_support}
BuildRequires:  libecwj2-devel
%endif
%endif
# 3.9.x we stop requiring this hardly
#Requires:       %%{mypython}-GDAL = %%{version}

%description
GDAL is a translator library for raster geospatial data formats that
is released under an Open Source license. As a library, it presents a
single abstract data model to the calling application for all
supported formats. The related OGR library (which lives within the
GDAL source tree) provides a similar capability for simple features
vector data.

%package devel
Summary:        GDAL library header files
Requires:       lib%{name}%{soversion} = %{version}
Requires:       pkgconfig(libopenjp2)
Provides:       lib%{name}%{soversion}-devel = %{version}
Provides:       lib%{name}-devel = %{version}

%description devel
Development Libraries for the GDAL file format library

%package -n lib%{name}%{soversion}
Summary:        GDAL static libraries
Requires:       lib%{name}-drivers >= %{version}

%description -n lib%{name}%{soversion}
GDAL and OGR are translator libraries for raster and vector geospatial data
formats. As a library, it presents a single abstract data model to the calling
application for all supported formats.

%package -n lib%{name}-drivers
Summary:        GDAL static libraries drivers files
# soversion 32 contained the drivers file and thus will cause a conflict
Conflicts:      lib%{name}32

%description -n lib%{name}-drivers
Drivers information for library

%package -n %{mypython}-%{pypi_package_name}
Summary:        GDAL %{mypython} module
Requires:       %{name} = %{version}-%{release}
Provides:       %{mypython}-%{name} = %{version}
Obsoletes:      %{mypython}-%{name} < %{version}

%description -n %{mypython}-%{pypi_package_name}
The GDAL python modules provide support to handle multiple GIS file formats.

%package bash-completion
Summary:        Bash completion for GDAL
Group:          System/Shells
Requires:       %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
bash command line completion support for GDAL

%prep
%autosetup -p1 -n %{sourcename}-%{version} -a2
# Delete bundled libraries
# keep zlib due to missing frmts/zlib/contrib/infback9 in our package
# rm -rv frmts/zlib
rm -rv frmts/png/libpng
rm -rv frmts/gif/giflib
rm -rv frmts/jpeg/libjpeg
rm -rv frmts/jpeg/libjpeg12
rm -rv frmts/gtiff/libgeotiff
rm -rv frmts/gtiff/libtiff
# internal but needed rm -rv frmts/pcidsk

# Fix wrong encoding EOL
for F in frmt_twms_srtm.xml frmt_wms_bluemarble_s3_tms.xml frmt_wms_virtualearth.xml frmt_twms_Clementine.xml;do
  find . -name "${F}" -exec dos2unix {} \;
done

# Remove shebang in scripts located in non executable dir
find swig/python/gdal-utils/osgeo_utils -iname '*.py' -ls -exec sed -i '/^#!\/usr\/bin\/env python3/d' {} \;
find swig/python/gdal-utils/osgeo_utils -iname '*.py' -ls -exec sed -i '/^#!\/usr\/bin\/env python/d' {} \;
# Fix wrong /usr/bin/env python3
find . -iname "*.py" -exec sed -i "s,^#!%{_bindir}/env python3,#!%{__mypython}," {} \;

# Remove libertiff
sed -e 's|gdal_optional_format(libertiff "GeoTIFF support through libertiff library")||1' -i frmts/CMakeLists.txt

%build
%{?gccver:export CC=gcc-%{gccver}}
%{?gccver:export CXX=g++-%{gccver}}
%cmake \
  -DGDAL_USE_INTERNAL_LIBS=OFF \
  -DGDAL_USE_EXTERNAL_LIBS=ON \
%if %{with ecw5_support}
  -DECW_ROOT="../ECW/Desktop_Read-Only" \
%endif
  -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir}/gdal \
  -DGDAL_USE_ARMADILLO=ON \
  -DGDAL_USE_CFITSIO=OFF \
  -DGDAL_USE_CURL=ON \
  -DGDAL_USE_EXPAT=ON \
  -DGDAL_USE_FREEXL=ON \
  -DGDAL_USE_GEOS=ON \
  -DGDAL_USE_GIF=ON \
%if %{with hdf4_support}
  -DGDAL_USE_HDF4=ON \
%else
  -DGDAL_USE_HDF4=OFF \
%endif
  -DGDAL_USE_HDF5=ON \
%if %{with heif_support}
  -DGDAL_USE_HEIF=ON \
%else
  -DGDAL_USE_HEIF=OFF \
%endif
  -DGDAL_USE_LERC_INTERNAL=ON \
  -DGDAL_USE_JPEG=ON \
  -DGDAL_USE_JPEG12_INTERNAL=OFF \
  -DGDAL_USE_JSONC=ON \
  -DGDAL_USE_KEA=ON \
%if %{with kml_support}
  -DGDAL_USE_LIBKML=ON \
%else
  -DGDAL_USE_LIBKML=OFF \
%endif
  -DGDAL_USE_LIBLZMA=ON \
  -DGDAL_USE_LIBXML2=ON \
  -DGDAL_USE_MYSQL=ON \
  -DGDAL_USE_NETCDF=ON \
  -DGDAL_USE_ODBC=ON \
  -DGDAL_USE_OGDI=OFF \
  -DGDAL_USE_OPENCL=ON \
  -DGDAL_USE_OPENJPEG=ON \
  -DGDAL_USE_PCRE2=ON \
  -DGDAL_USE_PNG=ON \
  -DGDAL_USE_POPPLER=ON \
  -DGDAL_USE_POSTGRESQL=ON \
%if %{with qhull_support}
  -DGDAL_USE_QHULL=ON \
%else
  -DGDAL_USE_QHULL=OFF \
%endif
%if %{with sfcgal_support}
  -DGDAL_USE_SFCGAL=ON \
%else
  -DGDAL_USE_SFCGAL=OFF \
%endif
  -DGDAL_USE_SHAPELIB=OFF \
  -DGDAL_USE_SPATIALITE=ON \
  -DGDAL_USE_TIFF=ON \
  -DGDAL_USE_WEBP=ON \
  -DGDAL_USE_XERCESC=ON \
  -DGDAL_USE_ZLIB=ON \
  -DGDAL_USE_ZSTD=ON \
  -DOGR_BUILD_OPTIONAL_DRIVERS=ON

%cmake_build

%install
%cmake_install
%python3_fix_shebang
%fdupes %{buildroot}%{mypython_sitearch}
#remove duplicate license file
rm -f %{buildroot}%{_datadir}/%{name}/LICENSE.TXT

%if %{with tests_support}
%check
%ctest
pushd %{name}autotest-%{version}
	export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{_libdir}
	export GDAL_DATA=%{buildroot}%{_datadir}/%{name}/
    export PYTHONPATH=%{buildroot}%{mypython_sitearch}/
	export GDAL_DOWNLOAD_TEST_DATA=0
	# Enable these tests on demand
	#export GDAL_RUN_SLOW_TESTS=1

	# Some tests are currently skipped:
    # - `test_fits_vector` because it's crashing.
	# - `test_http*`, `test_jp2openjpeg_45`, `*multithreaded_download*`,
	#   `*multithreaded_upload*`, and `test_vsis3_no_sign_request`, which
	#   try to connect externally.
	# - `test_eedai_GOOGLE_APPLICATION_CREDENTIALS` which seems to use the
	#   internet.
	# - `test_osr_erm_1`, `test_ers_4`, `test_ers_8`, and `test_ers_10` as
	#   they use `ecw_cs.wkt` which was removed due to unclear license.
	# - `test_jpeg2000_8` and `test_jpeg2000_11` as files don't load,
	#   perhaps due to buggy Jasper library?
	# - `test_osr_ct_options_area_of_interest` returns the wrong value, but
	#   it's skipped on macOS by upstream for mysteriously failing as well,
	#   so do the same here.
	# - `test_ndf_1` because it hangs on i686 and armv7hl
# FIXME: Tests hang on i686 and armv7hl
%ifnarch i686 armv7hl
	pytest -k 'not test_fits_vector and not test_http and not test_jp2openjpeg_45 and not multithreaded_download and not multithreaded_upload and not test_vsis3_no_sign_request and not test_eedai_GOOGLE_APPLICATION_CREDENTIALS and not test_osr_erm_1 and not test_ers_4 and not test_ers_8 and not test_ers_10 and not test_jpeg2000_8 and not test_jpeg2000_11 and not test_osr_ct_options_area_of_interest and not test_ndf_1 and not test_cog_small_world_to_web_mercator and not test_bag and not gpkg and not jp2openjpeg and not wms and not heif' || :
%endif
popd
%endif

%ldconfig_scriptlets -n lib%{name}%{soversion}

%files -n lib%{name}%{soversion}
%license LICENSE.TXT
%{_libdir}/*.so.%{soversion}.*
%{_libdir}/*.so.%{soversion}

%files -n lib%{name}-drivers
%license LICENSE.TXT
%dir %{_libdir}/gdalplugins
%{_libdir}/gdalplugins/drivers.ini

%files
%license LICENSE.TXT
%doc NEWS.md PROVENANCE.TXT
%{_bindir}/gdal
%{_bindir}/gdal_contour
%{_bindir}/gdal_create
%{_bindir}/gdal_footprint
%{_bindir}/gdal_grid
%{_bindir}/gdal_rasterize
%{_bindir}/gdal_translate
%{_bindir}/gdal_viewshed
%{_bindir}/gdaladdo
%{_bindir}/gdalbuildvrt
%{_bindir}/gdaldem
%{_bindir}/gdalenhance
%{_bindir}/gdalinfo
%{_bindir}/gdallocationinfo
%{_bindir}/gdalmanage
%{_bindir}/gdalmdiminfo
%{_bindir}/gdalmdimtranslate
%{_bindir}/gdalsrsinfo
%{_bindir}/gdaltindex
%{_bindir}/gdaltransform
%{_bindir}/gdalwarp
%{_bindir}/gnmanalyse
%{_bindir}/gnmmanage
%{_bindir}/nearblack
%{_bindir}/ogr2ogr
%{_bindir}/ogrinfo
%{_bindir}/ogrlineref
%{_bindir}/ogrtindex
%{_bindir}/sozip
%{_datadir}/gdal
%{_mandir}/man1/gdal_contour.1%{?ext_man}
%{_mandir}/man1/gdal_create.1%{?ext_man}
%{_mandir}/man1/gdal_footprint.1%{?ext_man}
%{_mandir}/man1/gdal_rasterize.1%{?ext_man}
%{_mandir}/man1/gdal_translate.1%{?ext_man}
%{_mandir}/man1/gdal_viewshed.1%{?ext_man}
%{_mandir}/man1/gdaladdo.1%{?ext_man}
%{_mandir}/man1/gdalbuildvrt.1%{?ext_man}
%{_mandir}/man1/gdaldem.1%{?ext_man}
%{_mandir}/man1/gdalinfo.1%{?ext_man}
%{_mandir}/man1/gdallocationinfo.1%{?ext_man}
%{_mandir}/man1/gdalmanage.1%{?ext_man}
%{_mandir}/man1/gdalmdiminfo.1%{?ext_man}
%{_mandir}/man1/gdalmdimtranslate.1%{?ext_man}
%{_mandir}/man1/gdalsrsinfo.1%{?ext_man}
%{_mandir}/man1/gdaltindex.1%{?ext_man}
%{_mandir}/man1/gdaltransform.1%{?ext_man}
%{_mandir}/man1/gdalwarp.1%{?ext_man}
%{_mandir}/man1/gnmanalyse.1%{?ext_man}
%{_mandir}/man1/gnmmanage.1%{?ext_man}
%{_mandir}/man1/nearblack.1%{?ext_man}
%{_mandir}/man1/ogr2ogr.1%{?ext_man}
%{_mandir}/man1/ogrinfo.1%{?ext_man}
%{_mandir}/man1/ogrlineref.1%{?ext_man}
%{_mandir}/man1/ogrtindex.1%{?ext_man}
%{_mandir}/man1/sozip.1%{?ext_man}
%{_mandir}/man1/gdal-convert.1%{?ext_man}
%{_mandir}/man1/gdal-info.1%{?ext_man}
%{_mandir}/man1/gdal-mdim-convert.1%{?ext_man}
%{_mandir}/man1/gdal-mdim-info.1%{?ext_man}
%{_mandir}/man1/gdal-mdim.1%{?ext_man}
%{_mandir}/man1/gdal-raster-calc.1%{?ext_man}
%{_mandir}/man1/gdal-raster-clean-collar.1%{?ext_man}
%{_mandir}/man1/gdal-raster-clip.1%{?ext_man}
%{_mandir}/man1/gdal-raster-color-map.1%{?ext_man}
%{_mandir}/man1/gdal-raster-contour.1%{?ext_man}
%{_mandir}/man1/gdal-raster-convert.1%{?ext_man}
%{_mandir}/man1/gdal-raster-create.1%{?ext_man}
%{_mandir}/man1/gdal-raster-edit.1%{?ext_man}
%{_mandir}/man1/gdal-raster-fill-nodata.1%{?ext_man}
%{_mandir}/man1/gdal-raster-footprint.1%{?ext_man}
%{_mandir}/man1/gdal-raster-hillshade.1%{?ext_man}
%{_mandir}/man1/gdal-raster-index.1%{?ext_man}
%{_mandir}/man1/gdal-raster-info.1%{?ext_man}
%{_mandir}/man1/gdal-raster-mosaic.1%{?ext_man}
%{_mandir}/man1/gdal-raster-overview-add.1%{?ext_man}
%{_mandir}/man1/gdal-raster-overview-delete.1%{?ext_man}
%{_mandir}/man1/gdal-raster-pipeline.1%{?ext_man}
%{_mandir}/man1/gdal-raster-pixel-info.1%{?ext_man}
%{_mandir}/man1/gdal-raster-polygonize.1%{?ext_man}
%{_mandir}/man1/gdal-raster-reclassify.1%{?ext_man}
%{_mandir}/man1/gdal-raster-reproject.1%{?ext_man}
%{_mandir}/man1/gdal-raster-resize.1%{?ext_man}
%{_mandir}/man1/gdal-raster-roughness.1%{?ext_man}
%{_mandir}/man1/gdal-raster-scale.1%{?ext_man}
%{_mandir}/man1/gdal-raster-select.1%{?ext_man}
%{_mandir}/man1/gdal-raster-set-type.1%{?ext_man}
%{_mandir}/man1/gdal-raster-sieve.1%{?ext_man}
%{_mandir}/man1/gdal-raster-slope.1%{?ext_man}
%{_mandir}/man1/gdal-raster-stack.1%{?ext_man}
%{_mandir}/man1/gdal-raster-tile.1%{?ext_man}
%{_mandir}/man1/gdal-raster-tpi.1%{?ext_man}
%{_mandir}/man1/gdal-raster-tri.1%{?ext_man}
%{_mandir}/man1/gdal-raster-unscale.1%{?ext_man}
%{_mandir}/man1/gdal-raster-viewshed.1%{?ext_man}
%{_mandir}/man1/gdal-raster.1%{?ext_man}
%{_mandir}/man1/gdal-vector-clip.1%{?ext_man}
%{_mandir}/man1/gdal-vector-convert.1%{?ext_man}
%{_mandir}/man1/gdal-vector-edit.1%{?ext_man}
%{_mandir}/man1/gdal-vector-filter.1%{?ext_man}
%{_mandir}/man1/gdal-vector-geom-buffer.1%{?ext_man}
%{_mandir}/man1/gdal-vector-geom-explode-collections.1%{?ext_man}
%{_mandir}/man1/gdal-vector-geom-make-valid.1%{?ext_man}
%{_mandir}/man1/gdal-vector-geom-segmentize.1%{?ext_man}
%{_mandir}/man1/gdal-vector-geom-set-type.1%{?ext_man}
%{_mandir}/man1/gdal-vector-geom-simplify.1%{?ext_man}
%{_mandir}/man1/gdal-vector-geom-swap-xy.1%{?ext_man}
%{_mandir}/man1/gdal-vector-geom.1%{?ext_man}
%{_mandir}/man1/gdal-vector-grid.1%{?ext_man}
%{_mandir}/man1/gdal-vector-info.1%{?ext_man}
%{_mandir}/man1/gdal-vector-pipeline.1%{?ext_man}
%{_mandir}/man1/gdal-vector-rasterize.1%{?ext_man}
%{_mandir}/man1/gdal-vector-select.1%{?ext_man}
%{_mandir}/man1/gdal-vector-sql.1%{?ext_man}
%{_mandir}/man1/gdal-vector.1%{?ext_man}
%{_mandir}/man1/gdal-vector_concat.1%{?ext_man}
%{_mandir}/man1/gdal-vsi-copy.1%{?ext_man}
%{_mandir}/man1/gdal-vsi-delete.1%{?ext_man}
%{_mandir}/man1/gdal-vsi-list.1%{?ext_man}
%{_mandir}/man1/gdal-vsi-move.1%{?ext_man}
%{_mandir}/man1/gdal-vsi-sozip.1%{?ext_man}
%{_mandir}/man1/gdal-vsi-sync.1%{?ext_man}
%{_mandir}/man1/gdal-vsi.1%{?ext_man}
%{_mandir}/man1/gdal.1%{?ext_man}
# 20240706 with 3.9.x release we have all binaries in gdal
# and python311-GDAL contains the *.py equivalent.
%{_bindir}/gdalattachpct
%{_bindir}/gdal2tiles
%{_bindir}/gdal2xyz
%{_bindir}/gdal_calc
%{_bindir}/gdal_edit
%{_bindir}/gdal_fillnodata
%{_bindir}/gdal_merge
%{_bindir}/gdal_pansharpen
%{_bindir}/gdal_polygonize
%{_bindir}/gdal_proximity
%{_bindir}/gdal_retile
%{_bindir}/gdal_sieve
%{_bindir}/gdalcompare
%{_bindir}/gdalmove
%{_bindir}/ogrmerge
%{_bindir}/ogr_layer_algebra
%{_bindir}/pct2rgb
%{_bindir}/rgb2pct
%{_mandir}/man1/gdal2tiles.1%{?ext_man}
%{_mandir}/man1/gdal_calc.1%{?ext_man}
%{_mandir}/man1/gdal_edit.1%{?ext_man}
%{_mandir}/man1/gdal_fillnodata.1%{?ext_man}
%{_mandir}/man1/gdal_grid.1%{?ext_man}
%{_mandir}/man1/gdal_merge.1%{?ext_man}
%{_mandir}/man1/gdal_pansharpen.1%{?ext_man}
%{_mandir}/man1/gdal_polygonize.1%{?ext_man}
%{_mandir}/man1/gdal_proximity.1%{?ext_man}
%{_mandir}/man1/gdal_retile.1%{?ext_man}
%{_mandir}/man1/gdal_sieve.1%{?ext_man}
%{_mandir}/man1/gdalcompare.1%{?ext_man}
%{_mandir}/man1/gdalmove.1%{?ext_man}
%{_mandir}/man1/ogrmerge.1%{?ext_man}
%{_mandir}/man1/ogr_layer_algebra.1%{?ext_man}
%{_mandir}/man1/pct2rgb.1%{?ext_man}
%{_mandir}/man1/rgb2pct.1%{?ext_man}

%files devel
%license LICENSE.TXT
%doc NEWS.md PROVENANCE.TXT
%if %{with docs}
%doc doc/build/html/
%endif
%attr(755,root,root) %{_bindir}/gdal-config
%dir %{_libdir}/cmake/gdal
%{_libdir}/cmake/gdal/*.cmake
%{_libdir}/libgdal.so
%{_libdir}/pkgconfig/gdal.pc
%dir %{_includedir}/gdal
%{_includedir}/gdal/*.h
%{_includedir}/gdal/gdal_minmax_element.hpp
%{_includedir}/gdal/gdal_priv_templates.hpp
%{_mandir}/man1/gdal-config.1%{?ext_man}

%files -n %{mypython}-%{pypi_package_name}
%license LICENSE.TXT
%doc NEWS.md PROVENANCE.TXT
%{mypython_sitearch}/osgeo_utils
%{mypython_sitearch}/osgeo
%{mypython_sitearch}/GDAL-%{version}*-info
%{_bindir}/gdalattachpct.py
%{_bindir}/gdal2tiles.py
%{_bindir}/gdal2xyz.py
%{_bindir}/gdal_calc.py
%{_bindir}/gdal_edit.py
%{_bindir}/gdal_fillnodata.py
%{_bindir}/gdal_merge.py
%{_bindir}/gdal_pansharpen.py
%{_bindir}/gdal_polygonize.py
%{_bindir}/gdal_proximity.py
%{_bindir}/gdal_retile.py
%{_bindir}/gdal_sieve.py
%{_bindir}/gdalcompare.py
%{_bindir}/gdalmove.py
%{_bindir}/ogrmerge.py
%{_bindir}/ogr_layer_algebra.py
%{_bindir}/pct2rgb.py
%{_bindir}/rgb2pct.py

%files bash-completion
%license LICENSE.TXT
%{_datadir}/bash-completion/completions/*

%changelog
