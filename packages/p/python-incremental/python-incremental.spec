#
# spec file for package python-incremental
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
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-incremental%{psuffix}
Version:        24.7.2
Release:        0
Summary:        Library that versions your Python projects
License:        MIT
URL:            https://github.com/twisted/incremental
Source:         https://files.pythonhosted.org/packages/source/i/incremental/incremental-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-Twisted >= 16.4.0
Suggests:       python-click >= 6.0
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Twisted >= 16.4.0}
BuildRequires:  %{python_module build}
BuildRequires:  %{python_module click >= 6.0}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
Incremental is a small library that versions your Python projects.

%prep
%setup -q -n incremental-%{version}

%build
%pyproject_wheel

%install
%if %{without test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# See: https://github.com/twisted/incremental/issues/110
%pytest -k 'not test_examples.py'
%endif

%if %{without test}
%files %{python_files}
%license LICENSE
%doc NEWS.rst README.rst
%{python_sitelib}/incremental
%{python_sitelib}/incremental-%{version}*-info
%endif

%changelog
