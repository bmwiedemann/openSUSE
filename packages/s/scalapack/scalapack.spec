#
# spec file for package scalapack
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

%define pname scalapack
%define so_ver  2
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

%if "%flavor" == ""
ExclusiveArch:  do_not_build
%define package_name %pname
%else
%define mpi_flavor %{flavor}
%endif

%if "%flavor" == "openmpi5"
ExcludeArch:    %{ix86} %{arm}
# Only build header back on one multibuild for non-HPC.
# Note: For HPC the headers need to be built always.
%{bcond_without blacs_devel_headers}
%else
%{bcond_with blacs_devel_headers}
%endif

%if 0%{!?package_name:1}
%define package_name %{pname}-%{mpi_flavor}
%endif
%define libname() lib%{pname}%{so_ver}-%{mpi_flavor}
%define libblacsname() libblacs%{so_ver}-%{mpi_flavor}
%define installdir %{_libdir}/mpi/gcc/%{mpi_flavor}
%define p_includedir %{_includedir}

Name:           %{package_name}
Version:        2.2.0
Release:        0
Summary:        A subset of LAPACK routines redesigned for heterogenous computing
# This is freely distributable without any restrictions.
License:        SUSE-Public-Domain
Group:          Development/Libraries/Parallel
URL:            http://www.netlib.org/scalapack/
Source0:        http://www.netlib.org/scalapack/%{pname}-%{version}.tgz
BuildRequires:  %{mpi_flavor}-devel
BuildRequires:  blas-devel
BuildRequires:  cmake >= 2.8
BuildRequires:  gcc-fortran
BuildRequires:  lapack-devel
%if %{without blacs_devel_headers}
BuildRequires:  blacs-devel-headers
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The ScaLAPACK (or Scalable LAPACK) library includes a subset
of LAPACK routines redesigned for distributed memory MIMD
parallel computers. It is currently written in a
Single-Program-Multiple-Data style using explicit message
passing for interprocessor communication. It assumes
matrices are laid out in a two-dimensional block cyclic
decomposition.

ScaLAPACK is designed for heterogeneous computing and is
portable on any computer that supports MPI or PVM.

Like LAPACK, the ScaLAPACK routines are based on
block-partitioned algorithms in order to minimize the frequency
of data movement between different levels of the memory hierarchy.
(For such machines, the memory hierarchy includes the off-processor
memory of other processors, in addition to the hierarchy of registers,
cache, and local memory on each processor.) The fundamental building
blocks of the ScaLAPACK library are distributed memory versions (PBLAS)
of the Level 1, 2 and 3 BLAS, and a set of Basic Linear Algebra
Communication Subprograms (BLACS) for communication tasks that arise
frequently in parallel linear algebra computations. In the ScaLAPACK
routines, all interprocessor communication occurs within the PBLAS and the
BLACS. One of the design goals of ScaLAPACK was to have the ScaLAPACK
routines resemble their LAPACK equivalents as much as possible.

%package -n     blacs-devel-headers
Summary:        Development headers for BLACS
Group:          Development/Libraries/Parallel

%description -n blacs-devel-headers
This package contains headers for BLACS.

%package -n     %{libname %_vers}
Summary:        ScaLAPACK libraries compiled against %{mpi_flavor}%{?mpi_vers}
Group:          Development/Libraries/Parallel
Obsoletes:      %{name} < %{version}
Provides:       %{name} = %{version}

%description -n %{libname %_vers}
The ScaLAPACK (or Scalable LAPACK) library includes a subset
of LAPACK routines redesigned for distributed memory MIMD
parallel computers. It is currently written in a
Single-Program-Multiple-Data style using explicit message
passing for interprocessor communication. It assumes
matrices are laid out in a two-dimensional block cyclic
decomposition.

ScaLAPACK is designed for heterogeneous computing and is
portable on any computer that supports MPI or PVM.

Like LAPACK, the ScaLAPACK routines are based on
block-partitioned algorithms in order to minimize the frequency
of data movement between different levels of the memory hierarchy.
(For such machines, the memory hierarchy includes the off-processor
memory of other processors, in addition to the hierarchy of registers,
cache, and local memory on each processor.) The fundamental building
blocks of the ScaLAPACK library are distributed memory versions (PBLAS)
of the Level 1, 2 and 3 BLAS, and a set of Basic Linear Algebra
Communication Subprograms (BLACS) for communication tasks that arise
frequently in parallel linear algebra computations. In the ScaLAPACK
routines, all interprocessor communication occurs within the PBLAS and the
BLACS. One of the design goals of ScaLAPACK was to have the ScaLAPACK
routines resemble their LAPACK equivalents as much as possible.

This package contains ScaLAPACK	libraries compiled with	%{mpi_flavor}%{?mpi_vers}.

%package -n     %{libname %_vers}-devel
Summary:        Development libraries for ScaLAPACK (%{mpi_flavor}%{?mpi_vers})
Group:          Development/Libraries/Parallel
Requires:       %{libname %_vers} = %{version}
Requires:       %{mpi_flavor}-devel
%if "%{mpi_flavor}" == "openmpi5"
Provides:       lib%{pname}-openmpi-devel
%endif
Obsoletes:      %{name}-devel < %{version}
Provides:       %{name}-devel = %{version}

%description -n %{libname %_vers}-devel
This package contains development libraries for ScaLAPACK, compiled against %{mpi_flavor}%{?mpi_vers}.

%package -n     %{libname %_vers}-devel-static
Summary:        Static libraries for ScaLAPACK (%{mpi_flavor}%{?mpi_vers})
Group:          Development/Libraries/Parallel
Requires:       %{libname %_vers}-devel = %{version}
Obsoletes:      %{name}-devel-static < %{version}
Provides:       %{name}-devel-static = %{version}

%description -n %{libname %_vers}-devel-static
This package contains static libraries for ScaLAPACK, compiled against %{mpi_flavor}%{?mpi_vers}.

%package        test
Summary:        Test programs for ScaLAPACK (%{mpi_flavor}%{?mpi_vers})
Group:          Development/Libraries/Parallel

%description    test
This packages contains some test programs for ScaLAPACK compiled against
%{mpi_flavor}%{?mpi_vers}.

%package -n     %{libblacsname %_vers}
Summary:        Basic Linear Algebra Communication Subprograms
Group:          Development/Libraries/Parallel

%description -n %{libblacsname %_vers}
The BLACS (Basic Linear Algebra Communication Subprograms) project
provides a linear algebra oriented message passing interface for
a large range of distributed memory platforms.

The length of time required to implement efficient distributed memory
algorithms makes it impractical to rewrite programs for every new
parallel machine. The BLACS exist in order to make linear algebra
applications both easier to program and more portable.

%package -n     %{libblacsname %_vers}-devel
Summary:        Development libraries for BLACS (%{mpi_flavor}%{?mpi_vers})
Group:          Development/Libraries/Parallel
Requires:       %{libblacsname %_vers} = %{version}
Requires:       %{mpi_flavor}-devel
Requires:       blacs-devel-headers
Obsoletes:      blacs-%{mpi_flavor}-devel < %{version}
Provides:       blacs-%{mpi_flavor}-devel = %{version}

%description -n %{libblacsname %_vers}-devel
This package contains development libraries for BLACS, compiled against %{mpi_flavor}%{?mpi_vers}.

%package -n     %{libblacsname %_vers}-devel-static
Summary:        Development libraries for BLACS (%{mpi_flavor}%{?mpi_vers})
Group:          Development/Libraries/Parallel
Requires:       %{libblacsname %_vers}-devel = %{version}
%if "%{mpi_flavor}" == "openmpi5"
Provides:       libblacs%{so_ver}-openmpi-devel
%endif

%description -n %{libblacsname %_vers}-devel-static
This package contains static libraries for BLACS, compiled against %{mpi_flavor}%{?mpi_vers}.

%prep
%setup -q -n %{pname}-%{version}
cp SLmake.inc.example SLmake.inc
cat > %{_sourcedir}/baselibs.conf  <<EOF
%{libname %{?_vers}}
%{libname %{?_vers}}-devel
  requires -%{mpi_flavor}-<targettype>
  requires "%{libname %{?_vers}}-<targettype> = <version>"
EOF

%build
# implicit-function-declaration: https://github.com/Reference-ScaLAPACK/scalapack/issues/81
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wno-error=implicit-function-declaration -fno-strict-aliasing -std=legacy"
echo $PATH | grep -q %{mpi_flavor} || \
    PATH=/usr/%_lib/mpi/gcc/%{mpi_flavor}/bin:$PATH
%define makeargs %{?_smp_flags}
#%%cmake -DCMAKE_C_FLAGS:STRING="$RPM_OPT_FLAGS -fPIC"
#    -DCMAKE_Fortran_FLAGS:STRING="$RPM_OPT_FLAGS -fPIC" \
#    -DBUILD_SHARED_LIBS:BOOL=ON -DBUILD_STATIC_LIBS:BOOL=ON \
#    -DCMAKE_INSTALL_LIBDIR:PATH=%%{installdir}/%%_lib
#%%make_jobs -C build
CC=mpicc
FC=mpif90
MYCFLAGS="$RPM_OPT_FLAGS -fPIC"
make lib CFLAGS="${MYCFLAGS}" CCFLAGS="${MYCFLAGS}" FCFLAGS="${MYCFLAGS}" %makeargs
cd TESTING/EIG;
make FCFLAGS="$RPM_OPT_FLAGS" %{makeargs}
cd ../LIN;
make FCFLAGS="$RPM_OPT_FLAGS" %{makeargs}

cd ../..
ar crs libblacs.a BLACS/SRC/*.o BLACS/SRC/*.oo
BLACS=blacs
for libname in scalapack ${BLACS}
do
${FC} -shared -Wl,--whole-archive lib${libname}.a  -Wl,--no-whole-archive \
       -Wl,-soname,lib${libname}.so.%{version} -o lib${libname}.so.%{version}
   ln -s lib${libname}.so.%{version} lib${libname}.so
   ln -s lib${libname}.so.%{version} lib${libname}.so.%{so_ver}
done

%install

#%%make_install -C build

mkdir -p %{buildroot}%{installdir}/%_lib
mkdir -p %{buildroot}%{installdir}/%{_lib}/TESTING

for f in *.a *.so*; do
    cp -f $f %{buildroot}%{installdir}/%_lib/$f
done
cp -f TESTING/x* TESTING/*.dat %{buildroot}%{installdir}/%{_lib}/TESTING

# blacs header
%if %{with blacs_devel_headers}
mkdir -p %{buildroot}%{p_includedir}/blacs/
install -m 644 BLACS/SRC/Bdef.h %{buildroot}%{p_includedir}/blacs/
%endif

# Copy docs
cp -f README LICENSE ../

%post -n %{libname %_vers} -p /sbin/ldconfig

%postun -n %{libname %_vers} -p/sbin/ldconfig

%post -n %{libblacsname %_vers} -p /sbin/ldconfig

%postun -n %{libblacsname %_vers} -p /sbin/ldconfig

%files -n %{libname %_vers}
%license LICENSE
%doc README
%{installdir}/%_lib/libscalapack.so.*

%files test
%{installdir}/%_lib/TESTING

%files -n %{libname %_vers}-devel
%{installdir}/%_lib/libscalapack.so

%files -n %{libname %_vers}-devel-static
%{installdir}/%_lib/libscalapack.a

%if %{with blacs_devel_headers}
%files -n blacs-devel-headers
%{p_includedir}/blacs/
%endif

%files -n %{libblacsname %_vers}
%{installdir}/%_lib/libblacs.so.*

%files -n %{libblacsname %_vers}-devel
%{installdir}/%_lib/libblacs.so

%files -n %{libblacsname %_vers}-devel-static
%{installdir}/%_lib/libblacs.a

%changelog
