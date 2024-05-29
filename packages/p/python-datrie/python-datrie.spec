#
# spec file for package python-datrie
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


Name:           python-datrie
Version:        0.8.2
Release:        0
Summary:        Trie data structure for Python
License:        LGPL-2.1-or-later
URL:            https://github.com/kmike/datrie
Source:         https://files.pythonhosted.org/packages/source/d/datrie/datrie-%{version}.tar.gz
Patch0:         datrie-bigendian.patch
# PATCH-FIX-UPSTREAM - Fix AlphaMap definition in cdatrie.pxd
Patch1:         https://github.com/pytries/datrie/pull/99.patch
BuildRequires:  %{python_module Cython >= 0.26.1}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
A trie data structure for Python (2.x and 3.x). Uses libdatrie.

%prep
%autosetup -p1 -n datrie-%{version}
# https://github.com/pytries/datrie/pull/89
sed -i 's:pytest-runner::' setup.py

%build
pushd src
cython datrie.pyx
cython *.pxd
popd
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%license COPYING
%doc README.rst CHANGES.rst
%{python_sitearch}/datrie.cpython-*linux*.so
%{python_sitearch}/datrie-%{version}.dist-info

%changelog
