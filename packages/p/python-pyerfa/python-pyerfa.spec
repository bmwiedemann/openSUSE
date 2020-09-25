#
# spec file for package python-pyerfa
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-pyerfa
Version:        1.7.0
Release:        0
Summary:        Python bindings for ERFA
License:        BSD-3-Clause
URL:            https://github.com/liberfa/pyerfa
Source:         https://files.pythonhosted.org/packages/source/p/pyerfa/pyerfa-%{version}.tar.gz
Patch0:         https://github.com/liberfa/pyerfa/pull/39.patch#/pyerfa-pr39-usesystemerfa.patch
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel >= 1.16}
BuildRequires:  %{python_module pytest-doctestplus >= 0.7}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(erfa) >= %{version}
Requires:       python-numpy >= 1.16
%python_subpackages

%description
A Python wrapper for the ERFA library (Essential Routines for
Fundamental Astronomy), a C library containing key algorithms for astronomy,
which is based on the SOFA library published by the International Astronomical
Union (IAU).  All C routines are wrapped as Numpy universal functions,
so that they can be called with scalar or array inputs.

The project is a split of astropy._erfa module, developed in the
context of Astropy project, into a standalone package.

%prep
%setup -q -n pyerfa-%{version}
sed '11,+14 c remove patching nonexistent .travis.yml' ${P:0}
%patch0 -p1
rm -rf liberfa/

%build
export PYERFA_USE_SYSTEM_LIBERFA=1
%python_build

%install
export PYERFA_USE_SYSTEM_LIBERFA=1
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# test_version https://github.com/liberfa/pyerfa/issues/52
%pytest_arch --pyargs erfa -k "not test_version"

%files %{python_files}
%license LICENSE.rst licenses/ERFA.rst
%{python_sitearch}/erfa
%{python_sitearch}/pyerfa-%{version}-py*.egg-info

%changelog
