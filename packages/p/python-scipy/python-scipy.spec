#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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
%define _ver 1_9_3
%define shortname scipy
%define pname python-%{shortname}
%define hpc_upcase_trans_hyph() %(echo %{**} | tr [a-z] [A-Z] | tr '-' '_')

%if "%{flavor}" == ""
 %bcond_with hpc
 %ifarch armv6l s390 s390x m68k
  %bcond_with openblas
 %else
    %if 0%{?sle_version} == 120200
      %ifarch i586
        %bcond_with openblas
      %else
        %bcond_without openblas
      %endif
    %else
      %bcond_without openblas
    %endif
  %endif
%endif

%if "%{flavor}" == "test"
%bcond_with hpc
%bcond_without test
%else
%bcond_with test
%endif

%if "%{flavor}" == "gnu-hpc"
 %define compiler_family gnu
 %bcond_without hpc
 %undefine c_f_ver
%endif
%if "%{flavor}" == "gnu7-hpc"
 %define compiler_family gnu
 %define c_f_ver 7
 %bcond_without hpc
%endif

%{?with_hpc:%{hpc_requires}}
%bcond_with ringdisabled
%if %{without hpc}
%define package_name %{pname}
# for file section
%define p_python_sitearch %{python_sitearch}
# for inside python_expand
%define p_python_sitearch_expand %{$python_sitearch}
%define p_prefix %{_prefix}
%define p_bindir %{_bindir}
%else
%{!?compiler_family:%global compiler_family gnu}
%{hpc_init -c %{compiler_family} %{?c_f_ver:-v %{c_f_ver}} %{?ext:-e %{ext}}}
%define package_name %{hpc_package_name %{_ver}}
# for file section
%define p_python_sitearch %{hpc_python_sitearch}
# for inside python_expand
%define p_python_sitearch_expand $($python -c "import sysconfig as s; print(s.get_paths(vars={'platbase':'%{hpc_prefix}','base':'%{hpc_prefix}'}).get('platlib'))")
%define p_prefix %{hpc_prefix}
%define p_bindir %{hpc_bindir}
# Magic for OBS Staging. Only build the flavors required by
# other packages in the ring.
%if %{with ringdisabled}
ExclusiveArch:  do_not_build
%endif
 %ifarch armv6l s390 s390x m68k i586
ExclusiveArch:  do_not_build
 %endif
%{hpc_modules_init openblas}
%endif

# TODO explore debundling Boost for standard and hpc

Name:           %{package_name}
Version:        1.9.3
Release:        0
Summary:        Scientific Tools for Python
License:        BSD-3-Clause AND LGPL-2.0-or-later AND BSL-1.0
Group:          Development/Libraries/Python
URL:            https://www.scipy.org
Source0:        https://files.pythonhosted.org/packages/source/s/scipy/scipy-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#scipy/scipy#16926#issuecomment-1287507634
Patch1:         fix-tests.patch
BuildRequires:  %{python_module Cython >= 0.29.32}
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module meson-python >= 0.9.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pybind11 >= 2.4.3}
BuildRequires:  %{python_module pybind11-devel >= 2.4.3}
BuildRequires:  %{python_module pythran >= 0.9.12}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  meson >= 0.62.2
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros >= 20220911
%if %{with test}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy = %{version}}
BuildRequires:  %{python_module threadpoolctl}
%endif
%if %{without hpc}
BuildRequires:  %{python_module numpy-devel >= 1.18.5}
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
Requires:       python-numpy >= 1.18.5
Requires:       python-pybind11 >= 2.4.3
 %if %{with openblas}
BuildRequires:  openblas-devel
 %else
BuildRequires:  blas-devel
BuildRequires:  lapack-devel
 %endif
%else
BuildRequires:  %{compiler_family}%{?c_f_ver}-compilers-hpc-macros-devel >= 1.3
BuildRequires:  %{python_module numpy%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc-devel}
BuildRequires:  libopenblas%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc-devel
BuildRequires:  lua-lmod
BuildRequires:  suse-hpc >= 0.3
Requires:       libopenblas%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc
Requires:       python-numpy%{?hpc_ext}-%{compiler_family}%{?c_f_ver}-hpc >= 1.18.5
%endif
%python_subpackages

%description
Scipy is open-source software for mathematics, science, and
engineering. The core library is NumPy which provides convenient and
fast N-dimensional array manipulation. The SciPy library is built to
work with NumPy arrays, and provides many numerical routines such as
for numerical integration and optimization.

%{?with_hpc:%{hpc_python_master_package -L -a }}

%prep
%autosetup -p1 -n scipy-%{version}
sed -i '1{/env python/d}' scipy/sparse/linalg/_isolve/tests/test_gcrotmk.py

%ifarch i586
# Limit double floating point precision for x87, triggered by GCC 12.
%global optflags %(echo "%{optflags} -ffloat-store")
%endif

%if !%{with openblas}
# Edit the options file until we have a way to provide options to meson-python from command line or environment
# https://github.com/FFY00/meson-python/pull/122
sed -i "s/option('blas', type: 'string', value: 'openblas'/option('blas', type: 'string', value: 'blas'/" meson_options.txt
sed -i "s/option('lapack', type: 'string', value: 'openblas'/option('lapack', type: 'string', value: 'lapack'/" meson_options.txt
%endif

%if !%{with test}
%build
# makes sure that the cython and pythran commands from the correct flavor are in PATH
%python_flavored_alternatives
%{python_expand #
%if %{with hpc}
py_ver=%{$python_version}
%hpc_setup
module load $python-numpy
%endif
export CFLAGS="%{optflags} -fno-strict-aliasing"
%{$python_pyproject_wheel}
}

%install
%{python_expand #
%if %{with hpc}
%hpc_setup
module load $python-numpy
%endif
%{$python_pyproject_install --prefix %{p_prefix}}
# https://github.com/scipy/scipy/issues/16310, delete in order to avoid rpmlint errors
rm %{buildroot}%{p_python_sitearch_expand}/scipy/linalg/_blas_subroutines.h
rm %{buildroot}%{p_python_sitearch_expand}/scipy/linalg/_lapack_subroutines.h
rm %{buildroot}%{p_python_sitearch_expand}/scipy/special/_ufuncs_cxx_defs.h
rm %{buildroot}%{p_python_sitearch_expand}/scipy/special/_ufuncs_defs.h
%fdupes %{buildroot}%{p_python_sitearch_expand}
}

%if %{with hpc}
%define hpc_module_pname ${python_flavor}-%{shortname}
%{python_expand #
rm -rf %{buildroot}%{p_python_sitearch_expand}/scipy/{,core,distutils,f2py,fft,lib,linalg,ma,matrixlib,oldnumeric,polynomial,random,testing}/tests
%hpc_write_modules_files
#%%Module1.0#####################################################################

proc ModulesHelp { } {

puts stderr " "
puts stderr "This module loads the %{pname} library built with the %{compiler_family} compiler "
puts stderr "toolchain."
puts stderr "\nVersion %{version}\n"

}
module-whatis "Name: %{pname} built with %{compiler_family} toolchain."
module-whatis "Version: %{version}"
module-whatis "Category: python module"
module-whatis "Description: %{SUMMARY}"
module-whatis "URL %{url}"

set     version             %{version}

depends-on $python-numpy

prepend-path    PYTHONPATH          ${sitesearch_path}

setenv          %{hpc_upcase_trans_hyph %{pname}}_DIR        %{hpc_prefix}
setenv          %{hpc_upcase_trans_hyph %{pname}}_BIN        %{hpc_bindir}

family %{shortname}
EOF
}
%endif
%endif

%if %{with test}
%check
# (occasional) precision errors
donttest="(TestLinprogIPSpecific and test_solver_select)"
donttest+=" or test_gh12922"
donttest+=" or (TestPeriodogram and test_nd_axis_m1)"
donttest+=" or (TestPeriodogram and test_nd_axis_0)"
donttest+=" or (TestPdist and test_pdist_jensenshannon_iris)"
donttest+=" or (test_rotation and test_align_vectors_single_vector)"
donttest+=" or (test_lobpcg and test_tolerance_float32)"
donttest+=" or (test_iterative and test_maxiter_worsening)"
# fails on big endian
donttest+=" or (TestNoData and test_nodata)"
# oom
donttest+=" or (TestBSR and test_scalar_idx_dtype)"
# error while getting entropy
donttest+=" or (test_cont_basic and 500-200-ncf-arg74)"
# https://github.com/scipy/scipy/issues/16927
donttest+=" or (test_lobpcg and test_failure_to_run_iterations)"
%ifarch %ix86 %arm
# fails on 32bit
mark32bit="or xfail_on_32bit"
# precision errors
donttest+=" or (test_peak_finding and TestFindPeaksCwt and test_find_peaks_exact)"
donttest+=" or (test_peak_finding and TestFindPeaksCwt and test_find_peaks_withnoise)"
donttest+=" or (test_iterative and test_x0_equals_Mb and bicgstab)"
donttest+=" or (test_orthogonal and test_roots_gegenbauer)"
donttest+=" or (test_discrete_basic and test_rv_sample)"
donttest+=" or (test_distributions and TestLevyStable and nolan_samples and pct_range0-alpha_range0-beta_range0)"
donttest+=" or (test_distributions and TestLevyStable and test_location_scale and pdf)"
donttest+=" or (test_data and test_boost and (betainc or btdtr))"
%endif
%ifarch %arm
donttest+=" or (test_cython_api and eval_sh_chebyt)"
donttest+=" or (test_stats_boost_ufunc)"
%endif
mv scipy scipy.dont-import-me
%pytest_arch --pyargs scipy -n auto -m "not (slow or xslow $mark32bit)" -k "not ($donttest)"
# prevent failing debuginfo extraction because we did not create anything for testing
touch debugsourcefiles.list
%endif

%if !%{with test}
%if %{with hpc}
%post
%{hpc_module_delete_if_default}
%endif

%files %{python_files}
%license LICENSE.txt
%{p_python_sitearch}/scipy/
%{p_python_sitearch}/scipy-%{version}*-info

%if %{with hpc}
%define hpc_module_pname %{python_flavor}-scipy
%{hpc_modules_files}
%{hpc_dirs}
%dir %{hpc_libdir}/python%{hpc_python_version}
%dir %{p_python_sitearch}
%endif
%endif

%changelog
