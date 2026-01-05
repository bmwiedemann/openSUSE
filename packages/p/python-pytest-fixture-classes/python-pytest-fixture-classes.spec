#
# spec file for package python-pytest-fixture-classes
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


Name:           python-pytest-fixture-classes
Version:        1.0.4
Release:        0
Summary:        Fixtures as classes that work well with dependency injection and more
License:        MIT
URL:            https://github.com/zmievsa/pytest-fixture-classes
Source:         https://files.pythonhosted.org/packages/source/p/pytest-fixture-classes/pytest_fixture_classes-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module hatchling >= 1.19.0}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module typing-extensions >= 4.4.0}
BuildRequires:  %{python_module pytest >= 7.1.3}
BuildRequires:  %{python_module pytest-asyncio >= 0.21.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-typing-extensions >= 4.4.0
BuildArch:      noarch
%python_subpackages

%description
Typed factory fixtures that work well with dependency injection, autocompletetion, type checkers, and language servers.

No mypy plugins required!

%prep
%autosetup -p1 -n pytest_fixture_classes-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%{python_sitelib}/pytest_fixture_classes
%{python_sitelib}/pytest_fixture_classes-%{version}.dist-info

%changelog
