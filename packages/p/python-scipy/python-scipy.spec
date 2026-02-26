#
# spec file for package python-scipy
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%{?sle15_python_module_pythons}
%global flavor @BUILD_FLAVOR@%{nil}

%if "%{flavor}" == ""
 %ifarch armv6l s390 m68k
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
%bcond_without test
%define psuffix -test
%else
%define psuffix %{nil}
%bcond_with test
%endif

# TODO explore debundling Boost for standard

Name:           python-scipy%{?psuffix}
Version:        1.17.1
Release:        0
Summary:        Scientific Tools for Python
License:        BSD-3-Clause AND LGPL-2.0-or-later AND BSL-1.0
URL:            https://www.scipy.org
Source0:        https://files.pythonhosted.org/packages/source/s/scipy/scipy-%{version}.tar.gz
# Create with pooch: `python3 scipy-%%{version}/scipy/datasets/_download_all.py scipy-datasets/scipy-data; tar czf scipy-datasets.tar.gz scipy-datasets`
Source1:        scipy-datasets.tar.gz
BuildRequires:  %{python_module Cython >= 3.0.8}
BuildRequires:  %{python_module devel >= 3.11}
BuildRequires:  %{python_module meson-python >= 0.15.0 with %python-meson-python < 0.21}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pybind11-devel >= 2.13.2 with %python-pybind11-devel < 3.1.0}
# Upstream's pre-emptive pin to < 0.18 is not necessary
BuildRequires:  %{python_module pythran >= 0.14}
BuildRequires:  fdupes
BuildRequires:  meson >= 0.62.2
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros >= 20220911
%if %{with test}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module pooch}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy = %{version}}
BuildRequires:  %{python_module threadpoolctl}
%endif
BuildRequires:  %{python_module numpy-devel >= 1.25.2 with %python-numpy-devel < 2.6}
%if 0%{?sle_version} && 0%{?sle_version} <= 150600
# The default gcc on SLE15 is gcc7 we need something newer
BuildRequires:  gcc10-c++
BuildRequires:  gcc10-fortran
%else
BuildRequires:  gcc-c++ >= 8
BuildRequires:  gcc-fortran >= 8
%endif
Requires:       (python-numpy >= 1.25.2 with python-numpy < 2.6)
Suggests:       python-pooch
 %if %{with openblas}
BuildRequires:  openblas-devel
 %else
BuildRequires:  blas-devel
BuildRequires:  lapack-devel
 %endif
%python_subpackages

%description
Scipy is open-source software for mathematics, science, and
engineering. The core library is NumPy which provides convenient and
fast N-dimensional array manipulation. The SciPy library is built to
work with NumPy arrays, and provides many numerical routines such as
for numerical integration and optimization.

%prep
%autosetup -p1 -n scipy-%{version} -a1
sed -i '1{/env python/d}' scipy/sparse/linalg/_isolve/tests/test_gcrotmk.py
chmod a-x scipy/stats/tests/test_distributions.py

%ifarch i586
# Limit double floating point precision for x87, triggered by GCC 12.
%global optflags %(echo "%{optflags} -ffloat-store")
%endif

%if !%{with openblas}
# Edit the options file until we have a way to provide options to meson-python from command line or environment
# https://github.com/mesonbuild/meson-python/issues/230 https://github.com/mesonbuild/meson-python/issues/235
sed -i "s/option('blas', type: 'string', value: 'openblas'/option('blas', type: 'string', value: 'blas'/" meson.options
sed -i "s/option('lapack', type: 'string', value: 'openblas'/option('lapack', type: 'string', value: 'lapack'/" meson.options
%endif

%if !%{with test}
%build
%if 0%{?sle_version} && 0%{?sle_version} <= 150600
# We need gcc >= 8 for SLE15
export CC=gcc-10
export CXX=g++-10
export FC=gfortran-10
%endif
# makes sure that the cython and pythran commands from the correct flavor are in PATH
%python_flavored_alternatives
origpath="$PATH"
%{python_expand #
export CFLAGS="%{optflags} -fno-strict-aliasing"
%{$python_pyproject_wheel}
}

%install
%{python_expand #
%{$python_pyproject_install}
# https://github.com/scipy/scipy/issues/16310, delete in order to avoid rpmlint errors
rm %{buildroot}%{$python_sitearch}/scipy/linalg/_blas_subroutines.h
rm %{buildroot}%{$python_sitearch}/scipy/linalg/_lapack_subroutines.h
find %{buildroot}%{$python_sitearch}/scipy/special -name '*.h' -delete
%fdupes %{buildroot}%{$python_sitearch}
}

%endif

%if %{with test}
%check
# pooch cache (extracted SOURCE1)
export XDG_CACHE_HOME=$PWD/scipy-datasets
# (occasional) precision errors
donttest="(TestLinprogIPSpecific and test_solver_select)"
donttest+=" or test_gh12922"
donttest+=" or (TestPeriodogram and test_nd_axis_m1)"
donttest+=" or (TestPeriodogram and test_nd_axis_0)"
donttest+=" or (TestPdist and test_pdist_jensenshannon_iris)"
donttest+=" or (test_rotation and test_align_vectors_single_vector)"
donttest+=" or (test_lobpcg and test_tolerance_float32)"
donttest+=" or (test_iterative and test_maxiter_worsening)"
donttest+=" or (test_resampling and test_bootstrap_alternative)"
%ifarch %ix86
donttest+=" or (test_solvers and test_solve_generalized_discrete_are)"
# Skip the following tests that fail with GCC 13 due to the excess precision change:
# https://gcc.gnu.org/gcc-13/porting_to.html#excess-precision
donttest+=" or (test_fitpack or test_fitpack2 or test_splint or test_integrate or test_boost)"
%endif
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
donttest+=" or (test_mstats_basic and test_skewtest_2D_WithMask)"
%endif
%ifarch %ix86
# illegal instruction (?)
donttest+=" or (test_fftlog and test_fht_identity)"
%endif
%ifarch %arm
donttest+=" or (test_cython_api and eval_sh_chebyt)"
donttest+=" or (test_stats_boost_ufunc)"
%endif

%ifarch s390x
# gh#scipy/scipy#18878
donttest+=" or (test_distance_transform_cdt05)"
donttest+=" or (test_svd_maxiter)"
%endif

# not enough precison on 32 bits
if [ $(getconf LONG_BIT) -eq 32 ]; then
    donttest+=" or (TestCheby1 and test_basic)"
    donttest+=" or test_extreme_entropy"
fi
mv scipy scipy.dont-import-me
%pytest_arch --pyargs scipy %{?jobs:-n %jobs} -m "not (slow or xslow $mark32bit)" -k "not ($donttest)"
# prevent failing debuginfo extraction because we did not create anything for testing
touch debugsourcefiles.list
%endif

%if !%{with test}

%files %{python_files}
%license LICENSE.txt
%{python_sitearch}/scipy/
%{python_sitearch}/scipy-%{version}*-info

%endif

%changelog
