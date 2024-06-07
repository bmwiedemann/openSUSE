#
# spec file for package python-awkward-cpp
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


%{?sle15_python_module_pythons}
Name:           python-awkward-cpp
Version:        34
Release:        0
Summary:        CPU kernels and compiled extensions for Awkward Array
License:        BSD-3-Clause
URL:            https://awkward-array.org/
# SourceRepository:  https://github.com/scikit-hep/awkward/awkward-cpp
Source0:        https://files.pythonhosted.org/packages/source/a/awkward-cpp/awkward-cpp-%{version}.tar.gz
Source99:       awkward-cpp.rpmlintrc
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pybind11-devel}
BuildRequires:  %{python_module scikit-build-core-pyproject >= 0.2}
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.17.0
Provides:       python-awkward_cpp = %{version}-%{release}
# SECTION test requirements
BuildRequires:  %{python_module numpy >= 1.17.0}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Awkward Array is a library for nested, variable-sized data, including
arbitrary-length lists, records, mixed types, and missing data, using
NumPy-like idioms.

Arrays are dynamically typed, but operations on them are compiled and fast.
Their behavior coincides with NumPy when array dimensions are regular and
generalizes when they're not.

awkward-cpp provides precompiled routines for the awkward package.
It is not useful on its own, only as a dependency for awkward.

%package -n awkward-devel
Summary:        Header files for using awkward in C/C++ code

%description -n awkward-devel
Awkward Array is a library for nested, variable-sized data, including
arbitrary-length lists, records, mixed types, and missing data, using
NumPy-like idioms.

This package provides the header files needed to compile C/C++ codes with
awkward.

%prep
%setup -q -n awkward-cpp-%{version}

%build
%pyproject_wheel
%cmake -S ../header-only
%cmake_build

%install
%pyproject_install
%cmake_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/awkward_cpp
%{python_sitearch}/awkward_cpp-%{version}.dist-info

%files -n awkward-devel
%doc README.md
%license LICENSE
%{_includedir}/builder-options
%{_includedir}/growable-buffer
%{_includedir}/layout-builder
%{_libdir}/cmake/awkward-headers

%changelog
