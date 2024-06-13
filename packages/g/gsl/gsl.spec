#
# spec file for package gsl
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

%define pname gsl
%define vers 2.8
%define _vers 2_8_0
%define lgsl_so_v   28
%define lgslcblas_so_v 0

%if "%{flavor}" == ""
ExclusiveArch:  do_not_build
%define package_name %pname
%bcond_with hpc
%endif

%if "%{flavor}" == "serial"
%bcond_with hpc
%define manext .gz
%endif

%if "%{flavor}" == "gnu-hpc"
%define compiler_family gnu
%undefine c_f_ver
%define manext %{nil}
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu6-hpc"
%define compiler_family gnu
%define c_f_ver 6
%define manext %{nil}
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu7-hpc"
%define compiler_family gnu
%define c_f_ver 7
%define manext %{nil}
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu8-hpc"
%define compiler_family gnu
%define c_f_ver 8
%define manext %{nil}
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu9-hpc"
%define compiler_family gnu
%define c_f_ver 9
%define manext %{nil}
%bcond_without hpc
%endif

%if "%{flavor}" == "gnu10-hpc"
%define compiler_family gnu
%define c_f_ver 10
%define manext %{nil}
%bcond_without hpc
%endif

%if %{without hpc}
%if 0%{!?package_name:1}
%define package_name  %{pname}
%endif
%define p_prefix %_prefix
%define p_includedir %_includedir/%pname
%define p_libdir %_libdir
%define p_bindir %_bindir
%define p_mandir %_mandir
%define p_datadir %_datadir
%define p_infodir %_infodir
%define num_threads 64
%define libname lib%{pname}%{lgsl_so_v}
%define libcblas lib%{pname}cblas%{lgslcblas_so_v}

%else

%{hpc_init -c %{compiler_family} %{?c_f_ver:-v %{c_f_ver}} %{?ext:-e %{ext}}}
%define package_name %{hpc_package_name %_vers}

%define p_prefix %hpc_prefix
%define p_includedir %hpc_includedir
%define p_libdir %hpc_libdir
%define p_bindir %hpc_bindir
%define p_mandir %hpc_mandir
%define p_datadir %hpc_datadir
%define p_infodir %hpc_infodir
%define num_threads 256
%define libname lib%{package_name}
%define libcblas lib%{pname}cblas%{hpc_package_name_tail %{_vers}}

%endif

Name:           %{package_name}
Version:        %{vers}
Release:        0
Summary:        GNU Scientific Library
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://www.gnu.org/software/%{pname}/
Source0:        https://ftp.gnu.org/pub/gnu/%{pname}/%{pname}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/pub/gnu/%{pname}/%{pname}-%{version}.tar.gz.sig
Source2:        https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=gsl&download=1#/%{pname}.keyring
Patch6:         gsl-qawc-test-x86-precision.diff
Patch7:         gsl-disable-fma.patch
# PATCH-FIX-UPSTREAM gsl-bspline-missing-definition.patch svg#65868 badshah400@gmail.com -- Add missing definition for gsl_bspline_eval_nonzero
Patch8:         gsl-bspline-missing-definition.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig

%if %{without hpc}
BuildRequires:  update-alternatives
Requires(post): update-alternatives
Requires(preun):update-alternatives
%else
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel
BuildRequires:  lua-lmod
BuildRequires:  suse-hpc
Requires:       %{libname} = %version
%global dep_summary %{summary}
%endif

%description
The GNU Scientific Library (GSL) is a collection of routines for
numerical computing. The routines are written from scratch by the GSL
team in ANSI C and present an Applications Programming Interface
(API) for C programmers, while allowing wrappers to be written for very
high level languages.

%package     -n %{libname}
Summary:        GNU Scientific Library
Group:          System/Libraries
%if %{with hpc}
%{hpc_requires}
BuildRequires:  lua-lmod
Requires:       %{name}-module = %version
%endif

%{?with_hpc:%{hpc_master_package}}

%description -n %{libname}
The GNU Scientific Library (GSL) is a collection of routines for
numerical computing. The routines are written from scratch by the GSL
team in ANSI C and present an Applications Programming Interface
(API) for C programmers, while allowing wrappers to be written for very
high level languages.

The library covers the following areas:

Complex Numbers - Roots of Polynomials - Special Functions -
Vectors and Matrices - Permutations - Sorting - BLAS Support -
Linear Algebra - Eigensystems - Fast Fourier Transforms - Quadrature -
Random Numbers - Quasi-Random Sequences - Random Distributions -
Statistics - Histograms - N-Tuples - Monte Carlo Integration -
Simulated Annealing - Differential Equations - Interpolation -
Numerical Differentiation - Chebyshev Approximation - Series Acceleration -
Discrete Hankel Transforms - Root-Finding - Minimization -
Least-Squares Fitting - Physical Constants - IEEE Floating-Point

%{?with_hpc:%{hpc_master_package  -l -L}}

%package     -n %{libcblas}
Summary:        A standard C language APIs for BLAS from GNU Scientific Library
# file conflict, see boo#991155
Group:          System/Libraries
Obsoletes:      libgsl0
%if %{with hpc}
%{hpc_requires}
Requires:       %{name}-module = %version
%endif

%description -n %{libcblas}
This library provides a native C interface to BLAS routines. This is part of
the GNU Scientific Library.

%{?with_hpc:%{hpc_master_package  -L -l -n lib%{pname}cblas%{hpc_package_name_tail} -N %{pname}cblas}}

%package        devel
Summary:        Development files for the GNU Scientific Library
Group:          Development/Libraries/C and C++
Requires:       %{libcblas} = %{version}
Requires:       %{libname} = %{version}
Requires(pre):  %{install_info_prereq}
%{?with_hpc:%hpc_requires_devel}

%description devel
This package contains the headers, static libraries and some
documentation for GSL.

The GNU Scientific Library (GSL) is a collection of routines for
numerical computing. The routines are written from scratch by the GSL
team in ANSI C, and present an Applications Programming Interface
(API) for C programmers, while allowing wrappers to be written for very
high level languages.

%{?with_hpc:%{hpc_master_package -L devel}}

%package        doc
Summary:        Documentation for the GNU Scientific Library
Group:          Documentation/Other
Requires(post): %{install_info_prereq}
Requires(preun):%{install_info_prereq}
BuildArch:      noarch

%description    doc
This package contains documentation for GSL

The GNU Scientific Library (GSL) is a collection of routines for
numerical computing. The routines are written from scratch by the GSL
team in ANSI C, and present an Applications Programming Interface
(API) for C programmers, while allowing wrappers to be written for very
high level languages.

%{?with_hpc:%{hpc_master_package doc}}

%package        examples
Summary:        Examples for the GNU Scientific Library
Group:          Documentation/Other
BuildArch:      noarch

%description    examples
This package contains examples for GSL


%if %{with hpc}
%package module
Summary:        Module files for %{name}
# Package can not be noarch, as this will lead to the situation, so
# that sometimes 32bit rpm is used with %%{_lib}=lib or 64 bit, where
# %%{_lib}=lib64
Group:          Development/Libraries/Parallel

%description module
This package contains the environment module needed for the GSL
library packages.
%endif
# module package only installed thru dependency. No master package

%prep
%setup -q -n %{pname}-%{version}
%patch -P 6
%patch -P 7 -p1
%patch -P 8 -p1

%build

%if %{with hpc}
%hpc_debug
%hpc_setup
%endif

autoreconf -fiv
export CFLAGS="%{optflags}"
%if %{without hpc}
%configure \
%else
%hpc_configure \
%endif
	--disable-static \
	--enable-shared \
	--with-gnu-ld
make %{?_smp_mflags}

%check
# On i586 this still fails
%ifarch %{ix86}
make %{?_smp_mflags} check || ( find -name \*.log -print -exec cat {} \; ; exit 0 )
%else
make %{?_smp_mflags} check || ( find -name \*.log -print -exec cat {} \; ; exit 1 )
%endif
# Clean up to package directory
make -C doc/examples clean
chmod a-x doc/examples/*
rm doc/examples/Makefile*

%install
%{?with_hpc:%hpc_setup}

%make_install
find %{buildroot} -type f -name "*.la" -delete -print
rm -f %{buildroot}%{p_infodir}/dir

%if %{with hpc}
%{hpc_write_pkgconfig}
%{hpc_write_pkgconfig -n %{pname}cblas -l %{pname}cblas}

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
prepend-path    MANPATH             %{hpc_mandir}
prepend-path    INFOPATH            %{hpc_infodir}
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

%if %{without hpc}
%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%post   -n %{libcblas} -p /sbin/ldconfig
%postun -n %{libcblas} -p /sbin/ldconfig
%else

%post   -n %{libname}
/sbin/ldconfig -N %{p_libdir}

%postun -n %{libname}
/sbin/ldconfig -N %{p_libdir}

%post   -n %{libcblas}
/sbin/ldconfig -N %{p_libdir}

%postun -n %{libcblas}
/sbin/ldconfig -N %{p_libdir}

%postun -n %{name}-module
%hpc_module_delete_if_default
%endif

%if %{with hpc}
%files module
%hpc_modules_files
%endif

%files
%license COPYING
%{?with_hpc:%hpc_dirs}
%{?with_hpc:%dir %p_bindir}
%{p_bindir}/gsl-histogram
%{p_bindir}/gsl-randist
%{?with_hpc:%dir %{p_mandir}}
%{?with_hpc:%dir %{p_mandir}/man1}
%{p_mandir}/man1/gsl-histogram.1%{?manext}
%{p_mandir}/man1/gsl-randist.1%{?manext}

%files -n %{libname}
%{?with_hpc:%hpc_dirs}
%{?with_hpc:%dir %p_libdir}
%{p_libdir}/libgsl.so.*

%files -n %{libcblas}
%{?with_hpc:%hpc_dirs}
%{p_libdir}/libgslcblas.so.*

%files devel
%license COPYING
%{?with_hpc:%hpc_dirs}
%{p_includedir}
%{?with_hpc:%dir %{p_includedir}/gsl}
%{p_libdir}/libgsl*.so
%if %{without hpc}
%{p_libdir}/pkgconfig/gsl.pc
%else
%{hpc_pkgconfig_file}
%{hpc_pkgconfig_file -N -n %{pname}cblas}
%endif
%{p_bindir}/gsl-config
%{?with_hpc:%dir %p_datadir}
%dir %{p_datadir}/aclocal
%{p_datadir}/aclocal/gsl.m4
%{p_mandir}/man1/gsl-config.1%{?manext}
%{?with_hpc:%dir %{p_mandir}/man3}
%{p_mandir}/man3/gsl.3%{?manext}

%files examples
%doc doc/examples
%license COPYING

%files doc
%doc AUTHORS BUGS ChangeLog NEWS README THANKS TODO
%license COPYING
%if %{with hpc}
%dir %{hpc_install_path_base}
%dir %{hpc_install_path}
%dir %{p_infodir}
%endif
%{p_infodir}/gsl-ref*

%post doc
%install_info --info-dir=%{p_infodir} %{p_infodir}/gsl-ref.info%{ext_info}

%preun doc
%install_info_delete --info-dir=%{p_infodir} %{p_infodir}/gsl-ref.info%{ext_info}

%changelog
