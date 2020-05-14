#
# spec file for package ocr
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

# Base package name
%define pname ocr
%define PNAME %(echo %{pname} | tr [a-z] [A-Z])
%define _ver 1_0_1

%if 0%{?sle_version} >= 150200
%define DisOMPI1 ExclusiveArch:  do_not_build
%endif

# Build options

%if "%flavor" == ""
%define package_name %{pname}
ExclusiveArch:  do_not_build
%endif

%if "%{flavor}" == "gnu-hpc"
%define compiler_family gnu
%undefine c_f_ver
%bcond_with mpi
%endif

%if "%{flavor}" == "gnu-mvapich2-hpc"
%define compiler_family gnu
%undefine c_f_ver
%global mpi_family mvapich2
%bcond_without mpi
%endif

%if "%{flavor}" == "gnu-mpich-hpc"
%define compiler_family gnu
%undefine c_f_ver
%global mpi_family mpich
%bcond_without mpi
%endif

%if "%{flavor}" == "gnu-openmpi-hpc"
%define compiler_family gnu
%undefine c_f_ver
%global mpi_family openmpi
%define mpi_vers 1
%bcond_without mpi
%{?DisOMPI1}
%endif

%if "%{flavor}" == "gnu-openmpi2-hpc"
%define compiler_family gnu
%undefine c_f_ver
%global mpi_family openmpi
%define mpi_vers 2
%bcond_without mpi
%{?DisOMPI2}
%endif

%if "%{flavor}" == "gnu-openmpi3-hpc"
%define compiler_family gnu
%undefine c_f_ver
%global mpi_family openmpi
%define mpi_vers 3
%bcond_without mpi
%{?DisOMPI3}
%endif

%{hpc_init -c %compiler_family %{?c_f_ver:-v %{c_f_ver}} %{?with_mpi:-m {%mpi_family}} %{?mpi_ver:-V %{mpi_ver}} %{?ext:-e %{ext}}}
%{?hpc_package_name:%define package_name %{hpc_package_name %_ver}}

Name:           %package_name
Version:        1.0.1
Release:        0
Summary:        Open Community Runtime (OCR) for shared memory
License:        BSD-3-Clause
Group:          Productivity/Clustering/Computing
URL:            https://xstack.exascale-tech.com/wiki
# The Wiki/git-repo/download site for the source code at Exascale
# seems to have issues. Let's hope these are temporary.
# Source0:       https://xstack.exascale-tech.com/git/public/snapshots/ocr-refs/tags/OCRv%%{version}.tbz2
Source0:        OCRv%{version}.tbz2
Patch0:         reproducible.patch
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel
BuildRequires:  fdupes
BuildRequires:  suse-hpc
%if %{with mpi}
BuildRequires:  %{mpi_family}%{?mpi_vers}-%{compiler_family}%{?c_f_ver}-hpc-macros-devel
Requires:       %{mpi_family}%{?mpi_vers}-%{compiler_family}%{?c_f_ver}-hpc
%endif
%hpc_requires

%description
The Open Community Runtime project is an application
building framework that explores methods for high-core-count
programming with focus on HPC applications.

%package -n %{hpc_package_name %_ver}-devel
Summary:        Headers and development files for the Open Community Runtime
Group:          Development/Libraries/Parallel
Requires:       %{hpc_package_name %_ver}
%hpc_requires_devel

%description -n %{hpc_package_name %_ver}-devel
The Open Community Runtime project is an application
building framework that explores methods for high-core-count
programming with focus on HPC applications.

OCR headers and libraries files needed for development.

%package        doc
Summary:        Documentation for %{package_name}
Group:          Documentation/Other

%description    doc
The Open Community Runtime project is an application
building framework that explores methods for high-core-count
programming with focus on HPC applications.

Documentation for ocr packages.

%package        examples
Summary:        Examples for %{package_name}
Group:          Documentation/Other
Recommends:     %{package_name}

%description    examples
The Open Community Runtime project is an application
building framework that explores methods for high-core-count
programming with focus on HPC applications.

Examples for ocr packages.

%{hpc_master_package -L}
%{hpc_master_package -L devel}
%{hpc_master_package doc}
%{hpc_master_package -L examples}

%prep

%setup -q -n ocr-OCRv%{version}
%patch0 -p1

%build
cd ocr/build
%hpc_setup

OCR_TYPE=x86 make %{?_smp_mflags} all
%if %{with mpi}
OCR_TYPE=x86-mpi make %{?_smp_mflags} all
%endif

%install
mv ocr/tests examples
find ./examples -type f -a -name ".*" -delete
%fdupes -s examples
cd ocr/build
%hpc_setup

mkdir -p %{buildroot}/%{hpc_prefix}
make OCR_TYPE=x86 OCR_INSTALL=%{buildroot}/%{hpc_prefix} %{?_smp_mflags} install
%if %{with mpi}
make OCR_TYPE=x86-mpi OCR_INSTALL=%{buildroot}/%{hpc_prefix} %{?_smp_mflags} install
%endif
%if "%{hpc_prefix}/lib" != "%{hpc_libdir}"
mv %{buildroot}/%{hpc_prefix}/lib %{buildroot}/%{hpc_libdir}
%endif
cd  %{buildroot}/%{hpc_prefix}/config/
ln -s default.cfg generated.cfg
cd -
# Remove static libraries
find "%buildroot" -type f "(" -name "*.a" -o -name "*.la" ")" -delete
# Add the spec
%{hpc_write_pkgconfig}

%hpc_write_modules_files
#%%Module1.0#####################################################################

proc ModulesHelp { } {

puts stderr " "
puts stderr "This module loads the %{PNAME} library built with the %{compiler_family} compiler toolchain %{?with_mpi: using %{mpi_family}%{?mpi_vers}} for shared memory"
puts stderr "\nVersion %{version}\n"

}
module-whatis "Name: %{PNAME} for shared memory built with %{compiler_family} toolchain%{?with_mpi: using %{mpi_family}%{?mpi_vers}}"
module-whatis "Version: %{version}"
module-whatis "Category: runtime library"
module-whatis "Description: %{SUMMARY}"
module-whatis "%{url}"

set             version		    %{version}

prepend-path    PATH                %{hpc_bindir}
if {[file isdirectory  %{hpc_includedir}]} {
prepend-path    INCLUDE             %{hpc_includedir}
}
prepend-path    LD_LIBRARY_PATH     %{hpc_libdir}

setenv          %{PNAME}_DIR        %{hpc_prefix}
setenv          %{PNAME}_BIN        %{hpc_bindir}
setenv          %{PNAME}_LIB        %{hpc_libdir}
if {[file isdirectory  %{hpc_includedir}]} {
setenv          %{PNAME}_INC        %{hpc_includedir}
prepend-path    CPATH               %{hpc_includedir}
prepend-path    C_INCLUDE_PATH      %{hpc_includedir}
prepend-path    CPLUS_INCLUDE_PATH  %{hpc_includedir}
%hpc_modulefile_add_pkgconfig_path
}
setenv          OCR_INSTALL         %{hpc_prefix}
setenv          OCR_TYPE            x86

EOF
%fdupes -s %{buildroot}

%postun
%hpc_module_delete_if_default

%files
%license ocr/LICENSE
%hpc_modules_files
%{hpc_dirs}
%dir %hpc_bindir
%hpc_libdir/*.so
%hpc_pkgconfig_file
%hpc_bindir/ocrrun
%hpc_prefix/config

%files devel
%license ocr/LICENSE
%{hpc_includedir}

%files doc
%doc ocr/spec/ocr-1.0.1.pdf

%files examples
%license ocr/LICENSE
%doc examples

%changelog
