#
# spec file for package superlu
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
%define pname superlu
%define ver 5.2.1

%define _ver %(echo %{ver} | tr . _)

%if "%flavor" == ""
ExclusiveArch:  do_not_build
%endif

%if "%{flavor}" == "serial"
%bcond_with hpc
%endif

%if "%{flavor}" == "gnu-hpc"
%bcond_without hpc
%global compiler_family gnu
%undefine c_f_ver
%endif

%if "%{flavor}" == "gnu7-hpc"
%bcond_without hpc
%global compiler_family gnu
%undefine c_f_ver 7
%endif

%if "%{flavor}" == "gnu8-hpc"
%bcond_without hpc
%global compiler_family gnu
%define c_f_ver 8
%endif

%if "%{flavor}" == "gnu9-hpc"
%bcond_without hpc
%global compiler_family gnu
%define c_f_ver 9
%endif

%if "%{flavor}" == "gnu10-hpc"
%bcond_without hpc
%global compiler_family gnu
%define c_f_ver 10
%endif

%bcond_with ringdisabled

%if %{with hpc} && %{with ringdisabled}
ExclusiveArch:  do_not_build
%endif

%define package_name %pname
%if %{without hpc}
%define p_prefix %_prefix
%define p_includedir %_includedir
%define p_libdir %_libdir
%define _sover 5
%define libname lib%{name}%{?_sover}
%else
%{hpc_init -c %compiler_family %{?c_f_ver:-v %{c_f_ver}} %{?ext:-e %{ext}}}
%define package_name %{hpc_package_name %_ver}
%define p_prefix %hpc_prefix
%define p_includedir %hpc_includedir
%define p_libdir %hpc_libdir
%define libname lib%{name}
%endif

Name:           %{package_name}
Summary:        A general purpose library for the direct solution of linear equations
License:        BSD-3-Clause
Group:          Productivity/Scientific/Math
Version:        %{ver}
Release:        0
Source:         http://crd-legacy.lbl.gov/%7Exiaoye/SuperLU/%{pname}_%{version}.tar.gz
Source1:        superlu_ug.pdf
Source2:        README.SUSE
# PATCH-FEATURE-OPENSUSE superlu-5.2-make.patch : add compiler and build flags in make.inc
Patch0:         superlu-5.2-make.patch
# PATCH-FIX-UPSTREAM superlu-4.3-include.patch : avoid implicit declaration warnings
Patch1:         superlu-4.3-include.patch
# PATCH-FIX-UPSTREAM superlu-4.3-dont-opt-away.diff
Patch2:         superlu-4.3-dont-opt-away.diff
# PATCH-FIX-OPENSUSE superlu-5.2-remove-mc64ad.patch [bnc#796236]
# The Harwell Subroutine Library (HSL) routine mc64ad.c have been removed
# from the original sources for legal reasons. This patch disables the inclusion of
# this routine in the library which, however, remains fully functional
Patch3:         superlu-5.2-remove-mc64ad.patch
Patch4:         superlu-examples_Makefile_remove_itersol.patch
Patch5:         superlu-make.linux.patch
URL:            http://crd.lbl.gov/~xiaoye/SuperLU/
BuildRequires:  cmake >= 2.8.12
BuildRequires:  fdupes
BuildRequires:  tcsh
%if %{without hpc}
BuildRequires:  blas-devel
BuildRequires:  gcc-fortran
%else
Requires:       %{compiler_family}%{?c_f_ver}-compilers-hpc
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel
BuildRequires:  libopenblas%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc-devel
BuildRequires:  suse-hpc >= 0.3
%endif

%description
SuperLU is an algorithm that uses group theory to optimize LU
decomposition of sparse matrices.

Documentation can be found in the %{name}-doc package or on
http://www.netlib.org.

%package -n %libname
Summary:        SuperLU matrix solver
Group:          System/Libraries
%if %{with hpc}
Requires:       libopenblas%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc
Requires:       lua-lmod >= 7.6.1
%hpc_requires
%endif

%description -n %libname
SuperLU is an algorithm that uses group theory to optimize LU
decomposition of sparse matrices.

%package        devel
Summary:        Headers and development library for lib%{name}%{?_sover}
Group:          Development/Libraries/C and C++
Requires:       %libname = %version
%if %{with hpc}
Requires:       libopenblas%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc-devel
%hpc_requires_devel
%endif
Recommends:     %name-doc

%description    devel
SuperLU headers and libraries files needed for development

%package        doc
Summary:        Documentation for %name
Group:          Documentation/Other

%description    doc
Documentation (HTML/PDF) for SuperLU.
SuperLU is an algorithm that uses group theory to optimize LU
decomposition of sparse matrices.

%package        examples
Summary:        Examples for %name
Group:          Documentation/Other
Recommends:     %name-devel

%description    examples
Example programs for SuperLU.
SuperLU is an algorithm that uses group theory to optimize LU
decomposition of sparse matrices.

%if %{with hpc}
%{hpc_master_package -l -L}
%{hpc_master_package -L devel}
%{hpc_master_package doc}
%{hpc_master_package -L examples}
%endif

%prep
%setup -q -n SuperLU_%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0
%patch5 -p0
cp %SOURCE1 %SOURCE2 ./
# Create baselibs.conf dynamically (non-HPC build only).
%if %{without hpc}
cat > %{_sourcedir}/baselibs.conf  <<EOF
lib%{name}%{?_sover}
EOF
%endif

%build
%{?hpc_setup}
%if %{without hpc}
%cmake \
%else
module load openblas
%hpc_cmake \
%endif
  -DCMAKE_BUILD_TYPE=Release -DUSE_XSDK_DEFAULTS='TRUE' -Denable_tests=OFF
make %{?_smp_mflags}

%install
%cmake_install
#fix permissions
chmod 644 MATLAB/*

# remove all build examples
cd EXAMPLE
make clean
rm -rf *itersol* .gitignore
cd ..
mv EXAMPLE examples
cp MAKE_INC/make.linux examples/make.inc
sed -i -e 's&@superlu_home@&%p_prefix&' -e 's&@superlu_lib@&%p_libdir&' examples/make.inc
rm -f examples/.gitignore
cp FORTRAN/README README.fortran
%fdupes -s examples

%if %{with hpc}
%{hpc_write_pkgconfig}

# TODO: is there any path to add for Matlab files?
%hpc_write_modules_files
#%Module1.0#####################################################################

proc ModulesHelp { } {

puts stderr " "
puts stderr "This module loads the SuperLU library built with the %{compiler_family} compiler"
puts stderr "toolchain."
puts stderr " "
puts stderr "Note that this build of SuperLU leverages the OpenBLAS linear algebra libraries."
puts stderr "Consequently, openblas is loaded automatically with this module."

puts stderr "\nVersion %{version}\n"

}
module-whatis "Name: %{pname} built with %{compiler_family} compiler"
module-whatis "Version: %{version}"
module-whatis "Category: runtime library"
module-whatis "Description: %{SUMMARY}"
module-whatis "%{url}"

set     version                     %{version}

depends-on openblas

if {[file isdirectory  %{hpc_includedir}]} {
prepend-path    INCLUDE             %{hpc_includedir}
}
prepend-path    LD_LIBRARY_PATH     %{hpc_libdir}

setenv          %{hpc_PNAME %pname}_DIR        %{hpc_prefix}
if {[file isdirectory  %{hpc_includedir}]} {
setenv          %{hpc_PNAME %pname}_INC        %{hpc_includedir}
%hpc_modulefile_add_pkgconfig_path
}
setenv          %{hpc_PNAME %pname}_LIB        %{hpc_libdir}

EOF
%endif

%if %{without hpc}
%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig
%else
%post -n %libname
/sbin/ldconfig -N %hpc_libdir

%postun -n %libname
/sbin/ldconfig -N %hpc_libdir
%hpc_module_delete_if_default
%endif

%files -n %libname
%doc README MATLAB README.SUSE
%{?with_hpc:%hpc_dirs}
%{?with_hpc:%hpc_modules_files}
%{p_libdir}/*.so.*

%files devel
%doc README.fortran
%{?with_hpc:%{hpc_pkgconfig_file}}
%{p_includedir}/%{!?with_hpc:*}
%{p_libdir}/*.so

%files doc
%doc DOC/html superlu_ug.pdf

%files examples
%doc examples

%changelog
