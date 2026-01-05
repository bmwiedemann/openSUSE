#
# spec file for package python-pytest-lazy-fixtures
#
# Copyright (c) 2026 SUSE LLC
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


Name:           python-pytest-lazy-fixtures
Version:        1.4.0
Release:        0
Summary:        Allows you to use fixtures in @pytest.mark.parametrize
License:        MIT
URL:            https://github.com/dev-petrov/pytest-lazy-fixtures
Source:         https://files.pythonhosted.org/packages/source/p/pytest-lazy-fixtures/pytest_lazy_fixtures-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 7}
BuildRequires:  %{python_module pytest-deadfixtures}
BuildRequires:  %{python_module pytest-fixture-classes}
# /SECTION
BuildRequires:  fdupes
Requires:       python-pytest >= 7
BuildArch:      noarch
%python_subpackages

%description
Use your fixtures in `@pytest.mark.parametrize`.

This project was inspired by pytest-lazy-fixture

Improvements that have been made in this project:

1. You can use fixtures in any data structures
2. You can access the attributes of fixtures
3. You can use functions in fixtures
4. It is compatible with pytest-deadfixtures

%prep
%autosetup -p1 -n pytest_lazy_fixtures-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/pytest_lazy_fixtures
%{python_sitelib}/pytest_lazy_fixtures-%{version}.dist-info

%changelog
