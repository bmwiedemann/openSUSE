#
# spec file for package hypre
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


%global flavor @BUILD_FLAVOR@%{?nil}
%define ver 2.18.2
%define _ver 2_18_2
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
  %define my_prefix %_prefix
  %define my_bindir %_bindir
  %define my_libdir %_libdir
  %define my_incdir %_includedir
 %else
  %global my_suffix -%{?mpi_family}%{?mpi_ext}
  %global my_prefix %{_libdir}/mpi/gcc/%{mpi_family}%{?mpi_ext}
  %global my_bindir %{my_prefix}/bin
  %global my_libdir %{my_prefix}/%{_lib}/
  %global my_incdir %{my_prefix}/include/
  %global my_datadir %{my_prefix}/share/
 %endif
 %if 0%{!?package_name:1}
  %define package_name   %pname%{?my_suffix}
 %endif
 %define libname  lib%{PNAME}%{somver}%{?my_suffix}
%else # with hpc
%{hpc_init %{?compiler_family:-c %compiler_family %{?c_f_ver:-v %{c_f_ver}}} %{?with_mpi:-m {%mpi_family}} %{?mpi_vers:-V %{mpi_vers}} %{?ext:-e %{ext}}}
 %define my_prefix %hpc_prefix
 %define my_bindir %hpc_bindir
 %define my_libdir %hpc_libdir
 %define my_incdir %hpc_includedir
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
Patch1:         Fix-library-version-numbering.patch
Patch2:         Fix-empty-elseif-in-CMakeLists.txt.patch

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
Requires:       libopenblas%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc
Requires:       libsuperlu%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc
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
Requires:       lapack-devel
Requires:       superlu-devel
%if %{with hpc}
Requires:       libopenblas%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc-devel
Requires:       superlu%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc-devel
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
%patch1 -p2
%patch2 -p2
%if %{without hpc}
cat > %{_sourcedir}/baselibs.conf  <<EOF
%{libname}
%{libname}-devel
  requires %{?my_suffix}-<targettype>
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

# move libaries arround for mpi builds
 %if %{without hpc}
  %if %{with mpi}
mkdir -pv %{buildroot}%{my_libdir}
mv -v %{buildroot}/usr/%{_lib}/*.so* %{buildroot}%{my_libdir}
mv -v %{buildroot}/usr/include %{buildroot}%{my_incdir}
  %endif
 %endif

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
%fdupes -s %{buildroot}%{my_prefix}
%endif # build_all

%if %{without hpc} && %{without mpi}
%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%else
%post -n %{libname}
/sbin/ldconfig -N %{my_libdir}

%postun -n %{libname}
/sbin/ldconfig -N %{my_libdir}
%{?with_hpc:%hpc_module_delete_if_default}
%endif

%if %{with build_all}
%files -n %{libname}
%{?hpc_dirs}
%{?hpc_modules_files}
%{my_libdir}/*.so.*

%files devel
%if %{with hpc}
%{?hpc_dirs}
%{hpc_pkgconfig_file} 
%endif
%license COPYRIGHT LICENSE-APACHE LICENSE-MIT NOTICE 
%doc CHANGELOG README.md INSTALL.md
%{my_incdir}%{?!with_hpc:/%{pname}}
%{my_libdir}/*.so
%endif # build_all

%if %{with install_doc}
%files doc
%{_docdir}/%{package_name}

%files examples
%doc src/examples
%endif

%changelog
