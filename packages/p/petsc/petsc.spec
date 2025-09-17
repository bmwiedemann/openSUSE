#
# spec file for package petsc
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Atri B. <badshah400@opensuse.org>
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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

# Please also update slepc, which is version locked with petsc
%define pname petsc
%define so_ver 3_23

ExcludeArch:    s390 s390x

# Fails to link during configure, as it omits SuperLU from the link libraries
%bcond_with hypre
# Only available as openmpi flavor, and not in Factory
%bcond_with pastix

%if "%flavor" == ""
ExclusiveArch:  do_not_build
%endif

%if "%flavor" == "serial"
%endif

%if "%flavor" == "openmpi4"
%define mpi_flavor openmpi4
%endif

%if "%flavor" == "openmpi5"
%define mpi_flavor openmpi5
ExcludeArch:    %{ix86} %{arm}
%endif

%if 0%{?mpi_flavor:1}
%bcond_without mpi
%define mpi_suffix -%{mpi_flavor}
%else
%bcond_with mpi
%endif

%define package_name %{pname}%{?mpi_suffix}
%define libname      lib%{pname}%{so_ver}%{?mpi_suffix}

%if %{without mpi}
%define p_prefix %{_prefix}/
%else
%define p_prefix %{_libdir}/mpi/gcc/%{mpi_flavor}/
%endif
%define p_libdir %{p_prefix}%_lib
%define p_include %{p_prefix}include

%define petsc_arch %_arch

Name:           %{package_name}
Summary:        Portable Extensible Toolkit for Scientific Computation
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
Version:        3.23.0
Release:        0
URL:            https://www.mcs.anl.gov/petsc/
Source:         https://web.cels.anl.gov/projects/petsc/download/release-snapshots/petsc-%{version}.tar.gz
Patch0:         Remove-rpath-test.patch
Patch1:         petsc-3.7-fix-pastix-detection.patch
Patch2:         Allow-lib64-as-library-directory-for-scalapack.patch
Patch3:         petsc-fix-libdir.patch
BuildRequires:  bison
BuildRequires:  blas-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  hdf5%{?mpi_suffix}-devel
BuildRequires:  hwloc-devel
BuildRequires:  lapack-devel
BuildRequires:  pkg-config
BuildRequires:  python3-base
BuildRequires:  suitesparse-devel >= 5.6.0
BuildRequires:  xz
BuildRequires:  pkgconfig(valgrind)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(zlib)
%if %{with hypre}
BuildRequires:  hypre%{?mpi_suffix}-devel
BuildRequires:  superlu-devel
%endif
%if %{with mpi}
BuildRequires:  %{mpi_flavor}-devel
BuildRequires:  %{mpi_flavor}-macros-devel
BuildRequires:  blacs-%{mpi_flavor}-devel
BuildRequires:  ptscotch-%{mpi_flavor}-devel
BuildRequires:  scalapack-%{mpi_flavor}-devel
 %if %{with pastix}
BuildRequires:  pastix-%{mpi_flavor}-devel
 %endif
%else
BuildRequires:  metis-devel
%endif

%description
PETSc is a suite of data structures and routines for the scalable
(parallel) solution of scientific applications modeled by partial
differential equations.

%package -n %{libname}
Summary:        PETSc shared libraries
Group:          System/Libraries
# Fixup wrong package name
Conflicts:      libpetsc3%{?mpi_suffix}

%description -n %{libname}
PETSc is a suite of data structures and routines for the scalable
(parallel) solution of scientific applications modeled by partial
differential equations.

%package %{?n_pre}devel
Summary:        Devel files for petsc
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       hdf5%{?mpi_suffix}-devel
Requires:       suitesparse-devel
Requires:       pkgconfig(yaml-0.1)
%if %{with hypre}
Requires:       hypre%{?mpi_suffix}-devel
Requires:       superlu-devel
%endif
%if %{without mpi}
Requires:       metis-devel
%else
Requires:       blacs-%{mpi_flavor}-devel
Requires:       ptscotch-%{mpi_flavor}-devel
Requires:       scalapack-%{mpi_flavor}-devel
%endif

%description %{?n_pre}devel
PETSc is a suite of data structures and routines for the scalable
(parallel) solution of scientific applications modeled by partial
differential equations.

%package doc
Summary:        Documentation for petsc
Group:          Documentation/HTML

%description doc
This package contains the documentation for petsc.

%prep

%setup -q -n petsc-%{version}
%autopatch -p1
# Fix broken MAKEFLAGS usage
sed -i -e 's/MAKEFLAGS="[^"]*"//' lib/petsc/conf/rules

# Fix shebangs in packaged scripts
find src lib config share -type f -iname \*.py -exec sed -i \
  -e '1 s@#!.*env python3@#!/usr/bin/python3@' \
  -e '1 s@#!.*env python@#!/usr/bin/python%{python3_version}@' \
  \{\} \;
find lib/petsc/bin -type f -exec sed -i \
  -e '1 s@#!.*env sh@#!/usr/bin/sh@' \
  -e '1 s@#!.*env python3@#!/usr/bin/python3@' \
  -e '1 s@#!.*env python@#!/usr/bin/python%{python3_version}@' \
  \{\} \;

# Add missing hashbangs for py scripts
sed -E -i '1{s@^@#!%{_bindir}/python%{python3_version}\n@}' \
  lib/petsc/bin/PetscBinaryIO*.py \
  lib/petsc/bin/petsc_conf.py

# Delete hashbang from non-exec script
sed -E -i '1{\@#!.*@d}' share/petsc/bin/dmnetwork_view.py

sed -E -i 's/\r$//' src/tao/leastsquares/tutorials/tomographyGenerateData.m

%build
export PETSC_DIR=${RPM_BUILD_DIR}/petsc-%{version}
export PETSC_LIB_DIR=%{p_libdir}
export PETSC_ARCH=%petsc_arch
%{?with_mpi:%setup_openmpi}
%ifarch ppc64le ppc64 s390 aarch64 x86_64
export ARCHCFLAGS=-fPIC
%endif

%{_bindir}/python%{python3_version} ./configure \
  --COPTFLAGS="$RPM_OPT_FLAGS $ARCHCFLAGS" \
  --FOPTLAGS="$RPM_OPT_FLAGS $ARCHCFLAGS" \
  --CXXOPTFLAGS="$RPM_OPT_FLAGS $ARCHCFLAGS" \
  --prefix=%{p_prefix} \
  --with-batch=0 \
  --with-clanguage=C++ \
  --with-c-support \
  --with-fortran-interfaces=1 \
  --with-debugging=no \
  --with-hdf5=1 \
  --with-python-exec=%{_bindir}/python%{python3_version} \
  --with-shared-libraries \
  --with-suitesparse=1 \
  --with-yaml=1 \
  %if %{with hypre}
  --with-hypre=1 \
  --with-superlu=1 \
  %endif
  %if %{without mpi}
  --with-mpi=0 \
  %else
  --with-mpi=1 \
  --with-blacs=1 \
  --with-pastix=%{?with_pastix:1}%{!?with_pastix:0} \
  --with-ptscotch=1 \
  --with-scalapack=1 \
  %endif
|| { cat configure.log; exit 1; }

%make_build

%install
export PETSC_DIR=${RPM_BUILD_DIR}/petsc-%{version}
export PETSC_LIB_DIR=%{p_libdir}
export PETSC_ARCH=%{petsc_arch}
%make_install

find %{buildroot}%{p_prefix}/share/petsc/examples/src -type f -ipath '*/output/*out' -delete
rm -f %{buildroot}%{p_libdir}/conf/*.log
rm -f %{buildroot}%{p_libdir}/conf/.DIR

rm -rf %{buildroot}%{p_libdir}/conf/*.init
rm -rf %{buildroot}%{p_libdir}/conf/*.py
rm -rf %{buildroot}%{p_libdir}/conf/modules

# clean up non-include files
find %{buildroot}%{p_include} -name \*.html  -exec rm {} \;
find %{buildroot}%{p_include} -name makefile -exec rm {} \;

sed -i \
  -e 's!^\(#define PETSC_LIB_DIR\).*$!\1 "'%{p_libdir}'"!' \
  -e 's!^\(#define PETSC_DIR\).*$!\1 "'%{p_prefix}'"!' \
  %{buildroot}%{p_include}/petscconf.h

# remove buildroot
find %{buildroot}%{p_libdir}/{conf,bin}/ -type f -print0 | \
while IFS= read -r -d $'\0' line ; do
  if file -e soft $line | grep -q "text" ; then
    sed -i -e 's!%{buildroot}!!g' $line
  fi
done

for i in $(find %{buildroot}%{p_prefix}/share \( -perm /a+x -and -type f \) ) ; do
    grep -m 1 -q "^#!" $i || chmod a-x $i
done
chmod a+x %{buildroot}%{p_libdir}/petsc/bin/{configureTAS,extract,tasClasses}.py

# Remove CPU count from petscvariables, https://gitlab.com/petsc/petsc/-/issues/1315
sed -i -e '/^MAKE_/ { /MAKE_NP/ d ; /MAKE_LOAD/ d ; /MAKE_TEST_NP/ d }; /^NPMAX/ d' \
  %{buildroot}%{p_libdir}/petsc/conf/petscvariables

%fdupes %{buildroot}%{p_include}
%fdupes %{buildroot}%{p_libdir}
%fdupes %{buildroot}%{p_prefix}/share/petsc/examples

%check
%if %{with mpi}
%setup_openmpi
%endif
export LD_LIBRARY_PATH+=:%{buildroot}%{p_libdir}
%make_build check

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%{p_libdir}/*.so.*
%{p_prefix}/share/petsc/
%exclude %{p_prefix}/share/petsc/examples
%exclude %{p_prefix}/share/petsc/saws

%files %{?n_pre}devel
%exclude %{p_libdir}/petsc/bin/saws
%{p_include}/*.mod
%{p_include}/petsc/
%{p_include}/petsc*.h*
%{p_libdir}/*.so
%{p_libdir}/petsc/
%if %{with mpi}
%dir %{p_libdir}/pkgconfig
%endif
%{p_libdir}/pkgconfig/*.pc
%doc %{p_prefix}/share/petsc/examples

%changelog
