#
# spec file for package hdf
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


%if 0%{?sles_version}
%define _mvapich2 1
%endif
%if 0%{?suse_version}
%define _openmpi 1
%endif


Name:           hdf
%define libname libhdf
Version:        4.2.11
Release:        0
%define sonum   4
Summary:        Command-line programs for the HDF4 scientific data format
License:        BSD-4-Clause
Group:          Productivity/Scientific/Other
Url:            http://www.hdfgroup.org/products/hdf4/
Source0:        ftp://ftp.hdfgroup.org/HDF/releases/HDF%{version}/src/hdf-%{version}.tar.bz2
Source99:       baselibs.conf
Patch0:         hdf-4.2.9-maxavailfiles.patch
Patch1:         hdf-ppc.patch
Patch2:         hdf-4.2.11-tirpc.diff
Patch4:         hdf-4.2.10-arm.patch
Patch5:         hdf_hdf_util_he_file_c__fix_missing_sentinel.diff
Patch6:         hdf_mdhdf_ncgen_ncgen.y__fix_noreturn_nonvoid.diff
Patch7:         hdf-implict-decl.patch
Patch8:         hdf-return-value.patch
# Fix misc errors in test code.
Patch9:         hdf-misc-test.patch
# Fix a strict-aliasing warning.
Patch10:        hdf-strict-aliasing.patch
Patch11:        hdf-aarch64.patch
Patch12:        hdf-s390.patch
# The test for fortestF is failing, causing buildfailures for different platforms. Disable for now.
Patch13:        hdf-disable-fortestF.patch 
Patch14:        hdf-ppc64le.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  bison
BuildRequires:  bzip2
BuildRequires:  cmake >= 2.8.11
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libtirpc-devel
BuildRequires:  zlib-devel
%if 0%{?_openmpi}
BuildRequires:  openmpi-devel
BuildRequires:  openmpi-macros-devel
%endif
%if 0%{?_mvapich2}
BuildRequires:  mvapich2-devel
%endif
%if 0%{?suse_version}
BuildRequires:  gcc-fortran
%else
BuildRequires:  gcc-gfortran
%endif
Requires:       %{libname}%{sonum} = %{version}

%description
HDF4 (also known as HDF) is a library and multi-object file format for
storing and managing data between machines. There are two versions of
HDF technologies that are completely different: HDF4 and HDF5. HDF4 is
the first HDF format.

At its lowest level, HDF4 is a physical file format for storing scientific
data. At its highest level, HDF4 is a collection of utilities and
applications for manipulating, viewing, and analyzing data in HDF4 files.
Between these levels, HDF4 is a software library that provides high-level
APIs and a low-level data interface.

This is the legacy version HDF4.  Although it is still maintained, new
users that are not constrained to using HDF4, should use HDF5 instead.

This package contains utility functions for working with HDF4 files.

%package openmpi
Summary:        Command-line programs for the HDF4 scientific data format
Group:          Productivity/Scientific/Other
Requires:       %{libname}%{sonum}-openmpi = %{version}

%description openmpi
HDF4 (also known as HDF) is a library and multi-object file format for
storing and managing data between machines. There are two versions of
HDF technologies that are completely different: HDF4 and HDF5. HDF4 is
the first HDF format.

At its lowest level, HDF is a physical file format for storing scientific
data. At its highest level, HDF is a collection of utilities and
applications for manipulating, viewing, and analyzing data in HDF files.
Between these levels, HDF is a software library that provides high-level
APIs and a low-level data interface.

This is the legacy version HDF4.  Although it is still maintained, new
users that are not constrained to using HDF4, should use HDF5 instead.

This package contains the openmpi version of utility functions for
working with HDF files.

%package mvapich2
Summary:        Command-line programs for the HDF4 scientific data format
Group:          Productivity/Scientific/Other
Requires:       %{libname}%{sonum}-mvapich2 = %{version}

%description mvapich2
HDF4 (also known as HDF) is a library and multi-object file format for
storing and managing data between machines. There are two versions of
HDF technologies that are completely different: HDF4 and HDF5. HDF4 is
the first HDF format.

At its lowest level, HDF4 is a physical file format for storing scientific
data. At its highest level, HDF4 is a collection of utilities and
applications for manipulating, viewing, and analyzing data in HDF4 files.
Between these levels, HDF4 is a software library that provides high-level
APIs and a low-level data interface.

This is the legacy version HDF4.  Although it is still maintained, new
users that are not constrained to using HDF4, should use HDF5 instead.

This package contains the mvapich2 version of utility functions for
working with HDF4 files.

%package -n %{libname}%{sonum}
Summary:        Shared libraries for the HDF4 scientific data format
# To avoid unresolvable errors due to multiple providers of the library
Group:          Productivity/Scientific/Other
Provides:       %{libname} = %{version}
Obsoletes:      %{libname} < %{version}

%description -n %{libname}%{sonum}
HDF4 (also known as HDF) is a library and multi-object file format for
storing and managing data between machines. There are two versions of
HDF technologies that are completely different: HDF4 and HDF5. HDF4 is
the first HDF format.

At its lowest level, HDF4 is a physical file format for storing scientific
data. At its highest level, HDF4 is a collection of utilities and
applications for manipulating, viewing, and analyzing data in HDF4 files.
Between these levels, HDF4 is a software library that provides high-level
APIs and a low-level data interface.

This is the legacy version HDF4.  Although it is still maintained, new
users that are not constrained to using HDF4, should use HDF5 instead.

This package contains the HDF4 runtime libraries.

%package -n %{libname}%{sonum}-openmpi
Summary:        Shared libraries for the HDF4 scientific data format
# To avoid unresolvable errors due to multiple providers of the library
Group:          Productivity/Scientific/Other
Provides:       %{libname}-openmpi = %{version}
Obsoletes:      %{libname}-openmpi < %{version}

%description -n %{libname}%{sonum}-openmpi
HDF4 (also known as HDF) is a library and multi-object file format for
storing and managing data between machines. There are two versions of
HDF technologies that are completely different: HDF4 and HDF5. HDF4 is
the first HDF format.

At its lowest level, HDF4 is a physical file format for storing scientific
data. At its highest level, HDF4 is a collection of utilities and
applications for manipulating, viewing, and analyzing data in HDF4 files.
Between these levels, HDF4 is a software library that provides high-level
APIs and a low-level data interface.

This is the legacy version HDF4.  Although it is still maintained, new
users that are not constrained to using HDF4, should use HDF5 instead.

This package contains the openmpi version of the HDF4 runtime libraries.

%package -n %{libname}%{sonum}-mvapich2
Summary:        Shared libraries for the HDF4 scientific data format
# To avoid unresolvable errors due to multiple providers of the library
Group:          Productivity/Scientific/Other
Provides:       %{libname}-mvapich2 = %{version}
Obsoletes:      %{libname}-mvapich2 < %{version}

%description -n %{libname}%{sonum}-mvapich2
HDF4 (also known as HDF) is a library and multi-object file format for
storing and managing data between machines. There are two versions of
HDF technologies that are completely different: HDF4 and HDF5. HDF4 is
the first HDF format.

At its lowest level, HDF4 is a physical file format for storing scientific
data. At its highest level, HDF4 is a collection of utilities and
applications for manipulating, viewing, and analyzing data in HDF4 files.
Between these levels, HDF4 is a software library that provides high-level
APIs and a low-level data interface.

This is the legacy version HDF4.  Although it is still maintained, new
users that are not constrained to using HDF4, should use HDF5 instead.

This package contains the mvapich2 version of the HDF4 runtime libraries.

%package devel-data
Summary:        Development data files for %{name}
Group:          Development/Libraries/Other

%description devel-data
HDF4 (also known as HDF) is a library and multi-object file format for
storing and managing data between machines. There are two versions of
HDF technologies that are completely different: HDF4 and HDF5. HDF4 is
the first HDF format.

At its lowest level, HDF4 is a physical file format for storing scientific
data. At its highest level, HDF4 is a collection of utilities and
applications for manipulating, viewing, and analyzing data in HDF4 files.
Between these levels, HDF4 is a software library that provides high-level
APIs and a low-level data interface.

This is the legacy version HDF4.  Although it is still maintained, new
users that are not constrained to using HDF4, should use HDF5 instead.

This package contains generic files needed to create projects that use
any version of HDF4.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname}%{sonum} = %{version}
Requires:       %{name}-devel-data = %{version}
Requires:       libjpeg-devel
Requires:       zlib-devel

%description devel
HDF4 (also known as HDF) is a library and multi-object file format for
storing and managing data between machines. There are two versions of
HDF technologies that are completely different: HDF4 and HDF5. HDF4 is
the first HDF format.

At its lowest level, HDF4 is a physical file format for storing scientific
data. At its highest level, HDF4 is a collection of utilities and
applications for manipulating, viewing, and analyzing data in HDF4 files.
Between these levels, HDF4 is a software library that provides high-level
APIs and a low-level data interface.

This is the legacy version HDF4.  Although it is still maintained, new
users that are not constrained to using HDF4, should use HDF5 instead.

This package contains all files needed to create projects that use HDF4.

%package openmpi-devel
Summary:        Development files for %{name}-openmpi
Group:          Development/Libraries/Parallel
Requires:       %{libname}%{sonum}-openmpi = %{version}
Requires:       %{name}-devel-data = %{version}
Requires:       libjpeg-devel
Requires:       zlib-devel

%description openmpi-devel
HDF4 (also known as HDF) is a library and multi-object file format for
storing and managing data between machines. There are two versions of
HDF technologies that are completely different: HDF4 and HDF5. HDF4 is
the first HDF format.

At its lowest level, HDF4 is a physical file format for storing scientific
data. At its highest level, HDF4 is a collection of utilities and
applications for manipulating, viewing, and analyzing data in HDF4 files.
Between these levels, HDF4 is a software library that provides high-level
APIs and a low-level data interface.

This is the legacy version HDF4.  Although it is still maintained, new
users that are not constrained to using HDF4, should use HDF5 instead.

This package contains all files needed to create projects that use
the openmpi version of HDF4.

%package mvapich2-devel
Summary:        Development files for %{name}-mvapich2
Group:          Development/Libraries/Parallel
Requires:       %{libname}%{sonum}-mvapich2 = %{version}
Requires:       %{name}-devel-data = %{version}
Requires:       libjpeg-devel
Requires:       zlib-devel

%description mvapich2-devel
HDF4 (also known as HDF) is a library and multi-object file format for
storing and managing data between machines. There are two versions of
HDF technologies that are completely different: HDF4 and HDF5. HDF4 is
the first HDF format.

At its lowest level, HDF4 is a physical file format for storing scientific
data. At its highest level, HDF4 is a collection of utilities and
applications for manipulating, viewing, and analyzing data in HDF4 files.
Between these levels, HDF4 is a software library that provides high-level
APIs and a low-level data interface.

This is the legacy version HDF4.  Although it is still maintained, new
users that are not constrained to using HDF4, should use HDF5 instead.

This package contains all files needed to create projects that use
the mvapich2 version of HDF4.

%package devel-static
Summary:        Static development files for %{name}
Group:          Development/Libraries/Other
Requires:       %{name}-devel = %{version}

%description devel-static
HDF4 (also known as HDF) is a library and multi-object file format for
storing and managing data between machines. There are two versions of
HDF technologies that are completely different: HDF4 and HDF5. HDF4 is
the first HDF format.

At its lowest level, HDF4 is a physical file format for storing scientific
data. At its highest level, HDF4 is a collection of utilities and
applications for manipulating, viewing, and analyzing data in HDF4 files.
Between these levels, HDF4 is a software library that provides high-level
APIs and a low-level data interface.

This is the legacy version HDF4.  Although it is still maintained, new
users that are not constrained to using HDF4, should use HDF5 instead.

This package provides the static libraries for HDF4.

%package openmpi-devel-static
Summary:        Static development files for %{name}-openmpi
Group:          Development/Libraries/Parallel
Requires:       %{name}-openmpi-devel = %{version}

%description openmpi-devel-static
HDF4 (also known as HDF) is a library and multi-object file format for
storing and managing data between machines. There are two versions of
HDF technologies that are completely different: HDF4 and HDF5. HDF4 is
the first HDF format.

At its lowest level, HDF4 is a physical file format for storing scientific
data. At its highest level, HDF4 is a collection of utilities and
applications for manipulating, viewing, and analyzing data in HDF4 files.
Between these levels, HDF4 is a software library that provides high-level
APIs and a low-level data interface.

This is the legacy version HDF4.  Although it is still maintained, new
users that are not constrained to using HDF4, should use HDF5 instead.

This package provides the static libraries for the openmpi version of HDF4.


%package mvapich2-devel-static
Summary:        Static development files for %{name}-mvapich2
Group:          Development/Libraries/Parallel
Requires:       %{name}-mvapich2-devel = %{version}

%description mvapich2-devel-static
HDF4 (also known as HDF) is a library and multi-object file format for
storing and managing data between machines. There are two versions of
HDF technologies that are completely different: HDF4 and HDF5. HDF4 is
the first HDF format.

At its lowest level, HDF4 is a physical file format for storing scientific
data. At its highest level, HDF4 is a collection of utilities and
applications for manipulating, viewing, and analyzing data in HDF4 files.
Between these levels, HDF4 is a software library that provides high-level
APIs and a low-level data interface.

This is the legacy version HDF4.  Although it is still maintained, new
users that are not constrained to using HDF4, should use HDF5 instead.

This package provides the static libraries for the mvapich2 version of HDF4.


%prep
%setup -q
%patch0 -p1 -b .maxavailfiles
%patch1 -p1
%patch2 -p0
%patch4 -p0 -b .arm
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9
%patch10
%patch11 -p1
%patch12 -p0
%patch13 -p1
%patch14 -p1

%define _mpi %{?_openmpi:%(grep openmpi_prefix  /etc/rpm/macros.openmpi | sed -E 's|.*gcc/(openmpi.*)|\\1|')} %{?_mvapich2:mvapich2}

for mpi in %_mpi;
do
mkdir build_$mpi
mkdir build_static_$mpi
done
mkdir build_static

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
for mpi in %_mpi;
do
# parallel static library
pushd build_static_$mpi
export CC="%{_libdir}/mpi/gcc/$mpi/bin/mpicc"
export CXX="%{_libdir}/mpi/gcc/$mpi/bin/mpic++"
export FC="%{_libdir}/mpi/gcc/$mpi/bin/mpif90"
export F77="%{_libdir}/mpi/gcc/$mpi/bin/mpif77"
export LD_LIBRARY_PATH="%{_libdir}/mpi/gcc/$mpi/%{_lib}"
cmake .. \
    -DCMAKE_INSTALL_PREFIX:PATH=%{_libdir}/mpi/gcc/$mpi \
    -DHDF4_INSTALL_LIB_DIR:PATH=%{_libdir}/mpi/gcc/$mpi/%{_lib} \
    -DHDF4_INSTALL_BIN_DIR:PATH=%{_libdir}/mpi/gcc/$mpi/bin \
    -DHDF4_INSTALL_TOOLS_BIN_DIR:PATH=%{_libdir}/mpi/gcc/$mpi/bin \
    -DHDF4_INSTALL_UTILS_BIN_DIR:PATH=%{_libdir}/mpi/gcc/$mpi/bin \
    -DHDF4_INSTALL_INCLUDE_DIR:PATH=%{_libdir}/mpi/gcc/$mpi/include \
    -DHDF4_INSTALL_DATA_DIR:PATH=%{_libdir}/mpi/gcc/$mpi/share \
    -DHDF4_INSTALL_CMAKE_DIR:PATH=%{_libdir}/mpi/gcc/$mpi/share/cmake/Modules/ \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_C_COMPILER:PATH=%{_libdir}/mpi/gcc/$mpi/bin/mpicc \
    -DCMAKE_C_FLAGS="${CFLAGS:-%optflags} -DNDEBUG" \
    -DCMAKE_CXX_COMPILER:PATH=%{_libdir}/mpi/gcc/$mpi/bin/mpic++ \
    -DCMAKE_CXX_FLAGS="${CXXFLAGS:-%optflags} -DNDEBUG" \
    -DCMAKE_Fortran_FLAGS="${FFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}} -DNDEBUG" \
    -DCMAKE_EXE_LINKER_FLAGS="-Wl,--as-needed -Wl,--no-undefined -Wl,-z,now -ltirpc" \
    -DCMAKE_MODULE_LINKER_FLAGS="-Wl,--as-needed -Wl,--no-undefined -Wl,-z,now -ltirpc" \
    -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,--no-undefined -Wl,-z,now -ltirpc" \
    -DCMAKE_SKIP_RPATH:BOOL=ON \
    -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DBUILD_STATIC_LIBS:BOOL=ON \
    -DCMAKE_COLOR_MAKEFILE:BOOL=OFF \
    -DCMAKE_INSTALL_DO_STRIP:BOOL=OFF \
    -DCMAKE_BUILD_TYPE:STRING=Release  \
    -DHDF4_BUILD_TOOLS:BOOL=OFF \
    -DHDF4_BUILD_UTILS:BOOL=OFF \
    -DHDF4_ENABLE_NETCDF:BOOL=OFF \
    -DBUILD_TESTING:BOOL=ON \
    -DHDF4_ENABLE_PARALLEL:BOOL=ON \
%if "%{?_lib}" == "lib64"
    -DLIB_SUFFIX=64
%endif

make %{?_smp_mflags}
popd

# parallel shared library
pushd build_$mpi
export CC="%{_libdir}/mpi/gcc/$mpi/bin/mpicc"
export CXX="%{_libdir}/mpi/gcc/$mpi/bin/mpic++"
export FC="%{_libdir}/mpi/gcc/$mpi/bin/mpif90"
export F77="%{_libdir}/mpi/gcc/$mpi/bin/mpif77"
export LD_LIBRARY_PATH="%{_libdir}/mpi/gcc/$mpi/%{_lib}"
cmake .. \
    -DCMAKE_INSTALL_PREFIX:PATH=%{openmpi_prefix} \
    -DHDF4_INSTALL_LIB_DIR:PATH=%{_libdir}/mpi/gcc/$mpi/%{_lib} \
    -DHDF4_INSTALL_BIN_DIR:PATH=%{_libdir}/mpi/gcc/$mpi/bin \
    -DHDF4_INSTALL_TOOLS_BIN_DIR:PATH=%{_libdir}/mpi/gcc/$mpi/bin \
    -DHDF4_INSTALL_UTILS_BIN_DIR:PATH=%{_libdir}/mpi/gcc/$mpi/bin \
    -DHDF4_INSTALL_INCLUDE_DIR:PATH=%{_libdir}/mpi/gcc/$mpi/include \
    -DHDF4_INSTALL_DATA_DIR:PATH=%{_libdir}/mpi/gcc/$mpi/share \
    -DHDF4_INSTALL_CMAKE_DIR:PATH=%{_libdir}/mpi/gcc/$mpi/share/cmake/Modules/ \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_C_COMPILER:PATH=%{_libdir}/mpi/gcc/$mpi/bin/mpicc \
    -DCMAKE_C_FLAGS="${CFLAGS:-%optflags} -DNDEBUG" \
    -DCMAKE_CXX_COMPILER:PATH=%{_libdir}/mpi/gcc/$mpi/bin/mpic++ \
    -DCMAKE_CXX_FLAGS="${CXXFLAGS:-%optflags} -DNDEBUG" \
    -DCMAKE_Fortran_FLAGS="${FFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}} -DNDEBUG" \
    -DCMAKE_EXE_LINKER_FLAGS="-Wl,--as-needed -Wl,--no-undefined -Wl,-z,now -ltirpc" \
    -DCMAKE_MODULE_LINKER_FLAGS="-Wl,--as-needed -Wl,--no-undefined -Wl,-z,now -ltirpc" \
    -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,--no-undefined -Wl,-z,now -ltirpc" \
    -DCMAKE_SKIP_RPATH:BOOL=ON \
    -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DBUILD_STATIC_LIBS:BOOL=OFF \
    -DCMAKE_COLOR_MAKEFILE:BOOL=OFF \
    -DCMAKE_INSTALL_DO_STRIP:BOOL=OFF \
    -DCMAKE_BUILD_TYPE:STRING=Release  \
    -DHDF4_BUILD_TOOLS:BOOL=ON \
    -DHDF4_BUILD_UTILS:BOOL=ON \
    -DHDF4_ENABLE_NETCDF:BOOL=OFF \
    -DBUILD_TESTING:BOOL=ON \
    -DHDF4_ENABLE_PARALLEL:BOOL=ON \
%if "%{?_lib}" == "lib64"
    -DLIB_SUFFIX=64
%endif

make %{?_smp_mflags}
popd
done

# non-parallel static library
pushd build_static
cmake .. \
    -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
    -DHDF4_INSTALL_LIB_DIR:PATH=%{_libdir} \
    -DHDF4_INSTALL_BIN_DIR:PATH=%{_binddir} \
    -DHDF4_INSTALL_TOOLS_BIN_DIR:PATH=%{_bindir} \
    -DHDF4_INSTALL_UTILS_BIN_DIR:PATH=%{_binddir} \
    -DHDF4_INSTALL_INCLUDE_DIR:PATH=%{_includedir} \
    -DHDF4_INSTALL_DATA_DIR:PATH=%{_datadir} \
    -DHDF4_INSTALL_CMAKE_DIR:PATH=%{_datadir}/cmake/Modules/ \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_C_FLAGS="${CFLAGS:-%optflags} -DNDEBUG" \
    -DCMAKE_CXX_FLAGS="${CXXFLAGS:-%optflags} -DNDEBUG" \
    -DCMAKE_Fortran_FLAGS="${FFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}} -DNDEBUG" \
    -DCMAKE_EXE_LINKER_FLAGS="-Wl,--as-needed -Wl,--no-undefined -Wl,-z,now -ltirpc" \
    -DCMAKE_MODULE_LINKER_FLAGS="-Wl,--as-needed -Wl,--no-undefined -Wl,-z,now -ltirpc" \
    -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,--no-undefined -Wl,-z,now -ltirpc" \
    -DCMAKE_SKIP_RPATH:BOOL=ON \
    -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DBUILD_STATIC_LIBS:BOOL=ON \
    -DCMAKE_COLOR_MAKEFILE:BOOL=OFF \
    -DCMAKE_INSTALL_DO_STRIP:BOOL=OFF \
    -DCMAKE_BUILD_TYPE:STRING=Release  \
    -DHDF4_BUILD_TOOLS:BOOL=OFF \
    -DHDF4_BUILD_UTILS:BOOL=OFF \
    -DHDF4_ENABLE_NETCDF:BOOL=OFF \
    -DBUILD_TESTING:BOOL=ON \
    -DHDF4_ENABLE_PARALLEL:BOOL=ON \
%if "%{?_lib}" == "lib64"
    -DLIB_SUFFIX=64
%endif

make %{?_smp_mflags}
popd
# Non-parallel shared library
%cmake  -DHDF4_INSTALL_LIB_DIR:PATH=%{_libdir} \
        -DHDF4_INSTALL_DATA_DIR:PATH=%{_datadir} \
        -DHDF4_INSTALL_CMAKE_DIR:PATH=%{_datadir}/cmake/Modules/ \
        -DHDF4_INSTALL_BIN_DIR:PATH=%{_bindir} \
        -DHDF4_INSTALL_TOOLS_BIN_DIR:PATH=%{_bindir} \
        -DHDF4_INSTALL_UTILS_BIN_DIR:PATH=%{_bindir} \
        -DHDF4_INSTALL_INCLUDE_DIR:PATH=%{_includedir} \
        -DCMAKE_BUILD_TYPE:STRING=Release  \
        -DBUILD_SHARED_LIBS:BOOL=ON \
        -DBUILD_STATIC_LIBS:BOOL=OFF \
        -DHDF4_BUILD_TOOLS:BOOL=ON \
        -DHDF4_BUILD_UTILS:BOOL=ON \
        -DHDF4_ENABLE_NETCDF:BOOL=OFF \
        -DBUILD_TESTING:BOOL=ON \
        -DHDF4_ENABLE_PARALLEL:BOOL=OFF
make %{?_smp_mflags}
cd ..

%install
for mpi in %_mpi;
do
make VERBOSE=1 DESTDIR=%{buildroot} install/fast -C build_static_$mpi
make VERBOSE=1 DESTDIR=%{buildroot} install/fast -C build_$mpi
done
make VERBOSE=1 DESTDIR=%{buildroot} install/fast -C build_static
%cmake_install

# Add sonum library versions
for file in libhdf libhdf_fcstub libhdf_fortran libmfhdf libmfhdf_fcstub libmfhdf_fortran; do
  ln -s %{_libdir}/${file}.so.%{version} %{buildroot}%{_libdir}/${file}.so.%{sonum}
  for mpi in %_mpi; do
    ln -s %{_libdir}/mpi/gcc/$mpi/%{_lib}/${file}.so.%{version} %{buildroot}%{_libdir}/mpi/gcc/$mpi/%{_lib}/${file}.so.%{sonum}
  done
done
for file in ncdump ncgen; do
  mv %{buildroot}%{_bindir}/$file %{buildroot}%{_bindir}/h$file
  for mpi in %_mpi; do
      mv %{buildroot}%{_libdir}/mpi/gcc/$mpi/bin/$file %{buildroot}%{_libdir}/mpi/gcc/$mpi/bin/h$file
  done
done

# Add df versions of libraries
for file in df df_fcstub df_fortran; do
  ln -s %{_libdir}/libh${file}.a %{buildroot}%{_libdir}/lib${file}.a
  ln -s %{_libdir}/libh${file}.so %{buildroot}%{_libdir}/lib${file}.so
  ln -s %{_libdir}/libh${file}.so.%{sonum} %{buildroot}%{_libdir}/lib${file}.so.%{sonum}
  ln -s %{_libdir}/libh${file}.so.%{version} %{buildroot}%{_libdir}/lib${file}.so.%{version}
  for mpi in %_mpi; do
    ln -s %{_libdir}/mpi/gcc/$mpi/%{_lib}/libh${file}.a %{buildroot}%{_libdir}/mpi/gcc/$mpi/%{_lib}/lib${file}.a
    ln -s %{_libdir}/mpi/gcc/$mpi/%{_lib}/libh${file}.so %{buildroot}%{_libdir}/mpi/gcc/$mpi/%{_lib}/lib${file}.so
    ln -s %{_libdir}/mpi/gcc/$mpi/%{_lib}/libh${file}.so.%{sonum} %{buildroot}%{_libdir}/mpi/gcc/$mpi/%{_lib}/lib${file}.so.%{sonum}
    ln -s %{_libdir}/mpi/gcc/$mpi/%{_lib}/libh${file}.so.%{version} %{buildroot}%{_libdir}/mpi/gcc/$mpi/%{_lib}/lib${file}.so.%{version}
  done
done

# Remove duplicate documentation
for file in COPYING RELEASE.txt USING_HDF4_CMake.txt; do
  rm %{buildroot}%{_datadir}/$file
  for mpi in %_mpi; do
    rm %{buildroot}%{_libdir}/mpi/gcc/$mpi/share/$file
  done
done

# remove unneeded headers
for hname in alloc.h error.h glist.h hqueue.h mcache.h netcdf.inc vgint.h; do
  rm %{buildroot}%{_includedir}/$hname
  for mpi in %_mpi; do
    rm %{buildroot}%{_libdir}/mpi/gcc/$mpi/include/$hname
  done
done

# rpm macro for version checking
mkdir -p %{buildroot}%{_sysconfdir}/rpm
cat > %{buildroot}%{_sysconfdir}/rpm/macros.hdf <<EOF
#
# RPM macros for hdf5 packaging
#
%_hdf_sonum  %{sonum}
%_hdf_version  %{version}
EOF

# One fortran test fails under ppc64, s390 and aarch64
%check
for mpi in %_mpi; do
pushd build_static_$mpi
LD_LIBRARY_PATH=%{_libdir}/mpi/gcc/$mpi/%{_lib}:%{_builddir}/%{name}-%{version}/build_$mpi/bin:$LD_LIBRARY_PATH ctest --output-on-failure --force-new-ctest-process %{?_smp_mflags}
popd
pushd build_$mpi
LD_LIBRARY_PATH=%{_libdir}/mpi/gcc/$mpi/%{_lib}:%{_builddir}/%{name}-%{version}/build_$mpi/bin:$LD_LIBRARY_PATH ctest --output-on-failure --force-new-ctest-process %{?_smp_mflags}
popd
done
pushd build_static
LD_LIBRARY_PATH=%{buildroot}%{_libdir}:%{_builddir}/%{name}-%{version}/build/bin:$LD_LIBRARY_PATH ctest --output-on-failure --force-new-ctest-process %{?_smp_mflags}
popd
pushd build
LD_LIBRARY_PATH=%{buildroot}%{_libdir}:%{_builddir}/%{name}-%{version}/build/bin:$LD_LIBRARY_PATH ctest --output-on-failure --force-new-ctest-process %{?_smp_mflags}
popd

%post -n %{libname}%{sonum} -p /sbin/ldconfig
%postun -n %{libname}%{sonum} -p /sbin/ldconfig

%if 0%{?_openmpi}
%post -n %{libname}%{sonum}-openmpi -p /sbin/ldconfig
%postun -n %{libname}%{sonum}-openmpi -p /sbin/ldconfig
%endif

%if 0%{?_mvapich2}
%post -n %{libname}%{sonum}-mvapich2 -p /sbin/ldconfig
%postun -n %{libname}%{sonum}-mvapich2 -p /sbin/ldconfig
%endif

%files
%{_bindir}/*

%files -n %{libname}%{sonum}
%license COPYING
%doc MANIFEST README.txt release_notes/bugs_fixed.txt release_notes/HISTORY.txt release_notes/misc_docs.txt release_notes/RELEASE.txt
%{_libdir}/*.so.*

%files devel-data
%config(noreplace) %{_sysconfdir}/rpm/macros.hdf

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_datadir}/cmake/Modules/hdf4/

%files devel-static
%{_libdir}/*.a

%if 0%{?_openmpi}
%files openmpi
%{openmpi_prefix}/bin/*

%files -n %{libname}%{sonum}-openmpi
%license COPYING
%doc MANIFEST README.txt release_notes/bugs_fixed.txt release_notes/HISTORY.txt release_notes/misc_docs.txt release_notes/RELEASE.txt
%{openmpi_prefix}/%{_lib}/*.so.*

%files openmpi-devel
%{openmpi_prefix}/include/*
%{openmpi_prefix}/%{_lib}/*.so
%dir %{openmpi_prefix}/share/cmake/
%dir %{openmpi_prefix}/share/cmake/Modules/
%{openmpi_prefix}/share/cmake/Modules/hdf4/

%files openmpi-devel-static
%{openmpi_prefix}/%{_lib}/*.a
%endif

%if 0%{?_mvapich2}
%files mvapich2
%{_libdir}/mpi/gcc/mvapich2/bin/*

%files -n %{libname}%{sonum}-mvapich2
%license COPYING
%doc MANIFEST README.txt release_notes/bugs_fixed.txt release_notes/HISTORY.txt release_notes/misc_docs.txt release_notes/RELEASE.txt
%{_libdir}/mpi/gcc/mvapich2/%{_lib}/*.so.*

%files mvapich2-devel
%{_libdir}/mpi/gcc/mvapich2/include/*
%{_libdir}/mpi/gcc/mvapich2/%{_lib}/*.so
%dir %{_libdir}/mpi/gcc/mvapich2/share/cmake/
%dir %{_libdir}/mpi/gcc/mvapich2/share/cmake/Modules/
%{_libdir}/mpi/gcc/mvapich2/share/cmake/Modules/hdf4/

%files mvapich2-devel-static
%{_libdir}/mpi/gcc/mvapich2/%{_lib}/*.a
%endif

%changelog
