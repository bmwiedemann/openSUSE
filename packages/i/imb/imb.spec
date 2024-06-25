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

# Base package name
%define pname imb
%define PNAME IMB
%define ver 2021.7
%define _ver 2021_7

%if 0%{?sle_version} >= 150200
%define DisOMPI1 ExclusiveArch:  do_not_build
%endif
%if !0%{?is_opensuse} && 0%{?sle_version:1} && 0%{?sle_version} < 150200
%define DisOMPI3 ExclusiveArch:  do_not_build
%endif

%if "%flavor" == ""
%define package_name %{pname}
ExclusiveArch:  do_not_build
%endif

%if "%{flavor}" == "mvapich2"
%{bcond_with hpc}
%undefine c_f_ver
%global mpi_flavor mvapich2
%define buildtarget "IMB-MPI1 IMB-EXT IMB-IO IMB-P2P"
%endif

%if "%{flavor}" == "mpich"
%{bcond_with hpc}
%undefine c_f_ver
%global mpi_flavor mpich
%define buildtarget "IMB-MPI1 IMB-EXT IMB-IO IMB-P2P"
%endif

%if "%{flavor}" == "openmpi4"
%{bcond_with hpc}
%undefine c_f_ver
%global mpi_flavor openmpi
%define mpi_vers 4
%define buildtarget "IMB-MPI1 IMB-EXT IMB-P2P"
%{?DisOMPI4}
%endif

%if "%{flavor}" == "openmpi5"
%{bcond_with hpc}
%undefine c_f_ver
%global mpi_flavor openmpi
%define mpi_vers 4
%define buildtarget "IMB-MPI1 IMB-EXT IMB-P2P"
%{?DisOMPI5}
%endif

%if "%{flavor}" == "gnu-mvapich2-hpc"
%{bcond_without hpc}
%define compiler_family gnu
%undefine c_f_ver
%global mpi_flavor mvapich2
%define buildtarget "IMB-MPI1 IMB-EXT IMB-IO IMB-P2P"
%endif

%if "%{flavor}" == "gnu-mpich-hpc"
%{bcond_without hpc}
%define compiler_family gnu
%undefine c_f_ver
# macro mpi is used by macros for master package
%global mpi_flavor mpich
%define buildtarget "IMB-MPI1 IMB-EXT IMB-IO IMB-P2P"
%endif

%if "%{flavor}" == "gnu-openmpi4-hpc"
%{bcond_without hpc}
%define compiler_family gnu
%undefine c_f_ver
# macro mpi is used by macros for master package
%global mpi_flavor openmpi
%define mpi_vers 4
%define buildtarget "IMB-MPI1 IMB-EXT IMB-P2P"
%{?DisOMPI4}
%endif

%if "%{flavor}" == "gnu-openmpi5-hpc"
%{bcond_without hpc}
%define compiler_family gnu
%undefine c_f_ver
# macro mpi is used by macros for master package
%global mpi_flavor openmpi
%define mpi_vers 5
%define buildtarget "IMB-MPI1 IMB-EXT IMB-P2P"
%{?DisOMPI5}
%endif

%if "%{flavor}" == "gnu7-mvapich2-hpc"
%{bcond_without hpc}
%define compiler_family gnu
%define c_f_ver 7
%global mpi_flavor mvapich2
%define buildtarget "IMB-MPI1 IMB-EXT IMB-IO IMB-P2P"
%endif

%if "%{flavor}" == "gnu7-mpich-hpc"
%{bcond_without hpc}
%define compiler_family gnu
%define c_f_ver 7
# macro mpi is used by macros for master package
%global mpi_flavor mpich
%define buildtarget "IMB-MPI1 IMB-EXT IMB-IO IMB-P2P"
%endif

%if "%{flavor}" == "gnu7-openmpi4-hpc"
%{bcond_without hpc}
%define compiler_family gnu
%define c_f_ver 7
# macro mpi is used by macros for master package
%global mpi_flavor openmpi
%define mpi_vers 4
%define buildtarget "IMB-MPI1 IMB-EXT IMB-P2P"
%{?DisOMPI4}
%endif

%if "%{flavor}" == "gnu7-openmpi5-hpc"
%{bcond_without hpc}
%define compiler_family gnu
%define c_f_ver 7
# macro mpi is used by macros for master package
%global mpi_flavor openmpi
%define mpi_vers 5
%define buildtarget "IMB-MPI1 IMB-EXT IMB-P2P"
%{?DisOMPI5}
%endif

%if "%{flavor}" == "gnu8-mvapich2-hpc"
%{bcond_without hpc}
%define compiler_family gnu
%define c_f_ver 8
%global mpi_flavor mvapich2
%define buildtarget "IMB-MPI1 IMB-EXT IMB-IO IMB-P2P"
%endif

%if "%{flavor}" == "gnu8-mpich-hpc"
%{bcond_without hpc}
%define compiler_family gnu
%define c_f_ver 8
# macro mpi is used by macros for master package
%global mpi_flavor mpich
%define buildtarget "IMB-MPI1 IMB-EXT IMB-IO IMB-P2P"
%endif

%if "%{flavor}" == "gnu8-openmpi4-hpc"
%{bcond_without hpc}
%define compiler_family gnu
%define c_f_ver 8
# macro mpi is used by macros for master package
%global mpi_flavor openmpi
%define mpi_vers 4
%define buildtarget "IMB-MPI1 IMB-EXT IMB-P2P"
%{?DisOMPI4}
%endif

%if "%{flavor}" == "gnu8-openmpi5-hpc"
%{bcond_without hpc}
%define compiler_family gnu
%define c_f_ver 8
# macro mpi is used by macros for master package
%global mpi_flavor openmpi
%define mpi_vers 5
%define buildtarget "IMB-MPI1 IMB-EXT IMB-P2P"
%{?DisOMPI4}
%endif

%if "%{flavor}" == "gnu9-mvapich2-hpc"
%{bcond_without hpc}
%define compiler_family gnu
%define c_f_ver 9
%global mpi_flavor mvapich2
%define buildtarget "IMB-MPI1 IMB-EXT IMB-IO IMB-P2P"
%endif

%if "%{flavor}" == "gnu9-mpich-hpc"
%{bcond_without hpc}
%define compiler_family gnu
%define c_f_ver 9
# macro mpi is used by macros for master package
%global mpi_flavor mpich
%define buildtarget "IMB-MPI1 IMB-EXT IMB-IO IMB-P2P"
%endif

%if "%{flavor}" == "gnu9-openmpi4-hpc"
%{bcond_without hpc}
%define compiler_family gnu
%define c_f_ver 9
# macro mpi is used by macros for master package
%global mpi_flavor openmpi
%define mpi_vers 4
%define buildtarget "IMB-MPI1 IMB-EXT IMB-P2P"
%{?DisOMPI4}
%endif

%if "%{flavor}" == "gnu9-openmpi5-hpc"
%{bcond_without hpc}
%define compiler_family gnu
%define c_f_ver 9
# macro mpi is used by macros for master package
%global mpi_flavor openmpi
%define mpi_vers 5
%define buildtarget "IMB-MPI1 IMB-EXT IMB-P2P"
%{?DisOMPI5}
%endif

%if "%{flavor}" == "gnu10-mvapich2-hpc"
%{bcond_without hpc}
%define compiler_family gnu
%define c_f_ver 10
%global mpi_flavor mvapich2
%define buildtarget "IMB-MPI1 IMB-EXT IMB-IO IMB-P2P"
%endif

%if "%{flavor}" == "gnu10-mpich-hpc"
%{bcond_without hpc}
%define compiler_family gnu
%define c_f_ver 10
# macro mpi is used by macros for master package
%global mpi_flavor mpich
%define buildtarget "IMB-MPI1 IMB-EXT IMB-IO IMB-P2P"
%endif

%if "%{flavor}" == "gnu10-openmpi4-hpc"
%{bcond_without hpc}
%define compiler_family gnu
%define c_f_ver 10
# macro mpi is used by macros for master package
%global mpi_flavor openmpi
%define mpi_vers 4
%define buildtarget "IMB-MPI1 IMB-EXT IMB-P2P"
%{?DisOMPI4}
%endif

%if "%{flavor}" == "gnu10-openmpi5-hpc"
%{bcond_without hpc}
%define compiler_family gnu
%define c_f_ver 10
# macro mpi is used by macros for master package
%global mpi_flavor openmpi
%define mpi_vers 5
%define buildtarget "IMB-MPI1 IMB-EXT IMB-P2P"
%{?DisOMPI5}
%endif

%if "%{flavor}" == "gnu11-mvapich2-hpc"
%{bcond_without hpc}
%define compiler_family gnu
%define c_f_ver 11
%global mpi_flavor mvapich2
%define buildtarget "IMB-MPI1 IMB-EXT IMB-IO IMB-P2P"
%endif

%if "%{flavor}" == "gnu11-mpich-hpc"
%{bcond_without hpc}
%define compiler_family gnu
%define c_f_ver 11
# macro mpi is used by macros for master package
%global mpi_flavor mpich
%define buildtarget "IMB-MPI1 IMB-EXT IMB-IO IMB-P2P"
%endif

%if "%{flavor}" == "gnu11-openmpi3-hpc"
%{bcond_without hpc}
%define compiler_family gnu
%define c_f_ver 11
# macro mpi is used by macros for master package
%global mpi_flavor openmpi
%define mpi_vers 3
%define buildtarget "IMB-MPI1 IMB-EXT IMB-P2P"
%{?DisOMPI3}
%endif

%if "%{flavor}" == "gnu11-openmpi4-hpc"
%{bcond_without hpc}
%define compiler_family gnu
%define c_f_ver 11
# macro mpi is used by macros for master package
%global mpi_flavor openmpi
%define mpi_vers 4
%define buildtarget "IMB-MPI1 IMB-EXT IMB-P2P"
%{?DisOMPI4}
%endif

%if "%{flavor}" == "gnu12-mvapich2-hpc"
%{bcond_without hpc}
%define compiler_family gnu
%define c_f_ver 12
%global mpi_flavor mvapich2
%define buildtarget "IMB-MPI1 IMB-EXT IMB-IO IMB-P2P"
%endif

%if "%{flavor}" == "gnu12-mpich-hpc"
%{bcond_without hpc}
%define compiler_family gnu
%define c_f_ver 12
# macro mpi is used by macros for master package
%global mpi_flavor mpich
%define buildtarget "IMB-MPI1 IMB-EXT IMB-IO IMB-P2P"
%endif

%if "%{flavor}" == "gnu12-openmpi3-hpc"
%{bcond_without hpc}
%define compiler_family gnu
%define c_f_ver 12
# macro mpi is used by macros for master package
%global mpi_flavor openmpi
%define mpi_vers 3
%define buildtarget "IMB-MPI1 IMB-EXT IMB-P2P"
%{?DisOMPI3}
%endif

%if "%{flavor}" == "gnu12-openmpi4-hpc"
%{bcond_without hpc}
%define compiler_family gnu
%define c_f_ver 12
# macro mpi is used by macros for master package
%global mpi_flavor openmpi
%define mpi_vers 4
%define buildtarget "IMB-MPI1 IMB-EXT IMB-P2P"
%{?DisOMPI4}
%endif

%if %{without hpc}
%define p_bindir /usr/%_lib/mpi/gcc/%{flavor}/bin
%if "%{flavor}" == ""
%define package_name  %{pname}
%else
%define package_name  %{pname}-%{flavor}
%endif
%else
%{hpc_init -c %compiler_family %{?c_f_ver:-v %{c_f_ver}} -m {%mpi_flavor} %{?mpi_vers:-V %{mpi_vers}} %{?ext:-e %{ext}}}
%define package_name %{hpc_package_name %_ver}
%define p_bindir %hpc_bindir
ExcludeArch:    i586 %arm s390
%endif

Name:           %{package_name}
Version:        %ver
Release:        0
Summary:        Intel MPI Benchmarks (IMB)
License:        BSD-3-Clause
Group:          Development/Tools/Other
URL:            https://software.intel.com/en-us/articles/intel-mpi-benchmarks
Source0:        https://github.com/intel/mpi-benchmarks/archive/IMB-v%{version}.tar.gz#/%{pname}_%{version}.tar.gz
%if %{without hpc}
BuildRequires:  %{flavor}-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
Obsoletes:      imb < %{version}
%else
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel
BuildRequires:  %{mpi_flavor}%{?mpi_vers}-%{compiler_family}%{?c_f_ver}-hpc-macros-devel
BuildRequires:  suse-hpc
%hpc_requires
%endif

%description
The Intel MPI Benchmarks (IMB) perform a set of MPI performance
measurements for point-to-point and global communication operations for
a range of message sizes.

%{?with_hpc:%{hpc_master_package -L}}

%if "%(echo %version | tr '.' '_')" != "%_ver"
%{error: Fix _ver variable to match package version!}
%endif

%prep
%setup -n mpi-benchmarks-IMB-v%{version}

%build

%if %{without hpc}
%define makeargs CC=/usr/%_lib/mpi/gcc/%{flavor}/bin/mpicc CXX=/usr/%_lib/mpi/gcc/%{flavor}/bin/mpic++
. /usr/%_lib/mpi/gcc/%{flavor}/bin/mpivars.sh
%else
%{hpc_setup}
%define makeargs CC=mpicc CXX=mpic++
%endif
for target in $(echo %{?buildtarget}) ; do
echo "building $target"
make $target %{?makeargs} %{?_smp_mflags}
done
cd -

%install
%{__mkdir} -p %{buildroot}%{p_bindir}
cp IMB-*  %{buildroot}%{p_bindir}
mkdir -p %{buildroot}%{docdir}/%{name}
cat <<EOF > %{buildroot}%{docdir}/%{name}/README.SUSE
Product documentation is now available online only at: https://software.intel.com/en-us/imb-user-guide.
EOF
cd -

%if %{with hpc}
%hpc_write_modules_files
#%%Module1.0#####################################################################

proc ModulesHelp { } {

puts stderr " "
puts stderr "This module loads the %{pname} library built with the %{compiler_family} toolchain and %{mpi_flavor}%{?mpi_vers}."
puts stderr "\nVersion %{version}\n"

}
module-whatis "Name: %{pname} built with %{compiler_family} toolchain and %{mpi_flavor}%{?mpi_vers}"
module-whatis "Version: %{version}"
module-whatis "Category: application / benchmark"
module-whatis "Description: %{SUMMARY}"
module-whatis "URL: %{url}"

set     version                     %{version}

prepend-path    PATH                %{hpc_bindir}

setenv          %{PNAME}_DIR        %{hpc_prefix}

EOF
%endif

%postun
%{?with_hpc:%hpc_module_delete_if_default}

%files
%doc ReadMe_IMB.txt
%license license/license.txt license/use-of-trademark-license.txt
%if %{with hpc}
%hpc_modules_files
%dir %{hpc_install_path_base}
%dir %{hpc_prefix}
%endif
%{p_bindir}

%changelog
