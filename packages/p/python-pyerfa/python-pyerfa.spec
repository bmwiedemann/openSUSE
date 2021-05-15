#
# spec file for package python-pyerfa
#
# Copyright (c) 2021 SUSE LLC
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


%if 0%{suse_version} <= 1500
# use the bundled ERFA in Leap <=15.X, because the system provided one is too old
%bcond_with systemlibs
%else
%bcond_without systemlibs
%endif
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define erfaversion 1.7.3
%define skip_python2 1
%define skip_python36 1
Name:           python-pyerfa
Version:        1.7.3
Release:        0
Summary:        Python bindings for ERFA
License:        BSD-3-Clause
URL:            https://github.com/liberfa/pyerfa
Source:         https://files.pythonhosted.org/packages/source/p/pyerfa/pyerfa-%{version}.tar.gz
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
%if %{with systemlibs}
BuildRequires:  pkgconfig(erfa) >= %{erfaversion}
%endif
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
%if %{with systemlibs}
rm -rf liberfa/
%endif

%build
%if %{with systemlibs}
export PYERFA_USE_SYSTEM_LIBERFA=1
%endif
%python_build

%install
%if %{with systemlibs}
export PYERFA_USE_SYSTEM_LIBERFA=1
%endif
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch --pyargs erfa

%files %{python_files}
%license LICENSE.rst licenses/ERFA.rst
%{python_sitearch}/erfa
%{python_sitearch}/pyerfa-%{version}-py*.egg-info

%changelog
