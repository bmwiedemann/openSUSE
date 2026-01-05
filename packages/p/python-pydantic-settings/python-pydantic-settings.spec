#
# spec file for package python-pydantic-settings
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-pydantic-settings%{psuffix}
Version:        2.12.0
Release:        0
Summary:        Settings management using Pydantic
License:        MIT
URL:            https://github.com/pydantic/pydantic-settings
Source:         https://files.pythonhosted.org/packages/source/p/pydantic-settings/pydantic_settings-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module azure-identity}
BuildRequires:  %{python_module google-auth}
BuildRequires:  %{python_module pydantic-settings = %{version}}
BuildRequires:  %{python_module pytest-examples}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
%endif
# /SECTION
BuildRequires:  fdupes
Requires:       python-pydantic >= 2.7.0
Requires:       python-python-dotenv >= 0.21.0
Requires:       python-typing-inspection >= 0.4.0
Suggests:       python-PyYAML >= 6.0.1
Suggests:       python-tomli >= 2.0.1
Suggests:       python-google-cloud-secret-manager >= 2.23.1
Suggests:       python-azure-keyvault-secrets >= 4.8
Suggests:       python-azure-identity
BuildArch:      noarch
%python_subpackages

%description
Settings management using Pydantic, this is the new official home of Pydantic's `BaseSettings`.

%prep
%autosetup -p1 -n pydantic_settings-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# This test requires azure
skiptest="test_docs_examples[docs/index.md:1847-1890]"
%pytest -k "not ($skiptest)"
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/pydantic_settings
%{python_sitelib}/pydantic_settings-%{version}.dist-info
%endif

%changelog
