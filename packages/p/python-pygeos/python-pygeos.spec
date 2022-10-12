#
# spec file for package python-pygeos
#
# Copyright (c) 2022 SUSE LLC
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
%define skip_python2 1
Name:           python-pygeos
Version:        0.13
Release:        0
Summary:        GEOS wrapped in numpy ufuncs
License:        BSD-3-Clause
URL:            https://github.com/pygeos/pygeos
Source:         https://files.pythonhosted.org/packages/source/p/pygeos/pygeos-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  libgeos-devel
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.13
# SECTION test requirements
BuildRequires:  %{python_module numpy >= 1.13}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
PyGEOS is a C/Python library with vectorized geometry functions.
The geometry operations are done in the open-source geometry library GEOS.
PyGEOS wraps these operations in NumPy ufuncs providing a performance
improvement when operating on arrays of geometries.

%prep
%setup -q -n pygeos-%{version}
mv pygeos/tests/ .

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand rm %{buildroot}%{$python_sitearch}/pygeos/_{geometry,geos}.c
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
mv pygeos .pygeos
%pytest_arch -rs -k 'not test_float_arg_array'
mv .pygeos pygeos

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/pygeos*/

%changelog
