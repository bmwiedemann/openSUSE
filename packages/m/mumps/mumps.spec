#
# spec file for package mumps
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

%define pname mumps
%define ver 5.2.1
%define so_ver 5
%define openblas_vers 0.3.6
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

%define PNAME %(echo %{pname} | tr [a-z] [A-Z])
%define _ver %(echo %{ver} | tr . _)

%if "%flavor" == ""
%define package_name %{pname}
ExclusiveArch:  do_not_build
%endif

%if 0%{?sle_version} >= 150200
%define DisOMPI1 ExclusiveArch:  do_not_build
%endif
%if !0%{?is_opensuse} && 0%{?sle_version:1} && 0%{?sle_version} < 150200
%define DisOMPI3 ExclusiveArch:  do_not_build
%endif

%if "%{flavor}" == "serial"
# Stub MPI library
%define mumps_f77_mpilibs '-lmpiseq'
%bcond_with hpc
%endif

%if "%{flavor}" == "scotch-serial"
# Stub MPI library
%define mumps_f77_mpilibs '-lmpiseq'
%bcond_with hpc
%bcond_without scotch
%endif

%if "%{flavor}" == "openmpi1"
%{?DisOMPI1}
%define mpi_family  openmpi
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%define mpi_ver 1
%bcond_with hpc
%endif

%if "%{flavor}" == "openmpi2"
%define mpi_family  openmpi
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%define mpi_ver 2
%bcond_with hpc
%endif

%if "%{flavor}" == "openmpi3"
%define mpi_family  openmpi
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%define mpi_ver 3
%bcond_with hpc
%endif

%if "%{flavor}" == "openmpi4"
%define mpi_family  openmpi
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%define mpi_ver 4
%bcond_with hpc
%endif

%if "%{flavor}" == "mvapich2"
%define mpi_family  mvapich2
%define mumps_f77_mpilibs -lfmpich -lmpich
%bcond_with hpc
%endif

%if "%{flavor}" == "scotch-openmpi1"
%{?DisOMPI1}
%define mpi_family  openmpi
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%define mpi_ver 1
%bcond_with hpc
%bcond_without scotch
%endif

%if "%{flavor}" == "scotch-openmpi2"
%define mpi_family  openmpi
%define mpi_ver 2
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%bcond_with hpc
%bcond_without scotch
%endif

%if "%{flavor}" == "scotch-openmpi3"
%define mpi_family  openmpi
%define mpi_ver 3
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%bcond_with hpc
%bcond_without scotch
%endif

%if "%{flavor}" == "scotch-openmpi4"
%define mpi_family  openmpi
%define mpi_ver 4
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%bcond_with hpc
%bcond_without scotch
%endif

%if "%{flavor}" == "scotch-mvapich2"
%define mpi_family  mvapich2
%define mumps_f77_mpilibs -lfmpich -lmpich
%bcond_with hpc
%bcond_without scotch
%endif

%if "%{flavor}" == "gnu-openmpi-hpc"
%{?DisOMPI1}
%undefine c_f_ver
# macro mpi is used by macros for master package
%global mpi_family openmpi
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%define mpi_ver 1
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu-openmpi2-hpc"
%{?DisOMPI2}
%undefine c_f_ver
# macro mpi is used by macros for master package
%global mpi_family openmpi
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%define mpi_ver 2
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu-openmpi3-hpc"
%{?DisOMPI3}
%undefine c_f_ver
# macro mpi is used by macros for master package
%global mpi_family openmpi
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%define mpi_ver 3
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu-openmpi4-hpc"
%{?DisOMPI3}
%undefine c_f_ver
# macro mpi is used by macros for master package
%global mpi_family openmpi
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%define mpi_ver 4
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu-mvapich2-hpc"
%undefine c_f_ver
# macro mpi is used by macros for master package
%global mpi_family mvapich2
%define mumps_f77_mpilibs -lfmpich -lmpich
%undefine mpi_ver 
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu-mpich-hpc"
%undefine c_f_ver
%global mpi_family mpich
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu7-openmpi-hpc"
%{?DisOMPI1}
%define c_f_ver 7
# macro mpi is used by macros for master package
%global mpi_family openmpi
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%define mpi_ver 1
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu7-openmpi2-hpc"
%{?DisOMPI2}
%define c_f_ver 7
# macro mpi is used by macros for master package
%global mpi_family openmpi
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%define mpi_ver 2
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu7-openmpi3-hpc"
%{?DisOMPI3}
%define c_f_ver 7
# macro mpi is used by macros for master package
%global mpi_family openmpi
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%define mpi_ver 3
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu7-openmpi4-hpc"
%{?DisOMPI3}
%define c_f_ver 7
# macro mpi is used by macros for master package
%global mpi_family openmpi
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%define mpi_ver 4
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu7-mvapich2-hpc"
%define c_f_ver 7
# macro mpi is used by macros for master package
%global mpi_family mvapich2
%define mumps_f77_mpilibs -lfmpich -lmpich
%undefine mpi_ver 
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu7-mpich-hpc"
%define c_f_ver 7
%global mpi_family mpich
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu8-openmpi-hpc"
%{?DisOMPI1}
%define c_f_ver 8
# macro mpi is used by macros for master package
%global mpi_family openmpi
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%define mpi_ver 1
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu8-openmpi2-hpc"
%{?DisOMPI2}
%define c_f_ver 8
# macro mpi is used by macros for master package
%global mpi_family openmpi
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%define mpi_ver 2
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu8-openmpi3-hpc"
%{?DisOMPI3}
%define c_f_ver 8
# macro mpi is used by macros for master package
%global mpi_family openmpi
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%define mpi_ver 3
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu8-openmpi4-hpc"
%{?DisOMPI3}
%define c_f_ver 8
# macro mpi is used by macros for master package
%global mpi_family openmpi
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%define mpi_ver 4
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu8-mvapich2-hpc"
%define c_f_ver 8
# macro mpi is used by macros for master package
%global mpi_family mvapich2
%define mumps_f77_mpilibs -lfmpich -lmpich
%undefine mpi_ver 
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu8-mpich-hpc"
%define c_f_ver 8
%global mpi_family mpich
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu9-openmpi-hpc"
%{?DisOMPI1}
%define c_f_ver 9
# macro mpi is used by macros for master package
%global mpi_family openmpi
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%define mpi_ver 1
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu9-openmpi2-hpc"
%{?DisOMPI2}
%define c_f_ver 9
# macro mpi is used by macros for master package
%global mpi_family openmpi
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%define mpi_ver 2
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu9-openmpi3-hpc"
%{?DisOMPI3}
%define c_f_ver 9
# macro mpi is used by macros for master package
%global mpi_family openmpi
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%define mpi_ver 3
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu9-openmpi4-hpc"
%{?DisOMPI3}
%define c_f_ver 9
# macro mpi is used by macros for master package
%global mpi_family openmpi
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%define mpi_ver 4
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu9-mvapich2-hpc"
%define c_f_ver 9
# macro mpi is used by macros for master package
%global mpi_family mvapich2
%define mumps_f77_mpilibs -lfmpich -lmpich
%undefine mpi_ver 
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu9-mpich-hpc"
%define c_f_ver 9
%global mpi_family mpich
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu10-openmpi-hpc"
%{?DisOMPI1}
%define c_f_ver 10
# macro mpi is used by macros for master package
%global mpi_family openmpi
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%define mpi_ver 1
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu10-openmpi2-hpc"
%{?DisOMPI2}
%define c_f_ver 10
# macro mpi is used by macros for master package
%global mpi_family openmpi
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%define mpi_ver 2
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu10-openmpi3-hpc"
%{?DisOMPI3}
%define c_f_ver 10
# macro mpi is used by macros for master package
%global mpi_family openmpi
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%define mpi_ver 3
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu10-openmpi4-hpc"
%{?DisOMPI3}
%define c_f_ver 10
# macro mpi is used by macros for master package
%global mpi_family openmpi
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%define mpi_ver 4
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu10-mvapich2-hpc"
%define c_f_ver 10
# macro mpi is used by macros for master package
%global mpi_family mvapich2
%define mumps_f77_mpilibs -lfmpich -lmpich
%undefine mpi_ver 
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu10-mpich-hpc"
%define c_f_ver 10
%global mpi_family mpich
%bcond_without hpc
%endif

%ifarch i586 s390 ppc armv7l
ExclusiveArch:  do_not_build
%endif

%if !0%{?is_opensuse} && !0%{?with_hpc:1}
ExclusiveArch:  do_not_build
%endif

%{?mpi_family:%{bcond_without mpi}}%{!?mpi_family:%{bcond_with mpi}}

# openmpi 1 was called just "openmpi" in Leap 15.x/SLE15 
%if 0%{?suse_version} >= 1550 || "%{mpi_family}" != "openmpi" || "%{mpi_ver}" != "1"
%define mpi_ext %{?mpi_ver}
%endif

%if %{with scotch}
 %if %{with mpi}
  %define scotch ptscotch
 %else
 %define scotch scotch
 %endif
%endif

%if %{without hpc}
%if %{without mpi}
%define my_prefix %_prefix
%define my_bindir %_bindir
%define my_libdir %_libdir
%define my_incdir %_includedir
%define my_datadir %_datadir
%else
%define my_suffix  -%{mpi_family}%{?mpi_ext}
%define my_prefix %{_libdir}/mpi/gcc/%{mpi_family}%{?mpi_ext}
%define my_bindir %{my_prefix}/bin
%define my_libdir %{my_prefix}/%{_lib}/
%define my_incdir %{my_prefix}/include/
%define my_datadir %{my_prefix}/share/
%endif
%define package_name %{pname}%{?scotch:-%{scotch}}%{?my_suffix}
%define libname lib%{pname}%{?scotch:-%{scotch}}%{?so_ver}%{?my_suffix}
%else
%{!?compiler_family:%global compiler_family gnu}
%{?with_mpi:%{!?mpi_family:error "No MPI family specified!"}}

%{hpc_init -c %compiler_family %{?c_f_ver:-v %{c_f_ver}} %{?with_mpi:-m {%mpi_family}} %{?mpi_ver:-V %{mpi_ver}} %{?scotch:-e %{scotch}}}
%define my_prefix %{hpc_prefix}
%define my_bindir %{hpc_bindir}
%define my_libdir %{hpc_libdir}
%define my_incdir %{hpc_includedir}
%define my_datadir %{hpc_datadir}
%define package_name %{hpc_package_name %{?_ver}}
%define libname lib%{package_name}
%endif

Summary:        A MUltifrontal Massively Parallel Sparse direct Solver
License:        CECILL-C
Group:          Productivity/Scientific/Math
Name:           %{package_name}
Version:        %{ver}
Release:        0
URL:            http://mumps.enseeiht.fr/
Source0:        http://mumps.enseeiht.fr/MUMPS_%{version}.tar.gz#/%{pname}-%{version}.tar.gz
Source1:        Makefile.inc
Patch1:         Makefiles-Serialize-libseq-libplat-mommond_mod-for-parallel-builds.patch
%if %{without hpc}
BuildRequires:  gcc-fortran
%{?with_scotch:BuildRequires:  %{scotch}%{?with_mpi:-%{mpi_family}%{?mpi_ext}}-devel}
 %if %{with mpi}
BuildRequires:  %{mpi_family}%{?mpi_ext}-devel
BuildRequires:  libblacs2-%{mpi_family}%{?mpi_ext}-devel
BuildRequires:  scalapack-%{mpi_family}%{?mpi_ext}-devel
 %endif # mpi
BuildRequires:  blas-devel
BuildRequires:  lapack-devel
%else # hpc
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel
BuildRequires:  %{mpi_family}%{?mpi_ver}-%{compiler_family}%{?c_f_ver}-hpc-macros-devel
BuildRequires:  fdupes
BuildRequires:  libopenblas-%{compiler_family}%{?c_f_ver}-hpc >=  %{openblas_vers}
BuildRequires:  libscalapack2-%{compiler_family}%{?c_f_ver}-%{mpi_family}%{?mpi_ver}-hpc-devel
BuildRequires:  suse-hpc
%endif # hpc

%description
MUMPS implements a direct solver for large sparse linear systems, with a
particular focus on symmetric positive definite matrices.  It can
operate on distributed matrices e.g. over a cluster.  It has Fortran and
C interfaces, and can interface with ordering tools such as Scotch.


%package -n %{libname}
Summary:        A MUltifrontal Massively Parallel Sparse direct Solver
Group:          System/Libraries
 %if %{without hpc}
%{?with_mpi:Recommends:       %{name}-%{so_ver}-compat = %{version}}
# Explicitly include this library here:
# the solver doesn't have enough information to pick the correct MPI flavor
%{?with_mpi:Requires:         libblacs2-%{mpi_family}%{?mpi_ext}}
 %else
Requires:       libscalapack2-%{compiler_family}-%{mpi_family}%{?mpi_ver}-hpc
%hpc_requires
Requires:       lua-lmod >= 7.6.1
 %endif

%description -n %{libname}
MUMPS implements a direct solver for large sparse linear systems, with a
particular focus on symmetric positive definite matrices.  It can
operate on distributed matrices e.g. over a cluster.  It has Fortran and
C interfaces, and can interface with ordering tools such as Scotch.

%if %{!with mpi}
This package contains the sequential library%{?scotch: with Scotch support enabled}.
%else
This package contains the parallel library%{?with_mpi: with %{mpi_family}%{?mpi_ver}}%{?scotch: with Scotch support enabled}.
%endif

%package %{so_ver}-compat
Summary:        A MUltifrontal Massively Parallel Sparse direct Solver
Group:          System/Libraries
Requires:       lib%{pname}%{?scotch:-scotch}%{so_ver} = %{version}
%if %{without hpc} && %{with mpi}
# Install link targets for non-HPC MPI compat links from the MPI libdir - see below.
BuildRequires:  %{pname}%{?scotch:-scotch}-devel-static = %version
BuildRequires:  lib%{pname}%{?scotch:-scotch}%{so_ver} = %{version}
%endif

%description %{so_ver}-compat
MUMPS implements a direct solver for large sparse linear systems, with a
particular focus on symmetric positive definite matrices.  It can
operate on distributed matrices e.g. over a cluster.  It has Fortran and
C interfaces, and can interface with ordering tools such as Scotch.

This package provides links to the serial libraries from the MPI library
directory MUMPS built for %{mpi_family}%{?mpi_ver}.

%package doc
Summary:        A MUltifrontal Massively Parallel Sparse direct Solver
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
MUMPS implements a direct solver for large sparse linear systems, with a
particular focus on symmetric positive definite matrices.  It can
operate on distributed matrices e.g. over a cluster.  It has Fortran and
C interfaces, and can interface with ordering tools such as Scotch.

This package provides Documentation for %{package_name}.

%if %{!with mpi}
This package contains the sequential library%{?scotch: with Scotch support enabled}.
%else
This package contains the parallel library%{?with_mpi: with %{mpi_family}%{?mpi_ver}}%{?scotch: with Scotch support enabled}.
%endif

%package devel
Summary:        Files needed for developing mumps based applications
Group:          Development/Libraries/Parallel
Requires:       %{libname} = %version
%if %{without hpc}
 %if %{with mpi} || %{with scotch}
Requires:       mumps-devel = %{version}
 %endif
 %if %{with mpi}
Requires:       %{mpi_family}%{?mpi_ext}-devel
Requires:       scalapack-%{mpi_family}%{?mpi_ext}-devel
  %if %{with scotch}
Requires:       mumps-scotch-devel = %{version}
Requires:       ptscotch-%{mpi_family}%{?mpi_ext}-devel
  %endif
  %if "%{mpi_family}%{?mpi_ext}" == "openmpi1"
Provides:       %{pname}%{?scotch:-%{scotch}}-openmpi-devel
  %endif
 %else # mpi
Requires:       blas-devel
Requires:       lapack-devel
%{?with_scotch:Requires:       scotch-devel}
 %endif # mpi
Recommends:     gcc-fortran
%else # hpc
%hpc_requires_devel
Requires:       libscalapack2-%{compiler_family}-%{mpi_family}%{?mpi_ver}-hpc-devel
%endif

%description devel
MUMPS implements a direct solver for large sparse linear systems, with a
particular focus on symmetric positive definite matrices.  It can
operate on distributed matrices e.g. over a cluster.  It has Fortran and
C interfaces, and can interface with ordering tools such as Scotch.

Headers and development files for %{package_name}.

%package devel-static
Summary:        Files needed for developing mumps based applications
Group:          Development/Libraries/Parallel
Requires:       %{package_name}-devel
%{?with_mpi:Recommends:       %{name}-%{so_ver}-compat-static = %{version}}

%description devel-static
MUMPS implements a direct solver for large sparse linear systems, with a
particular focus on symmetric positive definite matrices.  It can
operate on distributed matrices e.g. over a cluster.  It has Fortran and
C interfaces, and can interface with ordering tools such as Scotch.

Static libraries for %{package_name}.

%package devel-static-compat
Summary:        Files needed for developing mumps based applications
Group:          Development/Libraries/Parallel
Requires:       %{pname}%{?scotch:-scotch}-devel-static = %version

%description devel-static-compat
MUMPS implements a direct solver for large sparse linear systems, with a
particular focus on symmetric positive definite matrices.  It can
operate on distributed matrices e.g. over a cluster.  It has Fortran and
C interfaces, and can interface with ordering tools such as Scotch.

This package provides links to the static serial libraries from the MPI
library directory MUMPS built for %{mpi_family}%{?mpi_ver}.

%package examples
Summary:        Test programs and examples for mumps
Group:          Documentation/Other
Requires:       %{libname} = %version
%if %{without hpc}
Provides:       mumps(examples)(%{?mpi_family}) = %version
Conflicts:      otherproviders(mumps(examples)(%{?mpi_family}))
%endif

%description examples
MUMPS implements a direct solver for large sparse linear systems, with a
particular focus on symmetric positive definite matrices.  It can
operate on distributed matrices e.g. over a cluster.  It has Fortran and
C interfaces, and can interface with ordering tools such as Scotch.

This packages contains some test and examples programs for mumps. In addition,
matlab and scilab extensions are provided in /usr/share/doc/packages/mumps.

%if %{with hpc}
%{hpc_master_package -l -L}
%{hpc_master_package -L devel}
%{hpc_master_package -L examples}
%{hpc_master_package doc}
%endif

%prep
%setup -q -n %{PNAME}_%{version}
%patch1 -p1

%build

export SUSE_ASNEEDED=0

%if %{with hpc}
%hpc_setup
module load openblas scalapack
%else
%{?with_mpi: source %{my_bindir}/mpivars.sh}
%endif

%define PLAT %{?scotch:_%{scotch}}%{!?scotch:%{!?with_mpi:_seq}}

%if %{without scotch}
 %define ORDERINGSF -Dpord
%else # scotch
 %if %{with mpi}
  %define scotch ptscotch
  %define LSCOTCH -lptesmumps -lptscotch -lptscotcherr -lscotch
  %define  ORDERINGSF -Dscotch -Dpord -Dptscotch
 %else # mpi
  %define scotch scotch
  %define LSCOTCH -lesmumps -lscotch -lscotcherr
  %define ISCOTCH -I%_includedir
  %define ORDERINGSF -Dscotch -Dpord
 %endif
%endif # scotch

%if %{with hpc}
 %define LIBBLAS -lopenblas -lscalapack
 %define LAPAK -lscalapack
%else # hpc
 %define LIBBLAS -lblas -llapack
 %define LAPACK -llapack
%endif # hpc

%if %{with mpi}
# Set LD_LIBRARY_PATH and PATH
 %define C_C mpicc
 %define F_C mpif77 -std=legacy
 %define F_L mpif77
 %define SCALAP -lscalapack %{!?with_hpc:-lblacs}
 %define MUMPS_LIBF77 %{!?with_hpc:-L%{my_libdir}} %{?mumps_f77_mpilibs}
 %define INCPAR %{!?with_hpc:-I%{my_incdir}}
 %define LIBPAR %{SCALAP} %{MUMPS_LIBF77}
 %define INCS \\\$(INCPAR)
 %define LIBS \\\$(LIBPAR)
%else # mpi
 %define C_C gcc
 %define F_C gfortran -std=legacy
 %define F_L gfortran
 %define LIBSEQNEEDED libseqneeded
 %define MUMPS_LIBF77 -lmpiseq%{?PLAT}
 %define INCS \\\$(INCSEQ)
 %define LIBS \\\$(LIBSEQ)
%endif # mpi

cp -f %{S:1} Makefile.inc
echo \
   "%{?C_C:CC=%C_C}
    %{?F_C:FC=%F_C}
    %{?F_L:FL=%F_L}
    %{?SCALAP:SCALAP=%SCALAP}
    %{?INCPAR:INCPAR=%INCPAR}
    %{?LIBPAR:LIBPAR=%LIBPAR}
    %{?LIBBLAS:LIBBLAS=%LIBBLAS}
    %{?INCS:INCS=%INCS}
    %{?LIBS:LIBS=%LIBS}
    %{?LIBSEQNEEDED:LIBSEQNEEDED=%LIBSEQNEEDED}
    %{?LSCOTCH:LSCOTCH=%LSCOTCH}
    %{?ISCOTCH:ISCOTCH=%ISCOTCH}
    %{?ORDERINGSF:ORDERINGSF=%ORDERINGSF}
    %{?PLAT:PLAT=%PLAT}
    OPTC=$RPM_OPT_FLAGS -fPIC
    OPTF=\$(OPTC)" >> Makefile.inc

make %{?_smp_mflags} alllib

%{!?with_mpi:cp -P libseq/libmpiseq*.a lib/}

mkdir lib/tmp; cd lib/tmp; 
%define LORDERINGS -lpord%{?PLAT} %{?scotch:-l%{scotch}}
%if %{without mpi}
  rm -f *.o; ar -x ../libmpiseq%{?PLAT}.a
  %F_C -shared *.o -Wl,-soname,libmpiseq%{?PLAT}.so.%{version} -o ../libmpiseq%{?PLAT}.so.%{version}
  ln -s libmpiseq%{?PLAT}.so.%{version} ../libmpiseq%{?PLAT}.so
%endif
rm -f *.o; ar -x ../libpord%{?PLAT}.a
%C_C -shared *.o -Wl,-soname,libpord%{?PLAT}.so.%{version} -o ../libpord%{?PLAT}.so.%{version}
ln -s libpord%{?PLAT}.so.%{version} ../libpord%{?PLAT}.so
rm -f *.o; ar -x ../libmumps_common%{?PLAT}.a
%F_C -shared *.o -Wl,-soname,libmumps_common$%{?PLAT}.so.%{version} -L.. %{LORDERINGS} \
     -lpthread %{MUMPS_LIBF77} -o ../libmumps_common%{?PLAT}.so.%{version}
ln -s libmumps_common%{?PLAT}.so.%{version} ../libmumps_common%{?PLAT}.so
for ARITH in c d s z ; do
   %F_C -shared -Wl,--whole-archive ../lib${ARITH}mumps%{?PLAT}.a  -Wl,--no-whole-archive \
       -Wl,-soname,lib${ARITH}mumps%{?PLAT}.so.%{version} -L.. -lmumps_common%{?PLAT} \
       %{LORDERINGS} %{MUMPS_LIBF77} %{LIBBLAS} %{?SCALAP} -o ../lib${ARITH}mumps%{?PLAT}.so.%{version}
   ln -s lib${ARITH}mumps%{?PLAT}.so.%{version} ../lib${ARITH}mumps%{?PLAT}.so
done
cd -
rm -rf lib/tmp/

# build test programs
make -C examples clean
echo \
"LPORD=-L\$(LPORDDIR) -lpord\$(PLAT)
 LIBEXT=.so" >> Makefile.inc
make -C examples \
    OPTL="-pie -L../lib" all
# Make sure the user can build these later on
echo "OPTL=-pie -L%{my_libdir}" >> Makefile.inc

%install
mkdir -p %{buildroot}%{my_bindir}
mkdir -p %{buildroot}%{my_libdir}

# install libs
cp -P lib/lib*.a %{buildroot}%{my_libdir}
cp -P lib/lib*.so* %{buildroot}%{my_libdir}
%if %{with hpc} || %{without mpi} && %{without scotch}
mkdir -p %{buildroot}%{my_incdir}/mumps
mkdir -p %{buildroot}%{my_incdir}/pord
install -m 644 include/* %{buildroot}%{my_incdir}/mumps
install -m 644 libseq/*.h %{buildroot}%{my_incdir}/mumps
install -m 644 PORD/include/* %{buildroot}%{my_incdir}/pord
%endif
install -m 755 examples/*simpletest %{buildroot}%{my_bindir}
install -m 755 examples/c_example %{buildroot}%{my_bindir}
install -m 755 examples/*_save_restore %{buildroot}%{my_bindir}

%if %{with mpi}
 %if %{without hpc}
# we make a symlink to the serial lib in the parallel lib prefix
# because some scientific packages don't manage different directories
# for the serial and parallel libs
for lib in libcmumps libdmumps libsmumps libzmumps libmumps_common libmpiseq libpord ; do
     for type in .a .so .so.%{version}; do
         name=${lib}_%{!?scotch:seq}%{?scotch:scotch}${type}
         ln -s %{_libdir}/$name %{buildroot}%{my_libdir}/$name
     done
done
 %endif # hpc
%endif # mpi

%if %{with hpc}
%hpc_write_modules_files
#%%Module1.0#####################################################################

proc ModulesHelp { } {

puts stderr " "
puts stderr "This module loads the mumps library built with the %{compiler_family} compiler"
puts stderr "toolchain and the %{mpi_family}%{?mpi_ver} MPI stack."
puts stderr " "

puts stderr "\nVersion %{version}\n"

}
module-whatis "Name: %{pname} built with %{compiler_family} compiler%{?with_mpi: and %{mpi_family}%{?mpi_ver} MPI}"
module-whatis "Version: %{version}"
module-whatis "Category: runtime library"
module-whatis "%{url}"

set     version                     %{version}

depends-on scalapack

prepend-path    PATH                %{hpc_bindir}
if {[file isdirectory  %{hpc_includedir}]} {
prepend-path    INCLUDE             %{hpc_includedir}
}
prepend-path    LD_LIBRARY_PATH     %{hpc_libdir}

setenv          %{PNAME}_DIR        %{hpc_prefix}
setenv          %{PNAME}_BIN        %{hpc_bindir}
if {[file isdirectory  %{hpc_includedir}]} {
setenv          %{PNAME}_INC        %{hpc_includedir}
}
setenv          %{PNAME}_LIB        %{hpc_libdir}

EOF
%endif

# Don't want binaries in docdir
rm -rf examples/*.o examples/*simpletest examples/*_save_restore examples/c_example examples/multiple_arithmetics_example

%if !%{with mpi}
%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%else
%post -n %{libname}
/sbin/ldconfig -N %{my_libdir}

%postun -n %{libname}
/sbin/ldconfig -N %{my_libdir}
%{?with_hpc:%{hpc_module_delete_if_default}}
%endif

%files -n %{libname}
%if %{with hpc}
%{hpc_dirs}
%{hpc_modules_files}
%endif
%license LICENSE
%doc ChangeLog README VERSION CREDITS
%{my_libdir}/libcmumps%{?PLAT}.so.*
%{my_libdir}/libdmumps%{?PLAT}.so.*
%{my_libdir}/libsmumps%{?PLAT}.so.*
%{my_libdir}/libzmumps%{?PLAT}.so.*
%{my_libdir}/libmumps_common%{?PLAT}.so.*
%{my_libdir}/libpord%{?PLAT}.so.*
%if %{without mpi}
%{_libdir}/libmpiseq%{?PLAT}.so.*
%endif

%if %{with mpi} && %{without hpc}
%files  %{so_ver}-compat
 %if %{without scotch}
%{my_libdir}/lib*_seq.so.*
 %else # scotch
%{my_libdir}/lib*_scotch.so.*
 %endif # scotch
%endif # mpi && !hpc

%files devel
 %if %{with hpc} || ( %{without scotch} && %{without mpi} )
%{?with_hpc:%dir %{my_incdir}}
%{my_incdir}/mumps
%{my_incdir}/pord
 %endif
%{my_libdir}/*.so

%files devel-static
%{?with_mpi:%exclude %{my_libdir}/*%{!?scotch:_seq}%{?scotch:_scotch}.a}
%{my_libdir}/*.a

%if %{with mpi} && %{without hpc}
%files devel-static-compat
%{my_libdir}/*%{!?scotch:_seq}%{?scotch:_scotch}.a
%endif

%if %{with hpc} || ( %{without mpi} && %{without scotch} )
%files doc
%doc doc SCILAB MATLAB
%endif

%files examples
%doc Makefile.inc examples
%{my_bindir}%{!?with_hpc:/*}

%changelog
