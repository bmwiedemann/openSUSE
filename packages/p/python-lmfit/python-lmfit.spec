#
# spec file for package python-lmfit
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-lmfit
Version:        0.9.13
Release:        0
Summary:        Least-Squares Minimization with Bounds and Constraints
License:        MIT AND BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://lmfit.github.io/lmfit-py/
Source:         https://files.pythonhosted.org/packages/source/l/lmfit/lmfit-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module asteval >= 0.9.12}
BuildRequires:  %{python_module numpy >= 1.10}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy >= 0.19}
BuildRequires:  %{python_module six >= 1.10}
BuildRequires:  %{python_module uncertainties >= 3.0}
# /SECTION
Requires:       python-asteval >= 0.9.12
Requires:       python-numpy >= 1.10
Requires:       python-scipy >= 0.19
Requires:       python-six >= 1.10
Recommends:     python-dill
Recommends:     python-emcee
Recommends:     python-matplotlib
Recommends:     python-pandas
Recommends:     python-uncertainties >= 3.0
BuildArch:      noarch

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

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# We don't care about speed, and test_itercb is architecture-specific
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_bin_suffix} -v -k 'not speed and not test_itercb'

%files %{python_files}
%doc README.rst THANKS.txt
%license LICENSE
%{python_sitelib}/*

%changelog
