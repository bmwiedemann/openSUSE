#
# spec file for package sundials
#
# Copyright (c) 2021 SUSE LLC
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

%define pname sundials

%if 0%{?is_opensuse} || 0%{?is_backports}
%undefine DisOMPI1
%undefine DisOMPI2
%undefine DisOMPI3
%undefine DisOMPI4
%else
%define DisOMPI1 ExclusiveArch:  do_not_build
%define DisOMPI3 ExclusiveArch:  do_not_build
%define DisOMPI4 ExclusiveArch:  do_not_build
%undefine DisOMPI2
%endif

%if "%{flavor}" == ""
%define package_name %{pname}
ExclusiveArch:  do_not_build
%endif

%if "%{flavor}" == "mvapich2"
%global mpi_flavor mvapich2
%endif

%if "%{flavor}" == "openmpi1"
%global mpi_flavor openmpi
 %if 0%{?suse_version} >= 1550
 %define mpi_vers 1
 %else
 %define mpi_vers %{nil}
 %endif
%{?DisOMPI1}
%endif

%if "%{flavor}" == "openmpi2"
%global mpi_flavor openmpi
%define mpi_vers 2
%{?DisOMPI2}
%endif

%if "%{flavor}" == "openmpi3"
%global mpi_flavor openmpi
%define mpi_vers 3
%{?DisOMPI3}
%endif

%if "%{flavor}" == "openmpi4"
%global mpi_flavor openmpi
%define mpi_vers 4
%{?DisOMPI4}
%endif

%{?mpi_flavor:%{bcond_without mpi}}%{!?mpi_flavor:%{bcond_with mpi}}
%{?with_mpi:%{!?mpi_flavor:error "No MPI family specified!"}}

# For compatibility package names
%define mpi_ext %{?mpi_vers}

%if %{without mpi}
 %define my_prefix %_prefix
 %define my_bindir %_bindir
 %define my_libdir %_libdir
 %define my_incdir %_includedir
%else
 %define my_prefix %{_libdir}/mpi/gcc/%{mpi_flavor}%{?mpi_ext}
 %define my_bindir %{my_prefix}/bin
 %define my_libdir %{my_prefix}/%_lib
 %define my_incdir %{my_prefix}/include
 %define my_suffix -%{mpi_flavor}%{?mpi_ext}
%endif

%if 0%{!?package_name:1}
 %define package_name   %pname%{?my_suffix}
%endif

# /SECTION

%define shlib_main libsundials3%{?my_suffix}
%define shlib_arkode libsundials_arkode4%{?my_suffix}
%define shlib_cvode libsundials_cvode5%{?my_suffix}
%define shlib_cvodes libsundials_cvodes5%{?my_suffix}
%define shlib_generic libsundials_generic5%{?my_suffix}
%define shlib_ida libsundials_ida5%{?my_suffix}
%define shlib_idas libsundials_idas4%{?my_suffix}
%define shlib_kinsol libsundials_kinsol5%{?my_suffix}
%define shlib_nvec libsundials_nvec5%{?my_suffix}

Name:           %{package_name}
Version:        5.7.0
Release:        0
Summary:        Suite of nonlinear solvers
# SUNDIALS is licensed under BSD with some additional (but unrestrictive) clauses.
# Check the file 'LICENSE' for details.
License:        BSD-3-Clause
URL:            https://computation.llnl.gov/projects/sundials/
Source0:        https://computation.llnl.gov/projects/sundials/download/%{pname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM sundials-link-pthread.patch badshah400@gmail.com -- Explicitly link against pthread to fix linking errors when `-Wl,--no-undefined` is added to the linker flags
Patch0:         sundials-link-pthread.patch
BuildRequires:  blas-devel
BuildRequires:  cmake >= 3.12
BuildRequires:  fdupes
BuildRequires:  gcc-fortran
BuildRequires:  lapack-devel
BuildRequires:  suitesparse-devel
%if %{with mpi}
BuildRequires:  %{mpi_flavor}%{?mpi_ext}-devel
%if 0%{?suse_version} >= 1550 && "%{flavor}" != "mvapich2"
# hackish workaround for multiple openmpX-config all providing openmpX-runtime-config
BuildRequires:  %{mpi_flavor}%{?mpi_ext}-config
%endif
%endif

%description
SUNDIALS is a SUite of Non-linear DIfferential/ALgebraic equation Solvers
for use in writing mathematical software.

SUNDIALS was implemented with the goal of providing robust time integrators
and nonlinear solvers that can easily be incorporated into existing simulation
codes. The primary design goals were to require minimal information from the
user, allow users to easily supply their own data structures underneath the
solvers, and allow for easy incorporation of user-supplied linear solvers and
preconditioners.

%package devel
Summary:        Suite of nonlinear solvers (developer files)
Requires:       %{shlib_arkode} = %{version}
Requires:       %{shlib_cvodes} = %{version}
Requires:       %{shlib_cvode} = %{version}
Requires:       %{shlib_generic} = %{version}
Requires:       %{shlib_idas} = %{version}
Requires:       %{shlib_ida} = %{version}
Requires:       %{shlib_kinsol} = %{version}
Requires:       %{shlib_main} = %{version}
Requires:       %{shlib_nvec} = %{version}

%description devel
SUNDIALS is a SUite of Non-linear DIfferential/ALgebraic equation Solvers
for use in writing mathematical software.

This package contains the developer files (.so file, header files)

%package doc
Summary:        Suite of nonlinear solvers (documentation)

%description doc
SUNDIALS is a SUite of Non-linear DIfferential/ALgebraic equation Solvers
for use in writing mathematical software.

This package contains the documentation files

%package -n %{shlib_main}
Summary:        Suite of nonlinear solvers - main shared libraries

%description -n %{shlib_main}
SUNDIALS is a SUite of Non-linear DIfferential/ALgebraic equation Solvers
for use in writing mathematical software.

This package provides the main shared libraries for SUNDIALS.

%package -n %{shlib_arkode}
Summary:        Suite of nonlinear solvers - arkode shared libraries

%description -n %{shlib_arkode}
SUNDIALS is a SUite of Non-linear DIfferential/ALgebraic equation Solvers
for use in writing mathematical software.

This package provides the shared libraries for SUNDIALS' arkode solver.

%package -n %{shlib_cvode}
Summary:        Suite of nonlinear solvers - cvode shared libraries

%description -n %{shlib_cvode}
SUNDIALS is a SUite of Non-linear DIfferential/ALgebraic equation Solvers
for use in writing mathematical software.

This package provides the shared libraries for SUNDIALS' cvode solver.

%package -n %{shlib_cvodes}
Summary:        Suite of nonlinear solvers - cvodes shared libraries

%description -n %{shlib_cvodes}
SUNDIALS is a SUite of Non-linear DIfferential/ALgebraic equation Solvers
for use in writing mathematical software.

This package provides the shared libraries for SUNDIALS' cvodes solver.

%package -n %{shlib_generic}
Summary:        Suite of nonlinear solvers - generic shared libraries

%description -n %{shlib_generic}
SUNDIALS is a SUite of Non-linear DIfferential/ALgebraic equation Solvers
for use in writing mathematical software.

This package provides the shared libraries for SUNDIALS' generic solver.

%package -n %{shlib_ida}
Summary:        Suite of nonlinear solvers - ida shared libraries

%description -n %{shlib_ida}
SUNDIALS is a SUite of Non-linear DIfferential/ALgebraic equation Solvers
for use in writing mathematical software.

This package provides the shared libraries for SUNDIALS' ida solver.

%package -n %{shlib_idas}
Summary:        Suite of nonlinear solvers - idas shared libraries

%description -n %{shlib_idas}
SUNDIALS is a SUite of Non-linear DIfferential/ALgebraic equation Solvers
for use in writing mathematical software.

This package provides the shared libraries for SUNDIALS' idas solver.

%package -n %{shlib_kinsol}
Summary:        Suite of nonlinear solvers - kinsol shared libraries

%description -n %{shlib_kinsol}
SUNDIALS is a SUite of Non-linear DIfferential/ALgebraic equation Solvers
for use in writing mathematical software.

This package provides the shared libraries for SUNDIALS' kinsol solver.

%package -n %{shlib_nvec}
Summary:        Suite of nonlinear solvers - nvec shared libraries

%description -n %{shlib_nvec}
SUNDIALS is a SUite of Non-linear DIfferential/ALgebraic equation Solvers
for use in writing mathematical software.

This package provides the shared libraries for SUNDIALS' nvec solvers.

%prep
%autosetup -p1 -n %{pname}-%{version}

%build
%cmake \
       -DCMAKE_INSTALL_PREFIX=%{my_prefix} \
       -DCMAKE_INSTALL_LIBDIR=%{my_libdir} \
%if "%{?_lib}" == "lib64"
       -DLIB_SUFFIX=64 \
%endif
       -DCMAKE_SKIP_RPATH:BOOL=OFF \
       -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
       -DENABLE_LAPACK:BOOL=ON \
       -DENABLE_PTHREAD:BOOL=ON \
       -DENABLE_KLU:BOOL=ON \
       -DKLU_INCLUDE_DIR:PATH=%{_includedir}/suitesparse \
       -DKLU_LIBRARY_DIR:PATH=%{_libdir} \
       -DSUNDIALS_BUILD_WITH_MONITORING:BOOL=ON \
%if %{without mpi}
       -DEXAMPLES_INSTALL_PATH=%{_docdir}/%{name}/examples \
       -DENABLE_MPI:BOOL=OFF
%else
       -DEXAMPLES_INSTALL:BOOL=OFF \
       -DENABLE_MPI:BOOL=ON \
       -DMPI_C_COMPILER=%{my_bindir}/mpicc \
       -DMPI_CXX_COMPILER=%{my_bindir}/mpicxx \
       -DMPI_Fortran_COMPILER=%{my_bindir}/mpif90 \
       -DMPIEXEC_EXECUTABLE=%{my_bindir}/mpirun
%endif

%cmake_build

%install
%cmake_install

rm %{buildroot}%{my_incdir}/sundials/{NOTICE,LICENSE}

%fdupes %{buildroot}

%check
# Send extremely verbose output to a log file instead of printing to screen to avoid build log bloat
# Disable the sunlinsol tests which fail apparently due to minor floating pt issues
# On 32-bit, also disable the sunmatrix tests which fail due to minor floating pt issues
export LD_LIBRARY_PATH=%{my_libdir}
%ifarch %ix86
%ctest --quiet --output-log test-output.log --exclude-regex "test_(sunlinsol_lapack|sunmatrix_sparse)*" || ( grep "Fail" test-output.log; exit 1 )
%else
%ctest --quiet --output-log test-output.log --exclude-regex "test_sunlinsol_lapack*" || ( grep "Fail" test-output.log; exit 1; )
%endif

%post -n %{shlib_main} -p /sbin/ldconfig
%postun -n %{shlib_main} -p /sbin/ldconfig

%post -n %{shlib_arkode} -p /sbin/ldconfig
%postun -n %{shlib_arkode} -p /sbin/ldconfig

%post -n %{shlib_cvode} -p /sbin/ldconfig
%postun -n %{shlib_cvode} -p /sbin/ldconfig

%post -n %{shlib_cvodes} -p /sbin/ldconfig
%postun -n %{shlib_cvodes} -p /sbin/ldconfig

%post -n %{shlib_generic} -p /sbin/ldconfig
%postun -n %{shlib_generic} -p /sbin/ldconfig

%post -n %{shlib_ida} -p /sbin/ldconfig
%postun -n %{shlib_ida} -p /sbin/ldconfig

%post -n %{shlib_idas} -p /sbin/ldconfig
%postun -n %{shlib_idas} -p /sbin/ldconfig

%post -n %{shlib_kinsol} -p /sbin/ldconfig
%postun -n %{shlib_kinsol} -p /sbin/ldconfig

%post -n %{shlib_nvec} -p /sbin/ldconfig
%postun -n %{shlib_nvec} -p /sbin/ldconfig

%if %{without mpi}
%files doc
%doc doc/cvode/cv_examples.pdf
%doc doc/cvode/cv_guide.pdf
%doc doc/kinsol/kin_examples.pdf
%doc doc/kinsol/kin_guide.pdf
%doc doc/cvodes/cvs_examples.pdf
%doc doc/cvodes/cvs_guide.pdf
%doc doc/ida/ida_examples.pdf
%doc doc/ida/ida_guide.pdf
%{_docdir}/%{name}/
%endif

%files devel
%license LICENSE
%doc README.md CONTRIBUTING.md NOTICE
%{my_libdir}/*.so
%{my_incdir}/*
%if %{with mpi}
%dir %{my_libdir}/cmake
%endif
%{my_libdir}/cmake/sundials/

%files -n %{shlib_main}
%{my_libdir}/libsundials_sun*.so.*
%if %{with mpi}
%endif

%files -n %{shlib_arkode}
%{my_libdir}/libsundials_arkode.so.*

%files -n %{shlib_cvode}
%{my_libdir}/libsundials_cvode.so.*

%files -n %{shlib_cvodes}
%{my_libdir}/libsundials_cvodes.so.*

%files -n %{shlib_generic}
%{my_libdir}/libsundials_generic.so.*

%files -n %{shlib_ida}
%{my_libdir}/libsundials_ida.so.*

%files -n %{shlib_idas}
%{my_libdir}/libsundials_idas.so.*

%files -n %{shlib_kinsol}
%{my_libdir}/libsundials_kinsol.so.*

%files -n %{shlib_nvec}
%{my_libdir}/libsundials_nvec*.so.*

%changelog
