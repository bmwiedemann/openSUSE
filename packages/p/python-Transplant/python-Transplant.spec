#
# spec file for package python-Transplant
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
%define         skip_python36 1
Name:           python-Transplant
Version:        0.8.11
Release:        0
Summary:        Python module for calling out to Matlab
License:        BSD-3-Clause
URL:            https://github.com/bastibe/transplant
Source:         https://files.pythonhosted.org/packages/source/T/Transplant/Transplant-%{version}.tar.gz
Source99:       https://raw.githubusercontent.com/bastibe/transplant/master/LICENSE
BuildRequires:  %{python_module devel >= 3.4}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-msgpack-python
Requires:       python-numpy
Requires:       python-pyzmq
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module msgpack-python}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pyzmq}
BuildRequires:  %{python_module scipy}
# /SECTION
%python_subpackages

%description
Transplant is a way of calling Matlab from Python.

Python lists are converted to cell arrays in Matlab, dicts are
converted to Maps, and numpy ND-Arrays are converted to native
Matlab matrices.

All Matlab functions and objects can be accessed from Python.

%prep
%setup -q -n Transplant-%{version}
cp %{SOURCE99} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests sadly need matlab install
#%%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
