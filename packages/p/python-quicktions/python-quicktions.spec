#
# spec file for package python-quicktions
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


Name:           python-quicktions
Version:        1.18
Release:        0
Summary:        Fast fractions data type for rational numbers
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/scoder/quicktions
Source:         https://files.pythonhosted.org/packages/source/q/quicktions/quicktions-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 3}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Python's Fraction data type is an excellent way to do exact money
calculations and largely beats Decimal in terms of simplicity,
accuracy and safety.  Clearly not in terms of speed, though, given
the cdecimal accelerator in Py3.3+.

Quicktions is an adaptation of the original fractions module
(as included in CPython 3.5) that is compiled and optimised with
Cython into a fast, native extension module.

Compared to the standard library fractions module in Py2.7 and
Py3.4, quicktions is currently about 10x faster, and still about
6x faster than the current version in Python 3.5.  It's also about
15x faster than the (Python implemented) decimal module in Py2.7.

%prep
%setup -q -n quicktions-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export PYTHONDONTWRITEBYTECODE=1
%pytest_arch --capture=no

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitearch}/quicktions.cpython-*so
%{python_sitearch}/quicktions-%{version}.dist-info

%changelog
