#
# spec file for package python-pytest-mypy-testing
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
Name:           python-pytest-mypy-testing
Version:        0.1.3
Release:        0
Summary:        Pytest plugin to check mypy output
License:        Apache-2.0 OR MIT
URL:            https://github.com/davidfritzsche/pytest-mypy-testing
Source:         https://files.pythonhosted.org/packages/source/p/pytest-mypy-testing/pytest-mypy-testing-%{version}.tar.gz
BuildRequires:  %{python_module flit-core >= 2}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module mypy >= 1.0}
BuildRequires:  %{python_module pytest >= 7}
# /SECTION
BuildRequires:  fdupes
Requires:       python-mypy >= 1.0
Requires:       python-pytest >= 7
BuildArch:      noarch
%python_subpackages

%description
pytest-mypy-testing — Plugin to test mypy output with pytest

`pytest-mypy-testing` provides a pytest plugin to test that
mypy produces a given output. As mypy can be told to display the
type of an expression this allows us to check mypys type interference.

%prep
%autosetup -p1 -n pytest-mypy-testing-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSES/Apache-2.0.txt LICENSES/CC0-1.0.txt LICENSES/MIT.txt
%{python_sitelib}/pytest_mypy_testing
%{python_sitelib}/pytest_mypy_testing-%{version}.dist-info

%changelog
