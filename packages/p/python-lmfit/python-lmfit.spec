#
# spec file for package python-lmfit
#
# Copyright (c) 2023 SUSE LLC
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
Version:        1.1.0
Release:        0
Summary:        Least-Squares Minimization with Bounds and Constraints
License:        BSD-3-Clause AND MIT
URL:            https://lmfit.github.io/lmfit-py/
Source:         https://files.pythonhosted.org/packages/source/l/lmfit/lmfit-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-asteval >= 0.9.28
Requires:       python-numpy >= 1.19
Requires:       python-scipy >= 1.6
Requires:       python-uncertainties >= 3.1.4
Recommends:     python-dill
Recommends:     python-emcee
Recommends:     python-matplotlib
Recommends:     python-pandas
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module asteval >= 0.9.28}
BuildRequires:  %{python_module numpy >= 1.19}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy >= 1.6}
BuildRequires:  %{python_module uncertainties >= 3.1.4}
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
%setup -q -n lmfit-%{version}
sed -i -e '/^#!\//, 1d' lmfit/jsonutils.py
# only coverage related pytest flags here. remove
sed -i '/addopts/d' setup.cfg

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
fi
%pytest -k "not ($donttest)"

%files %{python_files}
%doc README.rst AUTHORS.txt
%license LICENSE
%{python_sitelib}/lmfit
%{python_sitelib}/lmfit-%{version}*-info

%changelog
