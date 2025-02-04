#
# spec file for package python-dirty-equals
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


%{?sle15_python_module_pythons}
Name:           python-dirty-equals
Version:        0.9.0
Release:        0
Summary:        Doing dirty (but useful) things with equals
License:        MIT
URL:            https://dirty-equals.helpmanual.io
Source:         https://github.com/samuelcolvin/dirty-equals/archive/refs/tags/v%{version}.tar.gz#/dirty-equals-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pydantic >= 2.4}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz >= 2021.3}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytz >= 2021.3
BuildArch:      noarch
%python_subpackages

%description
Doing dirty (but extremely useful) things with equals.

%prep
%autosetup -p1 -n dirty-equals-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Doc tests need new pytest plugin, pytest-examples. Too much work for too low importance.
%pytest --ignore "tests/test_docs.py"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/dirty_equals
%{python_sitelib}/dirty_equals-%{version}*-info

%changelog
