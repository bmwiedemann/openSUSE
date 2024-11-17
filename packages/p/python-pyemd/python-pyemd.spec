#
# spec file for package python-pyemd
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


Name:           python-pyemd
Version:        1.0.0
Release:        0
Summary:        Python implementation of the Earth Mover's Distance
License:        MIT
URL:            https://github.com/wmayner/pyemd
Source:         https://files.pythonhosted.org/packages/source/p/pyemd/pyemd-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
# produces wrong results with numpy 2.1+: gh#wmayner/pyemd#68
BuildRequires:  %{python_module numpy-devel >= 1.9.0 with %python-numpy-devel < 2.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       (python-numpy >= 1.9.0 with python-numpy < 2.1)
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
PyEMD is a Python wrapper for Ofir Pele and Michael Werman's implementation
of the Earth Mover's Distance that allows it to be used with NumPy.

%prep
%autosetup -p1 -n pyemd-%{version}
sed -i '1{/env python/d}' src/pyemd/emd.pyx src/pyemd/__init__.py
echo "global-exclude *.cpp *.hpp" >> MANIFEST.in

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
pushd test
%pytest_arch
popd

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/pyemd
%{python_sitearch}/pyemd-%{version}.dist-info

%changelog
