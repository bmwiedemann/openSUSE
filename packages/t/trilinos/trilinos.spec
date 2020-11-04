#
# spec file for package trilinos
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


%global flavor @BUILD_FLAVOR@%{nil}

%bcond_with qt

# Base package name
%define pname trilinos
%define ver 12.14.1
%define ver_exp 12-14-1
%define so_ver 12
%define PNAME %(echo %{pname} | tr [a-z] [A-Z])
%define _ver %(echo %{ver} | tr . _)
%define openblas_vers 0.3.6

# Don't even try this package on 32bit
# - some modules require pointers of bigger size
ExcludeArch:    i586 s390 s390x ppc armv7l

%if 0%{?sle_version} >= 150200
%define DisOMPI1 ExclusiveArch:  do_not_build
%endif
%if !%{?is_opensuse} && 0%{?sle_version:1} && 0%{?sle_version} < 150200
%define DisOMPI3 ExclusiveArch:  do_not_build
%endif
%if 0%{?sle_version:1} && 0%{?sle_version} < 150300
%define DisOMPI4 ExclusiveArch:  do_not_build
%endif

%if "%flavor" == ""
ExclusiveArch:  do_not_build
%endif

%define package_name %{pname}

%if "%{flavor}" == "serial"
%undefine c_f_ver
%{bcond_with hpc}
%endif

%if "%{flavor}" == "mvapich2"
%undefine c_f_ver
%global mpi_family mvapich2
%{bcond_with hpc}
%endif

%if "%{flavor}" == "openmpi"
%{?DisOMPI1}
%undefine c_f_ver
%global mpi_family openmpi
%define mpi_ver 1
%{bcond_with hpc}
%endif

%if "%{flavor}" == "openmpi2"
%{?DisOMPI2}
%undefine c_f_ver
%global mpi_family openmpi
%define mpi_ver 2
%{bcond_with hpc}
%endif

%if "%{flavor}" == "openmpi3"
%{?DisOMPI3}
%undefine c_f_ver
%global mpi_family openmpi
%define mpi_ver 3
%{bcond_with hpc}
%endif

%if "%{flavor}" == "openmpi4"
%{?DisOMPI4}
%undefine c_f_ver
%global mpi_family openmpi
%define mpi_ver 4
%{bcond_with hpc}
%endif

%if "%{flavor}" == "gnu-mvapich2-hpc"
%undefine c_f_ver
%global mpi_family mvapich2
%global compiler_family gnu
%{bcond_without hpc}
%endif

%if "%{flavor}" == "gnu-mpich-hpc"
%undefine c_f_ver
%global mpi_family mpich
%global compiler_family gnu
%{bcond_without hpc}
%endif

%if "%{flavor}" == "gnu-openmpi-hpc"
%{?DisOMPI1}
%undefine c_f_ver
%global mpi_family openmpi
%global compiler_family gnu
%define mpi_ver 1
%{bcond_without hpc}
%endif

%if "%{flavor}" == "gnu-openmpi2-hpc"
%{?DisOMPI2}
%undefine c_f_ver
%global mpi_family openmpi
%global compiler_family gnu
%define mpi_ver 2
%{bcond_without hpc}
%endif

%if "%{flavor}" == "gnu-openmpi3-hpc"
%{?DisOMPI3}
%undefine c_f_ver
%global mpi_family openmpi
%global compiler_family gnu
%define mpi_ver 3
%{bcond_without hpc}
%endif

%if "%{flavor}" == "gnu-openmpi4-hpc"
%{?DisOMPI4}
%undefine c_f_ver
%global mpi_family openmpi
%global compiler_family gnu
%define mpi_ver 4
%{bcond_without hpc}
%endif

%if "%{flavor}" == "gnu7-mvapich2-hpc"
%define c_f_ver 7
%global mpi_family mvapich2
%global compiler_family gnu
%{bcond_without hpc}
%endif

%if "%{flavor}" == "gnu7-mpich-hpc"
%define c_f_ver 7
%global mpi_family mpich
%global compiler_family gnu
%{bcond_without hpc}
%endif

%if "%{flavor}" == "gnu7-openmpi-hpc"
%{?DisOMPI1}
%define c_f_ver 7
%global mpi_family openmpi
%global compiler_family gnu
%define mpi_ver 1
%{bcond_without hpc}
%endif

%if "%{flavor}" == "gnu7-openmpi2-hpc"
%{?DisOMPI2}
%define c_f_ver 7
%global mpi_family openmpi
%global compiler_family gnu
%define mpi_ver 2
%{bcond_without hpc}
%endif

%if "%{flavor}" == "gnu7-openmpi3-hpc"
%{?DisOMPI3}
%define c_f_ver 7
%global mpi_family openmpi
%global compiler_family gnu
%define mpi_ver 3
%{bcond_without hpc}
%endif

%if "%{flavor}" == "gnu7-openmpi4-hpc"
%{?DisOMPI4}
%define c_f_ver 7
%global mpi_family openmpi
%global compiler_family gnu
%define mpi_ver 4
%{bcond_without hpc}
%endif

%if "%{flavor}" == "gnu8-mvapich2-hpc"
%define c_f_ver 8
%global mpi_family mvapich2
%global compiler_family gnu
%{bcond_without hpc}
%endif

%if "%{flavor}" == "gnu8-mpich-hpc"
%define c_f_ver 8
%global mpi_family mpich
%global compiler_family gnu
%{bcond_without hpc}
%endif

%if "%{flavor}" == "gnu8-openmpi-hpc"
%{?DisOMPI1}
%define c_f_ver 8
%global mpi_family openmpi
%global compiler_family gnu
%define mpi_ver 1
%{bcond_without hpc}
%endif

%if "%{flavor}" == "gnu8-openmpi2-hpc"
%{?DisOMPI2}
%define c_f_ver 8
%global mpi_family openmpi
%global compiler_family gnu
%define mpi_ver 2
%{bcond_without hpc}
%endif

%if "%{flavor}" == "gnu8-openmpi3-hpc"
%{?DisOMPI3}
%define c_f_ver 8
%global mpi_family openmpi
%global compiler_family gnu
%define mpi_ver 3
%{bcond_without hpc}
%endif

%if "%{flavor}" == "gnu8-openmpi4-hpc"
%{?DisOMPI4}
%define c_f_ver 8
%global mpi_family openmpi
%global compiler_family gnu
%define mpi_ver 4
%{bcond_without hpc}
%endif

%if "%{flavor}" == "gnu9-mvapich2-hpc"
%define c_f_ver 9
%global mpi_family mvapich2
%global compiler_family gnu
%{bcond_without hpc}
%endif

%if "%{flavor}" == "gnu9-mpich-hpc"
%define c_f_ver 9
%global mpi_family mpich
%global compiler_family gnu
%{bcond_without hpc}
%endif

%if "%{flavor}" == "gnu9-openmpi-hpc"
%{?DisOMPI1}
%define c_f_ver 9
%global mpi_family openmpi
%global compiler_family gnu
%define mpi_ver 1
%{bcond_without hpc}
%endif

%if "%{flavor}" == "gnu9-openmpi2-hpc"
%{?DisOMPI2}
%define c_f_ver 9
%global mpi_family openmpi
%global compiler_family gnu
%define mpi_ver 2
%{bcond_without hpc}
%endif

%if "%{flavor}" == "gnu9-openmpi3-hpc"
%{?DisOMPI3}
%define c_f_ver 9
%global mpi_family openmpi
%global compiler_family gnu
%define mpi_ver 3
%{bcond_without hpc}
%endif

%if "%{flavor}" == "gnu9-openmpi4-hpc"
%{?DisOMPI4}
%define c_f_ver 9
%global mpi_family openmpi
%global compiler_family gnu
%define mpi_ver 4
%{bcond_without hpc}
%endif

%if "%{flavor}" == "gnu10-mvapich2-hpc"
%define c_f_ver 10
%global mpi_family mvapich2
%global compiler_family gnu
%{bcond_without hpc}
%endif

%if "%{flavor}" == "gnu10-mpich-hpc"
%define c_f_ver 10
%global mpi_family mpich
%global compiler_family gnu
%{bcond_without hpc}
%endif

%if "%{flavor}" == "gnu10-openmpi-hpc"
%{?DisOMPI1}
%define c_f_ver 10
%global mpi_family openmpi
%global compiler_family gnu
%define mpi_ver 1
%{bcond_without hpc}
%endif

%if "%{flavor}" == "gnu10-openmpi2-hpc"
%{?DisOMPI2}
%define c_f_ver 10
%global mpi_family openmpi
%global compiler_family gnu
%define mpi_ver 2
%{bcond_without hpc}
%endif

%if "%{flavor}" == "gnu10-openmpi3-hpc"
%{?DisOMPI3}
%define c_f_ver 10
%global mpi_family openmpi
%global compiler_family gnu
%define mpi_ver 3
%{bcond_without hpc}
%endif

%if "%{flavor}" == "gnu10-openmpi4-hpc"
%{?DisOMPI4}
%define c_f_ver 10
%global mpi_family openmpi
%global compiler_family gnu
%define mpi_ver 4
%{bcond_without hpc}
%endif

%if "%{flavor}" == "documentation-hpc"
%{bcond_without hpc}
%{bcond_without doc}
%else
 %if "%{flavor}" == "documentation"
%{bcond_with hpc}
%{bcond_without doc}
 %else
%{bcond_with doc}
 %endif
%endif

%if !0%{?is_opensuse} && !0%{?with_hpc:1}
ExclusiveArch:  do_not_build
%endif

%{?mpi_family:%{bcond_without mpi}}%{!?mpi_family:%{bcond_with mpi}}
%{?with_mpi:%{!?mpi_family:error "No MPI family specified!"}}

# For compatibility package names
%if "%{mpi_family}" != "openmpi" || "%{mpi_ver}" != "1" || 0%{?suse_version} >= 1550
%define mpi_ext %{?mpi_ver}
%endif

%if %{without hpc}
 %if %{with mpi}
%define p_prefix %{_libdir}/mpi/gcc/%{mpi_family}%{?mpi_ext}
%define p_includedir %{p_prefix}/include
%define mpi_suffix -%{mpi_family}%{?mpi_ext}
 %else
%define p_prefix %{_prefix}
%define p_includedir %{p_prefix}/include/%{pname}
 %endif
%define p_libdir %{p_prefix}/%{_lib}
%define p_bindir %{p_prefix}/bin
%define package_name %{pname}%{?mpi_suffix}
%define libname lib%{pname}%{?so_ver}%{?mpi_suffix}
%else
%{hpc_init %{?compiler_family:-c %compiler_family %{?c_f_ver:-v %{c_f_ver}}} %{?with_mpi:-m {%mpi_family}} %{?mpi_ver:-V %{mpi_ver}} %{?ext:-e %{ext}}}
%define package_name %{hpc_package_name %_ver}
%define p_prefix %{hpc_prefix}
%define p_includedir %hpc_includedir
%define p_libdir %hpc_libdir
%define p_bindir %hpc_bindir
%define libname lib%{name}
# This will avoid rpmint errors when non-python3 scripts are detected.
# It needs to be addressed at some point. This needs to come after hpc_init.
%undefine _hpc_python3
%endif

Name:           %package_name
Version:        %ver
Release:        0
Summary:        A collection of libraries of numerical algorithms
License:        LGPL-2.0-only
Group:          Productivity/Scientific/Math
URL:            http://trilinos.sandia.gov/index.html
Source0:        https://github.com/trilinos/Trilinos/archive/trilinos-release-%{ver_exp}.tar.gz
# PATCH-FIX-UPSTREAM trilinos-11.4.3-no-return-in-non-void.patch
Patch0:         trilinos-11.14.3-no-return-in-non-void.patch
Patch1:         Fix-Makefiles-for-gmake-4.3.patch
# PATCH-FIX-UPSTREAM 
Patch2:         reproducible.patch
# PATCH-FIX-UPSTREAM 
Patch3:         reproducible-docs.patch
BuildRequires:  cmake >= 2.8
BuildRequires:  fdupes
BuildRequires:  hwloc-devel
%if 0%{?sle_version} > 150100 || 0%{?suse_version} > 1500
BuildRequires:  ninja
%endif
%if %{with qt}
BuildRequires:  libqt4-devel
%endif
BuildRequires:  memory-constraints
BuildRequires:  swig > 2.0.0
BuildRequires:  xz
BuildRequires:  zlib-devel
%{?with_hpc:BuildRequires:  suse-hpc >= 0.5}

%if %{with doc}
BuildRequires:  doxygen
BuildRequires:  expat
BuildRequires:  graphviz
BuildRequires:  libxml2-devel
BuildRequires:  perl
%else

 %if %{with hpc}
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel
BuildRequires:  %{mpi_family}%{?mpi_ext}-%{compiler_family}%{?c_f_ver}-hpc-macros-devel
# Fix this once boost is available as a HPC version
BuildRequires:  boost-devel
#BuildRequires:  boost-%%{compiler_family}-hpc-devel
BuildRequires:  hdf5-%{compiler_family}-%{mpi_family}%{?mpi_ext}-hpc-devel
BuildRequires:  libopenblas-%{compiler_family}-hpc >=  %{openblas_vers}
BuildRequires:  libopenblas-%{compiler_family}-hpc-devel
BuildRequires:  netcdf-%{compiler_family}-%{mpi_family}%{?mpi_ext}-hpc-devel
# hpc
 %else
BuildRequires:  boost-devel
BuildRequires:  cppunit-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  glpk-devel
BuildRequires:  lapack-devel
BuildRequires:  libmatio-devel
BuildRequires:  mumps-devel
BuildRequires:  openblas-devel
BuildRequires:  superlu-devel
  %if %{without mpi}
BuildRequires:  hdf5-devel
BuildRequires:  netcdf-devel
BuildRequires:  scotch-devel
BuildRequires:  umfpack-devel
  %else
BuildRequires:  blacs-devel-headers
BuildRequires:  hdf5-%{mpi_family}%{?mpi_ext}-devel
BuildRequires:  hypre-%{mpi_family}%{?mpi_ext}-devel
BuildRequires:  mumps-%{mpi_family}%{?mpi_ext}-devel
BuildRequires:  netcdf-%{mpi_family}%{?mpi_ext}-devel
BuildRequires:  ptscotch-%{mpi_family}%{?mpi_ext}-devel
BuildRequires:  scalapack-%{mpi_family}%{?mpi_ext}-devel
  %endif
# hpc
 %endif

# FIXME: Serial package is currently not pulling in library
Requires:       %libname = %version

# doc
%endif

%{!?python_sitearch: %global python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

#!BuildIgnore: post-build-checks

# Default library install path

%description
Trilinos is a collection of compatible software packages that support parallel
linear algebra computations, solution of linear, non-linear and eigen systems
of equations and related capabilities. The majority of packages are written in
C++ using object-oriented techniques. All packages are self-contained, with the
Trilinos top layer providing a common look-and-feel and infrastructure.

%if %{without doc}
%package -n %{libname}
Summary:        A collection of libraries of numerical algorithms
# only used for HPC
Group:          System/Libraries
%if %{with hpc}
%hpc_requires
Requires:       %{compiler_family}%{?c_f_ver}-compilers-hpc
Requires:       %{mpi_family}%{?mpi_ver}-%{compiler_family}%{?c_f_ver}-hpc
# Fix this once boost is available as a HPC version
#Requires:       boost-%%{compiler_family}-hpc
Requires:       libhdf5%{hpc_package_name_tail} >= 1.8.8
Requires:       libnetcdf%{hpc_package_name_tail}
Requires:       libopenblas-%{compiler_family}-hpc
Requires:       lua-lmod >= 7.6.1
%endif

%description -n %{libname}
Trilinos is a collection of compatible software packages that support parallel
linear algebra computations, solution of linear, non-linear and eigen systems
of equations and related capabilities. The majority of packages are written in
C++ using object-oriented techniques. All packages are self-contained, with the
Trilinos top layer providing a common look-and-feel and infrastructure.

This subpackage contains the shared libraries.

%package devel
Summary:        Headers and development files for %{package_name}
Group:          Development/Libraries/C and C++
%if %{without hpc}
Requires:       glpk-devel
Requires:       swig
Recommends:     %{name}-doc
 %if %{without mpi}
Requires:       hdf5-devel
Requires:       lapack-devel
Requires:       libxml2-devel
Requires:       mumps-devel
Requires:       netcdf-devel
Requires:       scotch-devel
Requires:       suitesparse-common-devel
Requires:       umfpack-devel
Conflicts:      kokkos-devel
 %else
Requires:       blacs-devel-headers
Requires:       hdf5-%{mpi_family}%{?mpi_ext}-devel
Requires:       hypre-%{mpi_family}%{?mpi_ext}-devel
Requires:       mumps-%{mpi_family}%{?mpi_ext}-devel
Requires:       netcdf-%{mpi_family}%{?mpi_ext}-devel
Requires:       ptscotch-%{mpi_family}%{?mpi_ext}-devel
Requires:       scalapack-%{mpi_family}%{?mpi_ext}-devel
 %endif
# hpc
%else
%hpc_requires_devel
Requires:       %{compiler_family}%{?c_f_ver}-compilers-hpc
Requires:       %{mpi_family}%{?mpi_ver}-%{compiler_family}%{?c_f_ver}-hpc
# Fix this once boost is available as a HPC version
#Requires:       boost-%%{compiler_family}-hpc
Requires:       %libname = %version
Requires:       hdf5%{hpc_package_name_tail}-devel
Requires:       libopenblas-%{compiler_family}-hpc-devel
Requires:       netcdf%{hpc_package_name_tail}-devel
# hpc
%endif
Obsoletes:      %{name} <= %version

%description devel
Trilinos is a collection of compatible software packages that support parallel
linear algebra computations, solution of linear, non-linear and eigen systems
of equations and related capabilities. The majority of packages are written in
C++ using object-oriented techniques. All packages are self-contained, with the
Trilinos top layer providing a common look-and-feel and infrastructure.

This package contains the headers and libraries files for %{package_name}
needed for development.


%if %{with hpc}
%{hpc_master_package -l -L}
%{hpc_master_package -L -O %{pname}%{hpc_package_name_tail} devel}
%endif

%prep
%setup -q -n  Trilinos-trilinos-release-%{ver_exp}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
# https://en.opensuse.org/openSUSE:Build_system_recipes#cmake
%if 0%{?sle_version} > 150100 || 0%{?suse_version} > 1500
%define __builder ninja
%endif
# Do *not* replace by memoryperjob constraint!!! The latter
# attempts to find a work whose memory matches the number of
# jobs available * memoryperjob. Such workers may not exist!
%limit_build -m 4000
# Fix this once boost is available as a HPC version
# move this to the non-hpc section
BOOST_INC=%{_incdir}/boost
BOOST_LIB=%{_libdir}
#
%if %{with hpc}
%hpc_setup
%hpc_setup_mpi
# Fix this once boost is available as a HPC version
#module load boost
module load netcdf
module load %{?with_mpi:p}hdf5
module load openblas
%endif
export OLDPWD=..
%if %{without hpc}
 %if %{with mpi}
source %{p_bindir}/mpivars.sh
OPENBLAS_LIB=%{_incdir}/openblas
NETCDF_INC=%{p_incdir}
NETCDF_LIB=%{p_libdir}
HDF5_INC=%{p_incdir}
HDF5_LIB=%{p_libdir}
 %endif
%cmake \
%else
%hpc_cmake \
%endif
        -DCMAKE_INSTALL_PREFIX=%{p_prefix}                              \
        -DCMAKE_EXE_LINKER_FLAGS:STRING="-fPIC"                         \
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE                              \
        -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo                        \
        -DBUILD_SHARED_LIBS:BOOL=ON                                     \
        -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON                              \
        -DCMAKE_SKIP_RPATH:BOOL=ON                                      \
        -DTrilinos_INSTALL_LIB_DIR:PATH=%{p_libdir}                     \
%if %{without hpc} && %{without mpi}
	-DTrilinos_INSTALL_INCLUDE_DIR:PATH=include/%{pname}   	        \
%endif
        -DTrilinos_VERBOSE_CONFIGURE:BOOL=ON                            \
        -DTrilinos_ENABLE_ALL_PACKAGES:BOOL=OFF                         \
        -DTrilinos_EXTRA_LINK_FLAGS:STRING="-lgfortran"                 \
        -DTrilinos_ENABLE_Epetra:BOOL=OFF                               \
        -DTrilinos_ENABLE_Gtest:BOOL=OFF                                \
        -DTrilinos_ENABLE_MueLu:BOOL=ON                                 \
        -DTrilinos_ENABLE_Phalanx:BOOL=ON                               \
        -DTrilinos_ENABLE_Stokhos:BOOL=ON                               \
        -DTrilinos_ENABLE_Didasko:BOOL=ON                               \
        -DTrilinos_ENABLE_ROL:BOOL=%{?sle_version:OFF}%{!?sle_version:ON}\
        -DTrilinos_ENABLE_TrilinosCouplings:BOOL=ON                     \
        -DTrilinos_ENABLE_PyTrilinos:BOOL=OFF                           \
        -DTrilinos_ENABLE_CTrilinos:BOOL=ON                             \
        -DTrilinos_ENABLE_ForTrilinos:BOOL=ON                           \
        -DTrilinos_ENABLE_EXAMPLES:BOOL=OFF                             \
        -DTrilinos_ENABLE_STK:BOOL=OFF                                  \
        -DTrilinos_ENABLE_TESTS:BOOL=OFF                                \
        -DTrilinos_ENABLE_OpenMP:BOOL=ON                                \
        -DTrilinos_ENABLE_EXPLICIT_INSTANTIATION:BOOL=ON                \
        -DTEUCHOS_ENABLE_expat:BOOL=ON                                  \
        -DTEUCHOS_ENABLE_libxml2:BOOL=ON                                \
        -DTEUCHOS_ENABLE_gmp:BOOL=ON                                    \
        -DTPL_ENABLE_BLAS:BOOL=ON                                       \
        -DBLAS_LIBRARY_DIRS:PATH="${OPENBLAS_LIB}"                      \
        -DBLAS_LIBRARY_NAMES:STRING="openblas"                          \
        -DTPL_ENABLE_LAPACK:BOOL=ON                                     \
        -DLAPACK_LIBRARY_DIRS:PATH="${OPENBLAS_LIB}"                    \
        -DLAPACK_LIBRARY_NAMES:STRING="openblas"                        \
        -DTPL_ENABLE_MPI:BOOL=%{?with_mpi:ON}%{!?with_mpi:OFF}          \
%if %{with mpi}
        -DMPI_C_COMPILER:FILEPATH=mpicc                                 \
        -DMPI_CXX_COMPILER:FILEPATH=mpicxx                              \
        -DMPI_FORTRAN_COMPILER:FILEPATH=mpif90                          \
%endif
        -DTPL_ENABLE_Netcdf:BOOL=ON                                     \
%if %{with hpc} || %{with mpi}
        -DNetcdf_INCLUDE_DIRS:PATH="${NETCDF_INC}"                      \
        -DNetcdf_LIBRARY_DIRS:PATH="${NETCDF_LIB}"                      \
%endif
        -DTPL_ENABLE_HDF5:BOOL=ON                                       \
%if %{with hpc} || %{with mpi}
        -DHDF5_INCLUDE_DIRS:PATH="${HDF5_INC}"                          \
        -DHDF5_LIBRARY_DIRS:PATH="${HDF5_LIB}"                          \
%endif
        -DHDF5_LIBRARY_NAMES:STRING="hdf5"                              \
        -DTPL_ENABLE_Boost:BOOL=ON                                      \
%if %{with hpc} || %{with mpi}
        -DBoost_INCLUDE_DIRS:PATH="${BOOST_INC}"                        \
        -DBoost_LIBRARY_DIRS:PATH="${BOOST_LIB}"                        \
%endif
        -DBoost_LIBRARY_NAMES:STRING="boost"                            \
        -DTPL_ENABLE_Pthread:BOOL=ON                                    \
        -DTPL_ENABLE_CppUnit:BOOL=OFF                                   \
        -DTPL_ENABLE_Zlib:BOOL=ON                                       \
        -DTPL_ENABLE_QT:BOOL=%{?with_qt:ON}%{!?with_qt:OFF}             \
        -DTPL_ENABLE_Matio=OFF                                          \
        -DTPL_ENABLE_GLM=OFF                                            \
        ..

#	-DTPL_ENABLE_SuperLU:BOOL=ON					\
#	-DTPL_ENABLE_MUMPS:BOOL=ON					\
#	-DMUMPS_LIBRARY_DIRS:PATH=%%{_libdir}/mpi/gcc/openmpi/%%{_lib}	\
#	-DMUMPS_INCLUDE_DIRS:PATH=%%{_includedir}/mumps			\
#	-DTPL_ENABLE_AMD:BOOL=ON					\
#	-DAMD_INCLUDE_DIRS:PATH=%%{_includedir}/suitesparse		\
#	-DTPL_ENABLE_UMFPACK:BOOL=ON					\
#	-DUMFPACK_INCLUDE_DIRS:PATH=%%{_includedir}/suitesparse		\
#	-DTPL_ENABLE_Scotch:BOOL=ON					\
#	-DScotch_LIBRARY_DIRS:PATH=%%{p_libdir}	                        \
#	-DScotch_INCLUDE_DIRS:PATH=%%{p_includedir}                     \
#	-DTPL_ENABLE_HYPRE:BOOL=%%{?with_mpi:ON}%%{!?with_mpi:OFF}	\
#	-DHYPRE_INCLUDE_DIRS:PATH=%%{p_includedir}/hypre                \
#	-DHYPRE_LIBRARY_DIRS:PATH=%%{p_libdir}	                        \
#       -DTPL_ENABLE_SCALAPACK:BOOL=ON                                  \
#       -DSCALAPACK_LIBRARY_DIRS:PATH="${MKLROOT}/lib/intel64"          \
#       -DSCALAPACK_LIBRARY_NAMES:STRING="mkl_rt"                       \
#       -DTPL_ENABLE_BLACS:BOOL=ON                                      \
#       -DBLACS_LIBRARY_DIRS:PATH="$MKLROOT/lib/intel64"                \
#       -DBLACS_INCLUDE_DIRS:PATH="$MKLROOT/include"                    \
#       -DBLACS_LIBRARY_NAMES:STRING="mkl_rt"                           \

%make_jobs 
cd ..

%install
%{?with_hpc:%hpc_setup}
%{?with_hpc:%hpc_setup_mpi}
%cmake_install

%if %{with hpc}
%hpc_write_modules_files
#%%Module1.0#####################################################################

proc ModulesHelp { } {

puts stderr " "
puts stderr "This module loads the %{pname} library built with the %{compiler_family} compiler"
puts stderr "toolchain and the %{mpi_family}%{?mpi_ver} MPI stack."
puts stderr "\nVersion %{version}\n"

}
module-whatis "Name: %{pname} built with %{compiler_family} compiler and %{mpi_family}%{?mpi_ver} MPI"
module-whatis "Version: %{version}"
module-whatis "Category: runtime library"
module-whatis "Description: %{SUMMARY}"
module-whatis "URL %{url}"

set     version                     %{version}

prepend-path    PATH                %{hpc_bindir}

if {[file isdirectory  %{hpc_includedir}]} {
prepend-path    INCLUDE             %{hpc_includedir}
}
prepend-path    LD_LIBRARY_PATH     %{hpc_libdir}

setenv          %{PNAME}_DIR        %{hpc_prefix}
setenv          %{PNAME}_BIN        %{hpc_bindir}
if {[file isdirectory  %{hpc_includedir}]} {
setenv          %{PNAME}_INC        %{hpc_includedir}
prepend-path    CPATH               %{hpc_includedir}
prepend-path    C_INCLUDE_PATH      %{hpc_includedir}
prepend-path    CPLUS_INCLUDE_PATH  %{hpc_includedir}
}
setenv          %{PNAME}_LIB        %{hpc_libdir}

depends-on openblas
depends-on %{?with_mpi:p}hdf5
depends-on %{?with_mpi:p}netcdf
#depends-on boost
EOF
# hpc
%else
 %if %{without mpi}
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/%{name}" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}.conf
 %endif
%endif

# cleanup
find %{buildroot}%{p_prefix} -name .gitignore -delete
%fdupes %{buildroot}/%{p_includedir}
%fdupes %{buildroot}/%{p_libdir}/cmake
%{?with_hpc:%{hpc_shebang_sanitize_scripts %{buildroot}/%{p_libdir}/cmake}}
%{?with_hpc:%{hpc_shebang_sanitize_scripts %{buildroot}/%{p_bindir}}}
%{?with_hpc:%{hpc_shebang_sanitize_scripts doc/}}
for i in $(find %{buildroot}/%{p_libdir}/cmake -name "*.sh" -o -name "*.py"); do 
    head -1 $i | grep -qE "#! */" && chmod 0755 $i
done

%if %{without hpc} && %{without mpi}
%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig
%else
# For HPC or MPI do not rebuild the cache on non-standard directories
%post -n %{libname}
/sbin/ldconfig -N %{p_libdir}

%postun -n %{libname}
/sbin/ldconfig -N %{p_libdir}
%hpc_module_delete_if_default
%endif

%files -n %{libname}
%doc README RELEASE_NOTES
%license LICENSE Copyright.txt
%dir %{p_libdir}
%{?hpc_dirs}
%{?hpc_modules_files}
%{p_libdir}/*.so.*
%if %{without mpi} && %{without hpc}
%config %{_sysconfdir}/ld.so.conf.d/%{name}.conf
%endif

%files devel
%{p_includedir}
%{p_libdir}/cmake
%{p_libdir}/*.so
%{p_bindir}%{!?hpc:/*}
# doc
%endif

#############################################################################
# Build documentation only               
#############################################################################
%if %{with doc}
%package doc
Summary:        The documentation and HTML files for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
Trilinos is a collection of compatible software packages that support parallel
linear algebra computations, solution of linear, non-linear and eigen systems
of equations and related capabilities. The majority of packages are written in
C++ using object-oriented techniques. All packages are self-contained, with the
Trilinos top layer providing a common look-and-feel and infrastructure.

This package contains the Trilinos HTML documentation.

%{?with_hpc:%{hpc_master_package doc}}

%prep
%setup -q -n  Trilinos-trilinos-release-%{ver_exp}
%patch3 -p1

%build
# Build the doc
echo "HTML_TIMESTAMP=NO" >> packages/common/Doxyfile
find packages/ -name 'footer.html' -print0 | xargs -0 sed -i 's/ on \$datetime//'
find packages/ -name 'Doxyfile*' -print0 | xargs -0 sed -i 's/HTML_TIMESTAMP         = YES/HTML_TIMESTAMP         = NO/'

cd doc
perl ./build_docs.pl
cd ..
# move html files in a single directory for doc package
find ./ -type d -name html -print0 | xargs -0 -I '{}' cp --parent -r '{}' doc/
test -d doc/doc && rm -rf doc/doc
test -f doc/build_docs.pl && rm -f doc/build_docs.pl
sed -i s/href=\"\.\./href=\"\./ doc/index.html

%fdupes -s doc/

%install
# cleanup
find doc/ -name .gitignore -delete
find doc/ -name *do-configure -exec chmod 644 {}  \;
find doc/ -name *copy_xml_to_src_html.py -exec chmod 644 {}  \;

%files doc
%doc doc/*
# doc
%endif

%changelog
