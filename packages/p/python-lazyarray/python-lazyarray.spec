#
# spec file for package python-lazyarray
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-lazyarray
Version:        0.3.3
Release:        0
Summary:        Lazily-evaluated numerical array class, compatible with NumPy arrays
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            http://github.com/NeuralEnsemble/lazyarray/
Source:         https://files.pythonhosted.org/packages/source/l/lazyarray/lazyarray-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module numpy >= 1.5}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
# /SECTION
Requires:       python-numpy >= 1.5
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

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst changelog.txt
%license LICENSE
%{python_sitelib}/*

%changelog
