#
# spec file for package python-cytoolz
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
Name:           python-cytoolz
Version:        1.1.0
Release:        0
Summary:        High performance python functional utilities in Cython
License:        BSD-3-Clause
URL:            https://github.com/pytoolz/cytoolz
Source:         https://files.pythonhosted.org/packages/source/c/cytoolz/cytoolz-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toolz}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-toolz
%python_subpackages

%description
Cython implementation of the toolz package, which provides high
performance utility functions for iterables, functions, and
dictionaries.

%prep
%setup -q -n cytoolz-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand find %{buildroot}%{$python_sitearch}/cytoolz -name "*.c" -exec rm {} \;
%python_expand rm -r %{buildroot}%{$python_sitearch}/cytoolz/tests
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# Move tests around so pytest can find them
mkdir -p testing
cp -rf cytoolz/tests/ testing/
pushd testing
%pytest_arch
popd

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitearch}/cytoolz/
%{python_sitearch}/cytoolz-*-info/

%changelog
