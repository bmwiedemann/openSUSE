#
# spec file for package gdal
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


# Soname should be bumped on API/ABI break
# http://trac.osgeo.org/gdal/ticket/4543
%define soversion 26
%define sourcename gdal
# Uppercase GDAL is the canonical name for this package in Python
%define pypi_package_name GDAL
%bcond_with ecw_support
%bcond_with ecw5_support
%bcond_with fgdb_support
Name:           gdal
Version:        3.0.1
Release:        0
Summary:        GDAL/OGR - a translator library for raster and vector geospatial data formats
License:        MIT AND BSD-3-Clause AND SUSE-Public-Domain
Group:          Development/Libraries/C and C++
URL:            http://www.gdal.org/
Source0:        http://download.osgeo.org/%{name}/%{version}/%{sourcename}-%{version}.tar.xz
Source1:        http://download.osgeo.org/%{name}/%{version}/%{sourcename}-%{version}.tar.xz.md5
Patch0:         gdal-perl.patch
# Fix occasional parallel build failure
Patch1:         GDALmake.opt.in.patch
# PATCH-FIX-UPSTREAM -- https://github.com/OSGeo/gdal/pull/1819
Patch3:         0001-Replace-SWIG-Python-obj0-swig_obj-0-with-version-agn.patch
BuildRequires:  KEALib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  blas-devel
BuildRequires:  chrpath
BuildRequires:  curl-devel
BuildRequires:  dos2unix
BuildRequires:  doxygen >= 1.4.2
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  geos-devel >= 3
BuildRequires:  giflib-devel
BuildRequires:  hdf5-devel
BuildRequires:  lapack-devel
BuildRequires:  libtool
BuildRequires:  mysql-devel
BuildRequires:  opencl-headers
BuildRequires:  perl-ExtUtils-MakeMaker
BuildRequires:  perl-macros
BuildRequires:  pkgconfig
BuildRequires:  python-numpy-devel
BuildRequires:  python-setuptools
BuildRequires:  python3-numpy-devel
BuildRequires:  python3-setuptools
BuildRequires:  swig
BuildRequires:  unixODBC-devel
BuildRequires:  pkgconfig(OpenCL)
BuildRequires:  pkgconfig(freexl)
BuildRequires:  pkgconfig(json)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(expat) >= 1.95.0
BuildRequires:  pkgconfig(libgeotiff) >= 1.2.1
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(libtiff-4) >= 3.6.0
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwebpdecoder)
BuildRequires:  pkgconfig(libwebpdemux)
BuildRequires:  pkgconfig(libwebpmux)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(netcdf)
BuildRequires:  pkgconfig(ocl-icd)
BuildRequires:  pkgconfig(poppler)
BuildRequires:  pkgconfig(proj)
BuildRequires:  pkgconfig(spatialite)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(xerces-c)
BuildRequires:  pkgconfig(zlib) >= 1.1.4
%if %{with fgdb_support}
BuildRequires:  filegdb_api-devel
%endif
%if %{with ecw5_support}
BuildRequires:  ERDAS-ECW_JPEG_2000_SDK-devel
%else
%if %{with ecw_support}
BuildRequires:  libecwj2-devel
%endif
%endif

%description
GDAL is a translator library for raster geospatial data formats that
is released under an Open Source license. As a library, it presents a
single abstract data model to the calling application for all
supported formats. The related OGR library (which lives within the
GDAL source tree) provides a similar capability for simple features
vector data.

%package devel
Summary:        GDAL library header files
Group:          Development/Languages/C and C++
Requires:       lib%{name}%{soversion} = %{version}
Requires:       pkgconfig(libopenjp2)
Provides:       lib%{name}%{soversion}-devel = %{version}
Provides:       lib%{name}-devel = %{version}

%description devel
Development Libraries for the GDAL file format library

%package -n lib%{name}%{soversion}
Summary:        GDAL static libraries
Group:          System/Libraries

%description -n lib%{name}%{soversion}
GDAL and OGR are translator libraries for raster and vector geospatial data
formats. As a library, it presents a single abstract data model to the calling
application for all supported formats.

%package -n perl-%{name}
Summary:        Perl bindings for GDAL
Group:          Development/Languages/Perl
Requires:       %{name} = %{version}-%{release}
%{perl_requires}

%description -n perl-%{name}
Perl bindings for GDAL - Geo::GDAL, Geo::OGR and Geo::OSR modules.

%package -n python2-%{pypi_package_name}
Summary:        GDAL Python module
Group:          Development/Languages/Python
Requires:       %{name} = %{version}-%{release}
# Renaming to uppercase 'GDAL' during 2.4.0; previously used lowercase
Provides:       python2-%{name} = %{version}
Obsoletes:      python2-%{name} < %{version}
Provides:       python-%{name} = %{version}
Obsoletes:      python-%{name} < %{version}

%description -n python2-%{pypi_package_name}
The GDAL python modules provide support to handle multiple GIS file formats.

%package -n python3-%{pypi_package_name}
Summary:        GDAL Python3 module
Group:          Development/Languages/Python
Requires:       %{name} = %{version}-%{release}
Provides:       python3-%{name} = %{version}
Obsoletes:      python3-%{name} < %{version}

%description -n python3-%{pypi_package_name}
The GDAL python modules provide support to handle multiple GIS file formats.

%prep
%setup -q -n %{sourcename}-%{version}
%autopatch -p1

# Set the right (build) libproj.so version, use the upper found version.
PROJSOVER=$(ls -1 %_libdir/libproj.so.?? | tail -n1 | awk -F '.' '{print $3}')
sed -i "s,#  define LIBNAME \"libproj.so\",#  define LIBNAME \"libproj.so.${PROJSOVER}\",g" ogr/ogrct.cpp

# Fix mandir
sed -i "s|^mandir=.*|mandir='\${prefix}/share/man'|" configure

# Fix wrong encoding EOL
for F in frmt_twms_srtm.xml frmt_wms_bluemarble_s3_tms.xml frmt_wms_virtualearth.xml frmt_twms_Clementine.xml;do
  find . -name "${F}" -exec dos2unix {} \;
done

#Fix wrong /usr/bin/env phyton
#Create the move to python3
find . -iname "*.py" -exec sed -i 's,^#!%{_bindir}/env python$,#!%{_bindir}/python3,' {} \;
%if %{with ecw5_support}
# gdal configure script looks for a given layout, so reproduce what is expected.
%if 0%{?suse_version} >= 1500
%define ecw_abi_conf newabi
%else
%define ecw_abi_conf ""
%endif
mkdir -p ../ECW/Desktop_Read-Only/lib/%{ecw_abi_conf}/x64/release/
mkdir -p ../ECW/Desktop_Read-Only/include
cp %{_libdir}/libNCSEcw* ../ECW/Desktop_Read-Only/lib/%{ecw_abi_conf}/x64/release/
cp -r %{_includedir}/{ECW*,NCS*} ../ECW/Desktop_Read-Only/include/
%endif

%build
# need to regenerate (old one does not accept CFLAGS)
autoreconf -fi

%configure \
        --prefix=%{_prefix}     \
        --includedir=%{_includedir}/gdal \
        --datadir=%{_datadir}/gdal \
        --with-threads          \
        --disable-static        \
        --with-geotiff          \
        --with-libtiff          \
        --with-rename-internal-libtiff-symbols=yes \
        --with-rename-internal-libgeotiff-symbols=yes \
        --with-libz             \
        --with-liblzma          \
        --with-cfitsio=no       \
        --with-kea=yes          \
        --with-netcdf           \
        --with-openjpeg         \
        --with-curl             \
        --with-pg               \
        --with-ogdi             \
        --without-pcraster      \
        --with-jpeg12=no        \
        --without-libgrass      \
        --without-grass         \
        --enable-shared         \
        --with-geos             \
        --with-expat            \
        --without-jasper        \
        --with-png              \
        --with-gif              \
        --with-jpeg             \
        --with-spatialite       \
        --with-poppler          \
        --with-python           \
        --with-perl             \
        --with-mysql            \
        --with-freexl           \
        --with-xerces=yes       \
        --with-xerces-lib="-lxerces-c" \
        --with-xerces-inc=%{_includedir}/xercesc \
%if %{with ecw5_support}
        --with-ecw=../ECW/     \
%else
%if %{with ecw_support}
        --with-ecw              \
        CFLAGS="$CFLAGS -pthread" \
%endif
%endif
%if %{with fgdb_support}
       --with-fgdb \
       --with-static-proj4 \
       --with-proj5-api=no \
       CPPFLAGS="$CPPFLAGS -DACCEPT_USE_OF_DEPRECATED_PROJ_API_H" \
%endif
        --with-opencl           \
        --without-hdf4          \
        --with-hdf5             \
        --with-webp             \
        --disable-rpath

# regenerate where needed
for M in perl python;
do
  make %{?_smp_mflags} -C swig/${M} veryclean
  make %{?_smp_mflags} -C swig/${M} generate
done

make %{?_smp_mflags} VERBOSE=1 all docs man

# Make Python 3 module
pushd swig/python
  python3 setup.py build
popd

%install

# Install Python 3 module
# Must be done first so executables are env python
pushd swig/python
  python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
popd

make %{?_smp_mflags} install install-man \
  DESTDIR=%{buildroot} INST_MAN=%{_mandir}

# Not on buildroot : broke everything with python3
# If done got python3 needing python2 package heretic ..
# Futhermore duplicates are only existing in src html dir
%fdupes -s html
# Empty file
rm -f html/do-not-remove

# chrpath must be removed here
chmod 644 %{buildroot}%{perl_vendorarch}/auto/Geo/GDAL/Const/Const.so
chmod 644 %{buildroot}%{perl_vendorarch}/auto/Geo/GDAL/GDAL.so
chmod 644 %{buildroot}%{perl_vendorarch}/auto/Geo/GNM/GNM.so
chmod 644 %{buildroot}%{perl_vendorarch}/auto/Geo/OGR/OGR.so
chmod 644 %{buildroot}%{perl_vendorarch}/auto/Geo/OSR/OSR.so

chrpath --delete %{buildroot}%{perl_vendorarch}/auto/Geo/GDAL/Const/Const.so
chrpath --delete %{buildroot}%{perl_vendorarch}/auto/Geo/GDAL/GDAL.so
chrpath --delete %{buildroot}%{perl_vendorarch}/auto/Geo/GNM/GNM.so
chrpath --delete %{buildroot}%{perl_vendorarch}/auto/Geo/OGR/OGR.so
chrpath --delete %{buildroot}%{perl_vendorarch}/auto/Geo/OSR/OSR.so

# do not ship these
rm -rf %{buildroot}%{_mandir}/man1/_*
rm -rf %{buildroot}%{_libdir}/libgdal.la
rm -rf %{buildroot}%{perl_archlib}/perllocal.pod
rm -rf %{buildroot}%{perl_vendorarch}/auto/Geo/*/.packlist
rm -rf %{buildroot}%{perl_vendorarch}/auto/Geo/GDAL/Const/.packlist
rm -rf %{buildroot}%{_bindir}/*.dox
# License doesn't go there
rm -f %{buildroot}%{_datadir}/gdal/LICENSE.TXT

# avoid PACKAGE redefines
sed -i 's,\(#define PACKAGE_.*\),/* \1 */,' %{buildroot}%{_includedir}/gdal/cpl_config.h

%post -n lib%{name}%{soversion} -p /sbin/ldconfig
%postun	-n lib%{name}%{soversion} -p /sbin/ldconfig

%files -n lib%{name}%{soversion}
%license LICENSE.TXT
%{_libdir}/*.so.%{soversion}.*
%{_libdir}/*.so.%{soversion}

%files
%license LICENSE.TXT
%doc NEWS PROVENANCE.TXT
%{_bindir}/epsg_tr.py
%{_bindir}/esri2wkt.py
%{_bindir}/gcps2vec.py
%{_bindir}/gcps2wld.py
%{_bindir}/gdal2tiles.py
%{_bindir}/gdal2xyz.py
%{_bindir}/gdal_auth.py
%{_bindir}/gdal_calc.py
%{_bindir}/gdal_contour
%{_bindir}/gdal_edit.py
%{_bindir}/gdal_fillnodata.py
%{_bindir}/gdal_grid
%{_bindir}/gdal_merge.py
%{_bindir}/gdal_polygonize.py
%{_bindir}/gdal_proximity.py
%{_bindir}/gdal_pansharpen.py
%{_bindir}/gdal_rasterize
%{_bindir}/gdal_retile.py
%{_bindir}/gdal_sieve.py
%{_bindir}/gdal_translate
%{_bindir}/gdaladdo
%{_bindir}/gdalbuildvrt
%{_bindir}/gdalchksum.py
%{_bindir}/gdalcompare.py
%{_bindir}/gdaldem
%{_bindir}/gdalenhance
%{_bindir}/gdalident.py
%{_bindir}/gdalimport.py
%{_bindir}/gdalinfo
%{_bindir}/gdallocationinfo
%{_bindir}/gdalmanage
%{_bindir}/gdalmove.py
%{_bindir}/gdalserver
%{_bindir}/gdalsrsinfo
%{_bindir}/gdaltindex
%{_bindir}/gdaltransform
%{_bindir}/gdalwarp
%{_bindir}/gnmanalyse
%{_bindir}/gnmmanage
%{_bindir}/mkgraticule.py
%{_bindir}/nearblack
%{_bindir}/ogr2ogr
%{_bindir}/ogrinfo
%{_bindir}/ogrlineref
%{_bindir}/ogrmerge.py
%{_bindir}/ogrtindex
%{_bindir}/pct2rgb.py
%{_bindir}/rgb2pct.py
%{_bindir}/testepsg
%{_datadir}/gdal
%{_mandir}/man1/gdal2tiles.1%{?ext_man}
%{_mandir}/man1/gdal_calc.1%{?ext_man}
%{_mandir}/man1/gdal_contour.1%{?ext_man}
%{_mandir}/man1/gdal_edit.1%{?ext_man}
%{_mandir}/man1/gdal_fillnodata.1%{?ext_man}
%{_mandir}/man1/gdal_grid.1%{?ext_man}
%{_mandir}/man1/gdal_merge.1%{?ext_man}
%{_mandir}/man1/gdal_pansharpen.1%{?ext_man}
%{_mandir}/man1/gdal_polygonize.1%{?ext_man}
%{_mandir}/man1/gdal_proximity.1%{?ext_man}
%{_mandir}/man1/gdal_rasterize.1%{?ext_man}
%{_mandir}/man1/gdal_retile.1%{?ext_man}
%{_mandir}/man1/gdal_sieve.1%{?ext_man}
%{_mandir}/man1/gdal_translate.1%{?ext_man}
%{_mandir}/man1/gdal_utilities.1%{?ext_man}
%{_mandir}/man1/gdaladdo.1%{?ext_man}
%{_mandir}/man1/gdalbuildvrt.1%{?ext_man}
%{_mandir}/man1/gdalcompare.1%{?ext_man}
%{_mandir}/man1/gdaldem.1%{?ext_man}
%{_mandir}/man1/gdalinfo.1%{?ext_man}
%{_mandir}/man1/gdallocationinfo.1%{?ext_man}
%{_mandir}/man1/gdalmanage.1%{?ext_man}
%{_mandir}/man1/gdalmove.1%{?ext_man}
%{_mandir}/man1/gdalsrsinfo.1%{?ext_man}
%{_mandir}/man1/gdaltindex.1%{?ext_man}
%{_mandir}/man1/gdaltransform.1%{?ext_man}
%{_mandir}/man1/gdalwarp.1%{?ext_man}
%{_mandir}/man1/gnm_utilities.1%{?ext_man}
%{_mandir}/man1/gnmanalyse.1%{?ext_man}
%{_mandir}/man1/gnmmanage.1%{?ext_man}
%{_mandir}/man1/nearblack.1%{?ext_man}
%{_mandir}/man1/ogr2ogr.1%{?ext_man}
%{_mandir}/man1/ogr_utilities.1%{?ext_man}
%{_mandir}/man1/ogrinfo.1%{?ext_man}
%{_mandir}/man1/ogrlineref.1%{?ext_man}
%{_mandir}/man1/ogrmerge.1%{?ext_man}
%{_mandir}/man1/ogrtindex.1%{?ext_man}
%{_mandir}/man1/pct2rgb.1%{?ext_man}
%{_mandir}/man1/rgb2pct.1%{?ext_man}

%files devel
%license LICENSE.TXT
%doc NEWS PROVENANCE.TXT
%doc html
%attr(755,root,root) %{_bindir}/gdal-config
%{_libdir}/libgdal.so
%{_libdir}/pkgconfig/gdal.pc
%dir %{_includedir}/gdal
%{_includedir}/gdal/*.h
%{_mandir}/man1/gdal-config.1%{?ext_man}

%files -n perl-%{name}
%license LICENSE.TXT
%doc NEWS PROVENANCE.TXT
%{perl_vendorarch}/Geo/GDAL.pm
%dir %{perl_vendorarch}/Geo/GDAL
%{perl_vendorarch}/Geo/GDAL/Const.pm
%{perl_vendorarch}/Geo/GNM.pm
%{perl_vendorarch}/Geo/OGR.pm
%{perl_vendorarch}/Geo/OSR.pm
%dir %{perl_vendorarch}/Geo
%dir %{perl_vendorarch}/auto/Geo
%dir %{perl_vendorarch}/auto/Geo/GDAL
%attr(755,root,root) %{perl_vendorarch}/auto/Geo/GDAL/GDAL.so
%dir %{perl_vendorarch}/auto/Geo/GDAL/Const
%attr(755,root,root) %{perl_vendorarch}/auto/Geo/GDAL/Const/Const.so
%dir %{perl_vendorarch}/auto/Geo/GNM
%attr(755,root,root) %{perl_vendorarch}/auto/Geo/GNM/GNM.so
%dir %{perl_vendorarch}/auto/Geo/OGR
%attr(755,root,root) %{perl_vendorarch}/auto/Geo/OGR/OGR.so
%dir %{perl_vendorarch}/auto/Geo/OSR
%attr(755,root,root) %{perl_vendorarch}/auto/Geo/OSR/OSR.so
%{_mandir}/man3/Geo::GDAL.3pm%{?ext_man}

%files -n python2-%{pypi_package_name}
%license LICENSE.TXT
%doc NEWS PROVENANCE.TXT
%{python_sitearch}/*

%files -n python3-%{pypi_package_name}
%license LICENSE.TXT
%doc NEWS PROVENANCE.TXT
%{python3_sitearch}/*

%changelog
