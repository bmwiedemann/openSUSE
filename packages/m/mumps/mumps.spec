#
# spec file for package mumps
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

%define pname mumps
%define so_ver 5_3_5
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

%define PNAME %(echo %{pname} | tr [a-z] [A-Z])
%define _ver %(echo %{ver} | tr . _)

%if "%flavor" == ""
%define package_name %{pname}
ExclusiveArch:  do_not_build
%endif

%if "%{flavor}" == "serial"
# Stub MPI library
%define mumps_f77_mpilibs '-lmpiseq'
%endif

%if "%{flavor}" == "scotch-serial"
# Stub MPI library
%define mumps_f77_mpilibs '-lmpiseq'
%bcond_without scotch
%endif

%if "%{flavor}" == "openmpi4"
%define mpi_flavor  openmpi4
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%endif

%if "%{flavor}" == "openmpi5"
%define mpi_flavor  openmpi5
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
ExcludeArch:    %{ix86} %{arm}
%endif

%if "%{flavor}" == "mvapich2"
%define mpi_flavor  mvapich2
%define mumps_f77_mpilibs -lfmpich -lmpich
%endif

%if "%{flavor}" == "scotch-openmpi4"
%define mpi_flavor  openmpi4
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%bcond_without scotch
%endif

%if "%{flavor}" == "scotch-openmpi5"
%define mpi_flavor  openmpi5
%define mumps_f77_mpilibs -lmpi_mpifh -lmpi
%bcond_without scotch
ExcludeArch:    %{ix86} %{arm}
%endif

%if "%{flavor}" == "scotch-mvapich2"
%define mpi_flavor  mvapich2
%define mumps_f77_mpilibs -lfmpich -lmpich
%bcond_without scotch
%endif

%ifarch i586 s390 ppc armv7l
ExclusiveArch:  do_not_build
%endif

%{?mpi_flavor:%{bcond_without mpi}}%{!?mpi_flavor:%{bcond_with mpi}}

%if %{with scotch}
 %if %{with mpi}
  %define scotch ptscotch
 %else
 %define scotch scotch
 %endif
%endif

%if %{without mpi}
%define my_prefix %_prefix
%define my_bindir %_bindir
%define my_libdir %_libdir
%define my_incdir %_includedir
%define my_datadir %_datadir
%else
%define my_suffix  -%{mpi_flavor}
%define my_prefix %{_libdir}/mpi/gcc/%{mpi_flavor}
%define my_bindir %{my_prefix}/bin
%define my_libdir %{my_prefix}/%{_lib}/
%define my_incdir %{my_prefix}/include/
%define my_datadir %{my_prefix}/share/
%endif
%define package_name %{pname}%{?scotch:-%{scotch}}%{?my_suffix}
%define libname lib%{pname}%{?scotch:-%{scotch}}%{?so_ver}%{?my_suffix}

Summary:        A Multifrontal Massively Parallel Sparse direct Solver
License:        CECILL-C
Group:          Productivity/Scientific/Math
Name:           %{package_name}
Version:        5.3.5
Release:        0
URL:            http://mumps.enseeiht.fr/
Source0:        http://mumps.enseeiht.fr/MUMPS_%{version}.tar.gz#/%{pname}-%{version}.tar.gz
Source1:        Makefile.inc
BuildRequires:  gcc-fortran
%{?with_scotch:BuildRequires:  %{scotch}%{?with_mpi:-%{mpi_flavor}}-devel}
 %if %{with mpi}
BuildRequires:  %{mpi_flavor}-devel
BuildRequires:  libblacs2-%{mpi_flavor}-devel
BuildRequires:  scalapack-%{mpi_flavor}-devel
 %endif # mpi
BuildRequires:  blas-devel
BuildRequires:  lapack-devel

%description
MUMPS implements a direct solver for large sparse linear systems, with a
particular focus on symmetric positive definite matrices.  It can
operate on distributed matrices e.g. over a cluster.  It has Fortran and
C interfaces, and can interface with ordering tools such as Scotch.

%package -n %{libname}
Summary:        A MUltifrontal Massively Parallel Sparse direct Solver
Group:          System/Libraries
%{?with_mpi:Recommends:       %{libname}-compat = %{version}}
# Explicitly include this library here:
# the solver doesn't have enough information to pick the correct MPI flavor
%{?with_mpi:Requires:         libblacs2-%{mpi_flavor}}
Conflicts:      lib%{pname}%{?scotch:-%{scotch}}5%{?my_suffix} >= 5.3.5

%description -n %{libname}
MUMPS implements a direct solver for large sparse linear systems, with a
particular focus on symmetric positive definite matrices.  It can
operate on distributed matrices e.g. over a cluster.  It has Fortran and
C interfaces, and can interface with ordering tools such as Scotch.

%if %{!with mpi}
This package contains the sequential library%{?scotch: with Scotch support enabled}.
%else
This package contains the parallel library with %{mpi_flavor} and %{?scotch: with Scotch support enabled}.
%endif

%package -n %{libname}-compat
Summary:        A MUltifrontal Massively Parallel Sparse direct Solver
Group:          System/Libraries
Requires:       lib%{pname}%{?scotch:-scotch}%{so_ver} = %{version}
%if %{with mpi}
# Install link targets for non-HPC MPI compat links from the MPI libdir - see below.
BuildRequires:  %{pname}%{?scotch:-scotch}-devel-static = %version
BuildRequires:  lib%{pname}%{?scotch:-scotch}%{so_ver} = %{version}
%endif

%description -n %{libname}-compat
MUMPS implements a direct solver for large sparse linear systems, with a
particular focus on symmetric positive definite matrices.  It can
operate on distributed matrices e.g. over a cluster.  It has Fortran and
C interfaces, and can interface with ordering tools such as Scotch.

This package provides links to the serial libraries from the MPI library
directory MUMPS built for %{mpi_flavor}.

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
This package contains the parallel library with %{mpi_flavor} and %{?scotch: with Scotch support enabled}.
%endif

%package devel
Summary:        Files needed for developing mumps based applications
Group:          Development/Libraries/Parallel
Requires:       %{libname} = %version
%if %{with mpi} || %{with scotch}
Requires:       mumps-devel = %{version}
%endif
%if %{with mpi}
Requires:       %{mpi_flavor}-devel
Requires:       scalapack-%{mpi_flavor}-devel
 %if %{with scotch}
Requires:       mumps-scotch-devel = %{version}
Requires:       ptscotch-%{mpi_flavor}-devel
 %endif
%else # mpi
Requires:       blas-devel
Requires:       lapack-devel
%{?with_scotch:Requires:       scotch-devel}
%endif # mpi
Recommends:     gcc-fortran

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
library directory MUMPS built for %{mpi_flavor}.

%package examples
Summary:        Test programs and examples for mumps
Group:          Documentation/Other
Requires:       %{libname} = %version
Provides:       mumps(examples)(%{?mpi_family}) = %version
Conflicts:      otherproviders(mumps(examples)(%{?mpi_family}))

%description examples
MUMPS implements a direct solver for large sparse linear systems, with a
particular focus on symmetric positive definite matrices.  It can
operate on distributed matrices e.g. over a cluster.  It has Fortran and
C interfaces, and can interface with ordering tools such as Scotch.

This packages contains some test and examples programs for mumps. In addition,
matlab and scilab extensions are provided in /usr/share/doc/packages/mumps.

%prep
%autosetup -n %{PNAME}_%{version}

%build

export SUSE_ASNEEDED=0

%{?with_mpi: source %{my_bindir}/mpivars.sh}

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

%define LIBBLAS -lblas -llapack
%define LAPACK -llapack

%if %{with mpi}
# Set LD_LIBRARY_PATH and PATH
 %define C_C mpicc
 %define F_C mpif77 -std=legacy
 %define F_L mpif77
 %define SCALAP -lscalapack -lblacs
 %define MUMPS_LIBF77 -L%{my_libdir} %{?mumps_f77_mpilibs}
 %define INCPAR -I%{my_incdir}
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
%if %{without mpi} && %{without scotch}
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
# we make a symlink to the serial lib in the parallel lib prefix
# because some scientific packages don't manage different directories
# for the serial and parallel libs
for lib in libcmumps libdmumps libsmumps libzmumps libmumps_common libmpiseq libpord ; do
     for type in .a .so .so.%{version}; do
         name=${lib}_%{!?scotch:seq}%{?scotch:scotch}${type}
         ln -s %{_libdir}/$name %{buildroot}%{my_libdir}/$name
     done
done
%endif # mpi

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
%endif

%files -n %{libname}
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

%if %{with mpi}
%files -n %{libname}-compat
 %if %{without scotch}
%{my_libdir}/lib*_seq.so.*
 %else # scotch
%{my_libdir}/lib*_scotch.so.*
 %endif # scotch
%endif # mpi

%files devel
%if %{without scotch} && %{without mpi}
%{my_incdir}/mumps
%{my_incdir}/pord
%endif
%{my_libdir}/*.so

%files devel-static
%{?with_mpi:%exclude %{my_libdir}/*%{!?scotch:_seq}%{?scotch:_scotch}.a}
%{my_libdir}/*.a

%if %{with mpi}
%files devel-static-compat
%{my_libdir}/*%{!?scotch:_seq}%{?scotch:_scotch}.a
%endif

%if %{without mpi} && %{without scotch}
%files doc
%doc doc SCILAB MATLAB
%endif

%files examples
%doc Makefile.inc examples
%{my_bindir}/*

%changelog
