#
# spec file for package python-pytest_param_files
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-pytest-param-files
Version:        0.6.0
Release:        0
Summary:        Create pytest parametrize decorators from external files
License:        MIT
URL:            https://github.com/chrisjsewell/pytest-param-files
Source:         https://files.pythonhosted.org/packages/source/p/pytest-param-files/pytest_param_files-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module flit-core >= 3.2}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module ruamel.yaml >= 0.15}
# /SECTION
BuildRequires:  fdupes
Requires:       python-pytest
Requires:       python-ruamel.yaml >= 0.15
Suggests:       python-pytest-cov
BuildArch:      noarch
%python_subpackages

%description
A small package to generate parametrized pytest from external files.

%prep
%autosetup -p1 -n pytest_param_files-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pytest_param_files
%{python_sitelib}/pytest_param_files-%{version}.dist-info

%changelog
