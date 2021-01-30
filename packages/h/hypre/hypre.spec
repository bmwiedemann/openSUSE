#
# spec file for package hypre
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


%global flavor @BUILD_FLAVOR@%{?nil}
%define ver 2.20.0
%define _ver 2_20_0
%define somver %{_ver}
%define sover %{ver}

# Base package name
%define pname hypre
%define PNAME %(echo %{pname} | tr [a-z] [A-Z])

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
%define package_name %{pname}
ExclusiveArch:  do_not_build
%endif

%if "%{flavor}" == "serial"
%undefine mpi_family
%bcond_with hpc
%endif

%if "%{flavor}" == "openmpi"
%global mpi_family  openmpi
%define mpi_vers 1
%bcond_with hpc
%{?DisOMPI1}
%endif

%if "%{flavor}" == "openmpi2"
%global mpi_family  openmpi
%define mpi_vers 2
%bcond_with hpc
%{?DisOMPI2}
%endif

%if "%{flavor}" == "openmpi3"
%global mpi_family  openmpi
%define mpi_vers 3
%bcond_with hpc
%{?DisOMPI3}
%endif

%if "%{flavor}" == "openmpi4"
%global mpi_family  openmpi
%define mpi_vers 4
%bcond_with hpc
%{?DisOMPI4}
%endif

%if "%{flavor}" == "mvapich2"
%global mpi_family  mvapich2
%bcond_with hpc
%endif

%if "%{flavor}" == "mpich"
%global mpi_family  mpich
%bcond_with hpc
%endif

%if "%{flavor}" == "doc-hpc"
%bcond_without hpc
%bcond_without install_doc
%bcond_with build_all
%else
%bcond_without build_all
%endif

%if "%{flavor}" == "gnu-mvapich2-hpc"
%undefine c_f_ver
%define mpi_family mvapich2
%define compiler_family gnu
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu-mpich-hpc"
%undefine c_f_ver
%define mpi_family mpich
%define compiler_family gnu
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu-openmpi-hpc"
%undefine c_f_ver
%define compiler_family gnu
%define mpi_family openmpi
%define mpi_vers 1
%bcond_without hpc
%{?DisOMPI1}
%endif

%if "%{flavor}" == "gnu-openmpi2-hpc"
%undefine c_f_ver
%define compiler_family gnu
%define mpi_family openmpi
%define mpi_vers 2
%bcond_without hpc
%{?DisOMPI2}
%endif

%if "%{flavor}" == "gnu-openmpi3-hpc"
%undefine c_f_ver
%define compiler_family gnu
%define mpi_family openmpi
%define mpi_vers 3
%bcond_without hpc
%{?DisOMPI3}
%endif

%if "%{flavor}" == "gnu-openmpi4-hpc"
%undefine c_f_ver
%define compiler_family gnu
%define mpi_family openmpi
%define mpi_vers 4
%bcond_without hpc
%{?DisOMPI4}
%endif

%if "%{flavor}" == "gnu7-mvapich2-hpc"
%define c_f_ver 7
%define mpi_family mvapich2
%define compiler_family gnu
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu7-mpich-hpc"
%define c_f_ver 7
%define mpi_family mpich
%define compiler_family gnu
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu7-openmpi-hpc"
%define c_f_ver 7
%define compiler_family gnu
%define mpi_family openmpi
%define mpi_vers 1
%bcond_without hpc
%{?DisOMPI1}
%endif

%if "%{flavor}" == "gnu7-openmpi2-hpc"
%define c_f_ver 7
%define compiler_family gnu
%define mpi_family openmpi
%define mpi_vers 2
%bcond_without hpc
%{?DisOMPI2}
%endif

%if "%{flavor}" == "gnu7-openmpi3-hpc"
%define c_f_ver 7
%define compiler_family gnu
%define mpi_family openmpi
%define mpi_vers 3
%bcond_without hpc
%{?DisOMPI3}
%endif

%if "%{flavor}" == "gnu7-openmpi4-hpc"
%define c_f_ver 7
%define compiler_family gnu
%define mpi_family openmpi
%define mpi_vers 4
%bcond_without hpc
%{?DisOMPI4}
%endif

%if "%{flavor}" == "gnu8-mvapich2-hpc"
%define c_f_ver 8
%define mpi_family mvapich2
%define compiler_family gnu
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu8-mpich-hpc"
%define c_f_ver 8
%define mpi_family mpich
%define compiler_family gnu
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu8-openmpi-hpc"
%define c_f_ver 8
%define compiler_family gnu
%define mpi_family openmpi
%define mpi_vers 1
%bcond_without hpc
%{?DisOMPI1}
%endif

%if "%{flavor}" == "gnu8-openmpi2-hpc"
%define c_f_ver 8
%define compiler_family gnu
%define mpi_family openmpi
%define mpi_vers 2
%bcond_without hpc
%{?DisOMPI2}
%endif

%if "%{flavor}" == "gnu8-openmpi3-hpc"
%define c_f_ver 8
%define compiler_family gnu
%define mpi_family openmpi
%define mpi_vers 3
%bcond_without hpc
%{?DisOMPI3}
%endif

%if "%{flavor}" == "gnu8-openmpi4-hpc"
%define c_f_ver 8
%define compiler_family gnu
%define mpi_family openmpi
%define mpi_vers 4
%bcond_without hpc
%{?DisOMPI4}
%endif

%if "%{flavor}" == "gnu9-mvapich2-hpc"
%define c_f_ver 9
%define mpi_family mvapich2
%define compiler_family gnu
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu9-mpich-hpc"
%define c_f_ver 9
%define mpi_family mpich
%define compiler_family gnu
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu9-openmpi-hpc"
%define c_f_ver 9
%define compiler_family gnu
%define mpi_family openmpi
%define mpi_vers 1
%bcond_without hpc
%{?DisOMPI1}
%endif

%if "%{flavor}" == "gnu9-openmpi2-hpc"
%define c_f_ver 9
%define compiler_family gnu
%define mpi_family openmpi
%define mpi_vers 2
%bcond_without hpc
%{?DisOMPI2}
%endif

%if "%{flavor}" == "gnu9-openmpi3-hpc"
%define c_f_ver 9
%define compiler_family gnu
%define mpi_family openmpi
%define mpi_vers 3
%bcond_without hpc
%{?DisOMPI3}
%endif

%if "%{flavor}" == "gnu9-openmpi4-hpc"
%define c_f_ver 9
%define compiler_family gnu
%define mpi_family openmpi
%define mpi_vers 4
%bcond_without hpc
%{?DisOMPI4}
%endif

%if "%{flavor}" == "gnu10-mvapich2-hpc"
%define c_f_ver 10
%define mpi_family mvapich2
%define compiler_family gnu
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu10-mpich-hpc"
%define c_f_ver 10
%define mpi_family mpich
%define compiler_family gnu
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu10-openmpi-hpc"
%define c_f_ver 10
%define compiler_family gnu
%define mpi_family openmpi
%define mpi_vers 1
%bcond_without hpc
%{?DisOMPI1}
%endif

%if "%{flavor}" == "gnu10-openmpi2-hpc"
%define c_f_ver 10
%define compiler_family gnu
%define mpi_family openmpi
%define mpi_vers 2
%bcond_without hpc
%{?DisOMPI2}
%endif

%if "%{flavor}" == "gnu10-openmpi3-hpc"
%define c_f_ver 10
%define compiler_family gnu
%define mpi_family openmpi
%define mpi_vers 3
%bcond_without hpc
%{?DisOMPI3}
%endif

%if "%{flavor}" == "gnu10-openmpi4-hpc"
%define c_f_ver 10
%define compiler_family gnu
%define mpi_family openmpi
%define mpi_vers 4
%bcond_without hpc
%{?DisOMPI4}
%endif

# Don't build non-HPC on SLE
%if !0%{?is_opensuse} && !0%{?with_hpc:1}
ExclusiveArch:  do_not_build
%endif

%{?mpi_family:%{bcond_without mpi}}%{!?mpi_family:%{bcond_with mpi}}

# For compatibility package names
%if "%{mpi_family}" != "openmpi" || "%{mpi_vers}" != "1" || 0%{?suse_version} > 1500
%define mpi_ext %{?mpi_vers}
%endif

%if %{without hpc}
 %if %{without mpi}
  %global my_bindir %_bindir
  %global _incdir %{_prefix}/include/
 %else
  %global _bindir %_bindir
  %global _defaultlicensedir %_defaultlicensedir
  %global _prefix %{_libdir}/mpi/gcc/%{mpi_family}%{?mpi_ext}
  %global _suffix -%{?mpi_family}%{?mpi_ext}
  %global my_bindir %{_prefix}/bin
  %global _libdir %{_prefix}/%{_lib}/
  %global _incdir %{_prefix}/include/
 %endif
 %if 0%{!?package_name:1}
  %define package_name   %pname%{?_suffix}
 %endif
 %define libname  lib%{PNAME}%{somver}%{?_suffix}
%else # with hpc
%{hpc_init %{?compiler_family:-c %compiler_family %{?c_f_ver:-v %{c_f_ver}}} %{?with_mpi:-m {%mpi_family}} %{?mpi_vers:-V %{mpi_vers}} %{?ext:-e %{ext}}}
# Nail these down before changing _prefix
 %global hpc_base %hpc_base
 %global _bindir %_bindir
 %global _defaultlicensedir %_defaultlicensedir
 %define _prefix %hpc_prefix
 %define my_bindir %hpc_bindir
 %define _libdir %hpc_libdir
 %define _incdir %hpc_includedir
 %define package_name   %{hpc_package_name %_ver}
 %define libname lib%{PNAME}%{hpc_package_name_tail %{?_ver}}
%endif

Name:           %package_name
Version:        %{ver}
Release:        0
Summary:        Scalable algorithms for solving linear systems of equations
License:        Apache-2.0 OR MIT
Group:          Productivity/Scientific/Math
URL:            https://www.llnl.gov/casc/hypre/
Source:         https://github.com/hypre-space/hypre/archive/v%{version}.tar.gz#/hypre-%{version}.tar.gz
Patch0:         hypre_Makefile_examples.patch
Patch1:         Add-library-version.patch

# TODO : add babel
#BuildRequires:  babel-devel
%if %{with build_all}
 %if %{without hpc}
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  lapack-devel
BuildRequires:  superlu-devel
  %if 0%{?with mpi}
BuildRequires:  %{mpi_family}%{?mpi_ext}-devel
  %endif
 %else
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel
BuildRequires:  %{mpi_family}%{?mpi_vers}-%{compiler_family}%{?c_f_ver}-hpc-macros-devel
BuildRequires:  libopenblas%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc-devel
BuildRequires:  superlu%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc-devel
 %endif
BuildRequires:  cmake
%endif # build_all
%if %{with hpc}
BuildRequires:  suse-hpc
%endif
BuildRequires:  fdupes
# Default library install path

%description
Hypre is a library of preconditioners that feature parallel multigrid
methods for both structured and unstructured grid problems arising in
the simulation codes being developed at LLNL to study physical
phenomena in the defense, environmental, energy, and biological
sciences.

%package     -n %{libname}
Summary:        Scalable algorithms for solving linear systems of equations
Group:          System/Libraries
%if %{with hpc}
%hpc_requires
%{requires_eq libopenblas%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc}
%{requires_eq libsuperlu%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc}
Requires:       lua-lmod >= 7.6.1
%endif

%description -n %{libname}
Hypre is a library of preconditioners that feature parallel multigrid
methods for both structured and unstructured grid problems arising in
the simulation codes being developed at LLNL to study physical
phenomena in the defense, environmental, energy, and biological
sciences.

This package contains %{?mpi_family}%{?mpi_vers}%{!?mpi_family:serial} shared libraries of Hypre.

%package devel
Summary:        Headers and library links for %{libname}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %version
%if %{without hpc}
Requires:       lapack-devel
Requires:       superlu-devel
%else
%{requires_eq libopenblas%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc-devel}
%{requires_eq superlu%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc-devel}
%hpc_requires_devel
%endif

%description devel
%{PNAME} headers and libraries files needed for development
This package contains development files of the %{?mpi_family}%{?mpi_vers}%{!?mpi_family:serial} version of Hypre.

%package        examples
Summary:        Examples for Hypre
Group:          Documentation/Other
BuildArch:      noarch

%description    examples
This package contains examples for Hypre.

%if %{with install_doc}
%package        doc
Summary:        Development documentation for Hypre
Group:          Documentation/Other
BuildArch:      noarch
BuildRequires:  texlive-bibtex
BuildRequires:  texlive-latex-bin-bin
BuildRequires:  texlive-xypic

%description    doc
This package contains development documentation for Hypre.
%endif

%if %{with build_all}
%{?with_hpc:%{hpc_master_package -L -l -N %PNAME -n lib%{PNAME}%{hpc_package_name_tail}}}
%{?with_hpc:%{hpc_master_package -L devel}}
%endif

%prep
%setup -q -n %{pname}-%{version}
%patch0 -p0
%patch1 -p0

%if %{without hpc}
cat > %{_sourcedir}/baselibs.conf  <<EOF
%{libname}
%{libname}-devel
  requires %{?_suffix}-<targettype>
  requires "%{libname}-<targettype> = <version>"
EOF
%endif

%build
%if %{with build_all}
 %if %{without hpc}
%{?with_mpi: . %{my_bindir}/mpivars.sh}
 %else
%hpc_setup

module load openblas
module load superlu
 %endif

export LDFLAGS="-lm"

cd src/
 %if %{without hpc}
%cmake \
 %else
%hpc_cmake \
 %endif
       -DHYPRE_SHARED=ON \
       %if %{without mpi}
       -DHYPRE_WITH_MPI=OFF \
       %else
       -DHYPRE_WITH_MPI=ON \
       %endif
       -DHYPRE_USING_HYPRE_BLAS=OFF \
       -DHYPRE_USING_HYPRE_LAPACK=OFF \
       -DCMAKE_SHARED_LINKER_FLAGS="-lm" \

%make_jobs
%endif # build_all

%install
%if %{with install_doc}
install -m 644 -D docs/*pdf -t %{buildroot}%{_docdir}/%{package_name}/
%fdupes -s src/examples
%endif
%if %{with build_all}
pushd .
cd src/
%cmake_install

 %if %{with hpc}
%{hpc_write_pkgconfig -n %{pname} -l %{PNAME}}

%hpc_write_modules_files
#%%Module1.0#####################################################################

proc ModulesHelp { } {

puts stderr " "
puts stderr "This module loads the hypre library built with the %{compiler_family} compiler"
puts stderr "toolchain and the %{mpi_family}%{?mpi_vers} MPI stack."
puts stderr " "
puts stderr "Note that this build of hypre leverages the superlu and MKL libraries."
puts stderr "Consequently, these packages are loaded automatically with this module."

puts stderr "\nVersion %{version}\n"

}
module-whatis "Name: %{pname} built with %{compiler_family} compiler and %{mpi_family}%{?mpi_vers} MPI"
module-whatis "Description: %{SUMMARY}"
module-whatis "Version: %{version}"
module-whatis "Category: runtime library"
module-whatis "%{url}"

set     version                     %{version}

depends-on openblas
depends-on superlu

prepend-path    PATH                %{hpc_bindir}
if {[file isdirectory  %{hpc_includedir}]} {
prepend-path    INCLUDE             %{hpc_includedir}

%hpc_modulefile_add_pkgconfig_path
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

EOF
 %endif
%fdupes -s %{buildroot}%{_prefix}
%endif # build_all

%if %{without hpc} && %{without mpi}
%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%else
%post -n %{libname}
/sbin/ldconfig -N %{_libdir}

%postun -n %{libname}
/sbin/ldconfig -N %{_libdir}
%{?with_hpc:%hpc_module_delete_if_default}
%endif

%if %{with build_all}
%files -n %{libname}
%{?hpc_dirs}
%{?hpc_modules_files}
%{_libdir}/*.so.*

%files devel
%if %{with hpc}
%{?hpc_dirs}
%{hpc_pkgconfig_file}
%endif
%{_libdir}/cmake
%license COPYRIGHT LICENSE-APACHE LICENSE-MIT NOTICE 
%doc CHANGELOG README.md INSTALL.md
%{_incdir}%{?!with_hpc:/%{pname}}
%{_libdir}/*.so
%endif # build_all

%if %{with install_doc}
%files doc
%{_docdir}/%{package_name}

%files examples
%doc src/examples
%endif

%changelog
