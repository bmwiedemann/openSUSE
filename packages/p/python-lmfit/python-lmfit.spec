#
# spec file for package python-lmfit
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           python-lmfit
Version:        1.3.4
Release:        0
Summary:        Least-Squares Minimization with Bounds and Constraints
License:        BSD-3-Clause AND MIT
URL:            https://lmfit.github.io/lmfit-py/
Source:         https://files.pythonhosted.org/packages/source/l/lmfit/lmfit-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-asteval >= 1
Requires:       python-dill >= 0.3.4
Requires:       python-numpy >= 1.19
Requires:       python-scipy >= 1.6
Requires:       python-uncertainties >= 3.2.2
Recommends:     python-emcee
Recommends:     python-matplotlib
Recommends:     python-pandas
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module asteval >= 1}
BuildRequires:  %{python_module dill >= 0.3.4}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module numpy >= 1.19}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy >= 1.6}
BuildRequires:  %{python_module uncertainties >= 3.2.2}
# /SECTION
%python_subpackages

%description
A library for least-squares minimization and data fitting in
Python.  Built on top of scipy.optimize, lmfit provides a Parameter object
which can be set as fixed or free, can have upper and/or lower bounds, or
can be written in terms of algebraic constraints of other Parameters.  The
user writes a function to be minimized as a function of these Parameters,
and the scipy.optimize methods are used to find the optimal values for the
Parameters.  The Levenberg-Marquardt (leastsq) is the default minimization
algorithm, and provides estimated standard errors and correlations between
varied Parameters.  Other minimization methods, including Nelder-Mead's
downhill simplex, Powell's method, BFGS, Sequential Least Squares, and
others are also supported.  Bounds and constraints can be placed on
Parameters for all of these methods.

In addition, methods for explicitly calculating confidence intervals are
provided for exploring minmization problems where the approximation of
estimating Parameter uncertainties from the covariance matrix is
questionable.

%prep
%autosetup -p1 -n lmfit-%{version}
sed -i -e '/^#!\//, 1d' lmfit/jsonutils.py
sed -i 's/--cov=lmfit --cov-report html//' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# We don't care about speed on obs
donttest="speed"
# these tests fail on non x86_64. Upstream does not care: https://github.com/lmfit/lmfit-py/issues/692
donttest+=" or test_model_nan_policy"
donttest+=" or test_shgo_scipy_vs_lmfit_2"
# fails on 32-bit
if [ $(getconf LONG_BIT) -ne 64 ]; then
  donttest+=" or (test_itercb_minimizer_class and leastsq and False)"
  donttest+=" or (test_aborted_solvers and brute)"
fi
%pytest -k "not ($donttest)"

%files %{python_files}
%doc README.rst AUTHORS.txt
%license LICENSE
%{python_sitelib}/lmfit
%{python_sitelib}/lmfit-%{version}.dist-info

%changelog
