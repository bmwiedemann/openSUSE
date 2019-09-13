#
# spec file for package python-mpmath
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
Name:           python-mpmath
Version:        1.1.0
Release:        0
Summary:        Python library for arbitrary-precision floating-point arithmetic
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            https://github.com/fredrik-johansson/mpmath
Source:         https://files.pythonhosted.org/packages/source/m/mpmath/mpmath-%{version}.tar.gz
BuildRequires:  %{python_module gmpy >= 1.03}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-gmpy >= 1.03
Requires:       python-six
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONDONTWRITEBYTECODE=1
%python_expand PYTHONPATH="%{buildroot}%{$python_sitelib}" py.test-%{python_bin_suffix} -v --pyargs mpmath

%files %{python_files}
%license LICENSE
%doc CHANGES
%dir %{python_sitelib}/mpmath
%{python_sitelib}/mpmath
%{python_sitelib}/mpmath-%{version}-py*.egg-info

%changelog
