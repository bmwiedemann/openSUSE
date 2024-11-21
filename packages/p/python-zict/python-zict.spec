#
# spec file for package python-zict
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
Name:           python-zict
Version:        3.0.0
Release:        0
Summary:        Mutable mapping tools
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/dask/zict/
Source:         https://files.pythonhosted.org/packages/source/z/zict/zict-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
#BuildRequires:  %%{python_module lmdb}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Mutable Mapping interfaces for python.

%prep
%setup -q -n zict-%{version}
# needs more memory than what we have on generic hosts
rm zict/tests/test_lmdb.py
# ignore pytest-repeat marker: we don't stress test on OBS
sed -i '/markers =/ a \    repeat: Ignore me' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/zict
%{python_sitelib}/zict-%{version}.dist-info

%changelog
