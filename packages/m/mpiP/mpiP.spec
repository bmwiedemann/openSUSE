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

%define pname mpiP
%define _vers 3_5

%if 0%{?sle_version} >= 150200
%define DisOMPI1 ExclusiveArch:  do_not_build
%endif
%if 0%{?sle_version} >= 150300
%define DisOMPI2 ExclusiveArch:  do_not_build
%endif

%if "%flavor" == ""
ExclusiveArch:  do_not_build
%endif

%if "%{flavor}" == "gnu-openmpi4-hpc"
%{?DisOMPI4}
%global compiler_family gnu
%undefine c_f_ver
%define mpi_family openmpi
%define mpi_ver 4
%endif

%if "%{flavor}" == "gnu-openmpi5-hpc"
%{?DisOMPI5}
%global compiler_family gnu
%undefine c_f_ver
%define mpi_family openmpi
%define mpi_ver 5
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

%if "%{flavor}" == "gnu7-openmpi4-hpc"
%{?DisOMPI4}
%global compiler_family gnu
%define c_f_ver 7
%define mpi_family openmpi
%define mpi_ver 4
%endif

%if "%{flavor}" == "gnu7-openmpi5-hpc"
%{?DisOMPI5}
%global compiler_family gnu
%define c_f_ver 7
%define mpi_family openmpi
%define mpi_ver 5
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

%if "%{flavor}" == "gnu8-openmpi4-hpc"
%{?DisOMPI4}
%global compiler_family gnu
%define c_f_ver 8
%define mpi_family openmpi
%define mpi_ver 4
%endif

%if "%{flavor}" == "gnu8-openmpi5-hpc"
%{?DisOMPI5}
%global compiler_family gnu
%define c_f_ver 8
%define mpi_family openmpi
%define mpi_ver 5
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

%if "%{flavor}" == "gnu9-openmpi4-hpc"
%{?DisOMPI4}
%global compiler_family gnu
%define c_f_ver 9
%define mpi_family openmpi
%define mpi_ver 4
%endif

%if "%{flavor}" == "gnu9-openmpi5-hpc"
%{?DisOMPI5}
%global compiler_family gnu
%define c_f_ver 9
%define mpi_family openmpi
%define mpi_ver 5
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

%if "%{flavor}" == "gnu10-openmpi4-hpc"
%{?DisOMPI4}
%global compiler_family gnu
%define c_f_ver 10
%define mpi_family openmpi
%define mpi_ver 4
%endif

%if "%{flavor}" == "gnu10-openmpi5-hpc"
%{?DisOMPI5}
%global compiler_family gnu
%define c_f_ver 10
%define mpi_family openmpi
%define mpi_ver 5
%endif

%if "%{flavor}" == "gnu10-mvapich2-hpc"
%global compiler_family gnu
%define c_f_ver 10
%define mpi_family mvapich2
%endif

%if "%{flavor}" == "gnu10-mpich-hpc"
%global compiler_family gnu
%define c_f_ver 10
%define mpi_family mpich
%endif

%{?hpc_init:%{hpc_init -c %compiler_family -m %mpi_family %{?c_f_ver:-v %{c_f_ver}} %{?mpi_ver:-V %{mpi_ver}} %{?ext:-e %{ext}}}}

Name:           %{?hpc_package_name:%{hpc_package_name %_vers}}%{!?hpc_package_name:%pname}
Summary:        A profiling library for MPI applications
License:        BSD-3-Clause
Group:          Development/Tools/Debuggers
Version:        3.5
Release:        0
ExcludeArch:    i586 %arm s390
URL:            https://github.com/LLNL/mpiP
Source0:        https://github.com/LLNL/mpiP/releases/download/%{version}/mpip-%{version}.tgz#/%{pname}-%{version}.tgz
Patch1:         mpip.unwinder.patch
Patch2:         Add-return-value-to-non-void-function.patch
Patch3:         pc_lookup-replace-PTR-with-void.patch
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel
BuildRequires:  %{mpi_family}%{?mpi_ver}-%{compiler_family}%{?c_f_ver}-hpc-macros-devel
BuildRequires:  binutils-devel
BuildRequires:  dejagnu
BuildRequires:  libunwind-devel
BuildRequires:  lua-lmod
BuildRequires:  python3
#BuildRequires:  slurm-node
BuildRequires:  suse-hpc
%{?hpc_requires}

%description
mpiP is a profiling library for MPI applications.
It only collects statistical information about MPI functions, so mpiP
generates less overhead and much less data than tracing
tools. All the information captured by mpiP is task-local. It only
uses communication during report generation, typically at the end of
the experiment, to merge results from all of the tasks into one output
file.

%{hpc_master_package -L}

%package devel
Summary:        Headers for profiling library for MPI applications
Group:          Development/Libraries/C and C++
%{?hpc_requires_devel}

%description devel
mpiP is a profiling library for MPI applications. This packages contains
the build headers.

%{hpc_master_package devel}

%package devel-static
Summary:        Static version of profiling library for MPI applications
Group:          Development/Libraries/C and C++
%{?hpc_requires_devel}

%description devel-static
mpiP is a profiling library for MPI applications.

This package contains the static libraries.

%package doc
Summary:        Documentation for the mpiP profiling library
Group:          Documentation/Other

%description doc
mpiP is a profiling library for MPI applications.

This contains the documentation.

%{hpc_master_package doc}

%if "%(echo %version | tr '.' '_')" != "%_vers"
%{error: Fix _vers variable to match package version!}
%endif

%prep
%setup -q -n %{pname}-%{version}
%autopatch -p1
sed -i -e "/-shared -o \$@/s#\(\${LDFLAGS}\)#\1 -Wl,-soname,\$@#" Makefile.in

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%hpc_setup
export CC=mpicc
export CXX=mpicxx
export FC=mpifort
export F77=$FC
export CFLAGS="-D__DATE__=\\\"NODATE\\\" -D__TIME__=\\\"NOTIME\\\""
export FFLAGS="-std=legacy"
export HAVE_PYTHON="python3"
%hpc_configure \
    --enable-demangling \
%ifarch aarch64
    --enable-setjmp \
%endif
    --docdir=%{_docdir}/%{name}

make %{?_smp_mflags} PYTHON="python3" shared

%install
%hpc_setup
make install-all DESTDIR=%{?buildroot}
find "%{buildroot}" -type f -name "*.a" -exec chmod a-x {} +
find "%{buildroot}/%{_docdir}" -type f -exec chmod a-x {} +
find "%{buildroot}/%{hpc_includedir}" -type f -exec chmod a-x {} +
%{hpc_shebang_sanitize_scripts %{buildroot}%{hpc_bindir}}
for i in mpirun-mpip srun-mpip; do
    sed -i \
	-e "s@\(MPIP_DIR=\).*@\1%{?hpc_prefix}@" \
	-e "s@\(LD_PRELOAD=\).*:\(.*\)@\1\2@" \
	-e "s@\(ADDTL_RT_LIBS=.*\)@#\1@" \
	-e "s@/lib/libmpiP.so@/%{_lib}/libmpiP.so@" %{buildroot}%{hpc_bindir}/$i
done

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

prepend-path    PATH                %{hpc_bindir}
prepend-path    LD_LIBRARY_PATH     %{hpc_libdir}
if {[file isdirectory  %{hpc_includedir}]} {
prepend-path    C_INCLUDE_PATH      %{hpc_includedir}
prepend-path    INCLUDE             %{hpc_includedir}
}

setenv          %{hpc_upcase %pname}_DIR        %{hpc_prefix}
setenv          %{hpc_upcase %pname}_LIB        %{hpc_libdir}

EOF

%check
%hpc_setup
export CC=mpicc
export CXX=mpicxx
export FC=mpifort
export F77=$FC
export FFLAGS="-std=legacy"
LD_LIBRARY_PATH=$(pwd)${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
make FFLAGS+=${FFLAGS} check || exit 0

%postun
%hpc_module_delete_if_default

%files
%{hpc_dirs}
%{hpc_modules_files}
%{hpc_libdir}/*so
%{hpc_bindir}

%files doc
%{_docdir}/%{name}/

%files devel
%{hpc_includedir}

%files devel-static
%{hpc_libdir}/*.a

%changelog
