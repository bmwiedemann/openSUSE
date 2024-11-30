#
# spec file for package python-awkward
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
BuildArch:      noarch
%else
# tests fail with python 3.13
%global skip_python313 1
%bcond_without test
# Test suite fails on numerous tests when trying to convert 64-bit types
ExcludeArch:    %{ix86} %{arm32}
%define psuffix -%{flavor}
%if "%{flavor}" == "test-numba"
%bcond_without numba
%else
%bcond_with numba
%endif
%endif

%define awkward_cpp_version 41
%{?sle15_python_module_pythons}
Name:           python-awkward%{psuffix}
Version:        2.7.1
Release:        0
Summary:        Manipulate arrays of complex data structures as easily as Numpy
License:        BSD-3-Clause
URL:            https://github.com/scikit-hep/awkward
# SourceRepository: https://github.com/scikit-hep/awkward
Source0:        https://files.pythonhosted.org/packages/source/a/awkward/awkward-%{version}.tar.gz
Source1:        python-awkward.rpmlintrc
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatch-fancy-pypi-readme}
BuildRequires:  %{python_module hatchling >= 1.10.0}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-awkward-cpp >= %{awkward_cpp_version}
Requires:       python-fsspec >= 2022.11.0
Requires:       python-numpy >= 1.18.0
Requires:       python-packaging
Requires:       (python-importlib-metadata if python-base < 3.12)
Requires:       (python-importlib-resources if python-base < 3.9)
Requires:       (python-typing-extensions >= 4.1.0 if python-base < 3.11)
Recommends:     python-cupy
Recommends:     python-numba
Recommends:     python-pandas
%if %{with test}
BuildRequires:  %{python_module awkward = %{version}}
%if %{with numba}
# numba 0.60 requires numpy < 2.1
BuildRequires:  %{python_module numba >= 0.50 if %python-base < 3.11}
%endif
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module numexpr >= 2.7}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pyarrow}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module uproot >= 5}
%endif

%python_subpackages

%description
Awkward Array is a library for nested, variable-sized data, including
arbitrary-length lists, records, mixed types, and missing data, using
NumPy-like idioms.

Arrays are dynamically typed, but operations on them are compiled and fast.
Their behavior coincides with NumPy when array dimensions are regular and
generalizes when they're not.

%prep
%setup -q -n awkward-%{version}

%build
%if !%{with test}
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%{python_expand # remove devel files
rm -r %{buildroot}%{$python_sitelib}/awkward/_connect/rdataframe/include
%fdupes %{buildroot}%{$python_sitelib}
}
%endif

%if %{with test}
%check
export PYTEST_DEBUG_TEMPROOT=$(mktemp -d -p ./)
# need to package cupy
rm -rvf ./tests-cuda-kernels
# jax, jaxlib missing
%pytest -n auto --ignore tests-cuda/ -k "not test_2603_custom_behaviors_with_jax"
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/awkward/
%{python_sitelib}/awkward-%{version}.dist-info/
%endif

%changelog
