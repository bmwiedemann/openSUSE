#
# spec file for package python-pytest-astropy-header
#
# Copyright (c) 2019 SUSE LLC
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pytest-astropy-header
Version:        0.1
Release:        0
Summary:        Pytest plugin to add diagnostic information to the header of the test output
License:        BSD-3-Clause
Group:          Productivity/Scientific/Astronomy
URL:            https://github.com/astropy/pytest-astropy-header
Source:         https://files.pythonhosted.org/packages/source/p/pytest-astropy-header/pytest-astropy-header-%{version}.tar.gz
Patch0:         pytest-astropy-header-pr2.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pytest >= 2.8}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 2.8
# SECTION test requirements
BuildRequires:  %{python_module astropy >= 2.0}
BuildRequires:  %{python_module codecov}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module pytest-cov}
# /SECTION
%python_subpackages

%description
This plugin package provides a way to include information about the system, 
Python installation, and select dependencies in the header of the output when 
running pytest. It can be used with packages that are not affiliated with the 
Astropy project, but is optimized for use with astropy-related projects.

%prep
%setup -q -n pytest-astropy-header-%{version}
%patch0 -p1

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE.rst
%{python_sitelib}/pytest_astropy_header
%{python_sitelib}/pytest_astropy_header-%{version}-py*.egg-info

%changelog
