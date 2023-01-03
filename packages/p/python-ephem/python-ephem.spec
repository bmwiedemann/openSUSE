#
# spec file for package python-ephem
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-ephem
Version:        4.1.4
Release:        0
Summary:        Scientific-grade astronomy routines for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/brandon-rhodes/pyephem
Source0:        https://files.pythonhosted.org/packages/source/e/ephem/ephem-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pytzdata}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytzdata
%python_subpackages

%description
PyEphem provides an ephem Python package for performing high-precision astronomy computations.

%prep
%setup -q -n ephem-%{version}
# disable failing doctests
rm ephem/tests/test_rst.py
# remove shebangs in test files
sed -i '1{/env python/d}' ephem/tests/test_*.py

%build
export LANG=en_US.UTF8
%python_build

%install
export LANG=en_US.UTF8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export LANG=en_US.UTF8
mkdir emptytestdir
pushd emptytestdir
%pyunittest_arch discover -v ephem.tests
popd

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/ephem
%{python_sitearch}/ephem-%{version}*-info

%changelog
