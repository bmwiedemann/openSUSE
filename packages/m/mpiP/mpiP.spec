#
# spec file for package mpiP
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


%global flavor @BUILD_FLAVOR@%{nil}

%define pname mpiP
%define vers 3.4.1
%define _vers 3_4_1

%if 0%{?sle_version} >= 150200
%define DisOMPI1 ExclusiveArch:  do_not_build
%endif

%if "%flavor" == ""
ExclusiveArch:  do_not_build
%endif

%if "%{flavor}" == "gnu-openmpi-hpc"
%{?DisOMPI1}
%global compiler_family gnu
%undefine c_f_ver
%define mpi_family openmpi
%define mpi_ver 1
%endif

%if "%{flavor}" == "gnu-openmpi2-hpc"
%{?DisOMPI2}
%global compiler_family gnu
%undefine c_f_ver
%define mpi_family openmpi
%define mpi_ver 2
%endif

%if "%{flavor}" == "gnu-openmpi3-hpc"
%{?DisOMPI3}
%global compiler_family gnu
%undefine c_f_ver
%define mpi_family openmpi
%define mpi_ver 3
%endif

%if "%{flavor}" == "gnu-mvapich2-hpc"
%global compiler_family gnu
%undefine c_f_ver
%define mpi_family mvapich2
%endif

%if "%{flavor}" == "gnu-mpich-hpc"
%global compiler_family gnu
%undefine c_f_ver
%define mpi_family mpich
%endif

%if "%{flavor}" == "gnu7-openmpi-hpc"
%{?DisOMPI1}
%global compiler_family gnu
%define c_f_ver 7
%define mpi_family openmpi
%define mpi_ver 1
%endif

%if "%{flavor}" == "gnu7-openmpi2-hpc"
%{?DisOMPI3}
%global compiler_family gnu
%define c_f_ver 7
%define mpi_family openmpi
%define mpi_ver 2
%endif

%if "%{flavor}" == "gnu7-openmpi3-hpc"
%{?DisOMPI3}
%global compiler_family gnu
%define c_f_ver 7
%define mpi_family openmpi
%define mpi_ver 3
%endif

%if "%{flavor}" == "gnu7-mvapich2-hpc"
%global compiler_family gnu
%define c_f_ver 7
%define mpi_family mvapich2
%endif

%if "%{flavor}" == "gnu7-mpich-hpc"
%global compiler_family gnu
%define c_f_ver 7
%define mpi_family mpich
%endif

%if "%{flavor}" == "gnu8-openmpi-hpc"
%{?DisOMPI1}
%global compiler_family gnu
%define c_f_ver 8
%define mpi_family openmpi
%define mpi_ver 1
%endif

%if "%{flavor}" == "gnu8-openmpi3-hpc"
%{?DisOMPI3}
%global compiler_family gnu
%define c_f_ver 8
%define mpi_family openmpi
%define mpi_ver 3
%endif

%if "%{flavor}" == "gnu8-openmpi2-hpc"
%{?DisOMPI3}
%global compiler_family gnu
%define c_f_ver 8
%define mpi_family openmpi
%define mpi_ver 2
%endif

%if "%{flavor}" == "gnu8-mvapich2-hpc"
%global compiler_family gnu
%define c_f_ver 8
%define mpi_family mvapich2
%endif

%if "%{flavor}" == "gnu8-mpich-hpc"
%global compiler_family gnu
%define c_f_ver 8
%define mpi_family mpich
%endif

%if "%{flavor}" == "gnu9-openmpi-hpc"
%{?DisOMPI1}
%global compiler_family gnu
%define c_f_ver 9
%define mpi_family openmpi
%define mpi_ver 1
%endif

%if "%{flavor}" == "gnu9-openmpi2-hpc"
%{?DisOMPI3}
%global compiler_family gnu
%define c_f_ver 9
%define mpi_family openmpi
%define mpi_ver 2
%endif

%if "%{flavor}" == "gnu9-openmpi3-hpc"
%{?DisOMPI3}
%global compiler_family gnu
%define c_f_ver 9
%define mpi_family openmpi
%define mpi_ver 3
%endif

%if "%{flavor}" == "gnu9-mvapich2-hpc"
%global compiler_family gnu
%define c_f_ver 9
%define mpi_family mvapich2
%endif

%if "%{flavor}" == "gnu9-mpich-hpc"
%global compiler_family gnu
%define c_f_ver 9
%define mpi_family mpich
%endif

%{?hpc_init:%{hpc_init -c %compiler_family -m %mpi_family %{?c_f_ver:-v %{c_f_ver}} %{?mpi_ver:-V %{mpi_ver}} %{?ext:-e %{ext}}}}

Name:           %{?hpc_package_name:%{hpc_package_name %_vers}}%{!?hpc_package_name:%pname}
Summary:        A profiling library for MPI applications
License:        BSD-3-Clause
Group:          Development/Tools/Debuggers
Version:        %vers
Release:        0
URL:            http://mpip.sourceforge.net/
Source0:        http://sourceforge.net/projects/mpip/files/mpiP/mpiP-3.4.1/mpiP-%{version}.tar.gz
Patch1:         mpip.unwinder.patch

BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel
BuildRequires:  %{mpi_family}%{?mpi_ver}-%{compiler_family}%{?c_f_ver}-hpc-macros-devel
BuildRequires:  lua-lmod
BuildRequires:  python
BuildRequires:  suse-hpc
%hpc_requires
%hpc_requires_devel

%description
mpiP is a profiling library for MPI applications.
It only collects statistical information about MPI functions, so mpiP
generates less overhead and much less data than tracing
tools. All the information captured by mpiP is task-local. It only
uses communication during report generation, typically at the end of
the experiment, to merge results from all of the tasks into one output
file.

%{hpc_master_package -L}

%package devel-static
Summary:        Static version of profiling library for MPI applications
Group:          Development/Libraries/C and C++
%hpc_requires_devel

%description devel-static
mpiP is a profiling library for MPI applications.

%package doc
Summary:        Documentation for the mpiP profiling library
Group:          Documentation/Other

%description doc
mpiP is a profiling library for MPI applications.

This contains the documentation.

%{hpc_master_package doc}

%prep
%setup -q -n %{pname}-%{version}
%patch1 -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%hpc_setup
CC=mpicc
CXX=mpicxx
FC=mpif90
CFLAGS="-D__DATE__=\\\"NODATE\\\" -D__TIME__=\\\"NOTIME\\\""
%hpc_configure \
    --enable-demangling \
    --disable-libunwind \
%ifarch aarch64
    --enable-setjmp \
%endif
    --docdir=%{_docdir}/%{name}

make %{?_smp_mflags} shared

%install

%hpc_setup
%make_install
find "%{buildroot}" -type f -name "*.a" -exec chmod a-x {} +
find "%{buildroot}/%{_docdir}" -type f -exec chmod a-x {} +

%hpc_write_modules_files
#%%Module1.0#####################################################################

proc ModulesHelp { } {

puts stderr " "
puts stderr "This module loads the %{pname} library built with the %{compiler_family} compiler"
puts stderr "toolchain and the %{mpi_family} MPI stack."
puts stderr "\nVersion %{version}\n"

}
module-whatis "Name: %{pname} built with %{compiler_family} compiler and %{mpi_family} MPI"
module-whatis "Version: %{version}"
module-whatis "Category: Profiling library"
module-whatis "Description: %{SUMMARY:0}"
module-whatis "URL %{url}"

set     version                     %{version}

prepend-path    LD_LIBRARY_PATH     %{hpc_libdir}

setenv          %{hpc_upcase %pname}_DIR        %{hpc_prefix}
setenv          %{hpc_upcase %pname}_LIB        %{hpc_libdir}

EOF

%postun
%hpc_module_delete_if_default

%files
%defattr(-,root,root,-)
%{hpc_dirs}
%{hpc_modules_files}
%{hpc_libdir}/*so

%files doc
%defattr(0644,root,root,-)
%{_docdir}/%{name}/

%files devel-static
%defattr(0644,root,root,-)
%{hpc_libdir}/*.a

%changelog
