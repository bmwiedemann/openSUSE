#
# spec file for package hdf5
#
# Copyright (c) 2025 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}

%bcond_with sz2

%define sonum 310
%define pname hdf5
%bcond_with static

%if %{with static}
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%endif

%if "%{flavor}" == ""
ExclusiveArch:  do_not_build
 %define package_name %pname
%endif

%if "%{flavor}" == "serial"
%endif

%if "%{flavor}" == "openmpi4"
%global mpi_flavor %{flavor}
%endif

%if "%{flavor}" == "openmpi5"
%global mpi_flavor %{flavor}
ExcludeArch:    %{ix86} %{arm}
%endif

%if "%{flavor}" == "mvapich2"
%global mpi_flavor %{flavor}
%endif

%{?mpi_flavor:%{bcond_without mpi}}%{!?mpi_flavor:%{bcond_with mpi}}
%{?with_mpi:%{!?mpi_flavor:error "No MPI family specified!"}}

%if %{without mpi}
 %define my_prefix %_prefix
 %define my_bindir %_bindir
 %define my_libdir %_libdir
 %define my_incdir %_includedir
%else
 %define my_prefix %{_libdir}/mpi/gcc/%{mpi_flavor}
 %define my_suffix -%{mpi_flavor}
 %define my_bindir %{my_prefix}/bin
 %define my_libdir %{my_prefix}/%{_lib}
 %define my_incdir %{my_prefix}/include
%endif
%if 0%{!?package_name:1}
 %define package_name   %pname%{?my_suffix}
%endif
%define libname(l:s:)   lib%{pname}%{!-l:%{-s:-}}%{-l*}%{-s*}%{?my_suffix}
%define vname %{pname}

%define __builder ninja

Name:           %{package_name}
Version:        1.14.6
Release:        0
Summary:        Command-line programs for the HDF5 scientific data format
License:        BSD-3-Clause
Group:          Productivity/Scientific/Other
URL:            https://www.hdfgroup.org/HDF5/
Source0:        https://github.com/HDFGroup/hdf5/releases/download/%{pname}_%{version}/%{pname}-%{version}.tar.gz
Source100:      %{pname}.rpmlintrc
# PATCH-FIX-UPSTREAM hdf5-cmake-fix-script-paths.patch badshah400@gmail.com -- Fix paths in scripts when built using cmake
Patch0:         hdf5-cmake-fix-script-paths.patch
# not really needed but we want to get noticed if hdf5 doesn' t know our host
Patch2:         hdf5-1.8.11-abort_unknown_host_config.patch
%ifarch %arm
Patch4:         hdf5-1.8.10-tests-arm.patch
%endif
Patch5:         PPC64LE-Fix-long-double-handling.patch

BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  hostname
BuildRequires:  ninja
%if %{with sz2}
BuildRequires:  sz2-devel
%endif
BuildRequires:  zlib-devel
%if %{with mpi}
BuildRequires:  %{mpi_flavor}-devel
%else
Requires:       lib%{pname}_cpp%{sonum} = %{version}
Requires:       lib%{pname}_hl_cpp%{sonum} = %{version}
%endif
Requires:       lib%{pname}-%{sonum} = %{version}
Requires:       lib%{pname}_fortran%{sonum} = %{version}
Requires:       lib%{pname}_hl%{sonum} = %{version}
Requires:       lib%{pname}_hl_fortran%{sonum} = %{version}
Requires:       lib%{pname}_tools%{sonum} = %{version}

%description
HDF5 is a data model, library, and file format for storing and
managing data. It supports an unlimited variety of datatypes.

This package contains the %{flavor} version utility functions for working
with HDF5 files.

%package -n     %{libname -s %{sonum}}
Summary:        Shared libraries for the HDF5 scientific data format
# To avoid unresolvable errors due to multiple providers of the library
Group:          System/Libraries
Provides:       %{libname} = %{version}
Obsoletes:      %{libname} < %{version}

%description -n %{libname -s %{sonum}}
HDF5 is a data model, library, and file format for storing and
managing data. It supports an unlimited variety of datatypes.

This package contains the %{flavor} version of the HDF5 runtime libraries.

%package -n     %{libname -l _hl -s %{sonum}}
Summary:        High-level shared libraries for the HDF5 scientific data format
# To avoid unresolvable errors due to multiple providers of the library
Group:          System/Libraries
Provides:       %{libname -l _hl} = %{version}
Obsoletes:      %{libname -l _hl} < %{version}

%description -n %{libname -l _hl -s %{sonum}}
HDF5 is a data model, library, and file format for storing and
managing data. It supports an unlimited variety of datatypes.

This package contains the %{flavor} version of the high-level HDF5
runtime libraries.

%package -n     %{libname -l _cpp -s %{sonum}}
Summary:        Shared libraries for the HDF5 scientific data format
# To avoid unresolvable errors due to multiple providers of the library
Group:          System/Libraries
Provides:       %{libname -l _cpp} = %{version}
Obsoletes:      %{libname -l _cpp} < %{version}

%description -n %{libname -l _cpp -s %{sonum}}
HDF5 is a data model, library, and file format for storing and
managing data. It supports an unlimited variety of datatypes.

This package contains the HDF5 runtime libraries.

%package -n     %{libname -l _hl_cpp -s %{sonum}}
Summary:        High-level shared libraries for the HDF5 scientific data format
# To avoid unresolvable errors due to multiple providers of the library
Group:          System/Libraries
Provides:       %{libname -l _hl_cpp} = %{version}
Obsoletes:      %{libname -l _hl_cpp} < %{version}

%description -n %{libname -l _hl_cpp -s %{sonum}}
HDF5 is a data model, library, and file format for storing and
managing data. It supports an unlimited variety of datatypes.

This package contains the the high-level HDF5 runtime libraries.

%package -n     %{libname -l _fortran -s %{sonum}}
Summary:        Shared libraries for the HDF5 scientific data format
# To avoid unresolvable errors due to multiple providers of the library
Group:          System/Libraries
Provides:       %{libname -l _fortran} = %{version}
Obsoletes:      %{libname -l _fortran} < %{version}

%description -n %{libname -l _fortran -s %{sonum}}
HDF5 is a data model, library, and file format for storing and
managing data. It supports an unlimited variety of datatypes.

This package contains the %{flavor} version of the HDF5 runtime libraries.

%package -n     %{libname -l _hl_fortran -s %{sonum}}
Summary:        High-level shared libraries for the HDF5 scientific data format
# To avoid unresolvable errors due to multiple providers of the library
Group:          System/Libraries
Provides:       %{libname -l _hl_fortran} = %{version}
Obsoletes:      %{libname -l _hl_fortran} < %{version}

%description -n %{libname -l _hl_fortran -s %{sonum}}
HDF5 is a data model, library, and file format for storing and
managing data. It supports an unlimited variety of datatypes.

This package contains the %{flavor} version of the high-level HDF5
runtime libraries.

%package -n     %{libname -l _tools -s %{sonum}}
Summary:        Shared libraries for the HDF5 scientific data format
# To avoid unresolvable errors due to multiple providers of the library
Group:          System/Libraries
Provides:       %{libname -l _tools} = %{version}
Obsoletes:      %{libname -l _tools} < %{version}

%description -n %{libname -l _tools -s %{sonum}}
HDF5 is a data model, library, and file format for storing and
managing data. It supports an unlimited variety of datatypes.

This package contains the HDF5 runtime libraries.

%package -n %{pname}-devel-data
Summary:        Development data files for %{name}
Group:          Development/Libraries/Other
BuildArch:      noarch

%description -n %{pname}-devel-data
HDF5 is a data model, library, and file format for storing and
managing data. It supports an unlimited variety of datatypes.

This package contains generic files needed to create projects that use
any version of HDF5.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Parallel
Requires:       %{libname -l _cpp -s %{sonum}} = %{version}
Requires:       %{libname -l _hl_cpp -s %{sonum}} = %{version}
Requires:       %{name} = %{version}
Requires:       %{pname}-devel-data = %{version}
Requires:       zlib-devel
%if 0%{?use_sz2}
Requires:       libsz2-devel
%endif
Requires:       %{libname -s %{sonum}} = %{version}
# Required by Fortran programs?
Requires:       %{libname -l _fortran -s %{sonum}} = %{version}
Requires:       %{libname -l _hl -s %{sonum}} = %{version}
Requires:       %{libname -l _hl_fortran -s %{sonum}} = %{version}
Requires:       %{libname -l _tools -s %{sonum}} = %{version}

%description devel
HDF5 is a data model, library, and file format for storing and
managing data. It supports an unlimited variety of datatypes.

This package contains all files needed to create projects that use
the %{flavor} version of HDF5.

%package  devel-static
Summary:        Static development files for %{name}
Group:          Development/Libraries/Parallel
Requires:       %{name}-devel = %{version}

%description devel-static
HDF5 is a data model, library, and file format for storing and
managing data. It supports an unlimited variety of datatypes.

This package provides the static libraries for the %{flavor} version of HDF5.

%package -n %{vname}-examples
Summary:        Examples for %{name}
Group:          Documentation/Other
BuildArch:      noarch

%description -n %{vname}-examples
HDF5 is a data model, library, and file format for storing and
managing data. It supports an unlimited variety of datatypes.

This package provides examples of HDF5 library use.

%prep
%autosetup -N -n %{pname}-%{version}
%patch -P 0 -p1
%patch -P 2 -p0 -b .abort_unknown_host_config
%ifarch %arm
%patch -P 4 -p0 -b .tests-arm
%endif
%patch -P 5 -p1

# baselibs looks different for different flavors - generate it on the fly
cat > %{_sourcedir}/baselibs.conf << EOF
libhdf5-%{sonum}%{?my_suffix}
libhdf5_hl%{sonum}%{?my_suffix}
libhdf5_fortran%{sonum}%{?my_suffix}
libhdf5hl_fortran%{sonum}%{?my_suffix}
libhdf5_cpp%{sonum}%{?my_suffix}
libhdf5_hl_cpp%{sonum}%{?my_suffix}
libhdf5_tools%{sonum}%{?my_suffix}
hdf5%{?my_suffix}-devel
   requires %{?my_suffix}-<targettype>
   requires "libhdf5-%{sonum}%{?my_suffix}-<targettype> = <version>"
   requires "libhdf5_hl%{sonum}%{?my_suffix}-<targettype> = <version>"
   requires "libhdf5_fortran%{sonum}%{?my_suffix}-<targettype> = <version>"
   requires "libhdf5hl_fortran%{sonum}%{?my_suffix}-<targettype> = <version>"
   requires "libhdf5_cpp%{sonum}%{?my_suffix}-<targettype> = <version>"
   requires "libhdf5_hl_cpp%{sonum}%{?my_suffix}-<targettype> = <version>"
   requires "libhdf5_tools%{sonum}%{?my_suffix}-<targettype> = <version>"
EOF

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export FFLAGS="%{optflags}"
export FCFLAGS="%{optflags}"
%ifarch %arm
# we want to have useful H5_CFLAGS on arm too
test -e config/linux-gnueabi || cp config/linux-gnu config/linux-gnueabi
%endif

# SECTION Tests to disable by regex
## Long lasting tests for MPI
DISABLED_TEST_REGEX="MPI_TEST_t_.*"
## Failing tests on 32bit
%ifarch %ix86
DISABLED_TEST_REGEX+="|FORTRAN_testhdf5_fortran|MPI_TEST_testphdf5"
%endif
## PPC peculiarities
%ifarch %power64
DISABLED_TEST_REGEX+="|MPI_TEST_H5DIFF-h5diff_601"
%endif
%ifarch %arm64
DISABLED_TEST_REGEX+="|MPI_TEST_H5DIFF-h5diff_601"
%endif
export DISABLED_TEST_REGEX
# /SECTION

# NOTE 1: -DALLOW_UNSUPPORTED=ON is required when -DHDF5_BUILD_FORTRAN is
# enabled along with -DHDF5_ENABLE_THREADSAFE=ON.  Building with thise
# combination results in thread-safe C libraries and non-thread-safe fortran
# and/or C++ libraries. So you have to explicitly allow building the
# thread-safe C library and the non-thread-safe C++ and fortran libraries in
# order to make sure people don't assume that their fortran or C++ code is
# thread-safe.  Since our users are going to be accessing this through other
# programs, this doesn't matter.

# NOTE 2: It is absolutely critical to set explicitly the CMAKE_<LANG>_COMPILER
# options for each flavour of build, even for the serial one, especially when
# ccache is used to speed up builds. Otherwise, the scripts `h5(p)cc` and
# libhdf5.settings embed incorrect values of the compiler (e.g. ccache instead
# of gcc) causing major issues downstream.

%cmake \
 %if %{with mpi}
  -DCMAKE_C_COMPILER:FILEPATH="%{my_bindir}/mpicc" \
  -DCMAKE_CXX_COMPILER:FILEPATH="%{my_bindir}/mpicxx" \
  -DCMAKE_Fortran_COMPILER:FILEPATH="%{my_bindir}/mpif90" \
  -DCMAKE_INSTALL_BINDIR:PATH=%{my_bindir} \
  -DCMAKE_INSTALL_INCLUDEDIR:PATH=%{my_incdir} \
  -DCMAKE_INSTALL_LIBDIR:PATH=%{my_libdir} \
  -DCMAKE_INSTALL_PREFIX:PATH=%{my_prefix} \
 %else
  -DCMAKE_C_COMPILER:FILEPATH="%{my_bindir}/cc" \
  -DCMAKE_CXX_COMPILER:FILEPATH="%{my_bindir}/c++" \
  -DCMAKE_Fortran_COMPILER:FILEPATH="%{my_bindir}/gfortran" \
 %endif
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
  -DALLOW_UNSUPPORTED:BOOL=ON \
  -DBUILD_STATIC_LIBS:BOOL=%{?with_static:ON}%{!?with_static:OFF} \
  -DBUILD_TESTING:BOOL=ON \
  -DHDF5_INSTALL_CMAKE_DIR:PATH=%{_lib}/cmake/hdf5 \
  -DHDF5_BUILD_CPP_LIB:BOOL=ON \
  -DHDF5_BUILD_FORTRAN:BOOL=ON \
  -DHDF5_BUILD_HL_GIF_TOOLS:BOOL=OFF \
  -DHDF5_BUILD_HL_LIB:BOOL=ON \
  -DHDF5_BUILD_PARALLEL_TOOLS:BOOL=OFF \
  -DHDF5_BUILD_TOOLS:BOOL=ON \
  -DHDF5_DISABLE_TESTS_REGEX:STRING="${DISABLED_TEST_REGEX}" \
  -DHDF5_ENABLE_DEPRECATED_SYMBOLS:BOOL=ON \
  -DHDF5_ENABLE_PARALLEL:BOOL=%{?with_mpi:ON}%{!?with_mpi:OFF} \
  -DHDF5_ENABLE_SZIP_SUPPORT:BOOL=%{?with_sz2:ON}%{!?with_sz2:OFF} \
  -DHDF5_ENABLE_THREADSAFE:BOOL=ON \
  -DHDF5_USE_GNU_DIRS:BOOL=ON \
%{nil}

# Remove timestamp/buildhost/kernel version
export SDE_DATE=$(date -d @${SOURCE_DATE_EPOCH} -u)
export UNAME_M_O=$(uname -m -o)
sed -i -e "s/\(Configured on: \).*/\1 $SDE_DATE/" \
       -e "s#\(Uname information: \).*#\1 $UNAME_M_O#" \
       -e "s/\(Configured by: \).*/\1 abuild@OBS/" \
       src/libhdf5.settings

# Not clear why we need to do this for mvapich2,
# but linking against libmpi.so.* fails otherwise
%if "%{?mpi_flavor}" == "mvapich2"
export LD_LIBRARY_PATH+=":%{my_libdir}"
%endif
%cmake_build

%install
%cmake_install
find %{buildroot} -type f -name "*.la" -delete -print

# Incorrect path pointing to package build dir
sed -Ei "s@(Module Directory: ).*@\1%{my_incdir}/mod@" %{buildroot}%{my_libdir}/libhdf5.settings

chmod -x HDF5Examples/C/H5FLT/tfiles/h5ex_d_*.*

# Delete %%doc files from all possible combinations of dirs
rm -rf %{buildroot}%{_prefix}/share/COPYING \
       %{buildroot}%{my_prefix}/share/COPYING \
       %{buildroot}%{_docdir}/%{name}/ \
       %{buildroot}%{_docdir}/%{vname}/ \
       %{buildroot}%{my_prefix}/share/doc/packages/%{name}/ \
       %{buildroot}%{my_prefix}/share/doc/packages/%{vname}/ \
%{nil}

sed -Ei "1{s@/usr/bin/env bash@%{my_bindir}/bash@}" %{buildroot}%{my_bindir}/h5fuse

# HACK: We need the _test.so libraries in buildroot for tests
# to succeed, but we can exclude them from file lists
cp %{__builddir}/bin/libhdf5_test*.so* %{buildroot}%{my_libdir}

%if %{without mpi}
# Manually install examples as cmake does not do it (unversioned dir)
install -m 0755 -d %{buildroot}%{_datadir}/hdf5_examples
cp -pr HDF5Examples/* %{buildroot}%{_datadir}/hdf5_examples/
# rpm macro for version checking
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d/
cat > %{buildroot}%{_rpmconfigdir}/macros.d/macros.hdf5 <<EOF
#
# RPM macros for hdf5 packaging
#
%_hdf5_sonum  %{sonum}
%_hdf5_version  %{version}
EOF
%else
# delete examples from parallel builds
find  %{buildroot} -type d -name "hdf5_examples" -exec rm -rf {} +;
# fix double / in pkgconfig files
sed -Ei "s@//@/@g" %{buildroot}%{my_libdir}/pkgconfig/*.pc
%fdupes %{buildroot}%{my_bindir}/
%endif

%fdupes %{buildroot}/%{my_incdir}/
%fdupes -s %{buildroot}/%{_datadir}

%check
%if %{with mpi}
 source %{my_bindir}/mpivars.sh
%endif

%if "%{?mpi_flavor}" != "mpich" || ("%_arch" != "s390" && "%_arch" != "s390x")
 %if "%{?mpi_flavor}" == "mvapich2"
  export MV2_SMP_USE_CMA=0
 %endif
 export LD_LIBRARY_PATH+=":%{buildroot}%{my_libdir}"
 export TMPDIR=`mktemp -d -p ${PWD}`
 %ctest
%endif

%ldconfig_scriptlets -n %{libname -s %{sonum}}
%ldconfig_scriptlets -n %{libname -l _cpp -s %{sonum}}
%ldconfig_scriptlets -n %{libname -l _fortran -s %{sonum}}
%ldconfig_scriptlets -n %{libname -l _hl -s %{sonum}}
%ldconfig_scriptlets -n %{libname -l _hl_cpp -s %{sonum}}
%ldconfig_scriptlets -n %{libname -l _hl_fortran -s %{sonum}}
%ldconfig_scriptlets -n %{libname -l _tools -s %{sonum}}

%if 0%{?sle_version} > 120200 || 0%{?suse_version} > 1320
%define mylicense %license
%else
%define mylicense %doc
%endif

%if %{without mpi}
%files -n %{vname}-examples
%{_prefix}/share/hdf5_examples

%files -n %{pname}-devel-data
%{_rpmconfigdir}/macros.d/macros.hdf5
%endif # ?mpi

%files -n %{name}
%{my_bindir}/h5clear
%{my_bindir}/h5copy
%{my_bindir}/h5debug
%{my_bindir}/h5delete
%{my_bindir}/h5diff
%{my_bindir}/h5dump
%{my_bindir}/h5format_convert
%{my_bindir}/h5fuse
%{my_bindir}/h5import
%{my_bindir}/h5jam
%{my_bindir}/h5ls
%{my_bindir}/h5mkgrp
%if %{with mpi}
%{my_bindir}/ph5diff
%{my_bindir}/h5perf
%endif
%{my_bindir}/h5perf_serial
%{my_bindir}/h5repack
%{my_bindir}/h5repart
%{my_bindir}/h5stat
%{my_bindir}/h5unjam
%{my_bindir}/h5watch
%{my_bindir}/mirror_server*

%files -n %{libname -s %{sonum}}
%doc ACKNOWLEDGMENTS README.md
%mylicense COPYING
##
%if %{without mpi}
%doc release_docs/HISTORY-1_14.txt
%doc release_docs/RELEASE.txt
%endif
%defattr(0755,root,root)
%{my_libdir}/libhdf5.so.%{sonum}
%{my_libdir}/libhdf5.so.%{sonum}.*

%files -n %{libname -l _hl -s %{sonum}}
%mylicense COPYING
%defattr(0755,root,root)
%{my_libdir}/libhdf5_hl.so.%{sonum}
%{my_libdir}/libhdf5_hl.so.%{sonum}.*

%files -n %{libname -l _cpp -s %{sonum}}
%mylicense COPYING
%defattr(0755,root,root)
%{my_libdir}/libhdf5_cpp.so.%{sonum}
%{my_libdir}/libhdf5_cpp.so.%{sonum}.*

%files -n %{libname -l _hl_cpp -s %{sonum}}
%mylicense COPYING
%defattr(0755,root,root)
%{my_libdir}/libhdf5_hl_cpp.so.%{sonum}
%{my_libdir}/libhdf5_hl_cpp.so.%{sonum}.*

%files -n %{libname -l _fortran -s %{sonum}}
%mylicense COPYING
%defattr(0755,root,root)
%{my_libdir}/libhdf5_fortran.so.%{sonum}
%{my_libdir}/libhdf5_fortran.so.%{sonum}.*
%{my_libdir}/libhdf5_f90cstub.so.%{sonum}
%{my_libdir}/libhdf5_f90cstub.so.%{sonum}.*

%files -n %{libname -l _hl_fortran -s %{sonum}}
%mylicense COPYING
%defattr(0755,root,root)
%{my_libdir}/libhdf5_hl_fortran.so.%{sonum}
%{my_libdir}/libhdf5_hl_fortran.so.%{sonum}.*
%{my_libdir}/libhdf5_hl_f90cstub.so.%{sonum}
%{my_libdir}/libhdf5_hl_f90cstub.so.%{sonum}.*

%files -n %{libname -l _tools -s %{sonum}}
%mylicense COPYING
%defattr(0755,root,root)
%{my_libdir}/libhdf5_tools.so.%{sonum}
%{my_libdir}/libhdf5_tools.so.%{sonum}.*

%files devel
##
%doc release_docs/HISTORY-1_14.txt
%doc release_docs/RELEASE.txt
%doc ACKNOWLEDGMENTS README.md
%doc release_docs/USING_HDF5_CMake.txt
%{my_bindir}/h5c++
%{my_bindir}/h5cc
%{my_bindir}/h5fc
%{my_bindir}/h5hlc++
%{my_bindir}/h5hlcc
%{my_bindir}/h5hlfc
%if %{with mpi}
%{my_bindir}/h5pcc
%{my_bindir}/h5pfc
%endif
%{my_incdir}/*.h
%{my_incdir}/H5fortran_types.F90
%{my_incdir}/H5config_f.inc
%{my_incdir}/mod/
%{my_libdir}/*.so
%{my_libdir}/*.settings
%{my_incdir}/*.mod
%{my_libdir}/pkgconfig/*.pc
%dir %{my_libdir}/cmake
%{my_libdir}/cmake/hdf5/
%exclude %{my_libdir}/libhdf5_test*.so*

%if %{with static}
%files devel-static
%{my_libdir}/*.a
%endif

%changelog
