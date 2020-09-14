#
# spec file for package metis
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

%define vers 5.1.0
%define _vers 5_1_0
%define short_ver 5.1
%define src_ver %{version}
%define pname metis
%define somajor 5

%if "%{flavor}" == ""
ExclusiveArch:  do_not_build
%define package_name %pname
%bcond_with hpc
%endif

%if "%{flavor}" == "serial"
%bcond_with hpc
%endif

%if "%{flavor}" == "gnu-hpc"
%bcond_without hpc
%global compiler_family gnu
%undefine c_f_ver
%endif

%if "%{flavor}" == "gnu6-hpc"
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 6
%undefine mpi_flavor
%endif

%if "%{flavor}" == "gnu7-hpc"
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 7
%undefine mpi_flavor
%endif

%if "%{flavor}" == "gnu8-hpc"
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 8
%undefine mpi_flavor
%endif

%if "%{flavor}" == "gnu9-hpc"
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 9
%undefine mpi_flavor
%endif

%if "%{flavor}" == "gnu10-hpc"
%bcond_without hpc
%define compiler_family gnu
%define c_f_ver 10
%undefine mpi_flavor
%endif

%if %{without hpc}
%if 0%{!?package_name:1}
%define package_name  %{pname}
%endif
%define p_prefix %_prefix
%define p_includedir %_includedir
%define p_libdir %_libdir
%define p_bindir %_bindir
%define p_mandir %_mandir
%define p_datadir %_datadir
%define p_infodir %_infodir
%define libname lib%{pname}%{somajor}

%else

%define package_name %{hpc_package_name %_vers}
%define p_prefix %hpc_prefix
%define p_includedir %hpc_includedir
%define p_libdir %hpc_libdir
%define p_bindir %hpc_bindir
%define p_mandir %hpc_mandir
%define p_datadir %hpc_datadir
%define p_infodir %hpc_infodir
%define libname lib%{pname}%{hpc_package_name_tail %{_vers}}

%{hpc_init -c %{compiler_family} %{?c_f_ver:-v %{c_f_ver}} %{?ext:-e %{ext}}}
%endif

Name:           %{package_name}
Version:        %{vers}
Release:        0
Summary:        Serial Graph Partitioning and Fill-reducing Matrix Ordering
License:        Apache-2.0
Group:          Productivity/Scientific/Math
URL:            http://glaros.dtc.umn.edu/gkhome/metis/metis/overview
Source0:        http://glaros.dtc.umn.edu/gkhome/fetch/sw/metis/%{pname}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE metis-cmake.patch
Patch1:         metis-cmake.patch
# PATCH-FIX-OPENSUSE metis-programs-no-compilation-time.patch -- Fix W: file-contains-date-and-time
Patch2:         metis-programs-no-compilation-time.patch
Patch3:         metis-makefile-c-directives.patch
BuildRequires:  cmake >= 2.8
BuildRequires:  gcc
BuildRequires:  gcc-c++
%if %{with hpc}
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel
BuildRequires:  lua-lmod
BuildRequires:  suse-hpc
%hpc_requires
Requires:       %libname = %version
%endif

Recommends:     %{name}-doc = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
METIS is a family of programs for partitioning unstructured graphs and hypergraph
and computing fill-reducing orderings of sparse matrices. The underlying algorithms
used by METIS are based on a multilevel paradigm that, at the time, had been
shown to produce quality results and scale to large problems.

%{?with_hpc:%{hpc_master_package -L}}

%package     -n %{libname}
Summary:        Serial Graph Partitioning and Fill-reducing Matrix Ordering library
Group:          System/Libraries
Obsoletes:      %libname < %{version}

%description -n %{libname}
METIS library provides to partitioning unstructured graphs and hypergraph
and computing fill-reducing orderings of sparse matrices. The underlying algorithms
used by METIS are based on a multilevel paradigm that, at the time, had been
shown to produce quality results and scale to large problems.

%{?with_hpc:%{hpc_master_package -l -L}}

%package        devel
Summary:        Metis development files
Group:          Development/Libraries/C and C++
Requires:       %libname = %{version}
%if %{with hpc}
%hpc_requires_devel
Requires:       %libname = %version
%endif

%description    devel
METIS library provides to partitioning unstructured graphs and hypergraph
and computing fill-reducing orderings of sparse matrices. The underlying algorithms
used by METIS are based on a multilevel paradigm that, at the time, had been
shown to produce quality results and scale to large problems.

This package provides development files.

%{?with_hpc:%{hpc_master_package -L devel}}

%package        doc
Summary:        Metis documentation
Group:          Documentation/Other
BuildArch:      noarch

%description    doc
METIS is a family of programs for partitioning unstructured graphs and hypergraph
and computing fill-reducing orderings of sparse matrices. The underlying algorithms
used by METIS are based on a multilevel paradigm that, at the time, had been
shown to produce quality results and scale to large problems.

%{?with_hpc:%{hpc_master_package doc}}

%package        examples
Summary:        Metis examples
Group:          Documentation/Other
BuildArch:      noarch

%description    examples
METIS library provides to partitioning unstructured graphs and hypergraph
and computing fill-reducing orderings of sparse matrices. This package provides
graph files you can use to test Metis.

%{?with_hpc:%{hpc_master_package examples}}

%prep
%{?with_hpc: %hpc_debug}
%setup -q -n %{pname}-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1

# set width (32 or 64 bits) of the elementary data type, see Install.txt
sed -i 's|#define IDXTYPEWIDTH 32|#define IDXTYPEWIDTH %{__isa_bits}|' include/metis.h

%build

%if %{with hpc}
%hpc_debug
%hpc_setup_compiler
%endif

make config shared=1 prefix=%{p_prefix} cflags="%{optflags} -fopenmp -pthread -fpie -pie" ldflags="-pie"
make %{?_smp_mflags}

%install
%{?with_hpc:%hpc_setup}
%{?with_hpc:%hpc_debug}
make install DESTDIR=%{buildroot}

%if %{with hpc}
%{hpc_write_pkgconfig}

%hpc_write_modules_files
#%%Module1.0#####################################################################

proc ModulesHelp { } {

puts stderr " "
puts stderr "This module loads the %{pname} library built with the %{compiler_family} compiler toolchain."
puts stderr "\nVersion %{version}\n"

}
module-whatis "Name: %{pname} built with %{compiler_family} toolchain"
module-whatis "Version: %{version}"
module-whatis "Category: runtime library"
module-whatis "Description: %{SUMMARY}"
module-whatis "%{url}"

set     version                     %{version}

prepend-path    PATH                %{hpc_bindir}
prepend-path    LD_LIBRARY_PATH     %{hpc_libdir}

setenv          %{hpc_upcase %pname}_DIR        %{hpc_prefix}
setenv          %{hpc_upcase %pname}_BIN        %{hpc_bindir}
setenv          %{hpc_upcase %pname}_LIB        %{hpc_libdir}

prepend-path    LIBRARY_PATH        %{hpc_libdir}
if {[file isdirectory  %{hpc_includedir}]} {
prepend-path    CPATH               %{hpc_includedir}
prepend-path    C_INCLUDE_PATH      %{hpc_includedir}
prepend-path    CPLUS_INCLUDE_PATH  %{hpc_includedir}
prepend-path    INCLUDE             %{hpc_includedir}
%hpc_modulefile_add_pkgconfig_path
setenv          %{hpc_upcase %pname}_INC        %{hpc_includedir}
}

family "%pname"

EOF
%endif

%check
pushd graphs
LD_LIBRARY_PATH=%{buildroot}%{p_libdir}:$LD_LIBRARY_PATH %{buildroot}%{p_bindir}/ndmetis mdual.graph
LD_LIBRARY_PATH=%{buildroot}%{p_libdir}:$LD_LIBRARY_PATH %{buildroot}%{p_bindir}/mpmetis metis.mesh 2
LD_LIBRARY_PATH=%{buildroot}%{p_libdir}:$LD_LIBRARY_PATH %{buildroot}%{p_bindir}/gpmetis test.mgraph 4
LD_LIBRARY_PATH=%{buildroot}%{p_libdir}:$LD_LIBRARY_PATH %{buildroot}%{p_bindir}/gpmetis copter2.graph 4
LD_LIBRARY_PATH=%{buildroot}%{p_libdir}:$LD_LIBRARY_PATH %{buildroot}%{p_bindir}/graphchk 4elt.graph
popd

%if %{without hpc}
%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig
%else
%post -n %libname
/sbin/ldconfig -N %{p_libdir}

%postun -n %libname
/sbin/ldconfig -N %{p_libdir}
%hpc_module_delete_if_default
%endif

%files
%{?with_hpc:%dir %p_bindir}
%doc Changelog
%license LICENSE.txt
%{p_bindir}/*

%files -n %{libname}
%{?with_hpc:%hpc_dirs}
%{?hpc_modules_files}
%{p_libdir}/lib%{pname}.so.%{somajor}*

%files devel
%{?with_hpc:%dir %{p_includedir}}
%{p_includedir}/%{pname}.h
%{p_libdir}/lib%{pname}.so
%{?with_hpc:%{hpc_pkgconfig_file -n %{pname}}}

%files doc
%doc manual/manual.pdf

%files examples
%doc graphs

%changelog
