#
# spec file for package python-fastnumbers
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
Name:           python-fastnumbers
Version:        5.1.0
Release:        0
Summary:        Drop-in replacement for Python's int and float
License:        MIT
URL:            https://github.com/SethMMorton/fastnumbers
Source:         https://files.pythonhosted.org/packages/source/f/fastnumbers/fastnumbers-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix-compiler-errors.patch mcepl@suse.com
# Code from gh#SethMMorton/fastnumbers@5522116cd03a and gh#SethMMorton/fastnumbers@8d2104e5cd93
Patch0:         fix-compiler-errors.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module typing-extensions}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if 0%{?suse_version} <= 1500
BuildRequires:  gcc13
BuildRequires:  gcc13-c++
%else
BuildRequires:  gcc
BuildRequires:  gcc-c++
%endif
# SECTION test requirements
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest >= 5}
BuildRequires:  python3-testsuite
# /SECTION
%python_subpackages

%description
fastnumbers is a Python module with three objectives:

1. To provide drop-in replacements for the Python built-in `int` and
   `float` that, on average, are around 2x faster. These functions
   should behave identically to the Python built-ins except for a few
   specific corner-cases as mentioned in the API documentation.
2. To provide a set of convenience functions that wrap the above int
   and float replacements and provide error handling.
3. To provide a set of functions that can be used to identify whether
   an input could be converted to int or float.

%prep
%autosetup -p1 -n fastnumbers-%{version}

%build
%if 0%{?suse_version} <= 1500
export CC=gcc-13
export CXX=g++-13
%endif
export CFLAGS="%{optflags} -Wno-error=return-type"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/fastnumbers
%{python_sitearch}/fastnumbers-%{version}.dist-info

%changelog
