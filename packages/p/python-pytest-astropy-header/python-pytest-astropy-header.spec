#
# spec file for package python-pytest-astropy-header
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


%define modname pytest-astropy-header
%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
# current astropy in TW requires python >= 3.7
%define skip_python36 1
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-%{modname}%{psuffix}
Version:        0.1.2
Release:        0
Summary:        Pytest plugin to add diagnostic information to the header of the test output
License:        BSD-3-Clause
Group:          Productivity/Scientific/Astronomy
URL:            https://github.com/astropy/pytest-astropy-header
Source:         https://files.pythonhosted.org/packages/source/p/%{modname}/%{modname}-%{version}.tar.gz
Patch0:         https://github.com/astropy/pytest-astropy-header/pull/16.patch#/pytest-astropy-header-pr16-no-helper-version.patch
Patch1:         https://github.com/astropy/pytest-astropy-header/pull/29.patch#/pytest-astropy-header-pr29-nohelpers.patch
BuildRequires:  %{python_module setuptools >= 30.3.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 2.8
%if %{with test}
# Patch0 and Patch1: helpers got removed in astropy 4
BuildRequires:  %{python_module astropy >= 4.0}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest >= 2.8}
%endif
%python_subpackages

%description
This plugin package provides a way to include information about the system,
Python installation, and select dependencies in the header of the output when
running pytest. It can be used with packages that are not affiliated with the
Astropy project, but is optimized for use with astropy-related projects.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# multibuild: nothing has been installed, test the source directory
export PYTHONPATH=$(pwd)
%pytest
%endif

%if !%{with test}
%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE.rst
%{python_sitelib}/pytest_astropy_header
%{python_sitelib}/pytest_astropy_header-%{version}-py*.egg-info
%endif

%changelog
