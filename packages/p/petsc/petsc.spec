#
# spec file
#
# Copyright (c) 2024 SUSE LLC
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

%define pname petsc
%define vers 3.21.2
%define _vers 3_21_2
%define so_ver 3_21
%define openblas_vers 0.3.6

ExcludeArch:    s390 s390x

# Fails to link during configure, as it omits SuperLU from the link libraries
%bcond_with hypre
# Only available as openmpi flavor, and not in Factory
%bcond_with pastix

%define python_ver 3

%if 0%{?sle_version} >= 150200
%define DisOMPI1 ExclusiveArch:  do_not_build
%endif
%if !0%{?is_opensuse} && 0%{?sle_version:1} && 0%{?sle_version} < 150200
%define DisOMPI3 ExclusiveArch:  do_not_build
%endif
%if 0%{?sle_version:1} && 0%{?sle_version} < 150300
%define DisOMPI4 ExclusiveArch:  do_not_build
%endif

%if "%flavor" == ""
ExclusiveArch:  do_not_build
%endif

%if "%flavor" == "serial"
%{bcond_with hpc}
%endif

%if "%flavor" == "openmpi4"
%{?DisOMPI4}
%define mpi_family openmpi
%define mpi_vers 4
%{bcond_with hpc}
%endif

%if "%flavor" == "openmpi5"
%{?DisOMPI5}
%define mpi_family openmpi
%define mpi_vers 5
%{bcond_with hpc}
%endif

%if "%flavor" == "gnu-openmpi4-hpc"
%{?DisOMPI4}
%define mpi_family openmpi
%define compiler_family gnu
%undefine c_f_ver
%define mpi_vers 4
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu-openmpi5-hpc"
%{?DisOMPI5}
%define mpi_family openmpi
%define compiler_family gnu
%undefine c_f_ver
%define mpi_vers 5
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu-mvapich2-hpc"
%define mpi_family mvapich2
%define compiler_family gnu
%undefine c_f_ver
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu-mpich-hpc"
%define mpi_family mpich
%define compiler_family gnu
%undefine c_f_ver
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu7-openmpi4-hpc"
%{?DisOMPI4}
%define mpi_family openmpi
%define compiler_family gnu
%define c_f_ver 7
%define mpi_vers 4
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu7-openmpi5-hpc"
%{?DisOMPI5}
%define mpi_family openmpi
%define compiler_family gnu
%define c_f_ver 7
%define mpi_vers 5
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu7-mvapich2-hpc"
%define mpi_family mvapich2
%define compiler_family gnu
%define c_f_ver 7
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu7-mpich-hpc"
%define mpi_family mpich
%define compiler_family gnu
%define c_f_ver 7
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu8-openmpi4-hpc"
%{?DisOMPI4}
%define mpi_family openmpi
%define compiler_family gnu
%define c_f_ver 8
%define mpi_vers 4
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu8-openmpi5-hpc"
%{?DisOMPI5}
%define mpi_family openmpi
%define compiler_family gnu
%define c_f_ver 8
%define mpi_vers 5
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu8-mvapich2-hpc"
%define mpi_family mvapich2
%define compiler_family gnu
%define c_f_ver 8
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu9-openmpi4-hpc"
%{?DisOMPI4}
%define mpi_family openmpi
%define compiler_family gnu
%define c_f_ver 9
%define mpi_vers 4
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu9-openmpi5-hpc"
%{?DisOMPI5}
%define mpi_family openmpi
%define compiler_family gnu
%define c_f_ver 9
%define mpi_vers 5
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu9-mvapich2-hpc"
%define mpi_family mvapich2
%define compiler_family gnu
%define c_f_ver 9
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu9-mpich-hpc"
%define mpi_family mpich
%define compiler_family gnu
%define c_f_ver 9
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu10-openmpi4-hpc"
%{?DisOMPI4}
%define mpi_family openmpi
%define compiler_family gnu
%define c_f_ver 10
%define mpi_vers 4
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu10-openmpi5-hpc"
%{?DisOMPI5}
%define mpi_family openmpi
%define compiler_family gnu
%define c_f_ver 10
%define mpi_vers 5
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu10-mvapich2-hpc"
%define mpi_family mvapich2
%define compiler_family gnu
%define c_f_ver 10
%{bcond_without hpc}
%endif

%if "%flavor" == "gnu10-mpich-hpc"
%define mpi_family mpich
%define compiler_family gnu
%define c_f_ver 10
%{bcond_without hpc}
%endif

%if !0%{?is_opensuse} && !0%{?with_hpc:1}
ExclusiveArch:  do_not_build
%endif

%if %{without hpc}
%define package_name() %{pname}%{?with_mpi:-%{mpi_family}%{?mpi_vers}}
%define libname() lib%{pname}%{so_ver}%{?with_mpi:-%{mpi_family}%{?mpi_vers}}
%else
ExcludeArch:    %ix86
%{hpc_init -c %compiler_family -m %mpi_family %{?c_f_ver:-v %{c_f_ver}} %{?mpi_vers:-V %{mpi_vers}} %{?ext:-e %{ext}}}

%define package_name() %{hpc_package_name %_vers}
%define libname() lib%{pname}%{expand:%%{hpc_package_name_tail %{**}}}
%global libname_plain %{libname}
%endif

%if 0%{?mpi_family:1}
%{bcond_without mpi}
%else
%{bcond_with mpi}
%endif

%if %{without hpc}
 %if %{without mpi}
%define p_base %{_prefix}/
 %else
 %{?with_mpi:%{!?mpi_family:error "No MPI family specified!"}}

%define p_base %{_libdir}/mpi/gcc/%{mpi_family}%{?mpi_vers}/
 %endif
%define p_prefix %{p_libdir}/petsc/%{version}/%petsc_arch
%else
%define p_base %{hpc_prefix}/
%define p_prefix %{hpc_prefix}
%endif

%define p_libdir %{p_base}%_lib
%define p_include %{p_prefix}/include

%define petsc_arch linux-gnu-c-opt

Name:           %{package_name}
Summary:        Portable Extensible Toolkit for Scientific Computation
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
Version:        %vers
Release:        0

Source:         https://web.cels.anl.gov/projects/petsc/download/release-snapshots/petsc-%{version}.tar.gz
Patch0:         Remove-rpath-test.patch
Patch1:         petsc-3.7-fix-pastix-detection.patch
Patch2:         Allow-lib64-as-library-directory-for-scalapack.patch
URL:            https://www.mcs.anl.gov/petsc/
BuildRequires:  fdupes
BuildRequires:  hwloc-devel
BuildRequires:  libyaml-devel
BuildRequires:  pkg-config
BuildRequires:  python3-base

%if %{without hpc}
BuildRequires:  Modules
BuildRequires:  blas-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  lapack-devel
BuildRequires:  suitesparse-devel

 %if %{with mpi}
BuildRequires:  %{mpi_family}%{?mpi_vers}-devel
BuildRequires:  blacs-%{mpi_family}%{?mpi_vers}-devel
BuildRequires:  hdf5-%{mpi_family}%{?mpi_vers}-devel
%if %{with hypre}
BuildRequires:  hypre-%{mpi_family}%{?mpi_vers}-devel
BuildRequires:  superlu-devel
%endif
BuildRequires:  ptscotch-%{mpi_family}%{?mpi_vers}-devel
BuildRequires:  ptscotch-parmetis-%{mpi_family}%{?mpi_vers}-devel
#!BuildIgnore:  metis-devel
%if %{with pastix}
BuildRequires:  pastix-%{mpi_family}%{?mpi_vers}-devel
%endif
BuildRequires:  scalapack-%{mpi_family}%{?mpi_vers}-devel
 %else
BuildRequires:  metis-devel
 %endif
%else
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel
BuildRequires:  %{mpi_family}%{?mpi_vers}-%{compiler_family}%{?c_f_ver}-hpc-macros-devel
BuildRequires:  hdf5%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-%{mpi_family}%{?mpi_vers}-hpc-devel
BuildRequires:  libopenblas%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc-devel
BuildRequires:  libopenblas-%{compiler_family}-hpc >=  %{openblas_vers}
BuildRequires:  libscalapack2%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-%{mpi_family}%{?mpi_vers}-hpc-devel
BuildRequires:  lua-lmod
BuildRequires:  suse-hpc
%endif

BuildRequires:  valgrind-devel
BuildRequires:  xz
BuildRequires:  zlib-devel

%description
PETSc is a suite of data structures and routines for the scalable
(parallel) solution of scientific applications modeled by partial
differential equations.

%package -n %{libname %_vers}
Summary:        PETSc shared libraries
Group:          System/Libraries
%if %{with hpc}
%{hpc_requires}
%{requires_eq libhdf5%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-%{mpi_family}%{?mpi_vers}-hpc}
%{requires_eq libscalapack2%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-%{mpi_family}%{?mpi_vers}-hpc}
%else
# Fixup wrong package name
Conflicts:      libpetsc3%{?with_mpi:-%{mpi_family}%{?mpi_vers}}
%endif

%description -n %{libname %_vers}
PETSc is a suite of data structures and routines for the scalable
(parallel) solution of scientific applications modeled by partial
differential equations.

%{?with_hpc:%{hpc_master_package -n %{libname_plain} -l -L}}

%package %{?n_pre}devel
Summary:        Devel files for petsc
Group:          Development/Libraries/C and C++
Requires:       %{libname %_vers} = %{version}
%if %{without hpc}
Requires:       Modules
Requires:       suitesparse-devel
 %if %{without mpi}
Requires:       metis-devel
 %else
Requires:       blacs-%{mpi_family}%{?mpi_vers}-devel
Requires:       hdf5-%{mpi_family}%{?mpi_vers}-devel
Requires:       hypre-%{mpi_family}%{?mpi_vers}-devel
Requires:       ptscotch-%{mpi_family}%{?mpi_vers}-devel
Requires:       ptscotch-parmetis-%{mpi_family}%{?mpi_vers}-devel
Requires:       scalapack-%{mpi_family}%{?mpi_vers}-devel
 %endif
%else
# with hpc:
%{requires_eq hdf5%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-%{mpi_family}%{?mpi_vers}-hpc-devel}
%{requires_eq libopenblas%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc-devel}
%{requires_eq libscalapack2%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-%{mpi_family}%{?mpi_vers}-hpc-devel}
%hpc_requires_devel
%endif

%description %{?n_pre}devel
PETSc is a suite of data structures and routines for the scalable
(parallel) solution of scientific applications modeled by partial
differential equations.

%{?with_hpc:%{hpc_master_package -a devel}}

%package doc
Summary:        Documentation for petsc
Group:          Documentation/HTML

%description doc
This package contains the documentation for petsc.

%if %{with hpc}
%package saws
Summary:        PETsc SAWs infrastructure
#Requires:      saws
#Requires:      jshon
Group:          Productivity/Scientific/Other
Requires:       %{libname %_vers} = %{version}

%description saws
This package contains the files to interface with SAWs
(Scientific Application Web server). SAWs itself is not
yet supported by %{?is_opensuse:open}SUSE.
%endif

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

%if 0 && %{without hpc}
cat > %{_sourcedir}/baselibs.conf  <<EOF
%{libname %_vers}
%{name}-devel
  requires -blas-<targettype>
  requires -lapack-<targettype>
  requires " %{libname %_vers}-<targettype> = <version>"
EOF
%endif

%build

%if %{without hpc}
export PETSC_DIR=${RPM_BUILD_DIR}/petsc-%{version}
export PETSC_ARCH=%petsc_arch
%{?with_mpi:export LD_LIBRARY_PATH=%{p_libdir}}
%else
%hpc_setup
module load phdf5 scalapack openblas
%endif
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
%if %{without hpc}
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
%else
  --with-blas-lapack-lib=$OPENBLAS_LIB/libopenblas.so \
  --with-scalapack=1 \
  --with-scalapack-dir=$SCALAPACK_DIR \
  --with-hdf5=1 \
  --with-hdf5-lib=$HDF5_LIB/libhdf5.so \
  --with-hdf5-include=$HDF5_INC
%endif

%make_build

%install
%if %{without hpc}
export PETSC_DIR=${RPM_BUILD_DIR}/petsc-%{version}
export PETSC_ARCH=%petsc_arch
%endif

make install DESTDIR=%{buildroot}

find %{buildroot}%{p_prefix}/share/petsc/examples/src -type f -ipath '*/output/*out' -delete
rm -f %{buildroot}%{p_prefix}/lib/petsc/conf/*.log
rm -f %{buildroot}%{p_prefix}/lib/petsc/conf/.DIR

%if %{without hpc}

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
cat << EOF > %{buildroot}/usr/share/modules/%{name}-%{petsc_arch}/%version%{?with_mpi:-%{mpi_family}%{?mpi_vers}}
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
%else
# with hpc:

if [ ! -d %{buildroot}%{p_libdir} -a -d %{buildroot}%{p_base}/lib ]
then
    mkdir -p %{buildroot}%{p_libdir}
    mv  %{buildroot}%{p_base}/lib/lib*.so %{buildroot}%{p_base}/lib/lib*.so.* %{buildroot}%{p_libdir}
    mv  %{buildroot}%{p_base}/lib/pkgconfig  %{buildroot}%{p_libdir}
fi

for i in update.py \
    bin/FASTMathInstaller.py \
    bin/TOPSGenerator.py \
    bin/petscnagupgrade.py \
    bin/configVars.py bin/update.py \
    lib/petsc/conf/reconfigure-arch-linux2-cxx-opt.py \
    lib/petsc/conf/uninstall.py
do
    rm -f %{buildroot}%{p_prefix}/$i
done

for file in %{hpc_prefix}/lib/petsc/bin/petsc_conf.py \
    %{hpc_prefix}/lib/petsc/bin/PetscBinaryIO.py \
    %{hpc_prefix}/lib/petsc/bin/PetscBinaryIOTrajectory.py
do
    %{hpc_python_mv_to_sitearch $file}
done

%{hpc_shebang_prepend_list %{buildroot}%{p_prefix}/lib/petsc/bin/*.py}
%hpc_shebang_sanitize_scripts %{buildroot}%{p_prefix}/lib/petsc/bin
%hpc_shebang_sanitize_scripts %{buildroot}%{p_prefix}/lib/petsc

tmp=$(mktemp /tmp/bad-XXXXXX})
for file in $(find %{buildroot}%{p_prefix} -name "*.py"); do
    %{hpc_verify_python3 $file} || echo "$file" >> $tmp
done
[ -s $tmp ] && { echo "One or more python script not Python 3 compliant!"; cat $tmp; exit 1; }
rm -f $tmp

python_sitearch_path=%{hpc_python_sitearch_no_singlespec}
%hpc_write_modules_files
#%%Module1.0#####################################################################

proc ModulesHelp { } {

puts stderr " "
puts stderr "This module loads the PETSc library built with the %{compiler_family} compiler"
puts stderr "toolchain and the %{mpi_family}%{?mpi_vers} MPI stack."
puts stderr " "

puts stderr "\nVersion %{version}\n"

}
module-whatis "Name: %{pname} built with %{compiler_family} compiler and %{mpi_family}%{?mpi_vers} MPI"
module-whatis "Version: %{version}"
module-whatis "Category: runtime library"
module-whatis "Description: %{SUMMARY:0}"
module-whatis "%{url}"

set     version                     %{version}

# Require phdf5 (and scalapack for gnu compiler families)

if [ expr [ module-info mode load ] || [module-info mode display ] ] {
    if {  ![is-loaded phdf5]  } {
        module load phdf5
    }
    if { ![is-loaded openblas]  } {
        module load openblas
    }
    if { ![is-loaded scalapack]  } {
        module load scalapack
    }
}

prepend-path    PATH                %{hpc_prefix}/lib/petsc/bin
prepend-path    LD_LIBRARY_PATH     %{hpc_libdir}
if {[file isdirectory  $python_sitearch_path]} {
prepend-path    PYTHONPATH          $python_sitearch_path
}

setenv          %{hpc_upcase %pname}_DIR        %{hpc_prefix}
if {[file isdirectory  %{hpc_prefix}/lib/petsc/bin]} {
setenv          %{hpc_upcase %pname}_BIN        %{hpc_prefix}/lib/petsc/bin
}
if {[file isdirectory  %{hpc_includedir}]} {
prepend-path    LIBRARY_PATH        %{hpc_libdir}
prepend-path    CPATH               %{hpc_includedir}
prepend-path    C_INCLUDE_PATH      %{hpc_includedir}
prepend-path    CPLUS_INCLUDE_PATH  %{hpc_includedir}
prepend-path    INCLUDE                         %{hpc_includedir}
%hpc_modulefile_add_pkgconfig_path

setenv          %{hpc_upcase %pname}_INC        %{hpc_includedir}
setenv          %{hpc_upcase %pname}_LIB        %{hpc_libdir}
}
EOF
%endif
# with/out hpc

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

%if %{without hpc}
# Make pkgconfig file visible to pkg-config
mkdir -p %{buildroot}%{p_libdir}/pkgconfig
ln -s %{p_libdir}/petsc/%{version}/%{petsc_arch}/lib/pkgconfig/petsc.pc \
      %{buildroot}%{p_libdir}/pkgconfig/
%endif
for d in /usr/lib64/petsc/3.21.2/linux-gnu-c-opt/share/petsc/matlab \
 /usr/lib64/petsc/3.21.2/linux-gnu-c-opt/lib/petsc/bin \
 /usr/lib64/petsc/3.21.2/linux-gnu-c-opt/share/petsc/bin
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
%post -n %{libname %_vers} -p /sbin/ldconfig

%postun -n %{libname %_vers}
/sbin/ldconfig
%{?with_hpc:%{hpc_module_delete_if_default}}

%files -n %{libname %_vers}
%dir %{p_prefix}
%dir %{p_prefix}/lib
%{p_libdir}/*.so.*
%{p_prefix}/share
%exclude %{p_prefix}/share/petsc/examples
%exclude %{p_prefix}/share/petsc/saws
%if %{without hpc}
%dir %{p_libdir}/petsc
%dir %{p_libdir}/petsc/%{version}
%{p_prefix}/lib/*.so.*
%else
%hpc_dirs
%hpc_modules_files
%{dirname:%{hpc_python_sitearch_no_singlespec}}
%endif

%files %{?n_pre}devel
%exclude %{p_prefix}/lib/petsc/bin/saws
%{p_prefix}/include
%{p_prefix}/lib/petsc
%{p_prefix}/%{!?with_hpc:lib}%{?with_hpc:%_lib}/pkgconfig
%{p_libdir}/*.so
%{p_libdir}/pkgconfig/*.pc
  %if %{without hpc}
%{p_prefix}/lib/*.so
%dir %{_datadir}/modules/%{name}-%{petsc_arch}
%{_datadir}/modules/%{name}-%{petsc_arch}/%version%{?with_mpi:-%{mpi_family}%{?mpi_vers}}
  %endif
%doc %{p_prefix}/share/petsc/examples

%if %{with hpc}
%files saws
%{p_prefix}/lib/petsc/bin/saws
%{p_prefix}/share/petsc/saws
%endif

%changelog
