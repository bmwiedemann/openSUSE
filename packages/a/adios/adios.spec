#
# spec file for package adios
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


%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects

%global flavor @BUILD_FLAVOR@%{nil}

%define pname adios
%define vers 1.13.1
%define _vers %(echo %{vers} | tr . _)

%if "%{flavor}" == ""
ExclusiveArch:  do_not_build
%endif

# No netcdf on s390.
ExcludeArch:    s390 s390x

%if 0%{?sle_version} >= 150200
%define DisOMPI1 ExclusiveArch:  do_not_build
%endif
%if !0%{?is_opensuse} && 0%{?sle_version:1} && 0%{?sle_version} < 150200
%define DisOMPI3 ExclusiveArch:  do_not_build
%endif
%if 0%{?sle_version:1} && 0%{?sle_version} < 150300
%define DisOMPI4 ExclusiveArch:  do_not_build
%endif

# this is a non-HPC build
%if "%{flavor}" == "openmpi"
%{?DisOMPI1}
%global mpi_flavor openmpi
%define mpi_ver 1
%bcond_with hpc
%endif

%if "%{flavor}" == "openmpi2"
%global mpi_flavor openmpi
%define mpi_ver 2
%bcond_with hpc
%endif

%if "%{flavor}" == "openmpi3"
%{?DisOMPI3}
%global mpi_flavor openmpi
%define mpi_ver 3
%bcond_with hpc
%endif

%if "%{flavor}" == "openmpi4"
%{?DisOMPI4}
%global mpi_flavor openmpi
%define mpi_ver 4
%bcond_with hpc
%endif

# All the HPC builds are below
%if "%{flavor}" == "gnu-openmpi-hpc"
%{?DisOMPI1}
%bcond_without hpc
%define compiler_family gnu
%undefine c_f_ver
%global mpi_flavor openmpi
%define mpi_ver 1
%endif

%if "%{flavor}" == "gnu-openmpi2-hpc"
%bcond_without hpc
%define compiler_family gnu
%undefine c_f_ver
%global mpi_flavor openmpi
%define mpi_ver 2
%endif

%if "%{flavor}" == "gnu-openmpi3-hpc"
%{?DisOMPI3}
%bcond_without hpc
%define compiler_family gnu
%undefine c_f_ver
%global mpi_flavor openmpi
%define mpi_ver 3
%endif

%if "%{flavor}" == "gnu-openmpi4-hpc"
%{?DisOMPI4}
%bcond_without hpc
%define compiler_family gnu
%undefine c_f_ver
%global mpi_flavor openmpi
%define mpi_ver 4
%endif

%if "%{flavor}" == "gnu-mvapich2-hpc"
%bcond_without hpc
%define compiler_family gnu
%undefine c_f_ver
%global mpi_flavor mvapich2
%endif

%if "%{flavor}" == "gnu-mpich-hpc"
%bcond_without hpc
%define compiler_family gnu
%undefine c_f_ver
%global mpi_flavor mpich
%endif

# All the HPC builds are below
%if "%{flavor}" == "gnu7-openmpi-hpc"
%{?DisOMPI1}
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 7
%global mpi_flavor openmpi
%define mpi_ver 1
%endif

%if "%{flavor}" == "gnu7-openmpi2-hpc"
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 7
%global mpi_flavor openmpi
%define mpi_ver 2
%endif

%if "%{flavor}" == "gnu7-openmpi3-hpc"
%{?DisOMPI3}
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 7
%global mpi_flavor openmpi
%define mpi_ver 3
%endif

%if "%{flavor}" == "gnu7-openmpi4-hpc"
%{?DisOMPI4}
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 7
%global mpi_flavor openmpi
%define mpi_ver 4
%endif

%if "%{flavor}" == "gnu7-mvapich2-hpc"
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 7
%global mpi_flavor mvapich2
%endif

%if "%{flavor}" == "gnu7-mpich-hpc"
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 7
%global mpi_flavor mpich
%endif

%if "%{flavor}" == "gnu8-openmpi-hpc"
%{?DisOMPI1}
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 8
%global mpi_flavor openmpi
%define mpi_ver 1
%endif

%if "%{flavor}" == "gnu8-openmpi2-hpc"
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 8
%global mpi_flavor openmpi
%define mpi_ver 2
%endif

%if "%{flavor}" == "gnu8-openmpi3-hpc"
%{?DisOMPI3}
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 8
%global mpi_flavor openmpi
%define mpi_ver 3
%endif

%if "%{flavor}" == "gnu8-openmpi4-hpc"
%{?DisOMPI4}
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 8
%global mpi_flavor openmpi
%define mpi_ver 4
%endif

%if "%{flavor}" == "gnu8-mvapich2-hpc"
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 8
%global mpi_flavor mvapich2
%endif

%if "%{flavor}" == "gnu8-mpich-hpc"
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 8
%global mpi_flavor mpich
%endif

%if "%{flavor}" == "gnu9-openmpi-hpc"
%{?DisOMPI1}
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 9
%global mpi_flavor openmpi
%define mpi_ver 1
%endif

%if "%{flavor}" == "gnu9-openmpi2-hpc"
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 9
%global mpi_flavor openmpi
%define mpi_ver 2
%endif

%if "%{flavor}" == "gnu9-openmpi3-hpc"
%{?DisOMPI3}
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 9
%global mpi_flavor openmpi
%define mpi_ver 3
%endif

%if "%{flavor}" == "gnu9-openmpi4-hpc"
%{?DisOMPI4}
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 9
%global mpi_flavor openmpi
%define mpi_ver 4
%endif

%if "%{flavor}" == "gnu9-mvapich2-hpc"
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 9
%global mpi_flavor mvapich2
%endif

%if "%{flavor}" == "gnu9-mpich-hpc"
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 9
%global mpi_flavor mpich
%endif
#
%if "%{flavor}" == "gnu10-openmpi-hpc"
%{?DisOMPI1}
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 10
%global mpi_flavor openmpi
%define mpi_ver 1
%endif

%if "%{flavor}" == "gnu10-openmpi2-hpc"
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 10
%global mpi_flavor openmpi
%define mpi_ver 2
%endif

%if "%{flavor}" == "gnu10-openmpi3-hpc"
%{?DisOMPI3}
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 10
%global mpi_flavor openmpi
%define mpi_ver 3
%endif

%if "%{flavor}" == "gnu10-openmpi4-hpc"
%{?DisOMPI4}
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 10
%global mpi_flavor openmpi
%define mpi_ver 4
%endif

%if "%{flavor}" == "gnu10-mvapich2-hpc"
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 10
%global mpi_flavor mvapich2
%endif

%if "%{flavor}" == "gnu10-mpich-hpc"
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 10
%global mpi_flavor mpich
%endif

%if !0%{?is_opensuse} && !0%{?with_hpc:1}
ExclusiveArch:  do_not_build
%endif

%{?mpi_flavor:%{bcond_without mpi}}%{!?mpi_flavor:%{bcond_with mpi}}
%{?with_mpi:%{!?mpi_flavor:%global mpi_flavor openmpi}}

# openmpi 1 was called just "openmpi" in Leap 15.x/SLE15
%if 0%{?suse_version} >= 1550 || "%{mpi_flavor}" != "openmpi"  || "%{mpi_ver}" != "1"
%define mpi_ext %{?mpi_ver}
%endif

%if %{with hpc}
 %{hpc_init %{?compiler_family:-c %{compiler_family} %{?c_f_ver:-v %{c_f_ver}}} %{?with_mpi:-m %{?mpi_flavor}} %{?mpi_ver:-V %{?mpi_ver}} %{?ext:-e %{ext}}}
 %{hpc_modules_init phdf5 netcdf}
 %global hpc_module_pname %{pname}
 %define pkg_prefix %{hpc_prefix}
 %define pkg_bindir %{hpc_bindir}
 %define pkg_libdir %{hpc_libdir}
 %define pkg_incdir %{hpc_includedir}
 %define pkg_datadir %{hpc_datadir}
 %define pkg_sysconfdir %{hpc_prefix}/etc/
 %define pkg_skeldir %{hpc_prefix}/etc/skel/
 %define package_name   %{hpc_package_name %{_vers}}
 %define libname(l:s:)   lib%{pname}%{-l*}%{hpc_package_name_tail %{?_vers}}
%else
 %global pkg_suffix %{?mpi_flavor:-%{mpi_flavor}%{?mpi_ext}}
 %define pkg_prefix %{_libdir}/mpi/gcc/%{mpi_flavor}%{?mpi_ext}
 %define pkg_bindir %{pkg_prefix}/bin/
 %define pkg_libdir %{pkg_prefix}/%{_lib}/
 %define pkg_incdir %{pkg_prefix}/include/
 %define pkg_datadir %{pkg_prefix}/share/
 %define pkg_sysconfdir %{pkg_prefix}/etc/
 %define pkg_skeldir %{pkg_prefix}/etc/skel/
 %define package_name   %{pname}%{?pkg_suffix}
 %define libname(l:s:)   lib%{pname}%{!-l:%{-s:-}}%{-l*}%{-s*}%{?pkg_suffix}
%endif

%if 0%{?suse_version} >= 1500
%define my_py_version 3
%endif

Name:           %{package_name}
Version:        %{vers}
Release:        0
Summary:        The Adaptable IO System (ADIOS)
License:        BSD-3-Clause AND LGPL-2.1-or-later AND BSD-2-Clause
Group:          Productivity/Scientific/Other
URL:            https://www.olcf.ornl.gov/center-projects/adios/
Source0:        https://users.nccs.gov/~pnorbert/adios-%{version}.tar.gz
Patch0:         adios-correct-func-ret.patch
Patch1:         Fix-code-to-be-python3-compliant.patch
%{?with_hpc:BuildRequires:  suse-hpc >= 0.3}
BuildRequires:  autoconf
BuildRequires:  fdupes
BuildRequires:  libbz2-devel
BuildRequires:  liblz4-devel
BuildRequires:  python%{?my_py_version}
BuildRequires:  zlib-devel
%if %{without hpc}
BuildRequires:  %{mpi_flavor}%{?mpi_ext}-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  hdf5%{?pkg_suffix}-devel
BuildRequires:  netcdf%{?pkg_suffix}-devel
%else # hpc
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel
BuildRequires:  %{mpi_flavor}%{?mpi_ver}-%{compiler_family}%{?c_f_ver}-hpc-macros-devel
BuildRequires:  hdf5-%{compiler_family}%{?c_f_ver}%{?with_mpi:-%{mpi_flavor}%{?mpi_ver}}-hpc-devel
BuildRequires:  lua-lmod
BuildRequires:  netcdf-%{compiler_family}%{?c_f_ver}%{?with_mpi:-%{mpi_flavor}%{?mpi_ver}}-hpc-devel
%{hpc_requires}
%endif  # ?hpc
Requires:       python%{?my_py_version}-PyYAML
Requires:       python%{?my_py_version}-xml

%description
The Adaptable IO System (ADIOS) provides a way for scientists to
describe the data in their code that may need to be written, read, or
processed outside of the running simulation. By providing an external
to the code XML file describing the various elements, their types,
and how one wishes to process them for a particular run, the routines
in the host code (either FORTRAN or C) can transparently change how
they process the data.

%{?with_hpc:%hpc_master_package -L}

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Parallel
Requires:       %{name} = %{version}
Requires:       %{name}-devel-static = %{version}
%if %{without hpc}
Requires:       hdf5%{?pkg_suffix}-devel
Requires:       netcdf%{?pkg_suffix}-devel
%if "%{mpi_family}%{?mpi_ext}" == "openmpi1"
Provides:       %{pname}%-openmpi-devel
%endif
%else # hpc
%{requires_eq hdf5-%{compiler_family}%{?c_f_ver}%{?with_mpi:-%{mpi_flavor}%{?mpi_ver}}-hpc-devel}
Requires:       lua-lmod
%{requires_eq netcdf-%{compiler_family}%{?c_f_ver}%{?with_mpi:-%{mpi_flavor}%{?mpi_ver}}-hpc-devel}
%hpc_requires_devel
%endif  # ?hpc

%description devel
The Adaptable IO System (ADIOS) provides a way for scientists to
describe the data in their code that may need to be written, read, or
processed outside of the running simulation.

This package contains all files needed to create projects that use
the %{flavor} version of ADIOS.

%{?with_hpc:%{hpc_master_package -L devel}}

%package devel-static
Summary:        Static libraries for %{name}
Group:          Development/Libraries/Parallel

%description devel-static
The Adaptable IO System (ADIOS) provides a way for scientists to
describe the data in their code that may need to be written, read, or
processed outside of the running simulation.

This package contains all the static libraries needed to create projects
that use the %{flavor} version of ADIOS.

%{?with_hpc:%{hpc_master_package -L devel-static}}

%prep
%setup -q -n %{pname}-%{version}
%patch0 -p1
%patch1 -p1

%build
%{?with_hpc:%hpc_setup}

export CC=gcc
export CXX=g++
export F77=gfortran
export F9X=gfortran
export FC=gfortran
export MPICC=mpicc
export MPICXX=mpicxx
export MPIFC=mpif90
export CFLAGS="-fPIC %{optflags}"
%if 0%{?suse_version} >= 1550 || 0%{?c_f_ver} >= 10
# https://github.com/ornladios/ADIOS/issues/206
export FCFLAGS="-fPIC %{optflags} -fallow-argument-mismatch"
%else
export FCFLAGS="-fPIC %{optflags}"
%endif
export LDFLAGS="-pie"

%if %{without hpc}
export MPICC="%{pkg_bindir}/mpicc"
export MPIFC="%{pkg_bindir}/mpif90"
export PATH=${PATH}:%{pkg_bindir}
export LDFLAGS="${LDFLAGS} -L%{pkg_libdir}"
export LD_LIBRARY_PATH="%{pkg_libdir}"
%configure \
  --prefix=%{pkg_prefix} \
  --exec-prefix=%{_prefix} \
  --bindir=%{pkg_bindir} \
  --libdir=%{pkg_libdir} \
  --includedir=%{pkg_incdir} \
  --sysconfdir=%{pkg_sysconfdir} \
  --datadir=%{pkg_datadir} \
  --docdir=%{_docdir}/%{name} \
%else
%{hpc_setup}

%global _hpc_exec_prefix %{hpc_exec_prefix}
%global hpc_exec_prefix %{_prefix}
%{hpc_configure} \
  --sysconfdir=%{pkg_sysconfdir} \
%define hpc_exec_prefix %{expand:%_hpc_exec_prefix}
%endif
  --enable-fortran \
  --with-phdf5="%{pkg_prefix}" \
  --with-netcdf="%{pkg_prefix}" \
  --with-zlib="%{_prefix}" \
  --with-bzip2="%{_libdir}" \
  --with-lz4="%{_libdir}" \
  --without-evpath \
  --without-fastbit \
  --without-ffs \

make V=1 %{?_smp_mflags}

%install
%if %{with hpc}
%{hpc_setup}
%endif
%make_install
for i in %{buildroot}/%{pkg_bindir}/{skel,*.py} %{buildroot}/%{pkg_libdir}/python/*.py; do
    sed -e '1s@^\(#!.*\)\(python\)[23]*\( *.*\)@\1\2%{?my_py_version}\3@' -e '1s@/\env @/@' -i $i
done
%fdupes -s %{buildroot}/%{pkg_skeldir}/templates

%if %{with hpc}
%{hpc_write_modules_files}
#%%Module1.0#####################################################################

proc ModulesHelp { } {

puts stderr " "
puts stderr "This module loads the %{pname} library built with the %{compiler_family} compiler"
puts stderr "toolchain and the %{mpi_flavor} MPI stack."
puts stderr "\nVersion %{version}\n"

}
module-whatis "Name: %{pname} built with %{compiler_family} compiler and %{mpi_flavor} MPI"
module-whatis "Version: %{version}"
module-whatis "Category: runtime library"
module-whatis "Description: %{SUMMARY}"
module-whatis "%{url}"

set     version                     %{version}

depends-on phdf5

prepend-path    PATH                %{hpc_bindir}
prepend-path    LD_LIBRARY_PATH     %{hpc_libdir}
prepend-path    PYTHONPATH          %{hpc_libdir}/python

setenv          %{hpc_upcase %{pname}}_DIR        %{hpc_prefix}
setenv          %{hpc_upcase %{pname}}_BIN        %{hpc_bindir}
setenv          %{hpc_upcase %{pname}}_LIB        %{hpc_libdir}
setenv          %{hpc_upcase %{pname}}_ETC        %{hpc_prefix}/etc

if {[file isdirectory  %{hpc_includedir}]} {
prepend-path    LIBRARY_PATH        %{hpc_libdir}
prepend-path    INCLUDE             %{hpc_includedir}
prepend-path    CPATH               %{hpc_includedir}
prepend-path    C_INCLUDE_PATH      %{hpc_includedir}
prepend-path    CPLUS_INCLUDE_PATH  %{hpc_includedir}

setenv          %{hpc_upcase %{pname}}_INC        %{hpc_includedir}
}

EOF
%endif

%files
%if %{with hpc}
%{hpc_dirs}
%{hpc_modules_files}
%endif
%{pkg_bindir}
%{!?with_hpc:%config} %{pkg_sysconfdir}/*
%dir %{pkg_prefix}/etc
%{pkg_skeldir}
%{pkg_libdir}/python
%license COPYING
%doc AUTHORS KNOWN_BUGS NEWS README.md TODO

%files devel
%{pkg_incdir}

%files devel-static
%{pkg_libdir}/*.a

%if %{with hpc}
%postun 
%hpc_module_delete_if_default
%endif

%changelog
