#
# spec file
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
# Python2 support dropped since version 1.4.0
%define skip_python2 1
%define skip_python36 1
%define modname iminuit
Name:           python-%{modname}
Version:        2.18.0
Release:        0
Summary:        Python bindings for MINUIT2
License:        MIT
URL:            https://github.com/scikit-hep/iminuit
Source0:        https://files.pythonhosted.org/packages/source/i/iminuit/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module numpy >= 1.11.3}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module pybind11 >= 2.9.0}
BuildRequires:  %{python_module pybind11-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  cmake >= 3.13
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.11.3
Recommends:     python-matplotlib
Recommends:     python-scipy
# SECTION test requirements
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numba}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module tabulate}
# Fix unresolved status for Leap 15.x on account of multiple choices for python3-importlib-metadata (python3-importlib-metadata and python3-importlib_metadata)
BuildRequires:  %{python_module importlib-metadata}
# /SECTION
%python_subpackages

%description
iminuit is a Python interface to the MINUIT2 C++ package.

It can be used as a general function minimization method,
but is most commonly used for likelihood fits of models to data,
and to get model parameter error estimates from likelihood profile analysis.

%prep
%setup -q -n %{modname}-%{version}
# We use external pybind11, just to be sure remove bundled pybind11 entirely
rm -fr extern/pybind11

%build
export CFLAGS="%{optflags}"
export CMAKE_ARGS="-DIMINUIT_EXTERNAL_PYBIND11=ON"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# A tolerance issue on 32-bit
%ifarch %ix86
%pytest_arch -k 'not test_matrix'
%else
%pytest_arch
%endif

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/%{modname}/
%{python_sitearch}/%{modname}-%{version}-py%{python_version}.egg-info/

%changelog
