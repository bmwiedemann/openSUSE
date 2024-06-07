#
# spec file for package python-sparse
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


%{?sle15_python_module_pythons}
Name:           python-sparse
Version:        0.15.4
Release:        0
Summary:        Sparse n-dimensional arrays for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pydata/sparse
Source:         https://files.pythonhosted.org/packages/source/s/sparse/sparse-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 64}
BuildRequires:  %{python_module setuptools_scm >= 8}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module dask-array}
BuildRequires:  %{python_module numba >= 0.49}
BuildRequires:  %{python_module numpy >= 1.17}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy >= 0.19}
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numba >= 0.49
Requires:       python-numpy >= 1.17
Requires:       python-scipy >= 0.19
BuildArch:      noarch

%python_subpackages

%description
This module implements sparse multidimensional arrays on top of NumPy and
Scipy.sparse. It generalizes the scipy.sparse.coo_matrix layout, but
extends beyond just rows and columns to an arbitrary number of
dimensions.

The original motivation is for machine learning algorithms, but it is
intended for somewhat general use.

%prep
%autosetup -p1 -n sparse-%{version}
sed -i /addopts/d pytest.ini

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# 32bit fails in half of the test suite because the tests try to convert to 64bit types
if [ $(getconf LONG_BIT) -eq 64 ]; then
%pytest
fi

%files %{python_files}
%doc README.rst docs/*.rst
%license LICENSE
%{python_sitelib}/sparse
%{python_sitelib}/sparse-%{version}*-info

%changelog
