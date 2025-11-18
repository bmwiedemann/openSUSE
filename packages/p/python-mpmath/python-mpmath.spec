#
# spec file for package python-mpmath
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


%{?sle15_python_module_pythons}
Name:           python-mpmath
Version:        1.3.0
Release:        0
Summary:        Python library for arbitrary-precision floating-point arithmetic
License:        BSD-3-Clause
URL:            https://github.com/fredrik-johansson/mpmath
Source:         https://files.pythonhosted.org/packages/source/m/mpmath/mpmath-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module gmpy2 >= 2.1.0a4}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python >= 3.8
Requires:       python-gmpy2 >= 2.1.0a4
BuildArch:      noarch
%python_subpackages

%description
Mpmath is a pure-Python library for multiprecision floating-point
arithmetic. It provides a set of transcendental functions,
unlimited exponent sizes, complex numbers, interval arithmetic,
numerical integration and differentiation, root-finding, linear
algebra, and others. Almost any calculation can be performed just
as well at 10-digit or 1000-digit precision, and in many cases, mpmath
implements algorithms that scale well for high precision work.
If available, mpmath will (optionally) use gmpy to speed up high
precision operations.

%prep
%setup -q -n mpmath-%{version}
sed -i 's/\r//' mpmath/tests/runtests.py  # fix wrong-script-end-of-line-encoding rpmlint warning
sed -i '1d' mpmath/tests/runtests.py  # fix non-executable-script rpmlint warning

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# "Broken" by https://github.com/python/cpython/issues/121149 in 3.14
%pytest -v --pyargs mpmath -k 'not mpmath.functions.orthogonal.spherharm'

%files %{python_files}
%license LICENSE
%doc README.rst
%dir %{python_sitelib}/mpmath
%{python_sitelib}/mpmath
%{python_sitelib}/mpmath-%{version}.dist-info

%changelog
