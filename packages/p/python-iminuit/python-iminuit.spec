#
# spec file for package python-iminuit
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
%define psuffix %{nil}
%bcond_with test
%else
%bcond_without test
%define psuffix -%{flavor}
%if "%{flavor}" == "test-numba"
%bcond_without numba
%else
%bcond_with numba
%endif
%endif

%{?sle15_python_module_pythons}
Name:           python-iminuit%{psuffix}
Version:        2.30.1
Release:        0
Summary:        Python bindings for MINUIT2
License:        MIT
URL:            https://github.com/scikit-hep/iminuit
Source0:        https://files.pythonhosted.org/packages/source/i/iminuit/iminuit-%{version}.tar.gz
%if !%{with test}
BuildRequires:  %{python_module devel >= 3.9}
BuildRequires:  %{python_module numpy-devel >= 1.21}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pybind11 >= 2.9.0}
BuildRequires:  %{python_module pybind11-devel}
BuildRequires:  %{python_module scikit-build-core-pyproject >= 0.3.0}
BuildRequires:  cmake >= 3.13
BuildRequires:  fdupes
BuildRequires:  gcc-c++
%endif
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.21
Recommends:     python-matplotlib
Recommends:     python-scipy
%if %{with test}
BuildRequires:  %{python_module iminuit = %{version}}
%if %{with numba}
# numba 0.60 requires numpy < 2.1. This resolves to numpy1,
# if no other **Build**Requires on a conflicting numpy interferes.
BuildRequires:  %{python_module numba}
%endif
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module ipywidgets}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module tabulate}
%endif
# /SECTION
%python_subpackages

%description
iminuit is a Python interface to the MINUIT2 C++ package.

It can be used as a general function minimization method,
but is most commonly used for likelihood fits of models to data,
and to get model parameter error estimates from likelihood profile analysis.

%prep
%setup -q -n iminuit-%{version}
# We use external pybind11, just to be sure remove bundled pybind11 entirely
rm -fr extern/pybind11

%build
%if !%{with test}
export CXXFLAGS="%{optflags}"
export CMAKE_ARGS="-DIMINUIT_EXTERNAL_PYBIND11=ON -DCMAKE_VERBOSE_MAKEFILE=ON"
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%endif

%if %{with test}
%check
%pytest_arch -v
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/iminuit/
%{python_sitearch}/iminuit-%{version}.dist-info/
%endif

%changelog
