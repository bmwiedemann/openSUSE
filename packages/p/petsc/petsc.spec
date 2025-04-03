#
# spec file for package petsc
#
# Copyright (c) 2025 SUSE LLC
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
%define so_ver 3_22

ExcludeArch:    s390 s390x

# Fails to link during configure, as it omits SuperLU from the link libraries
%bcond_with hypre
# Only available as openmpi flavor, and not in Factory
%bcond_with pastix

%define python_ver 3

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

%define package_name %{pname}%{?with_mpi:-%{mpi_flavor}}
%define libname      lib%{pname}%{so_ver}%{?with_mpi:-%{mpi_flavor}}

%if 0%{?mpi_flavor:1}
%{bcond_without mpi}
%else
%{bcond_with mpi}
%endif

%if %{without mpi}
%define p_base %{_prefix}/
%else
%define p_base %{_libdir}/mpi/gcc/%{mpi_flavor}/
%endif
%define p_prefix %{p_libdir}/petsc/%{version}/%petsc_arch
%define p_libdir %{p_base}%_lib
%define p_include %{p_prefix}/include

%define petsc_arch linux-gnu-c-opt

Name:           %{package_name}
Summary:        Portable Extensible Toolkit for Scientific Computation
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
Version:        3.22.2
Release:        0

Source:         https://web.cels.anl.gov/projects/petsc/download/release-snapshots/petsc-%{version}.tar.gz
Patch0:         Remove-rpath-test.patch
Patch1:         petsc-3.7-fix-pastix-detection.patch
Patch2:         Allow-lib64-as-library-directory-for-scalapack.patch
URL:            https://www.mcs.anl.gov/petsc/
BuildRequires:  fdupes
BuildRequires:  hwloc-devel
BuildRequires:  pkg-config
BuildRequires:  python3-base
BuildRequires:  pkgconfig(yaml-0.1)

BuildRequires:  Modules
BuildRequires:  blas-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  lapack-devel
BuildRequires:  suitesparse-devel >= 5.6.0

%if %{with mpi}
BuildRequires:  %{mpi_flavor}-devel
BuildRequires:  blacs-%{mpi_flavor}-devel
BuildRequires:  hdf5-%{mpi_flavor}-devel
 %if %{with hypre}
BuildRequires:  hypre-%{mpi_flavor}-devel
BuildRequires:  superlu-devel
 %endif
BuildRequires:  ptscotch-%{mpi_flavor}-devel
BuildRequires:  ptscotch-parmetis-%{mpi_flavor}-devel
#!BuildIgnore:  metis-devel
 %if %{with pastix}
BuildRequires:  pastix-%{mpi_flavor}-devel
 %endif
BuildRequires:  scalapack-%{mpi_flavor}-devel
%else
BuildRequires:  metis-devel
%endif

BuildRequires:  valgrind-devel
BuildRequires:  xz
BuildRequires:  zlib-devel

%description
PETSc is a suite of data structures and routines for the scalable
(parallel) solution of scientific applications modeled by partial
differential equations.

%package -n %{libname}
Summary:        PETSc shared libraries
Group:          System/Libraries
# Fixup wrong package name
Conflicts:      libpetsc3%{?with_mpi:-%{mpi_flavor}}

%description -n %{libname}
PETSc is a suite of data structures and routines for the scalable
(parallel) solution of scientific applications modeled by partial
differential equations.

%package %{?n_pre}devel
Summary:        Devel files for petsc
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       Modules
Requires:       suitesparse-devel
Requires:       pkgconfig(yaml-0.1)
%if %{without mpi}
Requires:       metis-devel
%else
Requires:       blacs-%{mpi_flavor}-devel
Requires:       hdf5-%{mpi_flavor}-devel
Requires:       hypre-%{mpi_flavor}-devel
Requires:       ptscotch-%{mpi_flavor}-devel
Requires:       ptscotch-parmetis-%{mpi_flavor}-devel
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
  -e '1 s@#!.*env python@#!/usr/bin/python%{python_ver}@' \
  \{\} \;
find lib/petsc/bin -type f -exec sed -i \
  -e '1 s@#!.*env sh@#!/usr/bin/sh@' \
  -e '1 s@#!.*env python3@#!/usr/bin/python3@' \
  -e '1 s@#!.*env python@#!/usr/bin/python%{python_ver}@' \
  \{\} \;

%build

export PETSC_DIR=${RPM_BUILD_DIR}/petsc-%{version}
export PETSC_ARCH=%petsc_arch
%{?with_mpi:export LD_LIBRARY_PATH=%{p_libdir}}
%ifarch ppc64le ppc64 s390 aarch64 x86_64
export ARCHCFLAGS=-fPIC
%endif

python%{python_ver} ./config/configure.py \
  --CFLAGS="$RPM_OPT_FLAGS $ARCHCFLAGS" \
  --FFLAGS="$RPM_OPT_FLAGS $ARCHCFLAGS" \
  --CXXFLAGS="$RPM_OPT_FLAGS $ARCHCFLAGS" \
  --prefix=%{p_prefix} \
  --with-clanguage=C++ \
  --with-c-support \
  --with-fortran-interfaces=1 \
  --with-debugging=no \
  --with-python-exec=python%{python_ver} \
  --with-shared-libraries \
  --with-batch=0 \
  --with-yaml=1 \
  --with-suitesparse=1 \
  --with-suitesparse-lib=[%{_libdir}/libklu.so,%{_libdir}/libumfpack.so,%{_libdir}/libcholmod.so,%{_libdir}/libcolamd.so,%{_libdir}/libccolamd.so,%{_libdir}/libcamd.so,%{_libdir}/libamd.so,%{_libdir}/libspqr.so,%{_libdir}/libsuitesparseconfig.so] \
  --with-suitesparse-include=%{_includedir}/suitesparse \
 %if %{without mpi}
  --with-mpi=0 \
 %else
  --with-mpi=1 \
  --with-mpi-dir=%{p_base}\
  --with-blacs=1 \
  --with-blacs-include=%{p_base}/include \
  --with-blacs-lib=[%{p_libdir}/libblacs.so] \
  %if %{with pastix}
  --with-pastix=1 \
  --with-pastix-pkg-config=%{p_libdir}/pkgconfig \
  %endif
  --with-ptscotch=1 \
  --with-ptscotch-include=%{p_base}/include \
  --with-ptscotch-lib=[%{p_libdir}/libptscotch.so,%{p_libdir}/libptscotcherr.so,%{p_libdir}/libptscotcherrexit.so,%{p_libdir}/libptscotchparmetis.so] \
  --with-scalapack=1 \
  --with-scalapack-include=%{p_base}/include \
  --with-scalapack-lib=[%{p_libdir}/libscalapack.so] \
  %if %{with hypre}
  --with-superlu=1 \
  --with-hypre=1 \
  --with-hypre-include=%{p_base}/include/hypre \
  --with-hypre-lib=[%{p_libdir}/libHYPRE.so] \
  %endif
  --with-hdf5=1 \
  --with-hdf5-lib=[%{p_libdir}/libhdf5.so] \
  --with-hdf5-include=%{p_base}/include \
        || cat configure.log
 %endif

%make_build

%install
export PETSC_DIR=${RPM_BUILD_DIR}/petsc-%{version}
export PETSC_ARCH=%petsc_arch

make install DESTDIR=%{buildroot}

find %{buildroot}%{p_prefix}/share/petsc/examples/src -type f -ipath '*/output/*out' -delete
rm -f %{buildroot}%{p_prefix}/lib/petsc/conf/*.log
rm -f %{buildroot}%{p_prefix}/lib/petsc/conf/.DIR

rm -rf %{buildroot}%{p_prefix}/lib/petsc/conf/*.init
rm -rf %{buildroot}%{p_prefix}/lib/petsc/conf/*.py
rm -rf %{buildroot}%{p_prefix}/lib/petsc/conf/modules

# create symlink for libs between %%libdir and petscdir
pushd %{buildroot}%{p_libdir}
for f in petsc/%{version}/%petsc_arch/lib/*.so*; do
   ln -s $f .
done
popd

# Module files
mkdir -p %{buildroot}/usr/share/modules/%{name}-%{petsc_arch}
cat << EOF > %{buildroot}/usr/share/modules/%{name}-%{petsc_arch}/%version%{?with_mpi:-%{mpi_flavor}}
#%%Module
proc ModulesHelp { } {
        global dotversion
        puts stderr "\tLoads the %{name}-%{petsc_arch} %version Environment"
}

module-whatis  "Loads the %{name}-%{petsc_arch} %version Environment."
conflict %{name}-%{petsc_arch}
setenv PETSC_ARCH %{petsc_arch}
setenv PETSC_DIR  %{p_libdir}/petsc/%{version}/%{petsc_arch}
prepend-path LD_LIBRARY_PATH %{p_libdir}/petsc/%{version}/%{petsc_arch}/lib

EOF

# clean up non-include files
find %{buildroot}%{p_include} -name \*.html  -exec rm {} \;
find %{buildroot}%{p_include} -name makefile -exec rm {} \;

sed -i \
	-e 's!^\(#define PETSC_LIB_DIR\).*$!\1 "'%{p_prefix}/lib'"!' \
	-e 's!^\(#define PETSC_DIR\).*$!\1 "'%{p_prefix}'"!' \
	%{buildroot}%{p_include}/petscconf.h

# remove buildroot
find %{buildroot}%{p_prefix}/lib/petsc/{conf,bin}/ -type f -print0 | \
while IFS= read -r -d $'\0' line ; do
  if file -e soft $line | grep -q "text" ; then
    sed -i -e 's!%{buildroot}!!g' $line
  fi
done

for i in $(find %{buildroot}%{p_prefix}/share \( -perm /a+x -and -type f \) ) ; do
    grep -m 1 -q "^#!" $i || chmod a-x $i
done
chmod a+x $i %{buildroot}%{p_prefix}/lib/petsc/bin/*

# Remove CPU count from petscvariables, https://gitlab.com/petsc/petsc/-/issues/1315
sed -i -e '/^MAKE_/ { /MAKE_NP/ d ; /MAKE_LOAD/ d ; /MAKE_TEST_NP/ d }; /^NPMAX/ d' \
  %{buildroot}%{p_prefix}/lib/petsc/conf/petscvariables

# Make pkgconfig file visible to pkg-config
mkdir -p %{buildroot}%{p_libdir}/pkgconfig
ln -s %{p_libdir}/petsc/%{version}/%{petsc_arch}/lib/pkgconfig/petsc.pc \
      %{buildroot}%{p_libdir}/pkgconfig/
for d in /usr/lib64/petsc/%{vers}/linux-gnu-c-opt/share/petsc/matlab \
 /usr/lib64/petsc/%{vers}/linux-gnu-c-opt/lib/petsc/bin \
 /usr/lib64/petsc/%{vers}/linux-gnu-c-opt/share/petsc/bin
do
   for i in `find %{buildroot}/$d -type f  -a -perm /a=x`
   do
     head -1 $i | grep -q "^#!" || chmod -x $i
   done
   for i in `find %{buildroot}/$d -type f -a -name "*.py" -a -not -perm /a=x`
   do
     head -1 $i | grep -q "^#!" && chmod a+x $i
   done
done

%fdupes %{buildroot}%{p_include}
%fdupes %{buildroot}%{p_libdir}
%fdupes %{buildroot}%{p_prefix}/share/petsc/examples

##
%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname}
/sbin/ldconfig

%files -n %{libname}
%dir %{p_prefix}
%dir %{p_prefix}/lib
%{p_libdir}/*.so.*
%{p_prefix}/share
%exclude %{p_prefix}/share/petsc/examples
%exclude %{p_prefix}/share/petsc/saws
%dir %{p_libdir}/petsc
%dir %{p_libdir}/petsc/%{version}
%{p_prefix}/lib/*.so.*

%files %{?n_pre}devel
%exclude %{p_prefix}/lib/petsc/bin/saws
%{p_prefix}/include
%{p_prefix}/lib/petsc
%{p_prefix}/lib/pkgconfig
%{p_libdir}/*.so
%{p_libdir}/pkgconfig/*.pc
%{p_prefix}/lib/*.so
%dir %{_datadir}/modules/%{name}-%{petsc_arch}
%{_datadir}/modules/%{name}-%{petsc_arch}/%version%{?with_mpi:-%{mpi_flavor}}
%doc %{p_prefix}/share/petsc/examples

%changelog
