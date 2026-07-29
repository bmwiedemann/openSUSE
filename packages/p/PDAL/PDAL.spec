#
# spec file for package PDAL
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define soname 20
%define sovers 20.2.0
%define lname   pdal
%define test_timeout 60
# Big C++ tree -- ninja parallelises it noticeably better than make
%define __builder ninja
Name:           PDAL
Version:        2.10.2
Release:        0
Summary:        Point Data Abstraction Library (GDAL for point cloud data)
# The code is licensed BSD except for:
# - filters/private/csf/* and plugins/i3s/lepcc/* are Apache-2.0
# - vendor/arbiter/*, plugins/nitf/io/nitflib.h and plugins/oci/io/OciWrapper.* are Expat/MIT
# - plugins/e57/io/{src,include}/* is BSD-3-Clause
# - plugins/e57/libE57Format/{src,include}/* is Boost 1-0
License:        Apache-2.0 AND BSD-3-Clause AND MIT AND BSL-1.0
URL:            https://pdal.org/
Source0:        https://github.com/PDAL/PDAL/releases/download/%{version}/%{name}-%{version}-src.tar.bz2
Source1:        https://github.com/PDAL/PDAL/releases/download/%{version}/%{name}-%{version}-src.tar.bz2.sha256sum
# Unbundle some bundled libraries inspired by Fedora work at
# https://src.fedoraproject.org/rpms/PDAL/blob/rawhide/f/PDAL_unbundle.patch
# Upstream is not interested in this patch/change, so we'll have to keep it around
Patch0:         PDAL_unbundle.patch
# GDAL headers are located in %%{_includedir}/gdal
Patch1:         PDAL-fix-gdal-includes.patch
BuildRequires:  bash-completion
BuildRequires:  cmake >= 3.13
BuildRequires:  curl-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++ >= 11
BuildRequires:  gdal >= 3.8
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libgdal-devel
BuildRequires:  libgeos-devel
# PDAL itself never asks for BLAS, but it is pulled in transitively (via gdal)
# and the test binaries then link libopenblas.so.0. Only an openblas -devel
# provides that unflavored soname link -- without it every one of the 143
# ctest binaries dies with "cannot open shared object file" and, because
# %%check is non-fatal, the build still goes green with an empty test run.
BuildRequires:  libopenblas_pthreads-devel
BuildRequires:  libspatialindex-devel
BuildRequires:  ninja
BuildRequires:  nlohmann_json-devel
BuildRequires:  pkgconfig
BuildRequires:  proj
BuildRequires:  python3-devel
BuildRequires:  cmake(GTest)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cunit)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(glut)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libcrypto) >= 1.1
BuildRequires:  pkgconfig(libgeotiff)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(libssl) >= 1.1
BuildRequires:  pkgconfig(libtiff-4)
# We don't have it yet
# BuildRequires:  pointcloud-devel
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(proj)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
# Needed for documentation but we don't build it (see comment below make_build)
# BuildRequires:  dblatex
# BuildRequires:  doxygen
# BuildRequires:  python3-docutils
# BuildRequires:  python3-Sphinx
# BuildRequires:  python3-breathe
# For doc but only in TW
# %%if 0%%{?suse_version} > 1550
# BuildRequires:  python3-sphinxcontrib-breathe
# %%endif
Requires:       lib%{name}%{soname} = %{version}
Provides:       pdal = %{version}
# https://github.com/connormanning/arbiter bundled in vendor/arbiter
Provides:       bundled(arbiter)
# https://github.com/mkazhdan/PoissonRecon bundled in vendor/kazhdan
Provides:       bundled(PoissonRecon)
# https://github.com/jlblancoc/nanoflann bundled in vendor/nanoflann
Provides:       bundled(nanoflann)

%description
PDAL is a C++ BSD library for translating and manipulating point cloud data.
It is very much like the GDAL library which handles raster and vector data.

In addition to the library code, PDAL provides a suite of command-line
applications that users can conveniently use to process, filter, translate,
and query point cloud data. See Applications for more information.

This package provides tools & utilities using PDAL library libpdal

%package -n lib%{name}%{soname}
Summary:        Point Data Abstraction Library (GDAL for point cloud data)

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
Requires:       cmake
Requires:       lib%{name}%{soname} = %{version}
Requires:       libboost_filesystem-devel
Requires:       libboost_headers-devel
Requires:       libboost_program_options-devel
Requires:       pkgconfig(liblzma)
Requires:       pkgconfig(zlib)
Provides:       lib%{lname}%{soname}-devel = %{version}
Provides:       lib%{name}%{soname}-devel = %{version}
Provides:       lib%{name}-devel
Provides:       libpdal-devel

%description devel
This package provides the headers files and tools you may need to
develop applications using PDAL.

%package doc
Summary:        Documentation, examples and demos for PDAL
BuildArch:      noarch

%description doc
This package provides the documentation and sources of examples and data demos of
PDAL algorithms.

%prep
%autosetup -p1 -n %{name}-%{version}-src
# Remove vendored eigen3 library
rm -rf vendor/eigen
# Fix all wrong shebang and move to python3 only
find . -type f -iname "*.py" -exec sed -i 's,^#!%{_bindir}/env python$,#!%{_bindir}/python3,' {} +

# Cleanup spurious perms in documentation
find ./doc/ -type f -exec chmod -v 0644 {} +
find ./doc/ -type f -iname "*.orig" -o -iname ".gitignore" -delete
find ./doc/ -type f -iname "*.ai" -delete

%build
%ifarch ppc64le
# boo#1194109 and upstream https://gcc.gnu.org/bugzilla/show_bug.cgi?id=102059
%define _lto_cflags %{nil}
%endif

# Note on -DBUILD_DOCS=OFF: doc building via cmake requires jupyter-book, which
# is not packaged

%cmake \
    -DCMAKE_VERBOSE_MAKEFILE=ON  \
    -DCMAKE_MODULE_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now" \
    -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now" \
    -DLIB_INSTALL_DIR=%{_libdir} \
    -DINCLUDE_INSTALL_DIR=%{_includedir} \
    -DENABLE_CTEST=ON \
    -DWITH_TESTS=ON \
    -DUSE_EXTERNAL_GTEST_DEFAULT=ON \
    -DUSE_EXTERNAL_GTEST=ON \
    -DWITH_COMPLETION=ON \
    -DWITH_LZMA=ON \
    -DPOSTGRESQL_INCLUDE_DIR=%{_includedir}/pgsql \
    -DGEOTIFF_INCLUDE_DIR=%{_includedir}/libgeotiff \
    -DBUILD_SHARED_LIBS=ON \
    -DWITH_BACKTRACE=ON \
    -DWITH_GCS=ON \
    -DBUILD_TOOLS_LASDUMP=ON \
    -DBUILD_PLUGIN_PGPOINTCLOUD=ON \
    -DBUILD_PLUGIN_GREYHOUND=OFF \
    -DBUILD_PLUGIN_PCL=OFF \
    -DBUILD_PLUGIN_CPD=OFF \
    -DBUILD_PLUGIN_DRACO=OFF \
    -DBUILD_PLUGIN_ICEBRIDGE=OFF \
    -DBUILD_PLUGIN_HDF=OFF \
    -DBUILD_PLUGIN_MATLAB=OFF \
    -DBUILD_PLUGIN_NITF=OFF \
    -DBUILD_PLUGIN_OPENSCENEGRAPH=OFF \
    -DBUILD_PLUGIN_RIVLIB=OFF \
    -DBUILD_PLUGIN_RDBLIB=OFF \
    -DBUILD_PLUGIN_MBIO=OFF \
    -DBUILD_PLUGIN_FBX=OFF \
    -DBUILD_PLUGIN_TEASER=OFF \
    -DBUILD_PLUGIN_TILEDB=OFF \
    -DBUILD_PLUGIN_TRAJECTORY=OFF \
    -DBUILD_PLUGIN_E57=OFF \
    -DBUILD_PLUGIN_ARROW=OFF \
    -DBUILD_PLUGIN_SPZ=OFF \
    -DBUILD_TOOLS_NITFWRAP=OFF \
    -DWITH_ABSEIL=OFF \
    -DBUILD_PGPOINTCLOUD_TESTS=OFF \
    -DBUILD_DOCS=OFF \
    ..

%cmake_build
# Building the docs requires jupyter-book, which is not packaged
# make doxygen html man pdf

%install
%cmake_install

# No executable hpp-Files
find %{buildroot} -type f -name "*.hpp" -executable -exec chmod -x '{}' \;
# No executable cmake-Files
find %{buildroot} -type f -name "*.cmake" -executable -exec chmod -x '{}' \;

# No .la / static libs.  The parentheses matter: `-name a -o -name b -delete`
# binds as `a OR (b AND delete)`, which silently left every *.la in place.
find %{buildroot} -type f \( -name "*.la" -o -name "*.a" \) -delete -print

%fdupes %{buildroot}/%{_prefix}
%fdupes -s doc

# Strange the @PDAL_CONFIG_LIBRARY_DIRS@ is wrongly expanded /usr//usr/lib64/ in PDALConfig.cmake
sed -i 's,%{_prefix}/%{_prefix}/lib64,%{_libdir},g' %{buildroot}/%{_libdir}/cmake/PDAL/PDALConfig.cmake

# WIP pgpointcloud test need a complete running pg server
#%%check
#pushd build
#export LD_LIBRARY_PATH=%%{buildroot}/%%{_libdir}:${LD_LIBRARY_PATH}
#export PDAL_DRIVER_PATH=%%{buildroot}/%%{_libdir}:${PDAL_DRIVER_PATH}
#export GDAL_DATA=/usr/share/gdal/
#ctest -V
#popd

%check
# Custom 60s timeout: some tests otherwise run to the ~20 minute default.
# Failures are reported but do not fail the build -- upstream issue 3501
# still has tests failing on several architectures. The result is read from
# the log rather than gated, which is why --output-on-failure is on.
# The PG tests stay off (BUILD_PGPOINTCLOUD_TESTS=OFF): they need a live
# PostgreSQL server, which a build root does not have.
%ctest --output-on-failure --timeout %{test_timeout} || :

%ldconfig_scriptlets -n lib%{name}%{soname}

%files
%license LICENSE.txt
%{_bindir}/pdal

%files -n lib%{name}%{soname}
%license LICENSE.txt
%doc README.md
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
%doc README.md CONTRIBUTING.md
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
