#
# spec file for package python-pydantic-settings
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


%{?sle15_python_module_pythons}
Name:           python-pydantic-settings
Version:        2.3.4
Release:        0
Summary:        Settings management using Pydantic
License:        MIT
URL:            https://github.com/pydantic/pydantic-settings
Source:         https://files.pythonhosted.org/packages/source/p/pydantic-settings/pydantic_settings-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Clear the environment before two test cases
Patch0:         clear-environment.patch
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pydantic >= 2.3.0}
BuildRequires:  %{python_module pytest-examples}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dotenv >= 0.21.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-pydantic >= 2.3.0
Requires:       python-python-dotenv >= 0.21.0
Suggests:       python-pyyaml >= 6.0.1
Suggests:       python-tomli >= 2.0.1
BuildArch:      noarch
%python_subpackages

%description
Settings management using Pydantic, this is the new official home of Pydantic's `BaseSettings`.

%prep
%autosetup -p1 -n pydantic_settings-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/pydantic_settings
%{python_sitelib}/pydantic_settings-%{version}.dist-info

%changelog
