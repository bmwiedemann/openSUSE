#
# spec file for package python-sgp4
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
%define skip_python2 1
Name:           python-sgp4
Version:        2.13
Release:        0
Summary:        Track earth satellite TLE orbits using up-to-date 2010 version of SGP4
License:        MIT
URL:            https://github.com/brandon-rhodes/python-sgp4
Source:         https://files.pythonhosted.org/packages/source/s/sgp4/sgp4-%{version}.tar.gz
Source99:       https://github.com/brandon-rhodes/python-sgp4/raw/master/LICENSE
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
%python_subpackages

%description
This Python package computes the position and velocity of an earth-orbiting 
satellite, given the satellite’s TLE orbital elements from a source like 
Celestrak. It implements the most recent version of SGP4, and is regularly run 
against the SGP4 test suite to make sure that its satellite position predictions 
agree to within 0.1 mm with the predictions of the standard distribution of the 
algorithm. This error is far less than the 1–3 km/day by which satellites 
themselves deviate from the ideal orbits described in TLE files.

This package compiles the verbatim source code from the official C++ version
of SGP4. You can call the routine directly, or through an array API that loops 
over arrays of satellites and arrays of times with machine code instead of Python.

%prep
%setup -q -n sgp4-%{version}
cp %{SOURCE99} .
# ease precision tolerances https://github.com/brandon-rhodes/python-sgp4/issues/69
sed -i 's/GRAVITY_DIGITS = (/GRAVITY_DIGITS = 10\nGRAVITY_DIGITS_UPSTREAM =(/' sgp4/tests.py
sed -i 's/error = 2e-7/error = 2e-5/' sgp4/tests.py

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# Upstreams custom tests.py does not exit with error code on import failures.
# Use pytest instead.
cd .. # SLE12 workaround
%pytest_arch --pyargs sgp4.tests
# Only the doctests acually import the compiled extension and fail if it is not present
%pytest_arch --pyargs sgp4 --doctest-modules

%files %{python_files}
%license LICENSE
%{python_sitearch}/sgp4
%{python_sitearch}/sgp4-%{version}-py*.egg-info

%changelog
