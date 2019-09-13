#
# spec file for package python-datrie
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
Name:           python-datrie
Version:        0.8
Release:        0
Summary:        Trie data structure for Python
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
URL:            https://github.com/kmike/datrie
Source:         https://files.pythonhosted.org/packages/source/d/datrie/datrie-%{version}.tar.gz
Patch0:         datrie-bigendian.patch
BuildRequires:  %{python_module Cython >= 0.26.1}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
A trie data structure for Python (2.x and 3.x). Uses libdatrie.

%prep
%setup -q -n datrie-%{version}
%patch0 -p1

%build
pushd src
cython datrie.pyx
cython *.pxd
popd
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_exec setup.py test

%files %{python_files}
%license COPYING
%doc README.rst CHANGES.rst
%{python_sitearch}/*

%changelog
