#
# spec file for package python-pytest-shell-utilities
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
Name:           python-pytest-shell-utilities%{psuffix}
Version:        1.9.7
Release:        0
Summary:        Pytest plugin to simplify running shell commands against the system
License:        Apache-2.0
URL:            https://github.com/saltstack/pytest-shell-utilities
Source:         https://files.pythonhosted.org/packages/source/p/pytest-shell-utilities/pytest_shell_utilities-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 50.3.2}
BuildRequires:  %{python_module setuptools_scm >= 3.4}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module attrs >= 22.1.0}
BuildRequires:  %{python_module psutil >= 6.0.0}
BuildRequires:  %{python_module pytest >= 7.3.0}
BuildRequires:  %{python_module pytest-helpers-namespace}
BuildRequires:  %{python_module pytest-shell-utilities = %{version}}
BuildRequires:  %{python_module pytest-skip-markers}
BuildRequires:  %{python_module pytest-subtests}
BuildRequires:  %{python_module typing-extensions}
%endif
# /SECTION
BuildRequires:  fdupes
Requires:       python-attrs >= 22.1.0
Requires:       python-psutil >= 6.0.0
Requires:       python-pytest >= 7.3.0
Requires:       python-pytest-helpers-namespace
Requires:       python-pytest-skip-markers
Requires:       python-typing-extensions
BuildArch:      noarch
%python_subpackages

%description
Pytest plugin to simplify running shell commands against the system

%prep
%setup -q -n pytest_shell_utilities-%{version}

%build
%pyproject_wheel

%if !%{with test}
%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/pytestshellutils
%{python_sitelib}/pytest_shell_utilities-%{version}*-info

%else

%check
%pytest
%endif

%changelog
