#
# spec file for package python-zict
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
Name:           python-zict
Version:        1.0.0
Release:        0
Summary:        Mutable mapping tools
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/dask/zict/
Source:         https://files.pythonhosted.org/packages/source/z/zict/zict-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-HeapDict
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module HeapDict}
BuildRequires:  %{python_module lmdb}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Mutable Mapping interfaces for python.

%prep
%setup -q -n zict-%{version}
# needs more memory than what we have on generic hosts
rm zict/tests/test_lmdb.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/*

%changelog
