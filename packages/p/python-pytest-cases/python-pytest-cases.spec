#
# spec file for package python-pytest-cases
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
Name:           python-pytest-cases
Version:        3.8.6
Release:        0
Summary:        Separate test code from test cases in pytest
License:        BSD-3-Clause
URL:            https://github.com/smarie/python-pytest-cases
Source:         https://files.pythonhosted.org/packages/source/p/pytest-cases/pytest_cases-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 39.2}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module decopatch}
BuildRequires:  %{python_module makefun >= 1.15.1}
BuildRequires:  %{python_module packaging}
# SECTION test requirements
# BuildRequires:  python_module pytest
# BuildRequires:  python_module pytest-steps
# BuildRequires:  python_module pytest-harvest
# BuildRequires:  python_module pytest-asyncio}
# /SECTION
BuildRequires:  fdupes
Requires:       python-decopatch
Requires:       python-makefun >= 1.15.1
Requires:       python-packaging
BuildArch:      noarch
%python_subpackages

%description
Separate test code from test cases in pytest.

%prep
%autosetup -p1 -n pytest_cases-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/pytest_cases
%{python_sitelib}/pytest_cases-%{version}.dist-info

%changelog
