#
# spec file for package python-lazyarray
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-lazyarray
Version:        0.6.0
Release:        0
Summary:        Lazily-evaluated numerical array class, compatible with NumPy arrays
License:        BSD-3-Clause
URL:            http://github.com/NeuralEnsemble/lazyarray/
Source:         https://files.pythonhosted.org/packages/source/l/lazyarray/lazyarray-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module numpy >= 1.20}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy >= 0.19}
# /SECTION
Requires:       python-numpy >= 1.20
Recommends:     python-scipy >= 0.19
BuildArch:      noarch

%python_subpackages

%description
lazyarray is a Python package that provides a lazily-evaluated numerical array
class, larray, based on and compatible with NumPy arrays.

Lazy evaluation means that any operations on the array (potentially including
array construction) are not performed immediately, but are delayed until
evaluation is specifically requested. Evaluation of only parts of the array is
also possible.

Use of an larray`can potentially save considerable computation time
and memory in cases where:

* arrays are used conditionally (i.e. there are cases in which the array is
  never used)
* only parts of an array are used (for example in distributed computation,
  in which each MPI node operates on a subset of the elements of the array)

%prep
%setup -q -n lazyarray-%{version}
%autopatch -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Skip test_create_with_sparse_array (gh#NeuralEnsemble/lazyarray#24)
%pytest -k 'not test_create_with_sparse_array'

%files %{python_files}
%doc README.rst changelog.txt
%license LICENSE
%{python_sitelib}/lazyarray.py*
%pycache_only %{python_sitelib}/__pycache__/lazyarray*.pyc
%{python_sitelib}/lazyarray-%{version}.dist-info

%changelog
