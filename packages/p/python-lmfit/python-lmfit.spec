#
# spec file for package python-lmfit
#
# Copyright (c) 2020 SUSE LLC.
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
%define         skip_python2 1
Name:           python-lmfit
Version:        1.0.1
Release:        0
Summary:        Least-Squares Minimization with Bounds and Constraints
License:        MIT AND BSD-3-Clause
URL:            https://lmfit.github.io/lmfit-py/
Source:         https://files.pythonhosted.org/packages/source/l/lmfit/lmfit-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-asteval >= 0.9.16
Requires:       python-numpy >= 1.16
Requires:       python-scipy >= 1.2
Recommends:     python-dill
Recommends:     python-emcee
Recommends:     python-matplotlib
Recommends:     python-pandas
Recommends:     python-uncertainties >= 3.0.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module asteval >= 0.9.16}
BuildRequires:  %{python_module numpy >= 1.16}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy >= 1.2}
BuildRequires:  %{python_module uncertainties >= 3.0.1}
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

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
python3 -c "import sys, lmfit, numpy, scipy, asteval, uncertainties, six;print('Python: {}\n\nlmfit: {}, scipy: {}, numpy: {}, asteval: {}, uncertainties: {}, six: {}'.format(sys.version, lmfit.__version__, scipy.__version__, numpy.__version__, asteval.__version__, uncertainties.__version__, six.__version__))"

cat << 'EOF' >> testexample.py
import numpy as np

import lmfit
from lmfit.lineshapes import gaussian
from lmfit.models import PseudoVoigtModel

x = np.linspace(0, 10, 201)
np.random.seed(0)
y = gaussian(x, 10.0, 6.15, 0.8)
y += gaussian(x, 8.0, 6.35, 1.1)
y += gaussian(x, 0.25, 6.00, 7.5)
y += np.random.normal(size=len(x), scale=0.5)

# with NaN values in the input data
y[55] = y[91] = np.nan
mod = PseudoVoigtModel()
params = mod.make_params(amplitude=20, center=5.5,
                         sigma=1, fraction=0.25)
params['fraction'].vary = False

# with propagate, should get no error, but bad results
result = mod.fit(y, params, x=x, nan_policy='propagate')
lmfit.report_fit(result)

print(result.__dict__)
EOF

cat testexample.py

python3 testexample.py


# We don't care about speed, and test_itercb is architecture-specific
# test_model_nan_policy - fails on non x86_64
# test_shgo_scipy_vs_lmfit_2 - fails on non x86_64
%pytest -k 'not speed and not (test_model_nan_policy or test_shgo_scipy_vs_lmfit_2)'

%files %{python_files}
%doc README.rst THANKS.txt
%license LICENSE
%{python_sitelib}/*

%changelog
