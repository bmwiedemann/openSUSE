#
# spec file for package python-PeachPy
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
%bcond_without python2
Name:           python-PeachPy
Version:        0.2.0~pre.1583266105.f189ad2
Release:        0
Summary:        Portable Efficient Assembly Codegen in Higher-level Python
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/Maratyszcza/PeachPy
Source0:        PeachPy-%{version}.tar.xz
Patch1:         automated-convertion-form-2to3.patch
BuildRequires:  %{python_module opcodes >= 0.3.13}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
ExclusiveArch:  x86_64
%ifpython2
Requires:       python-enum34
%endif
%if %{with python2}
BuildRequires:  python-enum34
%endif
%python_subpackages

%description
Portable Efficient Assembly Code-generator in Higher-level Python (PEACH-Py)
PEACH-Py is a Python framework for writing high-performance assembly kernels.
PEACH-Py is developed to simplify writing optimized assembly kernels while
preserving all optimization opportunities of traditional assembly. Some
PEACH-Py features:
  - Automatic register allocation
  - Stack frame management, including re-aligning of stack frame as needed
  - Generating versions of a function for different calling conventions from
    the same source (e.g. functions for Microsoft x64 ABI and System V x86-64
    ABI can be generated from the same source)
  - Allows to define constants in the place where they are used (just like in
    high-level languages)
  - Tracking of instruction extensions used in the function.
  - Multiplexing of multiple instruction streams (helpful for software
    pipelining)

%prep
%setup -q -n PeachPy-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# this test is even not ported to python3 and has other issues
rm test/arm/test_arm.py
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.rst
%{python_sitelib}/*

%changelog
