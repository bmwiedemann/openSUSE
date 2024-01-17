#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define modname pytest-astropy-header

Name:           python-%{modname}%{psuffix}
Version:        0.2.2
Release:        0
Summary:        Pytest plugin to add diagnostic information to the header of the test output
License:        BSD-3-Clause
Group:          Productivity/Scientific/Astronomy
URL:            https://github.com/astropy/pytest-astropy-header
Source:         https://files.pythonhosted.org/packages/source/p/%{modname}/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module setuptools >= 30.3.0}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 4.6
%if %{with test}
BuildRequires:  %{python_module astropy >= 4.0}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest >= 4.6}
%endif
Provides:       python-pytest_astropy_header = %{version}-%{release}
BuildArch:      noarch
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
%{python_sitelib}/pytest_astropy_header-%{version}*-info
%endif

%changelog
