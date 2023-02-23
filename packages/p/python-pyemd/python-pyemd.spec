#
# spec file for package python-pyemd
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


%define         skip_python36 1
# pytest is too smart for its own good, prevent use of compiled version
%bcond_with     test
Name:           python-pyemd
Version:        0.5.1
Release:        0
Summary:        Python implementation of the Earth Mover's Distance
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/wmayner/pyemd
Source:         https://files.pythonhosted.org/packages/source/p/pyemd/pyemd-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/wmayner/pyemd/commit/34631658ae0cc555001b692623c23c02ed8d5611 Mark uses of ragged nested sequences in NumPy arrays as intented
Patch0:         numpy-arrays.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel >= 1.9.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.9.0
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
PyEMD is a Python wrapper for Ofir Pele and Michael Werman's implementation
of the Earth Mover's Distance that allows it to be used with NumPy.

%prep
%autosetup -p1 -n pyemd-%{version}

sed -i -e '/^#!\//, 1d' pyemd/__about__.py pyemd/__init__.py

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
mv conftest.py conftest_bad.py_bad
pushd test
%pytest_arch
popd
mv conftest_bad.py_bad conftest.py

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/pyemd
%{python_sitearch}/pyemd-%{version}*-info

%changelog
