#
# spec file for package PDAL
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2021 Friedmann Bruno, Ioda-Net Sàrl, Charmoille, Switzerland.
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


%define soname 18
%define sovers 18.0.0
%define lname   pdal
Name:           PDAL
Version:        2.8.2
Release:        0
Summary:        Point Data Abstraction Library (GDAL for point cloud data)
# The code is licensed BSD except for:
# - filters/private/csf/* and plugins/i3s/lepcc/* are Apache-2.0
# - vendor/arbiter/*, plugins/nitf/io/nitflib.h and plugins/oci/io/OciWrapper.* are Expat/MIT
# - plugins/e57/io/{src,include}/* is BSD-3-Clause
# - plugins/e57/libE57Format/{src,include}/* is Boost 1-0
License:        Apache-2.0 AND BSD-3-Clause AND MIT AND BSL-1.0
Group:          Productivity/Graphics/CAD
URL:            https://www.pdal.io/
Source0:        https://github.com/PDAL/PDAL/releases/download/%{version}/%{name}-%{version}-src.tar.bz2
Source1:        https://github.com/PDAL/PDAL/releases/download/%{version}/%{name}-%{version}-src.tar.bz2.sha256sum
# Unbundle some bundled libraries inspired by Fedora work at
# https://src.fedoraproject.org/rpms/PDAL/blob/rawhide/f/PDAL_unbundle.patch
# Upstream is not interested in this patch/change, so we'll have to keep it around
Patch0:         PDAL_unbundle.patch
BuildRequires:  bash-completion
BuildRequires:  cairo-devel
BuildRequires:  cmake >= 2.8
BuildRequires:  cunit-devel
BuildRequires:  curl-devel
BuildRequires:  eigen3-devel
BuildRequires:  fdupes
BuildRequires:  freeglut-devel
BuildRequires:  gdal
BuildRequires:  geotiff-devel
BuildRequires:  gtest
BuildRequires:  jsoncpp-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libgdal-devel
BuildRequires:  libgeos-devel
BuildRequires:  libopenssl-devel >= 1.1
BuildRequires:  proj-devel
# Needed to have proj.db for tests
BuildRequires:  libpsl5
BuildRequires:  libspatialindex-devel
BuildRequires:  libtiff-devel
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig
BuildRequires:  proj
# We don't have it yet
# BuildRequires:  pointcloud-devel
BuildRequires:  libunwind-devel
BuildRequires:  libzstd-devel
BuildRequires:  python3-devel
BuildRequires:  sqlite3-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(libpq)
# Needed for documentation but we don't build it.
# BuildRequires:  dblatex
# BuildRequires:  doxygen
# BuildRequires:  python-docutils
# BuildRequires:  python-Sphinx
# BuildRequires:  python3-docutils
# BuildRequires:  python3-Sphinx
# For doc but only in TW
# BuildRequires:  python-sphinxcontrib-breathe
# Doesn't exist on obs BuildRequires:  python3-breathe
Requires:       lib%{name}%{soname} = %{version}
Provides:       pdal = %{version}
# https://github.com/connormanning/arbiter bundled in vendor/arbiter
Provides:       bundled(arbiter)
# https://github.com/mkazhdan/PoissonRecon bundled in vendor/kazhdan
Provides:       bundled(PoissonRecon)
# https://github.com/jlblancoc/nanoflann bundled in vendor/nanoflann
Provides:       bundled(nanoflann)
# https://github.com/nlohmann/json bundled in vendor/nlohmann
Provides:       bundled(nlohmann)
%if 0%{?suse_version} < 1550
BuildRequires:  gcc12-c++
%else
BuildRequires:  gcc-c++ >= 11
%endif

%description
PDAL is a C++ BSD library for translating and manipulating point cloud data.
It is very much like the GDAL library which handles raster and vector data.

In addition to the library code, PDAL provides a suite of command-line
applications that users can conveniently use to process, filter, translate,
and query point cloud data. See Applications for more information.

This package provides tools & utilities using PDAL library libpdal

%package -n lib%{name}%{soname}
Summary:        Point Data Abstraction Library (GDAL for point cloud data)
Group:          System/Libraries

%description -n lib%{name}%{soname}
PDAL is a C++ BSD library for translating and manipulating point cloud data.
It is very much like the GDAL library which handles raster and vector data.

In addition to the library code, PDAL provides a suite of command-line
applications that users can conveniently use to process, filter, translate,
and query point cloud data. See Applications for more information.

PDAL should not be confused with PCL (Point Cloud Library).
PCL is a library specifically designed to provide algorithmic analysis and
modification of point clouds. PDAL provides a limited interface to the PCL's
facilities, but does not in general attempt to duplicate its capabilites.
PDAL is focused more on data access and translation than PCL.

%package bash-completion
Summary:        Bash completion for PDAL
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
This package contain the bash completion command for PDAL.

%package devel
Summary:        Development files and tools for PDAL applications
Group:          Development/Libraries/C and C++
Requires:       cmake
Requires:       lib%{name}%{soname} = %{version}
Requires:       libboost_filesystem-devel
Requires:       libboost_headers-devel
Requires:       libboost_program_options-devel
Requires:       xz-devel
Requires:       zlib-devel
Provides:       lib%{lname}%{soname}-devel = %{version}
Provides:       lib%{name}%{soname}-devel = %{version}
Provides:       lib%{name}-devel
Provides:       libpdal-devel

%description devel
This package provides the headers files and tools you may need to
develop applications using PDAL.

%package doc
Summary:        Documentation, examples and demos for PDAL
Group:          Documentation/Other
BuildArch:      noarch

%description doc
This package provides the documentation and sources of examples and data demos of
PDAL algorithms.

%prep
%autosetup -p1 -n %{name}-%{version}-src
# Remove some bundled libraries	to use system
rm -rf vendor/{eigen,gtest}
# Fix all wrong shebang and move to python3 only
find . -type f -iname "*.py" -exec sed -i 's,^#!%{_bindir}/env python$,#!%{_bindir}/python3,' {} +

#Cleanup spurious perms in documentation
find ./doc/ -type f -exec chmod -v 0644 {} +
find ./doc/ -type f -iname "*.orig" -o -iname ".gitignore" -delete
find ./doc/ -type f -iname "*.ai" -delete

%build
%ifarch ppc64le
# boo#1194109 and upstream https://gcc.gnu.org/bugzilla/show_bug.cgi?id=102059
%define _lto_cflags %{nil}
%endif
%if 0%{?suse_version} < 1550
export CXX=g++-12
%endif

%cmake \
    -DCMAKE_VERBOSE_MAKEFILE=ON  \
    -DCMAKE_MODULE_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now" \
    -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now" \
    -DLIB_INSTALL_DIR=%{_libdir} \
    -DINCLUDE_INSTALL_DIR=%{_includedir} \
    -DENABLE_CTEST=ON \
    -Dgtest_build_tests=OFF \
    -DWITH_TESTS=ON \
    -DWITH_COMPLETION=ON \
    -DWITH_LZMA=ON \
    -DPOSTGRESQL_INCLUDE_DIR=%{_includedir}/pgsql \
    -DGEOTIFF_INCLUDE_DIR=%{_includedir}/libgeotiff \
    -DBUILD_SHARED_LIBS=ON \
    -DNUMPY_INCLUDE_DIR=%{_libdir}/python%{py3_ver}/site-packages/numpy \
    -DBUILD_PLUGIN_PYTHON=ON \
    -DBUILD_PLUGIN_SQLITE=ON \
    -DBUILD_PLUGIN_HEXBIN=OFF \
    -DBUILD_PLUGIN_ICEBRIDGE=OFF \
    -DBUILD_PLUGIN_NITF=OFF \
    -DBUILD_PLUGIN_PGPOINTCLOUD=ON \
    -DBUILD_PGPOINTCLOUD_TESTS:BOOL=OFF \
    -DBUILD_PLUGIN_GREYHOUND=OFF \
    -DBUILD_PLUGIN_PCL=OFF \
    ..

%make_build
# Make documentation once fixed upstream
# make doxygen html man pdf

%install
%cmake_install

# No executable hpp-Files
find %{buildroot} -type f -name "*.hpp" -executable -exec chmod -x '{}' \;
# No executable cmake-Files
find %{buildroot} -type f -name "*.cmake" -executable -exec chmod -x '{}' \;

#No .la lib
find %{buildroot} -type f -name "*.la" -o -name "*.a" -delete -print

%if 0%{?suse_version}
%fdupes %{buildroot}/%{_prefix}
%fdupes -s doc
%endif

# Strange the @PDAL_CONFIG_LIBRARY_DIRS@ is wrongly expanded /usr//usr/lib64/ in PDALConfig.cmake
sed -i 's,/usr//usr/lib64,%{_libdir},g' %{buildroot}/%{_libdir}/cmake/PDAL/PDALConfig.cmake

# WIP pgpointcloud test need a complete running pg server
#%%check
#pushd build
#export LD_LIBRARY_PATH=%%{buildroot}/%%{_libdir}:${LD_LIBRARY_PATH}
#export PDAL_DRIVER_PATH=%%{buildroot}/%%{_libdir}:${PDAL_DRIVER_PATH}
#export GDAL_DATA=/usr/share/gdal/
#ctest -V
#popd

%check
## test the compiled code (see doc/project/testing.rst)
# A custom timeout of 60s is set. This avoids having tests timeout after the default
# timeout (about 20 minutes)
# we skip tests for selected architectures which need upstream fixes
%ifarch armv7hl aarch64 ppc64le s390x
%ctest --output-on-failure --timeout 60 || true
%else
## we skip the PG test (BUILD_PGPOINTCLOUD_TESTS:BOOL=OFF):
# PGUSER=pdal PGPASSWORD=password PGHOST=localhost PGPORT=5432 ctest -V
%ifarch i686
# https://github.com/PDAL/PDAL/issues/3501 should work with PROJ 8.2 and gdal 3.2.3.
%ctest --timeout 60 || :
%else
# https://github.com/PDAL/PDAL/issues/3501
%ctest  --timeout 60 || :
%endif
%endif

%post -n lib%{name}%{soname} -p /sbin/ldconfig

%postun -n lib%{name}%{soname} -p /sbin/ldconfig

%files
%license LICENSE.txt
%{_bindir}/pdal

%files -n lib%{name}%{soname}
%license LICENSE.txt
%doc AUTHORS.txt README.md RELEASENOTES.txt
%{_libdir}/libpdalcpp.so.%{soname}
%{_libdir}/libpdalcpp.so.%{sovers}
# Plugins
%{_libdir}/libpdal_plugin_kernel_fauxplugin.so.%{soname}
%{_libdir}/libpdal_plugin_kernel_fauxplugin.so.%{sovers}
%{_libdir}/libpdal_plugin_reader_pgpointcloud.so.%{soname}
%{_libdir}/libpdal_plugin_reader_pgpointcloud.so.%{sovers}
%{_libdir}/libpdal_plugin_writer_pgpointcloud.so.%{soname}
%{_libdir}/libpdal_plugin_writer_pgpointcloud.so.%{sovers}

%files bash-completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/pdal

%files devel
%license LICENSE.txt
%doc AUTHORS.txt README.md CONTRIBUTING.md
%{_includedir}/pdal
%{_libdir}/libpdalcpp.so
%{_libdir}/libpdal_plugin_kernel_fauxplugin.so
%{_libdir}/libpdal_plugin_reader_pgpointcloud.so
%{_libdir}/libpdal_plugin_writer_pgpointcloud.so
%{_libdir}/pkgconfig/pdal.pc
%{_libdir}/cmake/PDAL
%{_bindir}/pdal-config

%files doc
%doc doc

%changelog
